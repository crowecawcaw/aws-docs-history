# Preparing third-party input data

Third-party data services provide identifiers that can be matched with your known
identifiers.

AWS Entity Resolution currently supports the following third-party data provider services:

| Data provider services | Company Name                                                                                       | Available AWS Regions                   | Identifier |
| ---------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------- | ---------- |
| LiveRamp               | US East (N. Virginia) (us-east-1), US East (Ohio)<br>(us-east-2), and US West (Oregon) (us-west-2) | Ramp ID                                 |
| TransUnion             | US East (N. Virginia) (us-east-1), US East (Ohio)<br>(us-east-2), and US West (Oregon) (us-west-2) | TransUnion Individual and Household IDs |
| Unified ID 2.0         | US East (N. Virginia) (us-east-1), US East (Ohio)<br>(us-east-2), and US West (Oregon) (us-west-2) | raw UID 2                               |

The following steps describe how to prepare third-party data to use a [provider service-based matching workflow](glossary.md#provider-service-matching "glossary.md#provider-service-matching") or a [provider service-based ID mapping
workflow](create-IDMW-provider-services-one-acct.md "create-IDMW-provider-services-one-acct.md").

###### Topics

- [Step 1: Subscribe to a provider service on
  AWS Data Exchange](#subscribe-provider-service "#subscribe-provider-service")
- [Step 2: Prepare third-party data
  tables](#prepare-third-party-data-tables "#prepare-third-party-data-tables")
- [Step 3: Save your input data table in a supported
  data format](#save-third-party-data-tables "#save-third-party-data-tables")
- [Step 4: Upload your input data table to
  Amazon S3](#upload-third-party-data-tables "#upload-third-party-data-tables")
- [Step 5: Create an AWS Glue
  table](#create-glue-table-third-party-data-tables "#create-glue-table-third-party-data-tables")

## Step 1: Subscribe to a provider service on

AWS Data Exchange

If you have a subscription with a provider service through AWS Data Exchange, you can run a matching
workflow with one of the following provider services to match your known identifiers with your
preferred provider. Your data will be matched with a set of inputs defined by your preferred
provider.

To subscribe to a provider service on AWS Data Exchange

1. View the provider listing on AWS Data Exchange. The following provider listings are available:
   - LiveRamp
     - [LiveRamp
       Identity Resolution](https://aws.amazon.com/marketplace/pp/prodview-v4557zxjo6ykq "https://aws.amazon.com/marketplace/pp/prodview-v4557zxjo6ykq")
     - [LiveRamp
       Transcoding](https://aws.amazon.com/marketplace/pp/prodview-bpp2fvfcxk2kg "https://aws.amazon.com/marketplace/pp/prodview-bpp2fvfcxk2kg")

   - TransUnion
     - TruAudience Identity Resolution & Enrichment

   - Unified ID 2.0
     - [Unified ID 2.0 Identity Resolution](https://aws.amazon.com/marketplace/pp/prodview-66zqls7iqsm6o?sr=0-4&ref_=beagle&applicationId=AWSMPContessa#offers "https://aws.amazon.com/marketplace/pp/prodview-66zqls7iqsm6o?sr=0-4&ref_=beagle&applicationId=AWSMPContessa#offers")

2. Complete one of the following steps, depending on your offer type.
   - **Private offer** – If you have an existing relationship with a
     provider, follow the [Private products and offers](../../../data-exchange/latest/userguide/subscribe-to-private-offer.md "../../../data-exchange/latest/userguide/subscribe-to-private-offer.md") procedure in the _AWS Data Exchange User
     Guide_ to accept a private offer on AWS Data Exchange.
   - **Bring your own subscription** – If you already have an
     existing data subscription with a provider, follow the [Bring Your Own Subscription (BYOS) offers](../../../data-exchange/latest/userguide/subscribe-to-byos-offer.md "../../../data-exchange/latest/userguide/subscribe-to-byos-offer.md") procedure in the _AWS Data Exchange User Guide_ to accept a BYOS offer on AWS Data Exchange.

3. After you have subscribed to a provider service on AWS Data Exchange, you can then create a matching
   workflow or an ID mapping workflow with that provider service.

For more information about how to access a provider product that contains APIs, see [Accessing an API product](../../../data-exchange/latest/userguide/subscribing-to-product.md#use-API-product "../../../data-exchange/latest/userguide/subscribing-to-product.md#use-API-product") in the in the _AWS Data Exchange User Guide_.

## Step 2: Prepare third-party data

tables

Each third-party service has a different set of recommendations and guidelines to help
ensure a successful matching workflow.

To prepare third-party data tables, consult the following table:

| Data provider services guidelines | Provider service | Unique ID needed?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Actions |
| --------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| LiveRamp                          | Yes              | Ensure the following:<br>• The [Unique ID](glossary.md#unique-id-defn "glossary.md#unique-id-defn")<br>can be either your own pseudonymous identifier or a row ID.<br>• Your data input file format and normalization is aligned with the LiveRamp<br>guidelines.<br>For more information about input file formatting guidelines for the matching<br>workflow, see [Perform Identity Resolution Through ADX](https://docs.liveramp.com/identity/en/perform-identity-resolution-through-adx.html "https://docs.liveramp.com/identity/en/perform-identity-resolution-through-adx.html") in the LiveRamp documentation.<br>For more information about input file formatting guidelines for the ID mapping<br>workflow, see [Perform<br>Transcoding Through ADX](https://docs.liveramp.com/identity/en/perform-transcoding-through-adx.html "https://docs.liveramp.com/identity/en/perform-transcoding-through-adx.html") in the LiveRamp documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| TransUnion                        | Yes              | Ensure the following are a `string` type column in the input view:<br>• [Unique ID](glossary.md#unique-id-defn "glossary.md#unique-id-defn") is<br>required and can be a CRM ID, a contact ID, a user ID or any unique ID.<br>• `Name`<br>+ `First Name` can be lower or upper case, nicknames are<br>supported, but titles and suffixes should be excluded.<br>+ `Last Name` can be lower or upper case, middle initials to be<br>excluded.<br>• `Address`<br>+ `Street address1` and `Street address1`<br>is combined into a single `Full address` line, if present.<br>+ `City` is separated from the `Full<br>address`.<br>+ `Zip` (or `zip plus4`), without any<br>special characters such as spaces, hyphens, or blanks. Use nulls if no data.<br>+ `State` is specified as a 2-letter code in upper case.<br>• + `Phone`<br>• `Phone number` should be 10 digits, without any special<br>characters such as spaces or hyphens.<br>• `Email addresses` is either plaintext or SHA256-hashed lower<br>case strings.<br>• `Date of Birth` is in y`yyy-mm-dd` format.<br>• `Digital identifiers` (Device IDs) can include IDs with<br>hyphens (36-character length raw Device IDs/MAIDs/IFAs) and without hyphens (32 &<br>40-character long hashed Device IDs/MAIDs/IFAs).<br>+ `IPV4` is a 32-bit IP address expressed in dotted decimal<br>notation. For example: `192.0.2.1`<br>+ `IPV6` is a 128-bit IP address expressed in hexadecimal<br>notation, separated by colons. For example:<br>`2001:db8:0000:0000:0000:0000:0000:0001`<br>+ `MAID` (Mobile Advertising ID) is a unique, alphanumeric<br>string assigned to a mobile device for advertising purposes. A MAID usually has 36<br>characters. For example: `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` |
| Unified ID 2.0                    | Yes              | Ensure the following:<br>• The [Unique ID](glossary.md#unique-id-defn "glossary.md#unique-id-defn")<br>can't be a hash.<br>• Either `Phone number`or `Email<br>addresses` is used in the schema, not both.<br>• UID2 supports both email and phone number for UID2 generation. However, if both<br>values are present in the schema mapping, the workflow duplicates each record in the<br>output. One record uses the email for UID2 generation and the second record uses phone<br>number. If your data includes a mix of emails and phone numbers and you don't want this<br>duplication of records in the output, the best approach is to create a separate workflow<br>for each, with separate schema mappings. In this scenario, go through the steps<br>twice—create one workflow for emails and a separate one for phone numbers.<br>NoteA specific email or phone number, at any specific time, results in the same raw UID2<br>value, no matter who made the request.Raw UID2s are created by adding salts from salt buckets which are rotated<br>approximately once a year, causing the raw UID2 to also be rotated with it. Different salt<br>buckets rotate at different times throughout the year. AWS Entity Resolution currently doesn't keep track<br>of rotating salt buckets and raw UID2s, so it is recommended that you regenerate the raw<br>UID2s daily. For more information, see [How often should UID2s be refreshed for incremental updates?](https://unifiedid.com/docs/getting-started/gs-faqs#how-often-should-uid2s-be-refreshed-for-incremental-updates "https://unifiedid.com/docs/getting-started/gs-faqs#how-often-should-uid2s-be-refreshed-for-incremental-updates") in the UID 2.0<br>documentation.                         |

## Step 3: Save your input data table in a supported

data format

If you already saved your third-party input data in a supported data format, you can skip
this step.

To use AWS Entity Resolution, the input data must be in a format that AWS Entity Resolution supports.

AWS Entity Resolution supports the following data formats:

- comma-separated value (CSV)

###### Note

LiveRamp only supports CSV files.

- Parquet

## Step 4: Upload your input data table to

Amazon S3

If you already have your third-party data table in Amazon S3, you can skip this step.

###### Note

You can store the input data in Amazon S3 resources in any Region in the AWS commercial
partition where S3 is supported. This data can be accessed from a different Region or
AWS account when running the matching workflow.

###### To upload your input data table to Amazon S3

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **Buckets**, and then choose a bucket to store your data table.
3. Choose **Upload**, and then follow the prompts.
4. Choose the **Objects** tab to view the prefix where your data is stored.
   Make a note of the name of the folder.

You can select the folder to view the data table.

## Step 5: Create an AWS Glue

table

The input data in Amazon S3 must be cataloged in AWS Glue and represented as an AWS Glue table. For
more information about how to create an AWS Glue table with Amazon S3 as the input, see [Working with crawlers on the
AWS Glue console](../../../glue/latest/dg/console-crawlers.md "../../../glue/latest/dg/console-crawlers.md") in the _AWS Glue Developer Guide._

###### Note

AWS Entity Resolution doesn't support partitioned tables.

In this step, you set up a crawler in AWS Glue that crawls all the files in your S3 bucket and
create an AWS Glue table.

###### Note

AWS Entity Resolution doesn't currently support Amazon S3 locations registered with AWS Lake Formation.

###### To create an AWS Glue table

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. From the navigation bar, select **Crawlers**.
3. Select your S3 bucket from the list, and then choose **Add
   crawler**.
4. On the **Add crawler** page, enter a **Crawler name**
   and then choose **Next**.
5. Continue through the **Add crawler page**, specifying the details.
6. On the **Choose an IAM role** page, choose **Choose an
   existing IAM role** and then choose **Next**.

You can also choose **Create an IAM role** or have your administrator
create the IAM role if needed. 7. For **Create a schedule for this crawler**, keep the
**Frequency** default (**Run on demand**) and then choose
**Next**. 8. For **Configure the crawler’s output**, enter the AWS Glue database and
then choose **Next**. 9. Review all of the details, and then choose **Finish**. 10. On the **Crawlers** page, select the check box next to your S3 bucket
and then choose **Run crawler**. 11. After the crawler is finished running, on the AWS Glue navigation bar, choose
**Databases**, and then choose your database name. 12. On the **Database** page, choose **Tables in {your database
name}**.

    1. View the tables in the AWS Glue database.
    2. To view a table's schema, select a specific table.
    3. Make a note of the AWS Glue database name and AWS Glue table name.

You are now ready to create a schema mapping. For more information, see [Creating a schema mapping](create-schema-mapping.md "create-schema-mapping.md").
