

# Manage subscriptions using the console

Use subscriptions to send Infrastructure Performance metrics to Amazon CloudWatch and view them there. Using the console, you can subscribe to or unsubscribe from CloudWatch performance metrics.

**To manage CloudWatch subscriptions**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, under **Network Monitoring**, choose **Performance monitors**, and then choose the **Infrastructure Performance** tab.

1. Choose the Region or Availability Zone pairs that you want to manage. For detailed steps on how to choose them, see [Monitor using the console](CloudWatch-InfrastructurePerformance-Console.md).

1. Choose **Edit Subscription**.

1. Choose **Subscribe** or **Unsubscribe** for the pair.

1. Choose **Confirm**.

**Console not available in some Regions**  
The Infrastructure Performance console doesn't support the following Regions: ap-east-1 (Asia Pacific (Hong Kong)), ap-southeast-3 (Asia Pacific (Jakarta)), ap-southeast-4 (Asia Pacific (Melbourne)), eu-central-2 (Europe (Zurich)), eu-south-1 (Europe (Milan)), eu-south-2 (Europe (Spain)), and af-south-1 (Africa (Cape Town)). To unsubscribe from pairs in these Regions, use the AWS Command Line Interface. Existing metrics and alarms for these subscriptions continue to work in these Regions.