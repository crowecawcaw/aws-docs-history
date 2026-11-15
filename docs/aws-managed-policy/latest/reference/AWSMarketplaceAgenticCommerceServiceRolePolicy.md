

# AWSMarketplaceAgenticCommerceServiceRolePolicy
<a name="AWSMarketplaceAgenticCommerceServiceRolePolicy"></a>

**Description**: Allows AWS Marketplace to process AgentCore payments for AWS Marketplace products in Amazon Bedrock AgentCore. AWS Marketplace reads product and offer details, creates and accepts purchase agreements on your behalf, and records your usage for billing.

`AWSMarketplaceAgenticCommerceServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSMarketplaceAgenticCommerceServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSMarketplaceAgenticCommerceServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: November 12, 2026, 18:37 UTC 
+ **Edited time:** November 12, 2026, 18:37 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSMarketplaceAgenticCommerceServiceRolePolicy`

## Policy version
<a name="AWSMarketplaceAgenticCommerceServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSMarketplaceAgenticCommerceServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "MarketplaceAgreementCreation",
      "Effect" : "Allow",
      "Action" : [
        "aws-marketplace:CreateAgreementRequest",
        "aws-marketplace:AcceptAgreementRequest"
      ],
      "Resource" : "*",
      "Condition" : {
        "ForAllValues:StringEquals" : {
          "aws-marketplace:AgreementType" : [
            "PurchaseAgreement"
          ]
        },
        "Null" : {
          "aws-marketplace:AgreementType" : "false"
        },
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "MarketplaceAgreementRead",
      "Effect" : "Allow",
      "Action" : [
        "aws-marketplace:SearchAgreements",
        "aws-marketplace:DescribeAgreement",
        "aws-marketplace:GetAgreementTerms"
      ],
      "Resource" : "*",
      "Condition" : {
        "ForAllValues:StringEquals" : {
          "aws-marketplace:AgreementType" : [
            "PurchaseAgreement"
          ]
        },
        "Null" : {
          "aws-marketplace:AgreementType" : "false"
        },
        "StringEquals" : {
          "aws-marketplace:PartyType" : "Acceptor",
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "MarketplaceAgreementEntitlements",
      "Effect" : "Allow",
      "Action" : [
        "aws-marketplace:GetAgreementEntitlements"
      ],
      "Resource" : "*",
      "Condition" : {
        "ForAllValues:StringEquals" : {
          "aws-marketplace:AgreementType" : [
            "PurchaseAgreement"
          ]
        },
        "Null" : {
          "aws-marketplace:AgreementType" : "false"
        },
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "MarketplaceMetering",
      "Effect" : "Allow",
      "Action" : [
        "aws-marketplace:MeterUsage"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "MarketplaceDiscovery",
      "Effect" : "Allow",
      "Action" : [
        "aws-marketplace:GetProduct",
        "aws-marketplace:GetListing",
        "aws-marketplace:GetOffer",
        "aws-marketplace:GetOfferTerms",
        "aws-marketplace:ListFulfillmentOptions",
        "aws-marketplace:ListPurchaseOptions"
      ],
      "Resource" : [
        "arn:aws:aws-marketplace:::catalog/AWSMarketplace*/product/*",
        "arn:aws:aws-marketplace:::catalog/AWSMarketplace*/listing/*",
        "arn:aws:aws-marketplace:::catalog/AWSMarketplace*/offer/*",
        "arn:aws:aws-marketplace:::catalog/AWSMarketplace*/purchaseOption/*"
      ]
    }
  ]
}
```

## Learn more
<a name="AWSMarketplaceAgenticCommerceServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)