# Control access to multi-Region keys

You can use multi-Region keys in compliance, disaster recovery, and backup scenarios that
would be more complex with single-Region keys. However, because the security properties of
multi-Region keys are significantly different from those of single-Region keys, we recommend
using caution when authorizing the creation, management, and use of multi-Region
keys.

###### Note

Existing IAM policy statements with wildcard characters in the `Resource`
field now apply to both single-Region and multi-Region keys. To restrict them to
single-Region KMS keys or multi-Region keys, use the [kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion "conditions-kms.md#conditions-kms-multiregion") condition key.

Use your authorization tools to prevent creation and use of multi-Region keys in any
scenario where a single-Region will suffice. Allow principals to replicate a multi-Region
key only into AWS Regions that require them. Give permission for multi-Region keys only to
principals who need them and only for tasks that require them.

You can use key policies, IAM policies, and grants to allow IAM principals to manage
and use multi-Region keys in your AWS account. Each multi-Region key is an independent
resource with a unique key ARN and key policy. You need to establish and maintain a key
policy for each key and make sure that new and existing IAM policies implement your
authorization strategy.

To support multi-Region keys, AWS KMS uses an IAM service linked role. This role gives
AWS KMS the permissions it needs to synchronize [shared
properties](multi-region-keys-overview.md#mrk-sync-properties "multi-region-keys-overview.md#mrk-sync-properties"). For more information, see [Authorizing AWS KMS to synchronize multi-Region
keys](multi-region-auth-slr.md "multi-region-auth-slr.md").

###### Topics

- [Authorization basics for multi-Region
  keys](#multi-region-auth-about "#multi-region-auth-about")
- [Authorizing multi-Region key administrators
  and users](#multi-region-auth-users "#multi-region-auth-users")

## Authorization basics for multi-Region

keys

When designing key policies and IAM policies for multi-Region keys, consider the
following principles.

- **Key policy** — Each multi-Region key is
  an independent KMS key resource with its own [key
  policy](key-policies.md "key-policies.md"). You can apply the same or a different key policy to each key
  in the set of related multi-Region keys. Key policies are _not_
  [shared properties](multi-region-keys-overview.md#mrk-sync-properties "multi-region-keys-overview.md#mrk-sync-properties") of multi-Region
  keys. AWS KMS does not copy or synchronize key policies among related multi-Region
  keys.

When you create a replica key in the AWS KMS console, the console displays the
current key policy of the primary key as a convenience. You can use this key
policy, edit it, or delete and replace it. But even if you accept the primary
key policy unchanged, AWS KMS doesn't synchronize the policies. For example, if
you change the key policy of the primary key, the key policy of the replica key
remains the same.

- **Default key policy** — When you create
  multi-Region keys by using the [CreateKey](../../../IAM/latest/APIReference/API_CreateKey.md "../../../IAM/latest/APIReference/API_CreateKey.md") and `ReplicateKey` operations, the [default key policy](key-policy-default.md "key-policy-default.md") is applied unless you
  specify a key policy in the request. This is the same default key policy that is
  applied to single-Region keys.
- **IAM policies** — As with all
  KMS keys, you can use IAM policies to control access to multi-Region keys
  only when the [key
  policy allows it](key-policy-default.md#key-policy-default-allow-root-enable-iam "key-policy-default.md#key-policy-default-allow-root-enable-iam"). [IAM policies](iam-policies.md "iam-policies.md")
  apply to all AWS Regions by default. However, you can use condition keys, such
  as [aws:RequestedRegion](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requestedregion "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requestedregion"), to limit permissions to a particular Region.

To create primary and replica keys, principals must have
`kms:CreateKey` permission in an IAM policy that applies to the
Region where the key is created.

- **Grants** — AWS KMS [grants](grants.md "grants.md") are Regional. Each grant allows permissions to one KMS key.
  You can use grants to allow permissions to a multi-Region primary key or replica
  key. But you cannot use a single grant to allow permissions to multiple
  KMS keys, even if they are related multi-Region keys.
- **Key ARN** — Each multi-Region key has a
  [unique key ARN](mrk-how-it-works.md "mrk-how-it-works.md"). The key ARNs of
  related multi-Region keys have the same partition, account, and key ID, but
  different Regions.

To apply an IAM policy statement to a particular multi-Region key, use its
key ARN or a key ARN pattern that includes the Region. To apply an IAM policy
statement to all related multi-Region keys, use a wildcard character (\*) in the
Region element of the ARN, as shown in the following example.

```
{
  "Effect": "Allow",
  "Action": [
    "kms:Describe*",
    "kms:List*"
  ],
  "Resource": {
      "arn:aws:kms:**\***::111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab"
  }
}
```

To apply a policy statement to all multi-Region keys in your AWS account,
you can use the [kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion "conditions-kms.md#conditions-kms-multiregion") policy condition or a key ID pattern that includes
the distinctive `mrk-` prefix.

- **Service-linked role** — Principals who
  create multi-Region primary keys must have [iam:CreateServiceLinkedRole](../../../IAM/latest/APIReference/API_CreateServiceLinkedRole.md "../../../IAM/latest/APIReference/API_CreateServiceLinkedRole.md") permission.

To synchronize the shared properties of related multi-Region keys, AWS KMS
assumes an IAM [service-linked
role](multi-region-auth-slr.md "multi-region-auth-slr.md"). AWS KMS creates the service-linked role in the AWS account
whenever you create a multi-Region primary key. (If the role exists, AWS KMS
recreates it, which has no harmful effect.) The role is valid in all Regions. To
allow AWS KMS to create (or recreate) the service-linked role, principals who
create multi-Region primary keys must have [iam:CreateServiceLinkedRole](../../../IAM/latest/APIReference/API_CreateServiceLinkedRole.md "../../../IAM/latest/APIReference/API_CreateServiceLinkedRole.md") permission.

## Authorizing multi-Region key administrators

and users

Principals who create and manage multi-Region keys need the following permissions in
the primary and replica Regions:

- `kms:CreateKey`
- `kms:ReplicateKey`
- `kms:UpdatePrimaryRegion`
- `iam:CreateServiceLinkedRole`

### Creating a primary key

To [create a multi-Region primary key](create-primary-keys.md "create-primary-keys.md"),
the principal needs [kms:CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") and [iam:CreateServiceLinkedRole](../../../IAM/latest/APIReference/API_CreateServiceLinkedRole.md "../../../IAM/latest/APIReference/API_CreateServiceLinkedRole.md") permissions in an IAM policy that is
effective in the primary key's Region. Principals who have these permissions can
create single-Region and multi-Region keys unless you restrict their permissions.

The `iam:CreateServiceLinkedRole` permission allows AWS KMS to create the
[AWSServiceRoleForKeyManagementServiceMultiRegionKeys role](multi-region-auth-slr.md "multi-region-auth-slr.md") to synchronize the
[shared properties](multi-region-keys-overview.md#mrk-sync-properties "multi-region-keys-overview.md#mrk-sync-properties") of related
multi-Region keys.

For example, this IAM policy allows a principal to create multi-Region keys,
attach policies for those keys, and service linked roles for multi-Region
keys.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":{
 "Action": [
 "kms:CreateKey",
 "iam:CreateServiceLinkedRole"
 ],
 "Effect":"Allow",
 "Resource":"*"
 }
}`

```

To allow or deny permission to create multi-Region primary keys, use the [kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion "conditions-kms.md#conditions-kms-multiregion") condition key. Valid
values are `true` (multi-Region key) or `false` (single-Region
key). For example, the following IAM policy statement uses a `Deny`
action with the `kms:MultiRegion` condition key to prevent principals
from creating multi-Region keys.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":{
 "Action":"kms:CreateKey",
 "Effect":"Deny",
 "Resource":"*",
 "Condition": {
 "Bool": {
 "kms:MultiRegion": true
 }
 }
 }
}`

```

### Replicating keys

To create a multi-Region replica key,
the principal needs the following permissions:

- [kms:ReplicateKey](../APIReference/API_ReplicateKey.md "../APIReference/API_ReplicateKey.md")
  permission in the key policy of the primary key.
- [kms:CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md")
  permission in an IAM policy that is effective in the replica key
  Region.

Use caution when allowing these permissions. They allow principals to create
KMS keys and the key policies that authorize their use. The
`kms:ReplicateKey` permission also authorizes the transfer of key
material across Region boundaries within AWS KMS.

To restrict the AWS Regions in which a multi-Region key can be replicated, use
the [kms:ReplicaRegion](conditions-kms.md#conditions-kms-replica-region "conditions-kms.md#conditions-kms-replica-region") condition
key. It limits only the `kms:ReplicateKey` permission. Otherwise, it has
no effect. For example, the following key policy allows the principal to replicate
this primary key, but only in the specified Regions.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/Administrator"
  },
  "Action": "kms:ReplicateKey",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:ReplicaRegion": [
         "us-east-1",
         "eu-west-3",
         "ap-southeast-2"
      ]
    }
  }
}
```

### Updating the primary Region

Authorized principals can convert a replica key to a primary key, which changes
the former primary key into a replica. This action is known as [updating the primary Region](multi-region-update.md "multi-region-update.md"). To update the
primary Region, the principal needs [kms:UpdatePrimaryRegion](../APIReference/API_UpdatePrimaryRegion.md "../APIReference/API_UpdatePrimaryRegion.md")
permission in both Regions. You can provide these permissions in a key policy or
IAM policy.

- `kms:UpdatePrimaryRegion` on the primary key. This permission
  must be effective in the primary key Region.
- `kms:UpdatePrimaryRegion` on the replica key. This permission
  must be effective in the replica key Region.

For example, the following key policy gives users who can assume the Administrator
role permission to update the primary Region of the KMS key. This KMS key can be
the primary key or a replica key in this operation.

```
{
  "Effect": "Allow",
  "Resource": "*",
  "Principal": {
    "AWS": "arn:aws:iam::111122223333:role/Administrator"
  },
  "Action": "kms:UpdatePrimaryRegion"
}
```

To restrict the AWS Regions that can host a primary key, use the [kms:PrimaryRegion](conditions-kms.md#conditions-kms-primary-region "conditions-kms.md#conditions-kms-primary-region") condition key.
For example, the following IAM policy statement allows the principals to update
the primary Region of the multi-Region keys in the AWS account, but only when the
new primary Region is one of the specified Regions.

```
{
  "Effect": "Allow",
  "Action": "kms:UpdatePrimaryRegion",
  "Resource": {
      "arn:aws:kms:*:111122223333:key/*"
  },
  "Condition": {
    "StringEquals": {
      "kms:PrimaryRegion": [
         "us-west-2",
         "sa-east-1",
         "ap-southeast-1"
      ]
    }
  }
}
```

### Using and managing multi-Region keys

By default, principals who have permission to use and manage KMS keys in an
AWS account and Region also have permission to use and manage multi-Region keys.
However, you can use the [kms:MultiRegion](conditions-kms.md#conditions-kms-multiregion "conditions-kms.md#conditions-kms-multiregion") condition key to allow only single-Region keys or only
multi-Region keys. Or use the [kms:MultiRegionKeyType](conditions-kms.md#conditions-kms-multiregion-key-type "conditions-kms.md#conditions-kms-multiregion-key-type") condition key to allow only multi-Region primary
keys or only replica keys. Both condition keys controls access to the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") operation and to any
operation that uses an existing KMS key, such as [Encrypt](../APIReference/API_Encrypt.md "../APIReference/API_Encrypt.md") or [EnableKey](../APIReference/API_EnableKey.md "../APIReference/API_EnableKey.md").

The following example IAM policy statement uses the `kms:MultiRegion`
condition key to prevent the principals from using or managing any multi-Region
key.

```
{
  "Effect": "Deny",
  "Action": "kms:*",
  "Resource": "*",
  "Condition": {
    "Bool": "kms:MultiRegion": true
  }
}
```

This example IAM policy statement uses the `kms:MultiRegionKeyType`
condition to allow principals to schedule and cancel key deletion, but only on
multi-Region replica keys.

```
{
  "Effect": "Allow",
  "Action": [
    "kms:ScheduleKeyDeletion",
    "kms:CancelKeyDeletion"
  ],
  "Resource": {
      "arn:aws:kms:us-west-2:111122223333:key/*"
  },
  "Condition": {
    "StringEquals": "kms:MultiRegionKeyType": "REPLICA"
  }
}
```
