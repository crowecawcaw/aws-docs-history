# AWS KMS key management

Amazon Aurora automatically integrates with [AWS Key Management Service (AWS KMS)](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md") for key management.
Amazon Aurora uses envelope
encryption. For more information about envelope encryption, see [Envelope encryption](../../../kms/latest/developerguide/concepts.md#enveloping "../../../kms/latest/developerguide/concepts.md#enveloping") in the _AWS Key Management Service Developer
Guide_.

You can use two types of AWS KMS keys to encrypt your DB
clusters.

- If you want full control over a KMS key, you must create a
  _customer managed key_. For more information about
  customer managed keys, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer
  Guide_.
- _AWS managed keys_ are KMS keys in your account
  that are created, managed, and used on your behalf by an AWS service
  that is integrated with AWS KMS. By default, the RDS AWS managed key
  ( `aws/rds`) is used for encryption. You can't
  manage, rotate, or delete the RDS AWS managed key. For more
  information about AWS managed keys, see [AWS managed keys](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk") in the _AWS Key Management Service Developer
  Guide_.
  To manage KMS keys used for
  Amazon Aurora encrypted DB

clusters, use the [AWS Key Management Service
(AWS KMS)](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md") in the [AWS KMS console](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms"),
the AWS CLI, or the AWS KMS API. To view audit logs of every action taken with an
AWS managed or customer managed key, use [AWS CloudTrail](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
For more information about key rotation, see [Rotating AWS KMS
keys](../../../kms/latest/developerguide/rotate-keys.md "../../../kms/latest/developerguide/rotate-keys.md").

## Authorizing use of a customer managed key

When
Aurora uses a customer managed key in cryptographic operations, it acts
on behalf of the user who is creating or changing the
Aurora resource.

To create an
Aurora resource using a customer managed key, a user
must have permissions to call the following operations on the
customer managed key:

- `kms:CreateGrant`
- `kms:DescribeKey`

You can specify these required permissions in a key policy, or in an IAM
policy if the key policy allows it.

###### Important

When you use explicit deny statements for all resources (\*) in AWS KMS key policies with managed services like Amazon RDS, you must specify a condition to allow the resource owning account. Operations might fail without this condition, even if the deny rule includes exceptions for your IAM user.

###### Tip

To follow the principle of least privilege, do not allow full access
to `kms:CreateGrant`. Instead, use the [kms:ViaService condition key](../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-via-service "../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-via-service") to allow the user to create
grants on the KMS key only when the grant is created on the user's
behalf by an AWS service.

You can make the IAM policy stricter in various ways. For example, if
you want to allow the customer managed key to be used only for requests that originate
in
Aurora, use the [kms:ViaService condition key](../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-via-service "../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-via-service") with the
`rds.`<region>`.amazonaws.com`
value. Also, you can use the keys or values in the [Amazon RDS encryption context](#Overview.Encryption.Keys.encryptioncontext "#Overview.Encryption.Keys.encryptioncontext")
as a
condition for using the customer managed key for encryption.

For more information, see [Allowing users in other accounts to use a KMS key](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md") in the
_AWS Key Management Service Developer Guide_ and [Key
policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md").

## Amazon RDS encryption context

When
Aurora uses your KMS key, or when Amazon EBS uses the KMS key on
behalf of
Aurora, the service specifies an [encryption
context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context"). The encryption context is [additional
authenticated data](../../../crypto/latest/userguide/cryptography-concepts.md#term-aad "../../../crypto/latest/userguide/cryptography-concepts.md#term-aad") (AAD) that AWS KMS uses to ensure data
integrity. When an encryption context is specified for an encryption
operation, the service must specify the same encryption context for the
decryption operation. Otherwise, decryption fails. The encryption context is
also written to your [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") logs to help you understand why a given KMS key was
used. Your CloudTrail logs might contain many entries describing the use of a
KMS key, but the encryption context in each log entry can help you
determine the reason for that particular use.

At minimum,
Aurora always uses the DB
cluster ID for the
encryption context, as in the following JSON-formatted example:

```
{ "aws:rds:dbc-id": "cluster-CQYSMDPBRZ7BPMH7Y3RTDG5QY" }
```

This encryption context can help you identify the DB
cluster for which
your KMS key was used.

When your KMS key is used for a specific DB
cluster and a specific
Amazon EBS volume, both the DB
cluster ID and the Amazon EBS volume ID are used for
the encryption context, as in the following JSON-formatted example:

```
{
  "aws:rds:dbc-id": "cluster-BRG7VYS3SVIFQW7234EJQOM5RQ",
  "aws:ebs:id": "vol-ad8c6542"
}
```
