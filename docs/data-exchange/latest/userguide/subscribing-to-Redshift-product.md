# Subscribing to and accessing an AWS Data Exchange

product containing Amazon Redshift data sets

**Overview for recipients**

An Amazon Redshift data set is a data set that contains AWS Data Exchange datashares for Amazon Redshift. Datashares give
you read-only access to the tables, views, schemas, and user-defined functions that a data
provider adds to the datashare.

As a data subscriber, you can find and subscribe to products containing Amazon Redshift data sets.
After your subscription starts, you get access to query the data in Amazon Redshift without extracting,
transforming, and loading data. You lose access to a product's datashares after your
subscription expires.

Consider the following:

- It might take a few minutes to access the datashares after your subscription
  starts.
  The following sections describe the complete process of becoming an Amazon Redshift datashare
  product subscriber on AWS Data Exchange by using the AWS Data Exchange console.

For information about how to evaluate a product before subscribing, see [Evaluate products containing
data dictionaries and samples](subscriber-getting-started.md#evaluate-products "subscriber-getting-started.md#evaluate-products").

The process has the following steps:

###### Steps

- [Step 1: Subscribing to products containing
  Amazon Redshift data sets](#subscribe-Redshift-product "#subscribe-Redshift-product")
- [Step 2: Accessing the AWS Data Exchange datashares for Amazon Redshift](#use-Redshift-product "#use-Redshift-product")
  To practice subscribing to and accessing a product containing Amazon Redshift data sets, see the
  [Worldwide Event
  Attendance (Test Product) on AWS Data Exchange](subscriber-tutorial-RS-product.md "subscriber-tutorial-RS-product.md").

## Step 1: Subscribing to products containing

Amazon Redshift data sets

If you subscribe to a paid product, you're billed on your AWS bill. You get access
to all data sets included in the product. For more information, see [Subscribing to AWS Data Exchange data products on AWS Data Exchange](subscribe-to-data-sets.md "subscribe-to-data-sets.md").

###### To subscribe to a product containing Amazon Redshift data sets

1. Open and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, under **Discover data
   products**, choose **Browse catalog**.

For more information, see [Browse the catalog](subscriber-getting-started.md#browse-catalog "subscriber-getting-started.md#browse-catalog"). 3. Under **Refine results**, use the **Data set
type** filter and select **Amazon Redshift** to find products
containing Amazon Redshift datashares.

For more information, see [Browse the catalog](subscriber-getting-started.md#browse-catalog "subscriber-getting-started.md#browse-catalog"). 4. Select a product and view its product detail page.

The information on the product detail page includes a product description, the
provider's contact information, and the details of the product's public offer. The
public offer information includes price and duration, the data subscription agreement
(DSA), and the refund policy. You can view the names of the data sets included in the
product and the AWS Regions in which they are available. You can also continue to
browse other product detail pages by choosing a product under **Similar
products**.

If the provider has issued a custom offer to your account (for example, a [private offer](subscribe-to-private-offer.md "subscribe-to-private-offer.md") or [Bring Your Own Subscription (BYOS) offer)](subscribe-to-byos-offer.md "subscribe-to-byos-offer.md"),
you see those details, too.

###### Important

Be sure to review the date, time, and duration of the cluster’s maintenance
window. During the maintenance window, you do not have access to the
datashare. 5. In the top right corner, choose **Continue to subscribe**. 6. Review the **Product offer**, the **Subscription
terms**, the **Data sets** that are included in the offer,
and the **Support information**. 7. Choose whether to enable **Offer auto-renewal** for the
subscription

###### Note

Some products require subscription verification. For more information, see [Subscription verification for subscribers in
AWS Data Exchange](subscription-verification-sub.md "subscription-verification-sub.md"). 8. Choose **Subscribe**.

###### Note

If you subscribe to a paid product, you're prompted to confirm your decision to
subscribe. 9. Under **Data sets included with your subscription**, view the
listed **Data sets**.

After the subscription finishes processing, you can choose a data set to access
your entitled data or choose **View subscription** to view your
subscription.

## Step 2: Accessing the AWS Data Exchange datashares for Amazon Redshift

You have access to the product's data sets according to the terms of the data
subscription agreement (DSA). As a subscriber, your subscription to a product that
includes AWS Data Exchange datashares for Amazon Redshift gives you read-only access to the tables, views,
schemas, and functions within the datashare.

With a subscription, you can do the following:

- Query data without having to extract, transform, or load data.
- Access the latest provider data as soon as the provider updates it.

For more information, see [Working with AWS Data Exchange datashares](../../../redshift/latest/dg/adx-datashare.md "../../../redshift/latest/dg/adx-datashare.md") in the _Amazon Redshift Database Developer Guide_.

###### Note

You lose access to a product's datashares after your subscription expires.

For more information about how to subscribe to an Amazon Redshift data set, see [Worldwide Event
Attendance (Test Product) on AWS Data Exchange](subscriber-tutorial-RS-product.md "subscriber-tutorial-RS-product.md").
