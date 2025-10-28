# Using tags with Amazon EFS

You can use tags to control access to Amazon EFS resources and to implement
attribute-based access control (ABAC). For more information, see:

- [Tagging EFS resources](manage-fs-tags.md "manage-fs-tags.md")
- [Controlling access based on tags on a resource](#resource-tag-control "#resource-tag-control")
- [What is ABAC
  for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_

###### Note

Amazon EFS replication does not support using tags for attribute-based access control
(ABAC).

To apply tags to Amazon EFS resources during creation, users must have certain AWS Identity and Access Management
(IAM) permissions.

## Granting permissions to tag resources during

creation

The following tag-on create Amazon EFS API actions allow you to specify tags when you
create the resource.

- `CreateAccessPoint`
- `CreateFileSystem`

To enable users to tag resources on creation, they must have permissions to use the
action that creates the resources, such as `elasticfilesystem:CreateAccessPoint` or
`elasticfilesystem:CreateFileSystem`. If tags are specified in the
resource-creating action, AWS performs additional authorization on the
`elasticfilesystem:TagResource` action to verify if users have permission to
create tags. Therefore, users must also have explicit permissions to use the
`elasticfilesystem:TagResource` action.

In the IAM policy definition for the `elasticfilesystem:TagResource`
action, use the `Condition` element with the
`elasticfilesystem:CreateAction` condition key to give tagging permissions to the
action that creates the resource.

###### Example policy: Allow adding tags to file systems only at the time of creation

The following example policy allows users to create file systems and apply tags to them
only during creation. Users are not permitted to tag any existing resources (they cannot
call the `elasticfilesystem:TagResource` action directly).

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
         "elasticfilesystem:CreateFileSystem"
      ],
      "Resource": "arn:aws:elasticfilesystem:`region`:`account-id`:file-system/*"
    },
    {
      "Effect": "Allow",
      "Action": [
         "elasticfilesystem:TagResource"
      ],
      "Resource": "arn:aws:elasticfilesystem:`region`:`account-id`:file-system/*",
      "Condition": {
         "StringEquals": {
             "elasticfilesystem:CreateAction": "CreateFileSystem"
          }
       }
    }
  ]
}
```

## Using tags to control access to your Amazon EFS

resources

To control access to Amazon EFS resources and actions, you can use IAM policies based on tags.
You can provide this control in two ways:

- You can control access to Amazon EFS resources based on the tags on those resources.
- You can control which tags can be passed in an IAM request condition.

For information about how to use tags to control access to AWS resources, see [Controlling access using
tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User Guide_.

## Controlling access based on tags on a resource

To control which actions a user or role can perform on an Amazon EFS resource, you can use tags
on the resource. For example, you might want to allow or deny specific API operations on a
file system resource based on the key-value pair of the tag on the resource.

###### Example policy: Create a file system only when a specific tag is used

The following example policy allows the user to create a file system only when they tag
it with a specific tag key-value pair, in this example, `key=Department`,
`value=Finance`.

```
{
    "Effect": "Allow",
    "Action": [
        "elasticfilesystem:CreateFileSystem",
        "elasticfilesystem:TagResource"
    ],
    "Resource": "arn:aws:elasticfilesystem:`region`:`account-id`:file-system/*",
    "Condition": {
        "StringEquals": {
            "aws:RequestTag/Department": "Finance"
        }
    }
}
```

###### Example policy: Delete file systems with specific tags

The following example policy allows a user to delete only file systems that are tagged
with `Department=Finance`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticfilesystem:DeleteFileSystem"
 ],
 "Resource": "arn:aws:elasticfilesystem:`us-east-1`:`111122223333`:file-system/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Department": "Finance"
 }
 }
 }
 ]
}`

```
