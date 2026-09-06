

# Managing Access to AWS Flat-Rate Plans
<a name="security-pricing-plan"></a>

You can use AWS Identity and Access Management (IAM) to control access to AWS Flat-Rate Plans. The namespace for Flat-Rate Plans is `pricingplanmanager`.

## Available Actions
<a name="available-actions"></a>

The following table lists the `pricingplanmanager` actions you can perform in the console and specify in an IAM policy to allow or deny specific operations:


| Action | Description | 
| --- | --- | 
| ApprovePaidSubscription | Grants permission to approve a paid subscription and start billing | 
| AssociateResourcesToSubscription | Grants permission to associate resources with a subscription | 
| CancelSubscription | Grants permission to cancel a subscription | 
| CancelSubscriptionChange | Grants permission to cancel a pending change for a subscription | 
| CreateSubscription | Grants permission to create a subscription | 
| DisassociateResourcesFromSubscription | Grants permission to disassociate resources from a subscription | 
| GetSubscription | Grants permission to get the details for a subscription | 
| ListSubscriptions | Grants permission to list subscriptions in your account | 
| UpdateSubscription | Grants permission to update a subscription | 

For information about how to create an IAM policy, see [Creating IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

## AWS managed policies for AWS Flat-Rate Plans
<a name="security-iam-awsmanpol"></a>

To add permissions to users, groups, and roles, it’s easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your users with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can’t change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new permissions become available. Services do not remove permissions from an AWS managed policy, so policy updates won’t break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

### AWS managed policy: PricingPlanManagerReadOnlyAccess
<a name="security-iam-awsmanpol-ppm-read-only"></a>

You can attach the **PricingPlanManagerReadOnlyAccess** policy to your IAM identities. This policy allows read-only permissions to PricingPlanManager resources. It also allows read-only permissions to other AWS service resources that are related to pricing plans and that are visible in the console.

 **Permissions details** 

This policy includes the following permissions.
+  `pricingplanmanager:GetSubscription` — Allows principals read-only access to get details about pricing plan subscriptions.
+  `pricingplanmanager:ListSubscriptions` — Allows principals read-only access to list pricing plan subscriptions.

To view the permissions for this policy, see [PricingPlanManagerReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/PricingPlanManagerReadonlyAccess.html) in the *AWS Managed Policy Reference*.

### AWS managed policy: PricingPlanManagerFullAccess
<a name="security-iam-awsmanpol-ppm-full-access"></a>

You can attach the **PricingPlanManagerFullAccess** policy to your IAM identities. This policy allows administrative permissions to PricingPlanManager resources, including creating, approving, updating, and canceling pricing plan subscriptions. It also allows read-only permissions to other AWS service resources that are related to pricing plans and that are visible in the console.

**Note**  
The **PricingPlanManagerFullAccess** policy includes the `pricingplanmanager:ApprovePaidSubscription` permission, which commits your account to charges for paid plans that can’t be canceled until the end of the current billing period. For automated workflows—such as deployment pipelines, agents, or service roles—we recommend a scoped-down policy that grants `pricingplanmanager:CreateSubscription` without `pricingplanmanager:ApprovePaidSubscription`, so that a human authorizes billing. For more information, see [Getting started with the PricingPlanManager API](getting-started-pricingplanmanager-api.md).

 **Permissions details** 

This policy includes the following permissions.
+  `pricingplanmanager:GetSubscription` — Allows principals read-only access to get details about pricing plan subscriptions.
+  `pricingplanmanager:ListSubscriptions` — Allows principals read-only access to list pricing plan subscriptions.
+  `pricingplanmanager:CreateSubscription` — Allows principals to create a subscription to a pricing plan.
+  `pricingplanmanager:ApprovePaidSubscription` — Allows principals to approve a paid subscription and start billing.
+  `pricingplanmanager:UpdateSubscription` — Allows principals to modify an existing subscription, such as changing the pricing plan.
+  `pricingplanmanager:CancelSubscription` — Allows principals to cancel an existing subscription.
+  `pricingplanmanager:CancelSubscriptionChange` — Allows principals to cancel a pending change to an existing subscription, such as a plan upgrade, before the change is applied.
+  `pricingplanmanager:AssociateResourcesToSubscription` — Allows principals to associate resources to a subscription. This enables the resources to be covered by the subscription’s pricing plan.
+  `pricingplanmanager:DisassociateResourcesFromSubscription` — Allows principals to remove the association between resources and an existing subscription.
+  `freetier:GetAccountPlanState` — Allows principals to get the AWS Free Tier plan state for the account, used to determine plan eligibility.
+  `cloudwatch:GetMetricData` — Allows principals to retrieve CloudWatch metric data for usage and allowance monitoring.
+  `shield:ListProtections` — Allows principals to list AWS Shield protections that are relevant to plan eligibility.

To view the permissions for this policy, see [PricingPlanManagerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/PricingPlanManagerFullAccess.html) in the *AWS Managed Policy Reference*.

### AWS Flat-Rate Plans updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for AWS Flat-Rate Plans since this service began tracking these changes.


| Change | Description | Date | 
| --- | --- | --- | 
|  [PricingPlanManagerReadOnlyAccess](#security-iam-awsmanpol-ppm-read-only) — New policy | AWS Flat-Rate Plans added a new policy that grants read-only access to pricing plan subscriptions. | July 28, 2026 | 
|  [PricingPlanManagerFullAccess](#security-iam-awsmanpol-ppm-full-access) — New policy | AWS Flat-Rate Plans added a new policy that grants administrative access to pricing plan subscriptions and read-only access to related AWS service resources. | July 28, 2026 | 
| AWS Flat-Rate Plans started tracking changes | AWS Flat-Rate Plans started tracking changes for its AWS managed policies. | July 28, 2026 | 