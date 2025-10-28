# Reporting on network traffic in Network Firewall

AWS Network Firewall lets you generate reports on HTTP or HTTPS traffic observed over the last 30 days in any firewall, starting from
the point in time when you enable **Traffic analysis mode** in a firewall.
Network Firewall only starts collecting traffic analysis metrics when you enable **Traffic analysis mode** on your firewall.

###### Tip

If you enable **Traffic analysis mode**, then immediately generate a report, the report will only contain metrics from
when you enabled that setting. For the most comprehensive analysis, we recommend you wait 30 days after you enable
**Traffic analysis mode** before you generate a report.

Before you can generate a traffic analysis report, you must enable
**Traffic analysis mode** when you create or update a firewall.
For more information on firewall configuration, see [Managing a firewall and firewall endpoints in AWS Network Firewall](firewall-managing.md "firewall-managing.md").

###### Note

You can generate up to one report per traffic type, per 30 day period. For example, when you successfully create an HTTP traffic report,
you cannot create another HTTP traffic report until 30 days pass. Alternatively, if you generate a report that combines metrics on both HTTP and HTTPS
traffic, you cannot create another report for either traffic type until 30 days pass. Network Firewall automatically deletes the report after 30 days.

Each report provides insight into the following metrics for any given firewall:

- The most frequently accessed domains
- The number of access attempts made to each observed domain
- The number of unique source IPs connecting to each observed domain
- The date and time any domain was first accessed (within the last 30 day period)
- The date and time any domain last first accessed(within the last 30 day period)
- The protocol (HTTP or HTTPS) used by any domain's traffic

## Caveats and considerations for traffic analysis reports

Consider the following in your use of traffic analysis reports:

- When you generate a report, you create a snapshot into the last 30 days of network traffic monitored by your firewall.
- The maximum number of results per report is 1000.
- If your custom HTTP and TLS logs do not contain an SNI or the HTTP hostname,
  Network Firewall will classify it as UNKNOWN_DOMAIN.
- The observation count on reported domain access attempts cannot exceed the maximum of 2,147,483,647.
  For example, if one or more of your reported domains was accessed more than 2,147,483,647 times within the 30 day reporting period, the count shown in your generated report
  will not exceed 2,147,483,647.

## Generating traffic analysis reports

###### Before you generate a report

If you haven't enabled **Traffic analysis mode** on your firewall, do that now.
For more information, see [Managing a firewall and firewall endpoints in AWS Network Firewall](firewall-managing.md "firewall-managing.md").

###### Important

Network Firewall only starts collecting traffic analysis metrics when you enable **Traffic analysis mode** on your firewall.
Traffic observed before you enable **Traffic analysis mode** is not included in reporting.

###### To generate a traffic analysis report in Network Firewall

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewalls**.
3. In the **Firewalls** page, choose the name of the firewall that you want
   to edit. This takes you to the firewall's details page.
4. In the firewall's details page, choose the **Monitoring and observability tab**.
5. In the **Monitoring and observability tab**, select **Create report**.

## Creating stateful rule groups from reports

You can create stateful rule groups using the domains identified in your firewall's traffic analysis reports.

###### To generate a traffic analysis report in Network Firewall

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewalls**.
3. In the **Firewalls** page, choose the name of the firewall that you want
   to edit. This takes you to the firewall's details page.
4. In the firewall's details page, choose the **Monitoring and observability tab**.
5. Select any completed report.
6. Select **Create domain list group**. The workflow for creating a stateful rule group opens.
7. Complete the configuration for your domain list stateful rule group.
   For more information, see [Creating a stateful rule group](rule-group-stateful-creating.md "rule-group-stateful-creating.md").
