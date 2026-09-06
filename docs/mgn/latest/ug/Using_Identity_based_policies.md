

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Using identity-based policies
<a name="Using_Identity_based_policies"></a>

By default, users and roles don't have permission to create or modify AWS Transform MGN resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or AWS API. An IAM administrator must create IAM policies that grant users and roles permission to perform specific API operations on the specified resources they need. The administrator must then attach those policies to the users or groups that require those permissions. To understand how to attach policies to a user or group, learn about [adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html). To learn how to create an IAM identity-based policy using example JSON policy documents, see [Creating policies on the JSON tab in the IAM User Guide.](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor) 

**Topics**
+ [Customer-managed policies in MGN](customer_managed_policies_mgn.md)
+ [Restrict permission to act on a source server associated with given AWS vCenter client](restrict-to-vcenter-client.md)
+ [Network Migration API permissions](network-migration-api-permissions.md)