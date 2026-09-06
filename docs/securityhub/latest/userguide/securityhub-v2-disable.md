

# Disabling Security Hub
<a name="securityhub-v2-disable"></a>

## Disabling Security Hub for a single account
<a name="securityhub-v2-disable-single"></a>

If your account is not part of an organization, you can disable Security Hub in the Security Hub console at any time or use [DisableSecurityHubV2 API](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DisableSecurityHubV2.html). When you disable Security Hub, it stops ingesting findings from detection engines, you also lose access to existing findings, integrations and configurations.

 When you disable Security Hub for your account in all Regions, Security Hub also deletes the service-linked IAM Access Analyzer that was created when you enabled the service. If automatic deletion fails, you can delete the analyzer by calling the IAM Access Analyzer `DeleteServiceLinkedAnalyzer` API operation. This operation succeeds only after Security Hub is fully disabled for your account. If you disable Security Hub in a single Region but remain enabled in other Regions, the unused access analyzer continues to run and findings continue to be replicated to your remaining enabled Regions. 

**To disable Security Hub**

1. Sign in to your AWS account with your credentials, and open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home).

1. From the navigation pane, choose **General**.

1. In Security Hub, choose **Disable**. In the pop-up window, enter **Disable**, and choose **Disable**.

## Disabling Security Hub across an organization
<a name="securityhub-v2-disable-organization"></a>

If you are the delegated administrator for an AWS Organization, you have two options for disabling Security Hub across member accounts.

### Option 1: Disabling Security Hub with detection engines
<a name="securityhub-v2-disable-with-engines"></a>

You can leverage the **Security Hub (essential and additional capabilities)** deployment and policy from the policy catalog in your delegated administrator account to disable Security Hub along with Amazon Inspector for specific organizational units, accounts, or regions.

**To disable Security Hub and Amazon Inspector across member accounts using a policy**

1. Sign in using your AWS account with your delegated administrator credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home).

1. From the navigation pane, choose **Management**, and then choose **Configurations**.

1. Choose **Security Hub (essential and additional capabilities)** from the Configuration catalog.

1. On the **Configure Security Hub** page in the **Details** section, enter a name and description for the policy (for example, "Security Hub Disablement Policy").

1. In the **Account selection** section, select one of the following options. Choose **All organizational units and accounts** if you want to apply the disablement to all organizational units and accounts. Choose **Specific organizational units and accounts** if you want to apply the disablement to specific organizational units and accounts. If you choose this option, use the search bar or organizational structure tree to specify the target organizational units and accounts.

1. In the **Regions** section, choose **Disable all Regions** to disable Security Hub in all Regions. Optionally choose whether to automatically disable new Regions. Choose **Specify Regions** to choose which specific Regions you want to disable.

1. (Optional) For **Advanced settings**, refer to the guidance from AWS Organizations.

1. (Optional) For **Resource tags**, add tags as key-value pairs to help you easily identify the configuration.

1. Choose **Next**.

1. Review your changes, and then choose **Apply**. Your target accounts are configured based on the policy. The configuration status of your policy displays at the top of the Policies page.

**Disabling Amazon GuardDuty and AWS Security Hub CSPM**  
For GuardDuty and Security Hub CSPM capabilities, you must manually disable the capabilities from the respective delegated administrator accounts. GuardDuty and Security Hub CSPM use deployments (one-time actions) rather than policies, so disablement must be performed manually from their respective consoles.

### Option 2: Disabling Security Hub only
<a name="securityhub-v2-disable-only"></a>

If you have an existing Security Hub policy and want to disable Security Hub only, without affecting Amazon Inspector, GuardDuty, or Security Hub CSPM, follow these steps.

**To disable Security Hub only across member accounts**

1. Sign in using your AWS account with your delegated administrator credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home).

1. From the navigation pane, choose **Management**, and then choose **Configurations**.

1. Choose any of your **Security Hub policies** from the **Configured policies**.

1. Choose **Edit policy** and in the **Account selection** section, select one of the following options. Choose **All organizational units and accounts** if you want to apply the disablement to all organizational units and accounts. Choose **Specific organizational units and accounts** if you want to apply the disablement to specific organizational units and accounts. If you choose this option, use the search bar or organizational structure tree to specify the target organizational units and accounts.

1. In the **Regions** section, choose **Disable all Regions** to disable Security Hub in all Regions. Optionally choose whether to automatically disable new Regions. Choose **Specify Regions** to choose which specific Regions you want to disable.

1. (Optional) For **Advanced settings**, refer to the guidance from AWS Organizations.

1. (Optional) For **Resource tags**, add tags as key-value pairs to help you easily identify the configuration.

1. Choose **Next**.

1. Review your changes, and then choose **Apply**. Your target accounts are configured based on the policy. The configuration status of your policy displays at the top of the Configurations page.

**Impact on other security services**  
Disabling Security Hub through an Security Hub policy has **no impact** on Security Hub CSPM, GuardDuty, and Amazon Inspector configurations.

If you need to disable Amazon Inspector only across member accounts, you can use the **Vulnerability management** policy from the Security Hub configuration catalog. Navigate to the Security Hub Configuration page, choose **Vulnerability management from Amazon Inspector**, and create a disable policy following steps similar to the Security Hub disable procedure above.