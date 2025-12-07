# Supported product types for AWS Marketplace private offers

As an AWS Marketplace seller, you can use private offers to sell the following product types: Amazon Machine Images (AMIs), container, professional services, machine learning (ML), and
software as a service (SaaS) products. Private
offers are negotiated terms used to purchase a product from AWS Marketplace. This topic provides
information about private offers for AMI, container, SaaS, ML, and professional services
products.

For more information about private offers, see [Preparing a private offer for your AWS Marketplace product](private-offers-overview.md "private-offers-overview.md").

###### Topics

- [Private offers for AMI products](#supported-products-private-offers "#supported-products-private-offers")
- [Private offers for container products](#container-private-offers "#container-private-offers")
- [Private offers for professional services
  products](#proserv-private-offers "#proserv-private-offers")
- [Private offers for SaaS products](#saas-private-offers "#saas-private-offers")
- [Private offers for ML products](#ml-private-offers "#ml-private-offers")

## Private offers for AMI products

You can provide private offers pricing for AMI products.

The offer can be any custom duration for the following:

- AMI hourly or AMI hourly with annual private offers: up to 3 years (1,095 days). Only
  AMI hourly with annual private offers or AMI contracts support flexible payment
  scheduling.
- AMI contract private offers: up to 5 years (60 months)

For AMI contracts, private offers don't monitor usage.

Buyers can manually upgrade to new contract levels at any time. However, it is up to
the independent software vendor (ISV) to define contract tiers, enforce service
limitations, and advise buyers to manually upgrade their contracts with more units. Only
non-tiered pricing-based contracts support upgrades at this time. The contract duration of
the private offer can match the public product listing, or can be a custom duration in
months (up to 60).

License entitlements begin on the date the buyer accepts the private offer.

For AMI private offers with flexible payment schedules, you can set the number of annual
instance types agreed to in the contract, for the duration of the contract.

###### Note

Private offers are not available for monthly billing contracts.

## Private offers for container products

You can provide private offers pricing for container-based product contracts.

The offer can be any custom duration for the following:

- Container hourly or container hourly with long term private offers – Up to 3
  years (1,095 days). Only container hourly with long term private offers or container
  contracts support flexible payment scheduling.
- Container contract private offers – Up to 5 years (60 months)

For Container contracts, private offers don't monitor usage. Upgrading for container
contracts is only possible if you're using non-tiered pricing.

Buyers can manually upgrade to new contract levels at any time. However, the
independent software vendor (ISV) defines the contract tiers, enforces service
limitations, and advises buyers to manually upgrade their contracts with more units. Only
non-tiered pricing-based contracts support upgrades at this time. The contract duration of
the private offer can match the public product listing, or it can be a custom duration in
months (up to 60 months).

License entitlements begin on the date the buyer accepts the private offer. For container
private offers with flexible payment schedules, you can set the number of units agreed to in
the contract, for the duration of the contract. You can also define a custom hourly price for
those same units if the buyer uses more.

###### Note

Private offers are not available for monthly billing contracts.

## Private offers for professional services

products

All professional services product offerings are done through private offers. For more
information, see [Create private offers](proserv-getting-started.md#proserv-create-offer "proserv-getting-started.md#proserv-create-offer").

## Private offers for SaaS products

Software as a service (SaaS) private offer products can't change the pricing level for a
given pricing tier based on timing. For example, an offer can't charge $0.80/hour for three
months and then change pricing to $0.60/hour thereafter for the same pricing tier. For SaaS
contracts, private offers don't monitor usage.

Buyers can manually upgrade to new contract levels at any time. However, the independent
software vendor (ISV) defines contract tiers, enforces service limitations, and advises buyers
to manually upgrade to higher contract tiers when needed. The contract duration of the private
offer can match the public product listing, or it can be a custom duration in months (up to 60
months).

Express private offers are available for SaaS contracts and SaaS contracts with pay-as-you-go products. Complex opportunities that don't meet your predefined criteria are automatically routed to your sales team for manual processing. For more information, see [Express private offers](express-private-offers.md "express-private-offers.md").

## Private offers for ML products

Machine Learning (ML) private offer products give specific buyers a different price than
your publicly displayed price. The set of terms and agreement between you and the buyer in
private offers can differ from the one in the public offer or other private offers.

Private offers work in one of several ways:

- Hourly – Private offers can be an hourly rate
  that is different from the publicly displayed hourly rate. This hourly rate is perpetual
  because private offers for machine learning products don't expire. If a price change is
  needed in the future, the buyer must switch to the new private offer. Existing running
  instances or endpoints of the product are automatically billed the hourly rate set in the
  new accepted offer. Ensure you set it to the hourly rate for your product after any
  contract component within the private offer expires. Setting this hourly rate to $0 allows
  the buyer to use the product without your software fee indefinitely.
- Per inference – Private offers can have an
  inference rate that is different from the publicly displayed inference rate, if you've
  configured [inference pricing](machine-learning-pricing.md#ml-pricing-inference "machine-learning-pricing.md#ml-pricing-inference") for when your product is deployed as an endpoint.
- Contract – Private offers can be a contract with
  a fixed upfront fee for a specified number of days. The buyer is allowed to use an
  unlimited number of instances for the entire duration of the contract. At the end of the
  contract, any instances that continue to run are billed at the hourly rate that you set in
  the private offer. For example, you can create a contract with a fixed upfront fee for 365
  days of unlimited use. You also set an hourly rate for the private offer. When the buyer
  accepts this private offer, they pay that upfront fee. When the contract ends, any
  instances still running are billed at that hourly rate. If you’re offering a free private
  trial, ensure you set the correct hourly rate after the free trial period ends to avoid a
  free perpetual license.

You can create and extend multiple private offers to a single buyer. Buyers that you
extend the private offers to have the option to choose between the private offers and the
public offer. Buyers can only be subscribed to one offer at any given time. They can't be
subscribed to both a private offer and the public offer at the same time.

To create a private offer for a specific buyer for SageMaker products, see [Creating private offers for machine learning products](machine-learning-private-offers.md "machine-learning-private-offers.md").
