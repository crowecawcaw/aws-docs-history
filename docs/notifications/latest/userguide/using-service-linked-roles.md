# Using Service-Linked Roles for

User Notifications

AWS User Notifications uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that
is linked directly to User Notifications. Service-linked roles are predefined by User Notifications
and include all the permissions that the service requires to call other AWS services on
your behalf.

A service-linked role streamlines setting up User Notifications because you don’t have to
manually add the necessary permissions. User Notifications defines the permissions of its
service-linked roles. Unless defined otherwise, only User Notifications can assume its roles.
The defined permissions include the trust policy and the permissions policy. That
permissions policy can't be attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS Services
That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-Linked Role** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

###### Topics

- [AWS User Notifications service-Linked Role for calling AWS services, publishing metrics, and using AWS Organizations](slr-call-services.md "slr-call-services.md")
- [Supported Regions for
  User Notifications Service-Linked Roles](#slr-regions "#slr-regions")
- [Amazon EventBridge managed rules in AWS User Notifications](ev-managed-rules.md "ev-managed-rules.md")

## Supported Regions for

User Notifications Service-Linked Roles

User Notifications supports using service-linked roles in all of the Regions where the service
is available. For more information, see [AWS Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
