

# Updating a firewall in AWS Network Firewall
<a name="firewall-updating"></a>

To make changes to your firewall settings through the console, use the following procedure.

After you create a firewall, you can update the firewall settings or view reports on firewall traffic from within the console. To view your firewall settings and reports through the console, use the following procedure:

**Warning**  
If your firewall update changes any stateful engine option, including the rule evaluation order type, stream exception policy, or flow timeouts (such as TCP idle timeout), it may require a restart of the stateful engine in order to apply the changes. When this occurs, existing connections will be treated according to your stream exception policy configuration. For more information about stateful engine options, see [Firewall policy settings in AWS Network Firewall](firewall-policy-settings.md). 

Updating a firewall affects all endpoints for the firewall, both those defined inside the firewall and those defined as VPC endpoint associations.

**To update a firewall**

1. Sign in to the AWS Management Console and open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Firewalls**.

1. In the **Firewalls** page, choose the name of the firewall that you want to edit. This takes you to the firewall's details page. 

1. Choose the tab **Firewall details**, then, in each section where you want to make changes, choose **Edit** and follow the console guidance to make your changes. 
   + In the **Details** section, you can change the firewall description. The name is fixed after creation.
   + In the **Traffic analysis mode** section, you can enable or disable traffic analysis, which lets you generate reports on HTTP or HTTPS traffic from the last 30 days. Enabling and disabling **Traffic analysis mode** does not impact traffic flow or automatically trigger report creation.
**Important**  
Network Firewall only starts collecting traffic analysis metrics when you enable **Traffic analysis mode** on your firewall. Traffic observed before you enable **Traffic analysis mode** is not included in reporting. 
   + In the **Associated policy and VPC** section, you can add and remove Availability Zones and subnets and you can associate a different firewall policy. The VPC is fixed after creation. 
   + In the **Logging** section, you can configure logging for alert, flow, and TLS logs. For information about your logging options and costs, see [Logging network traffic from AWS Network Firewall](firewall-logging.md).
   + In the **Firewall tags** section, you can change the tags assigned to the AWS firewall resource. For information about tagging, see [Tagging AWS Network Firewall resources](tagging.md).

1. Choose the **Monitoring** tab, then follow the console guidance to use the available reporting capabilities. 
   + In the **Firewall requests** section, you can view a chart of dropped, passed, and received stateless and stateful packets monitored by the firewall within a customizable time frame.
   + In the **Reports** section, if you have enabled traffic analysis mode, you can generate an HTTP or HTTPS report or view the status of reports you already created. For information on these reports, see See [Reporting on network traffic in Network Firewall](reporting.md) for more information on report generation. 
**Note**  
Enabling traffic analysis mode does not automatically generate a report when you finish creating your firewall. See [Reporting on network traffic in Network Firewall](reporting.md) for more information on report generation. 

1. Choose **Save** to save your changes and return to the firewall's detail page.