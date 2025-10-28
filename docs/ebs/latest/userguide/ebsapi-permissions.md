# Control access to EBS direct APIs using IAM

A user must have the following policies to use the EBS direct APIs. For more
information, see [Changing permissions for a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md "../../../IAM/latest/UserGuide/id_users_change-permissions.md").

For more information about the EBS direct APIs resources, actions, and condition context keys for
use in IAM permission policies, see [Actions, resources, and condition keys for Amazon Elastic Block Store](../../../service-authorization/latest/reference/list_amazonelasticblockstore.md "../../../service-authorization/latest/reference/list_amazonelasticblockstore.md") in the _Service Authorization Reference_.

###### Important

Be cautious when assigning the following policies to users. By assigning
these policies, you might give access to a user who is denied access to the same resource through
the Amazon EC2 APIs, such as the CopySnapshot or CreateVolume actions.

The following policy allows the _read_ EBS direct APIs to be used on all
snapshots in a specific AWS Region. In the policy, replace
`<Region>` with the Region of the snapshot.

The following policy allows the _read_ EBS direct APIs to be used on
snapshots with a specific key-value tag. In the policy, replace
`<Key>` with the key value of the tag, and
`<Value>` with the value of the tag.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ebs:ListSnapshotBlocks",
 "ebs:ListChangedBlocks",
 "ebs:GetSnapshotBlock"
 ],
 "Resource": "arn:aws:ec2:*::snapshot/*",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "aws:ResourceTag/`<Key>`": "`<Value>`"
 }
 }
 }
 ]
}`

```

The following policy allows all of the _read_ EBS direct APIs to be used
on all snapshots in the account only within a specific time range. This policy authorizes
use of the EBS direct APIs based on the `aws:CurrentTime` global condition key. In
the policy, be sure to replace the date and time range shown with the date and time range
for your policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ebs:ListSnapshotBlocks",
 "ebs:ListChangedBlocks",
 "ebs:GetSnapshotBlock"
 ],
 "Resource": "arn:aws:ec2:*::snapshot/*",
 "Condition": {
 "DateGreaterThan": {
 "aws:CurrentTime": "`2018-05-29T00:00:00Z`"
 },
 "DateLessThan": {
 "aws:CurrentTime": "`2020-05-29T23:59:59Z`"
 }
 }
 }
 ]
}`

```

For more information, see [Changing permissions for a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md "../../../IAM/latest/UserGuide/id_users_change-permissions.md") in the _IAM User Guide_.

The following policy allows the _write_ EBS direct APIs to be used on all
snapshots in a specific AWS Region. In the policy, replace
`<Region>` with the Region of the snapshot.

The following policy allows the _write_ EBS direct APIs to be used on
snapshots with a specific key-value tag. In the policy, replace
`<Key>` with the key value of the tag, and
`<Value>` with the value of the tag.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ebs:StartSnapshot",
 "ebs:PutSnapshotBlock",
 "ebs:CompleteSnapshot"
 ],
 "Resource": "arn:aws:ec2:*::snapshot/*",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "aws:ResourceTag/`<Key>`": "`<Value>`"
 }
 }
 }
 ]
}`

```

The following policy allows all of the EBS direct APIs to be used. It also allows the
`StartSnapshot` action only if a parent snapshot ID is specified. Therefore,
this policy blocks the ability to start new snapshots without using a parent
snapshot.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ebs:*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "ebs:ParentSnapshot": "arn:aws:ec2:*::snapshot/*"
 }
 }
 }
 ]
}`

```

The following policy allows all of the EBS direct APIs to be used. It also allows only the
`user` tag key to be created for a new snapshot. This policy also ensures
that the user has access to create tags. The `StartSnapshot` action is the only
action that can specify tags.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ebs:*",
 "Resource": "*",
 "Condition": {
 "ForAllValues:StringEquals": {
 "aws:TagKeys": "user"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:CreateTags",
 "Resource": "*"
 }
 ]
}`

```

The following policy allows all of the _write_ EBS direct APIs to be used
on all snapshots in the account only within a specific time range. This policy authorizes
use of the EBS direct APIs based on the `aws:CurrentTime` global condition key. In
the policy, be sure to replace the date and time range shown with the date and time range
for your policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ebs:StartSnapshot",
 "ebs:PutSnapshotBlock",
 "ebs:CompleteSnapshot"
 ],
 "Resource": "arn:aws:ec2:*::snapshot/*",
 "Condition": {
 "DateGreaterThan": {
 "aws:CurrentTime": "`2018-05-29T00:00:00Z`"
 },
 "DateLessThan": {
 "aws:CurrentTime": "`2020-05-29T23:59:59Z`"
 }
 }
 }
 ]
}`

```

For more information, see [Changing permissions for a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md "../../../IAM/latest/UserGuide/id_users_change-permissions.md") in the
_IAM User Guide_.

The following policy grants permission to decrypt an encrypted snapshot using a specific
KMS key. It also grants permission to encrypt new snapshots using the default KMS key for
EBS encryption. In the policy, replace `<Region>` with the
Region of the KMS key, `<AccountId>` with the ID of the AWS
account of the KMS key, and `<KeyId>` with the ID of the
KMS key.

###### Note

By default, all principals in the account have access to the default AWS managed KMS key
for Amazon EBS encryption, and they can use it for EBS encryption and decryption operations. If you
are using a customer managed key, you must create a new key policy or modify the existing key policy for
the customer managed key to grant the principal access to the customer managed key. For more information, see
[Key policies in
AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS Key Management Service Developer Guide_.

###### Tip

To follow the principle of least privilege, do not allow full access to `kms:CreateGrant`.
Instead, use the `kms:GrantIsForAWSResource` condition key to allow the user to create grants
on the KMS key only when the grant is created on the user's behalf by an AWS service, as shown in
the following example.

For more information, see [Changing permissions for a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md "../../../IAM/latest/UserGuide/id_users_change-permissions.md") in the
_IAM User Guide_.
