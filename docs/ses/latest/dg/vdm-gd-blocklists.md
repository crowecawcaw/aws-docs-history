

# Blocklists
<a name="vdm-gd-blocklists"></a>

Blocklist monitoring watches your dedicated IPs and sending domains against the industry's major blocklist operators, with hourly checks and proactive alerts through Virtual Deliverability Manager Advisor when anything is listed.

**Monitored blocklist operators**  
Global deliverability monitors the following blocklist operators:
+ *IP blocklists* – Monitors your dedicated IPs against major IP-based blocklist operators.
+ *Domain blocklists* – Monitors your sending domains against major domain-based blocklist operators.

**What blocklist monitoring provides**  
The blocklists page displays the following information:
+ *Summary* – The number of monitored domains and IPs, and how many are currently listed on a blocklist.
+ *Monitored domains* – A table showing each monitored domain, its current status (Listed or Clean), and the number of blocklists it appears on.
+ *Monitored IPs* – A table showing each monitored IP address, its current status, and the number of blocklists it appears on.
+ *Listing details* – For each listed entity, the blocklist name, listing date, reason, and delisting procedure with direct links to the blocklist operator's removal process.

## Viewing blocklist status using the Amazon SES console
<a name="vdm-gd-blocklists-console"></a>

**To view blocklist status using the Amazon SES console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation pane, choose **Blocklists** under **Global deliverability** in the **Virtual Deliverability Manager** section.

1. Review the **Summary** section for an overview of your monitoring status.

1. In the **Monitored domains** or **Monitored IPs** tables, choose **Show details** for any entity to view its blocklist listings.

1. For listed entities, review the listing reason and follow the delisting procedure provided to request removal from the blocklist.

**Note**  
When a domain or IP is listed on a blocklist, Virtual Deliverability Manager Advisor generates a recommendation with guidance on how to resolve the issue. See [Virtual Deliverability Manager advisor](vdm-advisor.md) for more information.