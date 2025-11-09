# About channel

logs

MediaLive produces channel logs that contain detailed information
about activity in a channel. The logs provide a sequential
description of activity that occurs in the channel. These logs
can be useful when the information in alerts ([Monitoring a channel or
multiplex using Amazon CloudWatch Events](monitoring-via-cloudwatch.md "monitoring-via-cloudwatch.md")) does not provide
enough information to resolve an issue on the channel.

There are two sets of channel logs:

- Channel encoder logs. You must [enable](enabling-disabling-logs.md "enabling-disabling-logs.md") these logs.
- Channel as-run logs. MediaLive always produces these
  logs.

## Comparison of

types of logs

###### Features that are the same in both types of

logs

Both types of logs are sent to Amazon CloudWatch Logs. You can use
the standard features of CloudWatch Logs to view and manage the
logs. For more information, see [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md").

###### Features that are different in the two types of

logs

The following table describes the differences between
channel encoder logs and channel as-run logs.

|                       | Encoder logs                                                                                                                                                                                                                                                                                                                                                             | As-run logs                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Trigger for creation  | You must [enable<br>these logs](enabling-disabling-logs.md "enabling-disabling-logs.md") in order for MediaLive to<br>produce them.                                                                                                                                                                                                                                      | MediaLive always produces these logs.                                                     |
| Level of detail       | You can set a logging level to control<br>the detail collected.                                                                                                                                                                                                                                                                                                          | You can't change the logging<br>level.                                                    |
| Cost                  | There is a cost for these logs, as part<br>of your charges for Amazon CloudWatch Logs. See [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").<br>Remember to [remove the<br>logs](working-with-logs.md#manage-log-storage "working-with-logs.md#manage-log-storage") after you delete the<br>channel. | These logs are free.                                                                      |
| CloudWatch log stream | The log stream is named after the<br>ARN/pipeline.                                                                                                                                                                                                                                                                                                                       | The log stream is named after the<br>ARN/pipeline with `_as_run`<br>appended to the name. |
| Automation            | You should not automate any processing<br>based on the wording in these logs because<br>that wording is subject to change.(By<br>comparison, you can automate based on<br>the wording in alerts, which are<br>accessed using CloudWatch Events, because the<br>wording of alerts does not change.)                                                                       | You can automate based on the wording in<br>these logs.                                   |
