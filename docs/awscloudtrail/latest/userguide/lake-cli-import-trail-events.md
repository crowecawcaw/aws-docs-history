# Import trail events to an event data store with the AWS CLI

This section shows how to create and configure an event data store by running the
[create-event-data-store](../../../cli/latest/reference/cloudtrail/create-event-data-store.md "../../../cli/latest/reference/cloudtrail/create-event-data-store.md") command and then how to import the events to
that event data store by using the [start-import](../../../cli/latest/reference/cloudtrail/start-import.md "../../../cli/latest/reference/cloudtrail/start-import.md") command. For more information
about importing trail events, see [Copy trail events to an event data store](cloudtrail-copy-trail-to-lake-eds.md "cloudtrail-copy-trail-to-lake-eds.md").

## Preparing to import trail events

Before you import trail events, make the following preparations.

- Be sure you have a role with the [required permissions](cloudtrail-copy-trail-to-lake-eds.md#copy-trail-events-permissions-iam "cloudtrail-copy-trail-to-lake-eds.md#copy-trail-events-permissions-iam")
  to import trail events to an event data store.
- Determine the [--billing-mode](cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") value
  you want to specify for the event data store. The `--billing-mode` determines
  the cost of ingesting and storing events, and the default and maximum retention period for the event data store.

When you import trail events to CloudTrail Lake, CloudTrail unzips the logs that are stored in
gzip (compressed) format. Then CloudTrail copies the events contained in the
logs to your event data store. The size of the uncompressed data could
be greater than the actual Amazon S3 storage size. To get a general estimate
of the size of the uncompressed data, multiply the size of the logs in
the S3 bucket by 10. You can use this estimate to choose the
`--billing-mode` value for your use case.

- Determine the value you want to specify for the `--retention-period`.
  CloudTrail will not copy an event if its `eventTime` is older than
  the specified retention period.

To determine the appropriate
retention period, take the sum of the oldest event you want to copy in days and the number of days you
want to retain the events in the event data store as demonstrated
in this equation:

**Retention period** =
`oldest-event-in-days` +
`number-days-to-retain`

For example, if the oldest event you're copying is 45 days old
and you want to keep the events in the event data store for a
further 45 days, you would set the retention period to 90
days.

- Decide whether you want to use the event data store to analyze any
  future events. If you don't want to ingest any future events, include the
  `--no-start-ingestion` parameter when you create the event data store.
  By default, event data store's begin ingesting events when they're
  created.

## To create an event data store

and import trail events to that event data store

1. Run the **create-event-data-store** command to create the new event data store. In this example,
   the `--retention-period` is set to `120` because the oldest event being copied is 90 days old and we want to retain the events for 30 days.
   The `--no-start-ingestion` parameter is set because we don't want to ingest any future events. In this example, `--billing-mode` wasn't set, because we are
   using the default value `EXTENDABLE_RETENTION_PRICING` as we expect to ingest less than 25 TB of event data.

###### Note

If you're creating the event data store to replace your trail, we recommend configuring the `--advanced-event-selectors` to match
the event selectors of your trail to ensure you have the same event coverage. By default, event data stores log all management events.

```
aws cloudtrail create-event-data-store  --name import-trail-eds  --retention-period 120 --no-start-ingestion
```

The following is the example response:

```
{
    "EventDataStoreArn": "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLEa-4357-45cd-bce5-17ec652719d9",
    "Name": "import-trail-eds",
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
    "RetentionPeriod": 120,
    "TerminationProtectionEnabled": true,
    "CreatedTimestamp": "2023-11-09T16:52:25.444000+00:00",
    "UpdatedTimestamp": "2023-11-09T16:52:25.569000+00:00"
}
```

The initial `Status` is `CREATED` so we'll run the **get-event-data-store** command to verify ingestion is stopped.

```
aws cloudtrail get-event-data-store --event-data-store `eds-id`
```

The response shows the `Status` is now `STOPPED_INGESTION`, which indicates the event data store is not ingesting live events.

```
{
    "EventDataStoreArn": "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLEa-4357-45cd-bce5-17ec652719d9",
    "Name": "import-trail-eds",
    "Status": **"STOPPED\_INGESTION"**,
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
    "RetentionPeriod": 120,
    "TerminationProtectionEnabled": true,
    "CreatedTimestamp": "2023-11-09T16:52:25.444000+00:00",
    "UpdatedTimestamp": "2023-11-09T16:52:25.569000+00:00"
}
```

2. Run the **start-import** command to import the trail
   events to the event data store created in step 1. Specify the ARN (or ID
   suffix of the ARN) of the event data store as the value for the
   `--destinations` parameter. For
   `--start-event-time` specify the `eventTime` for
   the oldest event you want to copy and for `--end-event-time`
   specify the `eventTime` of the newest event you want to copy. For
   `--import-source` specify the S3 URI for the S3 bucket
   containing your trail logs, the AWS Region for the S3 bucket, and the ARN
   of the role used for importing trail events.

```
aws cloudtrail start-import \
--destinations ["arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLEa-4357-45cd-bce5-17ec652719d9"] \
--start-event-time 2023-08-11T16:08:12.934000+00:00 \
--end-event-time 2023-11-09T17:08:20.705000+00:00 \
--import-source {"S3": {"S3LocationUri": "s3://aws-cloudtrail-logs-123456789012-612ff1f6/AWSLogs/123456789012/CloudTrail/","S3BucketRegion":"us-east-1","S3BucketAccessRoleArn": "arn:aws:iam::123456789012:role/service-role/CloudTrailLake-us-east-1-copy-events-eds"}}

```

The following is an example response.

```
{
   "CreatedTimestamp": "2023-11-09T17:08:20.705000+00:00",
   "Destinations": [
        "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLEa-4357-45cd-bce5-17ec652719d9"
    ],
   "EndEventTime": "2023-11-09T17:08:20.705000+00:00",
   "ImportId": "EXAMPLEe-7be2-4658-9204-b38c3257fcd1",
   "ImportSource": {
      "S3": {
         "S3BucketAccessRoleArn": "arn:aws:iam::123456789012:role/service-role/CloudTrailLake-us-east-1-copy-events-eds",
         "S3BucketRegion":"us-east-1",
         "S3LocationUri": "s3://aws-cloudtrail-logs-123456789012-111ff1f6/AWSLogs/123456789012/CloudTrail/"
      }
   },
   "ImportStatus": "INITIALIZING",
   "StartEventTime": "2023-08-11T16:08:12.934000+00:00",
   "UpdatedTimestamp": "2023-11-09T17:08:20.806000+00:00"
}
```

3. Run the [get-import](../../../cli/latest/reference/cloudtrail/get-import.md "../../../cli/latest/reference/cloudtrail/get-import.md")
   command to get information about the import.

```
aws cloudtrail get-import --import-id `import-id`
```

The following is an example response.

```
{
    "ImportId": "EXAMPLEe-7be2-4658-9204-b38c3EXAMPLE",
    "Destinations": [
        "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLEa-4357-45cd-bce5-17ec652719d9"
    ],
    "ImportSource": {
        "S3": {
            "S3LocationUri": "s3://aws-cloudtrail-logs-123456789012-111ff1f6/AWSLogs/123456789012/CloudTrail/",
            "S3BucketRegion":"us-east-1",
            "S3BucketAccessRoleArn": "arn:aws:iam::123456789012:role/service-role/CloudTrailLake-us-east-1-copy-events-eds"
        }
    },
    "StartEventTime": "2023-08-11T16:08:12.934000+00:00",
    "EndEventTime": "2023-11-09T17:08:20.705000+00:00",
    "ImportStatus": "COMPLETED",
    "CreatedTimestamp": "2023-11-09T17:08:20.705000+00:00",
    "ImportStatistics": {
        "PrefixesFound": 1548,
        "PrefixesCompleted": 1548,
        "FilesCompleted": 92845,
        "EventsCompleted": 577249,
        "FailedEntries": 0
    }
}
```

An import finishes with an `ImportStatus` of `COMPLETED`
if there were no failures, or `FAILED` if there were failures.

If the import had `FailedEntries`, you can run the
[list-import-failures](../../../cli/latest/reference/cloudtrail/list-import-failures.md "../../../cli/latest/reference/cloudtrail/list-import-failures.md")
command to return a list of failures.

```
aws cloudtrail list-import-failures --import-id `import-id`
```

To retry an import that had failures, run the **start-import** command with only the `--import-id` parameter. When you retry an import,
CloudTrail resumes the import at the location where the failure occurred.

```
aws cloudtrail start-import --import-id `import-id`
```
