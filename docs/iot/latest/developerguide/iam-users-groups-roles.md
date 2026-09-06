

# IAM users, groups, and roles
<a name="iam-users-groups-roles"></a>

IAM users, groups, and roles are the standard mechanisms for managing identity and authentication in AWS. You can use them to connect to AWS IoT HTTP interfaces using the AWS SDK and AWS CLI.

IAM roles also allow AWS IoT to access other AWS resources in your account on your behalf. For example, if you want to have a device publish its state to a DynamoDB table, IAM roles allow AWS IoT to interact with Amazon DynamoDB. For more information, see [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html).

For message broker connections over HTTP, AWS IoT authenticates users, groups, and roles using the Signature Version 4 signing process. For information, see [Signing AWS API Requests](https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html).

When authenticating requests using query parameters with [temporary security credentials provided by AWS Security Token Service (AWS STS)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html), do not include `X-Amz-Security-Token` in the canonical query string when calculating the signature. Instead, append `X-Amz-Security-Token` as a query parameter after the signature has been computed. This differs from some other AWS services that require the security token to be part of the canonical request. For more information, see [ Signing requests with temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-create-signed-request.html#temporary-security-credentials).

**Note**  
The AWS IoT Device SDKs handle this signing behavior automatically. If you are implementing custom signing code, refer to the SDK source for reference:  
[AWS IoT Device SDK for Python v2](https://github.com/aws/aws-iot-device-sdk-python-v2/blob/main/awsiot/mqtt_connection_builder.py) — see `websockets_with_default_aws_signing()`, which sets `omit_session_token=True`
[AWS IoT Device SDK for Java v2](https://github.com/aws/aws-iot-device-sdk-java-v2/blob/main/sdk/src/main/java/software/amazon/awssdk/iot/AwsIotMqttConnectionBuilder.java) — see `setOmitSessionToken(true)`

When using AWS Signature Version 4 with AWS IoT, clients must support the following in their TLS implementation:
+ TLS 1.2
+ SHA-256 RSA certificate signature validation
+ One of the cipher suites from the TLS cipher suite support section

For information, see [Identity and access management for AWS IoT](security-iam.md).