

# Selling with AWS Marketplace Express Checkout

AWS Marketplace Express Checkout lets businesses that don't have an existing AWS account buy your SaaS product from AWS Marketplace with an email address or a social login and a credit or debit card, with no cloud setup required. You reach a new group of business buyers using the same public listing and AWS Marketplace integration you use today. AWS Marketplace handles checkout, card payments, billing and subscription management for these purchases.

Express Checkout is available to buyers in the United States and Canada.

**Topics**
+ [How Express Checkout works](#saas-express-checkout-how-it-works)
+ [Eligibility requirements](#saas-express-checkout-eligibility)
+ [Requesting to add your product](#saas-express-checkout-request)
+ [Linking buyers from your website](#saas-express-checkout-linking)
+ [Pricing recommendations](#saas-express-checkout-pricing)
+ [Customer onboarding and integration](#saas-express-checkout-onboarding)
+ [Express Checkout FAQ](#saas-express-checkout-faq)

## How Express Checkout works
<a name="saas-express-checkout-how-it-works"></a>

Products that are available with Express Checkout appear in the AWS Marketplace Express Checkout catalog, a curated set of products for businesses that don't have an existing AWS account. Your listing stays in the main AWS Marketplace catalog, so buyers with an AWS account can still buy it the usual way. Express Checkout adds a second way to buy the same listing.

From the buyer's side, the purchase works like this:

1. The buyer finds your product in the AWS Marketplace Express Checkout catalog, or follows a link from your website.

1. The buyer signs in with an email address or a social login (Google, Apple, GitHub or Amazon).

1. The buyer pays with a credit or debit card.

1. After the payment goes through, the buyer chooses **Set up product** and goes to your registration page to finish setup, the same as any other AWS Marketplace SaaS purchase.

1. The buyer manages the subscription in My Account in the AWS Marketplace Express Checkout catalog. They can view their subscriptions, update their card and cancel.

When a buyer purchases through Express Checkout, AWS creates a restricted AWS account for them in the background, tied to the email address or social login they used. The buyer can't sign in to the AWS Management Console or use other AWS services. For you, the buyer has a valid AWS account ID, so your integration works without changes.

## Eligibility requirements
<a name="saas-express-checkout-eligibility"></a>

Your product can be added to the AWS Marketplace Express Checkout catalog if it meets all of the following requirements:
+ **SaaS product.** AMI, container, machine learning, professional services and data products aren't supported.
+ **Public offer.** The product has an active, publicly visible listing with a public offer. Private offers, channel partner private offers, Express Private Offers and multi-product solutions aren't supported.
+ **Deployed on AWS.** The listing shows the Deployed on AWS badge.
+ **No resources in the buyer's AWS account.** Buyers can use your product in a browser without setting up anything in their own AWS account, such as AWS CloudFormation templates, IAM roles or cross-account access. There's no restriction on what you run in your own AWS account.
+ **Onboarding that doesn't require AWS.** Your registration flow works for a buyer who has never used AWS. It doesn't ask for an AWS account ID, console access or AWS credentials.

**Tip**  
If a buyer can sign up on your website and start using your product in a browser, your product is likely a good fit.

## Requesting to add your product
<a name="saas-express-checkout-request"></a>

Sellers don't turn on Express Checkout for a listing. Instead, you request to add your product to the AWS Marketplace Express Checkout catalog, and AWS Marketplace reviews the request.

**To request to add your product**

1. Make sure your product meets the [eligibility requirements](#saas-express-checkout-eligibility). If you don't have a public offer yet, create one first. For pricing guidance, see [Pricing recommendations](#saas-express-checkout-pricing).

1. Submit the [**List my product**](https://expresscheckout.storefront.marketplace.aws.com/list-product) form in the AWS Marketplace Express Checkout catalog.

1. AWS Marketplace reviews your request for eligibility and pricing fit, and then adds approved products to the catalog. There's no new listing to create, and your listing in the AWS Marketplace Management Portal doesn't change.

1. After your product is added, link buyers to it from your website. For the link format, see [Linking buyers from your website](#saas-express-checkout-linking).

There's no API to add or remove products from Express Checkout. If you have questions about your request, email [express-checkout-launch@amazon.com](mailto:express-checkout-launch@amazon.com) or contact your AWS Partner Development Manager.

## Linking buyers from your website
<a name="saas-express-checkout-linking"></a>

After your product is added to the AWS Marketplace Express Checkout catalog, you can send buyers to it from your website, pricing page, emails or other marketing materials. You can use either of the following links.

**Link to the catalog home page**

Use this link when you want buyers to browse all products available with Express Checkout:

```
https://expresscheckout.storefront.marketplace.aws.com/
```

**Link directly to checkout for your product**

Use this link when you want buyers to go straight to purchasing your product. The buyer signs in with an email address or social login, and then sees your public offer and pricing.

```
https://expresscheckout.marketplace.aws.com/procurement/?productId={{{productId}}}&sellerId={{{sellerId}}}&trk=express-checkout
```

Replace {{{productId}}} and {{{sellerId}}} with your values, and keep `trk=express-checkout` as is:


| Parameter | Required | Description | 
| --- | --- | --- | 
| productId | Yes | The AWS Marketplace product ID for your SaaS product (for example, prod-abc123example). You can find it in the AWS Marketplace Management Portal on your product's details page. | 
| sellerId | Yes | Your AWS Marketplace seller ID. | 
| trk | Yes | Tracking code for Express Checkout. Always use express-checkout. Don't change this value. | 

**Example**

```
https://expresscheckout.marketplace.aws.com/procurement/?productId=prod-abc123example&sellerId=seller-abc123example&trk=express-checkout
```

**Note**  
Linking directly to your product's page in the catalog isn't available yet. To send buyers to your product, use the checkout link.

**Tips for linking**
+ **Test your link** before you publish it, and check that it opens checkout for the right product and offer.
+ **Label the button clearly.** We recommend a label such as **Continue with email or social login**. Don't use "Buy with AWS," which refers to a different AWS Marketplace feature.
+ **Offer a choice if your customers already use AWS.** Consider showing two options: buy with an AWS account (charges go on the company's AWS bill and follow its purchasing rules) or continue with an email or social login.

## Pricing recommendations
<a name="saas-express-checkout-pricing"></a>

You set the price and term for your public offer. For Express Checkout buyers, we recommend the following:
+ **Fixed-price subscriptions with auto-renewal, preferably monthly.** These match how most businesses buy software online. The subscription renews automatically each term at a fixed price, and the buyer can cancel anytime before the next renewal. Annual terms are allowed.
+ **Pay-as-you-go (usage-based) pricing isn't recommended.** Buyers typically want a predictable price for each term, and usage charges are billed after the usage happens. If you offer usage-based pricing, submit metering records frequently (hourly is ideal), set usage limits in your product, and act on Spend Threshold notifications and Purchase Advisory alerts.

**Free trials** work as follows. Buyers enter a card when they start a trial for both pricing models.
+ **Usage-based offers:** the trial converts to a paid subscription automatically when it ends.
+ **Contract offers:** the trial doesn't convert automatically. The buyer gets an email 3 days before the trial ends with a link to subscribe, and their card is already on file.

**Fees.** Express Checkout uses your standard public offer, so the standard [listing fees](listing-fees.md) for public offers apply. There's no additional fee for Express Checkout, and disbursement timing doesn't change.

## Customer onboarding and integration
<a name="saas-express-checkout-onboarding"></a>

You don't need to change your integration. For Express Checkout purchases:
+ **`ResolveCustomer`**, subscription notifications, Amazon EventBridge events, entitlements and metering work the same as for other buyers. You receive a valid AWS account ID for each buyer.
+ **Reports and disbursements** don't change. At launch, Express Checkout purchases aren't flagged separately in your reports or notifications.
+ **Buyer details.** Collect any account or user details you need in your own registration flow. Buyer contact information sharing isn't available for Express Checkout purchases at launch.
+ **Timing.** The **Set up product** button appears after the buyer's payment goes through, so there can be a short delay between purchase and the redirect to your registration page.

**Updating your onboarding and support content.** Make sure your onboarding pages, emails and help content don't ask Express Checkout buyers to sign in to the AWS console, find their AWS account ID or use other AWS services. For anything about their subscription, billing, payment method, invoices or cancellation, point buyers to My Account in the AWS Marketplace Express Checkout catalog.

## Express Checkout FAQ
<a name="saas-express-checkout-faq"></a>

### Which countries can buy through Express Checkout?
<a name="saas-express-checkout-faq-countries"></a>

Buyers in the United States and Canada. Buyers in other countries can still buy your product through the standard AWS Marketplace website with an AWS account. We plan to expand to more countries.

### Who handles billing and tax?
<a name="saas-express-checkout-faq-billing-tax"></a>

AWS Marketplace handles buyer billing, card payments, tax and currency the same way as for other AWS Marketplace purchases.

### Who carries the risk if a card payment fails?
<a name="saas-express-checkout-faq-payment-risk"></a>

AWS Marketplace collects payment from the buyer and pays you after collection, the same as for other public offer sales. For contract pricing, the buyer can't choose **Set up product** until their card payment goes through.

### How do cancellations and refunds work?
<a name="saas-express-checkout-faq-cancellations-refunds"></a>

Buyers cancel their own subscriptions in My Account in the AWS Marketplace Express Checkout catalog.
+ **Contract offers:** canceling turns off renewal. The buyer keeps access through the period they've already paid for and isn't charged again. Canceling doesn't issue a refund.
+ **Usage-based (pay-as-you-go) offers:** cancellation works the same as for a standard pay-as-you-go SaaS subscription.

For details, see [Refunds and cancellations](refunds.md).

### Should buyers whose companies already use AWS use Express Checkout?
<a name="saas-express-checkout-faq-existing-aws-customers"></a>

No. The buyer's restricted account isn't connected to any existing AWS account. Buyers whose companies already use AWS should buy with their company's AWS account, so charges go on the company's AWS bill and follow its purchasing controls.

### If several people at the same company buy through Express Checkout, can they see each other's purchases?
<a name="saas-express-checkout-faq-shared-purchases"></a>

No. Each purchase is tied to the individual buyer's email address or social login, and each buyer sees only their own purchases. Teams that want to manage software in one place should buy with their company's AWS account.

### Who supports the buyer?
<a name="saas-express-checkout-faq-support"></a>

AWS Marketplace supports billing, payment, subscription and cancellation questions. You support your product, including setup, sign-in, seats and features, the same as today.

### Can buyers renew early or change their plan?
<a name="saas-express-checkout-faq-renew-or-change"></a>

No. Buyers can't renew early or change their plan.

### Where can I get help?
<a name="saas-express-checkout-faq-help"></a>

Email [express-checkout-launch@amazon.com](mailto:express-checkout-launch@amazon.com), or contact your AWS Partner Development Manager.