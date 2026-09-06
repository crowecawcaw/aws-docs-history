

# Global deliverability
<a name="vdm-global-deliverability"></a>

Global deliverability extends your visibility beyond Amazon SES. It provides analytics based on a representative sample of your sending—across every provider your domains send through, not just Amazon SES.

You can validate campaigns before they ship, track inbox placement at the ISP level, and monitor your IPs and domains against major blocklist operators—all from the Amazon SES console.

Global deliverability is enabled per region. In any region, domain monitoring tracks metrics across regions, accounts, and sending providers. IP monitoring only tracks the dedicated IPs available in that region. Inbox placement tests are not dependent on any specific region.

**Key features**  
Global deliverability includes the following features:
+ **Campaign analytics** – Surfaces per-campaign deliverability and engagement metrics based on a representative sample of emails sent from your monitored domains, even when they leave through a non-Amazon SES provider. See [Campaign analytics](vdm-gd-campaign-analytics.md).
+ **Inbox placement rates** – Provides ISP-level inbox placement rates for your monitored domains, updated hourly based on analytics. See [Inbox placement rates](vdm-gd-inbox-placement-rates.md).
+ **Inbox placement tests** – Sends your campaign to seed accounts across major mailbox providers before you send to real subscribers, so you can catch placement and authentication issues in advance. See [Inbox placement tests](vdm-gd-inbox-placement-tests.md).
+ **Blocklists** – Monitors your dedicated IPs and sending domains against the industry's major blocklist operators with hourly checks and proactive alerts through Virtual Deliverability Manager Advisor when anything is listed (you [can monitor](monitoring-eventbridge.md) these through EventBridge). See [Blocklists](vdm-gd-blocklists.md).

**Pricing**  
Global deliverability is sold as a single subscription package that includes monitored domains, dedicated IP monitoring, and inbox placement tests. For pricing details, see [Amazon SES Pricing](https://aws.amazon.com/ses/pricing/).

**Getting started**  
To start using global deliverability, enable it from the Virtual Deliverability Manager Settings page in the Amazon SES console. See [Getting started with global deliverability](vdm-gd-get-started.md).

**Topics**
+ [Getting started with global deliverability](vdm-gd-get-started.md)
+ [Campaign analytics](vdm-gd-campaign-analytics.md)
+ [Inbox placement rates](vdm-gd-inbox-placement-rates.md)
+ [Inbox placement tests](vdm-gd-inbox-placement-tests.md)
+ [Blocklists](vdm-gd-blocklists.md)