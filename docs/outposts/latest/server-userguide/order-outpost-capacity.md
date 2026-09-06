

# Create an Outpost and order Outpost capacity
<a name="order-outpost-capacity"></a>

To begin using AWS Outposts, log in with your AWS account. Create a site and an Outpost. Then, get a quote and place an order for the Outposts servers that you require.

**Prerequisites**
+ Review the [available configurations](https://aws.amazon.com/outposts/servers/pricing/) for your Outposts servers.
+ An Outpost site is the physical location for your Outpost equipment. Before ordering capacity, verify that your site meets the requirements. For more information, see [Site requirements for Outposts servers](outposts-requirements.md).
+ You must have an [AWS Enterprise Support](https://aws.amazon.com/premiumsupport/plans/enterprise/) plan or an [AWS Unified Operations](https://aws.amazon.com/premiumsupport/plans/unified-operations/) plan.
+ Determine which AWS account you will use to create the Outposts site, create the Outpost, and place the order. Monitor the email associated with this account for information from AWS.

**Topics**
+ [Step 1: Create a site](#create-site)
+ [Step 2: Create an Outpost](#create-outpost)
+ [Step 3: Create a quote](#create-quote-server)
+ [Step 4: Place the order](#place-order)
+ [Step 5: Modify instance capacity](#modify-instance-capacity)
+ [Next steps](#order-fulfillment)

## Step 1: Create a site
<a name="create-site"></a>

Create a site to specify the operating address. The operating address is the location where you will install and run your Outposts servers. After you create the site, AWS Outposts assigns an ID to your site. You must specify this site when you create an Outpost.

**Prerequisites**
+ Determine the operating address.

**To create a site**

1. Sign in to AWS.

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home).

1. To select the parent AWS Region, use the Region selector in the upper-right corner of the page.

1. In the navigation pane, choose **Sites**.

1. Choose **Create site**.

1. For **Supported hardware type**, choose **Servers only**.

1. Enter the name, description, and operating address for your site.

1. (Optional) For **Site notes**, enter any other information that might be useful for AWS to know about the site.

1. Choose **Create site**.

## Step 2: Create an Outpost
<a name="create-outpost"></a>

Create an Outpost for each server. An Outpost can only be associated with a single server. You will specify this Outpost when you create a quote and place your order.

**Prerequisites**
+ Determine the AWS Availability Zone to associate with your site.

**Unsupported Availability Zones**  
AWS Outposts doesn't support the following Availability Zones: use1-az3, usw1-az2, euw1-az2, and apne1-az3. To use AWS Outposts in these AWS Regions, select a different Availability Zone.

**To create an Outpost**

1. In the navigation pane, choose **Outposts**.

1. Choose **Create Outpost**.

1. Choose **Servers**.

1. Enter the name and a description for your Outpost.

1. Choose an Availability Zone for your Outpost.

1. For **Site ID**, choose your site.

1. Choose **Create Outpost**.

**Note**  
You won't be able to modify the AZ anchor or physical location of your Outpost after you complete the order.

## Step 3: Create a quote
<a name="create-quote-server"></a>

A quote provides a cost estimate based on your Outpost configuration. Quotes are generated within seconds and are valid for 30 days.

**Prerequisites**
+ A site with a complete operating address.
+ An Outpost associated with your site.

**To create a quote**

1. From the navigation pane, choose **Quotes**.

1. Choose **Create quote**.

1. For **General information**, provide the following:
   + **Description** (optional) – Enter a description to help differentiate between quotes. For example, include the purpose, configuration, or specific requirements of the Outpost.

1. **Country** – Select the country where your Outpost will be installed. Not all Outpost configurations are available in all countries.

1. For **Select capacities**, choose the compute capacity for your Outpost. You can select capacity in two ways:
   + **By capacity type** – Select the quantity of your desired Amazon EC2 instance types and sizes.
   + **By configuration** – Select from predefined configurations designed for common use cases, or previously used configurations from your account history.
**Note**  
You can only select instance capacities supported by your chosen Outpost generation and form factor.

1. Choose **Get quote**.

After your quote is generated, you can review the recommended Outpost configurations and pricing options. You can download your quote as a PDF for sharing or record-keeping.

**To edit a quote**
+ Navigate to the quotes page, select the quote you want to modify, choose **Actions**, and select **Edit quote**. This allows you to update your requirements and receive a revised estimate.

**Note**  
You can refresh an existing quote by using the **Refresh** button to update pricing without changing your configuration. Quotes expire after 30 days. You can recreate an expired quote by using the **Recreate quote** button, which will populate a new quote form with the same details from your expired quote.

## Step 4: Place the order
<a name="place-order"></a>

Once you have reviewed your quote, you can place your order. Each quote can only be used for a single order.

**Important**  
You can't edit an order after you submit it, so review all details carefully before submission. If you need to change an order, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/).

**Prerequisites**
+ An active Enterprise Support or Unified Operations plan.
+ An Outpost created with an associated site.
+ Determine how you will pay for the order. You can pay all upfront, partially upfront, or nothing upfront. If you choose the partial-upfront or no-upfront payment option, you'll pay monthly charges over the term. The pricing includes delivery, infrastructure service maintenance, and software patches and upgrades.
+ Determine whether the shipping address is different from the operating address that you specified for the site.

**To place an order**

1. From the navigation pane, choose **Quotes**.

1. Select the quote you want to order from and choose **Place order**.

1. If your quote was created with only a country selected, you will need to select an Outpost before proceeding.

1. For **Payment terms**, select your contract term and payment option:

   **Term length** – Choose the length of your Outpost contract:
   + **1-year contract** – Shorter commitment with higher overall costs.
   + **3-year contract** – Longer commitment with lower overall costs.
   + **5-year contract** – Longest commitment with the lowest overall costs.

   **Payment options** – Select how you want to pay:
   + **No upfront** – Pay nothing upfront and higher monthly charges throughout the contract term.
   + **Partial upfront** – Pay a portion upfront with reduced monthly charges for the remainder of the contract.
   + **All upfront** – Pay the entire contract amount upfront with no monthly charges.
**Note**  
If you are adding capacity to an existing Outpost, your order will be prorated to align with your existing Outpost's contract end date.

1. Specify the shipping address. You can specify a new address or select the site's operating address. If you select the operating address, be aware that any future change to the site's operating address will not propagate to existing orders. If you need to change the shipping address on an existing order, contact your AWS Account Manager.

1. Choose **Next**.

1. On the **Review and order** page, verify that your information is correct and edit as needed.

1. Choose **Place order**.

After placing your order, you'll receive an order confirmation with next steps via email.

**After placing your order**  
AWS will ship the Outposts server equipment, including rail mounts and required power and network cables, to the address that you provided. Your team or a third-party provider must install the equipment.

**Note**  
At the end of your contract term, you must choose between the following options at least 5 business days before your current subscription ends: renew your subscription, prepare your Outpost for return, or convert to month-to-month. If you take no action, your contract will automatically convert to a month-to-month subscription at the No Upfront rate.

## Step 5: Modify instance capacity
<a name="modify-instance-capacity"></a>

The capacity of each new Outpost order is configured with a default capacity configuration. You can convert the default configuration to create various instances to meet your business needs. To do so, you create a capacity task, specify the instance sizes and quantity, and run the capacity task to implement the changes.

**Note**  
You can change the quantity of instance sizes after you place the order for your Outposts.
Instances sizes and quantities are defined at the Outpost level.
Instances are placed automatically based on best practices.

**To modify instance capacity**

1. From the [AWS Outposts console's](https://console.aws.amazon.com/outposts/) left navigation pane, choose **Capacity tasks**.

1. On the **Capacity tasks** page, choose **Create capacity task**.

1. On the **Getting started** page, choose the order.

1. To modify capacity, you can use the steps in the console or upload a JSON file.

------
#### [ Console steps ]

1. Choose **Modify a new Outpost capacity configuration**.

1. Choose **Next**.

1. On the **Configure instance capacity** page, each instance type shows one instance size with the maximum quantity preselected. To add more instance sizes, choose **Add instance size**.

1. Specify the instance quantity and note the capacity that is displayed for that instance size.

1. View the message at the end of each instance-type section that informs you if you are over or under capacity. Make adjustments at the instance size or quantity level to optimize your total available capacity.

1. You can also request AWS Outposts to optimize the instance quantity for a specific instance size. To do so: 

   1. Choose the instance size.

   1. Choose **Auto-balance** at the end of the related instance-type section.

1. For each instance type, ensure that the instance quantity is specified for at least one instance size.

1. Choose **Next**.

1. On the **Review and create** page, verify the updates that you are requesting.

1. Choose **Create**. AWS Outposts creates a capacity task.

1. On the capacity task page, monitor the status of the task.
**Note**  
AWS Outposts might request you to stop one or more running instances to enable running the capacity task. After you stop these instances, AWS Outposts will run the task.

------
#### [ Upload JSON file ]

1. Choose **Upload a capacity configuration**.

1. Choose **Next**.

1. On the **Upload capacity configuration plan** page, upload the JSON file that specifies the instance type, size, and quantity.  
**Example**  

   Example JSON file:

   ```
   {
       "RequestedInstancePools": [
           {
               "InstanceType": "c5.24xlarge",
               "Count": 1
           },
           {
               "InstanceType": "m5.24xlarge",
               "Count": 2
           }
       ]
   }
   ```

1. Review the contents of the JSON file in the **Capacity configuration plan** section.

1. Choose **Next**.

1. On the **Review and create** page, verify the updates that you are requesting.

1. Choose **Create**. AWS Outposts creates a capacity task.

1. On the capacity task page, monitor the status of the task.
**Note**  
AWS Outposts might request you to stop one or more running instances to enable running the capacity task. After you stop these instances, AWS Outposts will run the task.

------

## Next steps
<a name="order-fulfillment"></a>

You can view the status of your order using the AWS Outposts console. The initial status of your order is **Created**. If you have any questions about your order, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/).

To fulfill the order, AWS will schedule a delivery date.

You are responsible for all installation tasks, including physical installation and network configuration. You can contract a third-party to perform these tasks for you. Whether you do the installation or contract to a third-party, installation requires IAM credentials in the AWS account that contains the Outpost to verify the identity of the new device. You are responsible for providing and managing this access. For more information, see the [Server installation guide](https://docs.aws.amazon.com/outposts/latest/install-server/install-server.html).

The installation is complete when Amazon EC2 capacity for your Outpost is available from your AWS account. After the capacity is available, you can launch Amazon EC2 instances on your Outposts server. For more information, see [Launch an instance on your Outposts server](launch-instance.md).

**Note**  
You won't be able to modify the service link configuration after you complete the order.