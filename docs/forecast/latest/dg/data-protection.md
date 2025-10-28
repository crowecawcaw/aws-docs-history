Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Data Protection in Amazon Forecast

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in Amazon Forecast. As described in this model, AWS is
responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are
responsible for maintaining control over your content that is hosted on this infrastructure.
You are also responsible for the security configuration and management tasks for the AWS services
that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/"). For information about data protection in Europe, see the [AWS Shared
Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security
Blog_.

For data protection purposes, we recommend that you protect AWS account
credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
- Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](../../../awscloudtrail/latest/userguide/cloudtrail-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-trails.md") in the _AWS CloudTrail User Guide_.
- Use AWS encryption solutions, along with all default security controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering
  and securing sensitive data that is stored in Amazon S3.
- If you require FIPS 140-3 validated cryptographic modules when accessing AWS through
  a command line interface or an API, use a FIPS endpoint. For more information about the
  available FIPS endpoints, see [Federal
  Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put confidential or sensitive information, such as your
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Forecast or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Encryption at Rest

In Amazon Forecast encryption configuration is provided during the [CreateDataset](API_CreateDataset.md "API_CreateDataset.md") and [CreatePredictor](API_CreatePredictor.md "API_CreatePredictor.md") operations. If encryption configuration is provided in the CreateDataset operation, your CMK and IAM Role for encryption at rest is used in the [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md") operation.

For example, if you provide your key's KMSKeyArn and a RoleArn in the EncryptionConfig statement of the CreateDataset operation, Forecast will assume that role and use the key to encrypt the dataset. If no configuration is provided, then Forecast uses the default service keys for encryption. Additionally, if you provide the EncryptionConfig information for the CreatePredictor operation, then all subsequent operations, such as CreatePredictorExplanability, CreateForecast and CreatePredictorBacktestExportJob, will use the same configuration to perform encryption at rest. Again, if you do not provide an encryption configuration, then Forecast will use the default service encryption.

For any data stored in your Amazon S3 bucket, data is encrypted by the default Amazon S3 key. You can also use your own AWS KMS key to encrypt your data and give Forecast access to this key. For information about data encryption in Amazon S3 see [Protecting data using encryption](../../../AmazonS3/latest/userguide/UsingEncryption.md "../../../AmazonS3/latest/userguide/UsingEncryption.md"). For information about managing your own AWS KMS key, see [Managing keys](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the _AWS Key Management Service Developer Guide_.

## Encryption in Transit and Processing

Amazon Forecast uses TLS with AWS certificates to encrypt any data sent to other AWS services.
Any communication with other AWS services happens over HTTPS, and Forecast endpoints support only secure connections over HTTPS.

Amazon Forecast copies data out of your account and processes it in an internal AWS system. When processing data, Forecast encrypts data with either a Forecast AWS KMS key or any AWS KMS key you provide.

## How Amazon Forecast uses grants in AWS KMS

Amazon Forecast requires a [grant](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") to use your customer managed key.

Forecast creates a grant using the IAM role that is passed during **EncryptionConfig** in the [CreatePredictor](API_CreatePredictor.md#forecast-CreatePredictor-request-EncryptionConfig "API_CreatePredictor.md#forecast-CreatePredictor-request-EncryptionConfig") or [CreateDataset](API_CreateDataset.md#forecast-CreateDataset-request-EncryptionConfig "API_CreateDataset.md#forecast-CreateDataset-request-EncryptionConfig") operation. Forecast assumes the role and does a create grant operation on your behalf. See [Setup IAM role](aws-forecast-iam-roles.md "aws-forecast-iam-roles.md") for more details.

However, when you create a predictor encrypted with a customer managed key, Amazon Forecast creates a grant on your behalf by sending a [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") request to AWS KMS. Grants in AWS KMS are used to give Amazon Forecast access to an AWS KMS key in a customer account.

Amazon Forecast requires the grant so that it can use your customer managed key to send Decrypt requests to AWS KMS in order to read the encrypted dataset artifacts. Forecast also uses the grant to send GenerateDataKey requests to AWS KMS in order to [encrypt](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md") the training artifacts back to Amazon S3.

You can revoke access to the grant, or remove the service's access to the customer managed key at any time. If you do, Amazon Forecast won't be able to access any of the data encrypted by the customer managed key, which affects operations that are dependent on that data. For example, if you attempt to perform the CreateForecast operation on an encrypted predictor that Amazon Forecast can't access, then the operation will return an AccessDeniedException error.

## Create a customer managed key

You can create a symmetric customer managed key by using the AWS Management Console or the AWS KMS API. To create a symmetric customer managed key, follow the steps for [Creating symmetric customer managed key](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer Guide_.

Key policies control access to your customer managed key. Every customer managed key must have exactly one key policy, which contains statements that determine who can use the key and how they can use it. When you create your customer managed key, you can specify a key policy. For more information, see [Managing access to customer managed keys](../../../kms/latest/developerguide/control-access-overview.md#managing-access "../../../kms/latest/developerguide/control-access-overview.md#managing-access") in the _AWS Key Management Service Developer Guide_.

To use your customer managed key with Amazon Forecast resources, the following API operations must be permitted in the key policy:

- [kms:DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") – Provides the customer managed key details that allow Amazon Forecast to validate the key.
- [kms:CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") – Adds a grant to a customer managed key. Grants control access to a specified AWS KMS key, which allows access to [grant operations](../../../kms/latest/developerguide/grants.md#terms-grant-operations "../../../kms/latest/developerguide/grants.md#terms-grant-operations") that Amazon Forecast requires. This operation allows Amazon Forecast to call `GenerateDataKey` to generate an encrypted data key and store it, because the data key is not immediately used for encryption. Also, the operation allows Amazon Forecast to call `Decrypt` so that it can use the stored encrypted data key and access the encrypted data.
- [kms:RetireGrant](../../../kms/latest/APIReference/API_RetireGrant.md "../../../kms/latest/APIReference/API_RetireGrant.md") - Retire all the grants provided during `CreateGrant` operation after the operation is completed.

###### Note

Amazon Forecast performs `kms:Decrypt` and `kms:GenerateDataKey` validation on the caller's identity. You will receive an AccessDeniedException in the event that the caller doesn't have the relevant permissions. The key policy should also resemble the following code:

```
`"Effect": "Allow",
"Principal": {
 "AWS": “AWS Invoking Identity”
},
"Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey”
 ],
 "Resource": "*"
}`
```

For more details, see [IAM Policy](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

The following are policy statement examples you can add for Amazon Forecast. These are the minimal permissions required, these can be added using IAM policies as well.

```
 `"Statement" : [
 {"Sid" : "Allow access to principals authorized to use Amazon Forecast",
 "Effect" : "Allow",
 "Principal" : {"AWS" : "arn:aws:iam::111122223333:role/`ROLE_PASSED_TO_FORECAST`"
 },
 "Action" : [
 "kms:DescribeKey",
 "kms:CreateGrant",
 "kms:RetireGrant"
 ],
 "Resource" : "*",
 "Condition" : {"StringEquals" : {"kms:ViaService" : "forecast.`region`.amazonaws.com",
 "kms:CallerAccount" : "111122223333"
 }
 },
 {"Sid": "Allow access for key administrators",
 "Effect": "Allow",
 "Principal": {"AWS": "arn:aws:iam::111122223333:root"
 },
 "Action" : [
 "kms:*"
 ],
 "Resource": "arn:aws:kms:`region`:111122223333:key/`key_ID`"
 }
 ]`
```

See the _AWS Key Management Service Developer Guide_ for more information about [specifying permissions in a policy](../../../kms/latest/developerguide/control-access-overview.md#overview-policy-elements "../../../kms/latest/developerguide/control-access-overview.md#overview-policy-elements") and [troubleshooting key access](../../../kms/latest/developerguide/policy-evaluation.md#example-no-iam "../../../kms/latest/developerguide/policy-evaluation.md#example-no-iam").

## Monitoring your encryption keys for Amazon Forecast Service

When you use an AWS KMS customer managed key with your Amazon Forecast Service resources, you can use [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") or [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") to track requests that Forecast sends to AWS KMS. The following examples are AWS CloudTrail events for `CreateGrant`, `RetireGrant`, and `DescribeKey` to monitor AWS KMS operations called by Amazon Forecast to access data encrypted by your customer managed key.

DescribeKey

```
`{
 "eventVersion": "1.08",
 "userIdentity": {
 "type": "AssumedRole",
 "principalId": "`AROAIGDTESTANDEXAMPLE:Sampleuser01`",
 "arn": "arn:aws:sts::111122223333:assumed-role/Admin/`Sampleuser01`",
 "accountId": "111122223333",
 "accessKeyId": "`AKIAIOSFODNN7EXAMPLE3`",
 "sessionContext": {
 "sessionIssuer": {
 "type": "Role",
 "principalId": "`AROAIGDTESTANDEXAMPLE:Sampleuser01`",
 "arn": "arn:aws:sts::111122223333:assumed-role/Admin/`Sampleuser01`",
 "accountId": "111122223333",
 "userName": "Admin"
 },
 "webIdFederationData": {},
 "attributes": {
 "creationDate": "2022-10-05T21:16:23Z",
 "mfaAuthenticated": "false"
 }
 }
 },
 "eventTime": "2022-10-05T21:16:23Z",
 "eventSource": "kms.amazonaws.com",
 "eventName": "DescribeKey",
 "awsRegion": "`region`",
 "sourceIPAddress": "172.12.34.56",
 "userAgent": "ExampleDesktop/1.0 (V1; OS)",
 "requestParameters": {
 "keyId": "arn:aws:kms:`region`:111122223333:key/`1234abcd-12ab-34cd-56ef-123456SAMPLE`"
 },
 "responseElements": null,
 "requestID": "`ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE`",
 "eventID": "`ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE`",
 "readOnly": true,
 "resources": [
 {
 "accountId": "111122223333",
 "type": "AWS::KMS::Key",
 "ARN": "arn:aws:kms:`region`:111122223333:key/`1234abcd-12ab-34cd-56ef-123456SAMPLE`"
 }
 ],
 "eventType": "AwsApiCall",
 "managementEvent": true,
 "recipientAccountId": "111122223333",
 "eventCategory": "Management",
 "tlsDetails": {
 "tlsVersion": "TLSv1.2",
 "cipherSuite": "ECDHE-RSA-AES256-GCM-SHA384",
 "clientProvidedHostHeader": "kms.`region`.amazonaws.com"
 }
}`
```

CreateGrant

```
`{
 "eventVersion": "1.08",
 "userIdentity": {
 "type": "AssumedRole",
 "principalId": "`AROAIGDTESTANDEXAMPLE:Sampleuser01`",
 "arn": "arn:aws:sts::111122223333:assumed-role/Admin/`Sampleuser01`",
 "accountId": "111122223333",
 "accessKeyId": "`AKIAIOSFODNN7EXAMPLE3`",
 "sessionContext": {
 "sessionIssuer": {
 "type": "Role",
 "principalId": "`AROAIGDTESTANDEXAMPLE:Sampleuser01`",
 "arn": "arn:aws:sts::111122223333:assumed-role/Admin/`Sampleuser01`",
 "accountId": "111122223333",
 "userName": "Admin"
 },
 "webIdFederationData": {},
 "attributes": {
 "creationDate": "2022-10-05T23:10:27Z",
 "mfaAuthenticated": "false"
 }
 }
 },
 "eventTime": "2022-10-05T23:10:27Z",
 "eventSource": "kms.amazonaws.com",
 "eventName": "CreateGrant",
 "awsRegion": "`region`",
 "sourceIPAddress": "172.12.34.56",
 "userAgent": "ExampleDesktop/1.0 (V1; OS)",
 "requestParameters": {
 "operations": [
 "Decrypt",
 "GenerateDataKey"
 ],
 "granteePrincipal": "AWS Internal",
 "keyId": "arn:aws:kms:`region`:111122223333:key/`1234abcd-12ab-34cd-56ef-123456SAMPLE`"
 },
 "responseElements": {
 "grantId": "`0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE`"
 },
 "requestID": "`ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE`",
 "eventID": "`ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE`",
 "readOnly": false,
 "resources": [
 {
 "accountId": "111122223333",
 "type": "AWS::KMS::Key",
 "ARN": "arn:aws:kms:`region`:111122223333:key/`1234abcd-12ab-34cd-56ef-123456SAMPLE`"
 }
 ],
 "eventType": "AwsApiCall",
 "managementEvent": true,
 "recipientAccountId": "111122223333",
 "eventCategory": "Management",
 "tlsDetails": {
 "tlsVersion": "TLSv1.2",
 "cipherSuite": "ECDHE-RSA-AES256-GCM-SHA384",
 "clientProvidedHostHeader": "kms.`region`.amazonaws.com"
 }
}`
```

RetireGrant

```
`{
 "eventVersion": "1.08",
 "userIdentity": {
 "type": "AssumedRole",
 "principalId": "`AROAIGDTESTANDEXAMPLE:Sampleuser01`",
 "arn": "arn:aws:sts::111122223333:assumed-role/Admin/`Sampleuser01`",
 "accountId": "111122223333",
 "accessKeyId": "`AKIAIOSFODNN7EXAMPLE3`",
 "sessionContext": {
 "sessionIssuer": {
 "type": "Role",
 "principalId": "`AROAIGDTESTANDEXAMPLE:Sampleuser01`",
 "arn": "arn:aws:sts::111122223333:assumed-role/Admin/`Sampleuser01`",
 "accountId": "111122223333",
 "userName": "Admin"
 },
 "webIdFederationData": {},
 "attributes": {
 "creationDate": "2022-10-06T04:56:14Z",
 "mfaAuthenticated": "false"
 }
 }
 },
 "eventTime": "2022-10-06T04:56:14Z",
 "eventSource": "kms.amazonaws.com",
 "eventName": "RetireGrant",
 "awsRegion": "`region`",
 "sourceIPAddress": "172.12.34.56",
 "userAgent": "ExampleDesktop/1.0 (V1; OS)",
 "requestParameters": null,
 "responseElements": null,
 "additionalEventData": {
 "grantId": "`0ab0ac0d0b000f00ea00cc0a0e00fc00bce000c000f0000000c0bc0a0000aaafSAMPLE`"
 },
 "requestID": "`ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE`",
 "eventID": "`ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE`",
 "readOnly": false,
 "resources": [
 {
 "accountId": "111122223333",
 "type": "AWS::KMS::Key",
 "ARN": "arn:aws:kms:`region`:111122223333:key/`1234abcd-12ab-34cd-56ef-123456SAMPLE`"
 }
 ],
 "eventType": "AwsApiCall",
 "managementEvent": true,
 "recipientAccountId": "111122223333",
 "eventCategory": "Management",
 "tlsDetails": {
 "tlsVersion": "TLSv1.2",
 "cipherSuite": "ECDHE-RSA-AES256-GCM-SHA384",
 "clientProvidedHostHeader": "kms.`region`.amazonaws.com"
 }
}`
```
