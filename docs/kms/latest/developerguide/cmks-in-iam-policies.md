# Specifying KMS keys in IAM policy

statements

You can use an IAM policy to allow a principal to use or manage KMS keys. KMS keys
are specified in the `Resource` element of the policy statement.

- To specify a KMS key in an IAM policy statement, you must use its [key ARN](concepts.md#key-id-key-ARN "concepts.md#key-id-key-ARN"). You cannot use a [key id](concepts.md#key-id-key-id "concepts.md#key-id-key-id"), [alias name](concepts.md#key-id-alias-name "concepts.md#key-id-alias-name"), or [alias ARN](concepts.md#key-id-alias-ARN "concepts.md#key-id-alias-ARN") to identify a KMS key in an IAM policy
  statement.

For example: "`Resource": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`"

To control access to a KMS key based on its aliases, use the [kms:RequestAlias](conditions-kms.md#conditions-kms-request-alias "conditions-kms.md#conditions-kms-request-alias") or [kms:ResourceAliases](conditions-kms.md#conditions-kms-resource-aliases "conditions-kms.md#conditions-kms-resource-aliases") condition keys. For
details, see [ABAC for AWS KMS](abac.md "abac.md").

Use an alias ARN as the resource only in a policy statement that controls access to
alias operations, such as [CreateAlias](../APIReference/CreateAlias.md "../APIReference/CreateAlias.md"),
[UpdateAlias](../APIReference/UpdateAlias.md "../APIReference/UpdateAlias.md"), or [DeleteAlias](../APIReference/DeleteAlias.md "../APIReference/DeleteAlias.md"). For details, see [Controlling access to aliases](alias-access.md "alias-access.md").

- To specify multiple KMS keys in the account and Region, use wildcard characters (\*)
  in the Region or resource ID positions of the key ARN.

For example, to specify all KMS keys in the US West (Oregon) Region of an account,
use "`Resource": "arn:aws:kms:us-west-2:111122223333:key/**\***`". To specify all KMS keys in all Regions of the
account, use "`Resource": "arn:aws:kms:**\***:111122223333:key/**\***`".

- To represent all KMS keys, use a wildcard character alone (`"*"`). Use
  this format for operations that don't use any particular KMS key, namely [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md"), [GenerateRandom](../APIReference/API_GenerateRandom.md "../APIReference/API_GenerateRandom.md"), [ListAliases](../APIReference/API_ListAliases.md "../APIReference/API_ListAliases.md"), and [ListKeys](../APIReference/API_ListKeys.md "../APIReference/API_ListKeys.md").
  When writing your policy statements, it's a [best practice](iam-policies-best-practices.md "iam-policies-best-practices.md") to specify only the KMS keys that the principal needs to use, rather
  than giving them access to all KMS keys.

For example, the following IAM policy statement allows the principal to call the [DescribeKey](../APIReference/API_DescribeKey.md "../APIReference/API_DescribeKey.md"), [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md"), [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md") operations only on the KMS keys listed
in the `Resource` element of the policy statement. Specifying KMS keys by key
ARN, which is a best practice, ensures that the permissions are limited only to the specified
KMS keys.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey",
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-west-2:`111122223333`:key/1234abcd-12ab-34cd-56ef-1234567890ab",
 "arn:aws:kms:us-west-2:`111122223333`:key/01234abcd-12ab-34cd-56ef-1234567890ab"
 ]
 }
}`

```

To apply the permission to all KMS keys in a particular trusted AWS account, you can
use wildcard characters (\*) in the Region and key ID positions. For example, the following
policy statement allows the principal to call the specified operations on all KMS keys in
two trusted example accounts.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey",
 "kms:GenerateDataKey",
 "kms:GenerateDataKeyPair"
 ],
 "Resource": [
 "arn:aws:kms:*:`111122223333`:key/*",
 "arn:aws:kms:*:444455556666:key/*"
 ]
 }
}`

```

You can also use a wildcard character (`"*"`) alone in the
`Resource` element. Because it allows access to all KMS keys the account has
permission to use, it's recommended primarily for operations without a particular KMS key
and for `Deny` statements. You can also use it in policy statements that allow only
less sensitive read-only operations. To determine whether an AWS KMS operation involves a
particular KMS key, look for the **KMS key** value in the
**Resources** column of the table in [AWS KMS permissions](kms-api-permissions-reference.md "kms-api-permissions-reference.md").

For example, the following policy statement uses a `Deny` effect to prohibit
the principals from using the specified operations on any KMS key. It uses a wildcard
character in the `Resource` element to represent all KMS keys.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Deny",
 "Action": [
 "kms:CreateKey",
 "kms:PutKeyPolicy",
 "kms:CreateGrant",
 "kms:ScheduleKeyDeletion"
 ],
 "Resource": "*"
 }
}`

```

The following policy statement uses a wildcard character alone to represent all
KMS keys. But it allows only less sensitive read-only operations and operations that don't
apply to any particular KMS key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "kms:CreateKey",
 "kms:ListKeys",
 "kms:ListAliases",
 "kms:ListResourceTags"
 ],
 "Resource": "*"
 }
}`

```
