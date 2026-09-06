

# Getting started with CloudWatch Contributor Insights for DynamoDB
<a name="contributorinsights_tutorial"></a>

This section describes how to enable and use Amazon CloudWatch Contributor Insights in different modes to meet your monitoring needs using the Amazon DynamoDB console or the AWS Command Line Interface (AWS CLI). 

In the following examples, you use the DynamoDB table that is defined in the [Getting started with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html) tutorial.

**Topics**
+ [Choosing a Contributor Insights mode](#contributorinsights_tutorial.modes)
+ [Using Contributor Insights (console)](#usecontributorinsights_console)
+ [Using Contributor Insights (AWS CLI)](#usecontributorinsights_cli)

## Choosing a Contributor Insights mode
<a name="contributorinsights_tutorial.modes"></a>

Before enabling Contributor Insights, you should understand the two available modes. Review the mode comparison to select the option that best aligns with your specific requirements.


| Aspect | Accessed and throttled keys mode | Throttled keys mode | 
| --- | --- | --- | 
| Monitors | All requests (successful and throttled) | Only throttled requests | 
| Graphs | Most Accessed Items \+ Most Throttled Items | Most Throttled Items only | 
| Best for | Targeted analysis and optimization | Throttling monitoring | 
| Use when | You need complete visibility into access patterns. You're doing short-term analysis or debugging. | Your primary concern is identifying and resolving throttling issues. You want to keep Contributor Insights enabled continuously for real-time throttling alerts. | 

## Using Contributor Insights (console)
<a name="usecontributorinsights_console"></a>

The console provides an intuitive way to enable Contributor Insights and select the appropriate mode for your monitoring needs.

**To use Contributor Insights in the console**

1. Sign in to the AWS Management Console and open the DynamoDB console at [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/).

1. In the navigation pane on the left side of the console, choose **Tables**.

1. Choose the `Music` table.

1. Choose the **Monitor** tab.

1. Choose **Turn on CloudWatch Contributor Insights**.  
![Console screenshot showing monitor tab and button.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/CI_ChooseAndManageNew.PNG)

1. In the **Manage CloudWatch Contributor Insights settings** dialog box, toggle **Turn on** for both the `Music` base table and the `AlbumTitle-index` global secondary index.

1. Leave the **Only throttled keys mode** toggle in the off position for both and then choose **Save changes**.  
![Console screenshot showing Contributor Insights status list options.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/CI_Enable.png)

   This enables the default *accessed and throttled keys* mode for both the table and GSI, which provides monitoring of both accessed and throttled items. Switching the **Only throttled keys mode** toggle to the on position would enable the *throttled keys* mode.

   If the operation fails, see [DescribeContributorInsights FailureException](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeContributorInsights.html#DDB-DescribeContributorInsights-response-FailureException) in the *Amazon DynamoDB API Reference* for possible reasons.

1. The CloudWatch Contributor Insights graphs are now visible on the **Monitor** tab for the `Music` table. Since you enabled *accessed and throttled keys* mode, you see both accessed and throttled item graphs.  
![Console screenshot showing Contributor Insights tab with several graphs for the music table.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/CI_Graphs.png)

### Switching between modes
<a name="usecontributorinsights_console.switching-modes"></a>

You can switch between modes at any time without disabling Contributor Insights.

**To switch Contributor Insights modes**

1. On the **Monitor** tab of your table, choose **Manage CloudWatch Contributor Insights**.

1. In the **Manage Contributor Insights settings** dialog box, for each base table or GSIs:
   + Toggle **Only throttled keys mode** on or off to enable the *throttled keys* mode or go back to the default *accessed and throttled keys* mode.
   + Toggle **Turn on** off to disable CloudWatch Contributor Insight for a table or GSI.

1. Choose **Save changes**.

   After this is complete, the graphs will reflect the new mode.

### Creating CloudWatch alarms
<a name="usecontributorinsights_console_alarms"></a>

Follow these steps to create a CloudWatch alarm and be notified when any partition key consumes more than 50,000 [ConsumedThroughputUnits](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/contributorinsights_HowItWorks.html#contributorinsights_HowItWorks.Graphs.most-accessed) or experiences throttling.

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/)

1. In the navigation pane on the left side of the console, choose **Contributor Insights**.

1. Choose the appropriate rule based on your mode and what you want to monitor:
   + For accessed items monitoring (accessed and throttled keys mode only): Choose **DynamoDBContributorInsights-PKC-Music**
   + For throttled items monitoring (both modes): Choose **DynamoDBContributorInsights-PKT-Music**

1. Choose the **Actions** drop down.

1. Choose **View in metrics**.

1. Choose **Max Contributor Value**.
**Note**  
Only `Max Contributor Value` and `Maximum` return useful statistics. The other statistics in this list don't return meaningful values.  
![Console screenshot showing Contributor Insights tab and button.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/CI_AlarmsViewinMetrics.png)

1. On the **Actions** column, Choose **Create Alarm**.  
![Console screenshot showing Contributor Insights status list options.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/CI_AlarmsSetAlarm.png)

1. Enter an appropriate threshold value and choose **Next**:
   + For accessed items (PKC rules): Enter 50000 for `ConsumedThroughputUnits`
   + For throttled items (PKT rules): Enter 1 for `ThrottleCount` to be alerted on any throttling  
![Console screenshot showing Contributor Insights tab and button.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/CI_AlarmsSetAlarmThreashold.png)

1.  See [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) for details on how to configure the notification for the alarm.

## Using Contributor Insights (AWS CLI)
<a name="usecontributorinsights_cli"></a>

The AWS CLI provides programmatic access to Contributor Insights with full support for both modes. You can specify the mode when enabling Contributor Insights or switch modes later.

### Basic operations with default mode
<a name="usecontributorinsights_cli.basic"></a>

**To use Contributor Insights with default settings**

1. Enable CloudWatch Contributor Insights for DynamoDB on the `Music` base table with the *accessed and throttled keys* mode. Since `ACCESSED_AND_THROTTLED_KEYS` is the default mode, you can omit the `--contributor-insights-mode=ACCESSED_AND_THROTTLED_KEYS` parameter.

   ```
   aws dynamodb update-contributor-insights \
                       --table-name Music \
                       --contributor-insights-action=ENABLE
   ```

1. Enable Contributor Insights for DynamoDB on the `AlbumTitle-index` global secondary index.

   ```
   aws dynamodb update-contributor-insights \
                       --table-name Music \
                       --index-name AlbumTitle-index \
                       --contributor-insights-action=ENABLE
   ```

1. Get the status and rules for the `Music` table and all its indexes.

   ```
   aws dynamodb describe-contributor-insights 
                       --table-name Music
   ```

   The response will include the `ContributorInsightsMode` field showing `ACCESSED_AND_THROTTLED_KEYS`.

1. List the status of the `Music` table and all its indexes.

   ```
   aws dynamodb list-contributor-insights --table-name Music
   ```

### Enabling throttled keys mode
<a name="usecontributorinsights_cli.throttled-mode"></a>

**To enable Contributor Insights in throttled keys mode**

1. Enable CloudWatch Contributor Insights for DynamoDB on the `Music` base table with *throttled keys* mode.

   ```
   aws dynamodb update-contributor-insights \
       --table-name Music \
       --contributor-insights-action=ENABLE \
       --contributor-insights-mode=THROTTLED_KEYS
   ```

1. Enable Contributor Insights in *throttled keys* mode for the `AlbumTitle-index` global secondary index.

   ```
   aws dynamodb update-contributor-insights \
       --table-name Music \
       --index-name AlbumTitle-index \
       --contributor-insights-action=ENABLE \
       --contributor-insights-mode=THROTTLED_KEYS
   ```

1. Verify the mode by describing the Contributor Insights configuration.

   ```
   aws dynamodb describe-contributor-insights --table-name Music
   ```

   The response will show `ContributorInsightsMode` as `THROTTLED_KEYS` and fewer rules compared to the default mode.

### Switching between modes
<a name="usecontributorinsights_cli.switching-modes"></a>

**To switch Contributor Insights modes**

1. Switch from *throttled keys* mode to *accessed and throttled keys* mode.

   ```
   aws dynamodb update-contributor-insights \
       --table-name Music \
       --contributor-insights-action=ENABLE \
       --contributor-insights-mode=ACCESSED_AND_THROTTLED_KEYS
   ```

1. Switch from *accessed and throttled keys* mode to *throttled keys* mode.

   ```
   aws dynamodb update-contributor-insights \
       --table-name Music \
       --contributor-insights-action=ENABLE \
       --contributor-insights-mode=THROTTLED_KEYS
   ```

1. Check the status during the transition.

   ```
   aws dynamodb describe-contributor-insights --table-name Music
   ```

   During the mode switch, the `ContributorInsightsStatus` will show as `ENABLING`. After this is complete, it will show as `ENABLED` with the new mode.

### Managing Contributor Insights
<a name="usecontributorinsights_cli.management"></a>

**To manage Contributor Insights settings**

1. Disable CloudWatch Contributor Insights for DynamoDB on the `AlbumTitle-index` global secondary index.

   ```
   aws dynamodb update-contributor-insights \
                       --table-name Music --index-name AlbumTitle-index \
                       --contributor-insights-action=DISABLE
   ```

1. List all Contributor Insights configurations in your account.

   ```
   aws dynamodb list-contributor-insights
   ```

   This shows all tables and indexes with Contributor Insights enabled, along with their modes.

1. Get detailed information about a specific configuration.

   ```
   aws dynamodb describe-contributor-insights \
                       --table-name Music \
                       --index-name AlbumTitle-index
   ```

### Example responses
<a name="usecontributorinsights_cli.examples"></a>

Here are example responses showing the differences between modes:

#### Accessed and throttled keys mode response
<a name="usecontributorinsights_cli.examples.accessed-throttled"></a>

```
{
    "TableName": "Music",
    "ContributorInsightsRuleList": [
        "DynamoDBContributorInsights-PKC-Music-1234567890123",
        "DynamoDBContributorInsights-PKT-Music-1234567890123",
        "DynamoDBContributorInsights-SKC-Music-1234567890123",
        "DynamoDBContributorInsights-SKT-Music-1234567890123"
    ],
    "ContributorInsightsStatus": "ENABLED",
    "ContributorInsightsMode": "ACCESSED_AND_THROTTLED_KEYS",
    "LastUpdateDateTime": "2024-01-15T10:30:00.000Z"
}
```

#### Throttled keys mode response
<a name="usecontributorinsights_cli.examples.throttled-only"></a>

```
{
    "TableName": "Music",
    "ContributorInsightsRuleList": [
        "DynamoDBContributorInsights-PKT-Music-1234567890123",
        "DynamoDBContributorInsights-SKT-Music-1234567890123"
    ],
    "ContributorInsightsStatus": "ENABLED",
    "ContributorInsightsMode": "THROTTLED_KEYS",
    "LastUpdateDateTime": "2024-01-15T10:35:00.000Z"
}
```

Notice that throttled keys mode has fewer rules (only PKT and SKT), which corresponds to a more focused monitoring.