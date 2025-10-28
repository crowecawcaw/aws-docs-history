# Create an event data store with the AWS CLI

This section describes how to use the [`create-event-data-store`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-event-data-store.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-event-data-store.html")
command to create an event data store and provides examples of different types of event data stores that you can create.

When you create an event data store, the only required parameter is `--name`, which is used to identify the event data store. You can configure additional optional parameters, including:

- `--advanced-event-selectors` - Specifies the type of events to include in the event data store.
  By default, event data stores log all management events. For more information about advanced event selectors,
  see [AdvancedEventSelector](../APIReference/API_AdvancedEventSelector.md "../APIReference/API_AdvancedEventSelector.md") in the CloudTrail API
  Reference.
- `--kms-key-id` - Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by `alias/`,
  a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
- `--multi-region-enabled` - Creates a multi-Region event data store that logs events for all AWS Regions in your account. By default, `--multi-region-enabled` is
  set, even if the parameter is not added.
- `--organization-enabled` - Enables an event data store to collect events for all accounts in an organization. By default, the event data store is not enabled for all accounts
  in an organization.
- `--billing-mode` - Determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store.

The following are the possible values:

    + `EXTENDABLE_RETENTION_PRICING` - This billing mode is generally recommended if you ingest less than 25 TB of event data a month
     and want a flexible retention period of up to 3653 days (about 10 years).
     The default retention period for this billing mode is 366 days.
    + `FIXED_RETENTION_PRICING` - This billing mode is recommended if you expect to ingest more than 25 TB of event data per month and need a retention period of up to 2557 days (about 7 years).
     The default retention period for this billing mode is 2557 days.

The default value is `EXTENDABLE_RETENTION_PRICING`.

- `--retention-period` - The number of days to keep events in the event data store. Valid values are integers between 7 and 3653 if the
  `--billing-mode` is `EXTENDABLE_RETENTION_PRICING`, or between 7 and 2557 if the `--billing-mode`
  is set to `FIXED_RETENTION_PRICING`. If you do not specify `--retention-period`, CloudTrail uses the default
  retention period for the `--billing-mode`.
- `--start-ingestion` - The `--start-ingestion` parameter starts event ingestion
  on the event data store when it's created. This parameter is set even if the parameter is not added.

Specify the `--no-start-ingestion` if you do not want the event data store to ingest live events. For example,
you may want to set this parameter if you are copying events to the event data store and only plan to use the event data to analyze past events. The `--no-start-ingestion` parameter is only valid if the
`eventCategory` is `Management`, `Data`, or `ConfigurationItem`.
The following examples show how to create different types of event data stores.

###### Examples:

- [Create an event data store for S3 data events with the AWS CLI](#lake-cli-create-eds-data "#lake-cli-create-eds-data")
- [Create an event data store for KMS network activity events with the AWS CLI](#lake-cli-create-eds-network "#lake-cli-create-eds-network")
- [Create an event data store for AWS Config
  configuration items with the AWS CLI](#lake-cli-create-eds-config "#lake-cli-create-eds-config")
- [Create an organization event data store for management events with the AWS CLI](#lake-cli-create-eds-org "#lake-cli-create-eds-org")
- [Create event data stores for Insights events with the AWS CLI](#lake-cli-insights "#lake-cli-insights")

## Create an event data store for S3 data events with the AWS CLI

The following example AWS Command Line Interface (AWS CLI) **create-event-data-store** command creates an event data store named
`my-event-data-store` that selects all Amazon S3 data events and is encrypted using a KMS key.

```
aws cloudtrail create-event-data-store \
--name my-event-data-store \
--kms-key-id "arn:aws:kms:us-east-1:123456789012:alias/`KMS_key_alias`" \
--advanced-event-selectors '[
        {
            "Name": "Select all S3 data events",
            "FieldSelectors": [
                { "Field": "eventCategory", "Equals": ["Data"] },
                { "Field": "resources.type", "Equals": ["AWS::S3::Object"] },
                { "Field": "resources.ARN", "StartsWith": ["arn:aws:s3"] }
            ]
        }
    ]'

```

The following is an example response.

```
{
    "EventDataStoreArn": "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-ee54-4813-92d5-999aeEXAMPLE",
    "Name": "my-event-data-store",
    "Status": "CREATED",
    "AdvancedEventSelectors": [
        {
            "Name": "Select all S3 data events",
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
                        "AWS::S3::Object"
                    ]
                },
                {
                    "Field": "resources.ARN",
                    "StartsWith": [
                        "arn:aws:s3"
                    ]
                }
            ]
        }
    ],
    "MultiRegionEnabled": true,
    "OrganizationEnabled": false,
    "BillingMode": "EXTENDABLE_RETENTION_PRICING",
    "RetentionPeriod": 366,
    "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:alias/`KMS_key_alias`",
    "TerminationProtectionEnabled": true,
    "CreatedTimestamp": "2023-11-09T22:19:39.417000-05:00",
    "UpdatedTimestamp": "2023-11-09T22:19:39.603000-05:00"
}
```

## Create an event data store for KMS network activity events with the AWS CLI

The following example shows how to create an event data store to include
`VpceAccessDenied` network activity events for AWS KMS. This example
sets the `errorCode` field equal to `VpceAccessDenied` events
and the `eventSource` field equal to
`kms.amazonaws.com`.

```
aws cloudtrail create-event-data-store \
--name `EventDataStoreName` \
--advanced-event-selectors '[
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
]'
```

The command returns the following example output.

```
{
    "EventDataStoreArn": "arn:aws:cloudtrail:us-east-1:111122223333:eventdatastore/EXAMPLEb4a8-99b1-4ec2-9258-EXAMPLEc890",
    "Name": "EventDataStoreName",
    "Status": "CREATED",
    "AdvancedEventSelectors": [
        {
            "Name": "Audit AccessDenied AWS KMS events over a VPC endpoint",
            "FieldSelectors": [
                {
                    "Field": "eventCategory",
                    "Equals": [
                        "NetworkActivity"
                    ]
                },
                {
                    "Field": "eventSource",
                    "Equals": [
                        "kms.amazonaws.com"
                    ]
                },
                {
                    "Field": "errorCode",
                    "Equals": [
                        "VpceAccessDenied"
                    ]
                }
            ]
        }
    ],
    "MultiRegionEnabled": true,
    "OrganizationEnabled": false,
    "RetentionPeriod": 366,
    "TerminationProtectionEnabled": true,
    "CreatedTimestamp": "2024-05-20T21:00:17.673000+00:00",
    "UpdatedTimestamp": "2024-05-20T21:00:17.820000+00:00"
}
```

For more information about network activity events, see
[Logging network activity
events](logging-network-events-with-cloudtrail.md "logging-network-events-with-cloudtrail.md").

## Create an event data store for AWS Config

configuration items with the AWS CLI

The following example AWS CLI **create-event-data-store** command creates an event data store named
`config-items-eds` that selects AWS Config configuration items. To collect configuration items, specify that the
`eventCategory` field Equals `ConfigurationItem` in the advanced event selectors.

```
aws cloudtrail create-event-data-store \
--name config-items-eds \
--advanced-event-selectors '[
    {
        "Name": "Select AWS Config configuration items",
        "FieldSelectors": [
            { "Field": "eventCategory", "Equals": ["ConfigurationItem"] }
        ]
    }
]'
```

The following is an example response.

```
{
    "EventDataStoreArn": "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-ee54-4813-92d5-999aeEXAMPLE",
    "Name": "config-items-eds",
    "Status": "CREATED",
    "AdvancedEventSelectors": [
        {
            "Name": "Select AWS Config configuration items",
            "FieldSelectors": [
                {
                    "Field": "eventCategory",
                    "Equals": [
                        "ConfigurationItem"
                    ]
                }
            ]
        }
    ],
    "MultiRegionEnabled": true,
    "OrganizationEnabled": false,
    "BillingMode": "EXTENDABLE_RETENTION_PRICING",
    "RetentionPeriod": 366,
    "TerminationProtectionEnabled": true,
    "CreatedTimestamp": "2023-11-07T19:03:24.277000+00:00",
    "UpdatedTimestamp": "2023-11-07T19:03:24.468000+00:00"
}
```

## Create an organization event data store for management events with the AWS CLI

The following example AWS CLI **create-event-data-store** command creates an organization event data store that collects all management events and sets
the `--billing-mode` parameter to `FIXED_RETENTION_PRICING`.

```
aws cloudtrail create-event-data-store --name org-management-eds --organization-enabled --billing-mode FIXED_RETENTION_PRICING
```

The following is an example response.

```
{
    "EventDataStoreArn": "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE6-d493-4914-9182-e52a7934b207",
    "Name": "org-management-eds",
    "Status": "CREATED",
    "AdvancedEventSelectors": [
        {
            "Name": "Default management events",
            "FieldSelectors": [
                {
                    "Field": "eventCategory",
                    "Equals": [
                        "Management"
                    ]
                }
            ]
        }
    ],
    "MultiRegionEnabled": true,
    "OrganizationEnabled": true,
    "BillingMode": "FIXED_RETENTION_PRICING",
    "RetentionPeriod": 2557,
    "TerminationProtectionEnabled": true,
    "CreatedTimestamp": "2023-11-16T15:30:50.689000+00:00",
    "UpdatedTimestamp": "2023-11-16T15:30:50.851000+00:00"
}
```

## Create event data stores for Insights events with the AWS CLI

To log Insights events in CloudTrail Lake, you need a destination event data store that collects Insights events
and a source event data store that enables Insights and logs management events.

This procedure shows you how to create the destination and source event data stores and then enable Insights events.

1. Run the [**aws cloudtrail create-event-data-store**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-event-data-store.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-event-data-store.html") command to
   create a destination event data store that collects Insights events. The value for `eventCategory` must be `Insight`. Replace `retention-period-days`
   with the number of days you would like to retain events in your event data store. Valid values are integers between 7 and 3653 if the
   `--billing-mode` is `EXTENDABLE_RETENTION_PRICING`, or between 7 and 2557 if the `--billing-mode`
   is set to `FIXED_RETENTION_PRICING`. If you do not specify `--retention-period`, CloudTrail uses the default
   retention period for the `--billing-mode`.

If you are signed in with the management account for an AWS Organizations organization, include the `--organization-enabled` parameter if you want to give your [delegated administrator](cloudtrail-delegated-administrator.md "cloudtrail-delegated-administrator.md") access to the event data store.

```
aws cloudtrail create-event-data-store \
--name insights-event-data-store \
--no-multi-region-enabled \
--retention-period `retention-period-days` \
--advanced-event-selectors '[
    {
      "Name": "Select Insights events",
      "FieldSelectors": [
          { "Field": "eventCategory", "Equals": ["Insight"] }
        ]
    }
  ]'

```

The following is an example response.

```
{
    "Name": "insights-event-data-store",
    "ARN": "arn:aws:cloudtrail:us-east-1:111122223333:eventdatastore/EXAMPLEf852-4e8f-8bd1-bcf6cEXAMPLE",
    "AdvancedEventSelectors": [
        {
           "Name": "Select Insights events",
           "FieldSelectors": [
              {
                  "Field": "eventCategory",
                  "Equals": [
                      "Insight"
                    ]
                }
            ]
        }
    ],
    "MultiRegionEnabled": false,
    "OrganizationEnabled": false,
    "BillingMode": "EXTENDABLE_RETENTION_PRICING",
    "RetentionPeriod": "90",
    "TerminationProtectionEnabled": true,
    "CreatedTimestamp": "2023-05-08T15:22:33.578000+00:00",
    "UpdatedTimestamp": "2023-05-08T15:22:33.714000+00:00"
}
```

You will use the `ARN` (or ID suffix of the ARN) from the response as the value for the `--insights-destination` parameter in step 3. 2. Run the [**aws cloudtrail create-event-data-store**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-event-data-store.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-event-data-store.html") command to create a source event data store that logs management events.
By default, event data stores log all management events. You don't need to specify the advanced event selectors if you want to log all management events. Replace `retention-period-days`
with the number of days you would like to retain events in your event data store. Valid values are integers between 7 and 3653 if the
`--billing-mode` is `EXTENDABLE_RETENTION_PRICING`, or between 7 and 2557 if the `--billing-mode`
is set to `FIXED_RETENTION_PRICING`. If you do not specify `--retention-period`, CloudTrail uses the default
retention period for the `--billing-mode`. If you are creating an organization event data store, include
the `--organization-enabled` parameter.

```
aws cloudtrail create-event-data-store --name source-event-data-store --retention-period `retention-period-days`
```

The following is an example response.

```
{
    "EventDataStoreArn": "arn:aws:cloudtrail:us-east-1:111122223333:eventdatastore/EXAMPLE9952-4ab9-49c0-b788-f4f3EXAMPLE",
    "Name": "source-event-data-store",
    "Status": "CREATED",
    "AdvancedEventSelectors": [
        {
            "Name": "Default management events",
            "FieldSelectors": [
                {
                    "Field": "eventCategory",
                    "Equals": [
                        "Management"
                    ]
                }
            ]
        }
    ],
    "MultiRegionEnabled": true,
    "OrganizationEnabled": false,
    "BillingMode": "EXTENDABLE_RETENTION_PRICING",
    "RetentionPeriod": 90,
    "TerminationProtectionEnabled": true,
    "CreatedTimestamp": "2023-05-08T15:25:35.578000+00:00",
    "UpdatedTimestamp": "2023-05-08T15:25:35.714000+00:00"
}
```

You will use the `ARN` (or ID suffix of the ARN) from the response as the value for the `--event-data-store` parameter in step 3. 3. Run the
[**put-insight-selectors**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/put-insight-selectors.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/put-insight-selectors.html") command to enable Insights events. Insights selector values
can be `ApiCallRateInsight`, `ApiErrorRateInsight`, or both.
For the `--event-data-store` parameter, specify the ARN (or ID suffix of the ARN) of the
source event data store that logs management events and will enable Insights. For
the `--insights-destination` parameter, specify the ARN (or ID suffix of the ARN) of the
destination event data store that will log Insights events.

```
aws cloudtrail put-insight-selectors --event-data-store arn:aws:cloudtrail:us-east-1:111122223333:eventdatastore/EXAMPLE9952-4ab9-49c0-b788-f4f3EXAMPLE --insights-destination arn:aws:cloudtrail:us-east-1:111122223333:eventdatastore/EXAMPLEf852-4e8f-8bd1-bcf6cEXAMPLE --insight-selectors '[{"InsightType": "ApiCallRateInsight"},{"InsightType": "ApiErrorRateInsight"}]'
```

The following result shows the Insights event selector that is configured for the
event data store.

```
{
  "EventDataStoreARN": "arn:aws:cloudtrail:us-east-1:111122223333:eventdatastore/EXAMPLE9952-4ab9-49c0-b788-f4f3EXAMPLE",
  "InsightsDestination": "arn:aws:cloudtrail:us-east-1:111122223333:eventdatastore/EXAMPLEf852-4e8f-8bd1-bcf6cEXAMPLE",
  "InsightSelectors":
      [
         {
            "InsightType": "ApiErrorRateInsight"
         },
         {
            "InsightType": "ApiCallRateInsight"
         }
      ]
}
```

After you enable CloudTrail Insights for the first time on an event data store, CloudTrail may take up to 7 days to begin delivering Insights events,
provided that unusual activity is detected during that time.

CloudTrail Insights
analyzes management events that occur in a single Region, not globally. A CloudTrail Insights event is
generated in the same Region as its supporting management events are generated.

For an organization event data store, CloudTrail analyzes management events from each member's account
instead of analyzing the aggregation of all management events for the organization.

Additional charges apply for
ingesting Insights events in CloudTrail Lake. You will be charged separately if you enable Insights for both trails and event data stores. For information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").
