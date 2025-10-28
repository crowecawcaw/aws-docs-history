# Creating a SaaS free trial offer in AWS Marketplace

As an AWS Marketplace seller, you can create software as a service (SaaS) free trial offers in the AWS Marketplace Management Portal (AMMP).
Customers can evaluate software products before making large purchase decisions by using the
SaaS free trial option. After a customer subscribes to your product, your product performs
entitlement checks the same way it does for paid customers.

Each AWS account can only use a free trial for a SaaS product once. The free usage amount
granted during a free trial is not shared across linked accounts in an AWS organization.
Different linked accounts within a single main payer account can create their own individual
free trials.

###### Note

- If you use the Seller Data Delivery Service (SDDS), you receive an [Agreement
  details trial report](supplementary-reports.md "supplementary-reports.md") in your Amazon Simple Storage Service bucket. The report includes agreement
  details such as the subscriber name and ID, offer ID, and agreement start and end dates.
- Sellers also receive [Amazon Simple Notification Service (Amazon SNS)
  notifications](saas-notification.md "saas-notification.md") when new subscriptions are created. Amazon SNS notifications include an
  `isFreeTrialTermPresent` flag to identify free trial agreements.
- Also, customers who subscribe to your free trial are redirected to your
  registration URL with an additional token, `x-amzn-marketplace-offer-type=free-trial`.
  You can use the token to create a unique registration experience for the customers who use your free trials.

## Creating a SaaS free trial offer

Sellers can create SaaS free trial offers in the AWS Marketplace Management Portal (AMMP).

###### To create a SaaS free trial offer

1. Sign in to the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management").
2. On the AWS Marketplace Management Portal, choose either:
   - **Create or manage offers**
   - The **Offers** tab

3. On the **Offers** page, choose the **Public free
   trials** tab to review all SaaS free trials.
4. Choose **Create free trial offer**. Sellers can create one SaaS free
   trial offer per each public SaaS product.
5. For **Offer fundamentals**, select your **Product**
   and then choose **Next**.
6. In **Free trial settings**:
   1. Enter the number of days for your **Free trial length
      (days)**.

   The duration of free trials range from 7–90 days. 2. View the **Product dimensions** from your existing public
   offer.

   You can't change the product dimensions for SaaS subscription free trials.

   You can set the quantity limits per each dimension for SaaS contract free trials,
   and **Remove** or **Add dimensions**.

7. View the **Service agreement**.

For the EULA version, you can select either **Standard contract for
AWS Marketplace** or **Custom EULA**, and then choose **Review
offer**. 8. Verify and review all information for the offer, and then choose **Create
offer**.

## Cancelling a SaaS free trial offer

Sellers can cancel free trial offers at any time from the AWS Marketplace Management Portal.

To cancel a SaaS free trial offer

1. Sign in to the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management "https://aws.amazon.com/marketplace/management").
2. On the AWS Marketplace Management Portal, choose either:
   - **Create or manage offers**
   - The **Offers** tab

3. On the **Offers** page, select the offer.
4. Choose **View offer**.
5. Choose **Cancel offer**.

After an offer is canceled, active agreements for this offer are active until expiration.
New agreements for a canceled offer can't be created.
