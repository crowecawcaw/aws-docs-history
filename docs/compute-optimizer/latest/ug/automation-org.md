# Enabling Automation for your organization

When you enable Automation for your organization’s management account, you can also configure Automation for your organization’s member accounts, enabling centralized implementation of optimization actions across your organization. This centralized approach can help you optimize for cost and performance at scale.

## Policy to enable Automation across your

organization

The following policy statement enables Automation across your organization.

```

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
            "Action": "aco-automation:ListAccounts",
            "Resource": "*"
        }
    ]
}

```

## Trusted access for AWS Organizations

You must have trusted access enabled to manage automation for your member accounts. When you opt in to Compute Optimizer using your organization's management account and include all member accounts, trusted access is automatically enabled. This allows Compute Optimizer to analyze resources and generate recommendations for member accounts. Trusted access also allows Compute Optimizer to implement recommendations for member accounts that have also enabled the Automation feature.

Compute Optimizer verifies that trusted access is enabled each time you access recommendations or apply recommendations for member accounts. If you disable trusted access, the management account loses access to recommendations and automation for your organization's member accounts. To re-enable trusted access, opt in to Compute Optimizer again using your organization's management account and include all the member accounts. For more information, see [Opting in to AWS Compute Optimizer](account-opt-in.md "account-opt-in.md"). For more information about AWS Organizations trusted access, see [Using AWS Organizations with other AWS services](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md") in the AWS Organizations User Guide.

## Configure automation for member accounts

To enable Automation for member accounts, the management account needs permissions to associate and disassociate accounts. These permissions allow the management account to enable Automation for member accounts and configure whether the management account can implement optimizations on behalf of member accounts. For more information , see [Policy to enable Automation across your
organization](security-iam.md#automation-enable-org "security-iam.md#automation-enable-org").

Once a member account is associated, the management account or delegated administrator can view and apply recommended actions to the member account. When you associate a member account, its organization rule mode is automatically set to Any Allowed, which permits the management account to create Automation rules that automatically apply actions to that account. If the member account has not previously enabled the Automation feature, the association process automatically enables it.

###### To enable Automation for member accounts

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. In the navigation pane, choose **Account management** under the **Preferences** section.
3. Choose the
   **Automation** tab.
4. Search for the account using its account Id.
5. Select the account and choose Add. You can enable Automation for up to 50 accounts at a time.

## Organization rule mode

This setting controls whether the management account can implement automated optimization actions for the member account. When set to Any Allowed, the management account can directly implement recommended actions or create Automation rules that apply to the member account. When set to None Allowed, only the member account can act on its own recommendations, and management account rules will not apply. When you enable Automation for a member account, its organization rule mode is automatically set to Any Allowed.

Organization rules targeting a member account automatically start or stop applying based on the organization rule mode setting. Rules apply when the mode is set to Any Allowed and stop applying when set to None Allowed. If you change the mode to None allowed, any in-progress automation steps initiated by organization rules will continue to completion, but no new automation steps will be triggered by organization rules for that account.

###### To configure organization rule mode for member accounts

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. In the navigation pane, choose **Account management** under the **Preferences** section.
3. Choose the
   **Automation** tab.
4. Select the accounts that you want to configure.
5. Choose **Actions** and select `Allow organization rules` or `Disallow organization rules`. You can select and update the configuration for up to 50 accounts at a time.
