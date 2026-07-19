# Using log centralization with multilocation canaries

When you configure a canary to run from multiple locations, each execution produces
logs in its respective Region. You can use CloudWatch Logs centralization to aggregate these logs
into a single Region, making it easier to monitor and troubleshoot canary results from
one place.

For information about how log centralization works, including concepts, permissions,
and setup, see [Centralize
logging from multiple accounts and Regions](../logs/CloudWatchLogs_Centralization.md "../logs/CloudWatchLogs_Centralization.md") in the
_CloudWatch Logs User Guide_.

###### Configuring log centralization for a multilocation canary

To centralize logs from a multilocation canary, create a log centralization rule in
CloudWatch Logs with the following recommended settings.

| Setting               | Recommended value                                                  |
| --------------------- | ------------------------------------------------------------------ |
| Source regions        | Same Regions as the replica locations on your multilocation canary |
| Destination account   | Same account where your multilocation canary lives                 |
| Destination region    | Primary Region of your multilocation canary                        |
| Filter                | `LogGroupName ^ /aws/lambda/cwsyn-`                                |
| Destination log group | `${source.logGroup}`                                               |

This rule centralizes all canary logs from the selected source Regions to the
destination Region—including logs from non-multilocation canaries running in
those Regions. For multilocation canaries specifically, using
`${source.logGroup}` as the destination log group places replica logs in the
same log group as the primary canary logs, because primary and replica canaries share the
same log group name.

For instructions on creating a log centralization rule, see [Centralize
logging from multiple accounts and Regions](../logs/CloudWatchLogs_Centralization.md "../logs/CloudWatchLogs_Centralization.md").

###### Viewing centralized logs

If you use the recommended settings above, logs from all canary execution Regions
appear in the primary Region's log group. If you configured a different destination,
your logs appear in the destination you specified.

###### To view centralized logs (console)

1. Open the CloudWatch console.
2. In the navigation pane, choose **Application Signals**,
   **Synthetics Canaries**.
3. Choose your multilocation canary name to open its details page.
4. In the **Selected canary runs** table, choose a canary run that
   occurred in the primary Region.
5. Choose the **Logs** tab at the bottom of the canary details
   page.
6. Choose **View/Download in Logs Insights**.
   You can use CloudWatch Logs Insights to query across all log entries. For example, to find
   failures from a specific Region:

```
fields @timestamp, @message, @logStream
| filter @aws.region like /us-west-2/
| filter @message like /ERROR/
```
