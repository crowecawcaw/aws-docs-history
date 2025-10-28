# Getting started tutorial: Activating Amazon Inspector

This topic describes how to activate Amazon Inspector for a standalone account environment (member account) and multi-account environment (delegated administrator account).
When you activate Amazon Inspector, it automatically begins discovering workloads and scanning them for software vulnerabilities and unintended network exposure.

Standalone account environment

The following procedure describes how to activate Amazon Inspector in the console for a member account.
To programatically activate Amazon Inspector, [inspector2-enablement-with-cli](https://github.com/aws-samples/inspector2-enablement-with-cli "https://github.com/aws-samples/inspector2-enablement-with-cli").

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. Choose **Get Started**.
3. Choose **Activate Amazon Inspector**.

When you activate Amazon Inspector for a standalone account, [all scan types](scanning-resources.md "scanning-resources.md") are activated by default.
For information about member accounts, see [Understanding the delegated administrator account and member accounts in Amazon Inspector](managing-multiple-accounts.md "managing-multiple-accounts.md").

Multi-account environment

The following procedure describes how to activate Amazon Inspector in the console for a delegated administrator account.
To programatically activate Amazon Inspector for multiple accounts, use the Amazon Inspector [inspector2-enablement-with-cli](https://github.com/aws-samples/inspector2-enablement-with-cli "https://github.com/aws-samples/inspector2-enablement-with-cli") shell script.

###### Note

You must use the AWS Organizations management account to complete this procedure.
Only the AWS Organizations management account can designate a delegated administrator.
Permissions might be required to designate a delegated administrator.
For more information, see [Permissions required to designate a delegated administrator](designating-admin.md#delegated-admin-permissions "designating-admin.md#delegated-admin-permissions").

When you activate Amazon Inspector for the first time, Amazon Inspector creates the service linked role `AWSServiceRoleForAmazonInspector` for the account.
For information about how Amazon Inspector uses service-linked roles, see [Using service-linked roles for Amazon Inspector](using-service-linked-roles.md "using-service-linked-roles.md").

**To designate a delegated administrator for Amazon Inspector**

1. Sign in to the AWS Organizations management account, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. Choose **Get started**.
3. Under **Delegated administrator**, enter the 12-digit ID of the AWS account you want to designate as the delegated administrator.
4. Choose **Delegate**, and then choose **Delegate** again.
5. (Optional) If you want to activate Amazon Inspector for the AWS Organizations management account, choose **Activate Amazon Inspector** under **Service permissions**.

When you designate a delegated administrator, [all scan types](scanning-resources.md "scanning-resources.md") are activated for the account by default.
For information about the delegated administrator account,see [Understanding the delegated administrator account and member accounts in Amazon Inspector](managing-multiple-accounts.md "managing-multiple-accounts.md").
