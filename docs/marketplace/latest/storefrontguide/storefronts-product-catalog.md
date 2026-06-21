# Product catalog

Add products to your storefront and organize them with categories, badges, and tags.

## Importing products

You can add products to your storefront from the AWS Marketplace public catalog, from
your own seller account listings, or by creating custom entries.

### Product sources

| Source          | Description                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------- |
| AWS Marketplace | Browse and choose from publicly available AWS Marketplace<br>listings                          |
| My Listings     | Choose from your connected seller account's products, including<br>limited-visibility listings |
| Custom          | Manually create product entries or group listings                                              |

### To import products from the public marketplace

1.  Open the storefront and choose the **Selection** tab.
2.  Choose the **AWS marketplace** card from the marketplace cards row on the Selection tab.
3.  Browse or search for products. Use the search bar and the left-rail filter sections to narrow results. The following filter sections are available:

        * **TAGS FILTERS**
        * **AWS FILTERS**
        * **MY LISTINGS FILTERS**

    Use the **Show selected only** checkbox to display only products you have already chosen.

4.  For each product you want to add, choose **Use this product** on the product card.
5.  Selected products appear in your storefront catalog automatically.

### To import from your seller account

1. On the Selection tab, use the **MY LISTINGS FILTERS** section in the left rail to filter to your seller account products. This is a filter section, not a separate tab.
2. Your connected seller account's products are displayed, including
   limited-visibility listings that are not publicly searchable.
3. Choose **Use this product** on the product card for each product to include in your
   storefront.

### To create custom entries

1. Choose the **Custom** tab.
2. Choose **Add Product** to create a manual
   listing entry.
3. Fill in the product details (name, description, image URL, link).
4. Choose **Save**.

### Prerequisites

- To access **My Listings**, you must have a
  connected AWS Marketplace seller account. See Connecting your AWS Marketplace
  account.
- Products from the public marketplace are available without a seller
  account.

### Related topics

- [Bulk catalog import](#bulk-catalog-import "#bulk-catalog-import")
- Suggested products
- [Categories and badges](#categories-and-badges "#categories-and-badges")

## Bulk catalog import

You can import multiple products to your storefront at once using a CSV file. This is
useful when you need to add a large number of products or migrate an existing
catalog.

### CSV template

Download the CSV template from the Bulk Update panel on the Selection tab.

### To import products in bulk

1. Open the storefront and choose the **Selection** tab.
2. On the Selection tab, scroll to the **Bulk Update** panel and choose **Download template** to get the CSV.
3. After you complete the CSV, choose **Upload file**.
4. The system validates the CSV and displays a preview of products to
   import.
5. Review the preview and choose **Import**.

Imported products are added to your storefront catalog.

### CSV format requirements

- The supported format is CSV.
- First row must contain column headers matching the template
- Required columns vary by marketplace (refer to the downloaded
  template)
- Product identifiers must match existing marketplace listings
- For large datasets, split the data into multiple files.

### Error handling

If the CSV contains invalid rows:

- Valid rows are imported successfully.
- Invalid rows are listed in an error summary with the reason for
  failure.
- You can correct errors and re-import the failed rows.

### Related topics

- [Importing products](#importing-products "#importing-products")
- [Categories and badges](#categories-and-badges "#categories-and-badges")
- [Managing tags](#managing-tags "#managing-tags")

## Categories and badges

You can organize products in your storefront using categories and badges. Categories
group related products for navigation, and badges provide visual indicators that
highlight product attributes.

### Categories

Categories appear in the storefront's filter panel and help buyers navigate large
catalogs.

#### To create a category

1. Open the storefront and choose the **Selection** tab.
2. Choose **Manage Categories**.
3. Choose **Add Category**.
4. Enter the category **Name** and optional
   **Description**.
5. Choose **Save**.

#### To assign products to categories

1. Choose a product in the catalog.
2. In the product detail panel, choose **Categories**.
3. Choose one or more categories from the list.
4. Choose **Save**.

Products can belong to multiple categories.

### Badges

Badges are visual labels that appear on product tiles in the storefront. Use
badges to highlight attributes like "New," "Featured," "Best Value," or custom
labels.

#### To create a badge

1. Open the storefront and choose the **Selection** tab.
2. Choose **Manage Badges**.
3. Choose **Add Badge**.
4. Configure the badge:

   - **Label** - Text displayed on the
     badge
   - **Color** - Badge background
     color

5. Choose **Save**.

#### To assign badges to products

1. Choose a product in the catalog.
2. In the product detail panel, choose **Badges**.
3. Choose one or more badges to display on the product tile.
4. Choose **Save**.

### Related topics

- [Importing products](#importing-products "#importing-products")
- [Managing tags](#managing-tags "#managing-tags")

## Managing tags

Tags provide a flexible filtering system for your storefront. Buyers use tags to
narrow the product catalog by attributes such as category, use case, industry, or
deployment model.

### Tags tab structure

The Tags tab has two side-by-side sections, **Tags list** (with **Add Tag** and **Import**) and **Tags' categories list** (with **Add Category** and **Import**), plus a Tags and Categories relationship table at the bottom.

### To create a tag

1. Open the storefront and choose the **Tags**
   tab.
2. Choose **Add Tag**.
3. Enter the tag **Name**.
4. Choose **Save**.

### To assign tags to products

1. In the **Tags** tab, locate the tag you want
   to populate.
2. Drag products from the untagged product list into the tag container.
   Alternatively, choose the tag and choose products from the assignment
   dialog.
3. Products immediately appear under that tag in the storefront's filter
   panel.

### To edit a tag

Choose the inline pencil icon next to the tag name to edit it. Modify the **Name** or assigned products, then choose **Save**.

### To delete a tag

Choose the inline trash icon next to the tag to delete it. Products previously assigned to this tag remain in the catalog but are no longer associated with the deleted tag.

### Tag display in the storefront

- Tags appear in the storefront's filter sidebar.
- Buyers can choose one or multiple tags to filter the catalog.
- The order of tags in the filter panel is determined by drag-and-drop
  ordering. See [Drag-and-drop tag ordering](#drag-and-drop-ordering "#drag-and-drop-ordering").

### Related topics

- [Drag-and-drop tag ordering](#drag-and-drop-ordering "#drag-and-drop-ordering")
- [Categories and badges](#categories-and-badges "#categories-and-badges")

## Drag-and-drop tag ordering

You can control the order in which tags appear in the storefront's filter panel by
dragging and dropping tags into your preferred sequence.

### To reorder tags

1. Open the storefront and choose the **Tags**
   tab.
2. Choose and hold the drag handle (the six-dot icon on the left of a card), drag the card to the new position, then release.
3. The new order is saved automatically.

The System Tags row is pinned and cannot be reordered.

### How ordering affects the storefront

- Tags are displayed in the filter panel in the order you configure.
- The first tag in the list appears at the top of the filter panel.
- Buyers see tags in this exact order when browsing the storefront.

### Tips

- Place your most important or frequently used tags at the top.
- Group related tags together.
- Reordering does not affect product assignments. Products remain tagged
  regardless of tag order.

### Related topics

- [Managing tags](#managing-tags "#managing-tags")
- [Categories and badges](#categories-and-badges "#categories-and-badges")
