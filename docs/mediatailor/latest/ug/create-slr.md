# Creating a service-linked role for MediaTailor

You don't need to manually create a service-linked role. When you
enable session logging in the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the AWS API,
MediaTailor creates the service-linked role for you.

###### Important

This service-linked role can appear in your account if you completed an action in
another service that uses the features supported by this role. Also, if you were using the
MediaTailor service before September 15, 2021, when it began supporting service-linked roles,
then MediaTailor created the AWSServiceRoleForMediaTailor role in your account. To learn more, see [A
New Role Appeared in My IAM Account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you enable session logging,
MediaTailor creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the
**MediaTailor** use case. In the AWS CLI or the AWS API, create a
service-linked role with the `mediatailor.amazonaws.com` service name. For more
information, see [Creating a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you
delete this service-linked role, you can use this same process to create the role
again.
