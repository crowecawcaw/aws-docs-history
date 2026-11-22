

# Onboarding customers to your DaaS product through AWS Marketplace

With Data as a Service (DaaS) products, you deliver your data and content yourself, and AWS Marketplace handles the subscription and billing. After a buyer subscribes to your product, AWS Marketplace sends them to your fulfillment URL. The page at your fulfillment URL is where a buyer's subscription becomes access to your data. It connects the buyer's AWS account and their AWS Marketplace subscription to an account in your own system.

**Your fulfillment URL must accept a POST request**  
AWS Marketplace doesn't send buyers to your fulfillment URL with a plain link. It sends the buyer's browser to your fulfillment URL with an HTTP `POST` request. The request carries a registration token in the form data, and the token identifies the buyer and their subscription.  
Don't point your fulfillment URL at an existing sign-up page, login page, or static web page unless the page can accept the `POST` request and read the `x-amzn-marketplace-token` form field.

## What your fulfillment URL must do
<a name="daas-what-you-must-do"></a>

Your fulfillment URL must meet the following requirements:
+ It uses HTTPS.
+ It's no longer than 2,048 characters.
+ AWS Marketplace can reach it. If AWS Marketplace can't use your fulfillment URL, the update fails. In the **Fulfillment options** section in AWS Partner Central, the error message explains why. With the [StartDeploymentConfigurationJob](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_StartDeploymentConfigurationJob.html) API, call [GetDeploymentConfigurationJob](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-deployment_GetDeploymentConfigurationJob.html) to check the job. A failed job has the status `FAILED` and the error code `FULFILLMENT_URL_UNREACHABLE`, `ENDPOINT_INVALID`, or `INTERNAL_ERROR`.

To list a DaaS product, the page at your fulfillment URL must do the following:

1. Accept the `POST` request and read the `x-amzn-marketplace-token` value from the form data.

1. Call [ResolveCustomer](https://docs.aws.amazon.com/marketplacemetering/latest/APIReference/API_ResolveCustomer.html) on the AWS Marketplace Metering Service with the token. The response contains the buyer's AWS account ID (`CustomerAWSAccountId`), the `LicenseArn`, your product code (`ProductCode`), and the agreement ID (`Metadata.AgreementId`). Check that `ProductCode` matches your product before you continue. Resolve the token as soon as you receive it. For a code example, see [`ResolveCustomer` code example](saas-code-examples.md#saas-resolvecustomer-example). For DaaS products, the response doesn't include `CustomerIdentifier`. Leave out the line that reads it, and use `CustomerAWSAccountId` wherever the example uses `customerID`.

1. Save the `CustomerAWSAccountId` and `LicenseArn` with the buyer's account in your system, with a pending status. Keep the status pending until you receive the `License Updated` event. You use these values later to match subscription events to the buyer, check entitlements, and report usage.

   If you already have a record for the `CustomerAWSAccountId` that `ResolveCustomer` returns, sign the buyer in to that account. If the `LicenseArn` is the same, keep the record's current status. If it's different, the buyer has a new agreement: replace the stored `LicenseArn` (and `Metadata.AgreementId`, if you store it), and set the status as described in [Security and ordering](#daas-security-and-ordering).

1. If the token is missing, isn't valid, or has expired, show an error page that explains why and tells the buyer to return to the **Set up your account** page in AWS Marketplace and choose **Set up your account** again to get a new token.

**Note**  
A registration token expires after 4 hours.

**Follow AWS security best practices**  
AWS code examples are samples and aren't production ready. Before you publish, test your fulfillment URL for security issues. Validate all input, handle API errors, use HTTPS, and don't expose internal resource names or credentials.

## What you can choose
<a name="daas-what-you-can-choose"></a>

You decide the rest, based on your product and your systems. For example:
+ Where you store buyer records. Use any data store that suits you, such as a database table. Amazon DynamoDB is one option.
+ How buyers sign in. You can ask the buyer to create an account or sign in to an existing one. If setting up or linking an account requires a manual step by your team, you can use a contact form to collect their details. After you resolve the token, tell the buyer that their account is being set up, how long it takes, and how to contact you.
+ How buyers reach your data. You decide how to deliver it, for example through an API, a web portal, an Amazon S3 location, or a managed feed.

## How a new buyer is onboarded
<a name="daas-onboarding-process"></a>

The following process shows one recommended way to identify a new buyer and give them access:

1. A customer visits your product page on the AWS Marketplace website and subscribes to your product.

1. The customer's AWS account is subscribed to your product.

1. When the customer chooses **Set up your account** in AWS Marketplace, the customer's browser sends a `POST` request to your fulfillment URL. The customer can do this more than once, and each time, AWS Marketplace issues a new registration token. The request includes the following parameters:
   + `x-amzn-marketplace-token` – The registration token.
   + `x-amzn-marketplace-product-id` – The ID of the product that the buyer subscribed to.
   + `x-amzn-marketplace-agreement-id` – The ID of the agreement for the buyer's subscription to the product.

   Treat `x-amzn-marketplace-product-id` and `x-amzn-marketplace-agreement-id` as unverified input from the buyer's browser. Identify the buyer and their subscription only from the values that `ResolveCustomer` returns: `CustomerAWSAccountId`, `LicenseArn`, `ProductCode`, and `Metadata.AgreementId`.

1. Your page calls `ResolveCustomer` with the token and receives the buyer's AWS account ID, `LicenseArn`, and product code.

1. Your page saves the buyer's AWS account ID and `LicenseArn`, creates or links the buyer's account in your system, and tells the buyer how to access your data.

1. AWS Marketplace sends events to Amazon EventBridge in your seller account when a buyer subscribes, changes, or cancels. Use these events to grant and remove access. Don't activate a buyer's subscription until you receive a `License Updated` event. Usage records that you send before this event aren't metered. For more information, see [Managing DaaS subscription events with Amazon EventBridge](daas-eventbridge-integration.md).

1. Use the AWS account ID that you saved to check entitlements through the AWS Marketplace Entitlement Service. For usage-based pricing, also report usage through the AWS Marketplace Metering Service.

## Security and ordering
<a name="daas-security-and-ordering"></a>

As a seller, you're responsible for trusting only AWS account IDs that AWS returns immediately or that your system has signed. Resolve the registration token as soon as you receive it. After you resolve it, store the AWS account ID as a signed attribute on the customer's browser session until registration is complete.

Before you create or link an account, verify that no other account in your system already uses that AWS account ID.

If the buyer is already signed in, ask them to confirm before you link the subscription to their account.

If you receive the `License Updated` event before the buyer registers, keep it and apply it when they register, or check the buyer's entitlements with `GetEntitlements` at registration.