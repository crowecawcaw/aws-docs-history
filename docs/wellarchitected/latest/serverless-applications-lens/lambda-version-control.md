# Lambda version control

Like all software, maintaining versioning enables the quick visibility of previously
functioning code as well as the ability to revert back to a previous version if a new
deployment is unsuccessful. AWS Lambda allows you to [publish one or more immutable versions
for individual Lambda functions](../../../lambda/latest/dg/configuration-versions.md "../../../lambda/latest/dg/configuration-versions.md") such that previous versions cannot be changed. Each
Lambda function version has a unique Amazon Resource Name (ARN) and new version changes are
auditable as they are recorded in [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/").
As a best practice in production, customers should enable versioning to use a reliable
architecture.

To simplify deployment operations and reduce the risk of error, [Lambda function
aliases](../../../lambda/latest/dg/configuration-aliases.md "../../../lambda/latest/dg/configuration-aliases.md") activate different variations of your Lambda function in your development
workflow, such as development, beta, and production. An example of this is when an [API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/") integration with Lambda points to the ARN
of a production alias. The production alias will point to a Lambda version. The value of this
technique is that it activates a safe deployment when promoting a new version to the live
environment because the Lambda alias within the caller configuration remains static, thus there
are fewer changes to make.
