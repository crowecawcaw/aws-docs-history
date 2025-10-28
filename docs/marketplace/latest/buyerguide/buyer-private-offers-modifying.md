# Modifying or unsubscribing from a private offer in AWS Marketplace

You can update from standard subscriptions to private offers, and you can also modify
certain existing private offers in AWS Marketplace. The process varies based on the agreement in
place.

For many subscriptions, when you shift from public pricing to a private offer, you
negotiate the offer with the ISV or your channel partner. After you accept the private offer,
your related existing subscription or subscriptions automatically move to the private offer
pricing model. This doesn't require any further action from you. Use the following guidance to
identify your scenario and the steps to start receiving the pricing for your private offer.

## Changing from

public to private offer pricing

After you accept the private offer, no further action is needed for the user that
accepted the offer. They are switched to the pricing, terms, and conditions defined in the
private offer. To switch to the pricing, terms, and conditions for the private offer, each
linked user using the product must accept the private offer. Any user that starts using the
product must also accept the private offer to get the pricing, terms, and conditions defined
in the private offer.

## Changing a SaaS contract –

upgrades and renewals

This section applies to software as a service (SaaS) contract and SaaS contract with
consumption products. If you have an active contract in place from a previous private offer
and you want to accept a new private offer for the same product, the seller can upgrade or
renew your existing agreement to modify the terms, pricing, or duration, or to renew your
existing contract before it ends. This will result in a new private offer for you to accept,
without needing to cancel your existing agreement first.

###### Note

Future-dated private offers are listed as **Early renewals**. For more
information, see [Future dated agreements and private offers in AWS Marketplace](private-offers-buyer-future-dated-private-offers-and-agreements.md "private-offers-buyer-future-dated-private-offers-and-agreements.md").

To accept an upgrade or renewal, you must be on invoicing terms. If you're not currently
on invoicing terms, submit a ticket to [AWS Customer Service](https://support.console.aws.amazon.com/support/home#/ "https://support.console.aws.amazon.com/support/home#/")
to change your payment method to invoicing.

If you don't want to switch to invoicing, then you can take either of the following
actions:

- Work with the product vendor and AWS Marketplace customer support team to cancel the current
  contract before accepting a new private offer for that product.
- Accept the offer on another AWS account.

## Modifying your contract quantities

If your active SaaS contract includes configurable upfront pricing terms, you can modify the quantity of units in your contract without needing a new private offer from your seller. This allows you to:

- Increase the number of units in your contract
- Scale your usage up based on business needs

###### To modify your current contract

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace "https://console.aws.amazon.com/marketplace").
2. Choose **Manage subscriptions**, then search for your product by name and choose it.
3. In the **Agreement** section, choose **Actions**.
4. From the dropdown menu, choose **View terms**.
5. On the subscription page, choose **Modify**.
6. In the **Pricing details and unit configuration** section, increase your entitlements by using the arrows. You can't reduce the entitlement counts below what you've already purchased.
7. The contract details and total price appear in the **Purchase details** section.
8. Review your changes and choose **Save changes**.

###### Note

Not all contracts support quantity modifications. The ability to modify depends on whether your contract includes [configurable upfront pricing terms](../APIReference/API_marketplace-agreements_ConfigurableUpfrontPricingTerm.md "../APIReference/API_marketplace-agreements_ConfigurableUpfrontPricingTerm.md"). If you don't see a modify option, contact your seller to discuss upgrade or renewal options.

Your contract end date remains the same when you modify quantities. You're adjusting the scale of your existing agreement rather than extending its duration.

## Changing

from a SaaS subscription to a SaaS contract

To change from a SaaS subscription to a SaaS contract, you must first unsubscribe from
the SaaS subscription. Then you accept the private offer for the SaaS contract. To view your
existing SaaS subscriptions, choose **Your Marketplace Software** in the
upper-right corner of the AWS Marketplace console.

## Changing from

an AMI contract to a new contract

If you have an Amazon Machine Image (AMI) contract in place from a previous private offer
and you want to accept a new private offer for the same product, you must do one of the
following:

- Wait for the current AMI contract to expire before accepting the new AMI
  contract.
- Work with the product vendor and the AWS Marketplace customer support team to terminate your
  current contract.
- Accept the private offer using a different AWS account from the one that has the
  contract.

## Changing from AMI

hourly to AMI annual

When you move from an AMI hourly subscription to an AMI annual subscription, the
subscription works similar to a voucher system. Each hour of AMI usage is offset by one unit
in the AMI annual subscription. When you purchase the annual subscription through a private
offer, all associated accounts that are subscribed to the product are automatically switched
to the pricing negotiated in the private offer. Linked accounts that start a subscription
after the private offer is in place must subscribe to the private offer when they
subscribe.

###### Note

The annual licenses on your previous offer are deactivated immediately upon acceptance of the
terms of the new offer. Work with the ISV to discuss compensation for the deactivated licenses and
how to proceed forward with the new offer.

## Changing from AMI

annual to AMI hourly

When your annual subscription expires, any linked accounts subscribed to the product are
automatically switched to the AMI hourly pricing. If an annual subscription is in place, the
linked account can't switch to an hourly subscription for that product without canceling the
subscription.
