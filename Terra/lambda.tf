terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.57.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}


resource "aws_iam_role" "lambda_execution_role" {
  name = "LambdaExecutionRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        },
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_policy" "lambda_policy" {
  name = "LambdaPolicy"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = [
          "elasticloadbalancing:DescribeLoadBalancers",
          "elasticloadbalancing:DescribeTags",
          "route53:ChangeResourceRecordSets",
          "route53:ListHostedZones",
          "route53:ListHostedZonesByName"
        ],
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_role_policy_attachment" {
  role       = aws_iam_role.lambda_execution_role.name
  policy_arn  = aws_iam_policy.lambda_policy.arn
}

resource "aws_lambda_function" "find_and_create_record_function" {
  function_name = "FindAndCreateRecordFunction"
  role          = aws_iam_role.lambda_execution_role.arn
  handler       = "index.handler"
  runtime       = "python3.9"
  timeout       = 300

  # Lambda fonksiyonunun kodu (zip dosyası)
  filename       = "lambda_function_payload.zip"
  source_code_hash = filebase64sha256("lambda_function_payload.zip")

  environment {
    variables = {
      REGION = "us-east-1"
    }
  }
}

resource "aws_lambda_permission" "lambda_invoke_permission" {
  statement_id  = "AllowExecutionFromEvents"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.find_and_create_record_function.function_name
  principal     = "events.amazonaws.com"
}

resource "null_resource" "custom_resource_trigger" {
  triggers = {
    function_name = aws_lambda_function.find_and_create_record_function.function_name
  }

  provisioner "local-exec" {
    command = "echo 'Triggering Lambda Function'"
  }
}

output "lambda_function_arn" {
  description = "ARN of the Lambda function that creates the DNS record"
  value       = aws_lambda_function.find_and_create_record_function.arn
}
