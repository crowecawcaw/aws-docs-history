# Using tags with Amazon FSx

You can use tags to control access to Amazon FSx resources and to implement attribute-based
access control (ABAC). To apply tags to Amazon FSx resources during creation, users must have certain
AWS Identity and Access Management (IAM) permissions.

## Grant permission to tag resources during creation

With some resource-creating Amazon FSx API actions, you can specify tags when you
create the resource. You can use these resource tags to implement attribute-based access
control (ABAC). For more information, see [What is ABAC
for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

For users to tag resources on creation, they must have permission to use the action that
creates the resource, such as `fsx:CreateFileSystem`,
`fsx:CreateStorageVirtualMachine`, or `fsx:CreateVolume`. If tags are
specified in the resource-creating action, IAM performs additional authorization on the
`fsx:TagResource` action to verify if users have permissions to create tags.
Therefore, users must also have explicit permissions to use the `fsx:TagResource`
action.

The following example policy allows users to create file systems and storage virtual
machines (SVMs) and apply tags to them during creation in a specific AWS account.

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
         "fsx:CreateFileSystem",
         "fsx:CreateStorageVirtualMachine",
         "fsx:TagResource"
      ],
      "Resource": [
         "arn:aws:fsx:`region`:`account-id`:file-system/*",
         "arn:aws:fsx:`region`:`account-id`:file-system/*/`storage-virtual-machine`/*"
      ]
    }
  ]
}
```

Similarly, the following policy allows users to create backups on a specific file system and apply any tags
to the backup during backup creation.

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
         "fsx:CreateBackup"
      ],
      "Resource": "arn:aws:fsx:`region`:`account-id`:file-system/`file-system-id`*"
    },
    {
      "Effect": "Allow",
      "Action": [
         "fsx:TagResource"
      ],
      "Resource": "arn:aws:fsx:`region`:`account-id`:backup/*"
    }
  ]
}
```

The `fsx:TagResource` action is evaluated only if tags are applied during the
resource-creating action. Therefore, a user who has permissions to create a resource (assuming
there are no tagging conditions) does not require permission to use the
`fsx:TagResource` action if no tags are specified in the request. However, if the
user attempts to create a resource with tags, the request fails if the user does not have
permissions to use the `fsx:TagResource` action.

For more information about tagging Amazon FSx resources, see [Tagging Amazon FSx resources](tag-resources.md "tag-resources.md"). For more information about using tags to control access to
Amazon FSx resources, see [Using tags to control access to your Amazon FSx
resources](#restrict-fsx-access-tags "#restrict-fsx-access-tags").

## Using tags to control access to your Amazon FSx

resources

To control access to Amazon FSx resources and actions, you can use IAM policies based on tags.
You can provide this control in two ways:

- You can control access to Amazon FSx resources based on the tags on those resources.
- You can control which tags can be passed in an IAM request condition.

For information about how to use tags to control access to AWS resources, see
[Controlling access using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the
_IAM User Guide_. For more information about tagging Amazon FSx resources at creation,
see [Grant permission to tag resources during creation](#supported-iam-actions-tagging "#supported-iam-actions-tagging"). For
more information about tagging resources, see [Tagging Amazon FSx resources](tag-resources.md "tag-resources.md").

### Controlling access based on tags on a resource

To control which actions a user or role can perform on an Amazon FSx resource, you can use tags
on the resource. For example, you might want to allow or deny specific API operations on a
file system resource based on the key-value pair of the tag on the resource.

###### Example policy – Create a file system only when a specific tag is used

This policy allows the user to create a file system only when they tag it with a
specific tag key-value pair, in this example, `key=Department`,
`value=Finance`.

```
{
    "Effect": "Allow",
    "Action": [
        "fsx:CreateFileSystem",
        "fsx:TagResource"
    ],
    "Resource": "arn:aws:fsx:`region`:`account-id`:file-system/*",
    "Condition": {
        "StringEquals": {
            "aws:RequestTag/Department": "Finance"
        }
    }
}
```

###### Example policy – Create backups only of Amazon FSx for NetApp ONTAP volumes with a specific

tag

This policy allows users to create backups only of FSx for ONTAP volumes that are tagged
with the key-value pair `key=Department`, `value=Finance`. The
backup is created with the tag `Department=Finance`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "fsx:CreateBackup"
 ],
 "Resource": "arn:aws:fsx:`us-east-1`:`111122223333`:volume/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Department": "Finance"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "fsx:TagResource",
 "fsx:CreateBackup"
 ],
 "Resource": "arn:aws:fsx:`us-east-1`:`111122223333`:backup/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/Department": "Finance"
 }
 }
 }
 ]
}`

```

###### Example policy – Create a volume with a specific tag from backups with a specific tag

This policy allows users to create volumes that are tagged with `Department=Finance` only
from backups that are tagged with `Department=Finance`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "fsx:CreateVolumeFromBackup",
 "fsx:TagResource"
 ],
 "Resource": "arn:aws:fsx:`us-east-1`:`111122223333`:volume/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/Department": "Finance"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "fsx:CreateVolumeFromBackup"
 ],
 "Resource": "arn:aws:fsx:`us-east-1`:`111122223333`:backup/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Department": "Finance"
 }
 }
 }
 ]
}`

```

###### Example policy – Delete file systems with specific tags

This policy allows a user to delete only file systems that are tagged with `Department=Finance`.
If they create a final backup, then it must be tagged with `Department=Finance`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "fsx:DeleteFileSystem"
 ],
 "Resource": "arn:aws:fsx:`us-east-1`:`111122223333`:file-system/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Department": "Finance"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "fsx:TagResource"
 ],
 "Resource": "arn:aws:fsx:`us-east-1`:`111122223333`:backup/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/Department": "Finance"
 }
 }
 }
 ]
}`

```

###### Example policy – Delete a volume with specific tags

This policy allows a user to delete only volumes that are tagged with `Department=Finance`.
If they create a final backup, then it must be tagged with `Department=Finance`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "fsx:DeleteVolume"
 ],
 "Resource": "arn:aws:fsx:`us-east-1`:`111122223333`:volume/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Department": "Finance"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "fsx:TagResource"
 ],
 "Resource": "arn:aws:fsx:`us-east-1`:`111122223333`:backup/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/Department": "Finance"
 }
 }
 }
 ]
}`

```
