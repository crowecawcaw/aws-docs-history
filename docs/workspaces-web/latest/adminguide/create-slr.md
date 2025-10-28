# Creating a service-linked role for WorkSpaces Secure Browser

You don't need to manually create a service-linked role. When you create your first portal in the
AWS Management Console, the AWS CLI, or the AWS API, WorkSpaces Secure Browser creates the service-linked role for you.

###### Important

This service-linked role can appear in your account if you completed an action in
another service that uses the features supported by this role.

If you delete this service-linked role and later need to create it again, you can use the
same process to recreate the role in your account. When you create your first portal, WorkSpaces Secure Browser
creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the
**WorkSpaces Secure Browser** use case. In the AWS CLI or the AWS API, create
a service-linked role with the `workspaces-web.amazonaws.com` service name. For more
information, see [Creating a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you delete this
service-linked role, you can use this same process to create the role again.
