# Subscribing to and accessing an AWS Data Exchange

product containing AWS Lake Formation data sets (Preview)

An AWS Lake Formation data set is a data set that contains AWS Lake Formation data permission assets.

As a data subscriber, you can find and subscribe to products containing AWS Lake Formation data
sets. Once you're entitled to an AWS Data Exchange for AWS Lake Formation data set, you can query, transform,
and share access to the data within your AWS account using AWS Lake Formation, or across your AWS
organization using AWS License Manager.

## Step 1: Subscribing to products

containing AWS Lake Formation data sets

If you subscribe to a paid product, you're billed on your AWS bill. You get access
to all data sets included in the product. For more information, see [Subscribing to AWS Data Exchange data products on AWS Data Exchange](subscribe-to-data-sets.md "subscribe-to-data-sets.md").

###### To subscribe to a product containing AWS Lake Formation data sets

1. Open and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, under **Discover data
   products**, choose **Browse catalog**.

For more information, see [Browse the catalog](subscriber-getting-started.md#browse-catalog "subscriber-getting-started.md#browse-catalog"). 3. Under **Refine results**, use the **Data set
type** filter and select **AWS Lake Formation** to find products
containing AWS Lake Formation data sets. 4. Select a product and view its product detail page.

The information on the product detail page includes a product description, the
provider's contact information, and the details of the product's public offer. The
public offer information includes price and duration, the data subscription agreement
(DSA), and the refund policy. You can view the names of the data sets included in the
product and the AWS Regions in which they're available. You can also continue
browsing other product detail pages by choosing a product under **Similar
products**.

If the provider has issued a custom offer to your account (for example, a [private offer](subscribe-to-private-offer.md "subscribe-to-private-offer.md") or [Bring Your Own Subscription (BYOS) offer)](subscribe-to-byos-offer.md "subscribe-to-byos-offer.md"),
you see those details, too. 5. In the top right corner, choose **Continue to subscribe**. 6. Review the **Product offer**, the **Subscription
terms**, the **Data sets** that are included in the offer,
and the **Support information**. 7. Choose whether to enable **Offer auto-renewal** for the
subscription.

###### Note

Some products require subscription verification. For more information, see [Subscription verification for subscribers in
AWS Data Exchange](subscription-verification-sub.md "subscription-verification-sub.md"). 8. Choose **Subscribe**. If you subscribe to a paid product, you're
prompted to confirm your decision to subscribe. 9. Under **Data sets included with your subscription**, view the
listed **Data sets**.

After the subscription finishes processing, you can choose a data set to access
your entitled data or choose **View subscription** to view your
subscription.

## Step 2: Accessing the AWS Data Exchange datashares for

AWS Lake Formation

After you subscribe to a product containing AWS Lake Formation data sets, you can use Lake Formation
compatible query engines, like Amazon Athena, to query your data.

###### After subscription completion, you must do the following:

1. Accept the AWS Resource Access Manager (AWS RAM) share within 12 hours after you subscribe to the
   product. You can accept the AWS RAM share from your subscription page or the entitled
   data page for your AWS Lake Formation data permission data set on the AWS Data Exchange console. You
   only need to accept an AWS RAM share once per provider. For more information about
   accepting a resource share invitation from AWS RAM, see [Accepting a resource share
   invitation from AWS RAM](../../../lake-formation/latest/dg/accepting-ram-invite.md "../../../lake-formation/latest/dg/accepting-ram-invite.md").
2. Navigate to AWS Lake Formation and create resource links from the new shared
   resources.
3. Navigate to Athena or another AWS Lake Formation compatible query engine to query your
   data.
