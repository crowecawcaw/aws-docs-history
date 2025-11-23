# Enabling Security Hub

###### Note

Security Hub is in preview release and is subject to change.

You can enable Security Hub for any AWS account.
The procedures in this topic describe how to enable Security Hub from an AWS organization management account, a delegated administrator account, and a standalone account.

## Enable Security Hub for an organization

This section includes three steps.
In Step 1, the AWS organization management account enables Security Hub, designates a delegated administrator for their organization, and creates the delegated administrator policy.
In Step 2, the delegated administrator for the organization enables Security Hub.
In Step 3, the delegated administrator for the organization creates a policy that enables Security Hub for all member accounts in the organization.

### Step 1. Enable Security Hub in the AWS organization management account

###### Note

This step only needs to be completed in one region of the organization management account.

This step includes two procedures.
The first procedure describes how to enable Security Hub if you enabled Security Hub CSPM and designated a delegated administrator in Security Hub CSPM.
The second procedure describes how to enable Security Hub if you have not enabled Security Hub CSPM and designated a delegated administrator in Security Hub CSPM.
In both procedures, if you skip the step to designate a delegated administrator, you must skip the step to create the delegated administrator policy.
You can only create the delegated administrator policy after you designate a delegated administrator.
For information about designating a delegated administrator in Security Hub, see [Designating a delegated administrator account in Security Hub](securityhub-v2-set-da.md#securityhub-v2-policy-statement "securityhub-v2-set-da.md#securityhub-v2-policy-statement").
For information about creating the delegated administrator policy in Security Hub, see [Creating the delegated administrator policy in Security Hub](securityhub-v2-policy-statement.md "securityhub-v2-policy-statement.md").

Enable Security Hub with Security Hub CSPM

This procedure assumes the AWS organization management account previously enabled Security Hub CSPM and designated a delegated administrator in Security Hub CSPM.

###### To enable Security Hub

1. Sign in to your AWS account with your AWS organization management account credentials.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. From the Security Hub homepage, select **Security Hub**, and choose **Get started**.
3. (Optional) For **Delegated administrator account**, choose an administrator account based on the provided options.
   As a best practice, we recommend using the same delegated administrator across security services for consistent governance.
4. (Optional) For **Account enablement**, select the box to enable Security Hub for your AWS account.
5. (Optional) For **Delegated administrator policy**, choose one of the following options to add the policy statement.
   1. (Option 1) Choose **Update this for me**.
      Select the box under the policy statement to confirm Security Hub will automatically create a delegation policy granting all required permission to the delegated administrator.
   2. (Option 2) Choose **I want to attach this manually**.
      Choose **Copy and attach**.
      In the AWS Organizations console, under **Delegated administrator for AWS Organizations**, choose **Delegate**, and paste the resource policy in the delegation policy editor.
      Choose **Create Policy**.
      Open the tab where you are in the Security Hub console.

6. Choose **Configure**.

Enable Security Hub without Security Hub CSPM

This procedure assumes the AWS organization management account has not previously enabled Security Hub CSPM and designated a delegated administrator in Security Hub CSPM.

###### To enable Security Hub

1. Sign in to your AWS account with your organization management account credentials, and open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. From the Security Hub homepage, select **Security Hub**, and choose **Get started**.
3. (Optional) For **Delegated administrator**, select one of the provided AWS accounts or **Choose an account**.
   If you select **Choose an account**, enter the 12-digit number for the AWS account you want to designate as the delegated administrator in Security Hub.
4. (Optional) For **Account enablement**, select the box to enable Security Hub for your AWS account.
5. (Optional) For **Delegated administrator policy**, choose one of the following options to add the policy statement:
   1. (Option 1) Choose **Update this for me**.
      Select the box under the policy statement to confirm Security Hub will automatically create a delegation policy granting all required permission to the delegated administrator.
   2. (Option 2) Choose **I want to attach this manually**.
      Choose **Copy and attach**.
      In the AWS Organizations console, under **Delegated administrator for AWS Organizations**, choose **Delegate**, and paste the resource policy in the delegation policy editor.
      Choose **Create Policy**.
      Open the tab where you are in the Security Hub console.

6. Choose **Configure**.

After you enable Security Hub, a service-linked role called [AWSServiceRoleForSecurityHubV2](security-iam-awsmanpol.md#security-iam-awsmanpol-awssecurityhubv2servicerolepolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-awssecurityhubv2servicerolepolicy") and a service-linked recorder are created in your account.
The service-linked recorder is a type of AWS Config recorder managed by an AWS service that can record configuration data on service-specific resources.
With a service-linked recorder, Security Hub enables an event-driven approach for obtaining resource configuration items required for exposure analysis coverage and reporting resource inventory.
A service-linked recorder is configured per AWS account and AWS Region.
For global resource types, an additional service-linked recorder is automatically created in the home region to record configuration changes for global resources, as AWS Config only records global resource types in their designated home region.
For more information, see [Considerations for service-linked configuration recorders](../../../config/latest/developerguide/stop-start-recorder.md#stop-start-recorder-considerations-service-linked "../../../config/latest/developerguide/stop-start-recorder.md#stop-start-recorder-considerations-service-linked") and [Recording regional and global resources](../../../config/latest/developerguide/select-resources.md#select-resources-all "../../../config/latest/developerguide/select-resources.md#select-resources-all").

### Step 2. Enable Security Hub in the delegated administrator account

This step is for the delegated administrator to complete.
After the AWS organization management account designates a delegated administrator for their organization, the delegated administrator must enable Security Hub.

###### To enable Security Hub in the delegated administrator account

1. Sign in to your AWS account with your delegated administrator credentials.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. From the Security Hub homepage, select **Security Hub**, and choose **Get started**.
3. Choose **Enable**.
4. (Optional) For **Tags**, determine whether to add a key-value pair to the account setup.
5. Choose **Go to Security Hub**.

After you enable Security Hub, a service-linked role called [AWSServiceRoleForSecurityHubV2](security-iam-awsmanpol.md#security-iam-awsmanpol-awssecurityhubv2servicerolepolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-awssecurityhubv2servicerolepolicy") and a service-linked recorder are created in your account.
The service-linked recorder is a type of AWS Config recorder managed by an AWS service that can record configuration data on service-specific resources.
With a service-linked recorder, Security Hub enables an event-driven approach for obtaining resource configuration items required for exposure analysis coverage and reporting resource inventory.
A service-linked recorder is configured per AWS account and AWS Region.
For global resource types, an additional service-linked recorder is automatically created in the home region to record configuration changes for global resources, as AWS Config only records global resource types in their designated home region.
For more information, see [Considerations for service-linked configuration recorders](../../../config/latest/developerguide/stop-start-recorder.md#stop-start-recorder-considerations-service-linked "../../../config/latest/developerguide/stop-start-recorder.md#stop-start-recorder-considerations-service-linked") and [Recording regional and global resources](../../../config/latest/developerguide/select-resources.md#select-resources-all "../../../config/latest/developerguide/select-resources.md#select-resources-all").

### Step 3. Create a policy that enables Security Hub in all member accounts

This step is for the delegated administrator to complete.
After the delegated administrator for an organization enables Security Hub, it must create a policy allowing it to define which member accounts in an organization are enabled and disabled.
For more information, see [Creating a policy as the delegated administrator to manage member accounts](security-hub-v2-da-policy.md "security-hub-v2-da-policy.md").

## Enable Security Hub in a standalone account

This procedure describes how to enable Security Hub in a standalone account.
A standalone account is an AWS account that has not enabled AWS organizations.

###### To enable Security Hub in a standalone account

1. Sign in to your AWS account with your standalone account credentials.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. From the Security Hub homepage, select **Security Hub**, and choose **Get started**.
3. Choose **Enable**.

After you enable Security Hub, a service-linked role called [AWSServiceRoleForSecurityHubV2](security-iam-awsmanpol.md#security-iam-awsmanpol-awssecurityhubv2servicerolepolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-awssecurityhubv2servicerolepolicy") and a service-linked recorder are created in your account.
The service-linked recorder is a type of AWS Config recorder managed by an AWS service that can record configuration data on service-specific resources.
With a service-linked recorder, Security Hub enables an event-driven approach for obtaining resource configuration items required for exposure analysis coverage and reporting resource inventory.
A service-linked recorder is configured per AWS account and AWS Region.
For global resource types, an additional service-linked recorder is automatically created in the home region to record configuration changes for global resources, as AWS Config only records global resource types in their designated home region.
For more information, see [Considerations for service-linked configuration recorders](../../../config/latest/developerguide/stop-start-recorder.md#stop-start-recorder-considerations-service-linked "../../../config/latest/developerguide/stop-start-recorder.md#stop-start-recorder-considerations-service-linked") and [Recording regional and global resources](../../../config/latest/developerguide/select-resources.md#select-resources-all "../../../config/latest/developerguide/select-resources.md#select-resources-all").
