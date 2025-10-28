# Unpublish a product in AWS Data Exchange

After your product is published in AWS Data Exchange, it's available for all to find and subscribe to,
based on the product's visibility settings. You can unpublish a product if you want to achieve
any of the following results:

- Remove a product you created for the [Publishing a new product in AWS Data Exchange](publishing-products.md "publishing-products.md") exercise.
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

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. From the left navigation pane, under **Publish data**, choose
   **Products**.
3. From **Products**, choose the product you want to remove. Make sure
   its status is **Published**.
4. From **Product overview**, choose **Unpublish**, and
   then follow the instructions to unpublish the product.

###### Important

This action can't be undone.
After you complete these steps, your product's status is **Unpublished**.
An unpublished product can't be published again, but you can create a new product (with a new
product ID) that has the same data sets, product details, and offer details.
