

# Getting started with DaaS products on AWS Marketplace

As an AWS Marketplace seller, you can sell data and content as a Data as a Service (DaaS) product. You create and configure your product in AWS Partner Central. You also set up the part of your own system that identifies each buyer after they subscribe and gives them access to your data. This topic describes what you need before you start, and what to do next.

## Prerequisites
<a name="daas-prereqs"></a>

Before you create a DaaS product, complete the following prerequisites:

1. Access and use [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home). This is the tool that you use to register as a seller and manage the products that you sell in AWS Marketplace. For more information, see [AWS Partner Central](user-guide-for-sellers.md#aws-marketplace-management-portal).

1. Register as a seller, and submit your tax and banking information. For more information, see [Registration process](registration-process.md).

   To check that your account can publish paid products, open the [seller settings page](https://aws.amazon.com/marketplace/management/seller-settings/account?region=us-east-1&tabId=tax-information-tab). When your setup is complete, the account status reads **Publish paid and free products**.

1. Plan how to identify buyers and give them access to your data. Your product needs a fulfillment URL, which is a page that accepts the registration information that AWS Marketplace sends after a buyer subscribes. For more information, see [Onboarding customers to your DaaS product through AWS Marketplace](daas-product-customer-setup.md).

1. Have a developer who can integrate your system with the AWS Marketplace APIs. This includes the [ResolveCustomer](https://docs.aws.amazon.com/marketplacemetering/latest/APIReference/API_ResolveCustomer.html) operation of the AWS Marketplace Metering Service and the AWS Marketplace Entitlement Service. For usage-based pricing, it also includes the [BatchMeterUsage](https://docs.aws.amazon.com/marketplacemetering/latest/APIReference/API_BatchMeterUsage.html) operation. For more information, see [DaaS product pricing in AWS Marketplace](daas-pricing-models.md).

**Note**  
The AWS Marketplace APIs and events in this guide use the US East (N. Virginia) Region. Make sure that the Region selector in the AWS Management Console is set to **US East (N. Virginia)** when you set up resources for your integration.

## Information to keep track of
<a name="daas-keep-track"></a>

As you create your product and set up your integration, you use the following values in later steps. Record them as you go:
+ The product ID, which starts with `prod-`.
+ The product code, which you use to confirm that the `ResolveCustomer` response is for your product.
+ The fulfillment URL for your product.
+ The names or ARNs of the resources that you create for your integration, such as the data store for your buyer records and the queue that receives subscription events.

## Next steps
<a name="daas-next-steps"></a>

After you complete the prerequisites, you can create and configure your DaaS product. The following topics describe the main parts of the process:
+ [Creating a DaaS product in AWS Marketplace](daas-create-product.md) describes how to create your product and its public offer.
+ [DaaS product lifecycle in AWS Marketplace](daas-product-lifecycle.md) describes how your product moves from limited visibility to public.
+ [DaaS product pricing in AWS Marketplace](daas-pricing-models.md) describes the pricing models that you can choose.
+ [Onboarding customers to your DaaS product through AWS Marketplace](daas-product-customer-setup.md) describes how to accept new buyers at your fulfillment URL.
+ [Managing DaaS subscription events with Amazon EventBridge](daas-eventbridge-integration.md) describes how to receive subscription events.
+ [Testing your DaaS product in AWS Marketplace](daas-product-testing.md) describes how to test the buyer journey.
+ [Making your DaaS product public in AWS Marketplace](daas-make-public.md) describes how to request that your product become public.

**Topics**
+ [Prerequisites](#daas-prereqs)
+ [Information to keep track of](#daas-keep-track)
+ [Next steps](#daas-next-steps)
+ [Creating a DaaS product in AWS Marketplace](daas-create-product.md)