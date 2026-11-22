

# Removing a product from AWS Marketplace

After you publish your product, you can remove it from AWS Marketplace. This is also referred to as *sunsetting*. To remove a product, submit a request to change its visibility to **Restricted**. You can also provide a replacement product ID if you're replacing the current product with a new one.

After you request product removal, new customers can't subscribe to the product. You must support any existing customers for a minimum of 90 days.

**Note**  
You can't delete restricted products from AWS Partner Central. The portal retains them as part of the account's publication history.

We process requests for product removal from AWS Marketplace with the following conditions: 
+ The product is removed from AWS Marketplace search, browse, and other discovery tools. Any **Subscribe** button or functionality is disabled, and messaging on the page clearly indicates the product is no longer available. The product detail page is still accessible using the URL and might be indexed in public search engines. 
+ For the requirements for continuing support for removed products, see [ Terms and Conditions for AWS Marketplace Sellers](https://aws.amazon.com/marketplace/management/terms). 
+ AWS Marketplace contacts current buyers through an email message informing them of the product removal, reasons for the removal, and to provide seller contact information. 
+ Current buyers *do* retain access to the software until they cancel their subscription or their contract ends. They can't renew their contracts.

**To remove a product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose **Edit visibility**.

1. In the **Update listing visibility** dialog box, under **Change to**, choose **Restricted**.

   If **Restricted** is the only choice, the dialog box shows it without options to select.

1. (Optional) For **Replacement product ID**, enter the ID of the product that replaces this one.

   Use `prod-` followed by 13 or 25 letters and numbers, or a UUID. Existing subscribers keep access until their contracts end, and then move to the replacement product. If you leave this field blank, existing subscribers keep access to this product, but they can't renew their contracts.

1. Choose **Update visibility**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name.

After the request succeeds, the product stays on the **Products and services** page, and its **Visibility** is **Restricted**.

There's no waiting period. To make a **Restricted** product available again, choose **Edit visibility**, choose **Public**, and then choose **Update visibility**. AWS Marketplace might review the request before the product is **Public** again.

If you have questions about product removals, contact the AWS Marketplace Seller Operations team on the [AWS Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1).