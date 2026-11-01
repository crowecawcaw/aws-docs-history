

# Setting up managed entitlements
<a name="managed-entitlements-setup"></a>

Complete the following setup steps once for your AWS Organization. After setup is complete, you can subscribe to third-party Bedrock models and distribute licenses across your organization. To complete these steps, you need access to your organization's management account.

**Note**  
If you plan to distribute private offers from AWS Marketplace, as described in [Distribute through AWS Marketplace](managed-entitlements-marketplace.md), you don't need to create service-linked roles or link accounts in advance. When you choose **Distribute**, License Manager creates the required service-linked roles and links your accounts automatically. For all other subscriptions, and to designate a delegated administrator, complete the setup steps on this page.

## Step 1: Determine if you need a delegated admin
<a name="managed-entitlements-delegated-admin"></a>

If you will manage licenses directly from the management account, skip to Step 2. To delegate license management to a member account, designate a delegated administrator first.

**To designate a delegated administrator**

1. Sign in to your management account.

1. Open the AWS License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the navigation pane, choose **Settings**.

1. On the **Delegated administration** tab, enter the AWS account ID of the member account you want to designate.

1. Choose **Save changes**.

The delegated administrator account can now create grants and distribute licenses independently from the management account. The delegated administrator can distribute entitlements using individual account IDs, organization ID, or organizational unit IDs.

You can also designate a delegated administrator using the RegisterDelegatedAdministrator API.

To register a delegated administrator with the AWS CLI, run the following command from your management account. Replace {{444455556666}} with the account ID of the member account.

```
aws organizations register-delegated-administrator \
    --account-id {{444455556666}} \
    --service-principal license-manager.amazonaws.com
```

The command uses these values:

`account-id`  
The 12-digit ID of the member account that you want to register as the delegated administrator.

`service-principal`  
Always `license-manager.amazonaws.com`, which registers the account for AWS License Manager managed licenses.

To confirm the registration, run the following command:

```
aws organizations list-delegated-administrators \
    --service-principal license-manager.amazonaws.com
```

If this is the first time you are setting up License Manager for your organization, also run the following commands from your management account to enable the required service access and create the service-linked role:

```
aws organizations enable-aws-service-access --service-principal license-manager.amazonaws.com
aws organizations enable-aws-service-access --service-principal license-manager.member-account.amazonaws.com
aws iam create-service-linked-role --aws-service-name license-manager.amazonaws.com
```

**Important**  
To distribute a private offer from AWS Marketplace with the delegated administrator account, register the account before you accept the private offer, and then accept the offer from that account.

Once designated, the delegated administrator completes Steps 2 and 3 from their account.

## Step 2: Enable service-linked roles and trusted access
<a name="managed-entitlements-enable-slr"></a>

You must enable trusted access and create service-linked roles for both AWS License Manager and AWS Marketplace. Complete these steps from your management account.

**To set up AWS License Manager**

1. Sign in to your management account.

1. Open the AWS License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. Make sure you are in the us-east-1 (N. Virginia) Region. All license resources are created and managed in this region.

1. When you first access AWS License Manager, a popup appears asking you to create a service-linked role. Choose **Create service-linked role** to accept.

1. In the navigation pane, choose **Settings**.

1. On the **Managed licenses** tab, under **Account details**, choose **Link AWS Organizations accounts**.

This enables cross-account grant acceptance and creates a trusted access relationship between AWS Organizations and AWS License Manager.

**To set up AWS Marketplace**

1. While still signed in to your management account, open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/).

1. In the navigation pane, choose **Settings**.

1. Under **AWS License Manager integration**, choose **View setting details**.

1. Select both checkboxes:
   + **Enable trusted access across your organization**
   + **AWS Marketplace license management service-linked role for this account**

1. Choose **Create integration**.

This creates both the service-linked role and trusted access relationship.

**Important**  
When you select **Enable trusted access across your organization** from the management account, service-linked roles are automatically created for all member accounts in your organization. This ensures that any account that receives a grant will be able to use it.

## Step 3: Verify your setup
<a name="managed-entitlements-verify-setup"></a>

After completing the setup steps, verify that everything is configured correctly.

**To verify AWS License Manager configuration**

1. In the AWS License Manager console, choose **Settings** in the navigation pane.

1. On the **Managed licenses** tab, under **Account details**, confirm that your AWS Organizations accounts are linked.

1. The same section shows your account type, the License Manager Amazon S3 bucket ARN, and the AWS RAM share ARN that account linking creates.

**To verify AWS Marketplace configuration**

1. In the AWS Marketplace console, choose **Settings** in the navigation pane.

1. Under **AWS License Manager integration**, confirm that the integration has been created and that trusted access is enabled for your organization.

1. The status labels in this section can change. To confirm the setup definitively, use the service-linked role check that follows.

**To verify service-linked roles**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**.

1. In the search box, enter "AWSServiceRoleForAWSLicenseManager" and verify the role exists.

1. In the search box, enter "AWSServiceRoleForMarketplaceLicenseManagement" and verify the role exists.

If you do not see these roles, wait a few minutes for IAM propagation and refresh the console. If roles still do not appear, you might need to create them manually in the IAM console. Choose **Create role**, select **AWS service**, and then find License Manager or Marketplace in the service list.