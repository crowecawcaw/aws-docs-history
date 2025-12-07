# Public Preview to General Availability migration

This topic describes how to enable the Security Hub General Availability (GA) experience as a public preview user.
You must take action to continue using Security Hub or your preview service will be automatically disabled.
Disabling Security Hub does not impact any existing configurations for Security Hub CSPM. Security Hub CSPM will continue to work without any disruptions or changes.
For more details on how Security Hub and Security Hub CSPM compares you can reference [What are Security Hub and Security Hub CSPM?](what-are-securityhub-services.md "what-are-securityhub-services.md").

###### Action required by January 15, 2026 to avoid disruptions

If you do not opt-into the GA experience for Security Hub by January 15th 2026, Security Hub will automatically be disabled organization-wide across all accounts and Regions.
All current Security Hub configurations will be removed, new findings will not be integrated, existing findings will be deleted once they age out, and organization policies will remain in failed state until policies are deleted via console or API.
Re-enabling the service will require following the steps outlined in [Enabling Security Hub](securityhub-v2-enable.md "securityhub-v2-enable.md").

To opt-in to the GA experience for Security Hub, your AWS Organizations management or delegated administrator account can opt-in for the entire organization using a single click in the console or calling the [EnableSecurityHubV2](../../1.0/APIReference/API_EnableSecurityHubV2.md "../../1.0/APIReference/API_EnableSecurityHubV2.md") API in that account.
The settings and enablement you configured during the preview period will be retained until you opt-in to the GA experience, or until the time to opt-in to the GA expires on January 15th 2026.
Until you opt into the GA experience only read only APIs for Security Hub will work. Any automation rules that are defined to interact with Jira or ServiceNow connectors will continue to work for new or updated findings.
Making updates to your Security Hub configuration will require opting into the GA experience.

## Organization Management accounts

###### To migrate from Public Preview to General Availability using the AWS Organization management account (console)

1. Sign in to your AWS account with your AWS organization management account credentials.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. From the **General Availability** section choose the option you would like to proceed with:
   1. If you want to opt into the paid General Availability experience choose **Continue with Security Hub General Availability**.
      1. Review the **Delegated administrator policy** section.
         You will see a message of **You are missing permissions which are required to manage policies in Security Hub**.
      2. If your current policy has not been modified choose **Update**.
         Review the new policy, click the confirm checkbox, and choose the **Update** button to apply the updated policy.
      3. If you have modified the delegated administrator policy you must add the new policy details.
         Choose the **Copy and attach** option. In the console, under Delegated administrator for , choose **Delegate**, and paste the resource policy in the delegation policy editor.
         Choose **Create Policy**. You can then return to the tab where you are in the Security Hub console.
      4. Choose **Enable** to complete opting in.

   2. If you do not want to continue with the paid General Availability experience choose **Disable Security Hub**.
      1. Select the check box acknowledging you want to disable the service.
      2. Choose **Disable**.

## Delegated Admin Accounts

###### To migrate using the delegated administrator account (console)

1. Sign in to your AWS account with your delegated administrator credentials.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. You will be directed to the onboarding form for General Availability.
3. From the **General Availability** page choose **Continue with Security Hub General Availability** to opt into the paid General Availability experience then choose **Enable** to complete opting in.
   If you do not wish to continue with the General Availability experience, choose **Disable Security Hub**, acknowledge you want to disable the service, and choose **Disable** to complete the disable process.

###### Note

If you have not yet opted into General Availability in the Organizations management account you will have a warning message in your dashboard of "You are missing permissions which are required to manage policies in Security Hub."
To address this see the step for the Organizations Management account.

Once you have successfully completed the enablement for your account all of your security service integrations will continue to work as they did in the public preview.
If you need to make adjustments to security configurations of Organization member accounts, see Managing configuration of member accounts in an AWS Organization .

## Standalone accounts

###### To migrate a standalone account (console)

1. Sign in to your AWS account with your standalone credentials.
   Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
3. From the **General Availability** page choose **Continue with Security Hub General Availability** to opt into the paid GA experience.
   If you do not wish to continue with the GA experience, choose **Disable Security Hub**.
4. If you choose to enable the General Availability experience you will be taken to the **Coverage and capabilities page**.
   In the **Security capabilities** section do one of the following:
   1. (Option 1) Choose **Enable all capabilities**.
      This will turn on all of the Security Hub essential capabilties, threat analytics, and additional capabilties.
   2. (Option 2) Choose **Customize capabilities**.
      Select the threat analytics and additional capabilities that should be turned on.
      You cannot deselect any capabilities that are part of the Security Hub essential plan capabilities.

5. In the **Regions** section, choose **Enable all Regions**, **Disable all Regions**, or **Specify Regions**.
   If you choose **Enable all Regions**, you can determine whether to automatically enable new Regions.
   If you choose **Disable all Regions**, you can determine whether to automatically disable new Regions.
   If you choose **Specify Regions**, you must choose which Regions you want to enable and disable.
6. (Optional) For **Resource tags**, add tags as key-value pairs to help you easily identify the configuration.
7. Choose **Next Security Hub**.
   Review your configuration choices. Choose **Submit**.
