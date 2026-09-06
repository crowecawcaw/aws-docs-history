

# Enable trusted access for AWS Account Management
<a name="using-orgs-trusted-access"></a>

These instructions are for how to enable trusted access for AWS Account Management if you signed up for AWS using Sign up for AWS (advanced) or if you activated advanced features for your account. To compare sign-up options, see [Compare sign-up options](sign-up-for-aws.md).

Enabling trusted access for AWS Account Management allows the administrator of the management account to modify the information and metadata (for example, primary or alternate contact details) specific to each member account in AWS Organizations. For more information, see [AWS Account Management and AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html#integrate-enable-ta-account) in the *AWS Organizations User Guide*. For general information about how trusted access works, see [Using AWS Organizations with other AWS services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).

After trusted access has been enabled, you can use the `accountID` parameter in those [Account Management API operations](https://docs.aws.amazon.com/accounts/latest/APIReference/API_Operations.html) that support it. You can use this parameter successfully only if you call the operation using credentials from the management account, or from the delegated admin account for your organization if you enable one. For more information, see [Enable a delegated admin account for AWS Account Management](using-orgs-delegated-admin.md).

Use the following procedure to enable trusted access for Account Management in your organization.

**Minimum permissions**  
To perform these tasks, you must meet the following requirements:  
You can perform this only from the organization's management account.
Your organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html).

------
#### [ AWS Management Console ]

**To enable trusted access for AWS Account Management**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations). You must sign in as an IAM user, assume an IAM role, or sign in as the root user (not recommended) in the organization’s management account.

1. Choose **Services** in the navigation pane.

1. Choose **AWS Account Management** in the list of services.

1. Choose **Enable trusted access**.

1. In the **Enable trusted access for AWS Account Management** dialog box, type **enable** to confirm it, and then choose **Enable trusted access**.

------
#### [ AWS CLI & SDKs ]

**To enable trusted access for AWS Account Management**  
After running the following command, you can use credentials from the organization's management account to call Account Management API operations that use the `--accountId` parameter to reference member accounts in an organization.
+ AWS CLI: [enable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/enable-aws-service-access.html)

  The following example enables trusted access for AWS Account Management in the calling account's organization.

  ```
  $ aws organizations enable-aws-service-access \
      --service-principal account.amazonaws.com
  ```

  This command produces no output if it's successful.

------