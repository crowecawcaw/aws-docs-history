End of support notice: On May 31, 2026, AWS will end support for
AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama
resources. For more information, see [AWS Panorama end of support](panorama-end-of-support.md "panorama-end-of-support.md").

# AWS Panorama permissions

You can use AWS Identity and Access Management (IAM) to manage access to the AWS Panorama service and resources like appliances and
applications. For users in your account that use AWS Panorama, you manage permissions in a permissions policy that you can
apply to IAM roles. To manage permissions for an application, you create a role and assign it to the
application.

To [manage permissions for users](permissions-user.md "permissions-user.md") in your account, use the managed policy
that AWS Panorama provides, or write your own. You need permissions to other AWS services to get application and
appliance logs, view metrics, and assign a role to an application.

An AWS Panorama Appliance also has a role that grants it permission to access AWS services and resources. The appliance's
role is one of the [service roles](permissions-services.md "permissions-services.md") that the AWS Panorama service uses to access
other services on your behalf.

An [application role](permissions-application.md "permissions-application.md") is a separate service role that you create
for an application, to grant it permission to use AWS services with the AWS SDK for Python (Boto). To create an application
role, you need administrative privileges or the help of an administrator.

You can restrict user permissions by the resource an action affects and, in some cases, by additional
conditions. For example, you can specify a pattern for the Amazon Resource Name (ARN) of an application that
requires a user to include their user name in the name of applications that they create. For the resources and
conditions that are supported by each action, see [Actions,
resources, and condition keys for AWS Panorama](../../../service-authorization/latest/reference/list_awspanorama.md "../../../service-authorization/latest/reference/list_awspanorama.md") in the Service Authorization Reference.

For more information, see [What is IAM?](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md") in the IAM User Guide.

###### Topics

- [Identity-based IAM policies for AWS Panorama](permissions-user.md "permissions-user.md")
- [AWS Panorama service roles and cross-service resources](permissions-services.md "permissions-services.md")
- [Granting permissions to an application](permissions-application.md "permissions-application.md")
