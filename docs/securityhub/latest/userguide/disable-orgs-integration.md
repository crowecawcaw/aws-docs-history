# Disabling Security Hub CSPM integration with AWS Organizations

After an AWS Organizations organization is integrated with AWS Security Hub CSPM, the Organizations management account
can subsequently disable the integration. As a user of the Organizations management account, you
can do this by disabling trusted access for Security Hub CSPM in AWS Organizations.

When you disable trusted access for Security Hub CSPM, the following occurs:

- Security Hub CSPM loses its status as a trusted service in AWS Organizations.
- The Security Hub CSPM delegated administrator account loses access to Security Hub CSPM settings, data, and resources
  for all Security Hub CSPM member accounts in all AWS Regions.
- If you were using [central configuration](central-configuration-intro.md "central-configuration-intro.md"), Security Hub CSPM automatically stops using it for your organization.
  Your configuration policies and policy associations are deleted. Accounts retain the configurations that they had before
  you disabled trusted access.
- All Security Hub CSPM member accounts become standalone accounts and retain their current settings. If Security Hub CSPM was enabled for a
  member account in one or more Regions, Security Hub CSPM continues to be enabled for the account in
  those Regions. Enabled standards and controls are also unchanged. You can change these settings
  separately in each account and Region. However, the account is no longer associated with a delegated administrator in any Region.
  For additional information about the results of disabling trusted service access, see [Using AWS Organizations with other AWS services](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md") in the _AWS Organizations User Guide_.

To disable trusted access, you can use the AWS Organizations console, Organizations API, or the AWS CLI.
Only a user of the Organizations management account can disable trusted service access for
Security Hub CSPM. For details about the permissions that you need, see [Permissions required to disable trusted access](../../../organizations/latest/userguide/orgs_integrate_services.md#orgs_trusted_access_disable_perms "../../../organizations/latest/userguide/orgs_integrate_services.md#orgs_trusted_access_disable_perms") in the _AWS Organizations User Guide_.

Before you disable trusted access, we recommend working with the delegated administrator for
your organization to disable Security Hub CSPM in member accounts and to clean up Security Hub CSPM
resources in those accounts.

Choose your preferred method, and follow the steps to disable trusted access for Security Hub CSPM.

Organizations console

###### To disable trusted access for Security Hub CSPM

1. Sign in to the AWS Management Console using the credentials of the AWS Organizations management account.
2. Open the Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/ "https://console.aws.amazon.com/organizations/").
3. In the navigation pane, choose **Services**.
4. Under **Integrated services**, choose
   **AWS Security Hub CSPM**.
5. Choose **Disable trusted access**.
6. Confirm that you want to disable trusted access.

Organizations API
**To disable trusted access for Security Hub CSPM**

Invoke the [DisableAWSServiceAccess](../../../organizations/latest/APIReference/API_DisableAWSServiceAccess.md "../../../organizations/latest/APIReference/API_DisableAWSServiceAccess.md") operation of the AWS Organizations API. For the
`ServicePrincipal` parameter, specify the Security Hub CSPM service principal
(`securityhub.amazonaws.com`).

AWS CLI
**To disable trusted access for Security Hub CSPM**

Run the [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md") command of the AWS Organizations API. For the
`service-principal` parameter, specify the Security Hub CSPM service principal
(`securityhub.amazonaws.com`).

**Example:**

```
aws organizations disable-aws-service-access --service-principal securityhub.amazonaws.com
```
