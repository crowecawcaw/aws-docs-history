# Required KMS key policy for use with encrypted EBS volumes in AWS PCS

AWS PCS uses [service-linked
roles](service-linked-roles.md "service-linked-roles.md") to delegate permissions to other AWS services. The AWS PCS
service-linked role is predefined and includes permissions that AWS PCS requires to
call other AWS services on your behalf. The predefined permissions also include access
to your AWS managed keys but not to your customer managed keys.

This topic describes how to set up the key policy required to launch
instances when you specify a customer managed key for Amazon EBS encryption.

###### Note

AWS PCS doesn't require additional authorization to use the default
AWS managed key to protect the encrypted volumes in your account.

###### Contents

- [Overview](security-key-policy-for-encrypted-volumes.md#overview "security-key-policy-for-encrypted-volumes.md#overview")
- [Configure key policies](security-key-policy-for-encrypted-volumes.md#configuring-key-policies "security-key-policy-for-encrypted-volumes.md#configuring-key-policies")
- [Example 1: Key policy sections that
  allow access to the customer managed key](security-key-policy-for-encrypted-volumes.md#policy-example-cmk-access "security-key-policy-for-encrypted-volumes.md#policy-example-cmk-access")
- [Example 2: Key policy
  sections that allow cross-account access to the customer managed key](security-key-policy-for-encrypted-volumes.md#policy-example-cmk-cross-account-access "security-key-policy-for-encrypted-volumes.md#policy-example-cmk-cross-account-access")
- [Edit key policies in the AWS KMS
  console](security-key-policy-for-encrypted-volumes.md#eding-key-policies-console "security-key-policy-for-encrypted-volumes.md#eding-key-policies-console")

## Overview

You can use the following AWS KMS keys for Amazon EBS encryption when AWS PCS
launches instances:

- [AWS managed key](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk") – An encryption key in your account
  that Amazon EBS creates, owns, and manages. This is the default encryption key
  for a new account. Amazon EBS uses the AWS managed key for encryption unless you
  specify a customer managed key.
- [Customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") – A custom encryption key that you create,
  own, and manage. For more information, see [Create a KMS key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
  _AWS Key Management Service Developer Guide_.

###### Note

The key must be symmetric. Amazon EBS doesn't support asymmetric
customer managed keys.

You configure customer managed keys when you create encrypted snapshots or a launch template
that specifies encrypted volumes, or when you choose to enable encryption by default.

## Configure key policies

Your KMS keys must have a key policy that allows AWS PCS to launch instances
with Amazon EBS volumes encrypted with a customer managed key.

Use the examples on this page to configure a key policy to give AWS PCS access to
your customer managed key. You can modify the customer managed key's key policy when you create the key
or at a later time.

The key policy must have the following statements:

- A statement that allows the IAM identity specified in the
  `Principal` element to use the customer managed key directly. It
  includes permissions to perform the AWS KMS `Encrypt`,
  `Decrypt`, `ReEncrypt*`,
  `GenerateDataKey*`, and `DescribeKey` operations
  on the key.
- A statement that allows the IAM identity specified in the
  `Principal` element to use the `CreateGrant`
  operation to generate grants that delegate a subset of its own permissions
  to AWS services that are integrated with AWS KMS or another principal. This
  allows them to use the key to create encrypted resources on your
  behalf.

Don't change any existing statements in the policy when you add the
new policy statements to your key policy.

For more information, see:

- [create-key](../../../cli/latest/reference/kms/create-key.md "../../../cli/latest/reference/kms/create-key.md")
  in the _AWS CLI Command Reference_
- [put-key-policy](../../../cli/latest/reference/kms/put-key-policy.md "../../../cli/latest/reference/kms/put-key-policy.md")
  in the _AWS CLI Command Reference_
- [Find the key ID and
  key ARN](../../../kms/latest/developerguide/find-cmk-id-arn.md "../../../kms/latest/developerguide/find-cmk-id-arn.md")
  in the _AWS Key Management Service Developer Guide_
- [Service-linked roles for
  AWS PCS](service-linked-roles.md "service-linked-roles.md")
- [Amazon EBS encryption](../../../ebs/latest/userguide/ebs-encryption.md "../../../ebs/latest/userguide/ebs-encryption.md") in the _Amazon EBS User Guide_
- [AWS Key Management Service](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md")
  in the _AWS Key Management Service Developer Guide_

## Example 1: Key policy sections that

allow access to the customer managed key

Add the following policy statements to the key policy of the customer managed key.
Replace the example ARN with the ARN of the your `AWSServiceRoleForPCS`
service-linked role. This example policy gives the
AWS PCS service-linked role (`AWSServiceRoleForPCS`)
permissions to use the customer managed key.

```
{
   "Sid": "Allow service-linked role use of the customer managed key",
   "Effect": "Allow",
   "Principal": {
       "AWS": [
           "arn:aws:iam::`account-id`:role/aws-service-role/pcs.amazonaws.com/AWSServiceRoleForPCS"
       ]
   },
   "Action": [
       "kms:Encrypt",
       "kms:Decrypt",
       "kms:ReEncrypt*",
       "kms:GenerateDataKey*",
       "kms:DescribeKey"
   ],
   "Resource": "*"
}
```

```
{
   "Sid": "Allow attachment of persistent resources",
   "Effect": "Allow",
   "Principal": {
       "AWS": [
           "arn:aws:iam::`account-id`:role/aws-service-role/pcs.amazonaws.com/AWSServiceRoleForPCS"
       ]
   },
   "Action": [
       "kms:CreateGrant"
   ],
   "Resource": "*",
   "Condition": {
       "Bool": {
           "kms:GrantIsForAWSResource": true
       }
    }
}
```

## Example 2: Key policy

sections that allow cross-account access to the customer managed key

If you create a customer managed key in a different account than your AWS PCS cluster, you must
use a **grant** in combination with the key policy to allow
cross-account access to the key.

###### To grant access to the key

1. Add the following policy statements to the customer managed key's key
   policy. Replace the example ARN with the ARN of the other account.
   Replace `111122223333` with the
   actual account ID of the AWS account that you want to create the AWS PCS
   cluster in. This allows you to give an IAM user or role in the specified
   account permission to create a grant for the key using the CLI command that
   follows. By default, users don't have access to the key.

```
{.
   "Sid": "Allow external account `111122223333` use of the customer managed key",
   "Effect": "Allow",
   "Principal": {
       "AWS": [
           "arn:aws:iam::`111122223333`:root"
       ]
   },
   "Action": [
       "kms:Encrypt",
       "kms:Decrypt",
       "kms:ReEncrypt*",
       "kms:GenerateDataKey*",
       "kms:DescribeKey"
   ],
   "Resource": "*"
}
```

```
{
   "Sid": "Allow attachment of persistent resources in external account `111122223333`",
   "Effect": "Allow",
   "Principal": {
       "AWS": [
           "arn:aws:iam::`111122223333`:root"
       ]
   },
   "Action": [
       "kms:CreateGrant"
   ],
   "Resource": "*"
}
```

2. From the account that you want to create the AWS PCS cluster in, create a
   grant that delegates the relevant permissions to the AWS PCS
   service-linked role. The value of `grantee-principal`
   is the ARN of the service-linked role. The value of `key-id`
   is the ARN of the key.

The following example [create-grant](../../../cli/latest/reference/kms/create-grant.md "../../../cli/latest/reference/kms/create-grant.md") CLI
command gives the service-linked role named
`AWSServiceRoleForPCS` in account
`111122223333` permissions to use the
customer managed key in account
`444455556666`.

```
aws kms create-grant \
  --region `us-west-2` \
  --key-id `arn:aws:kms:us-west-2:444455556666:key/1a2b3c4d-5e6f-1a2b-3c4d-5e6f1a2b3c4d` \
  --grantee-principal arn:aws:iam::`111122223333`:role/aws-service-role/pcs.amazonaws.com/AWSServiceRoleForPCS \
  --operations "Encrypt" "Decrypt" "ReEncryptFrom" "ReEncryptTo" "GenerateDataKey" "GenerateDataKeyWithoutPlaintext" "DescribeKey" "CreateGrant"
```

###### Note

The user making the request must have
permissions to use the `kms:CreateGrant` action.

The following example IAM policy allows an IAM identity (user or role)
in account `111122223333` to create a
grant for the customer managed key in account
`444455556666`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreationOfGrantForTheKMSKeyinExternalAccount`444455556666`",
 "Effect": "Allow",
 "Action": "kms:CreateGrant",
 "Resource": "`arn:aws:kms:us-west-2:444455556666:key/1a2b3c4d-5e6f-1a2b-3c4d-5e6f1a2b3c4d`"
 }
 ]
}`

```

For more information about creating a grant for a KMS key in a different
AWS account, see [Grants in AWS KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") in
the _AWS Key Management Service Developer Guide_.

###### Important

The service-linked role name specified as the grantee principal must
be the name of an existing role. After creating the grant, to ensure
that the grant allows AWS PCS to use the specified KMS key, do not
delete and recreate the service-linked role.

## Edit key policies in the AWS KMS

console

The examples in the previous sections show only how to add statements to a key
policy, which is just one way of changing a key policy. The easiest way to change a
key policy is to use the AWS KMS console's default view for key policies and make an
IAM identity (user or role) one of the _key
users_ for the appropriate key policy. For more information, see
[Using the AWS Management Console default view](../../../kms/latest/developerguide/key-policy-modifying.md#key-policy-modifying-how-to-console-default-view "../../../kms/latest/developerguide/key-policy-modifying.md#key-policy-modifying-how-to-console-default-view") in the
_AWS Key Management Service Developer Guide_.

###### Warning

The console's default view policy statements include permissions
to perform AWS KMS `Revoke` operations on the customer managed key. If you
revoke a grant that gave an AWS account access to a customer managed key in
your account, users in that AWS account lose access to the encrypted
data and the key.
