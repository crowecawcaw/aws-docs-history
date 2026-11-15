

# Service-linked role for Amazon Bedrock AgentCore payments
<a name="buyer-service-linked-role-agentic-commerce"></a>

AWS Marketplace uses the `AWSServiceRoleForMarketplaceAgenticCommerce` service-linked role to process payments that you make through AgentCore payments, a capability of Amazon Bedrock AgentCore. The role reads product, offer, and agreement details, creates and accepts purchase agreements, and meters usage.

The role applies only to AgentCore payments for AWS Marketplace products. Payments through other payment providers, such as Coinbase or Stripe (Privy), don't use this role. You must create the role before AWS Marketplace can process these payments.

The `AWSServiceRoleForMarketplaceAgenticCommerce` service-linked role trusts the following services to assume the role:
+ `agentcore-payments.marketplace.amazonaws.com`

The `AWSMarketplaceAgenticCommerceServiceRolePolicy` policy grants AWS Marketplace permission to perform the following groups of actions:
+ Create and accept purchase agreements – AWS Marketplace creates a purchase agreement for the product that you pay for and accepts it on your behalf. These actions apply only to purchase agreements in your AWS account.
  + `aws-marketplace:CreateAgreementRequest`
  + `aws-marketplace:AcceptAgreementRequest`
+ Record usage for billing – AWS Marketplace records the usage for each payment so that it appears on your AWS bill. This action can't be limited to specific resources.
  + `aws-marketplace:MeterUsage`
+ Read purchase agreements (read-only) – AWS Marketplace finds your existing purchase agreement for the product and checks its terms and entitlements. These actions apply only to purchase agreements in your AWS account, and the search and describe actions apply only to agreements where you're the buyer.
  + `aws-marketplace:SearchAgreements`
  + `aws-marketplace:DescribeAgreement`
  + `aws-marketplace:GetAgreementTerms`
  + `aws-marketplace:GetAgreementEntitlements`
+ Read the catalog (read-only) – AWS Marketplace reads the product, listing, offer, and pricing details for the payment. These actions apply only to products, listings, offers, and purchase options in the AWS Marketplace catalog.
  + `aws-marketplace:GetProduct`
  + `aws-marketplace:GetListing`
  + `aws-marketplace:GetOffer`
  + `aws-marketplace:GetOfferTerms`
  + `aws-marketplace:ListFulfillmentOptions`
  + `aws-marketplace:ListPurchaseOptions`

To view the full policy, see [AWSMarketplaceAgenticCommerceServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceAgenticCommerceServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

**Note**  
For more information about AWS Marketplace managed policies, see [AWS managed policies for AWS Marketplace buyers](buyer-security-iam-awsmanpol.md).

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating the service-linked role
<a name="buyer-service-linked-role-agentic-commerce-create"></a>

You create this role when you set up AgentCore payments in the Amazon Bedrock AgentCore console. To create the role by using the AWS CLI, run the following command:

```
aws iam create-service-linked-role --aws-service-name agentcore-payments.marketplace.amazonaws.com
```

For more information, see [Create a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*. If you delete the role, you can use the same process to create it again.

## Deleting the service-linked role
<a name="buyer-service-linked-role-agentic-commerce-delete"></a>

To delete the role by using the AWS CLI, run the following command:

```
aws iam delete-service-linked-role --role-name AWSServiceRoleForMarketplaceAgenticCommerce
```

You can also delete the role by using the IAM console or the IAM API. For more information, see [Delete a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

IAM deletes the role only after AWS Marketplace finishes processing all your payments and records their usage for billing. If AWS Marketplace is still using the role, the deletion fails with one of the following messages:
+ `Payments are still being processed. Retry the deletion in a few minutes.` AWS Marketplace is still processing a payment. Wait a few minutes, and then delete the role again.
+ `Billing couldn't be processed for some payments. Contact AWS Support.` AWS Marketplace can't finish billing some payments without help. Create a case in the [AWS Support Center](https://support.console.aws.amazon.com/support/home).

While IAM deletes the role, AWS Marketplace doesn't accept new payments from your account. After IAM deletes the role, payments from your account fail until you create the role again.

## Supported Regions for the AgentCore payments service-linked role
<a name="buyer-service-linked-role-agentic-commerce-regions"></a>

You can use this role in all AWS Regions where AgentCore payments is available. For the list of Regions, see [Supported AWS Regions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html) in the *Amazon Bedrock AgentCore Developer Guide*.

AWS Marketplace processes every payment in the US East (N. Virginia) Region. If AgentCore payments receives a payment in another Region, it sends the payment to US East (N. Virginia) for processing. IAM roles aren't specific to a Region, so you create this role once for your AWS account.