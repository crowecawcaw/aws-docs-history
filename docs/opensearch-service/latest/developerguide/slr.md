# Using service-linked roles for Amazon OpenSearch Service

Amazon OpenSearch Service uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that
is linked directly to OpenSearch Service. Service-linked roles are predefined by OpenSearch Service
and include all the permissions that the service requires to call other AWS services on
your behalf.

A service-linked role makes setting up OpenSearch Service easier because you don’t have to
manually add the necessary permissions. OpenSearch Service defines the permissions of its
service-linked roles, and unless defined otherwise, only OpenSearch Service can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity. For updates to
service-linked roles and permissions policies, see [Document
history for Amazon OpenSearch Service](release-notes.md "release-notes.md").

For information about other services that support service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column. Choose a
**Yes** with a link to view the service-linked role
documentation for that service.

###### Topics

- [Using service-linked roles to create VPC domains and direct
  query data sources](slr-aos.md "slr-aos.md")
- [Using service-linked roles to create
  OpenSearch Serverless collections](serverless-service-linked-roles.md "serverless-service-linked-roles.md")
- [Using service-linked roles to create OpenSearch Ingestion
  pipelines](slr-osis.md "slr-osis.md")
