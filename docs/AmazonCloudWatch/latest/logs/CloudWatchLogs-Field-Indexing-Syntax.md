# Field index syntax and

quotas

You create field indexes by creating _field index policies_.
You can create account-level index policies that apply to your whole account, and
you can also create policies that apply to only a single log group. For account-wide
index policies, you can have one that applies to all log groups in the account. You
can also create account-level index policies that apply to a subset of log groups in
the account, selected by the prefixes of their log group names. If you have multiple
account-level policies in the same account, the log group name prefixes for these
policies can't overlap. Similarly, you can create account-level index policies that
apply to a specific data source name and type combination. Only one account policy
can be created per data source name and type combination.

Log group-level field index policies override account-level field index policies:
which apply to the log group as a whole (such as, account-level policies with no
selection criteria or with log group name prefix based selection criteria).
Account-level policies which match at the log event level (such as, for a given data
source name and type combination) will apply in addition to policies which match the
log group as a whole. If you create log-group level index policy, that log group
does not use account-level policies that match at the log group level.

Matches of log events to the names of field indexes are case-sensitive. For
example, a field index of `RequestId` won't match a log event containing
`requestId`.

You can have as many as 40 account-level index policies, of these policies 20 can
use log group name prefix selection criteria and 20 can use data source based
selection criteria. If you have multiple account-level index policies filtered to
log group name prefixes, no two of them can use the same or overlapping log group
name prefixes. For example, if you have one policy filtered to log groups that start
with `my-log`, you can't have another field index policy filtered to
`my-logpprod` or `my-logging`. Similarly, if you have
multiple account-level index policies filtered to data source name and type
combinations, no two of them can use the same data source name and type. For
example, if you have one policy filtered to the data source name
`amazon_vpc` and data source type `flow` you cannot create
another policy with this combination.

If you have an account-level index policy that has no name prefixes and applies to
all log groups, then no other account-level index policy with log group name prefix
filters can be created; you can create account-level index policies which use data
source name and type filters.

Each index policy has the following quotas and restrictions:

- As many as 20 fields can be included in the policy.
- Each field name can include as many as 100 characters.
- To create an index of a custom field in your log groups that starts with
  `@`, you must specify the field with an extra `@`
  at the beginning of the field name. For example, if your log events include
  a field named `@userId`, you must specify `@@userId`
  to create an index for this field.
  For account-level index policies with data source name and type based selection
  criteria an additional restriction applies: all of the fields must be primitive data
  types, nested primitives are only supported for structs.

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
- `@data_source_name`
- `@data_source_type`
- `@data_format`
- `traceId`
- `severityText`
- `attributes.session.id`
  CloudWatch Logs provides default field indexes for certain data source name and type combinations as well. Default field indexes are automatically available for the following data source name and type combinations:

| Data Source Name and Type                            | Default Field Indexes                                                                                                                                         |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `amazon_vpc.flow`                                    | `action`<br>`logStatus`<br>`region`<br>`flowDirection`<br>`type`                                                                                              |
| `amazon_route53.resolver_query`                      | `query_type`<br>`transport`<br>`rcode`                                                                                                                        |
| `aws_waf.access`                                     | `action`<br>`httpRequest.country`                                                                                                                             |
| `aws_cloudtrail.data`<br>`aws_cloudtrail.management` | `eventSource`<br>`eventName`<br>`awsRegion`<br>`userAgent`<br>`errorCode`<br>`eventType`<br>`managementEvent`<br>`readOnly`<br>`eventCategory`<br>`requestId` |

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

```
fields @timestamp, @message
| filterIndex userIdentity.accessKeyId = "11112222"

```

In the previous example event, the `instanceId` field is in an array
within `requestParameters.instancesSet.items` To represent this field
both when creating the field index and when querying, refer to it as
`requestParameters.instancesSet.items.0.instanceId` The 0 refers to
that field's place in the array.

Then a query for this field could be the following:

```
fields @timestamp, @message
| filterIndex requestParameters.instancesSet.items.0.instanceId="i-abcde123"

```
