# Using service-linked roles for

Security Lake

Security Lake uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A
service-linked role is an IAM role that's linked directly to Security Lake. It's predefined by
Security Lake, and it includes all the permissions that Security Lake requires to call other AWS services
on your behalf and operate the security data lake service. Security Lake uses this service-linked role in all
the AWS Regions where Security Lake is available.

The service-linked role eliminates the need to manually add
the necessary permissions when setting up Security Lake. Security Lake defines the permissions of this service-linked role, and
unless defined otherwise, only Security Lake can assume the role. The defined permissions include the
trust policy and the permissions policy, and that permissions policy can't be attached to any
other IAM entity.

You must configure permissions to allow an IAM entity (such as a user, group, or role) to
create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_. You
can delete a service-linked role only after you delete its related resources. This protects
your resources because you can't inadvertently remove permission to access the
resources.

For information about other services that support service-linked roles, see [AWS services that work with
IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the
**Service-linked roles** column. Choose a **Yes** with a link to review the service-linked role documentation for that
service.

###### Topics

- [Service-linked role (SLR) permissions for Security Lake](slr-permissions.md "slr-permissions.md")
- [Service-linked role (SLR) permissions for resource management](AWSServiceRoleForSecurityLakeResourceManagement.md "AWSServiceRoleForSecurityLakeResourceManagement.md")
