# Viewing Insights events for trails with the AWS CLI

This section describes how to use the AWS CLI `lookup-events`
command to lookup the last 90 days of Insights events for a trail with Insights events enabled. For
information about how to enable CloudTrail Insights on a trail, see [Logging Insights events for a trail using
the AWS CLI](insights-events-CLI-enable.md#insights-events-CLI-enable-trails "insights-events-CLI-enable.md#insights-events-CLI-enable-trails").

###### Note

You cannot use the `lookup-events` command
to lookup Insights events for an event data store, however, CloudTrail Lake offers a number of sample queries
for Insights event data stores. For more information, see [Viewing sample queries for
Insights events](insights-events-view-lake.md#insights-events-lake-queries "insights-events-view-lake.md#insights-events-lake-queries").

The `lookup-events` command has the following options:

- `--end-time`
- `--event-category`
- `--max-results`
- `--start-time`
- `--lookup-attributes`
- `--next-token`
- `--generate-cli-skeleton`
- `--cli-input-json`
  For general information about using the AWS Command Line Interface, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

###### Contents

- [Prerequisites](view-insights-events-cli.md#aws-cli-prerequisites-for-insights "view-insights-events-cli.md#aws-cli-prerequisites-for-insights")
- [Getting command line help](view-insights-events-cli.md#getting-command-line-help-insights "view-insights-events-cli.md#getting-command-line-help-insights")
- [Looking up Insights events](view-insights-events-cli.md#looking-up-insights-with-the-aws-cli "view-insights-events-cli.md#looking-up-insights-with-the-aws-cli")
- [Specifying the number of Insights events to return](view-insights-events-cli.md#specify-the-number-of-insights-to-return "view-insights-events-cli.md#specify-the-number-of-insights-to-return")
- [Looking up Insights events by time range](view-insights-events-cli.md#look-up-insights-by-time-range "view-insights-events-cli.md#look-up-insights-by-time-range")
- [Looking up Insights events by attribute](view-insights-events-cli.md#look-up-insights-by-attributes "view-insights-events-cli.md#look-up-insights-by-attributes")
  - [Attribute lookup examples](view-insights-events-cli.md#attribute-lookup-example-insights "view-insights-events-cli.md#attribute-lookup-example-insights")

- [Specifying the next page of results](view-insights-events-cli.md#specify-next-page-of-results "view-insights-events-cli.md#specify-next-page-of-results")
- [Getting JSON input from a file](view-insights-events-cli.md#json-input-from-file-insights "view-insights-events-cli.md#json-input-from-file-insights")
- [Lookup output fields](view-insights-events-cli.md#view-insights-events-cli-output-fields "view-insights-events-cli.md#view-insights-events-cli-output-fields")

## Prerequisites

- To run AWS CLI commands, you must install the AWS CLI. For more information, see
  [Get started with the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md").
- Make sure your AWS CLI version is greater than 1.6.6. To verify the CLI version,
  run **aws --version** on the command line.
- To set the account, Region, and default output format for an AWS CLI session,
  use the **aws configure** command. For more information, see
  [Configuring the AWS
  Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md").
- To log Insights events on the API call rate, the trail must log `write` management events.
  To log Insights events on the API error rate, the trail must log `read` or `write` management events.

###### Note

The CloudTrail AWS CLI commands are case-sensitive.

## Getting command line help

To see the command line help for `lookup-events`, type the following
command.

```
aws cloudtrail lookup-events help
```

## Looking up Insights events

To see the ten latest Insights events, type the following command.

```
aws cloudtrail lookup-events --event-category insight
```

A returned event looks similar to the following example,

```
{
    "NextToken": "kbOt5LlZe++mErCebpy2TgaMgmDvF1kYGFcH64JSjIbZFjsuvrSqg66b5YGssKutDYIyII4lrP4IDbeQdiObkp9YAlju3oXd12juEXAMPLE=",
    "Events": [
        {
            "eventVersion": "1.09",
            "eventTime": "2024-12-11T16:52:00Z",
            "awsRegion": "us-east-1",
            "eventID": "18378b1e-3653-433d-ba1e-aa11a5958f0c",
            "eventType": "AwsCloudTrailInsight",
            "recipientAccountId": "888888888888",
            "sharedEventID": "fccb064f-dd07-4822-97c0-11115d8b91d4",
            "insightDetails": {
                "state": "Start",
                "eventSource": "cloudtrail.amazonaws.com",
                "eventName": "DescribeQuery",
                "insightType": "ApiErrorRateInsight",
                "errorCode": "QueryIdNotFoundException",
                "insightContext": {
                    "statistics": {
                        "baseline": {
                            "average": 0
                        },
                        "insight": {
                            "average": 1.2
                        },
                        "insightDuration": 5,
                        "baselineDuration": 11092
                    },
                    "attributions": [
                        {
                            "attribute": "userIdentityArn",
                            "insight": [
                                {
                                    "value": "arn:aws:sts::888888888888:assumed-role/Admin",
                                    "average": 1.2
                                }
                            ],
                            "baseline": []
                        },
                        {
                            "attribute": "userAgent",
                            "insight": [
                                {
                                    "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
                                    "average": 1.2
                                }
                            ],
                            "baseline": []
                        }
                    ]
                }
            },
            "eventCategory": "Insight"
        },
        {
            "eventVersion": "1.09",
            "eventTime": "2024-12-11T16:53:00Z",
            "awsRegion": "us-east-1",
            "eventID": "b32f10a0-f039-419a-bad7-e95468930a4f",
            "eventType": "AwsCloudTrailInsight",
            "recipientAccountId": "888888888888",
            "sharedEventID": "fccb064f-dd07-4822-97c0-11115d8b91d4",
            "insightDetails": {
                "state": "End",
                "eventSource": "cloudtrail.amazonaws.com",
                "eventName": "DescribeQuery",
                "insightType": "ApiErrorRateInsight",
                "errorCode": "QueryIdNotFoundException",
                "insightContext": {
                    "statistics": {
                        "baseline": {
                            "average": 0
                        },
                        "insight": {
                            "average": 6
                        },
                        "insightDuration": 1,
                        "baselineDuration": 11092
                    },
                    "attributions": [
                        {
                            "attribute": "userIdentityArn",
                            "insight": [
                                {
                                    "value": "arn:aws:sts::888888888888:assumed-role/Admin",
                                    "average": 6
                                }
                            ],
                            "baseline": []
                        },
                        {
                            "attribute": "userAgent",
                            "insight": [
                                {
                                    "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
                                    "average": 6
                                }
                            ],
                            "baseline": []
                        }
                    ]
                }
            },
            "eventCategory": "Insight"
        }
    ]
}
```

For an explanation of the lookup-related fields in the output, see [Lookup output fields](#view-insights-events-cli-output-fields "#view-insights-events-cli-output-fields") in this topic. For an
explanation of fields in the Insights event,
see [CloudTrail record contents for Insights events for trails](cloudtrail-insights-fields-trails.md "cloudtrail-insights-fields-trails.md").

## Specifying the number of Insights events to return

To specify the number of events to return, type the following command.

```
aws cloudtrail lookup-events --event-category insight --max-results `<integer>`
```

The default value for `<integer>`, if it is not
specified, is 10. Possible values are 1 through 50. The following example returns one
result.

```
aws cloudtrail lookup-events --event-category insight --max-results 1
```

## Looking up Insights events by time range

Insights events from the past 90 days are available for lookup. To specify a time range, type
the following command.

```
aws cloudtrail lookup-events --event-category insight --start-time `<timestamp>` --end-time `<timestamp>`
```

`--start-time `<timestamp>`` specifies, in UTC, that
only Insights events that occur after or at the specified time are returned. If the specified
start time is after the specified end time, an error is returned.

`--end-time `<timestamp>`` specifies, in UTC, that
only Insights events that occur before or at the specified time are returned. If the specified
end time is before the specified start time, an error is returned.

The default start time is the earliest date that data is available within the last 90
days. The default end time is the time of the event that occurred closest to the current
time.

All timestamps are shown in UTC.

## Looking up Insights events by attribute

To filter by an attribute, type the following command.

```
aws cloudtrail lookup-events --event-category insight --lookup-attributes AttributeKey=`<attribute>`,AttributeValue=`<string>`
```

You can specify only one attribute key-value pair for each
**lookup-events** command. The following are valid Insights event
values for `AttributeKey`. Value names are case sensitive.

- `EventId`
- `EventName`
- `EventSource`

The maximum length for the `AttributeValue` is 2000 characters. The
following characters ('`_`', '', '`,`',
'`\\n`') count as two characters towards the 2000 character limit.

### Attribute lookup examples

The following example command returns Insights events in which the value of
`EventName` is `PutRule`.

```
aws cloudtrail lookup-events --event-category insight --lookup-attributes AttributeKey=EventName, AttributeValue=PutRule
```

The following example command returns Insights events in which the value of
`EventId` is
`b5cc8c40-12ba-4d08-a8d9-2bceb9a3e002`.

```
aws cloudtrail lookup-events --event-category insight --lookup-attributes AttributeKey=EventId, AttributeValue=b5cc8c40-12ba-4d08-a8d9-2bceb9a3e002
```

The following example command returns Insights events in which the value of
`EventSource` is `iam.amazonaws.com`.

```
aws cloudtrail lookup-events --event-category insight --lookup-attributes AttributeKey=EventSource, AttributeValue=iam.amazonaws.com
```

## Specifying the next page of results

To get the next page of results from a `lookup-events` command, type the
following command.

```
aws cloudtrail lookup-events --event-category insight `<same parameters as previous command>` --next-token=`<token>`
```

In this command, the value for `<token>` is taken from
the first field of the output of the previous command.

When you use `--next-token` in a command, you must use the same parameters
as in the previous command. For example, suppose you run the following command.

```
aws cloudtrail lookup-events --event-category insight --lookup-attributes AttributeKey=EventName, AttributeValue=PutRule
```

To get the next page of results, your next command would look like the
following.

```
aws cloudtrail lookup-events --event-category insight --lookup-attributes AttributeKey=EventName,AttributeValue=PutRule --next-token=EXAMPLEZe++mErCebpy2TgaMgmDvF1kYGFcH64JSjIbZFjsuvrSqg66b5YGssKutDYIyII4lrP4IDbeQdiObkp9YAlju3oXd12juEXAMPLE=
```

## Getting JSON input from a file

The AWS CLI for some AWS services has two parameters,
`--generate-cli-skeleton` and `--cli-input-json`, that you can
use to generate a JSON template, which you can modify and use as input to the
`--cli-input-json` parameter. This section describes how to use these
parameters with `aws cloudtrail lookup-events`. For more information, see
[AWS CLI skeletons and input files](../../../cli/latest/userguide/cli-usage-skeleton.md "../../../cli/latest/userguide/cli-usage-skeleton.md").

###### To look up Insights events by getting JSON input from a file

1. Create an input template for use with `lookup-events` by
   redirecting the `--generate-cli-skeleton` output to a file, as in the
   following example.

```
aws cloudtrail lookup-events --event-category insight --generate-cli-skeleton > LookupEvents.txt
```

The template file generated (in this case, LookupEvents.txt) looks like the
following.

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
   following example.

```
aws cloudtrail lookup-events --event-category insight --cli-input-json file://LookupEvents.txt
```

###### Note

You can use other arguments on the same command line as
`--cli-input-json`.

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

For more information about CloudTrail Insights events, see [Working with CloudTrail Insights](logging-insights-events-with-cloudtrail.md "logging-insights-events-with-cloudtrail.md") in this guide.
