

# Usage pricing

A usage pricing model, also known as *pay as you go* pricing, enables you to offer products to customers who only pay for what they use.

Usage pricing private offers support multi-currency pricing in EUR, GBP, AUD, JPY, CAD, SGD, and NZD.

Agentic Commerce products use a reserved usage dimension, `agentic_commerce_default`, at USD $1.00 per unit. AWS Marketplace meters this dimension for you. For more information, see [Pricing and metering](agentic-commerce-products.md#agentic-commerce-pricing).

For products other than Agentic Commerce products, when you add usage dimensions, you choose one **Dimension unit type** for all of the product's dimensions. The options are **Gbps**, **Mbps**, **GB**, **MB**, **TB**, **Requests**, **Units**, **Host hours**, **Tier hours**, and **User hours**. You can't change the unit type later. If the unit differs between dimensions, choose **Units**.

You can also define up to 200 dimensions for the product. Charges are measured and reported when the API is called by the software. We recommend that sellers configure the API to be called once per hour as a best practice, depending on their use case. All usage is calculated monthly and billed monthly using the same mechanism as existing AWS Marketplace software. 

Using the AWS Marketplace Metering Service, you can handle several new pricing scenarios. 

**Example Charge by Host**  
If your software monitors hosts, you can charge for each host monitored and set different pricing based on the host size. 

**Example Charge by User**  
If your software allows multiple users across an organization, you can charge by user. Each hour, the customer is charged for the total number of provisioned users. 

**Note**  
You choose usage pricing and add usage dimensions when you create your product's public offer. For AMI products, see [Adding your product to AWS Marketplace](custom-metering-pricing-ami-products.md#listing-your-product-on-aws-marketplace).

For AWS Marketplace Metering Service products, note the following: 
+ If your software is already on AWS Marketplace, you will need to create a product to enable an alternate usage dimension. You can't convert a standard product to use the AWS Marketplace Metering Service. After the new product is published, you can remove the old product or keep both on the website. 
+ The AWS Marketplace Metering Service requires that your software reports usage every hour, recording the customer usage for the hour. If there is a failure in the transmission or receipt of metering service records, AWS will be unable to bill for such usage. You are responsible for ensuring the successful receipt of metering records. 
+ Products that use the AWS Marketplace Metering Service don't support 1-Click. Buyers are required to launch your software with an AWS Identity and Access Management (IAM) role with specific permissions and have an internet gateway. 
+ AMI products that use the AWS Marketplace Metering Service can't offer a free trial or annual pricing.
+ You can't change the dimension unit type or a dimension's API identifier. To use a different unit type, create a new product. You can change a dimension's display name and description. On the product's **Procurement** tab, in the **Pricing dimensions** section, choose **Update**, and then choose **Update dimensions**.