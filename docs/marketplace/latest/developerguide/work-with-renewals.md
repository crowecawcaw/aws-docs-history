

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Work with renewals
<a name="work-with-renewals"></a>

Renewals in AWS Marketplace enable sellers, including independent software vendors (ISVs) and channel partners, to seamlessly extend existing agreements with customers. During the renewal process, sellers have the option to adjust terms by creating a new offer. 

There are four types of renewals in AWS Marketplace:
+ **Agreement based offers**: Sellers can replace an existing agreement to adjust pricing, duration, terms, and renew an existing contract before it ends. An agreement based offer can be extended to the customer beyond the current agreement's end date, granting new entitlements, discounts, or payment schedules based on the customers needs. 

  This support applies to software as a service (SaaS) products, including those with contract and consumption-based pricing (CCP), whether they offer flexible payment options or not.
+ **Future dated offers**: Sellers can create future dated offers to start on a date in the future, and use them to pre-book renewals while existing terms are still ongoing. Once accepted by the customer, the agreement begins on a specified **future date, allowing to start after the current agreement ends.** 

  This support applies to software as a service (SaaS) products, including those with contract and consumption-based pricing (CCP), whether they offer flexible payment options or not.
+ **New private offer**: Sellers can [create a new private offer](work-with-private-offers.md#create-offer) with new terms (for AMI hourly, AMI annual, and SaaS pay-as-you-go subscriptions) that can be accepted anytime to renew an existing agreement.
+ **Auto-renewal**: Customers can enable auto-renewal for contract-based offers, public or private, so that a new agreement starts automatically when the current agreement ends.

**Topics**
+ [Replacement offers](#replacement-offers)
+ [Future dated agreements](#future-dated-offers)
+ [Resources](#renewals-resources)

## Replacement offers
<a name="replacement-offers"></a>

 As a seller, you can offer renewals by replacing an active agreement that was originally created when the customer accepted your public offer or private offer. Using a replacement offer, you can extend a new offer to the customer that goes beyond the current agreements end date, grant new entitlements, offer pricing discounts, adjust payment schedules, change the payment schedule, or change the end user license agreement (EULA). 

 You can use the Catalog API to [create a replacement offer](https://docs.aws.amazon.com/marketplace/latest/APIReference/work-with-private-offers.html#create-replacement-offer) (also known as an agreement-based offer) in AWS Marketplace for [supported product types](https://docs.aws.amazon.com/marketplace/latest/userguide/private-offers-upgrades-and-renewals.html#private-offers-upgrades-and-renewals-supported-products). You will need to provide the unique identifier (agreement ID) of the current agreement you wish to replace. You can find this agreement ID in the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management) under the Agreements section or by using the [SearchAgreements](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_SearchAgreements.html) API operation. 

 Once the customer accepts the replacement offer, their current agreement will be replaced with a new agreement that can extend beyond the previous end date. 

**Note**  
 You cannot create a replacement agreement that specifies a seller of record that differs from the original agreement. 

 For more information on replacement offers, see [Amending private offers in AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/userguide/private-offers-upgrades-and-renewals.html) in the *AWS Marketplace Seller Guide*. 

## Future dated agreements
<a name="future-dated-offers"></a>

 Future-dated agreements are created when a customer accepts a private offer with a future service start date. To facilitate advance booking of upcoming renewals in AWS Marketplace, ISVs and channel partners can create private offers that start the day after the current agreement ends rather than immediately upon acceptance. 

 To set the start date of a renewal agreement as the day after the end date of the current agreement, you can use the [Catalog API UpdateValidityTerms change type](https://docs.aws.amazon.com/marketplace/latest/APIReference/work-with-private-offers.html#update-validity-terms) on a private offer that has already been published. Sellers can choose a service start date up to three years in the future. 

 Customers can review the terms and conditions of the private offer and accept it before it takes effect. Accepting a private offer with a start date in the future does not replace the current agreement. Instead, it creates a renewal agreement that begins immediately after the previous agreement ends. 

 For more information on product types that support future dated offers and agreements, see [Creating future dated agreements](https://docs.aws.amazon.com/marketplace/latest/userguide/private-offers-seller-future-dated-private-offers-and-agreements.html#seller-creating-future-dated-agreements) in the *AWS Marketplace Seller Guide*. 

## Resources
<a name="renewals-resources"></a>
+ For end-to-end labs with working code examples, see: 
  + [Lab: Create a private offer (with a future service start date)](https://catalog.workshops.aws/mpseller/en-US/manage-offers-with-api/create-a-private-offer-with-a-future-service-start-date)
  +  [Lab: Create a replacement private offer](https://catalog.workshops.aws/mpseller/en-US/manage-offers-with-api/create-a-replacement-private-offer) 
+ For a video on creating replacement offers, see [Renew SaaS Contract Private Offers - AWS Marketplace](https://www.youtube.com/watch?v=KzcE0ZWyjzk) on YouTube.
+  For a video on creating future dated offers, see [Create an AWS Marketplace Future Dated Private Offer](https://www.youtube.com/watch?v=xLqQjXa2edo) on YouTube. 