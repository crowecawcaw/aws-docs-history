# Enable trusted access for AWS Account Management

Enabling trusted access for AWS Account Management allows the administrator of the management account
to modify the information and metadata (for example, primary or alternate contact details)
specific to each member account in AWS Organizations. For more information, see [AWS Account Management and AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-account.md#integrate-enable-ta-account "../../../organizations/latest/userguide/services-that-can-integrate-account.md#integrate-enable-ta-account") in the _AWS Organizations User Guide_. For
general information about how trusted access works, see [Using AWS Organizations with other AWS
services](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md").

After trusted access has been enabled, you can use the `accountID` parameter in
those [Account Management API operations](API_Operations.md "API_Operations.md") that support it. You can
use this parameter successfully only if you call the operation using credentials from the
management account, or from the delegated admin account for your organization if you enable
one. For more information, see [Enable a delegated admin account for
AWS Account Management](using-orgs-delegated-admin.md "using-orgs-delegated-admin.md").

Use the following procedure to enable trusted access for Account Management in your
organization.

###### Minimum permissions

To perform these tasks, you must meet the following requirements:

- You can perform this only from the organization's management account.
- Your organization must have [all features
  enabled](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md").

AWS Management Console

###### To enable trusted access for AWS Account Management

1. Sign in to the [AWS Organizations
   console](https://console.aws.amazon.com/organizations "https://console.aws.amazon.com/organizations"). You must sign in as an IAM user, assume an IAM
   role, or sign in as the root user (not recommended) in the
   organization’s management account.
2. Choose **Services** in the navigation pane.
3. Choose **AWS Account Management** in the list of services.
4. Choose **Enable trusted access**.
5. In the **Enable trusted access for AWS Account Management**
   dialog box, type **enable** to confirm it, and then
   choose **Enable trusted access**.

AWS CLI & SDKs

###### To enable trusted access for AWS Account Management

After running the following command, you can use credentials from the
organization's management account to call Account Management API operations that use the
`--accountId` parameter to reference member accounts in an
organization.

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

The following example enables trusted access for AWS Account Management in the
calling account's organization.

```
`$` `aws organizations enable-aws-service-access \
 --service-principal account.amazonaws.com`
```

This command produces no output if it's successful.
