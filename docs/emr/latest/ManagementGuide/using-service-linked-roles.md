# Using service-linked roles for

Amazon EMR

Amazon EMR uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Amazon EMR. Service-linked roles are predefined by Amazon EMR and
include all the permissions that the service requires to call other AWS services on your
behalf.

###### Topics

- [Using service-linked roles for Amazon EMR for
  cleanup](using-service-linked-roles-cleanup.md "using-service-linked-roles-cleanup.md")
- [Using service-linked roles with Amazon EMR for write-ahead
  logging](using-service-linked-roles-wal.md "using-service-linked-roles-wal.md")
  For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles**
  column. Choose a **Yes** with a link to view the service-linked
  role documentation for that service.
