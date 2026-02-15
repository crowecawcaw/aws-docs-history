# Subscribing to and accessing an AWS Data Exchange product

containing APIs

The following topics describe the complete process of subscribing to and accessing a
product containing APIs on AWS Data Exchange by using the AWS Data Exchange console.

For information about how to evaluate a product before subscribing, see [Evaluate products containing
data dictionaries and samples](subscriber-getting-started.md#evaluate-products "subscriber-getting-started.md#evaluate-products").

The process has the following steps:

###### Steps

- [Step 1: Subscribing to a product containing
  APIs](#subscribe-to-API-product "#subscribe-to-API-product")
- [Step 2: Accessing an API product](#use-API-product "#use-API-product")
  To practice subscribing to and accessing a product containing APIs, see the [AWS Data Exchange for APIs (Test Product)](subscriber-tutorial-api-product.md "subscriber-tutorial-api-product.md").

## Step 1: Subscribing to a product containing

APIs

If you subscribe to a paid product, you're billed on your AWS bill. You get access to
all entitled data sets. For more information, see [Subscribing to AWS Data Exchange data products on AWS Data Exchange](subscribe-to-data-sets.md "subscribe-to-data-sets.md").

A provider might include metered costs to their product containing APIs. If a provider
decreases metered costs, the price decrease goes into effect immediately. If the provider
increases metered costs, and you're an existing subscriber, the price increase goes into
effect on the first day of the month, 90 days after the price increase was submitted OR upon
renewal (whichever is sooner). An email message is sent to existing subscribers when the
price change is submitted.

###### Example

For example, assume that a provider submits a metered cost price increase on May 10.
Existing subscribers receive an email message about the price change. The price increase
goes into effect on September 1.

###### To subscribe to a product containing APIs

1. Open and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, under **Discover data products**,
   choose **Browse catalog**.

For more information, see [Browse the catalog](subscriber-getting-started.md#browse-catalog "subscriber-getting-started.md#browse-catalog"). 3. Under **Refine results**, use the **Data set type**
filter and select **API** to find products containing APIs.

For more information, see [Browse the catalog](subscriber-getting-started.md#browse-catalog "subscriber-getting-started.md#browse-catalog"). 4. Select a product containing APIs, and view its product detail page.

The information on the product detail page includes a product description, the
provider's contact information, and the details of the product's public offer. The
public offer information includes price and durations, metered costs (if included), the
data subscription agreement (DSA), and the refund policy. You can view the names of the
data sets included in the product and the AWS Regions in which they are available. You
can also continue to browse other product detail pages by choosing a product under
**Similar products**.

If the provider has issued a custom offer to your account (for example, a [private offer](subscribe-to-private-offer.md "subscribe-to-private-offer.md") or [Bring Your Own Subscription (BYOS)
offer](subscribe-to-byos-offer.md "subscribe-to-byos-offer.md")), you see those details, too.

    1. Under **Public offer**, view the **API metered
     costs** (if included).
    2. (Optional) In the **Metered cost calculator**, choose
     **Select metered cost** and then enter the number of units to
     display an example of the cost.

5. In the top right corner, choose **Continue to subscribe**.
6. Choose your preferred price and duration combination, choose whether to enable
   auto-renewal for the subscription, and review the oﬀer details, including the
   DSA.

###### Note

Some products require subscription verification. For more information, see [Subscription verification for subscribers in
AWS Data Exchange](subscription-verification-sub.md "subscription-verification-sub.md"). 7. Review the pricing information, choose the pricing oﬀer, and then choose
**Subscribe**.

###### Note

If you subscribe to a paid product, you're prompted to confirm your decision to
subscribe. 8. Under **Data sets included with your subscription**, view the
listed **Data sets**.

After the subscription finishes processing, you can choose a data set to access
your entitled data or choose **View subscription** to view your
subscription.

## Step 2: Accessing an API product

The following topics provide details about how to access a product that includes API
data sets:

###### Topics

- [Viewing an API](#view-the-api "#view-the-api")
- [Downloading the API specification](#download-api-spec "#download-api-spec")
- [Making an API call (console)](#make-api-call-console "#make-api-call-console")
- [Making an API call (AWS CLI)](#make-api-call-cli "#make-api-call-cli")

### Viewing an API

###### To view an API

1. Open and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left navigation pane, under **My subscriptions**, choose
   **Entitled data**.
3. Choose a data set.
4. Under the **Revisions** tab, choose a revision.
5. Under **API assets**, choose the API.
6. View the **Asset overview**.
7. Follow the guidance in the **Integration notes** to call the
   API.

### Downloading the API specification

###### To download the API specification

1. Open and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left navigation pane, under **My subscriptions**, choose
   **Entitled data**.
3. Choose a data set.
4. Under the **Revisions** tab, choose a revision.
5. Under **API assets**, choose the API.
6. On the **OpenAPI 3.0 specification**, choose **Download
   API specification**.

The specification is downloaded onto your local computer. You can then export the
asset to a third-party tool for SDK generation.

### Making an API call (console)

You can call a single endpoint in the AWS Data Exchange console.

###### To make an API call from the console

1. Open and sign in to the [AWS Data Exchange
   console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left navigation pane, under **My subscriptions**, choose
   **Entitled data**.
3. Choose a data set.
4. Under the **Revisions** tab, choose a revision.
5. Under **API assets**, choose the API.
6. For **Integration notes**:
   1. Choose **Copy** to use the **Base
      URL**.
   2. Choose **Copy** to use the **Code
      structure**.
   3. Follow the information provided in the specification documentation to call the
      API.

### Making an API call (AWS CLI)

###### To make an API call (AWS CLI)

- Use the `send-api-asset` command to call the API.

```
$ AWS dataexchange send-api-asset \
  --asset-id $ASSET_ID \
  --data-set-id $DATA_SET_ID \
  --revision-id $REVISION_ID \
  --body "..." \
{
    "headers": {
        ...
    },
    "body": "..."
}

```
