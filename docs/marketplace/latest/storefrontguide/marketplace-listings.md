# Listings

Create and manage your AWS Marketplace product listings from the Storefront console.

## Creating a SaaS listing

You can create a SaaS product listing for AWS Marketplace directly from the Storefront
console. The listing wizard guides you through each step of the product
configuration.

### Prerequisites

- A connected AWS Marketplace seller account
- Seller registration approved by AWS Marketplace
- Account Admin or Listing Management role on the connected account.

### To create a SaaS listing

1. In your connected account, choose **Products**.
2. Choose **Add listing**.
3. Choose one of the following product types:

   - SaaS Contract
   - SaaS Subscription
   - AMI (hourly or hourly-annual)
   - Clone Existing Listing
     Container and Professional Services are visible but disabled.

4. Complete each section of the listing wizard:
5. Review the listing summary.
6. Choose **Submit for Review**.

The listing enters a pending state while AWS Marketplace reviews it. You receive a
notification when it is approved or if changes are required.

#### General information

- **SKU** - The product SKU identifier
- **Vendor** - The vendor name
- **Website** - The product website URL
- **Title** - The name buyers see
  in AWS Marketplace
- **Product Description** - Detailed product
  description
- **Short Product Description** - Brief summary of the product
- **Product Logo URL** - S3 URL for your product
  logo. This field accepts an S3 URL.
- **Product Video Link** - URL to a product video

#### Pricing

Configure the pricing model for your SaaS product:

- **Pricing dimensions** - Define the units
  buyers are charged for (for example, users, API calls, GB)
- **Contract terms** - Choose from the following durations:

  - Monthly
  - 1 Year
  - 2 Years
  - 3 Years

After your product is published to Limited, you cannot change the number of pricing dimensions or the dimension names.

For more information about pricing models, see [Pricing](../userguide/pricing.md "../userguide/pricing.md") in the AWS Marketplace Seller Guide.

#### Notifications

In the Notifications section, choose a value from the **Select Notification** dropdown (default: None).

### Notes

- Listing creation through the console uses the AWS Marketplace Catalog API.
  Ensure your connected account has the required IAM permissions.
- You can save a draft at any point and return to complete it later.
- After a listing is active, you can update it by creating a new
  version.

### Related topics

- Creating a Multi-Product Solution
- [Using listing templates](#using-listing-templates "#using-listing-templates")
- [Managing tags and categories on products](#managing-tags-and-categories "#managing-tags-and-categories")

## Creating a Multi-Product Solution

A Multi-Product Solution listing groups multiple related products into a single
solution offering. Buyers can discover and evaluate the complete solution from one
listing page, then procure individual components.

### Prerequisites

- A connected AWS Marketplace seller account
- 2 to 7 active product listings to include in the solution
- Account Admin or Listing Management role on the connected account.

### To create a Multi-Product Solution

1. In your connected account, choose **Products**.
2. Choose **Create Listing**.
3. Choose **Multi-Product Solution** as the
   product type.
4. Complete each section:
5. Review the solution summary.
6. Choose **Submit for Review**.

#### Products

Choose the products that make up this solution:

1. Choose **Add Product**.
2. Search for and choose products from your active listings.
3. For each product, add a **Role
   description** explaining how it fits in the solution.
4. Arrange products in the display order.

#### Use cases

Describe how buyers use the solution:

1. Choose **Add Use Case**.
2. Enter a **Title** and **Description** for each use case.
3. Add up to 3 use cases.

#### Promotional media

Add visual content to showcase the solution:

- **Architecture diagram** - Upload a
  diagram showing how components work together
- **Demo video** - Link to a product
  demonstration video
- **Screenshots** - Upload up to 5
  screenshots

#### Additional resources

Link supporting materials:

- Whitepapers
- Case studies
- Implementation guides
- Documentation links

### Notes

- Products included in a Multi-Product Solution must be active AWS
  Marketplace listings.
- The solution listing does not change the pricing or procurement of
  individual products. Buyers still procure each product separately.
- You can update the products included in a solution after it is
  published.

### Related topics

- [Creating a SaaS listing](#creating-a-saas-listing "#creating-a-saas-listing")
- [Using listing templates](#using-listing-templates "#using-listing-templates")
- Sharing products

## Using listing templates

Listing templates pre-populate common fields when creating a new product listing,
reducing setup time for products that share similar configurations.

### To use a template during listing creation

1. In your connected account, choose **Products**.
2. Choose **Add listing**.
3. At the top of the Add listing form, open the **Search Template - optional** dropdown and choose a template. The selection populates the form.
4. Complete the remaining required fields and submit.

### Available templates

Templates are based on common listing configurations:

- Standard SaaS listing
- Usage-based SaaS listing
- Contract SaaS listing
- AMI listing (basic)
- Multi-Product Solution

### Notes

- Templates pre-populate fields but do not lock them. You can change any
  pre-filled value.
- Templates are managed at the organization level. Contact your Admin to
  request new templates.

### Related topics

- [Creating a SaaS listing](#creating-a-saas-listing "#creating-a-saas-listing")
- Storefront templates

## Managing tags and categories on products

You can assign tags and categories to your products to improve discoverability
in your storefronts and help buyers find relevant products.

### Tags vs. categories

| Feature    | Tags                                           | Categories                                     |
| ---------- | ---------------------------------------------- | ---------------------------------------------- |
| Scope      | Storefront-level (specific to each storefront) | Product-level (applies across all storefronts) |
| Purpose    | Filter navigation within a storefront          | Product classification and search              |
| Assignment | Assigned in the storefront Tags tab            | Assigned during product creation or edit       |

### To assign categories to a product

1. In your connected account, choose **Products**.
2. Choose the product to edit.
3. In the **General** section, set **Product Category 1** (required), and optionally **Product Category 2** and **Product Category 3**.
4. Choose **Save**.

### To add custom tags to a product

Custom tags provide additional metadata for use in storefront filtering:

1. Choose the product to edit.
2. Choose **Tags**.
3. Choose **Add Tag** and enter a tag name (for
   example, "enterprise," "starter-friendly," "compliance").
4. Choose **Save**.

These tags are available for assignment when configuring storefront tag
filters.

### Tag dialog

You can also manage tags in bulk from the product list view:

1. In the **Products** page, choose one or more
   products using the checkboxes.
2. Choose **Manage Tags** from the actions
   menu.
3. Add or remove tags for the selected products.
4. Choose **Apply**.

### Related topics

- Managing tags
- Categories and badges
- [Setting listing visibility](#setting-listing-visibility "#setting-listing-visibility")

## Setting listing visibility

You can control whether a product is publicly visible on AWS Marketplace or limited to
specific buyers. Visibility settings determine who can discover and access your
products.

### Visibility options

| Visibility | Description                                                                                                                |
| ---------- | -------------------------------------------------------------------------------------------------------------------------- |
| Public     | Visible to all buyers on AWS Marketplace and in your<br>storefronts                                                        |
| Limited    | Limited products are only visible to allowlisted AWS accounts. This includes the seller account that you are signed in to. |
| Restricted | Existing users can continue to use the product. The product is no longer visible to the public or available to new users.  |

### To change product visibility

1. In your connected account, choose **Products**.
2. Choose the product.
3. Choose **Update Visibility** from the actions
   menu.
4. In the **Update Listing Visibility** dialog, choose **Public**, **Limited**, or **Restricted**.
5. Choose **Update**.

### Limited products in storefronts

Limited-visibility products can still be displayed in your storefronts. This is
useful for:

- Partner-exclusive products that should not appear on the public AWS
  Marketplace
- Pre-launch products shared with select buyers
- Internal tools available only to your organization's buyer
  community

To include limited products in a storefront:

1. Open the storefront's **Selection**
   tab.
2. Choose the **My Products** source tab.
3. Limited products from your connected account appear here alongside public
   products.
4. Choose the limited products to include.

### Notes

- Changing visibility does not affect existing agreements or active
  subscriptions.
- Limited products are accessible via direct URL even if not in a
  storefront.
- Visibility changes may take a few minutes to propagate across AWS
  Marketplace.

### Related topics

- Importing products
- [Managing tags and categories on products](#managing-tags-and-categories "#managing-tags-and-categories")
- Sharing products
