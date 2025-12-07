# Creating custom dimensions for private offers

Custom dimensions are pricing dimensions that you create specifically for private offers. Unlike standard dimensions that appear in your product's public offer, custom dimensions are only visible and available within private offers. This allows you to create specialized pricing structures for individual customers without affecting your public product listing.

Custom dimensions are particularly useful for express private offers when you need to offer pricing models that differ from your standard public offer dimensions.

## How custom dimensions work

Custom dimensions must be created within the private offer workflow in the AWS Marketplace Management Portal. The listing experience in the portal requires all dimensions to be associated with pricing on the public offer, which makes them publicly discoverable. To create dimensions that remain private, you must use the private offer creation workflow.

When you create a custom dimension through a private offer, the dimension is saved to your product and becomes available for use in any subsequent private offers or express private offers. You don't need to publish the private offer used to create the dimension—saving and exiting the workflow is sufficient to register the custom dimension with your product.

## Creating a custom dimension

To create a custom dimension, you create a draft private offer and define the dimension within that offer. The following procedure walks you through this process.

###### To create a custom dimension

1. Go to the private offer page on the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/offers "https://aws.amazon.com/marketplace/management/offers").
2. Select **Create private offer** to start a new private offer.
3. On the **Create offer** page, do the following:
   1. Choose **Direct private offer** as the offer type.
   2. Choose the SaaS product that you want to add the dimension to:
      - **SaaS contracts**
      - **SaaS contracts with pay-as-you-go**

   3. Choose **Next**.

4. On the **Provide offer information** page, do the following:
   1. Give your offer a name.
   2. For **Renewal**, choose **No, this isn't a renewal offer**.
   3. For **Offer expiration date**, set any future date for the offer expiration.

5. On the **Configure offer pricing and duration** page, do the following:
   1. Choose **Contract pricing with upfront payment** to keep the workflow simple.
   2. For **Contract duration**, specify `12` months for contract duration as placeholder.
   3. Keep the currency as **USD**.
   4. For **Purchasing options**, choose **Multiple dimensions per product** (if available).
   5. For **Product dimensions**, select **Add custom dimension**. Create contract custom dimensions for your express private offer. Enter a placeholder price of `$1`. When you're done, select **Add dimensions**.

6. Choose **Save and exit**.

## Verifying the custom dimension

After you save and exit the private offer workflow, verify that the custom dimension was created successfully.

###### To verify the custom dimension

1. On the private offer page, choose the **Request log** tab.
2. Refresh the page periodically to check the status of your request. Processing typically takes 5-15 minutes.
3. When the request shows a status of **Succeeded**, the custom dimension is available for use.
4. To confirm the dimension is accessible, create a new test offer and verify that the custom dimension appears in the available dimensions list.

The custom dimension is now available for selection in your express private offer configurations and any other private offers for this product.
