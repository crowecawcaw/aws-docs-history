# Copy trail events to an existing event data store using the CloudTrail console

Use the following procedure to copy trail events to an existing event data store. For information about how to create a new event data store, see [Create an event data store for CloudTrail
events with the console](query-event-data-store-cloudtrail.md "query-event-data-store-cloudtrail.md").

###### Note

Before copying trail events to an existing event data store, be sure the event data store's pricing option and retention period are configured appropriately for your use case.

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

###### To copy trail events to an event data store

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. Choose **Trails** in the left navigation pane of the CloudTrail console.
3. On the **Trails** page, choose the trail, and then choose
   **Copy events to Lake**. If the source S3 bucket for the
   trail uses a KMS key for data encryption, ensure that the KMS key policy
   allows CloudTrail to decrypt data in the bucket. If the source S3 bucket uses multiple
   KMS keys, you must update each key's policy to allow CloudTrail to decrypt data in
   the bucket. For more information about updating the KMS key policy, see [KMS key policy for decrypting data
   in the source S3 bucket](cloudtrail-copy-trail-to-lake.md#cloudtrail-copy-trail-events-permissions-kms "cloudtrail-copy-trail-to-lake.md#cloudtrail-copy-trail-events-permissions-kms").
4. (Optional) By default, CloudTrail only copies CloudTrail events contained in the S3 bucket's `CloudTrail` prefix and the prefixes inside the `CloudTrail` prefix, and does not check prefixes for other AWS services.
   If you want to copy CloudTrail events contained in another prefix, choose **Enter S3 URI**, and then choose **Browse S3** to browse to the prefix.

The S3 bucket policy must grant CloudTrail access to copy trail events. For more information about updating the S3 bucket policy, see [Amazon S3 bucket policy for copying trail
events](cloudtrail-copy-trail-to-lake.md#cloudtrail-copy-trail-events-permissions-s3 "cloudtrail-copy-trail-to-lake.md#cloudtrail-copy-trail-events-permissions-s3"). 5. For **Specify a time range of events**, choose the time range for
copying the events. CloudTrail checks the prefix and log file name to verify the name contains a date between the chosen start and end date before attempting to copy trail events. You can choose a **Relative range** or an
**Absolute range**. To avoid duplicating events between the source trail and destination event data store, choose a time range that is earlier than the creation of the event data store.

###### Note

CloudTrail only copies trail events that have an `eventTime` within the event data store’s retention period.
For example, if an event data store’s retention period is 90 days, then CloudTrail will not copy any trail events with an `eventTime` older than 90 days.

    * If you choose **Relative range**, you can
     choose to copy events logged in the last 6 months, 1 year, 2 years, 7 years, or a custom range. CloudTrail copies the events logged within the chosen time period.
    * If you choose **Absolute range**, you can choose a specific start and end date. CloudTrail copies the events that occurred between the chosen
     start and end dates.

6. For **Delivery location**, choose the destination event data
   store from the drop-down list.
7. For **Permissions**, choose from the following IAM role
   options. If you choose an existing IAM role, verify that the IAM role policy
   provides the necessary permissions. For more information about updating the
   IAM role permissions, see [IAM permissions
   for copying trail events](cloudtrail-copy-trail-to-lake.md#cloudtrail-copy-trail-events-permissions-iam "cloudtrail-copy-trail-to-lake.md#cloudtrail-copy-trail-events-permissions-iam").
   - Choose **Create a new role (recommended)** to create a new IAM role. For **Enter IAM role name**, enter a name for the role.
     CloudTrail automatically creates the necessary permissions for this new role.
   - Choose **Use a custom IAM role ARN** to use a custom IAM role that is not listed. For **Enter IAM role ARN**, enter the IAM ARN.
   - Choose an existing IAM role from the drop-down list.

8. Choose **Copy events**.
9. You are prompted to confirm the copy. When you are ready to confirm, choose **Copy trail events to Lake**, and then choose **Copy events**.
10. On the **Copy details** page, you can see the copy status and review any failures. When a trail event copy completes, its
    **Copy status** is set to either **Completed** if there were no errors, or **Failed** if errors occurred.

###### Note

Details shown on the event copy details page are not in real-time. The actual values
for details such as **Prefixes copied** may be higher than what is shown on the page.
CloudTrail updates the details incrementally over the course of the event copy. 11. If the **Copy status** is **Failed**, fix any errors shown in **Copy failures**, and then choose **Retry copy**.
When you retry a copy, CloudTrail resumes the copy at the location where the failure occurred.
For more information about viewing the details of a trail event copy, see [View event copy details with the CloudTrail console](copy-trail-details.md "copy-trail-details.md").
