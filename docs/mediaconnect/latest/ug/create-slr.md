# Creating a service-linked role for MediaConnect

You don't need to manually create a service-linked role. When you
create an associated MediaConnect resource in the AWS Management Console, the AWS CLI, or the AWS API, MediaConnect
creates the service-linked role for you.

###### Important

This service-linked role can appear in your account if you completed an action in
another service that uses the features supported by this role. Also, if you were using the
MediaConnect service before January 1, 2023, when it began supporting service-linked roles,
then MediaConnect created the AWSServiceRoleForMediaConnect role in your account. To learn more, see [A new
role appeared in my IAM account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you create an associated MediaConnect resource,
MediaConnect creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the
**MediaConnect** use case. In the AWS CLI or the AWS API, create
a service-linked role with the `MediaConnect` service name. For more
information, see [Creating a
service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you delete this
service-linked role, you can use this same process to create the role again.
