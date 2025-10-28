End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Using service-linked roles for

AWS Proton

AWS Proton uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS Proton. Service-linked roles are predefined by AWS Proton and
include all the permissions that the service requires to call other AWS services on your
behalf.

###### Topics

- [Using roles for AWS Proton sync](using-service-linked-roles-sync.md "using-service-linked-roles-sync.md")
- [Using roles for CodeBuild-based provisioning](using-service-linked-roles-codebuild.md "using-service-linked-roles-codebuild.md")
