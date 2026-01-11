# Unpublish a product in AWS Data Exchange

After your product is published in AWS Data Exchange, it's available for all to find and subscribe to,
based on the product's visibility settings. You can unpublish a product if you want to achieve
any of the following results:

- Clean up your resources.
- Remove a product from the publicly listed products on AWS Data Exchange.
- Stop subscribers from auto-renewing your product.
  Keep the following in mind when you unpublish a product:

- You can unpublish a product whenever you want.
- If you unpublish a product, it is no longer visible in the AWS Data Exchange catalog or on
  AWS Marketplace.
- Subscribers with an active subscription maintain access to the data product until the
  term of their subscription expires.
- Active subscriptions that expire after you have unpublished your product are not
  renewed, even if the subscriber has enabled auto-renewal.
- Existing subscribers can still view the product details until their subscription
  expires.

###### To unpublish a product

1. Sign in to your seller account in the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/").
2. Go to the **Data Products** page and select your product.
3. Choose **Request changes**, select **Update product visibilty**, and then select **Restricted**.
4. Review your changes and choose **Submit**.

###### Important

This action can't be undone.
After you complete these steps, your product's status is **Restricted**.
A restricted product can't be published again, but you can create a new product (with a new
product ID) that has the same data sets, product details, and offer details.
