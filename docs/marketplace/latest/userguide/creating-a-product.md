

# Creating a product in AWS Marketplace

You create and manage every product you sell in AWS Marketplace from one page in AWS Partner Central: **Products and services**. This page covers how to reach it, what it shows you, and how to create a product.

**Topics**
+ [Opening Products and services](#opening)
+ [What the page shows](#columns)
+ [Creating a product](#creating)
+ [Completing your listing](#stepper)
+ [Tracking your requests](#requests-tracking)

## Opening Products and services
<a name="opening"></a>

To open the Products and services page, do the following:

1. Sign in to the AWS Partner Central console at `https://us-east-1.console.aws.amazon.com/partnercentral/home`.

1. In the left navigation pane, under **Build**, choose a product type: **AI agents & tools**, **SaaS products**, **Server products**, **Machine learning products**, **Data products**, or **Professional services**.

All six choices open the same **Products and services** page. It lists your whole portfolio across every product type, and you filter it to the type you want.

If you used AWS Marketplace Management Portal, this page replaces the separate per-type product pages. A bookmark to one of those pages opens Products and services, without the product type preselected.

## What the page shows
<a name="columns"></a>

Each row is one product.


| Column | What it tells you | 
| --- | --- | 
| **Product name** | Choose it to open the product's overview. | 
| **Visibility** | `Draft`, `Limited`, `Public`, or `Restricted`. See the following table. | 
| **Issues** | Problems found on the product that you need to resolve. | 
| **Product type** | The delivery type, for example `Software - SaaS` or `Software - Container`. | 
| **Last modified on (EST)** | When the product last changed. | 
| **Listing strength** | How your listing compares with the standards that drive buyer engagement. | 
| **Product ID** | The product identifier, beginning `prod-`. | 

### Visibility values
<a name="columns-visibility-values"></a>


| Value | Meaning | 
| --- | --- | 
| **Draft** | This product is still being set up. Complete product details and deployments, then choose **Advance to procurement configuration** to move to Limited. | 
| **Limited** | This product is visible to select accounts for testing. Complete procurement configuration to request full publication. Most product types then go through an AWS Marketplace review before they become public. Machine learning products publish without one. | 
| **Public** | This product is live and available to all buyers on AWS Marketplace. | 
| **Restricted** | This product has been removed from public availability. Existing subscribers retain access, but new buyers cannot purchase. | 

You cannot move a product from **Public** back to **Limited**.

### Listing strength
<a name="columns-listing-strength"></a>

A position on a four-point scale, not a numeric score:


| Position | Rating | 
| --- | --- | 
| 1 of 4 | Needs improvement | 
| 2 of 4 | Basic | 
| 3 of 4 | Strong | 
| 4 of 4 | Excellent | 

Two values are not ratings. **Loading** appears while the rating is being read. A hyphen (**-**) appears when a product has not been rated yet, or when the rating could not be read.

To raise a product's rating, open the product and choose the **Listing strength** tab. For more information, see [AI-assisted product listing](ai-assisted-product-listing.md).

**Notes on this column**
+ You cannot sort by **Listing strength**. Ratings are read after the rows load, so the sort order would change as they arrive.
+ If every row shows a hyphen, your account might not be enabled for listing assessment. Contact AWS Marketplace Seller Operations on the [AWS Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1) in the AWS Partner Central console.

## Creating a product
<a name="creating"></a>

1. On the **Products and services** page, choose **Create product**.

1. Choose the product type you are creating.

1. Work through the listing steps.

There is one **Create product** action for every product type. You no longer start from a separate page per type.

For what each product type requires, see the chapter for that type. To decide whether you need a product, a solution, or both, see [Deciding what to list in AWS Marketplace](deciding-what-to-list.md).

## Completing your listing
<a name="stepper"></a>

A product's overview page carries a **Complete your listing** progress bar. Each step holds task cards, and each card is marked required or optional, so you can see which steps are complete and which remain.

One of the steps is **Testing and integrations**. It tells you which metering and entitlement API integrations your product requires, and verifies the ones AWS Marketplace can check automatically. Not every product has this step. **Publishing fails until your required integrations are complete.** For more information, see [Testing and integrations](testing-and-integrations.md).

## Tracking your requests
<a name="requests-tracking"></a>

When you submit a change to a product, AWS Marketplace creates a request.

To see your requests, in the left navigation pane, under **Build**, choose **Requests**. The **Requests history** table lists them.

Requests are no longer shown on a tab of a product-type page. For more information, see [Managing your requests](requests.md).