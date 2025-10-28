# Using service-linked roles for

Amazon Keyspaces

Amazon Keyspaces (for Apache Cassandra) uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Amazon Keyspaces. Service-linked roles are predefined by Amazon Keyspaces and
include all the permissions that the service requires to call other AWS services on your
behalf.

For information about other services that support service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column. Choose a
**Yes** with a link to view the service-linked role
documentation for that service.

###### Topics

- [Using roles for Amazon Keyspaces application auto scaling](using-service-linked-roles-app-auto-scaling.md "using-service-linked-roles-app-auto-scaling.md")
- [Using roles for Amazon Keyspaces Multi-Region Replication](using-service-linked-roles-multi-region-replication.md "using-service-linked-roles-multi-region-replication.md")
- [Using roles for Amazon Keyspaces CDC streams](using-service-linked-roles-CDC-streams.md "using-service-linked-roles-CDC-streams.md")
