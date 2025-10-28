# Planning your SaaS product

Before you add your software as a service (SaaS) product to AWS Marketplace, you must first do some
planning. This step is critical to the success of your product. A lack of planning can
result in billing issues or you might have to re-create your product in AWS Marketplace. The following sections
show you how to plan for SaaS product,

###### Important

Most of your product's settings can’t be changed after you've configured them. If you
need to change them after the product is created in AWS Marketplace, you probably need to create a
new product with the correct settings.

###### Topics

- [Plan your pricing](#plan-pricing "#plan-pricing")
- [Plan your billing integration](#saas-plan-integration "#saas-plan-integration")
- [Plan your Amazon SNS integration](#saas-plan-sns "#saas-plan-sns")
- [Plan how customers will access your
  product](#saas-plan-customer-access "#saas-plan-customer-access")

## Plan your pricing

There are three pricing models for SaaS products on AWS Marketplace. Choosing the right pricing
model for your product is the most important decision you'll make as you plan your
product. Choosing the wrong pricing model can set you back by weeks. The pricing model
determines the payment options for your customers and the billing integration code that
you need to write, test, and deploy. For information about the different types of
pricing models, see [SaaS product
pricing](saas-pricing-models.md "saas-pricing-models.md").

###### Note

All SaaS pricing models support free trials. For more information, see [SaaS free trials](saas-free-trials.md "saas-free-trials.md").

## Plan your billing integration

One of the benefits of having a SaaS product on AWS Marketplace is consolidating billing. In
order to take advantage of this benefit, you must integrate with the AWS Marketplace Metering Service or the
AWS Marketplace Entitlement Service, depending on your chosen pricing model. These two
services help you ensure that your billing and usage reporting is accurate.

After you plan your integration, you must test the integration with your product
before it goes live. For more information about integration and testing, see [Accessing the AWS Marketplace
Metering and Entitlement Service APIs](saas-integration-metering-and-entitlement-apis.md "saas-integration-metering-and-entitlement-apis.md").

## Plan your Amazon SNS integration

There are two Amazon Simple Notification Service (Amazon SNS) topics that you can subscribe to for your SaaS
product. For more information, see [SaaS notifications](saas-notification.md "saas-notification.md"). These messages can help you programmatically handle
changes to subscriptions and contracts initiated by AWS or by your customers. Amazon SNS
notifications can be programmatic triggers enabling customers to register for a new
account on your product registration website. They can also deny customers with expired
subscriptions from accessing your product. You have options for how your customers
receive notifications depending on how you program the handling of these
notifications.

## Plan how customers will access your

product

This section describes how to make your product accessible to buyers.

### Plan your SaaS product registration

website

Customers who buy your SaaS product need access to it. You must plan and implement
how you want your customers to access the product. SaaS products support the
following access options:

- Quick Launch
- AWS PrivateLink
- Your own product website

To validate AWS Marketplace customers using your registration website, see [SaaS
customer onboarding](saas-product-customer-setup.md "saas-product-customer-setup.md").

#### Using Quick Launch for customers to

access your product

Use the Quick Launch deployment option to reduce the time and resources that
are required for buyers to configure, deploy, and launch your products. Quick
Launch reduces the number of sites that buyers must visit during the process.
For more information, see [Configure Quick Launch](saas-product-settings.md#saas-quick-launch "saas-product-settings.md#saas-quick-launch").

#### Using AWS PrivateLink for customers to

access your SaaS product

You can use [Delivering your products through a Amazon VPC using AWS PrivateLink](privatelink.md "privatelink.md") to
conﬁgure your service as an Amazon Virtual Private Cloud (Amazon VPC) endpoint service. Your customers
can create a VPC endpoint and access your software across the AWS Cloud
virtual network. Alternatively, you can provide access to your software product
through a website you own and maintain, with customers creating a connection
across the internet.

#### Using your own website

Your SaaS product is hosted in your environment and it must be accessed over
the internet through a public endpoint that you manage and maintain, like a
website. Typically, you have a website that customers use to register for your
product, sign in to use the product, and access support for your product.
