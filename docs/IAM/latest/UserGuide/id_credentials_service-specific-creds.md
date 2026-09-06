

# Service-specific credentials for IAM users
<a name="id_credentials_service-specific-creds"></a>

Service-specific credentials are specialized authentication mechanisms designed for specific AWS services. These credentials provide simplified authentication compared to standard AWS credentials, and are tailored to the authentication requirements of individual AWS services. Unlike access keys, which can be used across multiple AWS services, service-specific credentials are designed for use with only the service for which they were created. This targeted approach enhances security by limiting the scope of the credentials.

Service-specific credentials typically consist of a user name and password pair or specialized API keys that are formatted according to the requirements of the specific service. When you create service-specific credentials, they are active by default and can be used immediately. You can have a maximum of two sets of service-specific credentials for each supported service per IAM user. This limit allows you to maintain one active set while rotating to a new set when needed. AWS currently supports service-specific credentials for the following services:

## When to use service-specific credentials
<a name="id_credentials_service-specific-creds-usecase"></a>

Service-specific credentials are intended for compatibility with third-party libraries, SDKs, tools, or applications that are not natively compatible with AWS credentials, AWS SDKs, or AWS APIs. Such use cases include migrating to AWS services from self-hosted infrastructure or from services hosted by other providers.

When starting from scratch, and wherever possible, we recommend that you use AWS temporary credentials, such as those provided by an IAM role, to authenticate with an AWS service using an AWS SDK or a library that supports AWS temporary credentials.

## Rotating service-specific credentials
<a name="id_credentials_service-specific-creds-rotation"></a>

As a security best practice, rotate service-specific credentials regularly. To rotate credentials without disrupting your applications:

1. Create a second set of service-specific credentials for the same service and IAM user

1. Update all applications to use the new credentials and verify they work correctly

1. Change the status of the original credentials to "Inactive"

1. Verify that all applications are still functioning properly

1. Delete the inactive service-specific credentials when you're confident they're no longer needed

## Monitoring service-specific credentials
<a name="id_credentials_service-specific-creds-monitoring"></a>

You can use AWS CloudTrail to monitor the use of service-specific credentials in your AWS account. To view CloudTrail events related to service-specific credential usage, review the CloudTrail logs for events from the service where the credentials are used. For more information, see [Logging IAM and AWS STS API calls with AWS CloudTrail](cloudtrail-integration.md).

For additional security, consider setting up CloudWatch alarms to notify you of specific credential usage patterns that might indicate unauthorized access or other security concerns. For more information, see [Monitoring CloudTrail Log Files with Amazon CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html) in the *AWS CloudTrail User Guide*.

The following topics provide information about service-specific credentials.

**Topics**
+ [When to use service-specific credentials](#id_credentials_service-specific-creds-usecase)
+ [Rotating service-specific credentials](#id_credentials_service-specific-creds-rotation)
+ [Monitoring service-specific credentials](#id_credentials_service-specific-creds-monitoring)
+ [API keys for AWS services](id_credentials_api_keys_for_aws_services.md)
+ [Use IAM with Amazon Keyspaces (for Apache Cassandra)](id_credentials_keyspaces.md)