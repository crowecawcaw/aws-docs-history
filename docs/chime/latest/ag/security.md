**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Security in Amazon Chime

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security
_of_ the cloud and security _in_ the cloud:

- **Security of the cloud** – AWS is responsible for protecting the
  infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn about the compliance programs that apply to Amazon Chime, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility is
  determined by the AWS service that you use. You are also responsible for other factors
  including the sensitivity of your data, your company’s requirements, and applicable laws and
  regulations.
  This documentation helps you understand how to apply the shared responsibility model when
  using Amazon Chime. The following topics show you how to configure Amazon Chime to meet your
  security and compliance objectives. You also learn how to use other AWSAWS services that help you
  to monitor and secure your Amazon Chime resources.

###### Topics

- [Identity and access management for Amazon Chime](security-iam.md "security-iam.md")
- [How Amazon Chime works with
  IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md")
- [Cross-service confused deputy prevention](confused-deputy.md "confused-deputy.md")
- [Amazon Chime
  resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on
  Amazon Chime tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Amazon Chime IAM
  roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")
- [Amazon Chime identity-based
  policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md")
- [Troubleshooting Amazon Chime identity and
  access](security_iam_troubleshoot.md "security_iam_troubleshoot.md")
- [Using service-linked roles for
  Amazon Chime](using-service-linked-roles.md "using-service-linked-roles.md")
- [Logging and monitoring in Amazon Chime](monitoring-overview.md "monitoring-overview.md")
- [Compliance validation for Amazon Chime](compliance.md "compliance.md")
- [Resilience in Amazon Chime](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md")
- [Infrastructure security in Amazon Chime](infrastructure-security.md "infrastructure-security.md")
- [Understanding Amazon Chime automatic updates](chime-auto-update.md "chime-auto-update.md")

## Amazon Chime

resource-based policies

Amazon Chime does not support resource-based policies.

## Authorization based on

Amazon Chime tags

Amazon Chime does not support tagging resources or controlling access based on tags.

## Amazon Chime IAM

roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using temporary

credentials with Amazon Chime

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security credentials by
calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Amazon Chime supports using temporary credentials.

### Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services that complete actions on your behalf. Service-linked roles appear in your
IAM account, and the services own the roles. An IAM administrator can view but
not edit the permissions for service-linked roles.

Amazon Chime supports service-linked roles. For details about creating or
managing Amazon Chime service-linked roles, see [Using service-linked roles for
Amazon Chime](using-service-linked-roles.md "using-service-linked-roles.md").

### Service roles

This feature allows a service to assume a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access resources in
other services to complete an action on your behalf. Service roles appear in your
IAM account and are owned by the account. This means that an IAM administrator
can change the permissions for this role. However, doing so might break the
functionality of the service.

Amazon Chime does not support service roles.
