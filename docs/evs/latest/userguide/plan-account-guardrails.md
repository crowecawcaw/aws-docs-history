

# Account permissions and guardrails

Amazon Elastic VMware Service creates and manages resources in your AWS account, so the permissions and policies in that account decide whether a deployment succeeds. Prepare the AWS Identity and Access Management (IAM) permissions and check the guardrails on the account before you create an environment.

## IAM permissions for administrators
<a name="plan-account-guardrails-iam"></a>

The people and automation that create and manage Amazon EVS environments need an IAM role with permissions for Amazon EVS operations. We recommend that you create a role for this purpose and grant only the actions that your administrators need. For the steps, see [Create an IAM role for Amazon EVS administrators](setup-iam-role.md). For example policies, see [Amazon EVS identity-based policy examples](security-iam-id-based-policy-examples.md).

For guidance on writing the policies, such as least privilege and conditions, see [Policy best practices](security-iam-id-based-policy-examples.md#security_iam_service-with-iam-policy-best-practices).

To use the Amazon EVS console, a principal also needs a minimum set of permissions to list and view Amazon EVS resources. For the policy, see [Using the Amazon EVS console](security-iam-id-based-policy-examples.md#security-iam-id-based-policy-examples-console).

Amazon EVS doesn’t support resource-based policies or access control lists (ACLs). To give principals in other accounts access to your Amazon EVS resources, use an IAM role. For more information, see [I want to give other accounts access to my Amazon EVS resources](security-iam-troubleshoot.md#security-iam-troubleshoot-cross-account-access).

To view all Amazon EVS actions, resources and condition keys, see [Actions, resources, and condition keys for Amazon Elastic VMware Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_evs.html) in the *Service Authorization Reference*.

**Note**  
Amazon EVS doesn’t support the use of an instance profile to pass an IAM role to an EC2 instance.

## Service-linked role
<a name="plan-account-guardrails-slr"></a>

Amazon EVS uses the service-linked role `AWSServiceRoleForAmazonEVS` to call other AWS services on your behalf. When you create an environment, Amazon EVS creates the role for you if the IAM principal that creates the environment has the `iam:CreateServiceLinkedRole` permission. Make sure that the role that creates the first environment in the account has this permission. Before you can delete the role, you must delete the environments and hosts that use it.

For more information, see [Using service-linked roles for Amazon EVS](using-service-linked-roles.md).

## Service control policies
<a name="plan-account-guardrails-scp"></a>

If your account is in an organization in AWS Organizations, service control policies (SCPs) limit the permissions that IAM principals in the account can use. Review the SCPs that apply to the account before you deploy. Make sure that they allow the actions in your IAM policy for Amazon EVS and for the other services that your deployment uses.

For the actions that the example policies grant, see [Permissions for an Amazon EVS organizational unit](security-iam-id-based-policy-examples.md#security-iam-id-based-policy-examples-ou).

## Allowed AMIs and other EC2 account settings
<a name="plan-account-guardrails-amis"></a>

Amazon EVS launches the hosts as Amazon EC2 bare metal instances in your account. If you use the Allowed AMIs setting in your account, your image criteria must include the Amazon EVS AMIs, or you can’t create an environment or add a host. For the criteria to use, see [EC2 Allowed AMIs (only if you restrict AMI usage)](evs-deployment-prereq-checklist.md#evs-prereq-allowed-amis).

Don’t use the Amazon EC2 console to stop, start, or terminate Amazon EVS hosts. On hosts with local storage, these actions cause the loss of the vSAN data on the instance store volumes. For more information, see [Host maintenance and retirement events](evs-host-maintenance.md).

## Other account requirements
<a name="plan-account-guardrails-other"></a>

Check the following account requirements before you deploy.

 **Support plan**   
Environment creation fails if your account isn’t enrolled in an AWS Business Support, AWS Enterprise On-Ramp, or AWS Enterprise Support plan. For more information, see [Shared responsibility and support](plan-shared-responsibility.md).

 **Quotas**   
Environment creation fails if the Amazon EVS host quota is too low for your VMware Cloud Foundation (VCF) topology. For the quotas to check, see [Size your environment](plan-sizing.md).

 **EC2 key pair**   
Amazon EVS uses an EC2 key pair that you provide to connect to your hosts. For more information, see [Create a key pair for your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html) in the *Amazon EC2 User Guide*.

For the security controls of a running environment, including data protection and infrastructure security, see [Security in Amazon Elastic VMware Service](security.md). For the compliance programs that apply to Amazon EVS, see [Compliance validation for Amazon EVS](compliance-validation.md).