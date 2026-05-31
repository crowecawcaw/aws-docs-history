# AWS DataSync Discovery statuses

You can check the status of your discovery jobs and whether AWS DataSync Discovery can
provide storage recommendations for your AWS migrations.

## Discovery job statuses

Use the following table to understand what's going on with your discovery
job.

| API status              | Description                                                                                                                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RUNNING`               | Your discovery job is running. The job collects data about<br>your on-premises storage system for the duration that you<br>specified.                                                        |
| `WARNING`               | Your discovery job has encountered errors and currently can't<br>collect data. Review the Amazon CloudWatch logs and address these issues<br>within 12 hours, or the job will be terminated. |
| `STOPPED`               | You stopped your discovery job before the job was expected to<br>finish.                                                                                                                     |
| `COMPLETED`             | Your discovery job successfully collected all data from your<br>on-premises storage system.                                                                                                  |
| `COMPLETED_WITH_ISSUES` | There were times during the discovery job when DataSync Discovery<br>couldn't collect data. For details, see your CloudWatch logs.                                                           |
| `TERMINATED`            | Your discovery job was canceled because of unresolved issues and<br>some data wasn’t collected. For details, see your CloudWatch logs.                                                       |
| `FAILED`                | Your discovery job encountered issues and couldn’t collect data<br>from your on-premises storage system. For details, see your CloudWatch<br>logs.                                           |

## Recommendation statuses

Use the following table to understand whether DataSync Discovery recommendations for a
specific on-premises storage resource are ready to view.

| API status    | Description                                                                                                                                                                                                                                                            |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `NONE`        | You can't generate recommendations yet. Try generating<br>recommendations when your discovery job completes.                                                                                                                                                           |
| `NONE`        | Your discovery job collected enough data for DataSync Discovery to<br>provide recommendations. You may be able to generate<br>recommendations if you stopped the discovery job early or the<br>job completed but had issues with data collection.                      |
| `IN_PROGRESS` | DataSync Discovery is working on your recommendations. How long this<br>takes depends on how many resources you're generating<br>recommendations for. If you're using the console, it may take a<br>few minutes to generate recommendations for a storage<br>resource. |
| `COMPLETED`   | You can view your recommendations.                                                                                                                                                                                                                                     |
| `FAILED`      | DataSync Discovery couldn't generate recommendations. You can review your<br>CloudWatch logs to identify the issue and try generating the<br>recommendations again.                                                                                                    |
| `NONE`        | Recommendations aren't available. You may see this status for a<br>failed discovery job or issue with the storage resource.                                                                                                                                            |
| `COMPLETED`   | DataSync Discovery currently doesn't support an AWS storage service that<br>meets the needs of the storage resource.                                                                                                                                                   |
