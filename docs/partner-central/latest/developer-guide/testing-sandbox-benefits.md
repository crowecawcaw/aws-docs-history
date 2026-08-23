The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Testing in a sandbox for the AWS Partner Central Benefits API

## How to use the sandbox

To use the sandbox, complete the following steps:

1. Create an IAM role:

Create an IAM role in the AWS account linked with your AWS Partner Central account. 2. Assign Policy:

Assign the following policy to the IAM role. For more information, see [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").

```
{
  "Version": "2012-10-17",
    "Statement": [{
            "Sid": "BenefitsManagement",
            "Effect": "Allow",
            "Action": [
                "partnercentral:ListBenefits",
                "partnercentral:GetBenefit",
                "partnercentral:CreateBenefitApplication",
                "partnercentral:AmendBenefitApplication",
                "partnercentral:UpdateBenefitApplication",
                "partnercentral:SubmitBenefitApplication",
                "partnercentral:GetBenefitApplication",
                "partnercentral:CancelBenefitApplication",
                "partnercentral:RecallBenefitApplication",
                "partnercentral:ListBenefitApplications",
                "partnercentral:AssociateBenefitApplicationResource",
                "partnercentral:DisasssociateBenefitApplicationResource",
                "partnercentral:ListBenefitAllocations",
                "partnercentral:GetBenefitAllocation",
                "partnercentral:TagResource",
                "partnercentral:UntagResource",
                "partnercentral:ListTagsForResource"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "partnercentral:Catalog": [
                        "Sandbox"
                    ]
                }
            }
        },
        {
            "Sid": "AWSPartnerOpportunityAccess",
            "Effect": "Allow",
            "Action": [
                "partnercentral:GetAwsOpportunitySummary",
                "partnercentral:GetOpportunity",
                "partnercentral:ListOpportunities"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "partnercentral:Catalog": [
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
            "Sid": "AWSMarketplaceOffersAccess",
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:DescribeEntity"
            ],

            "Resource": [
                "arn:aws:aws-marketplace:::AWSMarketplace/Offer/*"
            ]
        },
        {
            "Sid": "S3PutObjectAccess",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": ["arn:aws:s3:::aws-partner-central-marketplace-ephemeral-writeonly-files/*"]
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
                "arn:aws:partnercentral:us-east-1:*:catalog/Sandbox/benefit-application/*",
                "arn:aws:partnercentral:us-east-1:*:catalog/Sandbox/benefit-allocation/*"
            ],
            "Condition": {
                "StringEquals": {
                    "partnercentral:Catalog": [
                        "Sandbox"
                    ]
                }
            }
        }
    ]
}
```

3. Use IAM role credentials:

Use the credentials (secret key and access key) of this IAM role in your solution to
perform the API actions.

## Testing AWS actions

During the testing phase, it is often necessary to simulate AWS actions. This
simulation enables partners to thoroughly test the complete end-to-end flow of their
integration with AWS services. Each request includes a catalog parameter, which determines the data environment.

### Simulating the creation of a Benefit Application

To simulate the creation of a benefit application, in the payload of the
`CreateBenefitApplication` action, include `"catalog": "Sandbox"` in the payload.

For example:

```
{
  "Catalog": "Sandbox",
  "ClientToken": "String",
  "BenefitIdentifier": "String",
  "FulfillmentTypes": ["String"],
  "BenefitApplicationDetails": JsonDocument,
  "Name": "String",
  "Description": "String",
  "Tags": [
    {
      "Key": "string",
      "Value": "string"
    }
  ],
  "PartnerContacts": [
    {
      "BusinessTitle": "string",
      "Email": "string",
      "FirstName": "string",
      "LastName": "string",
      "Phone": "string"
    }
  ],
  "FileDetails": [
    {
      "FileURI": "String",
      "BusinessUseCase": "String"
    }
  ],
  "AssociatedResources": [
    {
      "ResourceType": "BENEFIT_ALLOCATION | OPPORTUNITY",
      "ResourceArn": "ARN"
    }
  ]
}
```

## Additional testing notes

Note the following when testing in the sandbox:

1. To test other actions, set `"catalog": "Sandbox"` in the payload.
2. The Benefit IDs in Sandbox catalog and AWS catalog are different. Make `GetBenefit` API call with `"catalog": "Sandbox"` to get Benefit Identifier in the Sandbox.
3. The Benefit allocation in Sandbox catalog and AWS catalog are different.
4. To move to production, change the catalog value from `Sandbox` to `AWS`.

## Testing events in the sandbox environment

Partners can consume events from the sandbox environment to help test the event-based implementations. Set up EventBridge in the same AWS account with rules to listen for sandbox events by specifying `catalog: Sandbox` in the event details. For more information, see [Notifications for the AWS Partner Central Benefits API](benefits-api-events.md "benefits-api-events.md").

Example event rule:

```
{
  "source": ["aws.partnercentral-benefits"],
  "detail": {
    "catalog": ["Sandbox"]
  }
}
```

Event rules that specify `catalog` as `Sandbox` will only match
events coming from the sandbox, generated by the actions you perform in the sandbox
environment.
