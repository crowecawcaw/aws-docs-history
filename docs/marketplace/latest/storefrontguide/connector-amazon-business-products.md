

# Adding Amazon Business products and the Buy button
<a name="connector-amazon-business-products"></a>

After the connector shows **Connected**, import Amazon Business products into the bound storefront, choose a display template, turn on the Buy button, and publish.

## Importing and selecting products
<a name="connector-amazon-business-products-import"></a>

**United States catalog only**  
Product import supports the United States Amazon Business marketplace only. The import resolves ASINs against the US catalog. An ASIN that isn't available in the US catalog returns an error, even if it's available in another Amazon Business marketplace.

**To import Amazon Business products**

1. Open your storefront's **Inventory**. On the **Offerings** tab, choose the **Amazon Business** catalog, and then choose **Import**. If your navigation uses **Selection**, choose **Selection** > **Amazon Business** > **Import** instead.

1. If prompted, choose the connected Amazon Business source.

1. In **Import from source**, drag a CSV file into the upload area, or choose the area to select a file. The CSV uses the following columns:


<table>
<thead>
  <tr><th>Column</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td> <code>asin</code> </td><td>Required. The Amazon product identifier (ASIN), one product per row.</td></tr>
  <tr><td> <code>selected</code> </td><td> <code>true</code> for products that you want visible on the storefront. <code>false</code> imports a product without selecting it.</td></tr>
  <tr><td> <code>group</code> </td><td>Optional. Product group. It must match a group that already exists in the storefront. If it doesn't, the product goes to the default group.</td></tr>
  <tr><td> <code>tags</code> </td><td>Optional. Comma-separated tags. Enclose a field that contains commas in quotation marks.</td></tr>
</tbody>
</table>


   For example:

   ```
   asin,selected,group,tags
   B0EXAMPLE01,true,Networking,"switch,office"
   ```

1. Review the number of unique ASINs that are ready to import, and then choose **Import**. Resolve any reported import issues. When the import finishes, a confirmation message shows the number of imported listings.

1. Review the imported products. For any product that isn't already selected, choose **Use this product**.

## Choosing the display template
<a name="connector-amazon-business-products-design"></a>

**To choose the display template**

1. Open **Design**.

1. For **Theme**, choose **Storefront Pro**.

1. For **Layout**, choose **Website** for a standalone storefront website.

1. Choose **Save**.

Storefront Pro supports Amazon Business price comparisons, quantity tiers, and other offers when Amazon Business supplies them. If Storefront Pro isn't available, contact [awsmp-storefront-support@amazon.com](mailto:awsmp-storefront-support@amazon.com) for an available template with equivalent product detail support.

## Turning on the Buy button and publishing
<a name="connector-amazon-business-products-publish"></a>

**To turn on the Buy button and publish the storefront**

1. Open **Checkout & Deployment** for the storefront that you bound to the Amazon Business connector.

1. Configure the following:


<table>
<thead>
  <tr><th>Setting</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td> <b>Buy on Amazon Business button</b> </td><td> <b>Enable</b> </td></tr>
  <tr><td> <b>Buy on Amazon button label</b> </td><td> <b>Buy on Amazon Business</b>, or your own label of up to 40 characters. If you leave it empty, the button uses <i>Buy on Amazon</i>.</td></tr>
</tbody>
</table>


1. Check **Notification receivers**. Publishing requires at least one receiver. If none exists, choose **Add new notification receiver**, and then enter the following:


<table>
<thead>
  <tr><th>Setting</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td> <b>Owner name</b> </td><td>Your notification contact's name</td></tr>
  <tr><td> <b>Owner email</b> </td><td>Your notification contact's email address</td></tr>
  <tr><td> <b>Custom email</b> </td><td> <b>No</b>, to use the standard sender</td></tr>
</tbody>
</table>


1. Choose **Add**, and confirm that the receiver appears.

1. Under **Deployment status**, check the **Domain label** and the displayed storefront address. For a new storefront, enter an available label.

1. Turn on **Deploy your storefront**, and then choose **Save**.

1. To view the published storefront, choose **Open link**.

Your storefront is online at the displayed address, the selected products appear, and the Buy button uses your label. If you use single sign-on (SSO), the full buyer SSO flow works only after you activate Amazon Business SSO.

## Related topics
<a name="connector-amazon-business-products-related"></a>
+  [Bulk catalog import](storefronts-product-catalog.md#bulk-catalog-import) 
+  [Design and layout](storefronts-design-layout.md) 
+  [Deployment](storefronts-creating-deploying.md#deployment) 
+  [Verifying and troubleshooting the Amazon Business connector](connector-amazon-business-verify.md) 