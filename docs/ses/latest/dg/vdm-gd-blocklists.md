# Blocklists

Blocklist monitoring watches your dedicated IPs and sending domains against the
industry's major blocklist operators, with hourly checks and proactive alerts
through Virtual Deliverability Manager Advisor when anything is listed.

###### Monitored blocklist operators

Global deliverability monitors the following blocklist operators:

- _IP blocklists_ – Monitors your dedicated IPs against
  major IP-based blocklist operators.
- _Domain blocklists_ – Monitors your sending domains
  against major domain-based blocklist operators.

###### What blocklist monitoring provides

The blocklists page displays the following information:

- _Summary_ – The number of monitored domains and IPs, and
  how many are currently listed on a blocklist.
- _Monitored domains_ – A table showing each monitored
  domain, its current status (Listed or Clean), and the number of blocklists it
  appears on.
- _Monitored IPs_ – A table showing each monitored IP
  address, its current status, and the number of blocklists it appears on.
- _Listing details_ – For each listed entity, the
  blocklist name, listing date, reason, and delisting procedure with direct links to
  the blocklist operator's removal process.

## Viewing blocklist status using the Amazon SES console

###### To view blocklist status using the Amazon SES console

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the left navigation pane, choose **Blocklists** under
   **Global deliverability** in the
   **Virtual Deliverability Manager** section.
3. Review the **Summary** section for an overview of your
   monitoring status.
4. In the **Monitored domains** or **Monitored
   IPs** tables, choose **Show details** for any
   entity to view its blocklist listings.
5. For listed entities, review the listing reason and follow the delisting
   procedure provided to request removal from the blocklist.

###### Note

When a domain or IP is listed on a blocklist, Virtual Deliverability Manager Advisor generates a
recommendation with guidance on how to resolve the issue. See [Virtual Deliverability Manager advisor](vdm-advisor.md "vdm-advisor.md") for more information.
