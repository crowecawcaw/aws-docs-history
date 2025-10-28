# Using service-linked roles for

AWS KMS

AWS Key Management Service uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS KMS. Service-linked roles are defined by AWS KMS and include all the
permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up AWS KMS easier because you don’t have to manually add
the necessary permissions. AWS KMS defines the permissions of its service-linked roles, and unless
defined otherwise, only AWS KMS can assume its roles. The defined permissions include the trust
policy and the permissions policy, and that permissions policy cannot be attached to any other
IAM entity.

You can delete a service-linked role only after first deleting the related resources. This
protects your AWS KMS resources because you can't inadvertently remove permission to access the
resources.

For information about other services that support service-linked roles, see [AWS Services That Work
with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in
the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that
service.

To view details about updates to the service-linked roles discussed in this topic, see [AWS KMS updates to AWS managed
policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates").

###### Topics

- [Authorizing AWS KMS to manage AWS CloudHSM and Amazon EC2 resources](authorize-kms.md "authorize-kms.md")
- [Authorizing AWS KMS to synchronize multi-Region
  keys](multi-region-auth-slr.md "multi-region-auth-slr.md")
