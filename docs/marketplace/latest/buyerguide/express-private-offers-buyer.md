# Express private offers

Express private offers is an AWS Marketplace capability that enables you to instantly access personalized pricing based on your specific needs, without going through lengthy negotiations. This automated system evaluates your requirements against pre-configured seller criteria to generate immediate private offers.

Key benefits for buyers include:

- Instant access to discounted pricing without waiting for sales negotiations
- Ability to qualify for private offers even on smaller purchases
- Self-service process that allows you to proceed at your own pace
- Option to transition to sales-assisted workflow when needed

## How express private offers work

The express private offer process streamlines the traditional private offer workflow into an automated, buyer-driven experience. When you engage with an express private offer-enabled product, you'll be guided through a series of steps to specify your requirements and qualify for instant pricing. The system employs an AI agent to guide you through your journey, evaluating your needs against seller requirements.

During the process, you'll specify your desired quantities, contract terms, and provide any additional information required by the seller. The system evaluates this information against predefined criteria to determine your eligibility for automated pricing. If your requirements align with the seller's parameters, you'll receive an instant private offer. For more custom scenarios or when your needs fall outside the automated parameters, the system will smoothly transition you to a sales-assisted workflow, ensuring you receive appropriate support for your purchase.

## Required permissions

Before initiating an express private offer request, ensure you have an AWS account with the appropriate permissions. Your account can use the [AWSMarketplaceManageSubscriptions](../../../aaws-managed-policy/latest/reference/AWSMarketplaceManageSubscriptions.md "../../../aaws-managed-policy/latest/reference/AWSMarketplaceManageSubscriptions.md") or [AWSMarketplaceFullAccess](../../../aws-managed-policy/latest/reference/AWSMarketplaceFullAccess.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceFullAccess.md") managed policy for the right permissions. You also can use the following IAM policy:

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
                        "RequestExpressPrivateOffer",
                        "ExpireToken"
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

## Requesting an express private offer

The request process begins on the product detail page, where you'll find the **Get Express Private Offer** button. Choosing this launches the express private offer workflow, starting with the configuration of product dimensions. The first page presents dimension options with comprehensive guidance from the seller. You can access more information about the dimension through the **View Guidance** option, which explains what each dimension means, how dimensions relate to each other, and methods for estimating quantities based on your business needs. If you find your requirements are more complex or difficult to estimate, you can opt to switch to a sales-assisted workflow at any point.

Moving to contract details, you'll specify your desired agreement duration within the seller's defined limits. Here you can choose whether to start your agreement immediately upon acceptance or at a future date, if the seller supports future-dated agreements. This page also presents the EULA for review, either the AWS Marketplace Standard Contract or the seller's public listing EULA. Custom EULA requirements will need to be handled through the sales-assisted workflow.

If the seller has configured profile-based qualifications, you'll proceed to answer additional questions about your organization. These might include details about your industry, company size, or specific use cases. The seller uses this information to determine additional discounts and ensure appropriate offer targeting.

The final step before offer generation involves reviewing all provided information and signing in with your AWS account credentials to confirm your authorization and generate the offer.

## Receiving and accepting your express private offer

Upon completing the request process, the system will either generate your express private offer immediately or direct you to a sales-assisted workflow, depending on your qualification status. For successful qualifications, you'll see your offer details immediately, including complete pricing information with all applicable discounts, contract terms and conditions, and EULA documentation.

The generated offer appears in your AWS Marketplace private offers page and the product's procurement page, where you can review details, share the offer with relevant stakeholders within your organization, and proceed with acceptance within the specified validity period. The acceptance process follows standard AWS Marketplace procedures, allowing you to complete the transaction through your established procurement workflow.

In cases where your request doesn't meet the automated criteria, whether due to size, complexity, or other factors, you'll be directed to provide contact information through a sales-assisted workflow. This ensures you receive appropriate support from the seller's sales team for your specific requirements.

Throughout the process, you'll receive standard AWS Marketplace notifications about your offer status, and you can manage all aspects of the offer through your AWS Marketplace console.
