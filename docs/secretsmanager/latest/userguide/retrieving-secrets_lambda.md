

# Use AWS Secrets Manager secrets in AWS Lambda functions
<a name="retrieving-secrets_lambda"></a>

AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers. Parameter Store, a capability of AWS Systems Manager, provides secure, hierarchical storage for configuration data management and secrets management. You can use the AWS Parameters and Secrets Lambda Extension to retrieve and cache AWS Secrets Manager secrets and Parameter Store parameters in Lambda functions without using an SDK. For detailed information about using this extension, see [Use Secrets Manager secrets in Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/with-secrets-manager.html) in the *Lambda Developer Guide*.

## Using Secrets Manager secrets with Lambda
<a name="retrieving-secrets_lambda_getting-started"></a>

The Lambda Developer Guide provides comprehensive instructions for using Secrets Manager secrets in Lambda functions. To get started:

1. Follow the step-by-step tutorial in [Use Secrets Manager secrets in Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/with-secrets-manager.html), which includes:
   + Creating a Lambda function with your preferred runtime (Python, Node.js, Java)
   + Adding the AWS Parameters and Secrets Lambda Extension as a layer
   + Configuring the necessary permissions
   + Writing code to retrieve secrets from the extension
   + Testing your function

1. Learn about environment variables for configuring the extension's behavior, including cache settings and timeouts

1. Understand best practices for working with secret rotation

### Using Secrets Manager and Lambda in a VPC
<a name="retrieving-secrets_lambda_vpc"></a>

If your Lambda function runs in a VPC, you need to create a VPC endpoint so that the extension can make calls to Secrets Manager. For more information, see [Using an AWS Secrets Manager VPC endpoint](vpc-endpoint-overview.md).

## Using the AWS Parameters and Secrets Lambda Extension
<a name="retrieving-secrets_lambda_parameter-store"></a>

The extension can retrieve both Secrets Manager secrets and Parameter Store parameters. For detailed information about using Parameter Store parameters with the extension, see [Using Parameter Store parameters in Lambda functions](https://docs.aws.amazon.com/systems-manager/latest/userguide/ps-integration-lambda-extensions.html) in the *AWS Systems Manager User Guide*.

The Systems Manager documentation includes:
+ Detailed explanation of how the extension works with Parameter Store
+ Instructions for adding the extension to a Lambda function
+ Environment variables for configuring the extension
+ Sample commands for retrieving parameters
+ Complete list of extension ARNs for all supported architectures and regions