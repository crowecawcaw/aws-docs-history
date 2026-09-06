

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner adds support for referencing secrets and configurations from AWS Secrets Manager and AWS Systems Manager Parameter Store on January 5, 2023
<a name="release-2023-01-05-secrets-paramters"></a>

AWS App Runner now supports referencing secrets and configuration data stored in AWS Secrets Manager and AWS SSM Parameter Store in App Runner service.

**Release date:** January 5, 2023

## Changes
<a name="release-2023-01-05-secrets-paramters.changes"></a>

AWS App Runner now supports securely referencing secrets and configuration data that are stored in Secrets Manager and SSM  Parameter Store by adding them as environment variables in your App Runner service. 

Secrets Manager and SSM  Parameter Store are AWS services that provide secure storage and reliable management of sensitive data such as configuration data and secrets. Examples of data you can store include passwords, database strings or connection parameters, license codes, API keys, and application versions. App Runner leverages the capabilities of Secrets Manager and SSM  Parameter Store to integrate a more secure experience for your applications using App Runner service. 

App Runner only stores reference to the Amazon Resource Name (ARN) of the secret or parameter stored in Secrets Manager or SSM  Parameter Store. This ensures that your sensitive data isn't visible to others in App Runner service configurations and application logs. As such, secrets and parameters are managed in a way that's completely isolated from your App Runner application code and your App Runner service configuration. 

For more information, see [Referencing environment variables](https://docs.aws.amazon.com/apprunner/latest/dg/env-variable.html) in the *AWS App Runner Developer Guide*.