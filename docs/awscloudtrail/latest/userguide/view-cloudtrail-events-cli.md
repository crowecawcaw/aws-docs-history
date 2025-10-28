# Viewing recent management events with the AWS CLI

You can look up CloudTrail management events for the last 90 days for the current
AWS Region using the **aws cloudtrail lookup-events**
command. The **aws cloudtrail lookup-events** command shows
events in the AWS Region where they occurred.

Lookup supports
the following attributes for management events:

- AWS access key
- Event ID
- Event name
- Event source
- Read only
- Resource name
- Resource type
- User name
  All attributes are optional.

The [`lookup-events`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/lookup-events.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/lookup-events.html") command includes the following options:

- `--max-items` `<integer>` – The total number of items to return in the command's output. If the
  total number of items available is more than the value specified, a
  `NextToken` is provided in the command's output. To resume pagination,
  provide the `NextToken` value in the starting-token argument of a sub-
  sequent command. Do not use the `NextToken` response element directly
  outside of the AWS CLI.
- `--start-time` `<timestamp>` – Specifies that only events that occur after or at the specified time
  are returned. If the specified start time is after the specified end
  time, an error is returned.
- `--lookup-attributes` `<integer>` – Contains a list of lookup attributes. Currently the list can contain
  only one item.
- `--generate-cli-skeleton` `<string>` – Prints a JSON skeleton to standard
  output without sending an API request. If provided with no value or the
  value input, prints a sample input JSON that can be used as an argument
  for `--cli-input-json`. Similarly, if provided yaml-input it will print a
  sample input YAML that can be used with `--cli-input-yaml`. If provided
  with the value output, it validates the command inputs and returns a
  sample output JSON for that command. The generated JSON skeleton is not
  stable between versions of the AWS CLI and there are no backwards
  compatibility guarantees in the JSON skeleton generated.
- `--cli-input-json` `<string>` – Reads arguments from the
  JSON string provided. The JSON string follows the format provided by the
  `--generate-cli-skeleton` parameter. If other arguments are provided on the command
  line, those values will override the JSON-provided values. It is not
  possible to pass arbitrary binary values using a JSON-provided value as
  the string will be taken literally. This may not be specified along
  with the `--cli-input-yaml` parameter.
  For general information about using the AWS Command Line Interface, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

###### Contents

- [Prerequisites](view-cloudtrail-events-cli.md#aws-cli-prerequisites-for-aws-cloudtrail "view-cloudtrail-events-cli.md#aws-cli-prerequisites-for-aws-cloudtrail")
- [Getting command line help](view-cloudtrail-events-cli.md#getting-command-line-help "view-cloudtrail-events-cli.md#getting-command-line-help")
- [Looking up events](view-cloudtrail-events-cli.md#looking-up-events-with-the-aws-cli "view-cloudtrail-events-cli.md#looking-up-events-with-the-aws-cli")
- [Specifying the number of events to return](view-cloudtrail-events-cli.md#specify-the-number-of-events-to-return "view-cloudtrail-events-cli.md#specify-the-number-of-events-to-return")
- [Looking up events by time range](view-cloudtrail-events-cli.md#look-up-events-by-time-range "view-cloudtrail-events-cli.md#look-up-events-by-time-range")
- [Looking up events by attribute](view-cloudtrail-events-cli.md#look-up-events-by-attributes "view-cloudtrail-events-cli.md#look-up-events-by-attributes")
  - [Attribute lookup examples](view-cloudtrail-events-cli.md#attribute-lookup-example "view-cloudtrail-events-cli.md#attribute-lookup-example")

- [Specifying the next page of results](view-cloudtrail-events-cli.md#specify-next-page-of-lookup-results "view-cloudtrail-events-cli.md#specify-next-page-of-lookup-results")
- [Getting JSON input from a file](view-cloudtrail-events-cli.md#json-input-from-file "view-cloudtrail-events-cli.md#json-input-from-file")
- [Lookup output fields](view-cloudtrail-events-cli.md#view-cloudtrail-events-cli-output-fields "view-cloudtrail-events-cli.md#view-cloudtrail-events-cli-output-fields")

## Prerequisites

- To run AWS CLI commands, you must install the AWS CLI. For information, see [Get started with the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md").
- Make sure your AWS CLI version is greater than 1.6.6. To verify the CLI version,
  run **aws --version** on the command line.
- To set the account, AWS Region, and default output format for an AWS CLI session,
  use the **aws configure** command. For more
  information, see [Configuring the AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md").

###### Note

The CloudTrail AWS CLI commands are case-sensitive.

## Getting command line help

To see the command line help for `lookup-events`, type the following
command:

```
aws cloudtrail lookup-events help
```

## Looking up events

###### Important

The rate of lookup requests is limited to two per second, per account, per Region. If
this limit is exceeded, a throttling error occurs.

To see the ten latest events, type the following command:

```
aws cloudtrail lookup-events --max-items 10
```

A returned event looks similar to the following fictitious example, which has been
formatted for readability:

```
{
    "NextToken": "kbOt5LlZe++mErCebpy2TgaMgmDvF1kYGFcH64JSjIbZFjsuvrSqg66b5YGssKutDYIyII4lrP4IDbeQdiObkp9YAlju3oXd12juy3CIZW8=",
    "Events": [
        {
            "EventId": "0ebbaee4-6e67-431d-8225-ba0d81df5972",
            "Username": "root",
            "EventTime": 1424476529.0,
            "CloudTrailEvent": "{
                  \"eventVersion\":\"1.02\",
                  \"userIdentity\":{
                        \"type\":\"Root\",
                        \"principalId\":\"111122223333\",
                        \"arn\":\"arn:aws:iam::111122223333:root\",
                        \"accountId\":\"111122223333\"},
                  \"eventTime\":\"2015-02-20T23:55:29Z\",
                  \"eventSource\":\"signin.amazonaws.com\",
                  \"eventName\":\"ConsoleLogin\",
                  \"awsRegion\":\"us-east-2\",
                  \"sourceIPAddress\":\"203.0.113.4\",
                  \"userAgent\":\"Mozilla/5.0\",
                  \"requestParameters\":null,
                  \"responseElements\":{\"ConsoleLogin\":\"Success\"},
                  \"additionalEventData\":{
                         \"MobileVersion\":\"No\",
                         \"LoginTo\":\"https://console.aws.amazon.com/console/home",
                         \"MFAUsed\":\"No\"},
                  \"eventID\":\"0ebbaee4-6e67-431d-8225-ba0d81df5972\",
                  \"eventType\":\"AwsApiCall\",
                  \"recipientAccountId\":\"111122223333\"}",
            "EventName": "ConsoleLogin",
            "Resources": []
        }
    ]
}
```

For an explanation of the lookup-related fields in the output, see the section [Lookup output fields](#view-cloudtrail-events-cli-output-fields "#view-cloudtrail-events-cli-output-fields") later in this document.
For an explanation of the fields in the CloudTrail event, see [CloudTrail record contents for management, data, and network activity events](cloudtrail-event-reference-record-contents.md "cloudtrail-event-reference-record-contents.md").

## Specifying the number of events to return

To specify the number of events to return, type the following command:

```
aws cloudtrail lookup-events --max-items `<integer>`
```

Possible values are 1 through 50. The following example returns one event.

```
aws cloudtrail lookup-events --max-items 1
```

## Looking up events by time range

Events from the past 90 days are available for lookup. To specify a time range, type
the following command:

```
aws cloudtrail lookup-events --start-time `<timestamp>` --end-time `<timestamp>`
```

`--start-time `<timestamp>`` specifies, in UTC, that
only events that occur after or at the specified time are returned. If the specified
start time is after the specified end time, an error is returned.

`--end-time `<timestamp>`` specifies, in UTC, that
only events that occur before or at the specified time are returned. If the specified
end time is before the specified start time, an error is returned.

The default start time is the earliest date that data is available within the last 90
days. The default end time is the time of the event that occurred closest to the current
time.

All timestamps are shown in UTC.

## Looking up events by attribute

To filter by an attribute, type the following command:

```
aws cloudtrail lookup-events --lookup-attributes AttributeKey=`<attribute>`,AttributeValue=`<string>`
```

You can specify only one attribute key/value pair for each
**lookup-events** command. The following are valid values for
`AttributeKey`. Value names are case sensitive.

- `AccessKeyId`
- `EventId`
- `EventName`
- `EventSource`
- `ReadOnly`
- `ResourceName`
- `ResourceType`
- `Username`

The maximum length for the `AttributeValue` is 2000 characters. The
following characters ('`_`', '', '`,`',
'`\\n`') count as two characters towards the 2000 character limit.

### Attribute lookup examples

The following example command returns events in which the value of
`AccessKeyId` is `AKIAIOSFODNN7EXAMPLE`.

```
aws cloudtrail lookup-events --lookup-attributes AttributeKey=AccessKeyId,AttributeValue=AKIAIOSFODNN7EXAMPLE
```

The following example command returns the event for the specified CloudTrail
`EventId`.

```
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventId,AttributeValue=b5cc8c40-12ba-4d08-a8d9-2bceb9a3e002
```

The following example command returns events in which the value of
`EventName` is `RunInstances`.

```
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=RunInstances
```

The following example command returns events in which the value of
`EventSource` is `iam.amazonaws.com`.

```
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventSource,AttributeValue=iam.amazonaws.com
```

The following example command returns write events. It excludes read events such
as `GetBucketLocation` and `DescribeStream`.

```
aws cloudtrail lookup-events --lookup-attributes AttributeKey=ReadOnly,AttributeValue=false
```

The following example command returns events in which the value of
`ResourceName` is `CloudTrail_CloudWatchLogs_Role`.

```
aws cloudtrail lookup-events --lookup-attributes AttributeKey=ResourceName,AttributeValue=CloudTrail_CloudWatchLogs_Role
```

The following example command returns events in which the value of
`ResourceType` is `AWS::S3::Bucket`.

```
aws cloudtrail lookup-events --lookup-attributes AttributeKey=ResourceType,AttributeValue=AWS::S3::Bucket
```

The following example command returns events in which the value of
`Username` is `root`.

```
aws cloudtrail lookup-events --lookup-attributes AttributeKey=Username,AttributeValue=root
```

## Specifying the next page of results

To get the next page of results from a `lookup-events` command, type the
following command:

```
aws cloudtrail lookup-events `<same parameters as previous command>` --next-token=`<token>`
```

where the value for `<token>` is taken from the first
field of the output of the previous command.

When you use `--next-token` in a command, you must use the same parameters
as in the previous command. For example, suppose you run the following command:

```
aws cloudtrail lookup-events --lookup-attributes AttributeKey=Username,AttributeValue=root
```

To get the next page of results, your next command would look like this:

```
aws cloudtrail lookup-events --lookup-attributes AttributeKey=Username,AttributeValue=root --next-token=kbOt5LlZe++mErCebpy2TgaMgmDvF1kYGFcH64JSjIbZFjsuvrSqg66b5YGssKutDYIyII4lrP4IDbeQdiObkp9YAlju3oXd12juy3CIZW8=
```

## Getting JSON input from a file

The AWS CLI for some AWS services has two parameters,
`--generate-cli-skeleton` and `--cli-input-json`, that you can
use to generate a JSON template which you can modify and use as input to the
`--cli-input-json` parameter. This section describes how to use these
parameters with `aws cloudtrail lookup-events`. For more general information,
see [AWS CLI skeletons and input files](../../../cli/latest/userguide/cli-usage-skeleton.md "../../../cli/latest/userguide/cli-usage-skeleton.md").

###### To look up CloudTrail events by getting JSON input from a file

1. Create an input template for use with `lookup-events` by
   redirecting the `--generate-cli-skeleton` output to a file, as in the
   following example.

```
aws cloudtrail lookup-events --generate-cli-skeleton > LookupEvents.txt
```

The template file generated (in this case, LookupEvents.txt) looks like
this:

```

{
    "LookupAttributes": [
        {
            "AttributeKey": "",
            "AttributeValue": ""
        }
    ],
    "StartTime": null,
    "EndTime": null,
    "MaxResults": 0,
    "NextToken": ""
}

```

2. Use a text editor to modify the JSON as needed. The JSON input must contain
   only values that are specified.

###### Important

All empty or null values must be removed from the template before you can
use it.

The following example specifies a time range and maximum number of results to
return.

```
{
    "StartTime": "2023-11-01",
    "EndTime": "2023-12-12",
    "MaxResults": 10
}
```

3. To use the edited file as input, use the syntax `--cli-input-json
file://``<filename>`, as in the
   following example:

```
aws cloudtrail lookup-events --cli-input-json file://LookupEvents.txt
```

###### Note

You can use other arguments on the same command line as
`--cli-input-json` .

## Lookup output fields

**Events**

A list of lookup events based on the lookup attribute and time range that
were specified. The events list is sorted by time, with the latest event
listed first. Each entry contains information about the lookup request and
includes a string representation of the CloudTrail event that was retrieved.

The following entries describe the fields in each lookup event.

**CloudTrailEvent**

A JSON string that contains an object representation of the event
returned. For information about each of the elements returned, see [Record Body Contents](cloudtrail-event-reference-record-contents.md "cloudtrail-event-reference-record-contents.md").

**EventId**

A string that contains the GUID of the event returned.

**EventName**

A string that contains the name of the event returned.

**EventSource**

The AWS service that the request was made to.

**EventTime**

The date and time, in UNIX time format, of the event.

**Resources**

A list of resources referenced by the event that was returned. Each
resource entry specifies a resource type and a resource name.

**ResourceName**

A string that contains the name of the resource referenced by the event.

**ResourceType**

A string that contains the type of a resource referenced by the event.
When the resource type cannot be determined, null is returned.

**Username**

A string that contains the user name of the account for the event
returned.

**NextToken**

A string to get the next page of results from a previous
`lookup-events` command. To use the token, the parameters
must be the same as those in the original command. If no
`NextToken` entry appears in the output, there are no more
results to return.
