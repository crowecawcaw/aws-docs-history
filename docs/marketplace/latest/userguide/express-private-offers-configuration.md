# Express private offer configuration

Configuring express private offers involves establishing the necessary permissions, selecting appropriate rate card types, and setting global controls to manage your automated private offer generation process.

## Required permissions

To configure express private offers, sellers must have an active SaaS contract or SaaS contract with pay-as-you-go listing on AWS Marketplace. Additionally, sellers must complete the onboarding process for the **Request Private Offer** button feature and possess the right permissions for pricing configuration.

For express private offer configuration permissions, you can use the [AWSMarketplaceFullAccess](../../../aws-managed-policy/latest/reference/AWSMarketplaceFullAccess.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceFullAccess.md") or [AWSMarketplaceSellerFullAccess](../../../aws-managed-policy/latest/reference/AWSMarketplaceSellerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceSellerFullAccess.md") managed policy. You also can use the following IAM policy:

```
{
    "Version": "2012-10-17"		 	 	 ,
    "Statement": [{
            "Sid": "AWSMarketplaceChangeSetReadAccess",
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:DescribeChangeSet",
                "aws-marketplace:ListChangeSets"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AWSMarketplaceTokenManagement",
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:StartChangeSet"
            ],
            "Resource": [
                "arn:aws:aws-marketplace:*:*:AWSMarketplace/AgentTokenContainer/*",
                "arn:aws:aws-marketplace:*:*:AWSMarketplace/ChangeSet/*"
            ],
            "Condition": {
                "StringEquals": {
                    "catalog:ChangeType": [
                        "CreateAgentTokenContainer",
                        "ExpireToken"
                    ]
                }
            }
        },
        {
            "Sid": "AWSMarketplaceEpoConfigManagement",
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:StartChangeSet"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "catalog:ChangeType": [
                        "CreateExpressPrivateOfferConfiguration",
                        "DeleteExpressPrivateOfferConfiguration"
                    ]
                }
            }
        },
        {
            "Sid": "AWSMarketplaceEntityReadAccess",
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:ListEntities",
                "aws-marketplace:DescribeEntity"
            ],
            "Resource": "*"
        }
    ]
}
```

## Access express private offers

You can access express private offers from the **Offers** or **Products** tab on the AWS Marketplace Management Portal.

## Rate card types and implementation

Express private offers provide sellers with three rate card types that can be implemented individually or in specific combinations to create comprehensive pricing strategies.

**Dimension-Based Rate Cards**

Dimension-based rate cards allow sellers to implement granular discount structures based on specific product dimension quantities or usage levels. When configuring these cards, sellers can establish quantity tiers for each product dimension, with each tier containing a minimum threshold and its associated discount percentage. The system automatically manages quantities that fall outside configured tiers - applying 0% discount to quantities below the lowest tier or above the highest tier (though less than the seller specified global level TCV maximum) without requiring explicit configuration. For example, if a seller configures tiers starting at 1,000 units (5% discount) and 10,000 units (15% discount), purchases of 500 units would receive no discount, while purchases of 5,000 units would qualify for the 5% discount tier.

**TCV-Based Rate Cards**

Total Contract Value (TCV) based rate cards focus on the overall monetary value of customer contracts rather than individual dimension quantities. This approach enables sellers to incentivize larger total purchases through graduated discount tiers. The system applies only the highest qualified discount tier based on the total contract value. Similar to dimension-based cards, contracts falling below the minimum threshold or exceeding the maximum threshold receive no discount. However, it's crucial to note that when contract values exceed the global TCV maximum set in top-level controls, buyers are routed to a sales-assisted workflow rather than receiving a 0% discount offer.

**Buyer-Profile Based Rate Cards**

This most flexible rate card type allows sellers to implement sophisticated qualification criteria beyond simple quantity or value thresholds. Sellers provide natural language specifications describing their desired qualification strategy, which the system transforms into appropriate buyer questionnaires. The system supports up to five distinct qualifiers that can be used for both inclusive discounting and exclusionary filtering. For instance, sellers might offer additional discounts to specific industry segments or restrict offer access based on company size. While AWS doesn't verify buyer-provided responses, this mechanism enables precise market segmentation and targeted pricing strategies.

## Rate card combinations and discount calculations

Express private offers supports specific combinations of rate card types while preventing others to maintain pricing logic integrity. Sellers can combine either dimension-based or TCV-based rate cards with buyer-profile based qualifications, but cannot use dimension-based and TCV-based rate cards simultaneously as these represent fundamentally different pricing approaches that could create conflicts.

When multiple discounts apply through combined rate cards, the system uses multiplicative calculation. For example, if a customer qualifies for both a 10% TCV-based discount and a 5% buyer-profile discount, the final price would reflect a multiplicative combination (0.9 × 0.95 = 0.855)—a 14.5% discount--rather than a 15% reduction.

## Global controls and guardrails

Express private offers include overarching controls that serve as guardrails for all rate card configurations. These include a global TCV maximum threshold that determines overall offer eligibility and a maximum discount setting that caps the total discount possible through any combination of rate cards. These controls ensure that larger deals receive appropriate sales attention and that discounts remain within acceptable bounds. Both of these are configurations that a seller provides in their express private offer setup.

Sellers may also choose to offer no discounts by setting the top-level maximum discount to 0%.

## Additional configuration considerations

Sellers should note several important limitations and considerations when configuring rate cards. The consumption component within a CCP product cannot be discounted through express private offer rate cards and maintains public offer pricing. Duration-based discounting is not supported in the initial release, and buyer-profile qualifications cannot discriminate based on protected characteristics or conflict with other offer configurations. When implementing complex dimension rules through buyer-profile qualifications, sellers should provide extremely specific natural language instructions to ensure accurate system interpretation.
