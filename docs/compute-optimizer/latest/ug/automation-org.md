

# Enabling Automation for your organization

When you enable Automation for your organization’s management account, you can also configure Automation for your organization’s member accounts. With this centralized approach, you can implement optimization actions across your organization at scale, which helps you optimize for cost and performance.

You can create automation rules for your organization with CloudFormation. For more information, see [Creating automation rules with CloudFormation](creating-automation-rules-with-cloudformation.md).

## Policy to enable Automation across your organization
<a name="automation-enable-org-coa"></a>

The following policy statement enables Automation across your organization.

```JSON
                {
    "Version": "2012-10-17",                   
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation",
            "Condition": {"StringLike": {"iam:AWSServiceName": "aco-automation.amazonaws.com"}}
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PutRolePolicy", 
                "iam:AttachRolePolicy"
            ],
            "Resource": "arn:aws:iam::*:role/aws-service-role/aco-automation.amazonaws.com/AWSServiceRoleForComputeOptimizerAutomation"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:UpdateEnrollmentConfiguration",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:AssociateAccounts",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:DisassociateAccounts",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "aco-automation:PutOrganizationEnrollmentConfiguration",
                "aco-automation:DeleteOrganizationEnrollmentConfiguration",
                "aco-automation:ListOrganizationEnrollmentConfigurations",
                "aco-automation:ListOrganizationalUnits"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "aco-automation:ListAccounts",
            "Resource": "*"
        }
    ]
}
```

## Trusted access for AWS Organizations
<a name="automation-org-access"></a>

You must have trusted access enabled to manage automation for your member accounts. When you opt in to AWS Compute Optimizer using your organization's management account and include all member accounts, Compute Optimizer automatically enables trusted access. With trusted access, Compute Optimizer can analyze resources and generate recommendations for member accounts. Compute Optimizer can also implement recommendations for member accounts that have enabled the Automation feature.

Compute Optimizer verifies that trusted access is enabled each time you access recommendations or apply recommendations for member accounts. If you disable trusted access, the management account loses access to recommendations and automation for your organization's member accounts. To re-enable trusted access, opt in to Compute Optimizer again using your organization's management account and include all the member accounts. For more information, see [Opting in to AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html). For more information about AWS Organizations trusted access, see [Using AWS Organizations with other AWS services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) in the AWS Organizations User Guide.

## Configure automation for member accounts
<a name="automation-org-configure"></a>

To enable Automation for member accounts, create an organization enrollment configuration on the root, an organizational unit (OU), or an account. An enrollment configuration enables Automation for every eligible member account that it applies to and sets the organization rule mode for those accounts. To create enrollment configurations, the management account or delegated administrator needs the permissions in [Policy to enable Automation across your organization](#automation-enable-org-coa).

If you organize your accounts in OUs in AWS Organizations, you can enable Automation for every account in an OU with one enrollment configuration. Choose where to create the enrollment configuration:
+ To enable Automation for every member account in your organization, including accounts that join later, create an enrollment configuration on the root.
+ To enable Automation for every account in an OU and its child OUs, including accounts that join later, create an enrollment configuration on the OU.
+ To enable Automation for specific member accounts, create an enrollment configuration on each account.

After Compute Optimizer enables Automation for a member account, the management account or a delegated administrator can view its recommended actions. They can apply recommended actions to the account and include it in organization rules only when its organization rule mode is **Any allowed**. For more information, see [Organization enrollment configurations](automation-org-enrollment.md).

**To enable Automation for member accounts**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Account management** under the **Preferences** section.

1. Choose the **Automation** tab.

1. In the **Enrollment configurations** section, choose **Create enrollment configuration**.

1. On the **Select organizational units and accounts** page, select the root, OUs, or accounts that you want to enable Automation for, and then choose **Next**.

1. On the **Set organization rule mode** page, choose **Any allowed** or **None allowed** for each OU and account.

1. Choose **Create enrollment configuration**.

## Organization rule mode
<a name="automation-org-rule"></a>

The organization rule mode controls whether the management account can apply recommended actions to a member account. With this setting, you can balance centralized governance with individual account autonomy. Each enrollment configuration sets the organization rule mode for the accounts that it applies to:
+ **Any allowed**. The management account can apply recommended actions to the account and include it in organization rules.
+ **None allowed**. The account applies its own recommended actions and runs its own automation rules. Organization rules don't apply to it.

OUs and accounts without their own enrollment configuration inherit from their closest parent that has one. If no parent has one, the organization rule mode is the default, **None allowed**. For more information, see [How Compute Optimizer determines an account's organization rule mode](automation-org-enrollment.md#automation-org-enrollment-determine).

Organization rules that target a member account start or stop applying when its organization rule mode changes. Rules apply when the mode is **Any allowed** and stop applying when it's **None allowed**. If you change the mode to **None allowed**, automation steps that organization rules already started continue to completion, but organization rules don't start new automation steps for that account.

**To configure organization rule mode for member accounts**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Account management** under the **Preferences** section.

1. Choose the **Automation** tab.

1. In the **Enrollment configurations** table, select the enrollment configurations that you want to update.

1. For **Actions**, choose **Update to any allowed** or **Update to none allowed**. To set a different organization rule mode for an OU or account that inherits one, create an enrollment configuration for it.

## Examples: Enabling Automation for your organization
<a name="automation-org-examples"></a>

The following examples use the same organization. Each example shows the enrollment configurations to create and the result for each member account.

```
Root (r-a1b2)
├── Management account (111122223333)
├── Production OU (ou-a1b2-prod0001)
│   ├── Account 444455556666
│   └── Web OU (ou-a1b2-web00001)
│       └── Account 123456789012
├── Sandbox OU (ou-a1b2-sbx00001)
│   └── Account 777788889999
└── Account 222222222222
```

An enrollment configuration doesn't apply to the management account, so the management account doesn't appear in the results.

### Example: Enable Automation for every member account
<a name="automation-org-examples-all"></a>

To enable Automation for every member account in your organization, create one enrollment configuration on the root. It also applies to accounts that join the organization later.

The following table lists the enrollment configurations to create.


| Target | Organization rule mode | 
| --- | --- | 
| Root (`r-a1b2`) | Any allowed | 

The following table shows the result for each member account.


| Account | Automation | Organization rule mode | Explanation | 
| --- | --- | --- | --- | 
| `444455556666` | Enabled | Any allowed | Inherits the enrollment configuration on the root. | 
| `123456789012` | Enabled | Any allowed | Inherits the enrollment configuration on the root through the Production OU and the Web OU. | 
| `777788889999` | Enabled | Any allowed | Inherits the enrollment configuration on the root. | 
| `222222222222` | Enabled | Any allowed | Inherits the enrollment configuration on the root. | 

### Example: Enable Automation for one OU
<a name="automation-org-examples-one-ou"></a>

To enable Automation for one part of your organization, create an enrollment configuration on the OU. The enrollment configuration applies to every account in the OU and in its child OUs.

The following table lists the enrollment configurations to create.


| Target | Organization rule mode | 
| --- | --- | 
| Production OU (`ou-a1b2-prod0001`) | Any allowed | 

The following table shows the result for each member account.


| Account | Automation | Organization rule mode | Explanation | 
| --- | --- | --- | --- | 
| `444455556666` | Enabled | Any allowed | Inherits the enrollment configuration on the Production OU. | 
| `123456789012` | Enabled | Any allowed | The Web OU is a child of the Production OU, so the account inherits the enrollment configuration. | 
| `777788889999` | No change | No change | No enrollment configuration applies to the Sandbox OU. | 
| `222222222222` | No change | No change | No enrollment configuration applies to the account. | 

### Example: Enable Automation for specific accounts
<a name="automation-org-examples-accounts"></a>

To enable Automation for specific accounts only, create an enrollment configuration on each account.

The following table lists the enrollment configurations to create.


| Target | Organization rule mode | 
| --- | --- | 
| Account `444455556666` | Any allowed | 
| Account `222222222222` | Any allowed | 

The following table shows the result for each member account.


| Account | Automation | Organization rule mode | Explanation | 
| --- | --- | --- | --- | 
| `444455556666` | Enabled | Any allowed | Has its own enrollment configuration. | 
| `123456789012` | No change | No change | The enrollment configuration on account 444455556666 doesn't apply to other accounts in the Production OU. | 
| `777788889999` | No change | No change | No enrollment configuration applies to the account. | 
| `222222222222` | Enabled | Any allowed | Has its own enrollment configuration. | 

### Example: Keep organization rules off one OU
<a name="automation-org-examples-exclude-ou"></a>

To enable Automation for every member account while the accounts in one OU act only on their own recommendations, create an enrollment configuration on the root and a **None allowed** enrollment configuration on that OU. The enrollment configuration on the OU takes precedence over the enrollment configuration on the root.

The following table lists the enrollment configurations to create.


| Target | Organization rule mode | 
| --- | --- | 
| Root (`r-a1b2`) | Any allowed | 
| Sandbox OU (`ou-a1b2-sbx00001`) | None allowed | 

The following table shows the result for each member account.


| Account | Automation | Organization rule mode | Explanation | 
| --- | --- | --- | --- | 
| `444455556666` | Enabled | Any allowed | Inherits the enrollment configuration on the root. | 
| `123456789012` | Enabled | Any allowed | Inherits the enrollment configuration on the root. | 
| `777788889999` | Enabled | None allowed | Inherits the enrollment configuration on the Sandbox OU, which takes precedence over the root. Organization rules don't apply to the account. | 
| `222222222222` | Enabled | Any allowed | Inherits the enrollment configuration on the root. | 

To check the result for each account, choose **View organization status** on the **Automation** tab.