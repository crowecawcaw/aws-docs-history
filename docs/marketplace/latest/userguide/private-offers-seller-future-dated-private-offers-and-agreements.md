# Creating future

dated agreements for private offers

As an AWS Marketplace seller, you can use future dated agreements to sell a product that a buyer
will receive on a _predetermined future date_. In a typical
AWS Marketplace transaction, the buyer receives the product license or entitlement _immediately_ after the offer is accepted or the agreement is created. In
contrast, with a future dated agreement (FDA), the buyer receives the product license or
entitlement on a _predetermined future date_. FDA can be used to
setup renewals for existing transactions with the buyer. FDA is supported for software as a
service (SaaS) products for contract and contracts with consumption (CCP) pricing, with and
without flexible payments. The following sections provide information about working with future
dated agreements.

With FDA, you can close transactions with buyers when they choose instead of when the buyer
wants to begin product usage. You can use FDA to dependently perform the following actions for
transactions on AWS Marketplace:

- Book (buyer accepts the offer) the deal based on sales needs.
- Charge the buyer based on your finance or accounting needs.
- Provide buyer access to the product, such as activating a license or entitlement, based on
  buyer needs.
  A buyer can accept an FDA offer, even while their current agreement is active, if:

- The FDA start date occurs after their existing agreement ends.
- Auto-renewal is disabled before accepting the FDA.

###### Important

Once an FDA is accepted, auto-renewal cannot be re-enabled.

- The service dates don't overlap with any other accepted FDAs.

###### Topics

- [Considerations for future data agreements](#fda-considerations "#fda-considerations")
- [Creating future dated
  agreements](#seller-creating-future-dated-agreements "#seller-creating-future-dated-agreements")
- [Using an
  installment plan with future dated agreements](#seller-using-flexible-payment-scheduler-with-future-dated-agreements "#seller-using-flexible-payment-scheduler-with-future-dated-agreements")
- [Receiving
  notifications for future dated agreements](#seller-receiving-notifications-for-future-dated-agreements "#seller-receiving-notifications-for-future-dated-agreements")
- [Using future dated
  agreements with reselling for Channel Partner private offers](#seller-using-future-dated-agreements-with-reselling "#seller-using-future-dated-agreements-with-reselling")

## Considerations for future data agreements

When you use future dated agreements, keep the following dates in mind :

**Agreement sign date**

The date when the buyer accepts the offer and when the agreement is created.

**Agreement start date**

The date when the buyer's license or entitlement to the product is activated and the buyer
can begin using the product.

**Agreement end date**

The date when the agreement ends. The agreement and the buyer's license or entitlement
expire on this date.

###### Note

The contract term specified in your end user license agreement, order form, or other
contract with a subscriber will control if there's a conflict with the term specified in the
subscriber's AWS Marketplace invoice.

## Creating future dated

agreements

The seller of record sets the agreement start date when generating a private offer with a
future start date. Buyers can't change the start date, but they can review the start date before
accepting the private offer in AWS Marketplace.

###### To create a private offer with a future start date

1. When creating a private offer, choose **Start at a future date** under
   **Contract duration**.
2. In the **Service dates** section, enter the **Service start
   date** and **Service end date**. The service start date you choose
   here will be the agreement start date of your future dated agreement when the buyer accepts the
   offer.

###### Note

To use an FDA for renewals, the service start date must be one or more days after the end
date of the agreement you want to renew. For example, if agreement end date is 12/31/2024, you
should set the service start date to be 1/1/2025.

Sellers can choose a service start date up to 3 years in the future.

## Using an

installment plan with future dated agreements

Using an installment plan with an FDA, you can set up payments for purchases to occur at any
time between the agreement sign date and the agreement end date. This includes payments before
and after the agreement start date.

The seller of record chooses private offer payment dates and amounts. For more details about
setting up an installment plan, see [Creating an installment plan for a private offer](installment-plans.md#creating-a-payment-schedule "installment-plans.md#creating-a-payment-schedule").

## Receiving

notifications for future dated agreements

You receive [email
notifications](email-notifications.md "email-notifications.md") to your designated root account for the following actions taken on your
future dated agreements:

- Offer acceptance/agreement creation (agreement sign date)
- Upon license or entitlement activation (agreement start date)
- Reminders for agreements expiring 30, 60, or 90 days in advance
- Agreement expiration (agreement end date)
- Upon an agreement amendment or replacement

###### Note

All existing Amazon Simple Notification Service (Amazon SNS) notifications for SaaS also work for FDA. For FDAs, both
Amazon SNS topics are initiated on the agreement start date (and not agreement sign date). For
more information, see [Amazon SNS notifications for SaaS products](saas-notification.md "saas-notification.md").

## Using future dated

agreements with reselling for Channel Partner private offers

Manufacturers and resellers can use future dated agreements for AWS Marketplace Channel Partner
private offers.

###### As the manufacturer:

- Similar to standard AWS Marketplace Channel Partner Private Offers (CPPOs), manufacturers must
  authorize AWS Marketplace Channel Partners to create CPPOs with a future start date by extending a resale
  authorization to them.

To learn how to create a resale authorization, follow the steps on the [Creating a selling authorization for an AWS Marketplace Channel Partner as an ISV](channel-partner-isv-info.md "channel-partner-isv-info.md") page.

- When creating a resale authorization, manufacturers can optionally choose to specify a
  maximum allowed service start date. This will be the maximum service start date the AWS Marketplace
  Channel Partner can specify when creating the corresponding AWS Marketplace Channel Partner private
  offer.

###### Note

If the manufacturer doesn't specify a maximum date, the AWS Marketplace Channel Partner can specify
any future service date up to 3 years in the future.

###### As the reseller:

- For resellers and Channel Partners, the steps for creating a future dated Channel Partner
  private offer and an ordinary future dated private offer are the same, with one key difference.
  The agreement start date resellers can specify must be earlier than what is specified as the
  maximum allowed service start date in the resale authorization by the manufacturer.
- To learn how to create a Channel Partner private offer, see [Creating private offers as an AWS Marketplace Channel Partner](channel-partner-offers.md "channel-partner-offers.md").
