

# Monitoring local gateway connectivity
<a name="monitor-lgw-connectivity"></a>

You can monitor the connection status and BGP session state of your local gateway virtual interfaces from the AWS Outposts console. In the console, navigate to your Outpost and choose the **Local Gateway Virtual Interfaces** tab. The **Network Status** column shows whether each VIF is up and ready to forward traffic. Choose the status link to open a pre-built Amazon CloudWatch graph showing `VifConnectionStatus` and `VifBgpSessionState` for that VIF. These metrics are published automatically to the `AWS/Outposts` namespace for all Outpost VIFs and require no additional setup. To receive proactive notification when a VIF goes down or a BGP session is no longer in the `Established` state, you can optionally create a CloudWatch alarm on either metric. For descriptions of metric values and dimensions, see [CloudWatch metrics for Outposts racks](outposts-cloudwatch-metrics.md).

**Note**  
If you build dashboards or alarms directly against the `VifConnectionStatus` or `VifBgpSessionState` metrics, note that the dimension name differs depending on which CloudWatch widget you use: the updated widget uses `OutpostId`, while the legacy widget still uses `OutpostsId` for backward compatibility. Confirm which dimension name your dashboard or alarm definition expects to avoid missing data. For more information, see [Metrics](outposts-cloudwatch-metrics.md#outposts-metrics).