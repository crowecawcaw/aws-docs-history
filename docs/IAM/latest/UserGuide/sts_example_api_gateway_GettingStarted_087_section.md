# Create a REST API with Lambda proxy integration

The following code example shows how to:

- Create an IAM role for Lambda execution
- Create and deploy a Lambda function
- Create a REST API
- Configure Lambda proxy integration
- Deploy and test the API
- Clean up resources

Bash

**AWS CLI with Bash script**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[Sample developer tutorials](https://github.com/aws-samples/sample-developer-tutorials/tree/main/tuts/087-apigateway-lambda-integration "https://github.com/aws-samples/sample-developer-tutorials/tree/main/tuts/087-apigateway-lambda-integration")
repository.

```
#!/bin/bash

# Simple API Gateway Lambda Integration Script
# This script creates a REST API with Lambda proxy integration

# Generate random identifiers
FUNCTION_NAME="GetStartedLambdaProxyIntegration-$(openssl rand -hex 4)"
ROLE_NAME="GetStartedLambdaBasicExecutionRole-$(openssl rand -hex 4)"
API_NAME="LambdaProxyAPI-$(openssl rand -hex 4)"

# Get AWS account info
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
REGION=$(aws configure get region || echo "us-east-1")

echo "Creating Lambda function code..."

# Create Lambda function code
cat > lambda_function.py << 'EOF'
import json

def lambda_handler(event, context):
    print(event)

    greeter = 'World'

    try:
        if (event['queryStringParameters']) and (event['queryStringParameters']['greeter']) and (
                event['queryStringParameters']['greeter'] is not None):
            greeter = event['queryStringParameters']['greeter']
    except KeyError:
        print('No greeter')

    try:
        if (event['multiValueHeaders']) and (event['multiValueHeaders']['greeter']) and (
                event['multiValueHeaders']['greeter'] is not None):
            greeter = " and ".join(event['multiValueHeaders']['greeter'])
    except KeyError:
        print('No greeter')

    try:
        if (event['headers']) and (event['headers']['greeter']) and (
                event['headers']['greeter'] is not None):
            greeter = event['headers']['greeter']
    except KeyError:
        print('No greeter')

    if (event['body']) and (event['body'] is not None):
        body = json.loads(event['body'])
        try:
            if (body['greeter']) and (body['greeter'] is not None):
                greeter = body['greeter']
        except KeyError:
            print('No greeter')

    res = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "*/*"
        },
        "body": "Hello, " + greeter + "!"
    }

    return res
EOF

# Create deployment package
zip function.zip lambda_function.py

echo "Creating IAM role..."

# Create IAM trust policy
cat > trust-policy.json << 'EOF'
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

# Create IAM role
aws iam create-role \
    --role-name "$ROLE_NAME" \
    --assume-role-policy-document file://trust-policy.json

# Attach execution policy
aws iam attach-role-policy \
    --role-name "$ROLE_NAME" \
    --policy-arn "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"

# Wait for role propagation
sleep 15

echo "Creating Lambda function..."

# Create Lambda function
aws lambda create-function \
    --function-name "$FUNCTION_NAME" \
    --runtime python3.9 \
    --role "arn:aws:iam::$ACCOUNT_ID:role/$ROLE_NAME" \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://function.zip

echo "Creating API Gateway..."

# Create REST API
aws apigateway create-rest-api \
    --name "$API_NAME" \
    --endpoint-configuration types=REGIONAL

# Get API ID
API_ID=$(aws apigateway get-rest-apis --query "items[?name=='$API_NAME'].id" --output text)

# Get root resource ID
ROOT_RESOURCE_ID=$(aws apigateway get-resources --rest-api-id "$API_ID" --query 'items[?path==`/`].id' --output text)

# Create helloworld resource
aws apigateway create-resource \
    --rest-api-id "$API_ID" \
    --parent-id "$ROOT_RESOURCE_ID" \
    --path-part helloworld

# Get resource ID
RESOURCE_ID=$(aws apigateway get-resources --rest-api-id "$API_ID" --query "items[?pathPart=='helloworld'].id" --output text)

# Create ANY method
aws apigateway put-method \
    --rest-api-id "$API_ID" \
    --resource-id "$RESOURCE_ID" \
    --http-method ANY \
    --authorization-type NONE

# Set up Lambda proxy integration
LAMBDA_URI="arn:aws:apigateway:$REGION:lambda:path/2015-03-31/functions/arn:aws:lambda:$REGION:$ACCOUNT_ID:function:$FUNCTION_NAME/invocations"

aws apigateway put-integration \
    --rest-api-id "$API_ID" \
    --resource-id "$RESOURCE_ID" \
    --http-method ANY \
    --type AWS_PROXY \
    --integration-http-method POST \
    --uri "$LAMBDA_URI"

# Grant API Gateway permission to invoke Lambda
SOURCE_ARN="arn:aws:execute-api:$REGION:$ACCOUNT_ID:$API_ID/*/*"

aws lambda add-permission \
    --function-name "$FUNCTION_NAME" \
    --statement-id "apigateway-invoke-$(openssl rand -hex 4)" \
    --action lambda:InvokeFunction \
    --principal apigateway.amazonaws.com \
    --source-arn "$SOURCE_ARN"

# Deploy API
aws apigateway create-deployment \
    --rest-api-id "$API_ID" \
    --stage-name test

echo "Testing API..."

# Test the API
INVOKE_URL="https://$API_ID.execute-api.$REGION.amazonaws.com/test/helloworld"

echo "API URL: $INVOKE_URL"

# Test with query parameter
echo "Testing with query parameter:"
curl -X GET "$INVOKE_URL?greeter=John"
echo ""

# Test with header
echo "Testing with header:"
curl -X GET "$INVOKE_URL" \
    -H 'content-type: application/json' \
    -H 'greeter: John'
echo ""

# Test with body
echo "Testing with POST body:"
curl -X POST "$INVOKE_URL" \
    -H 'content-type: application/json' \
    -d '{ "greeter": "John" }'
echo ""

echo "Tutorial completed! API is available at: $INVOKE_URL"

# Cleanup
echo "Cleaning up resources..."

# Delete API
aws apigateway delete-rest-api --rest-api-id "$API_ID"

# Delete Lambda function
aws lambda delete-function --function-name "$FUNCTION_NAME"

# Detach policy and delete role
aws iam detach-role-policy \
    --role-name "$ROLE_NAME" \
    --policy-arn "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"

aws iam delete-role --role-name "$ROLE_NAME"

# Clean up local files
rm -f lambda_function.py function.zip trust-policy.json

echo "Cleanup completed!"


```

- For API details, see the following topics in _AWS CLI Command Reference_.
  - [AddPermission](../../../goto/aws-cli/lambda-2015-03-31/AddPermission.md "../../../goto/aws-cli/lambda-2015-03-31/AddPermission.md")
  - [AttachRolePolicy](../../../goto/aws-cli/iam-2010-05-08/AttachRolePolicy.md "../../../goto/aws-cli/iam-2010-05-08/AttachRolePolicy.md")
  - [CreateDeployment](../../../goto/aws-cli/apigateway-2015-07-09/CreateDeployment.md "../../../goto/aws-cli/apigateway-2015-07-09/CreateDeployment.md")
  - [CreateFunction](../../../goto/aws-cli/lambda-2015-03-31/CreateFunction.md "../../../goto/aws-cli/lambda-2015-03-31/CreateFunction.md")
  - [CreateResource](../../../goto/aws-cli/apigateway-2015-07-09/CreateResource.md "../../../goto/aws-cli/apigateway-2015-07-09/CreateResource.md")
  - [CreateRestApi](../../../goto/aws-cli/apigateway-2015-07-09/CreateRestApi.md "../../../goto/aws-cli/apigateway-2015-07-09/CreateRestApi.md")
  - [CreateRole](../../../goto/aws-cli/iam-2010-05-08/CreateRole.md "../../../goto/aws-cli/iam-2010-05-08/CreateRole.md")
  - [DeleteFunction](../../../goto/aws-cli/lambda-2015-03-31/DeleteFunction.md "../../../goto/aws-cli/lambda-2015-03-31/DeleteFunction.md")
  - [DeleteRestApi](../../../goto/aws-cli/apigateway-2015-07-09/DeleteRestApi.md "../../../goto/aws-cli/apigateway-2015-07-09/DeleteRestApi.md")
  - [DeleteRole](../../../goto/aws-cli/iam-2010-05-08/DeleteRole.md "../../../goto/aws-cli/iam-2010-05-08/DeleteRole.md")
  - [DetachRolePolicy](../../../goto/aws-cli/iam-2010-05-08/DetachRolePolicy.md "../../../goto/aws-cli/iam-2010-05-08/DetachRolePolicy.md")
  - [GetCallerIdentity](../../../goto/aws-cli/sts-2011-06-15/GetCallerIdentity.md "../../../goto/aws-cli/sts-2011-06-15/GetCallerIdentity.md")
  - [GetResources](../../../goto/aws-cli/apigateway-2015-07-09/GetResources.md "../../../goto/aws-cli/apigateway-2015-07-09/GetResources.md")
  - [GetRestApis](../../../goto/aws-cli/apigateway-2015-07-09/GetRestApis.md "../../../goto/aws-cli/apigateway-2015-07-09/GetRestApis.md")
  - [PutIntegration](../../../goto/aws-cli/apigateway-2015-07-09/PutIntegration.md "../../../goto/aws-cli/apigateway-2015-07-09/PutIntegration.md")
  - [PutMethod](../../../goto/aws-cli/apigateway-2015-07-09/PutMethod.md "../../../goto/aws-cli/apigateway-2015-07-09/PutMethod.md")

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
