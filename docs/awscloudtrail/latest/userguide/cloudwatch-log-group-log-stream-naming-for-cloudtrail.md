# CloudWatch log group and log stream naming for CloudTrail

Amazon CloudWatch will display the log group that you created for CloudTrail events alongside any other
log groups you have in a Region. We recommend that you use a log group name that helps you
easily distinguish the log group from others. For example,
`CloudTrail/logs`.

Follow these guidelines when naming a log group:

- Log group names must be unique within a Region for an AWS account.
- Log group names can be between 1 and 512 characters long.
- Log group names consist of the following characters: a-z, A-Z, 0-9, '\_' (underscore), '-' (hyphen),
  '/' (forward slash), '.' (period), and '#' (number sign).
  When CloudTrail creates the log stream for the log group, it names the log stream according to
  the following format:
  `account_ID`\_CloudTrail\_`trail_region`.

###### Note

If the volume of CloudTrail logs is large, multiple log streams may be created to deliver log data
to your log group. When there are multiple log streams, CloudTrail names each log stream
according to the following format:
`account_ID`\_CloudTrail\_`trail_region`\_`number`.

For more information about CloudWatch log groups, see
[Working with log groups and log streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the _Amazon CloudWatch Logs User Guide_ and
[CreateLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md")
in the _Amazon CloudWatch Logs API Reference_.
