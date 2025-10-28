# Managing trails with the AWS CLI

The AWS CLI includes several other commands that help you manage your trails. These
commands add tags to trails, get trail status, start and stop logging for trails, and
delete a trail. You must run these commands from the same AWS Region where the trail
was created (its Home Region). When using the AWS CLI, remember that your commands run in
the AWS Region configured for your profile. If you want to run the commands in a
different Region, either change the default Region for your profile, or use the
**--region** parameter with the command.

###### Topics

- [Add one or more tags to a trail](#cloudtrail-additional-cli-commands-add-tag "#cloudtrail-additional-cli-commands-add-tag")
- [List tags for one or more trails](#cloudtrail-additional-cli-commands-list-tags "#cloudtrail-additional-cli-commands-list-tags")
- [Remove one or more tags from a trail](#cloudtrail-additional-cli-commands-remove-tag "#cloudtrail-additional-cli-commands-remove-tag")
- [Retrieving trail settings and the status of a trail](#cloudtrail-additional-cli-commands-retrieve "#cloudtrail-additional-cli-commands-retrieve")
- [Configuring CloudTrail Insights event selectors](#configuring-insights-selector "#configuring-insights-selector")
- [Configuring advanced event selectors](#configuring-adv-event-selector-examples "#configuring-adv-event-selector-examples")
- [Configuring basic event selectors](#configuring-event-selector-examples "#configuring-event-selector-examples")
- [Stopping and starting logging for a trail](#cloudtrail-start-stop-logging-cli-commands "#cloudtrail-start-stop-logging-cli-commands")
- [Deleting a trail](#cloudtrail-delete-trail-cli "#cloudtrail-delete-trail-cli")

## Add one or more tags to a trail

To add one or more tags to an existing trail, run the **add-tags**
command.

The following example adds a tag with the name `Owner`
and the value of `Mary` to a trail with the ARN of
`arn:aws:cloudtrail:`us-east-2`:`123456789012`:trail/`my-trail``
in the US East (Ohio) Region.

```
aws cloudtrail add-tags --resource-id arn:aws:cloudtrail:`us-east-2`:`123456789012`:trail/`my-trail` --tags-list Key=`Owner`,Value=`Mary` --region us-east-2
```

If successful, this command returns nothing.

## List tags for one or more trails

To view the tags associated with one or more existing trails, use the
**list-tags** command.

The following example lists the tags for `Trail1` and
`Trail2`.

```
aws cloudtrail list-tags --resource-id-list arn:aws:cloudtrail:`us-east-2`:`123456789012`:trail/`Trail1` arn:aws:cloudtrail:`us-east-2`:`123456789012`:trail/`Trail2`
```

If successful, this command returns output similar to the following.

```
{
 "ResourceTagList": [
     {
         "ResourceId": "arn:aws:cloudtrail:`us-east-2`:`123456789012`:trail/`Trail1`",
         "TagsList": [
             {
                 "Value": "`Alice`",
                 "Key": "`Name`"
             },
             {
                 "Value": "`Ohio`",
                 "Key": "`Location`"
             }
         ]
     },
     {
         "ResourceId": "arn:aws:cloudtrail:`us-east-2`:`123456789012`:trail/`Trail2`",
         "TagsList": [
             {
                 "Value": "`Bob`",
                 "Key": "`Name`"
             }
         ]
     }
  ]
}
```

## Remove one or more tags from a trail

To remove one or more tags from an existing trail, run the
**remove-tags** command.

The following example removes tags with the names
`Location` and `Name` from a
trail with the ARN of
`arn:aws:cloudtrail:`us-east-2`:`123456789012`:trail/`Trail1``
in the US East (Ohio) Region.

```
aws cloudtrail remove-tags --resource-id arn:aws:cloudtrail:`us-east-2`:`123456789012`:trail/`Trail1` --tags-list Key=Name Key=Location --region us-east-2
```

If successful, this command returns nothing.

## Retrieving trail settings and the status of a trail

Run the `describe-trails` command to retrieve information about trails
in an AWS Region. The following example returns information about trails
configured in the US East (Ohio) Region.

```
aws cloudtrail describe-trails --region us-east-2
```

If the command succeeds, you see output similar to the following.

```
{
  "trailList": [
    {
      "Name": "`my-trail`",
      "S3BucketName": "`amzn-s3-demo-bucket1`",
      "S3KeyPrefix": "`my-prefix`",
      "IncludeGlobalServiceEvents": true,
      "IsMultiRegionTrail": true,
      "HomeRegion": "`us-east-2`"
      "TrailARN": "arn:aws:cloudtrail:`us-east-2`:`123456789012`:trail/`my-trail`",
      "LogFileValidationEnabled": false,
      "HasCustomEventSelectors": false,
      "SnsTopicName": "`my-topic`",
      "IsOrganizationTrail": false,
    },
    {
      "Name": "`my-special-trail`",
      "S3BucketName": "`amzn-s3-demo-bucket2`",
      "S3KeyPrefix": "`example-prefix`",
      "IncludeGlobalServiceEvents": false,
      "IsMultiRegionTrail": false,
      "HomeRegion": "`us-east-2`",
      "TrailARN": "arn:aws:cloudtrail:`us-east-2`:`123456789012`:trail/`my-special-trail`",
      "LogFileValidationEnabled": false,
      "HasCustomEventSelectors": true,
      "IsOrganizationTrail": false
    },
    {
      "Name": "`my-org-trail`",
      "S3BucketName": "`amzn-s3-demo-bucket3`",
      "S3KeyPrefix": "`my-prefix`",
      "IncludeGlobalServiceEvents": true,
      "IsMultiRegionTrail": true,
      "HomeRegion": "`us-east-1`"
      "TrailARN": "arn:aws:cloudtrail:`us-east-2`:`123456789012`:trail/`my-org-trail`",
      "LogFileValidationEnabled": false,
      "HasCustomEventSelectors": false,
      "SnsTopicName": "`my-topic`",
      "IsOrganizationTrail": true
    }
  ]
}
```

Run the `get-trail` command to retrieve settings information about a
specific trail. The following example returns settings information for a trail named
`my-trail`.

```
aws cloudtrail get-trail - -name `my-trail`
```

If successful, this command returns output similar to the following.

```
{
   "Trail": {
      "Name": "`my-trail`",
      "S3BucketName": "`amzn-s3-demo-bucket`",
      "S3KeyPrefix": "`my-prefix`",
      "IncludeGlobalServiceEvents": true,
      "IsMultiRegionTrail": true,
      "HomeRegion": "`us-east-2`"
      "TrailARN": "arn:aws:cloudtrail:`us-east-2`:`123456789012`:trail/`my-trail`",
      "LogFileValidationEnabled": false,
      "HasCustomEventSelectors": false,
      "SnsTopicName": "`my-topic`",
      "IsOrganizationTrail": false,
   }
}
```

Run the `get-trail-status` command to retrieve the status of a trail.
You must either run this command from the AWS Region where it was created (the
Home Region), or you must specify that Region by adding the
**--region** parameter.

###### Note

If the trail is an organization trail and you are a member account in the
organization in AWS Organizations, you must provide the full ARN of that trail, and not
just the name.

```
aws cloudtrail get-trail-status --name `my-trail`
```

If the command succeeds, you see output similar to the following.

```
{
    "LatestDeliveryTime": 1441139757.497,
    "LatestDeliveryAttemptTime": "2015-09-01T20:35:57Z",
    "LatestNotificationAttemptSucceeded": "2015-09-01T20:35:57Z",
    "LatestDeliveryAttemptSucceeded": "2015-09-01T20:35:57Z",
    "IsLogging": true,
    "TimeLoggingStarted": "2015-09-01T00:54:02Z",
    "StartLoggingTime": 1441068842.76,
    "LatestDigestDeliveryTime": 1441140723.629,
    "LatestNotificationAttemptTime": "2015-09-01T20:35:57Z",
    "TimeLoggingStopped": ""
}
```

In addition to the fields shown in the preceding JSON code, the status contains
the following fields if there are Amazon SNS or Amazon S3 errors:

- `LatestNotificationError`. Contains the error emitted by Amazon SNS
  if a subscription to a topic fails.
- `LatestDeliveryError`. Contains the error emitted by Amazon S3 if
  CloudTrail cannot deliver a log file to a bucket.

## Configuring CloudTrail Insights event selectors

Enable Insights events on a trail by running the
**put-insight-selectors**, and specifying
`ApiCallRateInsight`, `ApiErrorRateInsight`, or both as
the value of the `InsightType` attribute. To view the Insights selector
settings for a trail, run the `get-insight-selectors` command. You must
either run this command from the AWS Region where the trail was created (the Home
Region), or you must specify that Region by adding the **--region**
parameter to the command.

###### Note

To log Insights events for `ApiCallRateInsight`, the trail must log `write` management events.
To log Insights events for `ApiErrorRateInsight`, the trail must log `read` or `write` management events.

### Example trail that logs Insights events

The following example uses **put-insight-selectors** to create
an Insights event selector for a trail named
`TrailName3`. This enables Insights event
collection for the `TrailName3` trail. The Insights
event selector logs both `ApiErrorRateInsight` and
`ApiCallRateInsight` Insights event types.

```
aws cloudtrail put-insight-selectors --trail-name `TrailName3` --insight-selectors '[{"InsightType": "ApiCallRateInsight"},{"InsightType": "ApiErrorRateInsight"}]'
```

The example returns the Insights event selector that is configured for the
trail.

```
{
   "InsightSelectors":
      [
         {
            "InsightType": "ApiErrorRateInsight"
         },
         {
            "InsightType": "ApiCallRateInsight"
         }
      ],
   "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/`TrailName3`"
}
```

### Example: Turn off collection of Insights events

The following example uses **put-insight-selectors** to remove
the Insights event selector for a trail named
`TrailName3`. Clearing the JSON string of Insights
selectors disables Insights event collection for the
`TrailName3` trail.

```
aws cloudtrail put-insight-selectors --trail-name `TrailName3` --insight-selectors '[]'
```

The example returns the now-empty Insights event selector that is configured
for the trail.

```
{
   "InsightSelectors": [ ],
   "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/`TrailName3`"
}
```

## Configuring advanced event selectors

You can use advanced event selectors to log [management events](logging-management-events-with-cloudtrail.md "logging-management-events-with-cloudtrail.md"),
[data events](logging-data-events-with-cloudtrail.md "logging-data-events-with-cloudtrail.md") for all resource types, and [network activity events](logging-network-events-with-cloudtrail.md "logging-network-events-with-cloudtrail.md").
In contrast, you can use basic event selectors to log management events and data events for the `AWS::DynamoDB::Table`, `AWS::Lambda::Function`,
and `AWS::S3::Object` resource types. You can use either basic event selectors, or advanced event selectors, but not both. If you apply advanced event selectors
to a trail that is using basic event selectors, the basic event selectors are overwritten.

To convert a trail to advanced event selectors, run the **get-event-selectors** command to confirm the
current event selectors, and then configure the advanced event selectors
to match the coverage of the previous event selectors, then add
any additional selectors.

You must either run the `get-event-selectors` command from
the AWS Region where the trail was created (the Home Region), or you must specify
that Region by adding the **--region** parameter.

```
aws cloudtrail get-event-selectors --trail-name `TrailName`
```

###### Note

If the trail is an organization trail, and you are signed in with a member
account in the organization in AWS Organizations, you must provide the full ARN of the
trail, and not just the name.

The following example shows the settings for a trail
that is using advanced event selectors to log management events. By default,
a trail is configured to log all management events and no data events or network activity events.

```
{
    "TrailARN": "arn:aws:cloudtrail:us-east-1:123456789012:trail/management-events-trail",
    "AdvancedEventSelectors": [
        {
            "Name": "Management events selector",
            "FieldSelectors": [
                {
                    "Field": "eventCategory",
                    "Equals": [
                        "Management"
                    ]
                }
            ]

        }
    ]
}
```

To create an advanced event selector, run the `put-event-selectors`
command. When an event occurs in your account, CloudTrail evaluates the configuration for
your trails. If the event matches any advanced event selector for a trail, the trail
processes and logs the event. You can configure up to 500 conditions on a trail,
including all values specified for all advanced event selectors on your trail. For
more information, see [Logging data events](logging-data-events-with-cloudtrail.md "logging-data-events-with-cloudtrail.md") and [Logging network activity
events](logging-network-events-with-cloudtrail.md "logging-network-events-with-cloudtrail.md").

###### Topics

- [Example trail with specific advanced event selectors](#configuring-adv-event-selector-specific "#configuring-adv-event-selector-specific")
- [Example trail that uses custom advanced event selectors to log Amazon S3 on AWS Outposts data events](#configuring-adv-event-selector-outposts "#configuring-adv-event-selector-outposts")
- [Example trail that uses advanced event selectors to exclude AWS Key Management Service events](#configuring-adv-event-selector-exclude "#configuring-adv-event-selector-exclude")
- [Example trail that
  uses advanced event selectors to exclude Amazon RDS Data API management
  events](#configuring-adv-event-selector-exclude-rds "#configuring-adv-event-selector-exclude-rds")

### Example trail with specific advanced event selectors

The following example creates custom advanced event selectors for a trail
named `TrailName` to include read and write management
events (by omitting the `readOnly` selector), `PutObject`
and `DeleteObject` data events for all Amazon S3 bucket/prefix
combinations except for a bucket named `amzn-s3-demo-bucket`, data
events for an AWS Lambda function named `MyLambdaFunction`,
and network activity events for AWS KMS access denied events over a VPC endpoint. Because
these are custom advanced event selectors, each set of selectors has a
descriptive name. Note that a trailing slash is part of the ARN value for S3
buckets.

```
aws cloudtrail put-event-selectors --trail-name `TrailName` --advanced-event-selectors
'[
  {
    "Name": "Log readOnly and writeOnly management events",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Management"] }
    ]
  },
  {
    "Name": "Log PutObject and DeleteObject events for all but one bucket",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::S3::Object"] },
      { "Field": "eventName", "Equals": ["PutObject","DeleteObject"] },
      { "Field": "resources.ARN", "NotStartsWith": ["arn:aws:s3:::`amzn-s3-demo-bucket`/"] }
    ]
  },
  {
    "Name": "Log data plane actions on MyLambdaFunction",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::Lambda::Function"] },
      { "Field": "resources.ARN", "Equals": ["arn:aws:lambda:`us-east-2:``111122223333`:function/`MyLambdaFunction`"] }
    ]
  },
  {
     "Name": "Audit AccessDenied AWS KMS events over a VPC endpoint",
     "FieldSelectors": [
       { "Field": "eventCategory", "Equals": ["NetworkActivity"]},
       { "Field": "eventSource", "Equals": ["kms.amazonaws.com"]},
       { "Field": "errorCode", "Equals": ["VpceAccessDenied"]}
     ]
  }
]'
```

The example returns the advanced event selectors that are configured for the
trail.

```
{
  "AdvancedEventSelectors": [
    {
      "Name": "Log readOnly and writeOnly management events",
      "FieldSelectors": [
        {
          "Field": "eventCategory",
          "Equals": [ "Management" ]
        }
      ]
    },
    {
      "Name": "Log PutObject and DeleteObject events for all but one bucket",
      "FieldSelectors": [
        {
          "Field": "eventCategory",
          "Equals": [ "Data" ]
        },
        {
          "Field": "resources.type",
          "Equals": [ "AWS::S3::Object" ]
        },
        {
          "Field": "resources.ARN",
          "NotStartsWith": [ "arn:aws:s3:::amzn-s3-demo-bucket/" ]
        },
      ]
    },
    {
      "Name": "Log data plane actions on MyLambdaFunction",
      "FieldSelectors": [
        {
          "Field": "eventCategory",
          "Equals": [ "Data" ]
        },
        {
          "Field": "resources.type",
          "Equals": [ "AWS::Lambda::Function" ]
        },
        {
          "Field": "eventName",
          "Equals": [ "Invoke" ]
        },
        {
          "Field": "resources.ARN",
          "Equals": [ "arn:aws:lambda:us-east-2:123456789012:function/MyLambdaFunction" ]
        }
      ]
    },
    {
       "Name": "Audit AccessDenied AWS KMS events over a VPC endpoint",
       "FieldSelectors": [
         {
           "Field": "eventCategory",
           "Equals": ["NetworkActivity"]
         },
         {
           "Field": "eventSource",
           "Equals": ["kms.amazonaws.com"]
         },
         {
           "Field": "errorCode",
           "Equals": ["VpceAccessDenied"]
         }
       ]
     }
  ],
  "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/`TrailName`"
}
```

### Example trail that uses custom advanced event selectors to log Amazon S3 on AWS Outposts data events

The following example shows how to configure your trail to include all data events
for all Amazon S3 on AWS Outposts objects in your outpost. In this release, the supported value
for S3 on AWS Outposts events for the `resources.type` field is
`AWS::S3Outposts::Object`.

```
aws cloudtrail put-event-selectors --trail-name `TrailName` --region `region` \
--advanced-event-selectors \
'[
    {
            "Name": "OutpostsEventSelector",
            "FieldSelectors": [
                { "Field": "eventCategory", "Equals": ["Data"] },
                { "Field": "resources.type", "Equals": ["AWS::S3Outposts::Object"] }
            ]
        }
]'

```

The command returns the following example output.

```
{
    "AdvancedEventSelectors": [
        {
            "Name": "OutpostsEventSelector",
            "FieldSelectors": [
                {
                    "Field": "eventCategory",
                    "Equals": [
                        "Data"
                    ]
                },
                {
                    "Field": "resources.type",
                    "Equals": [
                        "AWS::S3Outposts::Object"
                    ]
                }
            ]
        }
    ],
  "TrailARN": "arn:aws:cloudtrail:`region`:123456789012:trail/`TrailName`"
}
```

### Example trail that uses advanced event selectors to exclude AWS Key Management Service events

The following example creates an advanced event selector for a trail named
`TrailName` to include read-only and write-only
management events (by omitting the `readOnly` selector), but to
exclude AWS Key Management Service (AWS KMS) events. Because AWS KMS events are treated as management
events, and there can be a high volume of them, they can have a substantial
impact on your CloudTrail bill if you have more than one trail that captures
management events.

If you choose not to log management events, AWS KMS events are not logged, and
you cannot change AWS KMS event logging settings.

To start logging AWS KMS events to a trail again, remove the
`eventSource` selector, and run the command again.

```
aws cloudtrail put-event-selectors --trail-name `TrailName` \
--advanced-event-selectors '
[
  {
    "Name": "Log all management events except KMS events",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Management"] },
      { "Field": "eventSource", "NotEquals": ["kms.amazonaws.com"] }
    ]
  }
]'
```

The example returns the advanced event selectors that are configured for the
trail.

```
{
  "AdvancedEventSelectors": [
    {
      "Name": "Log all management events except KMS events",
      "FieldSelectors": [
        {
          "Field": "eventCategory",
          "Equals": [ "Management" ]
        },
        {
          "Field": "eventSource",
          "NotEquals": [ "kms.amazonaws.com" ]
        }
      ]
    }
  ],
  "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/`TrailName`"
}
```

To start logging excluded events to a trail again, remove the
`eventSource` selector, as shown in the following command.

```
aws cloudtrail put-event-selectors --trail-name `TrailName` \
--advanced-event-selectors '
[
  {
    "Name": "Log all management events",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Management"] }
    ]
  }
]'
```

### Example trail that

uses advanced event selectors to exclude Amazon RDS Data API management
events

The following example creates an advanced event selector for a trail named
`TrailName` to include read-only and write-only
management events (by omitting the `readOnly` selector), but to
exclude Amazon RDS Data API management events. To exclude Amazon RDS Data API management
events, specify the Amazon RDS Data API event source in the string value for the
`eventSource` field: `rdsdata.amazonaws.com`.

If you choose not to log management events, Amazon RDS Data API management events
are not logged, and you cannot change Amazon RDS Data API event logging
settings.

To start logging Amazon RDS Data API management events to a trail again, remove the
`eventSource` selector, and run the command again.

```
aws cloudtrail put-event-selectors --trail-name `TrailName` \
--advanced-event-selectors '
[
  {
    "Name": "Log all management events except Amazon RDS Data API management events",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Management"] },
      { "Field": "eventSource", "NotEquals": ["rdsdata.amazonaws.com"] }
    ]
  }
]'
```

The example returns the advanced event selectors that are configured for the
trail.

```
{
  "AdvancedEventSelectors": [
    {
      "Name": "Log all management events except Amazon RDS Data API management events",
      "FieldSelectors": [
        {
          "Field": "eventCategory",
          "Equals": [ "Management" ]
        },
        {
          "Field": "eventSource",
          "NotEquals": [ "rdsdata.amazonaws.com" ]
        }
      ]
    }
  ],
  "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/`TrailName`"
}
```

To start logging excluded events to a trail again, remove the
`eventSource` selector, as shown in the following command.

```
aws cloudtrail put-event-selectors --trail-name `TrailName` \
--advanced-event-selectors '
[
  {
    "Name": "Log all management events",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Management"] }
    ]
  }
]'
```

## Configuring basic event selectors

You can only use basic event selectors to log management events and data events
for the `AWS::DynamoDB::Table`, `AWS::Lambda::Function`, and
`AWS::S3::Object` resource types. You can log management events, all data resource types,
and network activity events by using advanced event selectors.

You can use either basic event selectors, or advanced event selectors, but not both. If you apply basic event selectors
to a trail that is using advanced event selectors, the advanced event selectors are overwritten.

To view the event selector settings for a trail, run the
`get-event-selectors` command. You must either run this command from
the AWS Region where it was created (the Home Region), or you must specify that
Region by using the **--region** parameter.

```
aws cloudtrail get-event-selectors --trail-name `TrailName`
```

###### Note

If the trail is an organization trail and you are a member account in the
organization in AWS Organizations, you must provide the full ARN of that trail, and not
just the name.

The following example shows the settings for a trail that is using basic event selectors to log management events.

```
{
    "EventSelectors": [
        {
            "ExcludeManagementEventSources": [],
            "IncludeManagementEvents": true,
            "DataResources": [],
            "ReadWriteType": "All"
        }
    ],
    "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/TrailName"
}
```

To create an event selector, run the
`put-event-selectors` command. If you want to log Insights events on the trail, be sure the event selector
enables logging of the Insights types you want configured your trail. For more information about logging Insights events, see [Working with CloudTrail Insights](logging-insights-events-with-cloudtrail.md "logging-insights-events-with-cloudtrail.md").

When an event occurs in your account,
CloudTrail evaluates the configuration for your trails. If the event matches any event
selector for a trail, the trail processes and logs the event. You can configure up
to 5 event selectors for a trail and up to 250 data resources for a trail. For more
information, see [Logging data events](logging-data-events-with-cloudtrail.md "logging-data-events-with-cloudtrail.md").

###### Topics

- [Example trail with specific event selectors](#configuring-event-selector-example1 "#configuring-event-selector-example1")
- [Example trail that logs all management and data events](#configuring-event-selector-example2 "#configuring-event-selector-example2")
- [Example trail that does not log AWS Key Management Service events](#configuring-event-selector-example-kms "#configuring-event-selector-example-kms")
- [Example trail that logs relevant low-volume AWS Key Management Service events](#configuring-event-selector-log-kms "#configuring-event-selector-log-kms")
- [Example trail that does not log Amazon RDS data API events](#configuring-event-selector-example-rds "#configuring-event-selector-example-rds")

### Example trail with specific event selectors

The following example creates an event selector for a trail named
`TrailName` to include read-only and write-only
management events, data events for two Amazon S3 bucket/prefix combinations, and data
events for a single AWS Lambda function named
`hello-world-python-function`.

```
aws cloudtrail put-event-selectors --trail-name `TrailName` --event-selectors '[{"ReadWriteType": "All","IncludeManagementEvents": true,"DataResources": [{"Type":"AWS::S3::Object", "Values": ["arn:aws:s3:::amzn-s3-demo-bucket/prefix","arn:aws:s3:::amzn-s3-demo-bucket2/prefix2"]},{"Type": "AWS::Lambda::Function","Values": ["arn:aws:lambda:us-west-2:999999999999:function:`hello-world-python-function`"]}]}]'
```

The example returns the event selector configured for the trail.

```
{
    "EventSelectors": [
        {
            "ExcludeManagementEventSources": [],
            "IncludeManagementEvents": true,
            "DataResources": [
                {
                    "Values": [
                        "arn:aws:s3:::amzn-s3-demo-bucket/prefix",
                        "arn:aws:s3:::amzn-s3-demo-bucket2/prefix2"
                    ],
                    "Type": "AWS::S3::Object"
                },
                {
                    "Values": [
                        "arn:aws:lambda:us-west-2:123456789012:function:hello-world-python-function"
                    ],
                    "Type": "AWS::Lambda::Function"
                },
            ],
            "ReadWriteType": "All"
        }
    ],
    "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/`TrailName`"
}
```

### Example trail that logs all management and data events

The following example creates an event selector for a trail named
`TrailName2` that includes all management events, including
read-only and write-only management events, and data events for all Amazon S3
buckets, AWS Lambda functions, and Amazon DynamoDB tables in the AWS account. Because
this example uses basic event selectors, it cannot configure logging for S3
events on AWS Outposts, Amazon Managed Blockchain JSON-RPC calls on Ethereum nodes, or other advanced event selector resource types.
You also can't log network activity events using basic event selectors. You must use
advanced event selectors to log network activity events and data events for all other resource types. For more
information, see [Configuring advanced event selectors](#configuring-adv-event-selector-examples "#configuring-adv-event-selector-examples").

###### Note

If the trail applies only to one Region, only events in that Region are
logged, even though the event selector parameters specify all Amazon S3 buckets
and Lambda functions. Event selectors apply only to the Regions where the
trail is created.

```
aws cloudtrail put-event-selectors --trail-name `TrailName2` --event-selectors '[{"ReadWriteType": "All","IncludeManagementEvents": true,"DataResources": [{"Type":"AWS::S3::Object", "Values": ["arn:aws:s3:::"]},{"Type": "AWS::Lambda::Function","Values": ["arn:aws:lambda"]},{"Type": "AWS::DynamoDB::Table","Values": ["arn:aws:dynamodb"]}]}]'
```

The example returns the event selectors configured for the trail.

```
{
    "EventSelectors": [
        {
            "ExcludeManagementEventSources": [],
            "IncludeManagementEvents": true,
            "DataResources": [
                {
                    "Values": [
                        "arn:aws:s3:::"
                    ],
                    "Type": "AWS::S3::Object"
                },
                {
                    "Values": [
                        "arn:aws:lambda"
                    ],
                    "Type": "AWS::Lambda::Function"
                },
{
                    "Values": [
                        "arn:aws:dynamodb"
                    ],
                    "Type": "AWS::DynamoDB::Table"
                }
            ],
            "ReadWriteType": "All"
        }
    ],
    "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/`TrailName2`"
}
```

### Example trail that does not log AWS Key Management Service events

The following example creates an event selector for a trail named
`TrailName` to include read-only and write-only
management events, but to exclude AWS Key Management Service (AWS KMS) events. Because AWS KMS events
are treated as management events, and there can be a high volume of them, they
can have a substantial impact on your CloudTrail bill if you have more than one trail
that captures management events. The user in this example has chosen to exclude
AWS KMS events from every trail except for one. To exclude an event source, add
`ExcludeManagementEventSources` to your event selectors, and
specify an event source in the string value.

If you choose not to log management events, AWS KMS events are not logged, and
you cannot change AWS KMS event logging settings.

To start logging AWS KMS events to a trail again, pass an empty array as the
value of `ExcludeManagementEventSources`.

```
aws cloudtrail put-event-selectors --trail-name `TrailName` --event-selectors '[{"ReadWriteType": "All","ExcludeManagementEventSources": ["kms.amazonaws.com"],"IncludeManagementEvents": true]}]'
```

The example returns the event selector that is configured for the
trail.

```
{
    "EventSelectors": [
        {
            "ExcludeManagementEventSources": [ "kms.amazonaws.com" ],
            "IncludeManagementEvents": true,
            "DataResources": [],
            "ReadWriteType": "All"
        }
    ],
    "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/`TrailName`"
}
```

To start logging AWS KMS events to a trail again, pass an empty array as the
value of `ExcludeManagementEventSources`, as shown in the following
command.

```
aws cloudtrail put-event-selectors --trail-name `TrailName` --event-selectors '[{"ReadWriteType": "All","ExcludeManagementEventSources": [],"IncludeManagementEvents": true]}]'
```

### Example trail that logs relevant low-volume AWS Key Management Service events

The following example creates an event selector for a trail named
`TrailName` to include write-only management events
and AWS KMS events. Because AWS KMS events are treated as management events, and
there can be a high volume of them, they can have a substantial impact on your
CloudTrail bill if you have more than one trail that captures management events. The
user in this example has chosen to include AWS KMS **Write**
events, which will include `Disable`, `Delete` and
`ScheduleKey`, but no longer include high-volume actions such as
`Encrypt`, `Decrypt`, and `GenerateDataKey`
(these are now treated as **Read** events).

```
aws cloudtrail put-event-selectors --trail-name `TrailName` --event-selectors '[{"ReadWriteType": "WriteOnly","ExcludeManagementEventSources": [],"IncludeManagementEvents": true]}]'
```

The example returns the event selector that is configured for the trail. This
logs write-only management events, including AWS KMS events.

```
{
    "EventSelectors": [
        {
            "ExcludeManagementEventSources": [],
            "IncludeManagementEvents": true,
            "DataResources": [],
            "ReadWriteType": "WriteOnly"
        }
    ],
    "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/`TrailName`"
}
```

### Example trail that does not log Amazon RDS data API events

The following example creates an event selector for a trail named
`TrailName` to include read-only and write-only
management events, but to exclude Amazon RDS Data API events. Because Amazon RDS Data API
events are treated as management events, and there can be a high volume of them,
they can have a substantial impact on your CloudTrail bill if you have more than one
trail that captures management events. The user in this example has chosen to
exclude Amazon RDS Data API events from every trail except for one. To exclude an
event source, add `ExcludeManagementEventSources` to your event
selectors, and specify the Amazon RDS Data API event source in the string value:
`rdsdata.amazonaws.com`.

If you choose not to log management events, Amazon RDS Data API events are not
logged, and you cannot change event logging settings.

To start logging Amazon RDS Data API management events to a trail again, pass an empty array
as the value of `ExcludeManagementEventSources`.

```
aws cloudtrail put-event-selectors --trail-name `TrailName` --event-selectors '[{"ReadWriteType": "All","ExcludeManagementEventSources": ["rdsdata.amazonaws.com"],"IncludeManagementEvents": true]}]'
```

The example returns the event selector that is configured for the
trail.

```
{
    "EventSelectors": [
        {
            "ExcludeManagementEventSources": [ "rdsdata.amazonaws.com" ],
            "IncludeManagementEvents": true,
            "DataResources": [],
            "ReadWriteType": "All"
        }
    ],
    "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/`TrailName`"
}
```

To start logging Amazon RDS Data API management events to a trail again, pass an empty array
as the value of `ExcludeManagementEventSources`, as shown in the
following command.

```
aws cloudtrail put-event-selectors --trail-name `TrailName` --event-selectors '[{"ReadWriteType": "All","ExcludeManagementEventSources": [],"IncludeManagementEvents": true]}]'
```

## Stopping and starting logging for a trail

The following commands start and stop CloudTrail logging.

```
aws cloudtrail start-logging --name `awscloudtrail-example`
```

```
aws cloudtrail stop-logging --name `awscloudtrail-example`
```

###### Note

Before deleting a bucket, run the `stop-logging` command to stop
delivering events to the bucket. If you don’t stop logging, CloudTrail attempts to
deliver log files to a bucket with the same name for a limited period of
time.

If you stop logging or delete a trail, CloudTrail Insights is disabled on that
trail.

## Deleting a trail

If you've enabled CloudTrail management events in Amazon Security Lake, you are required to maintain at least one
organizational trail that is multi-Region and logs both `read` and
`write` management events. You cannot delete a trail if it is the only trail
you have that meets this requirement, unless you turn off CloudTrail management events in Security Lake.

You can delete a trail with the following command. You can delete a trail only in
the Region it was created (the Home Region).

###### Important

While deleting a CloudTrail trail is an irreversible action, CloudTrail does not
delete log files in the Amazon S3 bucket for that trail, the Amazon S3 bucket itself, or the
CloudWatch log group to which the trail delivers events. Deleting a multi-Region trail
will stop logging of events in all AWS Regions enabled in your AWS account. Deleting a
single-Region trail will stop logging of events in that Region only. It will not stop
logging of events in other Regions even if the trails in those other Regions have
identical names to the deleted trail.

For information about account closure and deletion of CloudTrail trails, see [AWS account closure and trails](cloudtrail-account-closure.md "cloudtrail-account-closure.md").

```
aws cloudtrail delete-trail --name `awscloudtrail-example`
```

When you delete a trail, you do not delete the Amazon S3 bucket or the Amazon SNS topic
associated with it. Use the AWS Management Console, AWS CLI, or service API to delete these
resources separately.
