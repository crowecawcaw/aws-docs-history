# Use AWS KMS Permissions for Amazon SageMaker Partner AI Apps

You can protect your data at rest using encryption for Amazon SageMaker Partner AI Apps. By default, it uses
server-side encryption with a SageMaker owned key. SageMaker also supports an option for server-side
encryption with a customer managed KMS key.

## Server-side encryption with SageMaker managed keys

(Default)

Partner AI Apps encrypt all your data at rest using an AWS managed key by default.

## Server-side encryption with customer

managed KMS keys (Optional)

Partner AI Apps support the use of a symmetric customer managed key that you create, own, and
manage to replace the existing AWS owned encryption. Because you have full control of
this layer of encryption, you can perform such tasks as:

- Establishing and maintaining key policies
- Establishing and maintaining IAM policies and grants
- Enabling and disabling key policies
- Rotating key cryptographic material
- Adding tags
- Creating key aliases
- Scheduling keys for deletion

For more information, see [Customer managed
keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer Guide_.

## How Partner AI Apps use grants in AWS KMS

Partner AI Apps require a grant to use your customer managed key. When you create an
application encrypted with a customer managed key, Partner AI Apps creates a grant on
your behalf by sending a CreateGrant request to AWS KMS. Grants in AWS KMS are used to give
Partner AI Apps access to a KMS key in a customer account.

You can revoke access to the grant, or remove the service's access to the customer
managed key at any time. If you do, Partner AI App won't be able to access any of the data
encrypted by the customer managed key, which affects operations that are dependent on
that data. The application will not operate properly and will become
irrecoverable.

## Create a customer managed key

You can create a symmetric customer managed key by using the AWS Management Console or the
AWS KMS APIs.

**To create a symmetric customer managed key**

Follow the steps for [Creating
symmetric encryption KMS keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer
Guide_.

**Key policy**

Key policies control access to your customer managed key. Every customer managed key
must have exactly one key policy, which contains statements that determine who can use
the key and how they can use it. When you create your customer managed key, you can
specify a key policy. For more information, see [Determining access to AWS KMS
keys](../../../kms/latest/developerguide/determining-access.md "../../../kms/latest/developerguide/determining-access.md") in the _AWS Key Management Service Developer Guide_.

To use your customer managed key with your Partner AI App resources, the following API
operations must be permitted in the key policy. The principal for these operations
depends on whether the role is used to create or use the application.

- Creating the application:
  - `kms:CreateGrant`
  - [`kms:DescribeKey`](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md")

- Using the application:
  - [`kms:Decrypt`](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md")
  - [`kms:GenerateDataKey`](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md")

The following are policy statement examples you can add for Partner AI Apps based on
whether the persona is an administrator or user. For more information about specifying
permissions in a policy, see [AWS KMS
permissions](../../../kms/latest/developerguide/kms-api-permissions-reference.md "../../../kms/latest/developerguide/kms-api-permissions-reference.md") in the _AWS Key Management Service Developer Guide_. For more
information about troubleshooting, see [Troubleshooting key
access](../../../kms/latest/developerguide/policy-evaluation.md "../../../kms/latest/developerguide/policy-evaluation.md") in the _AWS Key Management Service Developer Guide_.

**Administrator**

The following policy statement is used for the administrator who is creating
Partner AI Apps.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "example-key-policy",
 "Statement": [
 {
 "Sid": "Allow use of the key",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`<admin-role>`"
 },
 "Action": [
 "kms:CreateGrant",
 "kms:DescribeKey"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "sagemaker.`us-east-1`.amazonaws.com"
 }
 }
 }
 ]
}`

```

**User**

The following policy statement is for the user of the Partner AI Apps.

JSON

```
`{
 "Version":"2012-10-17",
 "Id":"example-key-policy",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "AWS":"arn:aws:iam::`111122223333`:role/`user-role`"
 },
 "Action":[
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource":"*",
 "Condition":{
 "StringEquals":{
 "kms:ViaService":"sagemaker.`us-east-1`.amazonaws.com"
 }
 }
 }
 ]
}`

```
