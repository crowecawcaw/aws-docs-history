

# Custom metering pricing for AMI products with AWS Marketplace Metering Service

With the AWS Marketplace Metering Service, you can modify your software to send metering records to an endpoint to capture usage. You choose one dimension unit type and define up to 200 dimensions for it. These dimensions are metered once per hour, aggregated, and charged against a price plan that you define. Choose your dimension unit type and API identifiers before you create the public offer. You can't change them later. The following sections provide information about AWS Marketplace Metering Service.

**Topics**
+ [Metering service concepts](#metering-service-concepts)
+ [Pricing your software](#pricing-your-software)
+ [Adding your product to AWS Marketplace](#listing-your-product-on-aws-marketplace)
+ [Modifying your software to use the Metering Service](#modifying-your-software-to-use-the-metering-service)
+ [Vendor-metered tagging (Optional)](#ami-vendor-metered-tagging)
+ [Configuring custom metering](#configure-custom-metering)
+ [Configuring custom metering for AMI products with AWS Marketplace Metering Service](custom-metering-with-mp-metering-service.md)

## Metering service concepts
<a name="metering-service-concepts"></a>

Before you use the AWS Marketplace Metering Service, note the following important service concepts:
+  **Usage Category** – Any software product priced through the use of the Metering Service is categorized according to one usage category, which determines the appropriate way to charge customers. Usage categories include but aren't limited to: 
  + Users – A defined set of permissions associated with a single identifier. This category is appropriate for software in which a customer’s users connect to the software directly (for example, for customer-relationship management or business intelligence reporting). 
  + Hosts – Any server, node, instance, endpoint, or other part of a computing system. This category is appropriate for software that monitors or scans many customer-owned instances (for example, performance or security monitoring). 
  + Data – Storage or information, measured in MB, GB, or TB. This category is appropriate for software that manages stored data or processes data in batches. 
  + Bandwidth – Measured in Mbps or Gbps. This category is appropriate for software that allows customers to specify an amount of bandwidth to provision.
  + Unit – Unit of measurement; see the examples described next.
+  **Usage Unit** – A software product's specific usage unit corresponds to the selected usage category. This usage unit describes the unit your software will charge on. When you create the public offer, you choose it for **Dimension unit type**. Examples include: 
  + **Host hours** (corresponding to the Hosts category)
  + **User hours** (corresponding to the Users category)
  + **GB** (corresponding to the Data category)
+  **Consumption** – Software products priced through the use of the Metering Service charge for consumption in one of three ways: 
  + Provisioned – The software allows customers to configure a specific amount of resources for use (for example, number of users or a fixed amount of bandwidth). Each hour, customers pay for what they have provisioned. 
  + Concurrent – The software allows any number of distinct hosts or users to connect to the software. Each hour, customers pay based on the number of hosts or users who accessed the software. 
  + Accumulated – The software allows customers to use any amount of data, either processed or stored. Each hour, customers pay for the aggregated amount. 
+  **Pricing** – Software products priced through the use of the Metering Service must specify either a single price or define up to 200 dimensions, each with their own price. Details about the pricing options include:
  + Single dimension – This is the simplest pricing option. Customers pay a single price per resource unit per hour, regardless of size or volume (for example, $0.014 per user per hour, or $0.070 per host per hour). 
  + Multiple dimensions – This pricing option is appropriate when the selected usage category varies along multiple axes. For example, for host monitoring, a different price could be set depending on the size of the host. Or, for user-based pricing, a different price could be set based on the type of user (for example, admin, power user, and read-only user). 
+  **Metering** – All usage is recorded as a metering event, once each hour. Your software must be configured to send the appropriate dimension and usage amount to the AWS Marketplace Metering Service. 
  + Allocations – Optionally, you may distribute the usage into allocations by properties that you track. These allocations are represented as tags to the buyer. The tags allow the buyer to view their costs split into usage by tag. For example, if you charge by the user, and users have a "Department" property, you could create usage allocations with tags that have a key of "Department", and one allocation per value. This approach doesn't change the price, dimensions, or the total usage that you report. However, it allows your customer to view their costs by categories appropriate to your product.

## Pricing your software
<a name="pricing-your-software"></a>

When pricing your software with the AWS Marketplace Metering Service, you must first decide on a usage category and how it will be consumed. The service supports six distinct pricing scenarios. You must select only one of these for your product: 
+ Provisioned user (per hour) 
+ Concurrent user (per hour) 
+ Provisioned host (per hour) 
+ Concurrent host (per hour) 
+ Provisioned bandwidth (per hour) 
+ Accumulated data (per hour) 

Next, you must decide how to price the selected usage category: 
+ Single price 
+ Multiple dimensions (up to 200) 

[Adding your product to AWS Marketplace](#listing-your-product-on-aws-marketplace) describes how to provide a customer-friendly description of your dimension and pricing. 

### Example: Provisioned bandwidth with nonlinear pricing
<a name="example-provisioned-bandwidth-with-non-linear-pricing"></a>

Imagine you offer network appliance software. You choose to bill by provisioned bandwidth. For **Dimension unit type**, choose **Mbps** or **Gbps**. In addition to charging by bandwidth, you want to charge a different price as buyers scale up. You can define multiple dimensions within the bandwidth category. You can define a distinct price for 25 Mbps, 100 Mbps, and 1 Gbps. 

### Example: Concurrent hosts with multiple dimensions
<a name="example-concurrent-hosts-with-multiple-dimensions"></a>

Imagine you offer software that monitors other Amazon EC2 instances. You choose to bill by the number of hosts that are being monitored. For **Dimension unit type**, choose **Host hours**. In addition to charging by host, you want to charge for the extra value for monitoring larger hosts. You can use multiple dimensions within the host category. You can define a distinct price for micro, small, medium, large, x-large, 2XL, 4XL, and 8XL instances. Your software is responsible for mapping each particular host to one of your defined dimensions. Your software is responsible for sending a separate metering record for each dimension of your usage category if applicable. 

## Adding your product to AWS Marketplace
<a name="listing-your-product-on-aws-marketplace"></a>

To take advantage of the Metering Service, you must create a new product for AWS Marketplace to list. If your product is already on the AWS Marketplace, you will need to decide whether the new AWS Marketplace Metering Service product will be made available in addition to your current product, or if it will replace your current product as the only version available to new users. If you choose replacement, the existing product will be removed from the AWS Marketplace so that it is no longer available for new buyers. Existing customers will continue to have access to their old product and instances, but they can migrate to the new product at their convenience. The new product must meter usage to the AWS Marketplace Metering Service, as described in [Modifying your software to use the Metering Service](#modifying-your-software-to-use-the-metering-service).

After you have your AMI, create the product and add the AMI as its first version. For the procedure, see [Create the listing](ami-single-ami-products.md#ami-create-product). If you already have the same software on AWS Marketplace and you're adding it with the AWS Marketplace Metering Service, add the usage category to the product name to tell the two products apart (for example, "PRODUCT TITLE (Data)").

You set usage pricing when you create the product's public offer.

**To start a public offer**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

   The product must have Limited or Public visibility.

1. Choose the **Procurement** tab.

1. On the **Public offer** card, choose **Create public offer**.

   The **Create public offer** page opens. Continue with the following procedures.

**To set the pricing model and dimensions**

1. On the **Set pricing model and dimensions** step, for **Pricing model**, choose **Usage pricing**.

   You can't change the pricing model later. To use a different pricing model, create a new product.

1. For **Dimension unit type**, choose the unit that customers are charged on.

   The options are **Gbps**, **Mbps**, **GB**, **MB**, **TB**, **Requests**, **Units**, **Host hours**, **Tier hours**, and **User hours**. You can't change the unit type later. If the unit differs between dimensions, choose **Units**.

1. Choose **Add usage dimension**.

1. In the panel, enter the **API identifier**, **Display name**, and **Description**, and then choose **Add dimensions**.

   The API identifier is the dimension name that your software sends in `MeterUsage` calls, and it appears in billing reports. Use up to 60 letters, numbers, and underscores, and don't start with a number. You can't change the API identifier later. The display name can have up to 80 characters, and the description can have up to 90. To add more than one dimension, choose **Add new dimension** before you choose **Add dimensions**.

1. Choose **Next**.

**To set prices and create the public offer**

1. On the **Configure pricing details and duration** step, enter the price per unit for each dimension.

   Prices can have up to 8 decimal places.

1. Complete the **Specify refund policy**, **Configure legal terms and offer documents**, and **Configure offer availability** steps.

1. On the **Review and create** step, choose **Create public offer**.

AWS Partner Central returns you to the **Procurement** tab while AWS Marketplace processes the request. When the request succeeds, your public offer appears on the **Public offer** card.

**Note**  
Free trial and annual pricing aren't compatible. 
For an **AMI with CloudFormation** product, the AWS Marketplace Metering Service integration applies to the software that runs on the instances your product launches, including instances that your CloudFormation template launches. Call `MeterUsage` from those instances by using their IAM role.
Price, instance type, or AWS Region change will follow the same process as other AWS Marketplace products.
Products with the AWS Marketplace Metering Service can't be converted to other pricing models such as hourly, monthly, or Bring Your Own License (BYOL). 
AWS Marketplace recommends adding IAM policy information in your usage instructions or document. 
You can include up to 200 usage dimensions in total. After you publish, you can add dimensions up to that limit, and you can change the display name and description of a dimension. To make these changes, choose **Update** in the **Pricing dimensions** section of the product's **Procurement** tab.

If you have questions, contact the AWS Marketplace support team on the [AWS Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1) in the AWS Partner Central console. 

## Modifying your software to use the Metering Service
<a name="modifying-your-software-to-use-the-metering-service"></a>

You will need to modify your software to record customer usage, send hourly usage reports to the Metering Service, and handle new failure modes. The software operates independently of pricing, but the software will need to know about the usage category, how it's consumed, and any dimensions. 

### Measuring consumption
<a name="measuring-consumption"></a>

Your software must determine how much of the selected usage category and which dimensions the customer has consumed. This value will be sent, once each hour, to the Metering Service. In all cases, it's assumed that your software has the ability to measure, record, and read consumption of resources for the purpose of sending it on an hourly basis to the Metering Service. 

For provisioned consumption, this will typically be read from the software configuration as a sampled value, but might also be a maximum configured value, recorded each hour. For concurrent consumption, this might be either a periodic sample or a maximum value recorded each hour. For accumulated consumption, this will be a value that is accumulated each hour. 

For pricing on multiple dimensions, multiple values must be measured and sent to the Metering Service, one per dimension. This requires your software to be programmed or configured with the known set of dimensions when you provide the AMI. You can add dimensions later. You can't change a dimension's API identifier after you create it.

For each pricing scenario, the following table describes recommended ways for measuring consumption each hour. 


|  **Scenario **  |  **How to measure **  | 
| --- | --- | 
| Provisioned user  | Current number of provisioned users (sampled). <br />-OR- <br />Maximum number of provisioned users (seen that hour).  | 
| Concurrent user  | Current number of concurrent users (sampled). <br />-OR- <br />Maximum number of concurrent users (seen that hour). <br />-OR- <br />Total number of distinct users (seen that hour).  | 
| Provisioned host  | Current number of provisioned hosts (sampled). <br />-OR- <br />Maximum number of provisioned hosts (seen that hour).  | 
| Concurrent host  | Current number of concurrent hosts (sampled). <br />-OR- <br />Maximum number of concurrent hosts (seen that hour). <br />-OR- <br />Total number of distinct hosts (seen that hour).  | 
| Provisioned bandwidth  | Current provisioned bandwidth setting (sampled). <br />-OR- <br />Maximum provisioned bandwidth (seen that hour).  | 
| Accumulated data  | Current GB of data stored (sampled). <br />-OR- <br />Maximum GB of data stored (seen that hour). <br />-OR- <br />Total GB of data added or processed that hour. <br />-OR- <br />Total GB of data processed that hour.  | 

## Vendor-metered tagging (Optional)
<a name="ami-vendor-metered-tagging"></a>

Vendor-metered tagging helps Independent Software Vendors (ISVs) give the buyer more granular insight into their software usage and can help them perform cost allocation.

To tag a buyer's software usage, you need to determine how costs are allocated. First ask your buyers what they want to see in their cost allocation. Then you can split the usage across properties that you track for the buyer’s account. Examples of properties include `Account ID`, `Business Unit`, `Cost Centers`, and other relevant metadata for your product. These properties are exposed to the buyer as tags. Using tags, buyers can view their costs split into usage by the tag values in their AWS Billing Console ([https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/)). Vendor-metered tagging doesn't change the price, dimensions, or the total usage that you report. It allows your customer to view their costs by categories appropriate to your product.

In a common use case, a buyer subscribes to your product with one AWS account. The buyer also has numerous users associated with the same product subscription. You can create usage allocations with tags that have a key of `Account ID`, and then allocate usage to each user. In this case, buyers can activate the `Account ID` tag in their Billing and Cost Management console and analyze individual user usage.

### Seller experience
<a name="ami-vendor-metered-tag-seller"></a>

Sellers can aggregate the metering records for resources with the same set of tags instead of aggregating usage for all resources. For example, sellers can construct the metering record that includes different buckets of `UsageAllocations`. Each bucket represents `UsageQuantity` for a set of tags, such as `AccountId` and `BusinessUnit`. 

In the following diagram, **Resource 1** has a unique set of `AccountId` and `BusinessUnit` tags, and appears in the **Metering Record** as a single entry. 

**Resource 2** and **Resource 3** both have the same `AccountId` tag, `2222`, and the same `BusinessUnit` tag, `Operations`. As a result, they're combined into a single `UsageAllocations` entry in the **Metering Record**.

![Diagram showing how vendor metering tags combine usage data. Three resources (Resource 1, 2, and 3) with different AccountIds and BusinessUnits are consolidated into a single Metering Record with UsageAllocations grouped by AccountId and BusinessUnit before being sent to the AWS Marketplace Metering Service.](https://docs.aws.amazon.com/marketplace/latest/userguide/images/seller-vendor-meter-tag.png)


Sellers can also combine resources without tags into a single `UsageAllocation` with the allocated usage quantity and send it as one of the entries in `UsageAllocations`.

Limits include:
+ Number of tags – 5
+ Size of `UsageAllocations` (cardinality) – 2,500

Validations include:
+ Characters allowed for the tag key and value – a-zA-Z0-9\+ -=.\_:\\/@
+ Maximum tags across `UsageAllocation` list – 5
+ Two `UsageAllocations` can't have the same tags (that is, the same combination of tag keys and values). If that's the case, they must use the same `UsageAllocation`.
+ The sum of the allocated quantities of the `UsageAllocations` must equal the `MeterUsage` request's usage quantity (`UsageQuantity` or `UsageQuantityAsDecimal`), which is the aggregate usage.
+ Each `UsageAllocation` must specify exactly one of `AllocatedUsageQuantity` or `AllocatedUsageQuantityAsDecimal`.
+ Allocations must use the same type of quantity as the `MeterUsage` request: `AllocatedUsageQuantity` with `UsageQuantity`, or `AllocatedUsageQuantityAsDecimal` with `UsageQuantityAsDecimal`.

### Buyer experience
<a name="ami-vendor-metered-tag-buyer"></a>

The following table shows an example of the buyer experience after a buyer activates the `AccountId` and `BusinessUnit` vendor tags. 

In this example, the buyer can see allocated usage in their **Cost Usage Report**. The vendor-metered tags use the prefix `“aws:marketplace:isv”`. Buyers can activate them in the Billing and Cost Management, under **Cost Allocation Tags**, **AWS-generated cost allocation tags**.

The first and last rows of the **Cost Usage Report** are relevant to what the Seller sends to the Metering Service (as shown in the [Seller experience](container-metering-meterusage.md#container-vendor-metered-tag-seller) example).


**Cost Usage Report (Simplified)**  

| ProductCode  | Buyer | UsageDimension | UsageQuantity | `aws:marketplace:isv:AccountId ` | `aws:marketplace:isv:BusinessUnit` | 
| --- | --- | --- | --- | --- | --- | 
| xyz | 111122223333 | Network: per (GB) inspected  | 70 | 2222 | Operations | 
| xyz | 111122223333 | Network: per (GB) inspected  | 30 | 3333 | Finance | 
| xyz | 111122223333 | Network: per (GB) inspected  | 20 | 4444 | IT | 
| xyz | 111122223333 | Network: per (GB) inspected  | 20 | 5555 | Marketing | 
| xyz | 111122223333 | Network: per (GB) inspected  | 30 | 1111 | Marketing | 

For a code example, see [`MeterUsage` with usage allocation tagging (Optional)](custom-metering-with-mp-metering-service.md#ami-meterusage-code-example)

## Configuring custom metering
<a name="configure-custom-metering"></a>

For more information about working with AWS Marketplace Metering Service, see [Configuring custom metering for AMI products with AWS Marketplace Metering Service](custom-metering-with-mp-metering-service.md). 