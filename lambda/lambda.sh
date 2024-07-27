#!/bin/bash
zip lambda.zip lambda_function.py
aws configure

# Variables
FUNCTION_NAME="LambdaFunction"
ROLE_ARN="arn:aws:iam::170792677673:role/lambda"  # Replace with your IAM role ARN
HANDLER="lambda_function.lambda_handler"
RUNTIME="python3.8"
ZIP_FILE="fileb://lambda.zip"
TIMEOUT=15
MEMORY_SIZE=128

# Create the Lambda function
aws lambda create-function \
    --function-name $FUNCTION_NAME \
    --runtime $RUNTIME \
    --role $ROLE_ARN \
    --handler $HANDLER \
    --timeout $TIMEOUT \
    --memory-size $MEMORY_SIZE \
    --zip-file $ZIP_FILE

