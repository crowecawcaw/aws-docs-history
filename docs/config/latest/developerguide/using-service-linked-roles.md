# Using Service-Linked Roles for AWS Config

AWS Config uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS Config. Service-linked roles are predefined by AWS Config and include all the
permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up AWS Config easier because you don't have to manually add
the necessary permissions. AWS Config defines the permissions of its service-linked roles, and unless
defined otherwise, only AWS Config can assume its roles. The defined permissions include the trust
policy and the permissions policy, and that permissions policy cannot be attached to any other
IAM entity.

You can delete a service-linked role only after first deleting its related resources. This
protects your AWS Config resources because you can't inadvertently remove permission to access the
resources.

For information about other services that support service-linked roles, see [AWS Services That Work
with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in
the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that
service.

###### Topics

- [Using Service-Linked Roles for AWS Config](using-service-linked-roles-config.md "using-service-linked-roles-config.md")
- [Using Service-Linked Roles for Third-Party Cloud Integrations](using-service-linked-roles-config-third-party.md "using-service-linked-roles-config-third-party.md")
