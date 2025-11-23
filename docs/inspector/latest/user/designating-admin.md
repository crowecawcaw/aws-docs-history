# Designating a delegated administrator account for Amazon Inspector

The delegated administrator is an account that manages a service for an organiztion.
This topic describes how to designate a delegated administrator for Amazon Inspector.

## Considerations

Before designating a delegated administrator, note the following:

**The delegated administrator can manage a maximum of 10,000 members.**

If you exceed 10,000 member accounts, you receive a notification through the Amazon CloudWatch Personal Health Dashboard and email to the delegated administrator account.

###### Note

When Amazon Inspector is enabled through AWS Organizations policies for organizations with more than 10,000 accounts (up to 50,000), the policy applies to all accounts.
However, only 10,000 accounts will be associated with the Amazon Inspector organization.
i.e. the delegated administrator can view findings and account status for only these 10,000 accounts in the Amazon Inspector console.

**The delegated administrator is Regional.**

Amazon Inspector is a Regional service.
You must repeat the steps in the procedure in every AWS Region where you plan to use Amazon Inspector.

**An organization can have only one delegated administrator.**

If designate an account as the delegated administrator in one AWS Region, that account must be the delegated administrator in all other AWS Regions.

**Changing a delegated administrator does not deactivate Amazon Inspector for member accounts.**

If you remove a delegated administrator, member accounts become standalone accounts and scan settings aren't affected.

**Your AWS Organization must have all features activated.**

This is the default setting for AWS Organizations. If it's not activated, see [Activating all features in your organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md").

**Organization policies take precedence over delegated administrator settings.**

If your organization uses AWS Organizations policies to enable Amazon Inspector, the policy settings determine which scan types are enabled.
We recommend designating the delegated administrator before creating organization policies to ensure consistent governance.
For more information, see [Organization policy governance model](admin-member-relationship.md#org-policy-overview "admin-member-relationship.md#org-policy-overview").

## Permissions required to designate a delegated administrator

You must have permission to activate Amazon Inspector and to designate an Amazon Inspector delegated administrator.
Add the following statement to the end of your IAM policy to grant these permissions.
For more information, see [Managing IAM policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md").

```

{
    "Sid": "PermissionsForInspectorAdmin",
    "Effect": "Allow",
    "Action": [
        "inspector2:EnableDelegatedAdminAccount",
        "organizations:EnableAWSServiceAccess",
        "organizations:RegisterDelegatedAdministrator",
        "organizations:ListDelegatedAdministrators",
        "organizations:ListAWSServiceAccessForOrganization",
        "organizations:DescribeOrganizationalUnit",
        "organizations:DescribeAccount",
        "organizations:DescribeOrganization"
    ],
    "Resource": "*"
}

```

## Designating a delegated administrator for

your AWS organization

The following procedure describes how to designate a delegated administrator for your organization.
Before you complete the procedure, make sure you are in the same organization as the member accounts you want the delegated administrator to manage.

###### Note

You must use the AWS Organizations management account to complete this procedure.
Only the AWS Organizations management account can designate a delegated administrator.
Permissions might be required to designate a delegated administrator.
For more information, see [Permissions required to designate a delegated administrator](#delegated-admin-permissions "#delegated-admin-permissions").

When you activate Amazon Inspector for the first time, Amazon Inspector creates the service linked role `AWSServiceRoleForAmazonInspector` for the account.
For information about how Amazon Inspector uses service-linked roles, see [Using service-linked roles for Amazon Inspector](using-service-linked-roles.md "using-service-linked-roles.md").

Console

###### To designate a delegated administrator for Amazon Inspector

1. Sign in to the AWS Organizations management account, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. Use the AWS Region selector to specify the AWS Region where you want to designate the delegated administrator.
3. From the navigation pane, choose **General settings**.
4. Under **Delegated administrator**, enter the 12-digit ID of the AWS account you want to designate as the delegated administrator.
5. Choose **Delegate**, and then choose **Delegate** again.

When you designate a delegated administrator, [all scan types](scanning-resources.md "scanning-resources.md") are activated for the account by default.
If you want to activate Amazon Inspector for the AWS Organizations management account, complete the following procedure.

###### To activate Amazon Inspector for the AWS Organizations management account

1. Sign in to the delegated administrator account, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. From the navigation pane, choose **Account management**.
3. Under **Accounts**, select the AWS Organizations management account, and then choose **Activate**.
4. Select which scan types you want to activate for the AWS Organizations management account, and then choose **Submit**.

API

###### Designate a delegated administrator using the API

- Run the [EnableDelegatedAdminAccount](../../v2/APIReference/API_EnableDelegatedAdminAccount.md "../../v2/APIReference/API_EnableDelegatedAdminAccount.md") API operation using the credentials of the AWS account of the Organizations management account.
  You can also use the AWS Command Line Interface to do this by running the following CLI command:`aws inspector2 enable-delegated-admin-account --delegated-admin-account-id 11111111111`.

###### Note

Make sure to specify the account ID of the account that you want to make an Amazon Inspector delegated administrator.
