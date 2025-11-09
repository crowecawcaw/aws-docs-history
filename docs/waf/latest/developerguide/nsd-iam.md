**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Identity and Access Management for AWS Shield network security director

###### Note

AWS Shield network security director is in public preview release and is subject to change.

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_ (have permissions) to use AWS Shield network security director resources. IAM is an AWS service that you can use with no additional charge.

Review the guidance in this section to understand how to use supported policies and roles for AWS Shield network security director.

## How AWS Shield network security director works with IAM

This section explains how to use the features of IAM with AWS Shield network security director.

Before you use IAM to manage access to network security director, learn what IAM features are
available to use with network security director.

| IAM features you can use with AWS Shield network security director                                                            | IAM feature | AWS Shield network security director support |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------- | -------------------------------------------- |
| [Identity-based policies](#iam_nsd-with-iam-id-based-policies "#iam_nsd-with-iam-id-based-policies")                          | Yes         |
| [Service-linked roles](security_iam_nsd-with-iam-roles-service-linked.md "security_iam_nsd-with-iam-roles-service-linked.md") | Yes         |

To get a high-level view of how network security director and other AWS services work with most IAM features, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

### Identity-based

policies for network security director

**Supports identity-based policies:**

Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These
policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based
policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
_IAM User Guide_.

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a
JSON policy, see [IAM JSON
policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the
_IAM User Guide_.

To view examples of AWS Shield network security director identity-based policies, see [Identity-based
policy examples for AWS Shield network security director](security-nsd-with-iam-id-based-policies.md "security-nsd-with-iam-id-based-policies.md").

### Service-linked

roles for network security director

**Supports service-linked roles:**

Yes

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
but not edit the permissions for service-linked roles.

For details about creating or managing network security director service-linked roles, see [Using service-linked roles for AWS Shield network security director](security_iam_nsd-with-iam-roles-service-linked.md "security_iam_nsd-with-iam-roles-service-linked.md").
