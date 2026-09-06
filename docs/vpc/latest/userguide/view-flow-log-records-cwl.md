

# View flow log records with CloudWatch Logs
<a name="view-flow-log-records-cwl"></a>

You can view your flow log records using the CloudWatch Logs console. After you create your flow log, it might take a few minutes for it to be visible in the console.

**To view flow log records published to CloudWatch Logs using the console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Logs**, **Log groups**.

1. Select the name of the log group that contains your flow logs to open its details page.

1. Select the name of the log stream that contains the flow log records. For more information, see [Flow log records](flow-log-records.md).

**To view flow log records published to CloudWatch Logs using the command line**
+ [get-log-events](https://docs.aws.amazon.com/cli/latest/reference/logs/get-log-events.html) (AWS CLI)
+ [Get-CWLLogEvent](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-CWLLogEvent.html) (AWS Tools for Windows PowerShell)