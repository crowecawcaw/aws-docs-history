

# Managing your requests

When you submit a change to a product, AWS Marketplace creates a request and processes it. The **Requests** page lists your requests and their status.

**Topics**
+ [Opening the Requests page](#requests-opening)
+ [Request status](#status)
+ [Where else requests appear](#elsewhere)
+ [Submitting a change](#submitting)

## Opening the Requests page
<a name="requests-opening"></a>

1. Sign in to the AWS Partner Central console at `https://us-east-1.console.aws.amazon.com/partnercentral/home`.

1. In the left navigation pane, under **Build**, choose **Requests**.

The **Requests history** table lists your requests.

Requests are no longer shown on a tab of a product-type page. They are now consolidated into a single Requests page that covers every product type.

## Request status
<a name="status"></a>

A request moves through these states:


| Status | Meaning | 
| --- | --- | 
| **Preparing** | AWS Marketplace has received your request and is validating it. | 
| **Applying** | The request passed validation and is being applied to your product. | 
| **Succeeded** | The request completed. Your change is live on the product. | 
| **Failed** | The request did not complete. Your product is unchanged. | 
| **Cancelled** | The request was cancelled before it was applied. | 

A request is submitted either to apply a change or only to validate it, without applying it.

Request status is not the same as your product's visibility. A request that succeeds changes your product; it does not by itself make a product public. For product visibility, see [Creating a product in AWS Marketplace](creating-a-product.md).

## Where else requests appear
<a name="elsewhere"></a>

Two per-object views show a narrower slice of the same activity:
+ A product's **Change history** tab shows change requests for that product.
+ An offer's **Requests log** tab shows changes to that offer, such as new prices.

Use the **Requests** page when you want everything in one list; use the per-object tabs when you are already working on a product or an offer.

## Submitting a change
<a name="submitting"></a>

You submit most changes from the product itself, not from the Requests page. Open the product from **Products and services**, make your change, and submit it. The request then appears in your Requests history.

You can also submit changes programmatically with the AWS Marketplace Catalog API. If you do, note that the `Identifier` in a change set's `Entity` must include the revision suffix, for example `prod-t6cwxyglwbs7o@6`, taken from the `EntityIdentifier` returned by `DescribeEntity`. The shorter `EntityId` returned by `ListEntities` is not accepted and produces a revision mismatch error. For more information, see the *AWS Marketplace Catalog API Reference*.