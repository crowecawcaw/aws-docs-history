AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Using Service-Linked Roles for

Migration Hub

AWS Migration Hub uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that
is linked directly to Migration Hub. Service-linked roles are predefined by Migration Hub
and include all the permissions that the service requires to call other AWS services on
your behalf.

A service-linked role makes setting up Migration Hub easier because you don't have to
manually add the necessary permissions. Migration Hub defines the permissions of its
service-linked roles, and the services that can assume its roles. The permissions include
the trust policy and the permissions policy, which cannot be attached to any other IAM
entity.

For information about other services that support service-linked roles, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in
the **Service-Linked Role** column. Choose a **Yes** with
a link to view the service-linked role documentation for that service.

###### Topics

- [Using Roles to Connect Migration Hub to Application Discovery Service](using-service-linked-roles-discovery-service-role.md "using-service-linked-roles-discovery-service-role.md")
- [Using Roles to Connect Migration Hub to AWS DMS](using-service-linked-roles-dms-service-role.md "using-service-linked-roles-dms-service-role.md")
