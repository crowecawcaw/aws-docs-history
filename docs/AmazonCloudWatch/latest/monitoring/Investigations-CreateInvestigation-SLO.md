

# Create an investigation from a CloudWatch Application Signals Service Level Objective (SLO)
<a name="Investigations-CreateInvestigation-SLO"></a>

You can start an investigation from a CloudWatch Application Signals Service Level Objective (SLO) metric.

**To start an investigation from a CloudWatch Application Signals Service Level Objective (SLO)**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Navigate to the **Applications Signals (APM)**, **Service Level Objectives (SLO)** console page.

1. Select an entry from the **Service Level Objectives (SLO)** list to display the metrics available for that SLO.

1. Select a metric, then choose **Investigate** from the **Action** menu.

   Alternatively, in the visualization of the metric you want to investigate, next to the more ![Vertical ellipsis used to display more options.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/vmore.png) menu, select the AI ![Icon used to represent a feature that uses artificial intelligence .](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/cw-ai-icon.png) icon to start an investigation.
**Note**  
If you have not configured operational investigations in your account, the AI icon opens the **Operation troubleshooting** pane. Select **Get started** to configure an investigation group and then continue.

1. In the **Operational troubleshooting** pane on the **Investigate**, under **Investigation title** enter a name for the investigation and optionally enter notes about the selected metric. 

1. Under **Approximate impact start time** CloudWatch investigations recommends a timestamp to investigate based on the selected telemetry. To change the timestamp of the investigation, update the date and time. 

1. Then choose **Start investigation**.

   The investigation starts. CloudWatch investigations scans your telemetry data to find data that might be associated with this situation.

1. To move the investigation data to the larger pane, choose **Open in full page**.

1. For detailed instructions about steps that you can take while continuing the investigation, see [View and continue an open investigation](Investigations-Continue.md).