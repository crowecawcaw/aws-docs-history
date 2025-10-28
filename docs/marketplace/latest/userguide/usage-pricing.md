# Usage pricing

A usage pricing model, also known as _pay as you go_
pricing, enables you to offer products to customers who only pay for what they use.

Usage pricing private offers support multi-currency pricing in EUR, GBP, AUD, and JPY.

As a seller, you can choose one of the following usage categories:

- **Users**
- **Hosts**
- **Bandwidth**
- **Data**
- **Tiers**
- **Units** (for custom categories)
  You can also define up to 200 dimensions for the product. Charges are measured and
  reported when the API is called by the software. We recommend that sellers configure the API
  to be called once per hour as a best practice, depending on their use case. All usage is
  calculated monthly and billed monthly using the same mechanism as existing AWS Marketplace software.

Using the AWS Marketplace Metering Service, you can handle several new pricing scenarios.

###### Example Charge by Host

If your software monitors hosts, you can charge for each host monitored and set
different pricing based on the host size.

###### Example Charge by User

If your software allows multiple users across an organization, you can charge by user.
Each hour, the customer is charged for the total number of provisioned users.

###### Note

In the Product Load Form (PLF), relevant columns are preceded with "FCP" (Flexible
Consumption Pricing). For example: **FCP Category (Custom Pricing
Category)**.

For AWS Marketplace Metering Service products, note the following:

- If your software is already on AWS Marketplace, you will need to create a product to enable an
  alternate usage dimension. You can't convert a standard product to use the AWS Marketplace Metering Service.
  After the new product is published, you can remove the old product or keep both on the
  website.
- The AWS Marketplace Metering Service requires that your software reports usage every hour, recording the
  customer usage for the hour. If there is a failure in the transmission or receipt of
  metering service records, AWS will be unable to bill for such usage. You are
  responsible for ensuring the successful receipt of metering records.
- Products that use the AWS Marketplace Metering Service don't support 1-Click. Buyers are required to
  launch your software with an AWS Identity and Access Management (IAM) role with specific permissions and have
  an internet gateway.
- Free Trial and Annual Pricing aren't compatible with the AWS Marketplace Metering Service.
- Changing dimension (user, hosts, bandwidth, and data) or dimension name isn't
  supported. You will need to create a new product.
