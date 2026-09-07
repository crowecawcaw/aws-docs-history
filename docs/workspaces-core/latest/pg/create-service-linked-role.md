

# Create a Service-Linked Role
<a name="create-service-linked-role"></a>

WorkSpaces Core Managed Instances require an IAM service-linked role. This role:
+ Contains predefined trust and permissions policies.
+ Can only be assumed by WorkSpaces Instances.
+ Must be removed after associated resources are deleted.

For more information on service linked roles, see [Using service-linked roles for Amazon WorkSpaces Instances](https://docs.aws.amazon.com/workspaces-core/latest/ag/using-service-linked-roles.html)