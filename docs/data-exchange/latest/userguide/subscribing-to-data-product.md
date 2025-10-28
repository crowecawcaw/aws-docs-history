# Subscribing to and accessing an AWS Data Exchange product containing

file-based data

The following topics describe the complete process of subscribing to and accessing a
product containing file-based data stored as files on AWS Data Exchange. To complete the process, use the
AWS Data Exchange console.

For information about how to evaluate a product before subscribing, see [Evaluate products containing
data dictionaries and samples](subscriber-getting-started.md#evaluate-products "subscriber-getting-started.md#evaluate-products").

The process has the following steps:

###### Steps

- [Step 1: Subscribing to a product containing the
  file-based data](#subscribe-to-data-product "#subscribe-to-data-product")
- [Step 2: Accessing a product containing file-based data](#use-product "#use-product")
  To practice subscribing to and accessing a product containing file-based data, see the
  [AWS Data Exchange Heartbeat](heartbeat.md "heartbeat.md").

## Step 1: Subscribing to a product containing the

file-based data

If you subscribe to a paid product, you are billed on your AWS bill. You get access to
all entitled data sets. For more information, see [Subscribing to AWS Data Exchange data products on AWS Data Exchange](subscribe-to-data-sets.md "subscribe-to-data-sets.md").

###### To subscribe to a product containing the file-based data

1. Open and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, under **Discover data products**,
   choose **Browse catalog**.
3. Under **Refine results**, use the **Data set type**
   filter and select **Files (Amazon S3 Objects)** to find products containing
   file-based data.

For more information, see [Browse the catalog](subscriber-getting-started.md#browse-catalog "subscriber-getting-started.md#browse-catalog"). 4. Select a data product containing **Files (Amazon S3 Objects)**, and view
its product detail page.

The information on the product detail page includes a product description, the
provider's contact information, and the details of the product's public offer. The
public offer information includes price and durations, the data subscription agreement
(DSA), and the refund policy. You can view the names of the data sets included in the
product and the AWS Regions in which they are available. You can also continue to
browse other product detail pages by choosing a product under **Similar
products**.

If the provider has issued a custom offer to your account (for example, a [private offer](subscribe-to-private-offer.md "subscribe-to-private-offer.md") or [Bring Your Own Subscription (BYOS) offer](subscribe-to-byos-offer.md "subscribe-to-byos-offer.md")),
you see those details, too. 5. In the top right corner, choose **Continue to subscribe**. 6. Choose your preferred price and duration combination, choose whether to enable
auto-renewal for the subscription, and review the oﬀer details, including the
DSA.

###### Note

Some products require subscription verification. For more information, see [Subscription verification for subscribers in
AWS Data Exchange](subscription-verification-sub.md "subscription-verification-sub.md"). 7. Review the pricing information, choose the pricing oﬀer, and then choose
**Subscribe**.

###### Note

If you subscribe to a paid product, you are prompted to confirm your decision to
subscribe. 8. Under **Data sets included with your subscription**, view the
listed **Data sets**.

After the subscription finishes processing, you can choose a data set to access
your entitled data or choose **View subscription** to view your
subscription. 9. (_Optional_) For **Set up exports -
_optional_**, select the check boxes for
the data sets that contain the revisions that you want to export. Selecting a data set
will prepare its most recently published revision to be exported.

    1. Choose a **Simple** destination option to select an Amazon S3 bucket
     location or choose **Advanced** to configure an Amazon S3 key naming
     pattern. This choice determines where your revisions will be exported. For more
     information about using key patterns, see [Key patterns when exporting asset revisions
     from AWS Data Exchange](revision-export-keypatterns.md "revision-export-keypatterns.md").
    2. For **Auto-export future revisions**, choose whether to turn on
     or turn off automatic revision export:




    	* **On** – All future revisions will always be
    	 exported.
    	* **Off** – Only one export of the most recent
    	 revision will be exported.
    3. Choose the **Encryption** options, and review the
     **Amazon S3 pricing**.


    ###### Note

    If you choose to export using AWS Key Management Service (AWS KMS) encryption, make sure your
     account has the correct AWS Identity and Access Management (IAM) permissions to create and revoke grants
     on the AWS KMS key you choose. Without these permissions, automatic export will
     fail.
    4. Choose **Export** to export the data to Amazon S3, or choose
     **Skip** if you prefer to wait and export or download later. For
     more information about how to export data after subscribing, see [(Optional) Exporting data](#export-data-after-subscribing "#export-data-after-subscribing").


    ###### Note

    It can take a few minutes for your subscription to become active after you
     choose **Subscribe**. If you choose **Export**
     before the subscription is active, you are prompted to wait until it is
     complete.

    After your subscription is active, your export will begin.

    Navigating away from this page prior to your subscription becoming active will
     not prevent the subscription from processing. It will prevent your data export
     from occurring.

## Step 2: Accessing a product containing file-based data

After you successfully subscribe to a product, you have access to the product data sets
according to the terms of the data subscription agreement (DSA).

The following topic describes how to access a product containing file-based data.

### Viewing data sets, revisions, and

assets

###### To view the data sets, revisions, and assets

1. Open and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left navigation pane, choose **Subscriptions**, and then
   choose your product.
3. View the data sets that are part of the product under **Entitled data
   sets**.
4. Choose a data set.
5. View the **Data set overview**, **Auto-export job
   destinations** (Amazon S3 products only), the **Revisions**,
   and the **Description** of the data set.

For more information, see [Data in AWS Data Exchange](data-sets.md "data-sets.md"). 6. Choose a revision.

Revisions are listed from latest to oldest. 7. View the **Revision overview**, **Assets**, and
the **Jobs** that have been performed.

For information about exporting file-based assets, see [Exporting AWS Data Exchange assets to an S3 bucket as a
subscriber (console)](export-asset-s3-console-sub.md "export-asset-s3-console-sub.md").

### (Optional) Exporting data

After your subscription is active, you can set up your Amazon S3 bucket to receive assets
that you export.

You can export the associated assets to Amazon S3 or you can use jobs with a signed
URL.

If you want to export or download your data at a later time, including getting new
revisions, see [Exporting AWS Data Exchange assets to an S3 bucket as a
subscriber (console)](export-asset-s3-console-sub.md "export-asset-s3-console-sub.md").

###### Important

We recommend that you consider Amazon S3 security features when exporting data to Amazon S3.
For more information about general guidelines and best practices, see [Security
best practices for Amazon S3](../../../AmazonS3/latest/dev/security-best-practices.md "../../../AmazonS3/latest/dev/security-best-practices.md") in the _Amazon Simple Storage Service User Guide_.

For more information about how to export data, see [Exporting assets from AWS Data Exchange](exporting-assets.md "exporting-assets.md") and [Exporting revisions from AWS Data Exchange](exporting-revisions.md "exporting-revisions.md").
