

# Update your AWS account name
<a name="manage-acct-update-acct-name"></a>

These instructions are for how to update your AWS account name if you signed up for AWS using Sign up for AWS (advanced) or if you activated advanced features for your account. To compare sign-up options, see [Compare sign-up options](sign-up-for-aws.md).

When managing multiple AWS accounts, use clear naming conventions aligned with business units and applications for identification and organization. During reorganizations, mergers, acquisitions, or naming convention updates, you might need to rename accounts to maintain consistent identification and administrative standards.

The name of an account appears in several places, such as on your invoice and in consoles such as the Billing and Cost Management dashboard and the AWS Organizations console. We recommend that you use a standard way to name your accounts so that your account names are easy to recognize. For company accounts, consider using a naming standard such as *organization*-*purpose*-*environment* (for example, *sales*-*catalog*-*prod*). For privacy and security reasons, avoid using account names that reflect personally identifiable information (PII).
+ **Standalone AWS accounts or management accounts –** For AWS accounts not associated with an organization, or for the management account of an organization, you can update your account name using the AWS Management Console, or the AWS CLI and SDKs. To learn how to do this, see [Update your account name for a standalone AWS account or management account](#update-account-name-standalone).
+ **AWS accounts within an organization –** For member accounts that are part of an AWS Organizations, a user in the management account or delegated admin account can centrally update the account name of any member account in the organization from the AWS Organizations console, or programmatically via the AWS CLI and SDKs. To learn how to do this, see [Update your account name for any AWS account in your organization](#update-account-name-orgs).

**Note**  
Changes to an AWS account can take up to four hours to propagate everywhere.

**Topics**
+ [Update your account name for a standalone AWS account or management account](#update-account-name-standalone)
+ [Update your account name for any AWS account in your organization](#update-account-name-orgs)

## Update your account name for a standalone AWS account or management account
<a name="update-account-name-standalone"></a>

To change the account name for a standalone AWS account or a management account, perform the steps in the following procedure.

------
#### [ AWS Management Console ]

**Minimum permissions**  
You can update your account name using the root user, an IAM user, or an IAM role. If you are using the root user, no additional IAM permissions are needed to update an account name. When using an IAM user or IAM role, you must have at least the following IAM permissions:  
`account:GetAccountInformation`
`account:PutAccountName`

**To update the account name for a standalone account or management account**

1. Use your AWS account's email address and password to sign in to the [AWS Management Console](https://console.aws.amazon.com/) as your AWS account root user.

1. In the upper right corner of the console, choose your account name or number and then choose **Account**.

1. On the [**Account** page](https://console.aws.amazon.com/billing/home#/account), next to **Account details**, choose **Actions** and then select **Update account name**. 

1. Under **Name**, enter the new account name you want to update, and then choose **Save**.

------
#### [ AWS CLI & SDKs ]

**Minimum permissions**  
You can update your account name using the root user, an IAM user, or an IAM role. To perform the following steps, your IAM user or IAM role must have at least the following IAM permissions:  
`account:GetAccountInformation`
`account:PutAccountName`

**To update the account name for a standalone account or management account**  
You can use one of the following operations:
+ AWS CLI: [put-account-name](https://docs.aws.amazon.com/cli/latest/reference/account/put-account-name.html)

  ```
  $ C:\> aws account put-account-name \
          --account-name "{{New-Account-Name}}"
  ```
+ AWS SDKs: [PutAccountName](https://docs.aws.amazon.com/accounts/latest/APIReference/API_PutAccountName.html)

------

## Update your account name for any AWS account in your organization
<a name="update-account-name-orgs"></a>

In AWS Organizations with all features mode, authorized IAM users or IAM roles in both management and delegated admin accounts can centrally manage account names.

To change the account name for any member account in your organization, perform the steps in the following procedure.

### Requirements
<a name="update-account-name-orgs-requirement"></a>

To update an account name with the AWS Organizations console, you need to do some preliminary settings:
+ Your organization must enable *all features* to manage settings on your member accounts. This allows admin control over the member accounts. This is set by default when you create your organization. If your organization is set to *consolidated billing* only, and you want to enable all features, see [Enabling all features for an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html).
+ You need to enable trusted access for the AWS Account Management service. To set this up, see [Enable trusted access for AWS Account Management](using-orgs-trusted-access.md).

------
#### [ AWS Management Console ]

**Minimum permissions**  
To update the account name for a member account, your IAM user or IAM role must have the following permissions:  
`organizations:DescribeOrganization` (console only)
`account:PutAccountName`

**To update the account name for a member account**

1. Open the Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/).

1. In the main navigation pane, choose **AWS accounts**.

1. On the **AWS accounts** page, choose the member account that you want to update, choose the **Actions** drop-down menu, and then choose **Update account name**.

1. Under **Name**, enter the updated name, and choose **Save**.

------
#### [ AWS CLI & SDKs ]

**Minimum permissions**  
To update the account name for a member account, your IAM user or IAM role must have the following permissions:  
`organizations:DescribeOrganization` (console only)
`account:PutAccountName`

**To update the account name for a member account**  
You can use one of the following operations:
+ AWS CLI: [put-account-name](https://docs.aws.amazon.com/cli/latest/reference/account/put-account-name.html)

  ```
  $ C:\> aws account put-account-name \
          --account-id {{111111111111}} \
          --account-name "{{New-Account-Name}}"
  ```
+ AWS SDKs: [PutAccountName](https://docs.aws.amazon.com/accounts/latest/APIReference/API_PutAccountName.html)

------