# Use AWS Secrets Manager secrets in AWS Lambda functions

AWS Lambda is a serverless compute service that lets you run code without provisioning or
managing servers. Parameter Store, a capability of AWS Systems Manager, provides secure, hierarchical
storage for configuration data management and secrets management. You can use the
AWS Parameters and Secrets Lambda Extension to retrieve and cache AWS Secrets Manager secrets and Parameter Store parameters in Lambda
functions without using an SDK. For detailed information about using this extension, see [Use Secrets Manager
secrets in Lambda functions](../../../lambda/latest/dg/with-secrets-manager.md "../../../lambda/latest/dg/with-secrets-manager.md") in the _Lambda Developer Guide_.

## Using Secrets Manager secrets with

Lambda

The Lambda Developer Guide provides comprehensive instructions for using Secrets Manager secrets in
Lambda functions. To get started:

1. Follow the step-by-step tutorial in [Use Secrets Manager secrets in Lambda
   functions](../../../lambda/latest/dg/with-secrets-manager.md "../../../lambda/latest/dg/with-secrets-manager.md"), which includes:
   - Creating a Lambda function with your preferred runtime (Python, Node.js,
     Java)
   - Adding the AWS Parameters and Secrets Lambda Extension as a layer
   - Configuring the necessary permissions
   - Writing code to retrieve secrets from the extension
   - Testing your function

2. Learn about environment variables for configuring the extension's behavior, including
   cache settings and timeouts
3. Understand best practices for working with secret rotation

### Using Secrets Manager and Lambda in a VPC

If your Lambda function runs in a VPC, you need to create a VPC endpoint so that the
extension can make calls to Secrets Manager. For more information, see [Using an AWS Secrets Manager VPC endpoint](vpc-endpoint-overview.md "vpc-endpoint-overview.md").

## Using the AWS Parameters and Secrets Lambda Extension

The extension can retrieve both Secrets Manager secrets and Parameter Store parameters. For detailed
information about using Parameter Store parameters with the extension, see [Using Parameter
Store parameters in Lambda functions](../../../systems-manager/latest/userguide/ps-integration-lambda-extensions.md "../../../systems-manager/latest/userguide/ps-integration-lambda-extensions.md") in the
_AWS Systems Manager User Guide_.

The Systems Manager documentation includes:

- Detailed explanation of how the extension works with Parameter Store
- Instructions for adding the extension to a Lambda function
- Environment variables for configuring the extension
- Sample commands for retrieving parameters
- Complete list of extension ARNs for all supported architectures and regions
