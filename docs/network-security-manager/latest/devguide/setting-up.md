

# Setting up AWS Network Security Manager
<a name="setting-up"></a>

With AWS Network Security Manager, you can work in two organizational models. Use it directly in a single account, or use it with AWS Organizations to manage protections across multiple accounts. The setup steps depend on which model you choose.

**Topics**
+ [Choose your organizational model](#setting-up-deployment-mode)
+ [Setting up for single-account use](#setting-up-single-account)
+ [Setting up for multi-account use with AWS Organizations](#setting-up-organizations)
+ [Creating an AWS Network Security Manager administrator account](#setting-up-admin-account)
+ [Create an IAM identity with AWS Network Security Manager permissions](#setting-up-iam)
+ [Using AWS Network Security Manager in Regions that are disabled by default](#setting-up-opt-in-regions)

## Choose your organizational model
<a name="setting-up-deployment-mode"></a>

Choose from the following organizational models:
+ **Single-account** – Use AWS Network Security Manager to protect resources in one account. You do not need AWS Organizations or an administrator account. Create an IAM identity with AWS Network Security Manager permissions and start using the service directly. AWS Network Security Manager automatically creates a service-linked role in your account.
+ **Multi-account** – Use AWS Network Security Manager with AWS Organizations to protect resources across multiple accounts. This mode requires setting up AWS Organizations, enabling trusted access, and creating an administrator account.

## Setting up for single-account use
<a name="setting-up-single-account"></a>

To use AWS Network Security Manager in a single account, create an IAM identity with the appropriate permissions and start using the service directly. You do not need to create an administrator account. AWS Network Security Manager automatically creates a service-linked role in your account in the background. Skip to [Create an IAM identity with AWS Network Security Manager permissions](#setting-up-iam).

## Setting up for multi-account use with AWS Organizations
<a name="setting-up-organizations"></a>

To manage protections across multiple accounts, establish the required AWS Organizations membership and configuration.

1. **Choose an account to use as the AWS Network Security Manager administrator for the organization** – This is the account from which you create and manage AWS Network Security Manager resources.

1. **Verify organization membership** – If your chosen account is not already a member of the organization, have it join. Follow the guidance at [Inviting an AWS account to join your organization](orgs_manage_accounts_invites.html) in the *AWS Organizations User Guide*.

1. **Enable all features in your organization** – AWS Organizations has two available feature sets: consolidated billing features and all features. To use AWS Network Security Manager, your organization must be enabled for all features. If your organization is configured only for consolidated billing, follow the guidance at [Enabling all features in your organization](orgs_manage_org_support-all-features.html) in the *AWS Organizations User Guide*.

1. **Enable trusted access for AWS Network Security Manager** – Enable trusted access for AWS Network Security Manager in AWS Organizations. With trusted access enabled, AWS Network Security Manager can create a service-linked role in member accounts and manage resources on their behalf.

1. **Register a delegated administrator account** – Register your chosen account as a delegated administrator for AWS Network Security Manager in AWS Organizations. Use the Organizations management account to complete this step.

**Multi-account protections disabled when turning off trusted access**  
If you turn off trusted access for AWS Network Security Manager in AWS Organizations, or you deregister a delegated administrator account, AWS Network Security Manager sets the multi-account scope and deployment to a `DISABLED` state and cleans up the protections it manages.

## Creating an AWS Network Security Manager administrator account
<a name="setting-up-admin-account"></a>

This step applies to multi-account mode only. Only the organization's management account can create AWS Network Security Manager administrator accounts.

After you complete the Organizations setup, register your account as an AWS Network Security Manager administrator. You can do this from the console or the AWS Command Line Interface (AWS CLI).

When you create an administrator account, AWS Network Security Manager automatically creates a service-linked role in all accounts in your organization. With this role, AWS Network Security Manager discovers resources and manages protections in member accounts.

With AWS Network Security Manager, you can have multiple administrators who manage the firewall resources of your organization. If you want to use multiple administrators in your organization, you can apply administrative scope conditions to each administrator to define the resources that they can manage. This gives you the flexibility to have different administrator roles within your organization and helps you maintain the principle of least privileged access. For example, one administrator can manage a set of organizational units (OUs). Another administrator can manage only specific policy types.

For the maximum number of administrators that you can have per organization, see [AWS Network Security Manager quotas](quotas.md).

**Region registration**  
You register an AWS Network Security Manager administrator account in a single AWS Region. To use AWS Network Security Manager in additional Regions, repeat this step in each Region.

**To create an administrator account using the console**  


1. Open the AWS Network Security Manager console at [https://console.aws.amazon.com/network-security-manager/](https://console.aws.amazon.com/network-security-manager/).

1. In the navigation pane, choose **Settings**.

1. Choose **Add administrator**.

1. Select the account and enter a priority value (1 to 10).

1. Choose **Add administrator** to confirm.

**To create an administrator account using the AWS CLI**  


Call the `PutAdminAccount` operation. You must provide a priority value (1 to 10).

The following AWS CLI example registers an account as an AWS Network Security Manager administrator with priority 1:

```
aws network-security-manager put-admin-account \
    --account-id 123456789012 \
    --priority 1
```

You can designate multiple administrator accounts, each with a different priority. Optionally, you can limit each administrator to specific accounts, OUs, or firewall types by providing an `adminScope` parameter.

**To remove an administrator account using the console**  


**Multi-account protections disabled when removing an administrator**  
When you remove an administrator account, AWS Network Security Manager sets the multi-account scope and deployment to a `DISABLED` state and cleans up the protections it manages.

1. Open the AWS Network Security Manager console at [https://console.aws.amazon.com/network-security-manager/](https://console.aws.amazon.com/network-security-manager/).

1. In the navigation pane, choose **Settings**.

1. Select the administrator account that you want to remove.

1. Choose **Remove administrator**.

1. To confirm, choose **Confirm administrator deletion**.

## Create an IAM identity with AWS Network Security Manager permissions
<a name="setting-up-iam"></a>

To use AWS Network Security Manager, you need an IAM identity (user or role) with permissions to call AWS Network Security Manager operations. The IAM actions use the prefix `network-security-manager`.

The following example IAM policy contains three statements. The first statement grants full access to all AWS Network Security Manager operations. The second statement grants the additional AWS Organizations and AWS WAF permissions that AWS Network Security Manager needs. AWS Network Security Manager uses these permissions to identify the accounts and organizational units (OUs) in your organization and to list the available WAF rule groups and managed products. These permissions also let AWS Network Security Manager enable trusted access and register a delegated administrator in AWS Organizations. The third statement grants the `iam:CreateServiceLinkedRole` permission that AWS Network Security Manager needs to create its service-linked role, which it requires for both single-account and multi-account use.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "network-security-manager:*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "organizations:DescribeOrganization",
                "organizations:ListAccounts",
                "organizations:ListRoots",
                "organizations:ListOrganizationalUnitsForParent",
                "organizations:ListAccountsForParent",
                "organizations:EnableAWSServiceAccess",
                "organizations:RegisterDelegatedAdministrator",
                "wafv2:ListRuleGroups",
                "wafv2:ListAvailableManagedRuleGroups",
                "wafv2:DescribeAllManagedProducts"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "*"
        }
    ]
}
```

For production use, we recommend that you grant only the minimum permissions required. For more information, see [Identity and access management for AWS Network Security Manager](security-iam.md).

### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Using AWS Network Security Manager in Regions that are disabled by default
<a name="setting-up-opt-in-regions"></a>

To use AWS Network Security Manager in a Region that is disabled by default, you must enable the Region for both the management account of your organization and the AWS Network Security Manager administrator account. For information about Regions that are disabled by default and how to enable them, see [Managing AWS Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html) in the *AWS General Reference*.

**To enable a disabled Region**  


For both the Organizations management account and the AWS Network Security Manager administrator account, follow the guidance at [Enabling a Region](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable) in the *AWS General Reference*.