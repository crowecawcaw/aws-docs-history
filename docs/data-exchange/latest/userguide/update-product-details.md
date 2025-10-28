# Updating product and offer details in AWS Data Exchange

After you publish a product, you can use the AWS Data Exchange console to edit the product details.
You can also edit the product's public or custom offers and change the offer terms. When you
update your product's offer terms, subscribers with an active subscription keep their existing
offer terms as long as their subscription is active. Subscribers who have chosen auto-renewals
use the new offer terms.

Keep the following in mind when you update products:

- You can't remove or edit a subscription duration in your offers. This ensures that
  existing subscribers retain the ability to renew. If you no longer want to offer a
  specific subscription duration, you can unpublish your existing product and then publish a
  new product. For more information, see [Unpublish a product in AWS Data Exchange](unpublish-product.md "unpublish-product.md").
- You can't remove data sets from a product after it is published, regardless of how
  many subscribers have subscribed to your product.
- If you're updating the metered costs for a product that contains APIs:
  - A metered costs price decrease appears immediately on the product detail page for
    new subscribers.

  ###### Warning

  If you undo a price decrease for metered costs, you are increasing the price for
  metered costs. See the following point for more information about metered costs
  price increases.
  - A metered costs price increase will go into effect on the first day of the month,
    90 days after the price increase is submitted for existing subscribers OR upon renewal
    (whichever is sooner). The email is sent to existing subscribers when the price change
    is submitted. The price increase appears on the product detail page immediately for
    new subscribers.

  ###### Example

  You submit a metered costs price increase on May 10. Existing subscribers
  receive an email about the price change. The price increase goes into effect on
  September 1.

  ###### Warning

  You can't undo a price increase (because that action decreases the price) before
  the price increase goes into effect for existing subscribers.

###### To update a product, data set, or offer details

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. From the left navigation pane, under **Publish data**, choose
   **Products**.
3. From **Products**, choose the product you want to update. Make sure
   its status is **Published**.
4. From **Product details**:
   - If you're editing a public offer, choose the **Public offer**
     tab, choose **Edit**, and then follow the instructions to edit the
     product.
   - If you're editing a private offer, choose the **Custom offers**
     tab, choose the option button next to the private offer that you want to edit, choose
     **Edit**, and then follow the instructions to edit the
     product.
   1. For products containing APIs with metered costs, in **Metered costs –
      optional**, select the option button next to the **Type**
      of metered costs that you want to edit, and then choose
      **Edit**.
   2. In the **Edit metered cost** dialog box, update the
      **Price / unit** or **Description**.
   3. Choose **Update**.

   The updated metered costs appears under **Metered costs –
   optional**.

5. From **Data sets**, under **Sensitive information**,
   choose **Edit**, and then follow the instructions to edit the
   information.
6. From **Data evaluation**, update the data dictionary or sample by
   selecting the option button next to the data dictionary or sample
   **Name** and then choosing **Actions**. For more
   information, see [Updating a data dictionary in AWS Data Exchange](update-data-dictionary.md "update-data-dictionary.md") and [Updating a sample in AWS Data Exchange](update-sample.md "update-sample.md").
7. Configure your offer, depending on the offer type:
   - If your product is a public offer, from **Public offer**, choose
     **Edit**, and then follow the instructions to edit the public
     oﬀer.
   - If your product is a custom offer, from **Custom offers**, choose
     **Edit**, and then follow the instructions to edit the custom
     oﬀer.
   - If your product is a private offer, from **Private offers**,
     choose **Edit**, and then follow the instructions to edit the private
     offer.

8. Choose **Update**.
