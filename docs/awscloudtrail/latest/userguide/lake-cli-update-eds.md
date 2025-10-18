# Update an event data store with the AWS CLI

This section provides examples that show how to update an event data store's settings by running the AWS CLI `update-event-data-store` command.

###### Examples:

* [Update the billing mode with the AWS CLI](#lake-cli-update-billing-mode "#lake-cli-update-billing-mode")
* [Update the retention mode, enable termination protection, and specify a AWS KMS key with the AWS CLI](#lake-cli-update-retention "#lake-cli-update-retention")
* [Disable termination protection with the AWS CLI](#lake-cli-update-disable-termination "#lake-cli-update-disable-termination")

## Update the billing mode with the AWS CLI


The `--billing-mode` for the event data store determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. If an 
 event data store's `--billing-mode` is set to `FIXED_RETENTION_PRICING`, you can change the value to `EXTENDABLE_RETENTION_PRICING`. 
 `EXTENDABLE_RETENTION_PRICING` is generally recommended if your event data store ingests less than 25 TB of event data per month 
 and you want a flexible retention period of up to 3653 days. For
 information about pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/") and [Managing CloudTrail Lake costs](cloudtrail-lake-manage-costs.md "cloudtrail-lake-manage-costs.md").


###### Note

You cannot change the `--billing-mode` value from `EXTENDABLE_RETENTION_PRICING` to `FIXED_RETENTION_PRICING`. If the event data store's 
 billing mode is set to `EXTENDABLE_RETENTION_PRICING` and you want to use `FIXED_RETENTION_PRICING` instead, you can [stop ingestion](lake-cli-manage-eds.md#lake-cli-stop-ingestion-eds "lake-cli-manage-eds.md#lake-cli-stop-ingestion-eds") on the event data store 
 and create a new event data store that uses `FIXED_RETENTION_PRICING`.


The following example AWS CLI **update-event-data-store** command changes the `--billing-mode` for 
 the event data store from `FIXED_RETENTION_PRICING` to `EXTENDABLE_RETENTION_PRICING`. The required
 `--event-data-store` parameter value is an ARN (or the ID suffix of
 the ARN) and is required; other parameters are optional. 



```
aws cloudtrail update-event-data-store \
--region us-east-1 \
--event-data-store arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE \
--billing-mode EXTENDABLE_RETENTION_PRICING
```

The following is an example response.



```
{
    "EventDataStoreArn": "event-data-store arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE",
    "Name": "management-events-eds",
    "Status": "ENABLED",
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
    "RetentionPeriod": 2557,
    "TerminationProtectionEnabled": true,
    "CreatedTimestamp": "2023-10-27T10:55:55.384000-04:00",
    "UpdatedTimestamp": "2023-10-27T10:57:05.549000-04:00"
}
```

## Update the retention mode, enable termination protection, and specify a AWS KMS key with the AWS CLI


The following example AWS CLI **update-event-data-store** command updates an event data store to change its retention period
 to 100 days, and enable termination protection. The required
 `--event-data-store` parameter value is an ARN (or the ID suffix of
 the ARN) and is required; other parameters are optional. In this example, the
 `--retention-period` parameter is added to change the retention
 period to 100 days. Optionally, you can choose to enable AWS Key Management Service encryption and
 specify an AWS KMS key by adding `--kms-key-id` to the command, and
 specifying a KMS key ARN as the value.
 `--termination-protection-enabled` is added to enable termination
 protection on an event data store that did not have termination protection
 enabled.


An event data store that logs events from outside AWS cannot be updated to log
 AWS events. Similarly, an event data store that logs AWS events cannot be
 updated to log events from outside AWS.


###### Note

If you decrease the retention period of an event data store, CloudTrail will remove any events with an `eventTime` older than the new retention period. For example, if the previous 
 retention period was 365 days and you decrease it to 100 days, CloudTrail will remove events with an `eventTime` older than 100 days.



```
aws cloudtrail update-event-data-store \
--event-data-store arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE \
--retention-period 100 \
--kms-key-id "arn:aws:kms:us-east-1:0123456789:alias/`KMS_key_alias`" \
--termination-protection-enabled
```

The following is an example response.



```
{
    "EventDataStoreArn": "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-ee54-4813-92d5-999aeEXAMPLE",
    "Name": "my-event-data-store",
    "Status": "ENABLED",
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
    "RetentionPeriod": 100,
    "KmsKeyId": "arn:aws:kms:us-east-1:0123456789:alias/`KMS_key_alias`",
    "TerminationProtectionEnabled": true,
    "CreatedTimestamp": "2023-10-27T10:55:55.384000-04:00",
    "UpdatedTimestamp": "2023-10-27T10:57:05.549000-04:00"
}
```

## Disable termination protection with the AWS CLI


By default, termination protection is enabled on an event data store to protect the event data store from accidental deletion. You cannot delete an event data store when 
 termination protection is enabled. If you want to delete the event data store, you must first disable termination protection.


The following example AWS CLI **update-event-data-store** command
 disables termination protection by passing the `--no-termination-protection-enabled` parameter.



```
aws cloudtrail update-event-data-store \
--region us-east-1 \
--no-termination-protection-enabled \
--event-data-store arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE
```

The following is an example response.



```
{
    "EventDataStoreArn": "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE",
    "Name": "management-events-eds",
    "Status": "ENABLED",
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
    "RetentionPeriod": 366,
    "TerminationProtectionEnabled": false,
    "CreatedTimestamp": "2023-10-27T10:55:55.384000-04:00",
    "UpdatedTimestamp": "2023-10-27T10:57:05.549000-04:00"
}
```
