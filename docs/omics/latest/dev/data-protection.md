# Data protection in AWS HealthOmics

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS HealthOmics. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS HealthOmics or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Encryption at rest

###### Topics

- [AWS owned keys](#AWS-owned-cmk "#AWS-owned-cmk")
- [Customer managed keys](#customer-owned-cmk "#customer-owned-cmk")
- [Creating a customer managed key](#creating-co-cmk "#creating-co-cmk")
- [Required IAM permissions for using a customer managed key](#required-iam-cmk "#required-iam-cmk")
- [Learn more](#more-info-kms "#more-info-kms")

To protect sensitive customer data at rest, AWS HealthOmics provides encryption by default using a service-owned
AWS Key Management Service (AWS KMS) key. Customer managed keys are also supported. To learn more about customer managed key, see
[Amazon Key Management
Service](https://docs.AWS.amazon.com/kms/latest/developerguide/overview.html "https://docs.AWS.amazon.com/kms/latest/developerguide/overview.html").

All HealthOmics data stores (Storage and Analytics) support the use of customer managed keys.
The encryption configuration cannot be changed after a data store has been
created. If a data store is using an AWS owned key, it will be denoted as
AWS_OWNED_KMS_KEY and you will not see the specific key used for encryption at
rest.

For HealthOmics Workflows, customer-managed keys aren't supported by the temporary file
system; however, all data is encrypted at rest automatically using XTS-AES-256 block
cipher encryption algorithm to encrypt the file system. The IAM user and role used to
start a workflow run must also have access to the AWS KMS keys used for workflow input and
output buckets. Workflows does not use grants, and AWS KMS encryption is limited to input
and output Amazon S3 buckets. The IAM role used both for workflow APIs must also have
access to the AWS KMS keys used as well as the input and output Amazon S3 buckets. You can use
either IAM roles and permissions to control access or AWS KMS policies. To learn more,
see [Authentication and access control for AWS KMS](../../../kms/latest/developerguide/control-access.md "../../../kms/latest/developerguide/control-access.md").

When you use AWS Lake Formation with HealthOmics Analytics, any decrypt permissions associated with the Lake Formation are also given
to the input and output Amazon S3 buckets. More information about how AWS Lake Formation manages permissions can be found in the
[AWS Lake Formation
documentation](https://docs.AWS.amazon.com/lake-formation/latest/dg/register-encrypted.html "https://docs.AWS.amazon.com/lake-formation/latest/dg/register-encrypted.html").

HealthOmics Analytics grants Lake Formation kms:Decrypt permissions to read the encrypted
data in an Amazon S3 bucket. As long as you have permissions to query the data through Lake
Formation, you will be able to read the encrypted data. Access to the data is controlled
through data access control in Lake Formation, not through a KMS key policy. To learn
more, see the [AWS Integrated AWS service requests](https://docs.AWS.amazon.com/lake-formation/latest/dg/access-control-underlying-data.html "https://docs.AWS.amazon.com/lake-formation/latest/dg/access-control-underlying-data.html") in the Lake Formation documentation.

### AWS owned keys

By default, HealthOmics uses AWS owned keys to automatically encrypt data at rest, because this data can
contain sensitive information such as personally identifiable information (PII) or Protected Health Information
(PHI). AWS owned keys aren't stored in your account. They're part of a collection of KMS keys that AWS owns
and manages for use in multiple AWS accounts.

AWS services can use AWS owned keys to protect your data. You can't view, manage, or access
AWS owned keys, or audit their use. However, you don't need to do any work or change any programs to protect
the keys that encrypt your data.

You aren't charged a monthly fee or a usage fee for using AWS owned keys, and they don't count against
the AWS KMS quotas for your account. For more information, see [AWS managed keys](https://docs.AWS.amazon.com/kms/latest/developerguide/concepts.html#AWS-owned-cmk "https://docs.AWS.amazon.com/kms/latest/developerguide/concepts.html#AWS-owned-cmk").

### Customer managed keys

HealthOmics supports the use of symmetric customer managed keys that you create, own, and manage to add a second layer of
encryption over the existing AWS-owned encryption. Because you have full control of this layer of encryption,
you can perform such tasks as:

- Establishing and maintaining key policies, IAM policies, and
  grants
- Rotating key cryptographic material
- Enabling and disabling key policies
- Adding tags
- Creating key aliases
- Scheduling keys for deletion

You can also use CloudTrail to track the requests that HealthOmics sends to AWS KMS on your behalf. Additional AWS KMS
charges apply. For more information, see [customer managed keys](https://docs.AWS.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.AWS.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk").

### Creating a customer managed key

You can create a symmetric customer managed key by using the AWS Management Console, or the AWS KMS APIs.

Follow the steps for [Creating symmetric customer managed keys](https://docs.AWS.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk "https://docs.AWS.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk") in the AWS Key Management
Service Developer Guide.

Key policies control access to your customer managed key. Every customer managed key
must have exactly one key policy, which contains statements that determine who
can use the key and how they can use it. When you create a customer managed key,
you can specify a key policy. For more information, see [Managing access to customer managed keys](https://docs.AWS.amazon.com/kms/latest/developerguide/control-access-overview.html#managing-access "https://docs.AWS.amazon.com/kms/latest/developerguide/control-access-overview.html#managing-access") in the AWS Key Management
Service Developer Guide.

To use a customer managed key with your HealthOmics Analytics resources, the calling principal requires [kms:CreateGrant](https://docs.AWS.amazon.com/kms/latest/APIReference/API_CreateGrant.html "https://docs.AWS.amazon.com/kms/latest/APIReference/API_CreateGrant.html")
operations in the key policy. This allows the system to use a FAS Token to create a grant to a customer managed key
that controls access to a specified KMS key. This key gives a user access to the [kms:grant](https://docs.AWS.amazon.com/kms/latest/developerguide/grants.html#terms-grant-operations "https://docs.AWS.amazon.com/kms/latest/developerguide/grants.html#terms-grant-operations ") operations that HealthOmics requires. See [Using grants](https://docs.AWS.amazon.com/kms/latest/developerguide/grants.html "https://docs.AWS.amazon.com/kms/latest/developerguide/grants.html") for more
information.

For HealthOmics analytics, the following API operations must be permitted for the calling principal:

- kms:CreateGrant adds grants to a specific customer managed key, which
  allows access to grant operations in HealthOmics Analytics.
- kms:DescribeKey provides the customer managed key details needed to
  validate the key. This is required for all operations.
- kms:GenerateDataKey provides access to encrypt resources at rest for all write operations. Also, this
  action provides customer managed key details that the service can use to validate that the caller has access
  to use the key.
- kms:Decrypt provides access to read or search operations for encrypted
  resources.

To use a customer managed key with your HealthOmics storage resources, the HealthOmics service principal and the calling
principal must be permitted in the key policy. This allows the service to validate that the caller has access to
the key and uses the service principal to execute the store management using the customer managed key. For HealthOmics storage,
the key policy for the service principal must permit the following API operations:

- kms:DescribeKey provides the customer managed key details needed to
  validate the key. This is required for all operations.
- kms:GenerateDataKey provides access to encrypt resources at rest for all write operations.
  Also, this action provides customer managed key details that the service can use to validate that the caller
  has access to use the key.
- kms:Decrypt provides access to read or search operations for encrypted resources.

The following example shows a policy statement that allows a service principal to create and interact
with a HealthOmics sequence or reference store that is encrypted using the customer managed key:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
{
 "Effect": "Allow",
 "Principal": {
 "Service": "omics.amazonaws.com"
 },
 "Action": [
 "kms:Decrypt",
 "kms:DescribeKey",
 "kms:Encrypt",
 "kms:GenerateDataKey*"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following example shows a policy that creates permissions for a data store to decrypt data from an
Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "omics:GetReference",
 "omics:GetReferenceMetadata"
 ],
 "Resource": [
 "arn:aws:omics:`us-east-1`:`123456789012`:referenceStore/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::[[s3path]]/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key_id`"
 ],
 "Condition": {
 "StringEquals": {
 "kms:ViaService": [
 "s3.`us-east-1`.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

### Required IAM permissions for using a customer managed key

When creating a resource such as a data store with AWS KMS encryption using a customer managed key,
there are required permissions for both the key policy and the IAM policy for the IAM user or role.

You can use the [kms:ViaService condition key](https://docs.AWS.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-via-service "https://docs.AWS.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-via-service") to limit use of the KMS key to only
requests that originate from HealthOmics.

For more information about key policies, see [Enabling IAM policies](https://docs.AWS.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam "https://docs.AWS.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam") in the AWS Key Management Service Developer Guide.

###### Topics

- [Analytics API permissions](#analytics-permissions "#analytics-permissions")
- [Storage API permissions](#storage-permissions "#storage-permissions")
- [How HealthOmics uses grants in AWS KMS](#grants-kms "#grants-kms")
- [Monitoring your encryption keys for AWS HealthOmics](#monitoring-kms "#monitoring-kms")

#### Analytics API permissions

For HealthOmics analytics, the IAM user or role that creates the stores must have the kms:CreateGrant,
kms:GenerateDataKey, kms:Decrypt, and kms:DescribeKey permissions plus the necessary HealthOmics permissions.

#### Storage API permissions

For HealthOmics storage APIs, the IAM user or role that calls the following API operations requires the
listed permissions:

**CreateReferenceStore, CreateSequenceStore**

To create a store, the IAM caller must have `kms:DescribeKey` permissions plus the
necessary HealthOmics permissions. The HealthOmics service principal calls
`kms:GenerateDataKeyWithoutPlaintext` to perform access validation checks for data loading
and access.

**StartReadSetImportJob, StartReferenceImportJob**

To start data import jobs, the IAM caller must have `kms:Decrypt` and
`kms:GenerateDataKey` permissions for the KMS key on the store for the import, and
`kms:Decrypt` permissions on the Amazon S3 bucket containing the objects to import. In addition,
the role passed into the call must have `kms:Decrypt` permissions on the Amazon S3 bucket containing
the objects to import. The IAM caller must also have permissions to pass the role to the job.

**CreateMultipartReadSetUpload, UploadReadSetPart, CompleteMultipartReadSetUpload**

To complete a multi-part upload, the IAM caller must have `kms:Decrypt` and
`kms:GenerateDataKey` to create, upload, and complete the multi-part upload.

**StartReadSetExportJob**

To start a data export job, the IAM caller must have `kms:Decrypt` permission for the
KMS key on the store to export from and `kms:GenerateDataKey` and `kms:Decrypt`
permissions on the Amazon S3 bucket that receives the objects. In addition, the role passed into the call must
have `kms:Decrypt` permissions on the Amazon S3 bucket that receives the objects. The IAM caller
must also have permissions to pass the role to the job.

**StartReadsetActivationJob**

To start a read set activation job, the IAM caller must have `kms:Decrypt` and
`kms:GenerateDataKey` permissions for the objects.

**GetReference, GetReadSet**

To read objects from the store, the IAM caller must have `kms:Decrypt` permission
for the objects.

**Read Set S3 GetObject**

To read objects from the store using the Amazon S3 `GetObject` API, the IAM caller must
have `kms:Decrypt` permission for the objects. Set this permission for both customer managed key and
AWS owned key configurations.

#### How HealthOmics uses grants in AWS KMS

HealthOmics Analytics requires a [grant](https://docs.AWS.amazon.com/kms/latest/developerguide/grants.html "https://docs.AWS.amazon.com/kms/latest/developerguide/grants.html") to use your customer
managed KMS key. Grants aren't required or used for HealthOmics Workflows. HealthOmics Storage uses the customer managed key
directly from the service principal, so do not use a grant. When you create an analytics store encrypted
with a customer managed key, HealthOmics analytics creates a grant on your behalf by sending a [CreateGrant](https://docs.AWS.amazon.com/kms/latest/APIReference/API_CreateGrant.html "https://docs.AWS.amazon.com/kms/latest/APIReference/API_CreateGrant.html") request
to AWS KMS. Grants in AWS KMS are used to give HealthOmics access to a KMS key in a customer account.

It isn't recommended to revoke or retire the grants that HealthOmics analytics creates on your behalf. If
you revoke or retire the grant that gives HealthOmics permission to use the AWS KMS keys in your account, HealthOmics cannot
access this data, encrypt new resources pushed to the data store, or decrypt them when they are pulled.

When you revoke or retire a grant for HealthOmics, the change occurs immediately. To revoke access rights, we
recommend that you delete the data store rather than revoking the grant. When you delete the data store, HealthOmics
retires the grants on your behalf.

#### Monitoring your encryption keys for AWS HealthOmics

You can use CloudTrail to track the requests that AWS HealthOmics sends to AWS KMS on
your behalf when using a customer managed key. The log entries in the CloudTrail
log show HealthOmics.amazonAWS.com in the userAgent field to clearly
distinguish requests made by HealthOmics.

The following examples are CloudTrail events for CreateGrant, GenerateDataKey,
Decrypt, and DescribeKey to monitor AWS KMS operations called by HealthOmics to
access data encrypted by your customer managed key.

The following also shows how to use CreateGrant to allow HealthOmics analytics to access a customer
provided KMS key, enabling HealthOmics to use that KMS key to encrypt all customer data at rest.

You aren't required to create your own grants. HealthOmics creates a grant
on your behalf by sending a CreateGrant request to AWS KMS. Grants in AWS KMS are
used to give HealthOmics access to a AWS KMS key in a customer account.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "xx:test",
        "arn": "arn:AWS:sts::555555555555:assumed-role/user-admin/test",
        "accountId": "xx",
        "accessKeyId": "xxx",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "xxxx",
                "arn": "arn:AWS:iam::555555555555:role/user-admin",
                "accountId": "555555555555",
                "userName": "user-admin"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2022-11-11T01:36:17Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "apigateway.amazonAWS.com"
    },
    "eventTime": "2022-11-11T02:34:41Z",
    "eventSource": "kms.amazonAWS.com",
    "eventName": "CreateGrant",
    "AWSRegion": "us-west-2",
    "sourceIPAddress": "apigateway.amazonAWS.com",
    "userAgent": "apigateway.amazonAWS.com",
    "requestParameters": {
        "granteePrincipal": "AWS Internal",
        "keyId": "arn:AWS:kms:us-west-2:555555555555:key/a6e87d77-cc3e-4a98-a354-e4c275d775ef",
        "operations": [
            "CreateGrant",
            "RetireGrant",
            "Decrypt",
            "GenerateDataKey"
        ]
    },
    "responseElements": {
        "grantId": "4869b81e0e1db234342842af9f5531d692a76edaff03e94f4645d493f4620ed7",
        "keyId": "arn:AWS:kms:us-west-2:245126421963:key/xx-cc3e-4a98-a354-e4c275d775ef"
    },
    "requestID": "d31d23d6-b6ce-41b3-bbca-6e0757f7c59a",
    "eventID": "3a746636-20ef-426b-861f-e77efc56e23c",
    "readOnly": false,
    "resources": [
        {
            "accountId": "245126421963",
            "type": "AWS::KMS::Key",
            "ARN": "arn:AWS:kms:us-west-2:245126421963:key/xx-cc3e-4a98-a354-e4c275d775ef"
        }
    ],
    "eventType": "AWSApiCall",
    "managementEvent": true,
    "recipientAccountId": "245126421963",
    "eventCategory": "Management"
}

```

The following example shows how to use GenerateDataKey to ensure the user has
the necessary permissions to encrypt data before storing it.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLEUSER",
        "arn": "arn:AWS:sts::111122223333:assumed-role/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "EXAMPLEKEYID",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLEROLE",
                "arn": "arn:AWS:iam::111122223333:role/Sampleuser01",
                "accountId": "111122223333",
                "userName": "Sampleuser01"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2021-06-30T21:17:06Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "omics.amazonAWS.com"
    },
    "eventTime": "2021-06-30T21:17:37Z",
    "eventSource": "kms.amazonAWS.com",
    "eventName": "GenerateDataKey",
    "AWSRegion": "us-east-1",
    "sourceIPAddress": "omics.amazonAWS.com",
    "userAgent": "omics.amazonAWS.com",
    "requestParameters": {
        "keySpec": "AES_256",
        "keyId": "arn:AWS:kms:us-east-1:111122223333:key/EXAMPLE_KEY_ARN"
    },
    "responseElements": null,
    "requestID": "EXAMPLE_ID_01",
    "eventID": "EXAMPLE_ID_02",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:AWS:kms:us-east-1:111122223333:key/EXAMPLE_KEY_ARN"
        }
    ],
    "eventType": "AWSApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}

```

### Learn more

The following resources provide more information about data at rest
encryption.

For more information about [AWS Key Management Service basic concepts](https://docs.AWS.amazon.com/kms/latest/developerguide/concepts.html "https://docs.AWS.amazon.com/kms/latest/developerguide/concepts.html"), see the AWS KMS
documentation.

For more information about [Security best practices](https://docs.AWS.amazon.com/kms/latest/developerguide/best-practices.html "https://docs.AWS.amazon.com/kms/latest/developerguide/best-practices.html") in the AWS KMS documentation.

## Encryption in transit

AWS HealthOmics uses TLS 1.2+ to encrypt data in transit through the public endpoints
and through backend services.
