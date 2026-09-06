

# Listings
<a name="marketplace-listings"></a>

Create and manage your AWS Marketplace product listings from the Storefront console.

## Creating a SaaS listing
<a name="creating-a-saas-listing"></a>

You can create a SaaS product listing for AWS Marketplace directly from the Storefront console. The listing wizard guides you through each step of the product configuration.

### Prerequisites
<a name="creating-a-saas-listing-prerequisites"></a>
+ A connected AWS Marketplace seller account
+ Seller registration approved by AWS Marketplace
+ Account Admin or Listing Management role on the connected account.

### To create a SaaS listing
<a name="creating-a-saas-listing-create"></a>

1. In your connected account, choose **Products**.

1. Choose **Add listing**.

1. Choose one of the following product types:
   + SaaS Contract
   + SaaS Subscription
   + AMI (hourly or hourly-annual)
   + Clone Existing Listing

   Container and Professional Services are visible but disabled.

1. Complete each section of the listing wizard:

1. Review the listing summary.

1. Choose **Submit for Review**.

The listing enters a pending state while AWS Marketplace reviews it. You receive a notification when it is approved or if changes are required.

#### General information
<a name="creating-a-saas-listing-general"></a>
+ **SKU** - The product SKU identifier
+ **Vendor** - The vendor name
+ **Website** - The product website URL
+ **Title** - The name buyers see in AWS Marketplace
+ **Product Description** - Detailed product description
+ **Short Product Description** - Brief summary of the product
+ **Product Logo URL** - S3 URL for your product logo. This field accepts an S3 URL.
+ **Product Video Link** - URL to a product video

#### Pricing
<a name="creating-a-saas-listing-pricing"></a>

Configure the pricing model for your SaaS product:
+ **Pricing dimensions** - Define the units buyers are charged for (for example, users, API calls, GB)
+ **Contract terms** - Choose from the following durations:
  + Monthly
  + 1 Year
  + 2 Years
  + 3 Years

After your product is published to Limited, you cannot change the number of pricing dimensions or the dimension names.

For more information about pricing models, see [Pricing](https://docs.aws.amazon.com/marketplace/latest/userguide/pricing.html) in the AWS Marketplace Seller Guide.

#### Notifications
<a name="creating-a-saas-listing-notifications"></a>

In the Notifications section, choose a value from the **Select Notification** dropdown (default: None).

### Notes
<a name="creating-a-saas-listing-notes"></a>
+ Listing creation through the console uses the AWS Marketplace Catalog API. Ensure your connected account has the required IAM permissions.
+ You can save a draft at any point and return to complete it later.
+ After a listing is active, you can update it by creating a new version.

### Related topics
<a name="creating-a-saas-listing-related"></a>
+ Creating a Multi-Product Solution
+ [Using listing templates](#using-listing-templates)
+ [Managing tags and categories on products](#managing-tags-and-categories)

## Creating a Multi-Product Solution
<a name="creating-a-multi-product-solution"></a>

A Multi-Product Solution listing groups multiple related products into a single solution offering. Buyers can discover and evaluate the complete solution from one listing page, then procure individual components.

### Prerequisites
<a name="creating-a-multi-product-solution-prerequisites"></a>
+ A connected AWS Marketplace seller account
+ 2 to 7 active product listings to include in the solution
+ Account Admin or Listing Management role on the connected account.

### To create a Multi-Product Solution
<a name="creating-a-multi-product-solution-create"></a>

1. In your connected account, choose **Products**.

1. Choose **Create Listing**.

1. Choose **Multi-Product Solution** as the product type.

1. Complete each section:

1. Review the solution summary.

1. Choose **Submit for Review**.

#### Products
<a name="creating-a-multi-product-solution-products"></a>

Choose the products that make up this solution:

1. Choose **Add Product**.

1. Search for and choose products from your active listings.

1. For each product, add a **Role description** explaining how it fits in the solution.

1. Arrange products in the display order.

#### Use cases
<a name="creating-a-multi-product-solution-use-cases"></a>

Describe how buyers use the solution:

1. Choose **Add Use Case**.

1. Enter a **Title** and **Description** for each use case.

1. Add up to 3 use cases.

#### Promotional media
<a name="creating-a-multi-product-solution-media"></a>

Add visual content to showcase the solution:
+ **Architecture diagram** - Upload a diagram showing how components work together
+ **Demo video** - Link to a product demonstration video
+ **Screenshots** - Upload up to 5 screenshots

#### Additional resources
<a name="creating-a-multi-product-solution-resources"></a>

Link supporting materials:
+ Whitepapers
+ Case studies
+ Implementation guides
+ Documentation links

### Notes
<a name="creating-a-multi-product-solution-notes"></a>
+ Products included in a Multi-Product Solution must be active AWS Marketplace listings.
+ The solution listing does not change the pricing or procurement of individual products. Buyers still procure each product separately.
+ You can update the products included in a solution after it is published.

### Related topics
<a name="creating-a-multi-product-solution-related"></a>
+ [Creating a SaaS listing](#creating-a-saas-listing)
+ [Using listing templates](#using-listing-templates)
+ Sharing products

## Using listing templates
<a name="using-listing-templates"></a>

Listing templates pre-populate common fields when creating a new product listing, reducing setup time for products that share similar configurations.

### To use a template during listing creation
<a name="using-listing-templates-select"></a>

1. In your connected account, choose **Products**.

1. Choose **Add listing**.

1. At the top of the Add listing form, open the **Search Template - optional** dropdown and choose a template. The selection populates the form.

1. Complete the remaining required fields and submit.

### Available templates
<a name="using-listing-templates-available"></a>

Templates are based on common listing configurations:
+ Standard SaaS listing
+ Usage-based SaaS listing
+ Contract SaaS listing
+ AMI listing (basic)
+ Multi-Product Solution

### Notes
<a name="using-listing-templates-notes"></a>
+ Templates pre-populate fields but do not lock them. You can change any pre-filled value.
+ Templates are managed at the organization level. Contact your Admin to request new templates.

### Related topics
<a name="using-listing-templates-related"></a>
+ [Creating a SaaS listing](#creating-a-saas-listing)
+ Storefront templates

## Managing tags and categories on products
<a name="managing-tags-and-categories"></a>

You can assign tags and categories to your products to improve discoverability in your storefronts and help buyers find relevant products.

### Tags vs. categories
<a name="managing-tags-and-categories-vs"></a>


| Feature | Tags | Categories | 
| --- | --- | --- | 
| Scope | Storefront-level (specific to each storefront) | Product-level (applies across all storefronts) | 
| Purpose | Filter navigation within a storefront | Product classification and search | 
| Assignment | Assigned in the storefront Tags tab | Assigned during product creation or edit | 

### To assign categories to a product
<a name="managing-tags-and-categories-assign-categories"></a>

1. In your connected account, choose **Products**.

1. Choose the product to edit.

1. In the **General** section, set **Product Category 1** (required), and optionally **Product Category 2** and **Product Category 3**.

1. Choose **Save**.

### To add custom tags to a product
<a name="managing-tags-and-categories-add-tags"></a>

Custom tags provide additional metadata for use in storefront filtering:

1. Choose the product to edit.

1. Choose **Tags**.

1. Choose **Add Tag** and enter a tag name (for example, "enterprise," "starter-friendly," "compliance").

1. Choose **Save**.

These tags are available for assignment when configuring storefront tag filters.

### Tag dialog
<a name="managing-tags-and-categories-tag-dialog"></a>

You can also manage tags in bulk from the product list view:

1. In the **Products** page, choose one or more products using the checkboxes.

1. Choose **Manage Tags** from the actions menu.

1. Add or remove tags for the selected products.

1. Choose **Apply**.

### Related topics
<a name="managing-tags-and-categories-related"></a>
+ Managing tags
+ Categories and badges
+ [Setting listing visibility](#setting-listing-visibility)

## Setting listing visibility
<a name="setting-listing-visibility"></a>

You can control whether a product is publicly visible on AWS Marketplace or limited to specific buyers. Visibility settings determine who can discover and access your products.

### Visibility options
<a name="setting-listing-visibility-options"></a>


| Visibility | Description | 
| --- | --- | 
| Public | Visible to all buyers on AWS Marketplace and in your storefronts | 
| Limited | Limited products are only visible to allowlisted AWS accounts. This includes the seller account that you are signed in to. | 
| Restricted | Existing users can continue to use the product. The product is no longer visible to the public or available to new users. | 

### To change product visibility
<a name="setting-listing-visibility-change"></a>

1. In your connected account, choose **Products**.

1. Choose the product.

1. Choose **Update Visibility** from the actions menu.

1. In the **Update Listing Visibility** dialog, choose **Public**, **Limited**, or **Restricted**.

1. Choose **Update**.

### Limited products in storefronts
<a name="setting-listing-visibility-limited"></a>

Limited-visibility products can still be displayed in your storefronts. This is useful for:
+ Partner-exclusive products that should not appear on the public AWS Marketplace
+ Pre-launch products shared with select buyers
+ Internal tools available only to your organization's buyer community

To include limited products in a storefront:

1. Open the storefront's **Selection** tab.

1. Choose the **My Products** source tab.

1. Limited products from your connected account appear here alongside public products.

1. Choose the limited products to include.

### Notes
<a name="setting-listing-visibility-notes"></a>
+ Changing visibility does not affect existing agreements or active subscriptions.
+ Limited products are accessible via direct URL even if not in a storefront.
+ Visibility changes may take a few minutes to propagate across AWS Marketplace.

### Related topics
<a name="setting-listing-visibility-related"></a>
+ Importing products
+ [Managing tags and categories on products](#managing-tags-and-categories)
+ Sharing products