# Resource-level permissions

You can restrict the scope of permissions by specifying resources in an IAM policy. Many AWS CLI API actions support a resource type that
varies depending on the behavior of the action.

Every IAM policy statement grants permission to an action that's performed on a resource. When the action doesn't act on a named resource,
or when you grant permission to perform the action on all resources, the value of the resource in the policy is a wildcard (\*).
For many API actions, you can restrict the resources that a user can modify by specifying the Amazon Resource Name (ARN) of a resource, or an ARN pattern that matches multiple resources.

To restrict permissions by resource, specify the resource by ARN.

**MemoryDB Resource ARN Format**

###### Note

For resource-level permissions to be effective, the resource name on the ARN string should be lower case.

- User – arn:aws:memorydb:`us-east-1:123456789012`:user/user1
- ACL – arn:aws:memorydb:`us-east-1:123456789012`:acl/my-acl
- Cluster – arn:aws:memorydb:`us-east-1:123456789012`:cluster/my-cluster
- Snapshot – arn:aws:memorydb:`us-east-1:123456789012`:snapshot/my-snapshot
- Parameter group – arn:aws:memorydb:`us-east-1:123456789012`:parametergroup/my-parameter-group
- Subnet group – arn:aws:memorydb:`us-east-1:123456789012`:subnetgroup/my-subnet-group

###### Examples

- [Example 1: Allow a user full access to specific MemoryDB resource types](#example-allow-list-current-memorydb-resources-resource "#example-allow-list-current-memorydb-resources-resource")
- [Example 2: Deny a user access to a cluster.](#example-allow-specific-memorydb-actions-resource "#example-allow-specific-memorydb-actions-resource")

## Example 1: Allow a user full access to specific MemoryDB resource types

The following policy explicitly allows the specified `account-id` full access to all resources of type subnet group, security group and cluster.

```
{
        "Sid": "Example1",
        "Effect": "Allow",
        "Action": "memorydb:*",
        "Resource": [
             "arn:aws:memorydb:us-east-1:`account-id`:subnetgroup/*",
             "arn:aws:memorydb:us-east-1:`account-id`:securitygroup/*",
             "arn:aws:memorydb:us-east-1:`account-id`:cluster/*"
        ]
}
```

## Example 2: Deny a user access to a cluster.

The following example explicitly denies the specified `account-id` access to a particular cluster.

```
{
        "Sid": "Example2",
        "Effect": "Deny",
        "Action": "memorydb:*",
        "Resource": [
                "arn:aws:memorydb:us-east-1:`account-id`:cluster/`name`"
        ]
}
```
