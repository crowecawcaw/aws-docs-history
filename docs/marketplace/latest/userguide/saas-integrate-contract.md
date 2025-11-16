# Integrating your SaaS contract product with AWS Marketplace

Integrating your software as a service (SaaS) contract product with AWS Marketplace is one step in [Creating a SaaS product in AWS Marketplace](saas-create-product.md "saas-create-product.md"). To integrate your software as a service (SaaS)
contract product with AWS Marketplace, you must write code and demonstrate that it can respond
successfully to several customer scenarios. The following sections describe these scenarios,
explain how to respond to them, and provide an overview of testing your integration.

###### Note

Before you begin, make sure you've chosen the right pricing model for your software as
a service (SaaS) product in AWS Marketplace. For more information, see [Planning your SaaS product](saas-prepare.md "saas-prepare.md").

###### Topics

- [Scenario: Your service validates new
  customers](#saas-contract-validate-customer "#saas-contract-validate-customer")
- [Scenario: Your service handles
  customer requests](#saas-contract-customer-requests "#saas-contract-customer-requests")
- [Scenario: Monitor changes to user
  subscriptions](#saas-contract-monitor-changes "#saas-contract-monitor-changes")
- [Testing your SaaS contract product
  integration](#saas-contract-integration-testing "#saas-contract-integration-testing")

## Scenario: Your service validates new

customers

When a customer subscribes to your product, they are redirected to your registration
URL, which is an HTTP POST request with a temporary
`x-amzn-marketplace-token` token. Respond to this request in the
following ways:

1. Exchange the token for a `CustomerIdentifier`,
   `CustomerAWSAccountId`, and `ProductCode` by calling
   the `ResolveCustomer` API operation in the AWS Marketplace Metering Service.
2. Verify the subscription and quantity (if applicable) the customer has access
   to by calling the `GetEntitlements` API operation in the
   AWS Marketplace Entitlement Service.
3. Persist the `CustomerIdentifier`,
   `CustomerAWSAccountId`, and `ProductCode` in your system
   for future calls. Store whether the customer has a valid subscription, along
   with whatever information you need about the customer.
4. As a response to the request, you must show your user's first use experience
   (as applicable for your service).

## Scenario: Your service handles

customer requests

When a customer makes a request to your service, you must respond to the following
scenarios with appropriate actions or messaging:

- They don't have a customer ID in your system. This means that they have not
  yet subscribed. You should tell the user how to subscribe.
- They have a customer ID, and the `GetEntitlements` API operation
  returns an appropriate entitlement. In this scenario, you should fulfill the
  request.
- They do have a customer ID, but the `GetEntitlements` API operation
  returns no entitlement, or not enough quantity to fulfill the request. In this
  scenario, you must determine how to handle access and manage their
  experience.

## Scenario: Monitor changes to user

subscriptions

###### Important

SNS notifications for AWS Marketplace SaaS products are being replaced with Amazon EventBridge notifications. If you have existing SaaS products integrated with SNS, they will continue to function. New listings will eventually transition to using Amazon EventBridge instead of SNS. For more information, see [Managing SaaS subscription events with Amazon EventBridge](saas-eventbridge-integration.md "saas-eventbridge-integration.md").

Set up an Amazon Simple Queue Service (Amazon SQS) queue as a target for your Amazon EventBridge rules to receive events about changes to customer entitlements. Your
Amazon EventBridge event configuration was provided when you created your product. For more information, see [Creating a SaaS product in AWS Marketplace](saas-create-product.md "saas-create-product.md"). By configuring
Amazon EventBridge rules, you receive events about changes to customer entitlements,
including providing or revoking access for specific customers.

The only notification that you must respond to is:

- License Updated Amazon EventBridge events – The customer entitlement has
  changed, and you must call the `GetEntitlements` API operation to see
  the new status. Update your customer store, and, if applicable (for example, the
  customer's contract has lapsed), follow your practices for shutting down
  customer resources, adhering to your retention policies.

###### Note

For additional information, see [Checking entitlements using the AWS Marketplace Entitlement Service](checking-entitlements.md "checking-entitlements.md").

## Testing your SaaS contract product

integration

After you've integrated your SaaS contract product with AWS Marketplace, you must conduct
in-depth testing to ensure that the integration is successful. The following procedure
outlines the steps to verify your product integration.

###### Note

Use your own accounts to subscribe to your product and test that the integration
is successful. Prices can be temporarily reduced so that you can test the purchase
flow without incurring high charges in those accounts. For more information about
temporarily reducing the prices or allowing additional test accounts to access your
product, [contact us](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/").

After your product is launched, the service must continue to respond to these
scenarios for new customers.

1. Use an allowed account to test the customer experience by getting a contract
   for your product.
2. After the account has the contract, ensure that the account is redirected to
   the registration URL, and that the redirect is a POST request that includes a
   temporary token. Make sure that your application persists the customer ID for
   future calls and correctly handles the entitlement the customer has. This tests part of [Scenario: Your service validates new
   customers](#saas-contract-validate-customer "#saas-contract-validate-customer").
3. After verifying the test account in the previous step, onboard the account
   into your application. For example, you can have the test customer fill out a
   form to create a new user. Or, provide them with other next steps to get access
   to your SaaS application. This tests part of [Scenario: Your service validates new
   customers](#saas-contract-validate-customer "#saas-contract-validate-customer").
4. If no entitlement is returned from the `GetEntitlements` API
   operation, either during onboarding or in your ongoing verification passes, your
   application must correctly manage access and the experience for users who are
   not entitled. This tests [Scenario: Your service handles
   customer requests](#saas-contract-customer-requests "#saas-contract-customer-requests").
5. Test for subscription changes. Verify that your application correctly handles
   unsubscribes, successful subscription, and failed subscription scenarios. This tests [Scenario: Monitor changes to user
   subscriptions](#saas-contract-monitor-changes "#saas-contract-monitor-changes").
6. After you have completed all the integration requirements and tested the
   solution, notify the AWS Marketplace Operations team. They will then test the solution by
   verifying that you have successfully called the `GetEntitlements` API
   operation and sufficiently onboarded new customers.

After your integration and testing is complete, you can perform a final review and
list your product on the public AWS Marketplace. For more information, see [Creating a SaaS product in AWS Marketplace](saas-create-product.md "saas-create-product.md"). You can also
cancel your test subscription by completing a Refund Request Form. For more information
on cancelling a subscription, see the [Requesting a product refund](refunds.md#refund-process "refunds.md#refund-process").
