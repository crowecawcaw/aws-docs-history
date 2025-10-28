# Supported logs and discovered

fields

CloudWatch Logs Insights supports different log types. For every log that's sent to a Standard class
log group in Amazon CloudWatch Logs, CloudWatch Logs Insights automatically generates five system fields:

- `@message` contains the raw unparsed log event. This is the
  equivalent to the `message` field in [InputLogevent](../../../AmazonCloudWatchLogs/latest/APIReference/API_InputLogEvent.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_InputLogEvent.md").
- `@timestamp` contains the event timestamp in the log event's
  `timestamp` field. This is the equivalent to the
  `timestamp` field in [InputLogevent](../../../AmazonCloudWatchLogs/latest/APIReference/API_InputLogEvent.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_InputLogEvent.md").
- `@ingestionTime` contains the time when CloudWatch Logs received the log
  event.
- `@logStream` contains the name of the log stream that the log event
  was added to. Log streams group logs through the same process that generated
  them.
- `@log` is a log group identifier in the form of
  ``account-id`:`log-group-name``.
  When querying multiple log groups, this can be useful to identify which log
  group a particular event belongs to.
- `@entity` contains flattened JSON related to entities for the
  [Explore related
  telemetry](../monitoring/ExploreRelated.md "../monitoring/ExploreRelated.md") feature.

For example, this JSON can represent an entity.

```
{
  "Entity": {
    "KeyAttributes": {
      "Type": "Service",
      "Name": "PetClinic"
    },
    "Attributes": {
      "PlatformType": "AWS::EC2",
      "EC2.InstanceId": "i-1234567890123"
    }
  }
}
```

For this entity, the extracted system fields would be the following:

```
@entity.KeyAttributes.Type = Service
@entity.KeyAttributes.Name = PetClinic
@entity.Attributes.PlatformType = AWS::EC2
@entity.Attributes.EC2.InstanceId = i-1234567890123
```

###### Note

Field discovery is supported only for log groups in the Standard log class. For
more information about log classes, see [Log classes](CloudWatch_Logs_Log_Classes.md "CloudWatch_Logs_Log_Classes.md").

CloudWatch Logs Insights inserts the **@** symbol at the start of fields that it
generates.

For many log types, CloudWatch Logs also automatically discovers the log fields contained in the
logs. These automatic discovery fields are shown in the following table.

For other types of logs with fields that CloudWatch Logs Insights doesn't automatically discover, you
can use the `parse` command to extract and create extracted fields for use in
that query. For more information, see [CloudWatch Logs Insights language query syntax](CWL_QuerySyntax.md "CWL_QuerySyntax.md").

If the name of a discovered log field starts with the `@` character,
CloudWatch Logs Insights displays it with an additional `@` appended to the beginning. For
example, if a log field name is `@example.com`, this field name is displayed
as `@@example.com`.

###### Note

Except for `@message`, `@timestamp`, or `@log`,
you can create field indexes for discovered fields. For more information about field
indexes, see [Create field indexes to improve query
performance and reduce scan volume](CloudWatchLogs-Field-Indexing.md "CloudWatchLogs-Field-Indexing.md").

| Log type                                                              | Discovered log fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon VPC flow logs                                                  | `@timestamp`, `@logStream`, `@message`, `accountId`, `endTime`, `interfaceId`, `logStatus`, `startTime`, `version`, `action`, `bytes`, `dstAddr`, `dstPort`, `packets`, `protocol`, `srcAddr`, `srcPort`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Route 53 logs                                                         | `@timestamp`, `@logStream`, `@message`, `edgeLocation`, `ednsClientSubnet`, `hostZoneId`, `protocol`, `queryName`, `queryTimestamp`, `queryType`, `resolverIp`, `responseCode`, `version`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Lambda logs                                                           | `@timestamp`, `@logStream`, `@message`, `@requestId`, `@duration,` `@billedDuration`, `@type`, `@maxMemoryUsed`, `@memorySize` If a Lambda log line contains an X-Ray trace ID, it also includes the following fields: `@xrayTraceId` and `@xraySegmentId`. CloudWatch Logs Insights automatically discovers log fields in Lambda logs, but only for the first embedded JSON fragment in each log event. If a Lambda log event contains multiple JSON fragments, you can parse and extract the log fields by using the `**parse**` command. For more information, see [Fields in JSON logs](#CWL_AnalyzeLogData-discoverable-JSON-logs "#CWL_AnalyzeLogData-discoverable-JSON-logs").                                           |
| CloudTrail logs Logs in JSON format                                   | For more information, see [Fields in JSON logs](#CWL_AnalyzeLogData-discoverable-JSON-logs "#CWL_AnalyzeLogData-discoverable-JSON-logs").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Other log types                                                       | `@timestamp`, `@ingestionTime`, `@logStream`, `@message`, `@log`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | ## Fields in JSON logs With CloudWatch Logs Insights, you use dot notation to represent JSON fields. This section contains an example JSON event and code snippet that show how you can access JSON fields using dot notation. **Example: JSON event** `{ "eventVersion": "1.0", "userIdentity": { "type": "IAMUser", "principalId": "EX_PRINCIPAL_ID", "arn": "arn: aws: iam: : 123456789012: user/Alice", "accessKeyId": "EXAMPLE_KEY_ID", "accountId": "123456789012", "userName": "Alice" }, "eventTime": "2014-03-06T21: 22: 54Z", "eventSource": "ec2.amazonaws.com", "eventName": "StartInstances", "awsRegion": "us-east-2", "sourceIPAddress": "192.0.2.255", "userAgent": "ec2-api-tools1.6.12.2", "requestParameters": { "instancesSet": { "items": [ { "instanceId": "i-abcde123" } ] } }, "responseElements": { "instancesSet": { "items": [ { "instanceId": "i-abcde123", "currentState": { "code": 0, "name": "pending" }, "previousState": { "code": 80, "name": "stopped" } } ] } } }` The example JSON event contains an object that's named `userIdentity`. `userIdentity` contains a field that's named `type`. To represent value of `type` using dot notation, you use `userIdentity.type`. The example JSON event contains arrays that flatten to lists of nested field names and values. To represent the value of `instanceId` for the first item in `requestParameters.instancesSet`, you use `requestParameters.instancesSet.items.0.instanceId`. The number `0` that's placed before the field `instanceID` refers to the position of values for the field `items`. The following example contains a code snippet that shows how you can access nested JSON fields in a JSON log event. **Example: Query** ``` fields @timestamp, @message |
| filter requestParameters.instancesSet.items.0.instanceId="i-abcde123" | sort @timestamp desc ```The code snippet shows a query that uses dot notation with the`filter`command to access the value of the nested JSON field`instanceId`. The query filters on messages where the value of `instanceId`equals`"i-abcde123"`and returns all of the log events that contain the specified value. ###### Note CloudWatch Logs Insights can extract a maximum of 200 log event fields from a JSON log. For additional fields that aren't extracted, you can use the`parse`command to extract the fields from the raw unparsed log event in the message field. For more information about the`parse` command, see [Query syntax](CWL_QuerySyntax.md "CWL_QuerySyntax.md") in the Amazon CloudWatch User Guide. |
