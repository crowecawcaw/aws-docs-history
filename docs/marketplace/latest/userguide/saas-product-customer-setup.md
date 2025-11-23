# Onboarding customers to your SaaS product through AWS Marketplace

With software as a service (SaaS) subscriptions and SaaS contracts, your customers
subscribe to your products through AWS Marketplace but access the product in your AWS environment.
After subscribing to the product, your customer is directed to a website you create and manage
as a part of your SaaS product to register their account and conﬁgure the product.

When creating your SaaS product listing, you provide a URL to your registration landing
page. We use that URL to redirect customers to your registration landing page after they
subscribe. On your software's registration landing page, you collect the information that is
required to create an account for the customer. We recommend collecting your customer’s email
addresses if you plan to contact them through email for usage notifications.

The registration landing page must be able to identify and accept the
`x-amzn-marketplace-token` token in the form data from AWS Marketplace with the
customer’s identiﬁer for billing. It should then pass that token value to the AWS Marketplace Metering Service to
resolve for the unique customer AWS account ID, customer identiﬁer, and corresponding product code. For a code example, see [ResolveCustomer code
example](saas-code-examples.md#saas-resolvecustomer-example "saas-code-examples.md#saas-resolvecustomer-example").

###### Note

The registration token resolves to a specific subscribed customer and each generated token
has an expiration window of 4 hours. As long as the caller is calling the API with the same
token, it will keep returning the same response values until the token expires.

## Configuring your

SaaS product to accept new buyers

You're responsible for correctly configuring your SaaS software to accept new customers and
meter them appropriately. The following process outlines one recommended way of identifying,
implementing, and metering a new customer's access to your software:

1. When a customer visits your product page on the AWS Marketplace website, they choose to
   subscribe to your product.
2. The customer’s AWS account is subscribed to your product. This means subscription and
   metering records sent from your product become part of the customer’s AWS bill.
3. A registration token is generated for the customer that contains their AWS account
   ID, customer identiﬁer, and your product code.
4. The customer is redirected to your software's registration landing page. This page must be able
   to accept the token with the customer’s identiﬁer.
5. The customer’s browser sends a `POST` request to your software's registration
   landing page URL. The request contains one `POST` parameter,
   `x-amzn-marketplace-token`, containing the customer’s registration token. From
   the perspective of your registration website, the customer has submitted a form with this
   parameter. The registration token is an opaque string. If the offer type is a free trial, a
   second parameter, `x-amzn-marketplace-offer-type` with the value
   `free-trial`, will be added to the request.
6. To redeem this registration token for a customer AWS account ID, customer
   identifier, and product code, your website must call [ResolveCustomer](../../../marketplacemetering/latest/APIReference/API_ResolveCustomer.md "../../../marketplacemetering/latest/APIReference/API_ResolveCustomer.md") on the AWS Marketplace Metering Service. For an example of a
   `ResolveCustomer` call, see [ResolveCustomer code
   example](saas-code-examples.md#saas-resolvecustomer-example "saas-code-examples.md#saas-resolvecustomer-example"). The customer identiﬁer isn't the
   customer’s AWS account ID, but it's universal between products and should be saved to an
   internal source as part of your customer records. The product code is a unique string for
   your SaaS product that AWS provides to you. Each AWS product has one unique product
   code, which is assigned to you during registration.
7. The customer is instructed to either create an account in your product or sign in to an
   existing account.

###### Note

If setting up or linking to an existing customer account in your product requires a
manual process by your team, you can use a contact-us form to collect the customer's
contact information. After collecting their contact information and resolving their
AWS account ID and unique customer identifier (as obtained in step 6), display a
notification message for the customer. In the notification, state that their account is
being set up and request that they wait for you to contact them. Provide the customer
with the expected turnaround time and your contact information. Also send an email
message to the customer with the same details. 8. The customer is now signed in to your website using credentials speciﬁc to that SaaS
product. In your accounts database, you can have an entry for each customer. Your accounts
database must have a column for the AWS account ID. Verify that no other accounts in
your system share the AWS account ID. 9. ###### Important

SNS notifications for AWS Marketplace SaaS products are being replaced with Amazon EventBridge notifications. If you have existing SaaS products integrated with SNS, they will continue to function. New listings will eventually transition to using Amazon EventBridge instead of SNS. For more information, see [Managing SaaS subscription events with Amazon EventBridge](saas-eventbridge-integration.md "saas-eventbridge-integration.md").

During your seller registration process, you configure Amazon EventBridge rules to receive events that notify
you when customers subscribe or unsubscribe to your product. These are Amazon EventBridge events
in JSON format that inform you of customer actions:

    * Entitlement notification – For products with pricing models that include a contract,
     you are notified when buyers create a new contract, upgrade it, renew it, or it expires.
     Your accounts database must have an extra column for the subscription state. For more
     information, see [Managing SaaS subscription events with Amazon EventBridge](saas-eventbridge-integration.md "saas-eventbridge-integration.md").
    * Subscription notification – For products with any pricing model, including contracts
     and subscriptions, you are notified when a buyer subscribes or unsubscribes to a
     product. For more information, see [Managing SaaS subscription events with Amazon EventBridge](saas-eventbridge-integration.md "saas-eventbridge-integration.md").

We recommend that you use Amazon Simple Queue Service (Amazon SQS) as a target for your EventBridge rules to capture these events. After you receive
a subscription notification with `subscribe-success`, the customer account is
ready for metering. Records that you send before this event aren't metered. For
information about how to set up EventBridge rules with SQS targets, see [Amazon SQS targets](../../../eventbridge/latest/userguide/eb-targets.md#eb-targets-sqs "../../../eventbridge/latest/userguide/eb-targets.md#eb-targets-sqs") in the _Amazon EventBridge User Guide_.

###### Note

Do not activate a product subscription unless you receive a
`subscribe-success` notification. 10. Use the AWS account ID stored in your database to meter for usage through the
AWS Marketplace Metering Service or check for entitlements through the AWS Marketplace Entitlement Service.

## Security and ordering

As a seller, it’s your responsibility to trust only AWS account IDs that are
immediately returned from AWS or those that your system has signed. We recommend that you
resolve the registration token immediately because it may expire after approximately one hour.
After you resolve the registration token, store the AWS account ID as a signed attribute on
the customer’s browser session until the registration is complete.
