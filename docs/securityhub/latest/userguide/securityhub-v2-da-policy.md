# Managing configuration of member accounts in an AWS Organization

The delegated administrator for an AWS Organization can configure security capabilities across member accounts and Regions.
There are two types of configurations that are available, **Policies** and **Deployments**.
**Policies** generate AWS Organizations policies for accounts and Regions for AWS Security Hub and Amazon Inspector.
**Deployments** are a one-time action to enable a security capability across selected accounts and Regions for Amazon GuardDuty and AWS Security Hub CSPM.
Unlike policies, you cannot view or edit deployments and deployments will not apply to newly enabled accounts.
As an alternative, auto-enable features, for new member accounts, are available in Amazon GuardDuty and AWS Security Hub CSPM.

## Security Hub configuration catalog

The configuration catalog of Security Hub offers multiple options to help configure your AWS Organization accounts for the security capabilities provided by .

The following are the options available in the Security Hub configuration catalog.

### Security Hub (essential and additional capabilities)

This is the recommended configuration to deploy for Security Hub.

**Type**: Policy and Deployments

**Description**: This configuration tyurns on Security Hub's essential security management, posture management, threat analytics, and vulnerability management capabilities.
It optionally enables additional capabilities.

### Threat analytics from GuardDuty

**Type**: Deployment

**Description**: Turn on selected Amazon GuardDuty capabilities to continuously monitor, analyze, and process AWS data sources and logs in your AWS environment.

### Posture management from AWS Security Hub CSPM)

**Type**: Deployment

**Description**: This configuration turns on Security Hub CSPM's standards and controls which detects when your AWS accounts and resources deviate from security best practices.

### Vulnerability management from Amazon Inspector

**Type**: Policy

**Description**: This configuration turns on selected Amazon Inspector capabilities that automatically discover workloads, instances, container images, etc., and scans them for vulnerabilities and network exposure.

## Enabling a configuration with a type of policy

The following procedure describes how to create a configuration with a type of policy for your AWS Organization accounts.
To create a configuration policy the delegated administrator policy needs to be created in the AWS Organization management account.
For information about creating the delegated administrator policy in Security Hub, see [Creating the delegated administrator policy in Security Hub](securityhub-v2-policy-statement.md "securityhub-v2-policy-statement.md").

###### To create a policy that enables and disables member accounts

1. Sign in using your AWS account with your delegated administrator credentials.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home? "https://console.aws.amazon.com/securityhub/v2/home?").
2. From the navigation pane, choose **Management**, and then choose **Configurations**.
3. Choose an item with a type of **policy** or **policy and deployment** from the Configuration catalog.
   To fully configure Security Hub it is recommended to choose **Security Hub (essential and additional capabilities)**.
4. On the **Configure Security Hub** page in the **Details** section enter a name and a description for the policy.
5. In the **Security capabilities** section do one of the following:
   1. (Option 1) Choose **Enable all capabilities**.
      This will turn on all of the Security Hub essential capabilties, threat analytics, and additional capabilties.
   2. (Option 2) Choose **Customize capabilities**.
      Select the threat analytics and additional capabilities that should be turned on.
      You cannot deselect any capabilities that are part of the Security Hub essential plan capabilities.

6. In the **Account selection** section, select one of the following options.
   Choose **All organizational units and accounts** if you want to apply the configuration to all organizational units and accounts.
   Choose **Specific organizational units and accounts** if you want to apply the configuration to specific organizational units and accounts.
   If you choose this option, use the search bar or organizational structure tree to specify the organizational units and accounts where the policy will be applied.
   Choose **No organizational units or accounts** if you do not want to apply the configuration to any organizational unit or account.
7. In the **Regions** section, choose **Enable all Regions**, **Disable all Regions**, or **Specify Regions**.
   If you choose **Enable all Regions**, you can determine whether to automatically enable new Regions.
   If you choose **Disable all Regions**, you can determine whether to automatically disable new Regions.
   If you choose **Specify Regions**, you must choose which Regions you want to enable and disable.
8. (Optional) For **Advanced settings**, please refer to the [guidance](../../../organizations/latest/userguide/policy-operators.md "../../../organizations/latest/userguide/policy-operators.md") from AWS Organizations.
9. (Optional) For **Resource tags**, add tags as key-value pairs to help you easily identify the configuration.
10. Choose **Next**.
11. Review your changes, and then choose **Apply**.
    Your target accounts are configured based on the policy. The configuration status of your policy will display at the top of the Policies page.
    Each capability will provide a status on if it was configured or where there are deployment failures.
    For any failures click on the link for the failure message to see more details.
    To view the effective policy at the account level, you can review the **Organization** tab on the **Configurations** page where you can choose an account.

## Enabling a configuration with a type of deployment

The following procedure describes how to create a configuration with a type of deployment for your AWS Organization accounts.

###### To create a deployment that enables and disables member accounts

1. Sign in using your AWS account with your delegated administrator credentials.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home? "https://console.aws.amazon.com/securityhub/v2/home?").
2. From the navigation pane, choose **Management**, and then choose **Configurations**.
3. Choose an item with a type of **deployment** from the Configuration catalog.
   To fully configure Security Hub it is recommended to choose **Security Hub (essential and additional capabilities)**.
4. In the **Security capabilities** section
   Select the security capabilities that should be turned on.
5. In the **Account selection** section, select one of the following options.
   Choose **All organizational units and accounts** if you want to apply the configuration to all organizational units and accounts.
   Choose **Specific organizational units and accounts** if you want to apply the configuration to specific organizational units and accounts.
   If you choose this option, use the search bar or organizational structure tree to specify the organizational units and accounts where the policy will be applied.
   Choose **No organizational units or accounts** if you do not want to apply the configuration to any organizational unit or account.
6. In the **Regions** section, choose **Enable all Regions**, **Disable all Regions**, or **Specify Regions**.
   If you choose **Enable all Regions**, you can determine whether to automatically enable new Regions.
   If you choose **Disable all Regions**, you can determine whether to automatically disable new Regions.
   If you choose **Specify Regions**, you must choose which Regions you want to enable and disable.
7. Choose **Configure**.

## Editing a configuration policy

You can edit the capabilities, Regions, and accounts assocaited with configurations that have a type of **policy**.

The following describes how to edit a configuration policy in Security Hub

###### To create edit a configuration policy

1. Sign in using your AWS account with your delegated administrator credentials.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home? "https://console.aws.amazon.com/securityhub/v2/home?").
2. From the navigation pane, choose **Management**, and then choose **Configurations**.
3. In the **Configured policies** tab select the radio button for the policy you want to edit.
   Choose the **Edit**.
4. To make changes in the **Account selection** section, select one of the following options.
   Choose **All organizational units and accounts** if you want to apply the configuration to all organizational units and accounts.
   Choose **Specific organizational units and accounts** if you want to apply the configuration to specific organizational units and accounts.
   If you choose this option, use the search bar or organizational structure tree to specify the organizational units and accounts where the policy will be applied.
   Choose **No organizational units or accounts** if you do not want to apply the configuration to any organizational unit or account.
5. To make changes in the **Regions** section, choose **Enable all Regions**, **Disable all Regions**, or **Specify Regions**.
   If you choose **Enable all Regions**, you can determine whether to automatically enable new Regions.
   If you choose **Disable all Regions**, you can determine whether to automatically disable new Regions.
   If you choose **Specify Regions**, you must choose which Regions you want to enable and disable.
6. Choose **Next**.
7. Review your changes, and then choose **Update**.
   Your target accounts are configured based on the policy.

## Deleting a configuration policy

You can delete configuration that you have a type of **policy**.
When you delete a policy all attached accounts and organiational units will be removed from the policy.

The following describes how to delete a configuration policy in Security Hub.

###### To create delete a configuration policy

1. Sign in using your AWS account with your delegated administrator credentials.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home? "https://console.aws.amazon.com/securityhub/v2/home?").
2. From the navigation pane, choose **Management**, and then choose **Configurations**.
3. In the **Configured policies** tab select the radio button for the policy you want to edit.
   Choose the **Delete** button.
4. Type **delete** in the confirmation box.
   Choose the **Delete**.
