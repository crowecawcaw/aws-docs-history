

# Jobs pricing
<a name="jobs-pricing"></a>

You pay for Amazon Location Service Jobs based on the number of records processed. Jobs process records asynchronously and write results to your specified Amazon S3 bucket. The price varies based on the additional features you request for the job. If you cancel a job, you are billed for the number of records that were successfully processed and written to your output bucket before cancellation.

For detailed pricing information, see [Amazon Location Service Pricing](https://aws.amazon.com/location/pricing/).

The Amazon Location Service Jobs capability supports address validation. There are two pricing buckets for Jobs APIs: **Core** and **Advanced**.

## Core
<a name="jobs-core-pricing"></a>

The Core pricing bucket supports address validation. Address validation verifies that an address exists and is deliverable by checking it against authoritative address datasets. Address standardization formats addresses according to official postal standards. For example, it applies consistent abbreviations, capitalization, and punctuation. It also corrects errors such as spelling mistakes and adds missing address components such as postal codes and street names.

For a full list of response fields, see the [Jobs APIs](jobs-api-reference.md). You can store results permanently for this pricing bucket. Address validation jobs write the validated addresses directly to your specified Amazon S3 bucket. You can retain validated addresses indefinitely, similar to the Stored pricing tier for Amazon Location Service Places APIs. For more information, see [Places pricing](places-pricing.md).

## Advanced
<a name="jobs-advanced-pricing"></a>

The Advanced pricing bucket provides additional position context to validated addresses. When you turn on the Position feature, the output includes geographic coordinates (latitude and longitude) as an address point for each validated address. The Position feature is supported in the United States, Canada, and Australia. United Kingdom customers can access Core address validation but not the Advanced tier with position coordinates.

When you turn on the Position feature, you are charged at the Advanced price. As with the Core tier, you can store results permanently. For more information, see [Places pricing](places-pricing.md).