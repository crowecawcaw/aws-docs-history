# AWS Elemental MediaTailor ADS log analysis in Amazon CloudWatch Logs

Insights

You can view and query AWS Elemental MediaTailor ad decision server (ADS) logs using Amazon CloudWatch Logs
Insights. MediaTailor sends event logs to CloudWatch for normal processing and error
conditions. The logs adhere to a JSON schema. Through CloudWatch Logs Insights, you can select
logs by time frame, and then run queries against them.

For general information, see [Analyze log data with
CloudWatch Logs insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md").

###### Note

To access the logs, you need permissions to access Amazon CloudWatch. For instructions, see
[Permissions for Amazon CloudWatch Logs](monitoring-permissions.md "monitoring-permissions.md").

###### To view and query ADS logs using the CloudWatch console

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, under **Logs**, choose
   **Insights**.
3. In the search bar, enter `AdDec`, and then from the
   drop-down list, select
   `MediaTailor/AdDecisionServerInteractions`.
4. (Optional) Adjust the time period that you want to study.
5. (Optional) Change the query in the dialog box. For general guidance, see
   [CloudWatch Logs
   insights query syntax](../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax.md "../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax.md"). For examples of queries for MediaTailor
   ADS, see [Querying the ADS logs](querying-the-ads-logs.md "querying-the-ads-logs.md").
6. Choose **Run query**. The query might take a few seconds,
   during which time **Cancel** appears in place of **Run
   query**.
7. (Optional) To export the results as a CSV file, choose
   **Actions**, and then choose **Download query
   results (CSV)**.

###### Note

The console limits the number of records that it returns in query results and that
it exports, so for bulk data, use the API, the AWS Command Line Interface (AWS CLI), or an SDK.

###### Topics

- [Querying the ADS logs](querying-the-ads-logs.md "querying-the-ads-logs.md")
