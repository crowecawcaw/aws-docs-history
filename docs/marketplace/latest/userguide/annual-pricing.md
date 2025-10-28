# Annual pricing

An annual pricing model enables you to offer products to customers who can purchase a
12-month subscription. As an example, the subscription pricing can provide up to 40 percent
savings compared to running the same product hourly for extended periods. The customer is
invoiced for the full amount of the contract at the time of subscription. For more
information about how annual subscriptions are presented to customers, see [AMI
subscriptions](../buyerguide/buyer-ami-subscriptions.md "../buyerguide/buyer-ami-subscriptions.md") or [Pricing models for paid container products](../buyerguide/buyer-what-is-aws-marketplace-for-containers.md#what-is-aws-marketplace-for-containers-pricing "../buyerguide/buyer-what-is-aws-marketplace-for-containers.md#what-is-aws-marketplace-for-containers-pricing").

Considerations when working with an annual subscription include the following:

- Annual pricing is defined per instance type. It can be the same for all Amazon Elastic Compute Cloud
  (Amazon EC2) instance types or different for each instance type.
- All Annual instance types must also have an Hourly instance type defined. AWS Marketplace
  doesn't offer Annual-only pricing or Hourly without Annual on the same product. For any
  product offering Annual pricing, Hourly pricing also needs to be specified.
- A $0 Annual price is allowed on a specific instance type, if the Hourly price is
  also $0 and there are other non-$0 Annual instance types defined.
- At the end of the annual subscription period, the customer will start being charged
  at the hourly price.
- If a customer buys X Annual subscriptions but is running Y software on Y instances,
  then the customer is charged at Hourly software price for (Y-X) instances which are not
  covered by Annual subscriptions. As such, an Hourly rate must be included for all Annual
  pricing instance types.
- Using seller private offers, you can offer a multi-year (up to 3 years) or custom
  duration AMI with upfront payment, or a flexible payment schedule. For more information
  about multi-year and custom duration contracts, see [Preparing a private offer for your AWS Marketplace product](private-offers-overview.md "private-offers-overview.md") and [Private offer installment plans](installment-plans.md "installment-plans.md").
  If you offer an Annual product in AWS Marketplace, you agree to the specific refund policies for
  Annual products, located in the **File Uploader** documents section in the
  [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/tour "https://aws.amazon.com/marketplace/management/tour").
