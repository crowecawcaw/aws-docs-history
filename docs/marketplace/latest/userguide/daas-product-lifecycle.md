

# DaaS product lifecycle in AWS Marketplace

When you create a Data as a Service (DaaS) product in AWS Marketplace, it's first published with limited visibility, so that only your account and accounts you allowlist can see it. This lets you test the whole buyer journey before anyone else can subscribe. When you're ready, you request that the product be made public. After the product is public, buyers can find it in the AWS Marketplace catalog and subscribe.

A DaaS product has one of the following statuses:
+ **Staging** – The product is incomplete, and you're still adding information. The first time you choose **Save and exit**, AWS Marketplace creates an unpublished product with the information from the steps that you completed. From this status, you can keep adding information or change details that you already submitted.
+ **Limited** – Your product moves to **Limited** when you start **Step 3: Procurement configuration** in AWS Partner Central, before you create its public offer. It has a detail page that only your account and the accounts you allowlisted can open. Use this status to test your product, including your fulfillment URL and your subscription events. To let another account test, add its AWS account ID to your allowlist with an **Update allowlist** change request. Paid dimensions use a reduced test price while the product is **Limited**. For more information, see [Creating the public offer](daas-create-product.md#daas-create-product-offer).
+ **Public** – The product is visible to all buyers, and they can subscribe to it. To move a product from **Limited** to **Public**, you submit an **Update visibility** change request. At this point, you also set the prices of your pricing dimensions. The AWS Marketplace Seller Operations team then reviews your product against AWS Marketplace policies and might ask you to make changes or answer questions by email. After the team approves the request, the product status changes to **Public**.
+ **Restricted** – The product no longer accepts new buyers. To stop new buyers from subscribing, submit an **Update visibility** change request to restrict the product. Existing buyers can keep using the product, but it's no longer visible to the public or available to new buyers.

You can update your product while it has the **Staging**, **Limited**, or **Public** status. For more information, see [Update product information](saas-product-settings.md#update-product-information).

For help with a product, contact the AWS Marketplace Seller Operations team on the [AWS Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1).