# Updating a firewall in AWS Network Firewall

To make changes to your firewall settings through the console, use the following procedure.

After you create a firewall, you can update the firewall settings or view reports on firewall traffic from within the console.
To view your firewall settings and reports through the console, use the following procedure:

###### Warning

If your firewall update changes your stateful rule evaluation order type, you will experience an
interruption of in-flight traffic through the firewall for a few seconds during the reset. This is the only type of update
that has this effect. For more information about stateful rule evaluation order types, see
[Managing evaluation order for Suricata compatible rules in AWS Network Firewall](suricata-rule-evaluation-order.md "suricata-rule-evaluation-order.md").

Updating a firewall affects all endpoints for the firewall, both those defined inside the firewall and
those defined as VPC endpoint associations.

###### To update a firewall

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Network Firewall**, choose **Firewalls**.
3. In the **Firewalls** page, choose the name of the firewall that you want
   to edit. This takes you to the firewall's details page.
4. Choose the tab **Firewall details**, then, in each section where you want to
   make changes, choose **Edit** and follow the console
   guidance to make your changes.
   - In the **Details** section, you can change the firewall description.
     The name is fixed after creation.
   - In the **Traffic analysis mode** section, you can enable
     or disable traffic analysis, which lets you generate reports on HTTP or HTTPS
     traffic from the last 30 days. Enabling and disabling **Traffic analysis mode**
     does not impact traffic flow or automatically trigger report creation.

   ###### Important

   Network Firewall only starts collecting traffic analysis metrics when you enable **Traffic analysis mode** on your firewall.
   Traffic observed before you enable **Traffic analysis mode** is not included in reporting.
   - In the **Associated policy and VPC** section, you can add and remove
     Availability Zones and subnets and you can associate a different
     firewall policy. The VPC is fixed after creation.
   - In the **Logging** section, you can configure logging
     for alert, flow, and TLS logs. For information about your logging options and costs,
     see [Logging network traffic from AWS Network Firewall](firewall-logging.md "firewall-logging.md").
   - In the **Firewall tags** section, you can change the tags assigned to
     the AWS firewall resource. For information about tagging, see
     [Tagging AWS Network Firewall resources](tagging.md "tagging.md").

5. Choose the **Monitoring** tab, then follow the console guidance to use the available reporting capabilities.
   - In the **Firewall requests** section, you can view a chart of dropped, passed, and received
     stateless and stateful packets monitored by the firewall within a customizable time frame.
   - In the **Reports** section, if you have enabled traffic analysis mode, you can generate an HTTP
     or HTTPS report or view the status of reports you already created. For information on these reports,
     see See [Reporting on network traffic in Network Firewall](reporting.md "reporting.md")
     for more information on report generation.

   ###### Note

   Enabling traffic analysis mode does not automatically generate a report when you finish creating your firewall.
   See [Reporting on network traffic in Network Firewall](reporting.md "reporting.md")
   for more information on report generation.

6. Choose **Save** to save your changes and return to the firewall's
   detail page.
