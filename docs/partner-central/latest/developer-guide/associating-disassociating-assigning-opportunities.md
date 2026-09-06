

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Associating, disassociating and assigning opportunities
<a name="associating-disassociating-assigning-opportunities"></a>

 Opportunities can be associated or disassociated with Partner Solutions, AWS Products, AWS Marketplace Solutions, AWS Marketplace Products, AWS Marketplace Offers, and AWS Marketplace Offer Sets at any stage of the opportunity lifecycle. 

## Associating opportunities with other entities
<a name="associating-opportunities-with-other-entities"></a>

 The associated entities are retrieved from the `GetOpportunity` method within the `RelatedEntityIdentifiers` object. The `RelatedEntityIdentifiers` can be updated using `AssociateOpportunity`. Note that this field cannot be updated using the `UpdateOpportunity` or `CreateOpportunity` method. 

## Solutions
<a name="solutions"></a>

 Before an engagement with AWS is started using the `StartEngagementFromOpportunityTask` action, it is mandatory to associate at least one and up to ten Partner Solutions. An AWS Referral may or may not contain a Partner Solution. 

 To view your existing solutions, use the `ListSolutions` action. 

 Partners can create, update, and manage their solutions in the `Build` section on [AWS Partner Central](https://aws.amazon.com/partners/). 

**Important**  
To progress the opportunity stage to *Committed* or *Launched*, you must associate a valid solution or AWS Marketplace product listing with the opportunity.

**Note**  
Legacy Partner Solutions (`S-XXXX` identifiers) using the `Solutions` entity type are still supported. However, we recommend associating `AwsMarketplaceSolutions` entity type with the opportunities as the `Solution` entity type will be deprecated in the future.

## AWS products
<a name="aws-products"></a>

 Up to 20 AWS Products can be associated with an opportunity. To view a list of available AWS Products, use the list of [AWS Products hosted on GitHub](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/resources/aws_products.json). Association with AWS Products is exclusively done using the `AssociateOpportunity` action. To replace or remove a Product, use the `DisassociateOpportunity` action. 

## Solutions
<a name="aws-marketplace-solutions"></a>

 Opportunities can be associated with solutions from your seller account. Use the `AssociateOpportunity` action with `RelatedEntityType` set to `AwsMarketplaceSolutions`. 

 The entity must be in *Public* or *Limited* status. The service rejects draft or inactive entities. 

 For associating a solution, an ARN is required. The following example shows the ARN format for a solution:

```
arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Solution/soln-ab1c2de3fgh4i
```

 You can also associate solutions from a subsidiary AWS Marketplace account connected to your primary account through Partner Account Connection. Enter the full ARN, including the subsidiary account ID. 

 The `ListSolutions` action returns `AwsMarketplaceSolutionArn` on each solution summary, and supports filtering by ARN. 

## AWS Marketplace Products
<a name="aws-marketplace-products"></a>

 Opportunities can be associated with AWS Marketplace Products from your seller account. Use the `AssociateOpportunity` action with `RelatedEntityType` set to `AwsMarketplaceProducts`. 

 The entity must be in *Public* or *Limited* status. The service rejects draft or inactive entities. 

 For associating a product, an ARN is required. The ARN includes the product type (for example, `AmiProduct`, `SaaSProduct`, `ContainerProduct`). The following example shows the ARN format for an AMI product:

```
arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/AmiProduct/prod-ab1c2de3fgh4i
```

 You can also associate products from a subsidiary AWS Marketplace account connected to your primary account through Partner Account Connection. Enter the full ARN, including the subsidiary account ID. 

## AWS Marketplace offers and offer sets
<a name="aws-marketplace-offers-and-offer-sets"></a>

### AWS Marketplace offers
<a name="aws-marketplace-offers"></a>

 Opportunities can be tied to an AWS Marketplace Private Offer. To view available offers, use the ListEntities from the AWS Marketplace Catalog API. Currently, you can only associate offers from the AWS Marketplace Seller account linked to AWS Partner Central. 

 For associating a private offer ARN is required. Sample:

```
arn:aws:aws-marketplace:us-east-1:123123123123:AWSMarketplace/Offer/offer-dtn3example1tg
```

### AWS Marketplace offer sets
<a name="w2aac11b7b9c23c15b5"></a>

 Opportunities can also be associated with AWS Marketplace Offer Sets. Offer sets enable the grouping of multiple related marketplace offers together for comprehensive solution packaging. To view available offer sets, use the ListEntities from the AWS Marketplace Catalog API. 

 For associating an offer set, an ARN is required. Sample:

```
arn:aws:aws-marketplace:us-east-1:123123123123:AWSMarketplace/OfferSet/offerset-dtn3example1tg
```

 **Important:** An opportunity can be associated with either **one Offer** OR **one Offer Set**, but not both. Only one of these entity types can be associated with an opportunity at a time. 

## Disassociating opportunities from other entities
<a name="disassociating-opportunities-from-other-entities"></a>

 Use the `DisassociateOpportunity` action to unlink the opportunity from the following entity types:
+ Solutions
+ AWS Products
+ AWS Marketplace Solutions
+ AWS Marketplace Products
+ AWS Marketplace Offers
+ AWS Marketplace Offer Sets

 Depending on the state of the opportunity, different validation rules apply when you unlink these related objects. 

## Assigning opportunities
<a name="assigning-opportunities"></a>

 Use `AssignOpportunity` to change the opportunity's owner. You can set any of your Partner Central users to be the opportunity owner. 