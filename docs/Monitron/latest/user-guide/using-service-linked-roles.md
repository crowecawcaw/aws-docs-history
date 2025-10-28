Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Using service-linked roles for

Amazon Monitron

Amazon Monitron uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM
role that is linked directly to Amazon Monitron. Service-linked roles are predefined
by Amazon Monitron and include all the permissions that the service requires to call
other AWS services on your behalf.

A service-linked role makes setting up Amazon Monitron easier because you don’t have
to manually add the necessary permissions. Amazon Monitron defines the permissions of
its service-linked roles, and unless defined otherwise, only Amazon Monitron can
assume its roles. The defined permissions include the trust policy and the
permissions policy, and that permissions policy cannot be attached to any other
IAM entity.

For information about other services that support service-linked roles, see [AWS
services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have
**Yes** in the **Service-linked
roles** column. Choose a **Yes** with a
link to view the service-linked role documentation for that service.

###### Topics

- [Service-linked role permissions for
  Amazon Monitron](slr-permissions.md "slr-permissions.md")
- [Creating a service-linked role for
  Amazon Monitron](create-slr.md "create-slr.md")
- [Editing a service-linked role for
  Amazon Monitron](edit-slr.md "edit-slr.md")
- [Deleting a service-linked role for
  Amazon Monitron](delete-slr.md "delete-slr.md")
- [Supported regions for Amazon Monitron service-linked
  roles](slr-regions.md "slr-regions.md")
- [AWS managed policies for
  Amazon Monitron](monitron-managed-policies.md "monitron-managed-policies.md")
- [Amazon Monitron updates to AWS managed
  policies](managed-policy-updates.md "managed-policy-updates.md")
