# Logging Insights events with the AWS CLI

You can configure your trails and event data stores to log Insights events
using the AWS CLI.

###### Note

For Management events Insights: To log Insights events on the API call rate, the trail or event data store must log `write` management events.
To log Insights events on the API error rate, the trail or event data store must log `read` or `write` management.

For Data events Insights: To log Insights events on the API call rate or API error rate, the trail must log `read` or `write` data events.

###### Topics

- [Logging Insights events for a trail using
  the AWS CLI](#insights-events-CLI-enable-trails "#insights-events-CLI-enable-trails")
- [Logging Insights events for an event data
  store using the AWS CLI](#insights-events-CLI-enable-lake "#insights-events-CLI-enable-lake")

## Logging Insights events for a trail using

the AWS CLI

To return the current Insights selectors for a trail, run the
`get-insight-selectors` command.

```
aws cloudtrail get-insight-selectors --trail-name `TrailName`
```

The following example response shows the Insights selectors for a trail named
`insights-trail`.

```
{
    "TrailARN": "arn:aws:cloudtrail:us-east-1:123456789012:trail/insights-trail",
    "InsightSelectors": [
        {
            "InsightType": "ApiCallRateInsight",
            "EventCategories": [
                "Management",
                "Data"
            ]
        },
        {
            "InsightType": "ApiErrorRateInsight",
            "EventCategories": [
                "Management",
                "Data"
            ]
        }
    ]
}
```

If the trail does not have Insights enabled, the
**get-insight-selectors** command returns the following error
message: "An error occurred (InsightNotEnabledException) when calling the
GetInsightSelectors operation: Trail
arn:aws:cloudtrail:us-east-1:123456789012:trail/trailName does not have
Insights enabled. Edit the trail settings to enable Insights, and then try the
operation again."

To configure your trail to log Insights events, run the `put-insight-selectors`
command. The following example shows how to configure your trail to include Insights events.
Insights selector values can be `ApiCallRateInsight`,
`ApiErrorRateInsight`, or both. Each InsightType can be enabled for management EventCategory or data EventCategory or both.

```
aws cloudtrail put-insight-selectors --trail-name `TrailName` --insight-selectors '[{"InsightType": "ApiCallRateInsight", "EventCategories": ["Data"]},{"InsightType": "ApiErrorRateInsight", "EventCategories": ["Data", "Management"]}]'
```

The following result shows the Insights event selector that is configured for the
trail.

```
{
  "TrailARN": "arn:aws:cloudtrail:us-east-1:123456789012:trail/`TrailName`",
  "InsightSelectors":
      [
         {
            "InsightType": "ApiErrorRateInsight",
            "EventCategories": [
                "Data"
            ]
         },
         {
            "InsightType": "ApiCallRateInsight",
            "EventCategories": [
                "Data",
                "Management"
            ]
         }
      ]
 }
```

## Logging Insights events for an event data

store using the AWS CLI

To enable Insights on an event data store, you must have a source event data store
that logs management events and a destination event data store that logs Insights events.

To view whether Insights events are enabled on an event data store, run the
**get-insight-selectors** command.

```
aws cloudtrail get-insight-selectors --event-data-store arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE
```

To view whether an event data store is configured to receive Insights events or management
events, run the **get-event-data-store** command.

```
aws cloudtrail get-event-data-store --event-data-store arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-d483-5c7d-4ac2-adb5dEXAMPLE
```

If an event data store is configured to receive Insights events, its
`eventCategory` will be set to `Insight`.

The following procedure shows you how to create the destination and source event
data stores and then enable Insights events.

1. Run the [**aws cloudtrail create-event-data-store**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-event-data-store.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-event-data-store.html")
   command to create a destination event data store that collects Insights events. The
   value for `eventCategory` must be `Insight`. Replace
   `retention-period-days` with the number of days
   you would like to retain events in your event data store.

If you are signed in with the management account for an AWS Organizations
organization, include the `--organization-enabled` parameter if
you want to give your [delegated administrator](cloudtrail-delegated-administrator.md "cloudtrail-delegated-administrator.md") access to the event data store.

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
    "CreatedTimestamp": "2023-11-08T15:22:33.578000+00:00",
    "UpdatedTimestamp": "2023-11-08T15:22:33.714000+00:00"
}
```

You will use the `ARN` (or ID suffix of the ARN) from the
response as the value for the `--insights-destination` parameter
in step 3. 2. Run the [**aws cloudtrail create-event-data-store**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-event-data-store.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-event-data-store.html")
command to create a source event data store that logs management events. By
default, event data stores log all management events. You don't need to
specify the advanced event selectors if you want to log all management
events. Replace `retention-period-days` with the
number of days you would like to retain events in your event data store. If
you are creating an organization event data store, include the
`--organization-enabled` parameter.

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
    "CreatedTimestamp": "2023-11-08T15:25:35.578000+00:00",
    "UpdatedTimestamp": "2023-11-08T15:25:35.714000+00:00"
}
```

You will use the `ARN` (or ID suffix of the ARN) from the
response as the value for the `--event-data-store` parameter in
step 3. 3. Run the [**put-insight-selectors**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/put-insight-selectors.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/put-insight-selectors.html") command to enable
Insights events. Insights selector values can be `ApiCallRateInsight`,
`ApiErrorRateInsight`, or both. For the
`--event-data-store` parameter, specify the ARN (or ID suffix
of the ARN) of the source event data store that logs management events and
will enable Insights. For the `--insights-destination` parameter,
specify the ARN (or ID suffix of the ARN) of the destination event data
store that will log Insights events.

```
aws cloudtrail put-insight-selectors --event-data-store arn:aws:cloudtrail:us-east-1:111122223333:eventdatastore/EXAMPLE9952-4ab9-49c0-b788-f4f3EXAMPLE --insights-destination arn:aws:cloudtrail:us-east-1:111122223333:eventdatastore/EXAMPLEf852-4e8f-8bd1-bcf6cEXAMPLE --insight-selectors '[{"InsightType": "ApiCallRateInsight"},{"InsightType": "ApiErrorRateInsight"}]'
```

The following result shows the Insights event selector that is configured
for the event data store.

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

After you enable CloudTrail Insights for the first time on an event data store, CloudTrail may take up
to 7 days to begin delivering Insights events, provided that unusual activity is
detected during that time.
