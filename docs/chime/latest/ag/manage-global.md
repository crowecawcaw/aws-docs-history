**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Managing global settings in Amazon Chime

You use the Amazon Chime console to manage call detail record settings and usage report
settings.

###### Topics

- [Configuring call detail records](#call-detail "#call-detail")
- [Configuring usage reports](#configure-usage-reports "#configure-usage-reports")

## Configuring call detail records

Before you can configure call detail record settings for your Amazon Chime administrative
account, you must first create an Amazon Simple Storage Service bucket. The Amazon S3 bucket is used as the log
destination for your call detail records. When you configure your call detail record
settings, you grant Amazon Chime read and write access to the Amazon S3 bucket in order to save and
manage your data. For more information about creating an Amazon S3 bucket, see [Getting started with Amazon Simple Storage Service](../../../AmazonS3/latest/userguide/GetStartedWithS3.md "../../../AmazonS3/latest/userguide/GetStartedWithS3.md") in the
_Amazon Simple Storage Service User Guide_.

You can configure call detail record settings for Amazon Chime Business Calling. For more information about
Amazon Chime Business Calling, see [Managing phone numbers in Amazon Chime](phone-numbers.md "phone-numbers.md").

###### To configure call detail record settings

1. Create an Amazon S3 bucket by following the steps at [Getting started with
   Amazon Simple Storage Service](../../../AmazonS3/latest/userguide/GetStartedWithS3.md "../../../AmazonS3/latest/userguide/GetStartedWithS3.md") in the _Amazon Simple Storage Service User Guide_.
2. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com "https://chime.aws.amazon.com").
3. For **Global Settings**, choose **Call detail
   records**.
4. Choose **Business Calling Configuration**.
5. For **Log destination**, select the Amazon S3 bucket.
6. Choose **Save**.

You can stop logging call detail records at any time.

###### To stop logging call detail records

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com "https://chime.aws.amazon.com").
2. For **Global Settings**, choose **Call detail
   records**.
3. Choose **Disable logging** for the applicable
   configuration.

### Amazon Chime Business Calling call detail records

When you choose to receive call detail records for Amazon Chime Business Calling, they are sent to your
Amazon S3 bucket. The following example shows the general format of an Amazon Chime Business Calling call detail
record name.

```
Amazon-Chime-Business-Calling-CDRs/json/`111122223333`/`2019/03/01`/`123a4567-b890-1234-5678-cd90efgh1234`_`2019-03-01`-`17.10.00.020`_`1a234567-89bc-01d2-3456-e78f9g01234h`
```

The following example shows the data that is represented in the call detail record
name.

```
Amazon-Chime-Business-Calling-CDRs/json/`awsAccountID`/`year/month/day`/`conferenceID`_`connectionDate`-`callStartTime`-`callDetailRecordID`
```

The following example shows the general format of an Amazon Chime Business Calling call detail
record.

```
{
    "SchemaVersion": "2.0",
    "CdrId": "1a234567-89bc-01d2-3456-e78f9g01234h",
    "ServiceCode": "AmazonChimeBusinessCalling",
    "ChimeAccountId": "12a3456b-7c89-012d-3456-78901e23fg45",
    "AwsAccountId": "111122223333",
    "ConferenceId": "123a4567-b890-1234-5678-cd90efgh1234",
    "ConferencePin": "XXXXXXXXXX",
    "OrganizerUserId": "1ab2345c-67de-8901-f23g-45h678901j2k",
    "OrganizerEmail": "jdoe@example.com",

    "CallerPhoneNumber": "+12065550100",
    "CallerCountry": "US",

    "DestinationPhoneNumber": "+12065550101",
    "DestinationCountry": "US",

    "ConferenceStartTimeEpochSeconds": "1556009595",
    "ConferenceEndTimeEpochSeconds": "1556009623",
    "StartTimeEpochSeconds": "1556009611",
    "EndTimeEpochSeconds": "1556009623",
    "BillableDurationSeconds": "24",
    "BillableDurationMinutes": ".4",
    "Direction": "Outbound"
}
```

## Configuring usage reports

When you turn on usage reports, Amazon Chime will generate a weekly file for each Team or
Enterprise account managed in the Amazon Chime console.

Before you can configure usage report settings for your Amazon Chime administrative account,
you must first create or choose an Amazon S3 bucket. The Amazon S3 bucket is used as the file
destination for your usage reports. When you configure your usage report settings, you
grant Amazon Chime read and write access to the Amazon S3 bucket in order to save and manage your
data. For more information about creating an Amazon S3 bucket, see [Getting
started with Amazon S3](../../../AmazonS3/latest/userguide/GetStartedWithS3.md "../../../AmazonS3/latest/userguide/GetStartedWithS3.md") in the _Amazon S3 User Guide_ in the
_Amazon S3 User Guide_.

###### To configure usage report settings

1. Create or select an Amazon S3 bucket.
   1. Sign in to your AWS account and open the [Amazon Chime console](https://chime.aws.amazon.com/ "https://chime.aws.amazon.com/").
   2. Under **Global Settings**, choose **Usage
      reporting**.
   3. Under **Report destination**, choose **New S3
      bucket** to create a new location and enter a name
      following the guidance listed. You can also select **Existing S3
      bucket** if you have an existing Amazon S3 bucket where you want
      to store the files.
   4. Choose **Save** to create the new Amazon S3 bucket or
      select an existing Amazon S3 bucket. This also turns on reporting.

2. New weekly reports will be placed in the Amazon S3 bucket and be available on the
   Monday of each week to allow for processing times.

You can turn off usage reports at any time.

###### To turn off usage reports

1. Open the [Amazon Chime
   console](https://chime.aws.amazon.com/ "https://chime.aws.amazon.com/").
2. Under **Global Settings**, choose **Usage
   reporting**.
3. Choose **Turn off reporting** for the applicable
   configuration.

### Usage report contents

Weekly reports provide user activity data from Sunday 00:00 UTC through Saturday
23:59 UTC. Data processing may delay weekly reports until the Monday of the
week.

1. To view your data, return to the AWS Console home and enter Amazon S3 in the
   services search.
2. Locate the bucket name. For more information about creating Amazon S3 buckets,
   navigating, and managing access to your Amazon S3 bucket, see [Getting started
   with Amazon S3](../../../AmazonS3/latest/userguide/GetStartedWithS3.md "../../../AmazonS3/latest/userguide/GetStartedWithS3.md") in the _Amazon S3 User Guide_ in the
   _Amazon S3 User Guide_.
3. The weekly usage report file will be placed in the following location in
   your Amazon S3 bucket (`/` represents a folder).

```
Amazon-Chime-User-Activity-Reports/csv/`<AWSaccountID>`/`<year>`/`<month>`/`<day>`/`<AmazonChimeAccountName>`_`<AmazonChimeaccountId>`_`<yyyymmdd>`.csv
```

For example:

```
Amazon-Chime-User-Activity-Reports/csv/123456789012/2024/11/03/Example+Sales_86efea2f-96af-40f7-be75-be057ff52c8c_20241201.csv
```

The following data is included in each report for each user in each Team or
Enterprise account:

- Team or Enterprise account name
- Week starting date
- User’s full name that is associated with their Amazon Chime account
- User email address
- User’s registration status
- User’s account creation date
- The number of meetings attended during the week
- The number of meetings that the user hosted during the week
- The number of messages sent (1:1, group, and chat room posts) during the
  week
