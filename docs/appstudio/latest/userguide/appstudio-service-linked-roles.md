# Service-linked roles for

App Studio

App Studio uses [AWS Identity and Access Management (IAM) service-linked roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md"). A service-linked role
is a unique type of IAM role that is linked directly to App Studio. Service-linked roles are predefined by App Studio and include all the permissions that
the service requires to call other AWS services on your behalf.

A service-linked role makes setting up App Studio easier because you don’t have to manually add the necessary permissions.
App Studio defines the permissions of its service-linked roles, and unless defined otherwise, only App Studio can assume its
roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be
attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your App Studio
resources because you can't inadvertently remove permission to access the resources.

###### Contents

- [Service-linked role permissions for App Studio](#slr-permissions "#slr-permissions")
- [Creating a service-linked role for App Studio](#create-slr "#create-slr")
- [Editing a service-linked role for App Studio](#edit-slr "#edit-slr")
- [Deleting a service-linked role for App Studio](#delete-slr "#delete-slr")

## Service-linked role permissions for App Studio

App Studio uses the service-linked role named `AWSServiceRoleForAppStudio`. It's a service-linked role
required for App Studio to persistently manage AWS services, to maintain the application building experience.

The `AWSServiceRoleForAppStudio` service-linked role uses the following trust policy, which only
trusts the `appstudio-service.amazonaws.com` service:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "appstudio-service.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

For permissions, the `AWSServiceRoleForAppStudio` service-linked role provides permissions to the following services:

- Amazon CloudWatch: To send logs and metrics for App Studio usage.
- AWS Secrets Manager: To manage credentials for connectors in App Studio, used to connect apps to other services.
- IAM Identity Center: To read-only access to manage user access.

Specifically, the permissions granted with `AWSServiceRoleForAppStudio` are defined by the attached
`AppStudioServiceRolePolicy` managed policy. For more information about the managed policy, including the permissions it includes, see
[AWS managed policy: AppStudioServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-appstudioservicerolepolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-appstudioservicerolepolicy").

## Creating a service-linked role for App Studio

You don't need to manually create a service-linked role. When you create an App Studio
instance, App Studio creates the service-linked role for you.

If you delete this service-linked role, it is recommended to create an App Studio instance to
have another one automatically created for you.

While not neccesary, you can also use the IAM console or AWS CLI to create service-linked roles by creating
a service-linked role with the `appstudio-service.amazonaws.com` service name, as in the trust policy snippet shown earlier.
For more information, see
[Creating a service-linked role](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md") in
the _IAM User Guide_.

## Editing a service-linked role for App Studio

App Studio doesn't allow you to edit the `AWSServiceRoleForAppStudio` service-linked role. After
you create a service-linked role, you can't change the name of the role because various
entities might reference the role. However, you can edit the description of the role by
using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for App Studio

You don't need to delete the `AWSServiceRoleForAppStudio` role. When you delete
the App Studio instance, App Studio cleans up the resources and deletes the service-linked role automatically.

While not recommended, you can use the IAM console or the AWS CLI to delete the service-linked role.
To do this, you must first clean up the resources for your service-linked role and then you can delete it.

###### Note

If App Studio is using the role when you try to delete the resources, then the deletion might fail.
If that happens, wait for a few minutes and try the operation again.

###### To manually delete the service-linked role using IAM

1. Delete the applications and connectors from your App Studio instance.
2. Use the IAM console, the IAM CLI, or the IAM API to delete the
   `AWSServiceRoleForAppStudio` service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
   _IAM User Guide_.
