# Create an investigation from a

CloudWatch Application Signals Service Level Objective (SLO)

You can start an investigation from a CloudWatch Application Signals Service Level Objective (SLO)
metric.

###### To start an investigation from a CloudWatch Application Signals Service Level Objective

(SLO)

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Navigate to the **Applications Signals (APM)**,
   **Service Level Objectives (SLO)** console page.
3. Select an entry from the **Service Level Objectives (SLO)**
   list to display the metrics available for that SLO.
4. Select a metric, then choose **Investigate** from the
   **Action** menu.

Alternatively, in the visualization of the metric you want to investigate,
next to the more
![Vertical ellipsis used to display more options.](/images/AmazonCloudWatch/latest/monitoring/images/vmore.png)
menu, select the AI
![Icon used to represent a feature that uses artificial intelligence .](images/cw-ai-icon.png)
icon to start an investigation.

###### Note

If you have not configured operational investigations in your account, the
AI icon opens the **Operation troubleshooting** pane.
Select **Get started** to configure an investigation group
and then continue. 5. In the **Operational troubleshooting** pane on the
**Investigate**, under **Investigation
title** enter a name for the investigation and optionally enter
notes about the selected metric. 6. Under **Approximate impact start time** CloudWatch investigations recommends a
timestamp to investigate based on the selected telemetry. To change the
timestamp of the investigation, update the date and time. 7. Then choose **Start investigation**.

The investigation starts. CloudWatch investigations scans your telemetry data to find data that
might be associated with this situation. 8. To move the investigation data to the larger pane, choose **Open in
full page**. 9. For detailed instructions about steps that you can take while continuing the
investigation, see [View and continue an open
investigation](Investigations-Continue.md "Investigations-Continue.md").
