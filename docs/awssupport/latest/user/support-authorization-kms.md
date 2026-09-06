

# Configuring AWS KMS keys for AWS Support authorization
<a name="support-authorization-kms"></a>

## Key requirements
<a name="support-authorization-kms-requirements"></a>

A customer-managed AWS KMS key is required for cryptographic signing of support permits. Your key must meet the following requirements:
+ Key spec: `ECC_NIST_P384`
+ Key usage: `SIGN_VERIFY`
+ The key must be in the same AWS Region as the support permit.

Your private key material never leaves AWS KMS. You create a grant on your key that allows it to call `DescribeKey`, `GetPublicKey`, and `Sign`. The grant is scoped to the support permit and retires when the support permit is deleted or deactivated.

## How AWS Support authorization uses your AWS KMS key
<a name="support-authorization-kms-how-used"></a>

When you create a support permit, your AWS KMS key is used in the following way:

1. Uses [forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html) to call `DescribeKey` on your behalf, verifying that the key meets the required spec (`ECC_NIST_P384`) and usage (`SIGN_VERIFY`).

1. Creates a grant on the key by calling `CreateGrant` on your behalf. The grant allows `DescribeKey`, `GetPublicKey`, and `Sign` operations.

1. Verifies authorization when an AWS Support request matches an existing support permit by using the grant to call `Sign` on the key. The resulting signature verifies that AWS Support is authorized to perform the action.

## Required key policy statements
<a name="support-authorization-kms-policy"></a>

Add the following policy statements to your AWS KMS key policy. These are the minimum permissions required for AWS Support authorization to use your key.

```
{
  "Sid": "Allows access to CreateGrant through SupportAuthZ",
  "Effect": "Allow",
  "Principal": {"AWS": "arn:aws:iam::111122223333:role/ExampleRole"},
  "Action": ["kms:CreateGrant"],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:ViaService": "supportauthz.us-east-1.amazonaws.com",
      "kms:GranteeServicePrincipal": "us-east-1.supportauthz.amazonaws.com",
      "kms:RetiringServicePrincipal": "us-east-1.supportauthz.amazonaws.com"
    },
    "ForAllValues:StringEquals": {
      "kms:GrantOperations": ["DescribeKey", "GetPublicKey", "Sign"]
    },
    "ArnLike": {
      "kms:GrantConstraintSourceArn": "arn:aws:supportauthz:us-east-1:111122223333:supportpermit/*"
    }
  }
},
{
  "Sid": "Allows access to DescribeKey through SupportAuthZ",
  "Effect": "Allow",
  "Principal": {"AWS": "arn:aws:iam::111122223333:role/ExampleRole"},
  "Action": ["kms:DescribeKey"],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:ViaService": "supportauthz.us-east-1.amazonaws.com"
    }
  }
}
```

These statements grant the following permissions:

CreateGrant  
Allows the creation of grants for `DescribeKey`, `GetPublicKey`, and `Sign` operations. The conditions restrict grant creation to requests that are made through the AWS Support authorization service and scoped to support permit resources in your account. AWS Support authorization uses [forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html) to call `CreateGrant` as part of creating a support permit.

DescribeKey  
Allows verification that the key meets the required spec and usage type when you create a support permit using forward access sessions.

**Note**  
Replace `111122223333` with your AWS account ID and `us-east-1` with the AWS Region where you create your support permits.

## Revoking AWS Support authorization access
<a name="support-authorization-kms-revoke"></a>

The recommended way to revoke signing permissions on your key is to revoke the grant. This prevents further signing operations without affecting other uses of the key.

To list and revoke grants for AWS Support authorization:

1. List grants on the key to find the grant ID:

   ```
   aws kms list-grants \
       --key-id 1234abcd-12ab-34cd-56ef-1234567890ab
   ```

   Identify the grant by its name or the `GrantConstraints` source ARN that references your support permit.

1. Revoke the grant:

   ```
   aws kms revoke-grant \
       --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
       --grant-id grant-id-from-list-grants
   ```

After you revoke the grant, new signed authorizations can no longer be issued for any support permit that uses this key. Because the AWS KMS API follows an eventual consistency model, there might be a brief delay before the change is available throughout AWS KMS.

**Note**  
Revoking a grant doesn't delete the associated support permit. The support permit remains in ACTIVE state, but authorizations can't be signed for it. Grants are specific to each support permit. Creating a new support permit with the same AWS KMS key doesn't restore AWS Support authorization's ability to use the key for the original support permit.

## Disabling or deleting the key
<a name="support-authorization-kms-disable-delete"></a>

You can also disable or schedule deletion of the AWS KMS key to prevent AWS Support authorization from issuing signed authorizations. However, this affects all uses of the key, not just AWS Support authorization.

**Important**  
Both AWS KMS and AWS Support authorization are eventually consistent. After you disable or schedule deletion of a key, it can take up to several minutes for the change to take full effect. During this period, signed authorizations might continue to be issued by using the key. Grant revocation is also eventually consistent.

If you disable a key, then you can re-enable it in the AWS KMS console or by calling `EnableKey`. If you delete a key, it can't be recovered.

## Monitoring key usage
<a name="support-authorization-kms-monitoring"></a>

When your AWS KMS key is used to sign an authorization, AWS CloudTrail logs the signing operation in the key's event history. You can use these events to audit when and how often authorizations are signed on your behalf.