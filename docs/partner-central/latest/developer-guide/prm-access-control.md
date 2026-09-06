

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Access for the Revenue Measurement API
<a name="prm-access-control"></a>

Access control and permissions are managed by AWS Identity and Access Management (IAM). This section provides guidance for configuring the necessary permissions to interact with the Revenue Measurement API, including the permissions required to list AWS Marketplace entities.

## Prerequisites
<a name="prm-prerequisites"></a>

Before configuring permissions, ensure that your AWS account is linked to Partner Central and that you created the necessary IAM roles and users. For more information, see [Setup and Authentication](https://docs.aws.amazon.com/partner-central/latest/APIReference/setup-authentication.html).

## Using AWS managed policies
<a name="prm-using-aws-managed-policies"></a>

AWS provides managed policies that grant the required permissions to interact with the Revenue Measurement API. Two managed policies are available depending on your persona:
+ **Partners** — attach the `AWSPartnerCentralRevenueAttributionManagement` policy to your IAM identities.
+ **Customers** — attach the `AWSRevenueAttributionManagement` policy to your IAM identities.

For more information, see [AWS managed policies for AWS Partner Central users](https://docs.aws.amazon.com/partner-central/latest/getting-started/managed-policies.html).

### AWSPartnerCentralRevenueAttributionManagement policy
<a name="prm-partner-facing-policy"></a>

This policy provides necessary access for revenue attribution management activities for AWS accounts registered with AWS Partner Central.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RevenueMeasurementCreation",
            "Effect": "Allow",
            "Action": [
                "partnercentral:CreateRevenueAttribution",
                "partnercentral:CreateMarketplaceRevenueShare",
                "partnercentral:CreateMarketplaceRevenueShareAllocation"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "partnercentral:Catalog": [
                        "AWS",
                        "Sandbox"
                    ]
                }
            }
        },
        {
            "Sid": "RevenueMeasurementListing",
            "Effect": "Allow",
            "Action": [
                "partnercentral:ListRevenueAttributions",
                "partnercentral:ListRevenueAttributionAllocations",
                "partnercentral:ListMarketplaceRevenueShares",
                "partnercentral:ListMarketplaceRevenueShareAllocations"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "partnercentral:Catalog": [
                        "AWS",
                        "Sandbox"
                    ]
                }
            }
        },
        {
            "Sid": "RevenueAttributionManagement",
            "Effect": "Allow",
            "Action": [
                "partnercentral:GetRevenueAttribution",
                "partnercentral:UpdateRevenueAttribution",
                "partnercentral:GetRevenueAttributionAllocation",
                "partnercentral:StartRevenueAttributionAllocationsTask",
                "partnercentral:GetRevenueAttributionAllocationsTask"
            ],
            "Resource": "arn:aws:partnercentral:*:*:catalog/*/revenue-attribution/*",
            "Condition": {
                "StringEquals": {
                    "partnercentral:Catalog": [
                        "AWS",
                        "Sandbox"
                    ]
                }
            }
        },
        {
            "Sid": "MarketplaceRevenueShareManagement",
            "Effect": "Allow",
            "Action": [
                "partnercentral:GetMarketplaceRevenueShare",
                "partnercentral:GetMarketplaceRevenueShareAllocation",
                "partnercentral:UpdateMarketplaceRevenueShareAllocation"
            ],
            "Resource": "arn:aws:partnercentral:*:*:catalog/*/marketplace-revenue-share/*",
            "Condition": {
                "StringEquals": {
                    "partnercentral:Catalog": [
                        "AWS",
                        "Sandbox"
                    ]
                }
            }
        },
        {
            "Sid": "TaggingAccess",
            "Effect": "Allow",
            "Action": [
                "partnercentral:TagResource",
                "partnercentral:UntagResource",
                "partnercentral:ListTagsForResource"
            ],
            "Resource": [
                "arn:aws:partnercentral:*:*:catalog/*/revenue-attribution/*",
                "arn:aws:partnercentral:*:*:catalog/*/marketplace-revenue-share/*"
            ],
            "Condition": {
                "StringEquals": {
                    "partnercentral:Catalog": [
                        "AWS",
                        "Sandbox"
                    ]
                }
            }
        },
        {
            "Sid": "OpportunityAccess",
            "Effect": "Allow",
            "Action": [
                "partnercentral:ListOpportunities",
                "partnercentral:GetOpportunity"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "partnercentral:Catalog": [
                        "AWS",
                        "Sandbox"
                    ]
                }
            }
        },
        {
            "Sid": "PartnerResourceAccess",
            "Effect": "Allow",
            "Action": [
                "partnercentral:ListPartners",
                "partnercentral:GetPartner"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "partnercentral:Catalog": [
                        "AWS",
                        "Sandbox"
                    ]
                }
            }
        },
        {
            "Sid": "ListingAWSMarketplaceEntities",
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:ListEntities"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AWSMarketplaceEntityAccess",
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:DescribeEntity"
            ],
            "Resource": [
                "arn:aws:aws-marketplace:*:*:AWSMarketplace*/Offer/*"
            ]
        },
        {
            "Sid": "AmazonQPartnerAssistantAccess",
            "Effect": "Allow",
            "Action": [
                "q:StartConversation",
                "q:SendMessage",
                "q:GetConversation",
                "q:ListConversations",
                "q:PassRequest"
            ],
            "Resource": "*"
        }
    ]
}
```

### AWSRevenueAttributionManagement policy
<a name="prm-customer-facing-policy"></a>

This policy provides necessary access for revenue attribution management activities for AWS accounts who are not registered with AWS Partner Central.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RevenueAttributionCreation",
            "Effect": "Allow",
            "Action": [
                "partnercentral:CreateRevenueAttribution"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "partnercentral:Catalog": [
                        "AWS",
                        "Sandbox"
                    ]
                }
            }
        },
        {
            "Sid": "RevenueAttributionListing",
            "Effect": "Allow",
            "Action": [
                "partnercentral:ListRevenueAttributions"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "partnercentral:Catalog": [
                        "AWS",
                        "Sandbox"
                    ]
                }
            }
        },
        {
            "Sid": "RevenueAttributionManagement",
            "Effect": "Allow",
            "Action": [
                "partnercentral:GetRevenueAttribution",
                "partnercentral:UpdateRevenueAttribution"
            ],
            "Resource": "arn:aws:partnercentral:*:*:catalog/*/revenue-attribution/*",
            "Condition": {
                "StringEquals": {
                    "partnercentral:Catalog": [
                        "AWS",
                        "Sandbox"
                    ]
                }
            }
        },
        {
            "Sid": "TaggingAccess",
            "Effect": "Allow",
            "Action": [
                "partnercentral:TagResource",
                "partnercentral:UntagResource",
                "partnercentral:ListTagsForResource"
            ],
            "Resource": [
                "arn:aws:partnercentral:*:*:catalog/*/revenue-attribution/*"
            ],
            "Condition": {
                "StringEquals": {
                    "partnercentral:Catalog": [
                        "AWS",
                        "Sandbox"
                    ]
                }
            }
        }
    ]
}
```

## Assigning policies to IAM roles and users
<a name="prm-assigning-policies"></a>

Follow these steps to assign policies to IAM roles and users:

1. Sign in to the AWS Management Console.

1. Navigate to the IAM service.

1. Select roles or users, and choose the IAM role or user to which you want to attach a policy.

1. Attach the `AWSPartnerCentralRevenueAttributionManagement` policy (for partners) or the `AWSRevenueAttributionManagement` policy (for customers) to the selected IAM role or user.

For more information, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html).

## Managing permissions using condition keys
<a name="prm-managing-permissions-with-condition-keys"></a>

Condition keys in IAM policies provide resource-level permissions for when to enforce statement policies. You can use condition keys to specify conditions that dictate when certain permissions are allowed or denied.

For more information, see [IAM JSON policy elements: Condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html).


**Condition keys overview**  

| Condition key | Description | Applicable actions | Valid values | 
| --- | --- | --- | --- | 
| partnercentral:Catalog | Filters access by the type of the associated catalog entity | All actions | AWS, Sandbox | 

## Summary of required permissions
<a name="prm-summary-of-required-permissions"></a>


**Summary of required permissions**  

| Action | Description | 
| --- | --- | 
| partnercentral:CreateRevenueAttribution | Allows creating a new revenue attribution record | 
| partnercentral:UpdateRevenueAttribution | Allows updating an existing revenue attribution record | 
| partnercentral:GetRevenueAttribution | Allows retrieving the details of a specific revenue attribution | 
| partnercentral:ListRevenueAttributions | Allows listing revenue attributions with optional filters | 
| partnercentral:GetRevenueAttributionAllocation | Allows retrieving a single allocation by its ID | 
| partnercentral:ListRevenueAttributionAllocations | Allows listing committed allocations with filtering support | 
| partnercentral:StartRevenueAttributionAllocationsTask | Allows submitting a batch of up to 250 allocation changes for async processing | 
| partnercentral:GetRevenueAttributionAllocationsTask | Allows retrieving the status of a previously submitted allocations task | 
| partnercentral:CreateMarketplaceRevenueShare | Allows creating a new marketplace revenue share resource | 
| partnercentral:GetMarketplaceRevenueShare | Allows retrieving details of a specific marketplace revenue share | 
| partnercentral:ListMarketplaceRevenueShares | Allows listing marketplace revenue shares with optional filters | 
| partnercentral:CreateMarketplaceRevenueShareAllocation | Allows creating a new marketplace revenue share allocation | 
| partnercentral:GetMarketplaceRevenueShareAllocation | Allows retrieving details of a specific marketplace revenue share allocation | 
| partnercentral:UpdateMarketplaceRevenueShareAllocation | Allows updating an existing marketplace revenue share allocation | 
| partnercentral:ListMarketplaceRevenueShareAllocations | Allows listing allocations under a marketplace revenue share | 
| partnercentral:TagResource | Allows adding or overwriting tags for a resource | 
| partnercentral:UntagResource | Allows removing tags from a resource | 
| partnercentral:ListTagsForResource | Allows listing tags associated with a resource | 