# Service-linked roles for

Amazon MSK

Amazon MSK uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that
is linked directly to Amazon MSK. Service-linked roles are predefined by Amazon MSK
and include all the permissions that the service requires to call other AWS services on
your behalf.

A service-linked role makes setting up Amazon MSK easier because you do not have to
manually add the necessary permissions. Amazon MSK defines the permissions of its
service-linked roles. Unless defined otherwise, only Amazon MSK can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

For information about other services that support service-linked roles, see [Amazon Web Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md"), and look for the services that have **Yes** in the **Service-Linked Role** column. Choose a
**Yes** with a link to view the service-linked role
documentation for that service.

###### Topics

- [Service-linked role permissions](slr-permissions.md "slr-permissions.md")
- [Create a service-linked role](create-slr.md "create-slr.md")
- [Edit a service-linked role](edit-slr.md "edit-slr.md")
- [Supported Regions for service-linked roles](slr-regions.md "slr-regions.md")
