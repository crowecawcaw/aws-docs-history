# Data protection and the AWS shared responsibility model in Image Builder

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in EC2 Image Builder. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Image Builder or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Encryption and key management in

Image Builder

Image Builder encrypts data in transit and at rest by default with a service-owned
KMS key, except for the following:

- **Custom components** – Image Builder
  encrypts custom components with your default KMS key, or a
  service-owned KMS key.
- **Image workflows** – Image Builder
  can encrypt your image workflows with a customer managed key if you specify
  the key during workflow creation. Image Builder handles encryption and
  decryption with your key to run the workflows that you've configured
  for your images.

You can manage your own keys through AWS KMS. However, you don't have permission
to manage the Image Builder KMS key owned by Image Builder. For more information about managing
your KMS keys with AWS Key Management Service, see [Getting
Started](../../../kms/latest/developerguide/getting-started.md "../../../kms/latest/developerguide/getting-started.md") in the AWS Key Management Service Developer Guide.

###### Encryption context

To provide an additional integrity and authenticity check on your encrypted
data, you have the option of including an [encryption context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context")
when you encrypt the data. When a resource is encrypted with an encryption
context, AWS KMS cryptographically binds the context to the ciphertext. The
resource can only be decrypted if the requester provides an exact, case-sensitive
match for the context.

The policy examples in this section use an encryption context that resembles the
Amazon Resource Name (ARN) of an Image Builder workflow resource.

### Encrypt image workflows with a customer managed key

To add a layer of protection, you can encrypt your Image Builder workflow resources with
your own customer managed key. If you use your customer managed key to encrypt the Image Builder workflows that you
create, you must grant access in the key policy for Image Builder to use your key when it
encrypts and decrypts workflow resources. You can revoke access at any time. However,
Image Builder will not have access to any workflows that are already encrypted if you revoke
access to the key.

The process to grant Image Builder access to use your customer managed key has two steps, as follows:

###### Step 1: Add key policy permissions for Image Builder workflows

To enable Image Builder to encrypt and decrypt workflow resources when it creates
or uses those workflows, you must specify permissions in the
KMS key policy.

This example key policy grants access for Image Builder pipelines to encrypt workflow
resources during the creation process, and decrypt workflow resources to use them.
The policy also grants access for key administrators. The encryption context and
resource specification use a wildcard to cover all Regions where you have
workflow resources.

As a prerequisite for using image workflows, you created an IAM workflow execution
role that grants permission for Image Builder to run workflow actions. The principal for the
first statement shown in the key policy example here must specify your IAM workflow
execution role.

For more information about customer managed keys, see
[Managing access to customer managed keys](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the
_AWS Key Management Service Developer Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow access to build images with encrypted workflow",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`YourImageBuilderExecutionRole`"
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "kms:EncryptionContext:aws:imagebuilder:arn": "arn:aws:imagebuilder:*:`111122223333`:workflow/*"
 }
 }
 },
 {
 "Sid": "Allow access for key administrators",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "kms:*"
 ],
 "Resource": "arn:aws:kms:*:`111122223333`:key/*"
 }
 ]
}`

```

###### Step 2: Grant key access to your workflow execution role

The IAM role that Image Builder assumes to run your workflows needs permission
to use your customer managed key. Without access to your key, Image Builder won't be able
to encrypt or decrypt your workflow resources with it.

Edit the policy for your workflow execution role to add the following
policy statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAccessToWorkflowKey",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:`us-west-2`:`111122223333`:key/key_ID",
 "Condition": {
 "StringLike": {
 "kms:EncryptionContext:aws:imagebuilder:arn": "arn:aws:imagebuilder:*:`111122223333`:workflow/*"
 }
 }
 }
 ]
}`

```

### AWS CloudTrail events for image workflows

The following examples show typical AWS CloudTrail entries for encrypting
and decrypting image workflows that are stored with a customer managed key.

###### Example: GenerateDataKey

This example shows what a CloudTrail event might look like when Image Builder invokes
the AWS KMS **GenerateDataKey** API action from the Image Builder
**CreateWorkflow** API action. Image Builder must encrypt a new
workflow before it creates the workflow resource.

```
`{
 "eventVersion": "1.08",
 "userIdentity": {
 "type": "AssumedRole",
 "principalId": "PRINCIPALID1234567890:workflow-role-name",
 "arn": "arn:aws:sts::111122223333:assumed-role/Admin/workflow-role-name",
 "accountId": "111122223333",
 "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
 "sessionContext": {
 "sessionIssuer": {
 "type": "Role",
 "principalId": "PRINCIPALID1234567890",
 "arn": "arn:aws:iam::111122223333:role/Admin",
 "accountId": "111122223333",
 "userName": "Admin"
 },
 "webIdFederationData": {},
 "attributes": {
 "creationDate": "2023-11-21T20:29:31Z",
 "mfaAuthenticated": "false"
 }
 },
 "invokedBy": "imagebuilder.amazonaws.com"
 },
 "eventTime": "2023-11-21T20:31:03Z",
 "eventSource": "kms.amazonaws.com",
 "eventName": "GenerateDataKey",
 "awsRegion": "us-west-2",
 "sourceIPAddress": "imagebuilder.amazonaws.com",
 "userAgent": "imagebuilder.amazonaws.com",
 "requestParameters": {
 "encryptionContext": {
 "aws:imagebuilder:arn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/sample-encrypted-workflow/1.0.0/*",
 "aws-crypto-public-key": "`key value`"
 },
 "keyId": "arn:aws:kms:us-west-2:111122223333:alias/ExampleKMSKey",
 "numberOfBytes": 32
 },
 "responseElements": null,
 "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
 "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
 "readOnly": true,
 "resources": [
 {
 "accountId": "111122223333",
 "type": "AWS::KMS::Key",
 "ARN": "arn:aws:kms:us-west-2:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLEzzzzz"
 }
 ],
 "eventType": "AwsApiCall",
 "managementEvent": true,
 "recipientAccountId": "111122223333",
 "eventCategory": "Management"
}`
```

###### Example: Decrypt

This example shows what a CloudTrail event might look like when Image Builder
invokes the AWS KMS **Decrypt** API action from the Image Builder
**GetWorkflow** API action. Image Builder pipelines need to decrypt
a workflow resource before they can use it.

```
`{
 "eventVersion": "1.08",
 "userIdentity": {
 "type": "AssumedRole",
 "principalId": "PRINCIPALID1234567890:workflow-role-name",
 "arn": "arn:aws:sts::111122223333:assumed-role/Admin/workflow-role-name",
 "accountId": "111122223333",
 "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
 "sessionContext": {
 "sessionIssuer": {
 "type": "Role",
 "principalId": "PRINCIPALID1234567890",
 "arn": "arn:aws:iam::111122223333:role/Admin",
 "accountId": "111122223333",
 "userName": "Admin"
 },
 "webIdFederationData": {},
 "attributes": {
 "creationDate": "2023-11-21T20:29:31Z",
 "mfaAuthenticated": "false"
 }
 },
 "invokedBy": "imagebuilder.amazonaws.com"
 },
 "eventTime": "2023-11-21T20:34:25Z",
 "eventSource": "kms.amazonaws.com",
 "eventName": "Decrypt",
 "awsRegion": "us-west-2",
 "sourceIPAddress": "imagebuilder.amazonaws.com",
 "userAgent": "imagebuilder.amazonaws.com",
 "requestParameters": {
 "keyId": "arn:aws:kms:us-west-2:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLEzzzzz",
 "encryptionAlgorithm": "SYMMETRIC_DEFAULT",
 "encryptionContext": {
 "aws:imagebuilder:arn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/sample-encrypted-workflow/1.0.0/*",
 "aws-crypto-public-key": "ABC123def4567890abc12345678/90dE/F123abcDEF+4567890abc123D+ef1=="
 }
 },
 "responseElements": null,
 "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
 "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
 "readOnly": true,
 "resources": [
 {
 "accountId": "111122223333",
 "type": "AWS::KMS::Key",
 "ARN": "arn:aws:kms:us-west-2:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLEzzzzz"
 }
 ],
 "eventType": "AwsApiCall",
 "managementEvent": true,
 "recipientAccountId": "111122223333",
 "eventCategory": "Management"
}`
```

## Data storage in Image Builder

Image Builder doesn't store any of your logs in the service. All logs are saved on your
Amazon EC2 instance that is used to build the image, or in your Systems Manager automation logs.

## Inter-network Traffic Privacy in

Image Builder

Connections are secured between Image Builder and on-premises locations, between AZs within
an AWS Region, and between AWS Regions through HTTPS. There are no direct
connections between accounts.
