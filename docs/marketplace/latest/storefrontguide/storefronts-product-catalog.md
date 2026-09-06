

# Product catalog
<a name="storefronts-product-catalog"></a>

Add products to your storefront and organize them with categories, badges, and tags.

## Importing products
<a name="importing-products"></a>

You can add products to your storefront from the AWS Marketplace public catalog, from your own seller account listings, or by creating custom entries.

### Product sources
<a name="importing-products-sources"></a>


| Source | Description | 
| --- | --- | 
| AWS Marketplace | Browse and choose from publicly available AWS Marketplace listings | 
| My Listings | Choose from your connected seller account's products, including limited-visibility listings | 
| Custom | Manually create product entries or group listings | 

### To import products from the public marketplace
<a name="importing-products-public"></a>

1. Open the storefront and choose the **Selection** tab.

1. Choose the **AWS marketplace** card from the marketplace cards row on the Selection tab.

1. Browse or search for products. Use the search bar and the left-rail filter sections to narrow results. The following filter sections are available:
   + **TAGS FILTERS**
   + **AWS FILTERS**
   + **MY LISTINGS FILTERS**

   Use the **Show selected only** checkbox to display only products you have already chosen.

1. For each product you want to add, choose **Use this product** on the product card.

1. Selected products appear in your storefront catalog automatically.

### To import from your seller account
<a name="importing-products-seller"></a>

1. On the Selection tab, use the **MY LISTINGS FILTERS** section in the left rail to filter to your seller account products. This is a filter section, not a separate tab.

1. Your connected seller account's products are displayed, including limited-visibility listings that are not publicly searchable.

1. Choose **Use this product** on the product card for each product to include in your storefront.

### To create custom entries
<a name="importing-products-custom"></a>

1. Choose the **Custom** tab.

1. Choose **Add Product** to create a manual listing entry.

1. Fill in the product details (name, description, image URL, link).

1. Choose **Save**.

### Prerequisites
<a name="importing-products-prerequisites"></a>
+ To access **My Listings**, you must have a connected AWS Marketplace seller account. See Connecting your AWS Marketplace account.
+ Products from the public marketplace are available without a seller account.

### Related topics
<a name="importing-products-related"></a>
+ [Bulk catalog import](#bulk-catalog-import)
+ Suggested products
+ [Categories and badges](#categories-and-badges)

## Bulk catalog import
<a name="bulk-catalog-import"></a>

You can import multiple products to your storefront at once using a CSV file. This is useful when you need to add a large number of products or migrate an existing catalog.

### CSV template
<a name="bulk-catalog-import-template"></a>

Download the CSV template from the Bulk Update panel on the Selection tab.

### To import products in bulk
<a name="bulk-catalog-import-import"></a>

1. Open the storefront and choose the **Selection** tab.

1. On the Selection tab, scroll to the **Bulk Update** panel and choose **Download template** to get the CSV.

1. After you complete the CSV, choose **Upload file**.

1. The system validates the CSV and displays a preview of products to import.

1. Review the preview and choose **Import**.

Imported products are added to your storefront catalog.

### CSV format requirements
<a name="bulk-catalog-import-format"></a>
+ The supported format is CSV.
+ First row must contain column headers matching the template
+ Required columns vary by marketplace (refer to the downloaded template)
+ Product identifiers must match existing marketplace listings
+ For large datasets, split the data into multiple files.

### Error handling
<a name="bulk-catalog-import-errors"></a>

If the CSV contains invalid rows:
+ Valid rows are imported successfully.
+ Invalid rows are listed in an error summary with the reason for failure.
+ You can correct errors and re-import the failed rows.

### Related topics
<a name="bulk-catalog-import-related"></a>
+ [Importing products](#importing-products)
+ [Categories and badges](#categories-and-badges)
+ [Managing tags](#managing-tags)

## Categories and badges
<a name="categories-and-badges"></a>

You can organize products in your storefront using categories and badges. Categories group related products for navigation, and badges provide visual indicators that highlight product attributes.

### Categories
<a name="categories-and-badges-categories"></a>

Categories appear in the storefront's filter panel and help buyers navigate large catalogs.

#### To create a category
<a name="categories-and-badges-create-category"></a>

1. Open the storefront and choose the **Selection** tab.

1. Choose **Manage Categories**.

1. Choose **Add Category**.

1. Enter the category **Name** and optional **Description**.

1. Choose **Save**.

#### To assign products to categories
<a name="categories-and-badges-assign-category"></a>

1. Choose a product in the catalog.

1. In the product detail panel, choose **Categories**.

1. Choose one or more categories from the list.

1. Choose **Save**.

Products can belong to multiple categories.

### Badges
<a name="categories-and-badges-badges"></a>

Badges are visual labels that appear on product tiles in the storefront. Use badges to highlight attributes like "New," "Featured," "Best Value," or custom labels.

#### To create a badge
<a name="categories-and-badges-create-badge"></a>

1. Open the storefront and choose the **Selection** tab.

1. Choose **Manage Badges**.

1. Choose **Add Badge**.

1. Configure the badge:
   + **Label** - Text displayed on the badge
   + **Color** - Badge background color

1. Choose **Save**.

#### To assign badges to products
<a name="categories-and-badges-assign-badge"></a>

1. Choose a product in the catalog.

1. In the product detail panel, choose **Badges**.

1. Choose one or more badges to display on the product tile.

1. Choose **Save**.

### Related topics
<a name="categories-and-badges-related"></a>
+ [Importing products](#importing-products)
+ [Managing tags](#managing-tags)

## Managing tags
<a name="managing-tags"></a>

Tags provide a flexible filtering system for your storefront. Buyers use tags to narrow the product catalog by attributes such as category, use case, industry, or deployment model.

### Tags tab structure
<a name="managing-tags-structure"></a>

The Tags tab has two side-by-side sections, **Tags list** (with **Add Tag** and **Import**) and **Tags' categories list** (with **Add Category** and **Import**), plus a Tags and Categories relationship table at the bottom.

### To create a tag
<a name="managing-tags-create"></a>

1. Open the storefront and choose the **Tags** tab.

1. Choose **Add Tag**.

1. Enter the tag **Name**.

1. Choose **Save**.

### To assign tags to products
<a name="managing-tags-assign"></a>

1. In the **Tags** tab, locate the tag you want to populate.

1. Drag products from the untagged product list into the tag container. Alternatively, choose the tag and choose products from the assignment dialog.

1. Products immediately appear under that tag in the storefront's filter panel.

### To edit a tag
<a name="managing-tags-edit"></a>

Choose the inline pencil icon next to the tag name to edit it. Modify the **Name** or assigned products, then choose **Save**.

### To delete a tag
<a name="managing-tags-delete"></a>

Choose the inline trash icon next to the tag to delete it. Products previously assigned to this tag remain in the catalog but are no longer associated with the deleted tag.

### Tag display in the storefront
<a name="managing-tags-display"></a>
+ Tags appear in the storefront's filter sidebar.
+ Buyers can choose one or multiple tags to filter the catalog.
+ The order of tags in the filter panel is determined by drag-and-drop ordering. See [Drag-and-drop tag ordering](#drag-and-drop-ordering).

### Related topics
<a name="managing-tags-related"></a>
+ [Drag-and-drop tag ordering](#drag-and-drop-ordering)
+ [Categories and badges](#categories-and-badges)

## Drag-and-drop tag ordering
<a name="drag-and-drop-ordering"></a>

You can control the order in which tags appear in the storefront's filter panel by dragging and dropping tags into your preferred sequence.

### To reorder tags
<a name="drag-and-drop-ordering-reorder"></a>

1. Open the storefront and choose the **Tags** tab.

1. Choose and hold the drag handle (the six-dot icon on the left of a card), drag the card to the new position, then release.

1. The new order is saved automatically.

The System Tags row is pinned and cannot be reordered.

### How ordering affects the storefront
<a name="drag-and-drop-ordering-affects"></a>
+ Tags are displayed in the filter panel in the order you configure.
+ The first tag in the list appears at the top of the filter panel.
+ Buyers see tags in this exact order when browsing the storefront.

### Tips
<a name="drag-and-drop-ordering-tips"></a>
+ Place your most important or frequently used tags at the top.
+ Group related tags together.
+ Reordering does not affect product assignments. Products remain tagged regardless of tag order.

### Related topics
<a name="drag-and-drop-ordering-related"></a>
+ [Managing tags](#managing-tags)
+ [Categories and badges](#categories-and-badges)