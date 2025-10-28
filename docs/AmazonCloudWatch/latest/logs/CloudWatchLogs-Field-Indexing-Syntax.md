# Field index syntax and

quotas

You create field indexes by creating _field index policies_.
You can create account-level index policies that apply to your whole account, and
you can also create policies that apply to only a single log group. For account-wide
index policies, you can have one that applies to all log groups in the account. You
can also create account-level index policies that apply to a subset of log groups in
the account, selected by the prefixes of their log group names. If you have multiple
account-level policies in the same account, the log group name prefixes for these
policies can't overlap.

Log group-level field index policies override account-level field index policies:
if you create log-group level index policy, that log group uses only that policy and
ignores the account-level policies.

Matches of log events to the names of field indexes are case-sensitive. For
example, a field index of `RequestId` won't match a log event containing
`requestId`.

You can have as many as 20 account-level index policies. If you have multiple
account-level index policies filtered to log group name prefixes, no two of them can
use the same or overlapping log group name prefixes. For example, if you have one
policy filtered to log groups that start with `my-log`, you can't have
another field index policy filtered to `my-logpprod` or
`my-logging`.

If you have an account-level index policy that has no name prefixes and applies to
all log groups, then no other account-level index policy can be created.

Each index policy has the following quotas and restrictions:

- As many as 20 fields can be included in the policy.
- Each field name can include as many as 100 characters.
- To create an index of a custom field in your log groups that starts with
  `@`, you must specify the field with an extra `@`
  at the beginning of the field name. For example, if your log events include
  a field named `@userId`, you must specify `@@userId`
  to create an index for this field.
  **Generated fields and reserved fields**

CloudWatch Logs Insights automatically generates system fields in each log event. These generated
fields are prefixed with `@` For more information about generated fields,
see [Supported logs and discovered
fields](CWL_AnalyzeLogData-discoverable-fields.md "CWL_AnalyzeLogData-discoverable-fields.md").

Of these generated fields, the following are supported for use as field
indexes:

- `@logStream`
- `@ingestionTime`
- `@requestId`
- `@type`
- `@initDuration`
- `@duration`
- `@billedDuration`
- `@memorySize`
- `@maxMemoryUsed`
- `@xrayTraceId`
- `@xraySegmentId`
  To index these generated fields, you don't need to add an extra `@`
  when specifying them, as you have to do for custom fields that start with
  `@`. For example, to create a field index for
  `@logStream`, just specify `@logStream` as the field
  index.

CloudWatch Logs provides default field indexes for all log groups in the Standard log class. Default field
indexes are automatically available for the following fields:

- `@logStream`
- `@aws.region`
- `@aws.account`
- `@source.log`
- `traceId`
  Default field indexes are in addition to any custom
  field indexes you define within your policy. Default field indexes are not counted
  towards your field index quota.

**Child fields and array fields in JSON logs**

You can index fields that are nested child fields or array fields in JSON
logs.

For example, you can create an index of the `accessKeyId` child field
within the `userIdentity` field within this log:

```
{
    "eventVersion": "1.0",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "EXAMPLE_PRINCIPAL_ID",
        "arn": "arn: aws: iam: : 123456789012: user/Alice",
        "accessKeyId": "11112222",
        "accountId": "123456789012",
        "userName": "Alice"
    },
    "eventTime": "2014-03-06T21: 22: 54Z",
    "eventSource": "ec2.amazonaws.com",
    "eventName": "StartInstances",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "192.0.2.255",
    "userAgent": "ec2-api-tools1.6.12.2",
    "requestParameters": {
        "instancesSet": {
            "items": [{
                "instanceId": "i-abcde123",
                "currentState": {
                    "code": 0,
                    "name": "pending"
                },
                "previousState": {
                    "code": 80,
                    "name": "stopped"
                }
            }]
        }
    }
}
```

To create this field, you refer to it using dot notation
(`userIdentity.accessKeyId`) both when creating the field index and
when specifying it in a query. The query could look like this:

````
fields @timestamp, @message
| filterIndex userIdentity.accessKeyId = "11112222" ``` In the previous example event, the `instanceId` field is in an array within `requestParameters.instancesSet.items` To represent this field both when creating the field index and when querying, refer to it as `requestParameters.instancesSet.items.0.instanceId` The 0 refers to that field's place in the array. Then a query for this field could be the following: ``` fields @timestamp, @message
| filterIndex requestParameters.instancesSet.items.0.instanceId="i-abcde123" ```
````
