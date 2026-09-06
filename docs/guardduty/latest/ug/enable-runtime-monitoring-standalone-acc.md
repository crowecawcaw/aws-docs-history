

# Enabling Runtime Monitoring for a standalone account
<a name="enable-runtime-monitoring-standalone-acc"></a>

A standalone account owns the decision to enable or disable a protection plan in their AWS account in a specific AWS Region. 

If your account is associated with a GuardDuty administrator account through AWS Organizations, or by the method of invitation, this section doesn't apply to your account. For more information, see [Enabling Runtime Monitoring for multiple-account environments](enable-runtime-monitoring-multiple-acc-env.md).

After you enable Runtime Monitoring, ensure to install GuardDuty security agent through automated configuration or manual deployment. As a part of completing all the steps listed in the following procedure, make sure to install the security agent.

**To enable Runtime Monitoring in standalone account**

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the navigation pane, choose **Runtime Monitoring**.

1. Under the **Configuration** tab, choose **Enable** to enable Runtime Monitoring for your account.

1. Manage the security agent for your resource type. For more information, see [Managing GuardDuty security agents](runtime-monitoring-managing-agents.md).