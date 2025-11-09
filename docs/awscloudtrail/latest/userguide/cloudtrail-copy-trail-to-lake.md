# Copying trail events to CloudTrail

Lake

You can copy existing trail events to a CloudTrail Lake event data store to create a point-in-time
snapshot of events logged to the trail. Copying trail events does not interfere with the
trail's ability to log events and does not modify the trail in any way.

You can copy trail events to an existing event data store configured for CloudTrail events, or you can create a new CloudTrail event data store and choose the **Copy trail events** option as part of event data store creation. For more information about copying trail
events to an existing event data store, see [Copy trail events to an existing event data store using the CloudTrail console](cloudtrail-copy-trail-events.md "cloudtrail-copy-trail-events.md"). For more information about creating a new event data store, see
[Create an event data store for CloudTrail
events with the console](query-event-data-store-cloudtrail.md "query-event-data-store-cloudtrail.md").

Copying trail events to a CloudTrail Lake event data store, allows you to run queries on the copied events.
CloudTrail Lake queries offer a deeper and more customizable view of events than simple key and
value lookups in Event history, or running `LookupEvents`. For more information
on CloudTrail Lake, see [Working with AWS CloudTrail Lake](cloudtrail-lake.md "cloudtrail-lake.md").

If you are copying trail events to an organization event data store, you must use the management account for the organization. You cannot copy trail events using the delegated administrator account
for an organization.

CloudTrail Lake event data stores incur charges. When you create an event data store, you choose the [pricing option](cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want
to use for the event data store. The pricing option determines the cost for ingesting and storing events, and
the default and maximum retention period for the event data store. For information
about CloudTrail pricing and managing Lake costs, see
[AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/") and [Managing CloudTrail Lake costs](cloudtrail-lake-manage-costs.md "cloudtrail-lake-manage-costs.md").

When you copy trail events to a CloudTrail Lake event data store, you incur charges based on the amount of uncompressed data the event data store ingests.

When you copy trail events to CloudTrail Lake, CloudTrail unzips the logs that are stored in gzip
(compressed) format and then copies the events contained in the logs to your event data
store. The size of the uncompressed data could be greater than the actual S3 storage size.
To get a general estimate of the size of the uncompressed data, you can multiply the size
of the logs in the S3 bucket by 10.

You can reduce costs by specifying a narrower time range for the copied events. If you
are planning to only use the event data store to query your copied events, you can turn off
event ingestion to avoid incurring charges on future events. For more information, see
[AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/") and [Managing CloudTrail Lake costs](cloudtrail-lake-manage-costs.md "cloudtrail-lake-manage-costs.md").

**Scenarios**

The following table describes some common scenarios for copying trail events and how you accomplish each scenario using the console.

| Scenario                                                                                  | How do I accomplish this in the console?                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Analyze and query historical trail events in CloudTrail Lake without ingesting new events | Create a [new event data store](query-event-data-store-cloudtrail.md#query-event-data-store-cloudtrail-procedure "query-event-data-store-cloudtrail.md#query-event-data-store-cloudtrail-procedure")<br>and choose the **Copy trail events\*<br>• option as part of event data store creation.<br>When creating the event data store, deselect **Ingest events\*<br>• (step 15 of the procedure)<br>to ensure the event data store contains only the historical events for your trail and no future events. |
| Replace your existing trail with a CloudTrail Lake event data store                       | Create an event data store with the same event selectors as your trail to ensure that the event data store has the same coverage as your trail.<br>To avoid duplicating events between the source trail and destination<br>event data store, choose a date range for the copied events that is<br>earlier than the creation of the event data store.<br>After your event data store is created, you can turn off logging for the trail to avoid additional charges.                                         |

###### Topics

- [Considerations for copying trail events](#cloudtrail-trail-copy-considerations "#cloudtrail-trail-copy-considerations")
- [Required permissions for copying trail events](#cloudtrail-copy-trail-events-permissions "#cloudtrail-copy-trail-events-permissions")
- [Copy trail events to an existing event data store using the CloudTrail console](cloudtrail-copy-trail-events.md "cloudtrail-copy-trail-events.md")

## Considerations for copying trail events

Consider the following factors when copying trail events.

- When copying trail events, CloudTrail uses the S3 [`GetObject`](../../../AmazonS3/latest/API/API_GetObject.md "../../../AmazonS3/latest/API/API_GetObject.md") API operation to retrieve
  the trail events in the source S3 bucket. There are some S3 archived storage classes,
  such as S3 Glacier Flexible Retrieval, S3 Glacier Deep Archive, S3 Outposts, and S3 Intelligent-Tiering Deep Archive tiers
  that are not accessible by using `GetObject`. To copy trail events stored in these archived storage classes, you must first restore a
  copy using the S3 `RestoreObject` operation. For information about restoring archived objects, see
  [Restoring Archived Objects](../../../AmazonS3/latest/userguide/restoring-objects.md "../../../AmazonS3/latest/userguide/restoring-objects.md") in the _Amazon S3 User Guide_.
- When you copy trail events to an event data store, CloudTrail copies all trail events
  regardless of the configuration of the destination event data store's event types, advanced event selectors, or AWS Region.
- Before copying trail events to an existing event data store, be sure the event data store's pricing option and retention period are configured appropriately for your use case.
  - **Pricing option:** The pricing option determines the cost
    for ingesting and storing events. For more information about pricing options, see [AWS CloudTrail
    Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/") and [Event data store pricing
    options](cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option").
  - **Retention period:** The retention period determines how long event data is kept in the event data store. CloudTrail only copies trail events that have an `eventTime` within the event data store’s retention period.
    To determine the appropriate retention period, take the sum of the oldest event you want to copy in days and the number of days you
    want to retain the events in the event data store (**retention period** =
    `oldest-event-in-days` +
    `number-days-to-retain`). For example, if the oldest event you're copying is 45 days old
    and you want to keep the events in the event data store for a
    further 45 days, you would set the retention period to 90
    days.

- If you are copying trail events to an event data store for investigation and do not want to ingest any future events, you can stop ingestion on the event data store. When creating the event data store, deselect the **Ingest events** option (step 15 of the [procedure](query-event-data-store-cloudtrail.md#query-event-data-store-cloudtrail-procedure "query-event-data-store-cloudtrail.md#query-event-data-store-cloudtrail-procedure"))
  to ensure the event data store contains only the historical events for your trail and no future events.
- Before copying trail events, disable any access control lists (ACLs) attached to the source S3 bucket, and update the S3 bucket policy for the destination event data store. For more information about updating the S3 bucket policy, see [Amazon S3 bucket policy for copying trail
  events](#cloudtrail-copy-trail-events-permissions-s3 "#cloudtrail-copy-trail-events-permissions-s3"). For more information about disabling ACLs, see [Controlling ownership of objects and disabling ACLs for your bucket](../../../AmazonS3/latest/userguide/about-object-ownership.md "../../../AmazonS3/latest/userguide/about-object-ownership.md").
- CloudTrail only copies trail events from Gzip compressed log files that are in the source S3 bucket. CloudTrail does not copy trail events from uncompressed log files, or log files that were compressed using a format other than Gzip.
- To avoid duplicating events between the source trail and destination event data store, choose a time range for the copied events that is earlier than the creation of the event data store.
- By default, CloudTrail only copies CloudTrail events contained in the S3 bucket's `CloudTrail` prefix and the prefixes inside the `CloudTrail` prefix, and does not check prefixes for other AWS services. If you want to copy CloudTrail events contained in another prefix, you must choose the prefix when you copy trail events.
- To copy trail events to an organization event data store, you must use the management account for the organization. You cannot use the delegated administrator account to copy trail events to an organization event data store.

## Required permissions for copying trail events

Before copying trail events, ensure you have all the required permissions for your IAM role. You only need to update the IAM role permissions if you choose an
existing IAM role to copy trail events. If you choose to create a new IAM role, CloudTrail provides all necessary permissions for the role.

If the source S3 bucket uses a KMS key for data encryption, ensure that the
KMS key policy allows CloudTrail to decrypt data in the bucket. If the source S3 bucket uses
multiple KMS keys, you must update each key's policy to allow CloudTrail to decrypt the data
in the bucket.

###### Topics

- [IAM permissions
  for copying trail events](#cloudtrail-copy-trail-events-permissions-iam "#cloudtrail-copy-trail-events-permissions-iam")
- [Amazon S3 bucket policy for copying trail
  events](#cloudtrail-copy-trail-events-permissions-s3 "#cloudtrail-copy-trail-events-permissions-s3")
- [KMS key policy for decrypting data
  in the source S3 bucket](#cloudtrail-copy-trail-events-permissions-kms "#cloudtrail-copy-trail-events-permissions-kms")

### IAM permissions

for copying trail events

When copying trail events, you have the option to create a new IAM role, or use an existing IAM role. When you choose a new IAM role, CloudTrail creates an IAM role with the required permissions and no further action is required on your part.

If you choose an existing role, ensure the IAM role's policies allow CloudTrail to copy trail events from the source S3 bucket. This section provides examples of the required IAM role permission and trust policies.

The following example provides the permissions policy, which allows CloudTrail to copy trail events from
the source S3 bucket. Replace `amzn-s3-demo-bucket`, `myAccountID`, `region`,
`prefix`, and `eventDataStoreId` with the
appropriate values for your configuration. The `myAccountID` is the AWS account ID used for CloudTrail Lake, which may not
be the same as the AWS account ID for the S3 bucket.

Replace `key-region`, `keyAccountID`, and `keyID` with the values for the KMS key used to encrypt the source S3 bucket. You can omit the `AWSCloudTrailImportKeyAccess` statement if the source
S3 bucket does not use a KMS key for encryption.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AWSCloudTrailImportBucketAccess",
      "Effect": "Allow",
      "Action": ["s3:ListBucket", "s3:GetBucketAcl"],
      "Resource": [
        "arn:aws:s3:::`amzn-s3-demo-bucket`"
      ],
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`myAccountID`",
          "aws:SourceArn": "arn:aws:cloudtrail:`region`:`myAccountID`:eventdatastore/`eventDataStoreId`"
         }
       }
    },
    {
      "Sid": "AWSCloudTrailImportObjectAccess",
      "Effect": "Allow",
      "Action": ["s3:GetObject"],
      "Resource": [
        "arn:aws:s3:::`amzn-s3-demo-bucket`/`prefix`",
        "arn:aws:s3:::`amzn-s3-demo-bucket`/`prefix`/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`myAccountID`",
          "aws:SourceArn": "arn:aws:cloudtrail:`region`:`myAccountID`:eventdatastore/`eventDataStoreId`"
         }
       }
    },
    {
      "Sid": "AWSCloudTrailImportKeyAccess",
      "Effect": "Allow",
      "Action": ["kms:GenerateDataKey","kms:Decrypt"],
      "Resource": [
        "arn:aws:kms:`key-region`:`keyAccountID`:key/`keyID`"
      ]
    }
  ]
}
```

The following example provides the IAM trust policy, which allows CloudTrail to assume an IAM role to copy trail events from the source S3 bucket. Replace `myAccountID`, `region`, and `eventDataStoreArn` with the
appropriate values for your configuration. The `myAccountID` is the AWS account ID used for CloudTrail Lake, which may not
be the same as the AWS account ID for the S3 bucket.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudtrail.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`myAccountID`",
          "aws:SourceArn": "arn:aws:cloudtrail:`region`:`myAccountID`:eventdatastore/`eventDataStoreId`"
        }
      }
    }
  ]
}

```

### Amazon S3 bucket policy for copying trail

events

By default, Amazon S3 buckets and objects are private. Only the resource owner (the AWS
account that created the bucket) can access the bucket and objects it contains. The resource
owner can grant access permissions to other resources and users by writing an access
policy.

Before you copy trail events, you must update the S3 bucket policy
to allow CloudTrail to copy trail events from the source S3 bucket.

You can add the following statement to the S3 bucket policy to grant these permissions.
Replace `roleArn` and `amzn-s3-demo-bucket` with the
appropriate values for your configuration.

```
{
  "Sid": "AWSCloudTrailImportBucketAccess",
  "Effect": "Allow",
  "Action": [
    "s3:ListBucket",
    "s3:GetBucketAcl",
    "s3:GetObject"
  ],
  "Principal": {
    "AWS": "`roleArn`"
  },
  "Resource": [
    "arn:aws:s3:::`amzn-s3-demo-bucket`",
    "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
  ]
},
```

### KMS key policy for decrypting data

in the source S3 bucket

If the source S3 bucket uses a KMS key for data encryption, ensure the KMS key
policy provides CloudTrail with the `kms:Decrypt` and `kms:GenerateDataKey`
permissions required to copy trail events
from an S3 bucket with SSE-KMS encryption enabled. If your source S3 bucket uses
multiple KMS keys, you must update each key's policy. Updating the KMS key policy allows CloudTrail to decrypt data in the
source S3 bucket, run validation checks to ensure that events conform to CloudTrail
standards, and copy events into the CloudTrail Lake event data store.

The following example provides the KMS key policy, which allows CloudTrail
to decrypt the data in the source S3 bucket. Replace
`roleArn`, `amzn-s3-demo-bucket`,
`myAccountID`, `region`, and
`eventDataStoreId` with the appropriate values for
your configuration. The `myAccountID` is the AWS account
ID used for CloudTrail Lake, which may not be the same as the AWS account ID for the S3
bucket.

```
{
  "Sid": "AWSCloudTrailImportDecrypt",
  "Effect": "Allow",
  "Action": [
          "kms:Decrypt",
          "kms:GenerateDataKey"
  ],
  "Principal": {
    "AWS": "`roleArn`"
  },
  "Resource": "*",
  "Condition": {
    "StringLike": {
      "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
    },
    "StringEquals": {
      "aws:SourceAccount": "`myAccountID`",
      "aws:SourceArn": "arn:aws:cloudtrail:`region`:`myAccountID`:eventdatastore/`eventDataStoreId`"
    }
  }
}

```
