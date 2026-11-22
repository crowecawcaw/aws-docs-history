

AWS Well-Architected Agent is in preview release and is subject to change.

# Using service-linked roles for AWS Well-Architected

AWS Well-Architected uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to an AWS service. Service-linked roles are predefined by the service and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up AWS Well-Architected services easier because you don't have to manually add the necessary permissions. The service defines the permissions of its service-linked roles, and unless defined otherwise, only that service can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

AWS Well-Architected uses the following three service-linked roles:
+ **AWS Well-Architected Agent resource scanning** – the `` role, which AWS WA Agent uses to read resource configuration data across the accounts in your organization.
+ **AWS Well-Architected Agent Organizations access** – the `` role, which AWS WA Agent uses to read your organization structure and delegated administrator information in AWS Organizations.
+ **AWS Well-Architected Tool organization sharing and resource discovery** – the `AWSServiceRoleForWellArchitected` role, which carries two AWS managed policies. The `AWSWellArchitectedOrganizationsServiceRolePolicy` policy is used when you activate resource sharing with AWS Organizations in the AWS Well-Architected Tool, and the `` policy is used when you turn on Discovery support in the AWS Well-Architected Tool.

AWS WA Agent creates both agent service-linked roles when you enable the agent's organization integration. Enabling the organization integration is a single action in the management account that creates both the `` and `` roles in the management account. In each member account, AWS Organizations then provisions the `` resource-scanning role after you enable trusted access for the agent. For more information, see [Trusted access with AWS Organizations](agent-preferences.md#agent-preferences-trusted-access).

You can delete a service-linked role only after first deleting the related resources or disabling the related feature. This protects your AWS Well-Architected resources because you can't inadvertently remove permissions to access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes** in the **Service-linked role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

**Topics**
+ [Service-linked role permissions for AWS Well-Architected Agent resource scanning](using-service-linked-roles-agent-resource-scanning.md)
+ [Service-linked role permissions for AWS Well-Architected Agent Organizations access](using-service-linked-roles-agent-organizations.md)
+ [Service-linked role permissions for AWS Well-Architected Tool organization sharing and resource discovery](using-service-linked-roles-tool-org-sharing.md)