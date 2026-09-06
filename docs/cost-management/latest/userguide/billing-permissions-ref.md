

# Using identity-based policies (IAM policies) for AWS Cost Management
<a name="billing-permissions-ref"></a>

**Note**  
The following AWS Identity and Access Management (IAM) actions have reached the end of standard support on July 2023:  
`aws-portal` namespace
`purchase-orders:ViewPurchaseOrders`
`purchase-orders:ModifyPurchaseOrders`
If you're using AWS Organizations, you can use the [bulk policy migrator scripts](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/migrate-iam-permissions.html) to update polices from your payer account. You can also use the [old to granular action mapping reference](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/migrate-granularaccess-iam-mapping-reference.html) to verify the IAM actions that need to be added.  
For more information, see the [Changes to AWS Billing, AWS Cost Management, and Account Consoles Permission](https://aws.amazon.com/blogs/aws-cloud-financial-management/changes-to-aws-billing-cost-management-and-account-consoles-permissions/) blog.  
If you have an AWS account, or are a part of an AWS Organizations created on or after March 6, 2023, 11:00 AM (PDT), the fine-grained actions are already in effect in your organization.

This topic provides examples of identity-based policies that demonstrate how an account administrator can attach permissions policies to IAM identities (roles and groups) and thereby grant permissions to perform operations on Billing and Cost Management resources.

For a full discussion of AWS accounts and users, see [What Is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_Introduction.html) in the *IAM User Guide*.

For information on how you can update customer managed policies, see [Editing customer managed policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console) in the *IAM User Guide*.

**Topics**
+ [Billing and Cost Management actions policies](#user-permissions)
+ [Billing and Cost Management recommended actions policies](#allows-recommended-actions-access)
+ [Managed policies](#managed-policies)
+ [AWS Cost Management updates to AWS managed policies](#updates-managedIAM)

## Billing and Cost Management actions policies
<a name="user-permissions"></a>

This table summarizes the permissions that allow or deny users access to your billing information and tools. For examples of policies that use these permissions, see [AWS Cost Management policy examples](billing-example-policies.md). 

For a list of actions policies for the Billing console, see [Billing actions policies](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions) in the *Billing user guide*.


| Permission name | Description | 
| --- | --- | 
| `aws-portal:ViewBilling` | Allow or deny users permission to view the Billing and Cost Management console pages. For an example policy, see [Allow IAM users to view your billing information](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-example-policies.html#example-billing-view-billing-only) in the *Billing User Guide*. | 
| aws-portal:ViewUsage | Allow or deny users permission to view AWS usage [Reports](https://portal.aws.amazon.com/billing/home#/reports).<br />To allow users to view usage reports, you must allow both `ViewUsage` and `ViewBilling`.<br /> For an example policy, see [Allow IAM users to access the reports console page](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-example-policies.html#example-billing-view-reports) in the *Billing User Guide*. | 
| `aws-portal:ModifyBilling` | Allow or deny users permission to modify the following Billing and Cost Management console pages:+  [Budgets](https://portal.aws.amazon.com/billing/home#/budgets) <br />+  [Consolidated Billing](https://portal.aws.amazon.com/billing/home#/consolidatedbilling) <br />+  [Billing preferences](https://portal.aws.amazon.com/billing/home#/preferences) <br />+  [Credits](https://portal.aws.amazon.com/billing/home#/credits) <br />+  [Tax settings](https://portal.aws.amazon.com/billing/home#/tax) <br />+  [Payment methods](https://portal.aws.amazon.com/billing/home#/paymentmethods) <br />+  [Purchase orders](https://portal.aws.amazon.com/billing/home#/purchaseorders) <br />+  [Cost Allocation Tags](https://portal.aws.amazon.com/billing/home#/tags) <br />To allow users to modify these console pages, you must allow both `ModifyBilling` and `ViewBilling`. For an example policy, see [Allow users to modify billing information](billing-example-policies.md#example-billing-deny-modifybilling). | 
| `aws-portal:ViewAccount` | Allow or deny users permission to view the following Billing and Cost Management console pages:+  [Billing Dashboard]() <br />+  [Account Settings](https://portal.aws.amazon.com/billing/home#/account)  | 
| aws-portal:ModifyAccount | Allow or deny users permission to modify [Account Settings](https://portal.aws.amazon.com/billing/home#/account).<br />To allow users to modify account settings, you must allow both `ModifyAccount` and `ViewAccount`.<br />For an example of a policy that explicitly denies a user access to the **Account Settings** console page, see [Deny access to account settings, but allow full access to all other billing and usage information](billing-example-policies.md#example-billing-deny-modifyaccount).  | 
| budgets:ViewBudget | Allow or deny users permission to view [Budgets](https://portal.aws.amazon.com/billing/home#/budgets).<br />To allow users to view budgets, you must also allow `ViewBilling`. | 
| budgets:ModifyBudget | Allow or deny users permission to modify [Budgets](https://portal.aws.amazon.com/billing/home#/budgets).<br />To allow users to view and modify budgets, you must also allow `ViewBilling`. | 
| ce:GetPreferences | Allow or deny users permissions to view the Cost Explorer preferences page.<br />For an example policy, see [View and update the Cost Explorer preferences page](billing-example-policies.md#example-view-update-ce). | 
| ce:UpdatePreferences | Allow or deny users permissions to update the Cost Explorer preferences page.<br />For an example policy, see [View and update the Cost Explorer preferences page](billing-example-policies.md#example-view-update-ce). | 
| ce:DescribeReport | Allow or deny users permissions to view the Cost Explorer reports page.<br />For an example policy, see [View, create, update, and delete using the Cost Explorer reports page](billing-example-policies.md#example-view-ce-reports). | 
| ce:CreateReport | Allow or deny users permissions to create reports using the Cost Explorer reports page.<br />For an example policy, see [View, create, update, and delete using the Cost Explorer reports page](billing-example-policies.md#example-view-ce-reports). | 
| ce:UpdateReport | Allow or deny users permissions to update using the Cost Explorer reports page.<br />For an example policy, see [View, create, update, and delete using the Cost Explorer reports page](billing-example-policies.md#example-view-ce-reports). | 
| ce:DeleteReport | Allow or deny users permissions to delete reports using the Cost Explorer reports page.<br />For an example policy, see [View, create, update, and delete using the Cost Explorer reports page](billing-example-policies.md#example-view-ce-reports). | 
| ce:DescribeNotificationSubscription | Allow or deny users permissions to view Cost Explorer reservation expiration alerts in the reservation overview page.<br />For an example policy, see [View, create, update, and delete reservation and Savings Plans alerts](billing-example-policies.md#example-view-ce-expiration). | 
| ce:CreateNotificationSubscription | Allow or deny users permissions to create Cost Explorer reservation expiration alerts in the reservation overview page.<br />For an example policy, see [View, create, update, and delete reservation and Savings Plans alerts](billing-example-policies.md#example-view-ce-expiration). | 
| ce:UpdateNotificationSubscription | Allow or deny users permissions to update Cost Explorer reservation expiration alerts in the reservation overview page.<br />For an example policy, see [View, create, update, and delete reservation and Savings Plans alerts](billing-example-policies.md#example-view-ce-expiration). | 
| ce:DeleteNotificationSubscription | Allow or deny users permissions to delete Cost Explorer reservation expiration alerts in the reservation overview page.<br />For an example policy, see [View, create, update, and delete reservation and Savings Plans alerts](billing-example-policies.md#example-view-ce-expiration). | 
| ce:CreateCostCategoryDefinition | Allow or deny users permissions to create cost categories.<br /> For an example policy, see [View and manage cost categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-example-policies.html#example-policy-cc-api) in the *Billing User Guide*.<br />You can add resource tags to monitors during `Create`. In order to create monitors with resource tags, you need the `ce:TagResource` permission. | 
| ce:DeleteCostCategoryDefinition | Allow or deny users permissions to delete cost categories.<br /> For an example policy, see [View and manage cost categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-example-policies.html#example-policy-cc-api) in the *Billing User Guide*. | 
| ce:DescribeCostCategoryDefinition | Allow or deny users permissions to view cost categories.<br /> For an example policy, see [View and manage cost categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-example-policies.html#example-policy-cc-api) in the *Billing User Guide*. | 
| ce:ListCostCategoryDefinitions | Allow or deny users permissions to list cost categories.<br /> For an example policy, see [View and manage cost categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-example-policies.html#example-policy-cc-api) in the *Billing User Guide*. | 
| ce:ListTagsForResource | Allow or deny users permissions to list all resource tags for a given resource. For a list of supported resources, see [ResourceTag](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ResourceTag.html) in the *AWS Billing and Cost Management API Reference*. | 
| ce:UpdateCostCategoryDefinition | Allow or deny users permissions to update cost categories.<br /> For an example policy, see [View and manage cost categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-example-policies.html#example-policy-cc-api) in the *Billing User Guide*. | 
| ce:CreateAnomalyMonitor | Allow or deny users permissions to create a single [AWS Cost Anomaly Detection](manage-ad.md) monitor. You can add resource tags to monitors during `Create`. In order to create monitors with resource tags, you need the `ce:TagResource` permission. | 
| ce:GetAnomalyMonitors | Allow or deny users permissions to view all [AWS Cost Anomaly Detection](manage-ad.md) monitors. | 
| ce:UpdateAnomalyMonitor | Allow or deny users permissions to update [AWS Cost Anomaly Detection](manage-ad.md) monitors. | 
| ce:DeleteAnomalyMonitor | Allow or deny users permissions to delete [AWS Cost Anomaly Detection](manage-ad.md) monitors. | 
| ce:CreateAnomalySubscription | Allow or deny users permissions to create a single subscription for [AWS Cost Anomaly Detection](manage-ad.md). You can add resource tags to subscriptions during `Create`. In order to create subscriptions with resource tags, you need the `ce:TagResource` permission. | 
| ce:GetAnomalySubscriptions | Allow or deny users permissions to view all subscriptions for [AWS Cost Anomaly Detection](manage-ad.md). | 
| ce:UpdateAnomalySubscription | Allow or deny users permissions to update [AWS Cost Anomaly Detection](manage-ad.md) subscriptions. | 
| ce:DeleteAnomalySubscription | Allow or deny users permissions to delete [AWS Cost Anomaly Detection](manage-ad.md) subscriptions. | 
| ce:GetAnomalies | Allow or deny users permissions to view all anomalies in [AWS Cost Anomaly Detection](manage-ad.md). | 
| ce:ProvideAnomalyFeedback | Allow or deny users permissions to provide feedback on a detected [AWS Cost Anomaly Detection](manage-ad.md). | 
| ce:TagResource | Allow or deny users permissions to add resource tag key-value pairs to a resource. For a list of supported resources, see [ResourceTag](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ResourceTag.html) in the *AWS Billing and Cost Management API Reference*. | 
| ce:UntagResource | Allow or deny users permissions to delete resource tags from a resource. For a list of supported resources, see [ResourceTag](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ResourceTag.html) in the *AWS Billing and Cost Management API Reference*. | 
| ce:GetCostAndUsageComparisons | Allow or deny users permissions to retrieve cost and usage comparisons. | 
| ce:GetCostComparisonDrivers | Allow or deny users permissions to retrieve cost drivers. | 

## Billing and Cost Management recommended actions policies
<a name="allows-recommended-actions-access"></a>

To get started with recommended actions, you need to have the following core permission:
+ `bcm-recommended-actions:ListRecommendedActions`

Additional permissions are then required based on recommended action type. The following table summarizes the different recommended action types and the corresponding IAM policy permissions needed in order to see the recommended actions.

**Note**  
Even with a granted IAM policy permission, the corresponding recommended action type is only seen if the recommended action actually applies.


| Recommended action type | Required permission name | Description | 
| --- | --- | --- | 
| Expired payment method |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"payments:ListPaymentPreferences",<br />"payments:GetPaymentInstrument"<br />                                </pre>  | For payment-related recommended actions. | 
| Invalid payment method |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"payments:ListPaymentPreferences",<br />"payments:GetPaymentInstrument"<br />                                </pre>  | For payment-related recommended actions. | 
| Payments past due |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"payments:GetPaymentStatus"</pre>  | For payment-related recommended actions. | 
| Payments due |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"payments:GetPaymentStatus"</pre>  | For payment-related recommended actions. | 
| Fix tax registration information |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"tax:GetTaxRegistration"</pre>  | For recommended actions related to tax settings. | 
| Update tax exemption certificate |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"tax:GetExemptions"</pre>  | For recommended actions related to tax settings. | 
| Migrate to granular permissions |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"aws-portal:GetConsoleActionSetEnforced",<br />"ce:GetConsoleActionSetEnforced",<br />"purchase-orders:GetConsoleActionSetEnforced"<br /></pre>  | For recommended actions related to IAM permissions. | 
| Review budget alerts |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"budgets:DescribeBudgetNotificationsForAccount",<br />"budgets:DescribeBudget"</pre>  | For budget-related recommended actions. | 
| Review budgets exceeded |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"budgets:DescribeBudgets"</pre>  | For budget-related recommended actions. | 
| Review Free Tier usage alerts |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"freetier:GetFreeTierUsage"</pre>  | For recommended actions related to Free Tier. | 
| Review anomalies |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"ce:GetAnomalies"</pre>  | For recommended actions related to cost anomaly detection. | 
| Review expiring reservations |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"ce:GetReservationUtilization"</pre>  | For recommended actions related to cost optimization. | 
| Review expiring Savings Plans |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"ce:GetSavingsPlansUtilizationDetails"</pre>  | For recommended actions related to cost optimization. | 
| Review savings opportunity recommendations |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"cost-optimization-hub:ListEnrollmentStatuses",<br />"cost-optimization-hub:ListRecommendationSummaries"<br />                                </pre>  | For recommended actions related to cost optimization. | 
| Enable Cost Optimization Hub |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"cost-optimization-hub:ListEnrollmentStatuses"</pre>  | For recommended actions related to cost optimization. | 
| Create a budget |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"budgets:DescribeBudgets"</pre>  | For budget-related recommended actions. | 
| Create a reservation budget |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"budgets:DescribeBudgets",<br />"ce:GetReservationUtilization"</pre>  | For budget-related recommended actions. | 
| Create a Savings Plans budget |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"budgets:DescribeBudgets",<br />"ce:GetSavingsPlansUtilizationDetails"</pre>  | For budget-related recommended actions. | 
| Add an alternate billing contact |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"account:GetAlternateContact"</pre>  | For account-related recommended actions. | 
| Create an anomaly monitor |  <pre>"bcm-recommended-actions:ListRecommendedActions",<br />"ce:GetAnomalyMonitors"</pre>  | For recommended actions related to cost anomaly detection. | 

## Managed policies
<a name="managed-policies"></a>

**Note**  
The following AWS Identity and Access Management (IAM) actions have reached the end of standard support on July 2023:  
`aws-portal` namespace
`purchase-orders:ViewPurchaseOrders`
`purchase-orders:ModifyPurchaseOrders`
If you're using AWS Organizations, you can use the [bulk policy migrator scripts](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/migrate-iam-permissions.html) to update polices from your payer account. You can also use the [old to granular action mapping reference](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/migrate-granularaccess-iam-mapping-reference.html) to verify the IAM actions that need to be added.  
For more information, see the [Changes to AWS Billing, AWS Cost Management, and Account Consoles Permission](https://aws.amazon.com/blogs/aws-cloud-financial-management/changes-to-aws-billing-cost-management-and-account-consoles-permissions/) blog.  
If you have an AWS account, or are a part of an AWS Organizations created on or after March 6, 2023, 11:00 AM (PDT), the fine-grained actions are already in effect in your organization.

Managed policies are standalone identity-based policies that you can attach to multiple users, groups, and roles in your AWS account. You can use AWS managed policies to control access in Billing and Cost Management.

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases. AWS managed policies make it easier for you to assign appropriate permissions to users, groups, and roles than if you had to write the policies yourself.

You can't change the permissions defined in AWS managed policies. AWS occasionally updates the permissions defined in an AWS managed policy. When this occurs, the update affects all principal entities (users, groups, and roles) that the policy is attached to.

Billing and Cost Management provides several AWS managed policies for common use cases.

**Topics**
+ [Allows full access to AWS Budgets including budgets actions](#budget-managedIAM-full)
+ [Allows read only access to AWS Budgets](#budget-managedIAM-read-only)
+ [Allows AWS Budgets to call services required to verify billing view access](#budget-managedIAM-billing-view)
+ [Allows permission to control AWS resources](#budget-managedIAM-SSM)
+ [Allows Cost Optimization Hub to call services required to make the service work](#cost-optimization-hub-managedIAM)
+ [Allows read-only access to Cost Optimization Hub](#cost-optimization-hub-read-only)
+ [Allows admin access to Cost Optimization Hub](#cost-optimization-hub-admin)
+ [Allows split cost allocation data to call services required to make the service work](#split-cost-allocation-data-managedIAM)
+ [Allows Data Exports to access other AWS services](#data-exports-managedIAM)

### Allows full access to AWS Budgets including budgets actions
<a name="budget-managedIAM-full"></a>

Managed policy name: `AWSBudgetsActionsWithAWSResourceControlAccess`

This managed policy is focused on the user, ensuring that you have the proper permissions to grant permission to AWS Budgets to run the defined actions. This policy provides full access to AWS Budgets, including budgets actions, to retrieve the status of your policies and run AWS resources using the AWS Management Console.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "budgets:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "aws-portal:ViewBilling"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "budgets.amazonaws.com"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "aws-portal:ModifyBilling",
                "ec2:DescribeInstances",
                "iam:ListGroups",
                "iam:ListPolicies",
                "iam:ListRoles",
                "iam:ListUsers",
                "organizations:ListAccounts",
                "organizations:ListOrganizationalUnitsForParent",
                "organizations:ListPolicies",
                "organizations:ListRoots",
                "rds:DescribeDBInstances",
                "sns:ListTopics"
            ],
            "Resource": "*"
        }
    ]
}
```

------

### Allows read only access to AWS Budgets
<a name="budget-managedIAM-read-only"></a>

Managed policy name: `AWSBudgetsReadOnlyAccess`

This managed policy allows read only access to AWS Budgets through the AWS Management Console. The policy can be attached to your users, groups, and roles.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement" : [
    {
      "Sid": "AWSBudgetsReadOnlyAccess",
      "Effect" : "Allow",
      "Action" : [
        "aws-portal:ViewBilling",
        "budgets:ViewBudget",
        "budgets:Describe*",
        "budgets:ListTagsForResource"
      ],
      "Resource" : "*"
    }
  ]
}
```

------

### Allows AWS Budgets to call services required to verify billing view access
<a name="budget-managedIAM-billing-view"></a>

Managed policy name: `BudgetsServiceRolePolicy`

Allows AWS Budgets to verify access to billing views shared across account boundaries.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "billing:GetBillingViewData"
            ],
            "Resource": "*"
        }
    ]
}
```

------

For more information, see [Service-linked roles for Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-SLR.html).

### Allows permission to control AWS resources
<a name="budget-managedIAM-SSM"></a>

Managed policy name: `AWSBudgetsActions_RolePolicyForResourceAdministrationWithSSM`

This managed policy is focused on specific actions that AWS Budgets takes on your behalf when completing a specific action. This policy gives permission to control AWS resources. For example, starts and stops Amazon EC2 or Amazon RDS instances by running AWS Systems Manager (SSM) scripts.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstanceStatus",
                "ec2:StartInstances",
                "ec2:StopInstances",
                "rds:DescribeDBInstances",
                "rds:StartDBInstance",
                "rds:StopDBInstance"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws:CalledVia": [
                        "ssm.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:StartAutomationExecution"
            ],
            "Resource": [
                "arn:aws:ssm:*:*:document/AWS-StartEC2Instance",
                "arn:aws:ssm:*:*:document/AWS-StopEC2Instance",
                "arn:aws:ssm:*:*:document/AWS-StartRdsInstance",
                "arn:aws:ssm:*:*:document/AWS-StopRdsInstance",
                "arn:aws:ssm:*:*:automation-execution/*",
                "arn:aws:ssm:*:*:automation-definition/AWS-StartEC2Instance:*",
                "arn:aws:ssm:*:*:automation-definition/AWS-StopEC2Instance:*",
                "arn:aws:ssm:*:*:automation-definition/AWS-StartRdsInstance:*",
                "arn:aws:ssm:*:*:automation-definition/AWS-StopRdsInstance:*"
            ]
        }
    ]
}
```

### Allows Cost Optimization Hub to call services required to make the service work
<a name="cost-optimization-hub-managedIAM"></a>

Managed policy name: `CostOptimizationHubServiceRolePolicy`

Allows Cost Optimization Hub to retrieve organization information and collect optimization-related data and metadata.

To view the permissions for this policy, see [CostOptimizationHubServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CostOptimizationHubServiceRolePolicy.html) in the *AWS Managed Policy Reference Guide*.

For more information, see [Service-linked roles for Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub-SLR.html).

### Allows read-only access to Cost Optimization Hub
<a name="cost-optimization-hub-read-only"></a>

Managed policy name: `CostOptimizationHubReadOnlyAccess`

This managed policy provides read-only access to Cost Optimization Hub.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "CostOptimizationHubReadOnlyAccess",
            "Effect": "Allow",
            "Action": [
                "cost-optimization-hub:ListEnrollmentStatuses",
                "cost-optimization-hub:GetPreferences",
                "cost-optimization-hub:GetRecommendation",
                "cost-optimization-hub:ListRecommendations",
                "cost-optimization-hub:ListRecommendationSummaries"
            ],
            "Resource": "*"
        }
    ]
}
```

------

### Allows admin access to Cost Optimization Hub
<a name="cost-optimization-hub-admin"></a>

Managed policy name: `CostOptimizationHubAdminAccess`

This managed policy provides admin access to Cost Optimization Hub.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "CostOptimizationHubAdminAccess",
            "Effect": "Allow",
            "Action": [
                "cost-optimization-hub:ListEnrollmentStatuses",
                "cost-optimization-hub:UpdateEnrollmentStatus",
                "cost-optimization-hub:GetPreferences",
                "cost-optimization-hub:UpdatePreferences",
                "cost-optimization-hub:GetRecommendation",
                "cost-optimization-hub:ListRecommendations",
                "cost-optimization-hub:ListRecommendationSummaries",
                "organizations:EnableAWSServiceAccess"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowCreationOfServiceLinkedRoleForCostOptimizationHub",
            "Effect": "Allow",
            "Action": [
                "iam:CreateServiceLinkedRole"
            ],
            "Resource": [
                "arn:aws:iam::*:role/aws-service-role/cost-optimization-hub.bcm.amazonaws.com/AWSServiceRoleForCostOptimizationHub"
            ],
            "Condition": {
                "StringLike": {
                    "iam:AWSServiceName": "cost-optimization-hub.bcm.amazonaws.com"
                }
            }
        },
        {
            "Sid": "AllowAWSServiceAccessForCostOptimizationHub",
            "Effect": "Allow",
            "Action": [
                "organizations:EnableAWSServiceAccess"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "organizations:ServicePrincipal": [
                        "cost-optimization-hub.bcm.amazonaws.com"
                    ]
                }
            }
        }
    ]
}
```

------

### Allows split cost allocation data to call services required to make the service work
<a name="split-cost-allocation-data-managedIAM"></a>

Managed policy name: `SplitCostAllocationDataServiceRolePolicy`

Allows split cost allocation data to retrieve AWS Organizations information, if applicable, and collect telemetry data for the split cost allocation data services that the customer has opted in to.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AwsOrganizationsAccess",
            "Effect": "Allow",
            "Action": [
                "organizations:DescribeOrganization",
                "organizations:ListAccounts",
                "organizations:ListAWSServiceAccessForOrganization",
                "organizations:ListParents"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AmazonManagedServiceForPrometheusAccess",
            "Effect": "Allow",
            "Action": [
                "aps:ListWorkspaces",
                "aps:QueryMetrics"
            ],
            "Resource": "*"
        }
    ]
}
```

------

For more information, see [Service-linked roles for split cost allocation data](https://docs.aws.amazon.com/cost-management/latest/userguide/split-cost-allocation-data-SLR.html).

### Allows Data Exports to access other AWS services
<a name="data-exports-managedIAM"></a>

Managed policy name: `AWSBCMDataExportsServiceRolePolicy`

Allows Data Exports to access other AWS services such as Cost Optimization Hub on your behalf.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "CostOptimizationRecommendationAccess",
            "Effect": "Allow",
            "Action":  [
                "cost-optimization-hub:ListEnrollmentStatuses",
                "cost-optimization-hub:ListRecommendations"
            ],
            "Resource": "*" 
        }
    ]
}
```

------

For more information, see [Service-linked roles for Data Exports](https://docs.aws.amazon.com/cost-management/latest/userguide/data-exports-SLR.html).

## AWS Cost Management updates to AWS managed policies
<a name="updates-managedIAM"></a>

View details about updates to AWS managed policies for AWS Cost Management since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the AWS Cost Management [Document history](https://docs.aws.amazon.com/cost-management/latest/userguide/doc-history.html) page.



| Change | Description | Date | 
| --- | --- | --- | 
| Update to existing policy<br />[AWSBudgetsActions\_RolePolicyForResourceAdministrationWithSSM](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html#budget-managedIAM-SSM) | We updated the policy with require automation-execution and document permissions to use ssm:StartAutomationExecution. | 04/07/2026 | 
| Update to existing policies<br />[CostOptimizationHubReadOnlyAccess](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html#cost-optimization-hub-read-only)<br />[CostOptimizationHubAdminAccess](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html#cost-optimization-hub-admin) | We updated the policy to add the "cost-optimization-hub:ListEfficiencyMetrics" action. | 11/20/2025 | 
| Addition of a new policy<br />[BudgetsServiceRolePolicy](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html#budget-managedIAM-billing-view) | Budgets added a new policy to be used with service-linked roles, which enables access to AWS services and resources used or managed by Budgets. | 08/06/2025 | 
| Update to existing policy<br />[CostOptimizationHubServiceRolePolicy](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html#cost-optimization-hub-managedIAM) | We updated the policy to add the ce:GetDimensionValues action. | 07/23/2025 | 
| Update to existing policy<br />[CostOptimizationHubServiceRolePolicy](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html#cost-optimization-hub-managedIAM) | We updated the policy to add the organizations:ListDelegatedAdministrators and ce:GetCostAndUsage actions. | 07/05/2024 | 
| Update to existing policy<br />[AWSBudgetsReadOnlyAccess](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html#budget-managedIAM-read-only) | We updated the policy to add the budgets:ListTagsForResource action. | 06/17/2024 | 
| Addition of a new policy<br />[AWSBCMDataExportsServiceRolePolicy](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html#data-exports-managedIAM) | Data Exports added a new policy to be used with service-linked roles, which enables access to other AWS services such as Cost Optimization Hub. | 06/10/2024 | 
| Addition of a new policy<br />[SplitCostAllocationDataServiceRolePolicy](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html#split-cost-allocation-data-managedIAM) | Split cost allocation data added a new policy to be used with service-linked roles, which enables access to AWS services and resources used or managed by split cost allocation data. | 04/16/2024 | 
| Update to existing policy<br />[AWSBudgetsActions\_RolePolicyForResourceAdministrationWithSSM](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html#budget-managedIAM-SSM) | We updated the policy with scoped down permissions. The ssm:StartAutomationExecution action is only allowed for specific resources used by Budget actions. | 12/14/2023 | 
| Update to existing policies<br />[CostOptimizationHubReadOnlyAccess](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html#cost-optimization-hub-read-only)<br />[CostOptimizationHubAdminAccess](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html#cost-optimization-hub-admin) | Cost Optimization Hub updated the following two managed policies:+  `CostOptimizationHubReadOnlyAccess`: Fixed typo in "GetRecommendation"; removed permissions covered by the SLR policy. <br />+  `CostOptimizationHubAdminAccess`: Fixed typo in "GetRecommendation"; removed permissions covered by the SLR policy; added permissions to enable service access and to create the SLR, so that the policy provides all necessary permissions to opt in and use Cost Optimization Hub.  | 12/14/2023 | 
| Addition of a new policy<br />[CostOptimizationHubServiceRolePolicy](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html#cost-optimization-hub-managedIAM) | Cost Optimization Hub added a new policy to be used with service-linked roles, which enables access to AWS services and resources used or managed by Cost Optimization Hub. | 11/02/2023 | 
| AWS Cost Management started tracking changes | AWS Cost Management started tracking changes for its AWS managed policies | 11/02/2023 | 