# Enabling Security Hub

You can enable Security Hub for any AWS account.
This section of the documentation describes all the steps required to enable Security Hub for an AWS Organization, or a standalone account.

## Enable Security Hub for an AWS Organization

This section includes three steps:

- In **Step 1**, the AWS organization management account designates a delegated administrator for their AWS Organization, creates the delegated administrator policy, and optionally enables Security Hub for their own account.
- In **Step 2**, the delegated administrator for the organization enables Security Hub for their own account.
- In **Step 3**, the delegated administrator for the organization configures all member accounts in the organization, for Security Hub and other supported security services.

### Step 1. Delegating an administrator account and optionally enabling Security Hub in the AWS organization management account

###### Note

This step only needs to be completed in one region of the organization management account.

When assigning the delegated administrator account for Security Hub, the account you can choose for your delegated administrator will depend how you have configured a delegated administrator for Security Hub CSPM.
If you have configured a delegated administrator for Security Hub CSPM, and that account is not the organizations management account, then that account will automatically be set as the Security Hub delegated administrator and a different account cannot be chosen.
If the delegated administrator account for Security Hub CSPM is set as the organizations management account or is not set at all, you can choose which account will be your Security Hub delegated administrator account, except for the organizations management account.

For information about designating a delegated administrator in Security Hub, see [Designating a delegated administrator account in Security Hub](securityhub-v2-set-da.md "securityhub-v2-set-da.md").
For information about creating the delegated administrator policy in Security Hub, see [Creating the delegated administrator policy in Security Hub](securityhub-v2-policy-statement.md "securityhub-v2-policy-statement.md").

###### To designate an admistrator for Security Hub

1. Sign in to your AWS account with your AWS organization management account credentials.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. From the Security Hub homepage, select **Security Hub**, and choose **Get started**.
3. In the **Delegated administrator** section, choose an administrator account based on the provided options.
   As a best practice, we recommend using the same delegated administrator across security services for consistent governance.
4. Choose the **Trusted access** checkbox.
   Choosing this option grants your delegated administrator account the ability to configure certain capabilities, such as GuardDuty Malware Protection, on member accounts.
   If you uncheck this option Security Hub will not be able to enable these features on your behalf and you will need to enable them directly through the service that the feature is associated with.
5. (Optional) For **Account enablement**, select the box to enable Security Hub for your AWS account.
6. For **Delegated administrator policy**, choose one of the following options to add the policy statement.
   1. (Option 1) Choose **Update this for me**.
      Select the box under the policy statement to confirm Security Hub will automatically create a delegation policy granting all required permission to the delegated administrator.
   2. (Option 2) Choose **I want to attach this manually**.
      Choose **Copy and attach**.
      In the AWS Organizations console, under **Delegated administrator for AWS Organizations**, choose **Delegate**, and paste the resource policy in the delegation policy editor.
      Choose **Create Policy**.
      Open the tab where you are in the Security Hub console.

7. Choose **Configure**.

### Step 2. Enable Security Hub in the delegated administrator account

The delegated administrator account completes this step.
After the AWS Organization management account designates a delegated administrator for their organization, the delegated administrator must enable Security Hub for their own account before enabling for the entire AWS Organization.

###### To enable Security Hub in the delegated administrator account

1. Sign in to your AWS account with your delegated administrator credentials.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. From the Security Hub homepage and choose **Get started**.
3. The security capabilities section outlines the capabilities that are automatically enabled and includedin the base per-resource price of Security Hub
4. (Optional) For **Tags**, determine whether to add a key-value pair to the account setup.
5. Choose **Enable Security Hub** to finish enabling Security Hub.
6. (Recommended) from the popup choose **Configure my organization** and proceed to Step 3.

After you enable Security Hub, a service-linked role called [AWSServiceRoleForSecurityHubV2](security-iam-awsmanpol.md#security-iam-awsmanpol-awssecurityhubv2servicerolepolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-awssecurityhubv2servicerolepolicy") and a service-linked recorder are created in your account.
The service-linked recorder is a type of AWS Config recorder managed by an AWS service that can record configuration data on service-specific resources.
With a service-linked recorder, Security Hub enables an event-driven approach for obtaining resource configuration items required for exposure analysis coverage and reporting resource inventory.
A service-linked recorder is configured per AWS account and AWS Region.
For global resource types, an additional service-linked recorder is automatically created in the home region to record configuration changes for global resources, as AWS Config only records global resource types in their designated home region.
For more information, see [Considerations for service-linked configuration recorders](../../../config/latest/developerguide/stop-start-recorder.md#stop-start-recorder-considerations-service-linked "../../../config/latest/developerguide/stop-start-recorder.md#stop-start-recorder-considerations-service-linked") and [Recording regional and global resources](../../../config/latest/developerguide/select-resources.md#select-resources-all "../../../config/latest/developerguide/select-resources.md#select-resources-all").

### Step 3. Create a policy that enables Security Hub in all member accounts

After enbling Security Hub in the delegated administrator account for an organization you need to create a policy that defines which services and capabilities are enabled in the organization member accounts.
For more information, see [Enabling a configuration with a type of policy](securityhub-v2-da-policy.md#securityhub-v2-configuration-enable-policy "securityhub-v2-da-policy.md#securityhub-v2-configuration-enable-policy").

## Enable Security Hub in a standalone account

This procedure describes how to enable Security Hub in a standalone account.
A standalone account is an AWS account that has not enabled AWS organizations.

###### To enable Security Hub in a standalone account

1. Sign in to your AWS account with your account credentials.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. From the Security Hub homepage, select **Get started**.
3. In the **Security capabilities** section do one of the following:
   1. (Option 1) Choose **Enable all capabilities**.
      This will turn on all of the Security Hub essential capabilties, threat analytics, and additional capabilties.
   2. (Option 2) Choose **Customize capabilities**.
      Select the threat analytics and additional capabilities that should be turned on.
      You cannot deselect any capabilities that are part of the Security Hub essential plan capabilities.

4. In the **Regions** section, choose **Enable all Regions** or **Enable specific Regions**.
   If you choose **Enable all Regions**, you can determine whether to automatically enable new Regions.
   If you choose **Enable specific Regions**, you must choose which Regions you want to enable.
5. (Optional) For **Resource tags**, add tags as key-value pairs to help you easily identify the configuration.
6. Choose **Enable Security Hub**.

After you enable Security Hub, a service-linked role called [AWSServiceRoleForSecurityHubV2](security-iam-awsmanpol.md#security-iam-awsmanpol-awssecurityhubv2servicerolepolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-awssecurityhubv2servicerolepolicy") and a service-linked recorder are created in your account.
The service-linked recorder is a type of AWS Config recorder managed by an AWS service that can record configuration data on service-specific resources.
With a service-linked recorder, Security Hub enables an event-driven approach for obtaining resource configuration items required for exposure analysis coverage and reporting resource inventory.
A service-linked recorder is configured per AWS account and AWS Region.
For global resource types, an additional service-linked recorder is automatically created in the home region to record configuration changes for global resources, as AWS Config only records global resource types in their designated home region.
For more information, see [Considerations for service-linked configuration recorders](../../../config/latest/developerguide/stop-start-recorder.md#stop-start-recorder-considerations-service-linked "../../../config/latest/developerguide/stop-start-recorder.md#stop-start-recorder-considerations-service-linked") and [Recording regional and global resources](../../../config/latest/developerguide/select-resources.md#select-resources-all "../../../config/latest/developerguide/select-resources.md#select-resources-all").
