# Create an Outpost and order Outpost capacity

To begin using AWS Outposts, log in with your AWS account. Create a
site and an Outpost. Then, get a quote and place an order for the Outposts servers that you
require.

###### Prerequisites

- Review the [available
  configurations](https://aws.amazon.com/outposts/servers/pricing/ "https://aws.amazon.com/outposts/servers/pricing/") for your Outposts servers.
- An Outpost site is the physical location for your Outpost equipment. Before ordering
  capacity, verify that your site meets the requirements. For more information, see [Site requirements for Outposts servers](outposts-requirements.md "outposts-requirements.md").
- You must have an [AWS Enterprise Support](https://aws.amazon.com/premiumsupport/plans/enterprise/ "https://aws.amazon.com/premiumsupport/plans/enterprise/") plan or an [AWS Unified
  Operations](https://aws.amazon.com/premiumsupport/plans/unified-operations/ "https://aws.amazon.com/premiumsupport/plans/unified-operations/") plan.
- Determine which AWS account you will use to create the
  Outposts site, create the Outpost, and place the order. Monitor the email associated with
  this account for information from AWS.

###### Tasks

- [Step 1: Create a site](#create-site "#create-site")
- [Step 2: Create an Outpost](#create-outpost "#create-outpost")
- [Step 3: Create a quote](#create-quote-server "#create-quote-server")
- [Step 4: Place the order](#place-order "#place-order")
- [Step 5: Modify instance capacity](#modify-instance-capacity "#modify-instance-capacity")
- [Next steps](#order-fulfillment "#order-fulfillment")

## Step 1: Create a site

Create a site to specify the operating address. The operating address is the location where
you will install and run your Outposts servers. After you create the site, AWS Outposts assigns an
ID to your site. You must specify this site when you create an Outpost.

###### Prerequisites

- Determine the operating address.

###### To create a site

1. Sign in to AWS.
2. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
3. To select the parent AWS Region, use the Region selector in the upper-right corner of
   the page.
4. In the navigation pane, choose **Sites**.
5. Choose **Create site**.
6. For **Supported hardware type**, choose **Servers
   only**.
7. Enter the name, description, and operating address for your site.
8. (Optional) For **Site notes**, enter any other information that might be
   useful for AWS to know about the site.
9. Choose **Create site**.

## Step 2: Create an Outpost

Create an Outpost for each server. An Outpost can only be associated with a single server.
You will specify this Outpost when you create a quote and place your order.

###### Prerequisites

- Determine the AWS Availability Zone to associate with your site.

###### Unsupported Availability Zones

AWS Outposts doesn't support the following Availability Zones: use1-az3, usw1-az2, euw1-az2, and apne1-az3. To use
AWS Outposts in these AWS Regions, select a different Availability Zone.

###### To create an Outpost

1. In the navigation pane, choose **Outposts**.
2. Choose **Create Outpost**.
3. Choose **Servers**.
4. Enter the name and a description for your Outpost.
5. Choose an Availability Zone for your Outpost.
6. For **Site ID**, choose your site.
7. Choose **Create Outpost**.

###### Note

You won't be able to modify the AZ anchor or physical location of your Outpost after you
complete the order.

## Step 3: Create a quote

A quote provides a cost estimate based on your Outpost configuration. Quotes are
generated within seconds and are valid for 30 days.

###### Prerequisites

- A site with a complete operating address.
- An Outpost associated with your site.

###### To create a quote

1. From the navigation pane, choose **Quotes**.
2. Choose **Create quote**.
3. For **General information**, provide the following:

   - **Description** (optional) – Enter a description to help
     differentiate between quotes. For example, include the purpose, configuration, or specific
     requirements of the Outpost.

4. **Country** – Select the country where your Outpost will be
   installed. Not all Outpost configurations are available in all countries.
5. For **Select capacities**, choose the compute capacity for your
   Outpost. You can select capacity in two ways:

   - **By capacity type** – Select the quantity of your desired
     Amazon EC2 instance types and sizes.
   - **By configuration** – Select from predefined configurations
     designed for common use cases, or previously used configurations from your account
     history.

###### Note

You can only select instance capacities supported by your chosen Outpost generation
and form factor. 6. Choose **Get quote**.

After your quote is generated, you can review the recommended Outpost configurations and
pricing options. You can download your quote as a PDF for sharing or record-keeping.

###### To edit a quote

- Navigate to the quotes page, select the quote you want to modify, choose
  **Actions**, and select **Edit quote**. This allows you
  to update your requirements and receive a revised estimate.

###### Note

You can refresh an existing quote by using the **Refresh** button to
update pricing without changing your configuration. Quotes expire after 30 days. You can
recreate an expired quote by using the **Recreate quote** button, which
will populate a new quote form with the same details from your expired quote.

## Step 4: Place the order

Once you have reviewed your quote, you can place your order. Each quote can only be used
for a single order.

###### Important

You can't edit an order after you submit it, so review all details carefully before
submission. If you need to change an order, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

###### Prerequisites

- An active Enterprise Support or Unified Operations plan.
- An Outpost created with an associated site.
- Determine how you will pay for the order. You can pay all upfront, partially upfront, or
  nothing upfront. If you choose the partial-upfront or no-upfront payment option, you'll pay
  monthly charges over the term. The pricing includes delivery, infrastructure service
  maintenance, and software patches and upgrades.
- Determine whether the shipping address is different from the operating address that you
  specified for the site.

###### To place an order

1. From the navigation pane, choose **Quotes**.
2. Select the quote you want to order from and choose **Place
   order**.
3. If your quote was created with only a country selected, you will need to select an
   Outpost before proceeding.
4. For **Payment terms**, select your contract term and payment
   option:

**Term length** – Choose the length of your Outpost
contract:

    * **1-year contract** – Shorter commitment with higher overall
     costs.
    * **3-year contract** – Longer commitment with lower overall
     costs.
    * **5-year contract** – Longest commitment with the lowest
     overall costs.

**Payment options** – Select how you want to pay:

    * **No upfront** – Pay nothing upfront and higher monthly
     charges throughout the contract term.
    * **Partial upfront** – Pay a portion upfront with reduced
     monthly charges for the remainder of the contract.
    * **All upfront** – Pay the entire contract amount upfront
     with no monthly charges.

###### Note

If you are adding capacity to an existing Outpost, your order will be prorated to
align with your existing Outpost's contract end date. 5. Specify the shipping address. You can specify a new address or select the site's operating
address. If you select the operating address, be aware that any future change to the site's
operating address will not propagate to existing orders. If you need to change the shipping
address on an existing order, contact your AWS Account Manager. 6. Choose **Next**. 7. On the **Review and order** page, verify that your information is correct
and edit as needed. 8. Choose **Place order**.

After placing your order, you'll receive an order confirmation with next steps via
email.

###### After placing your order

AWS will ship the Outposts server equipment, including rail mounts and required power
and network cables, to the address that you provided. Your team or a third-party provider must
install the equipment.

###### Note

At the end of your contract term, you must choose between the following options at least
5 business days before your current subscription ends: renew your subscription, prepare your
Outpost for return, or convert to month-to-month. If you take no action, your contract will
automatically convert to a month-to-month subscription at the No Upfront rate.

## Step 5: Modify instance capacity

The capacity of each new Outpost order is configured with a default capacity configuration.
You can convert the default configuration to create various instances to meet your business
needs. To do so, you create a capacity task, specify the instance sizes and quantity, and run the
capacity task to implement the changes.

###### Note

- You can change the quantity of instance sizes after you place the order for your
  Outposts.
- Instances sizes and quantities are defined at the Outpost level.
- Instances are placed automatically based on best practices.

###### To modify instance capacity

1. From the [AWS Outposts
   console's](https://console.aws.amazon.com/outposts/ "https://console.aws.amazon.com/outposts/") left navigation pane, choose **Capacity tasks**.
2. On the **Capacity tasks** page, choose **Create capacity
   task**.
3. On the **Getting started** page, choose the order.
4. To modify capacity, you can use the steps in the console or upload a JSON file.

Console steps

1. Choose **Modify a new Outpost capacity configuration**.
2. Choose **Next**.
3. On the **Configure instance capacity** page, each instance type shows
   one instance size with the maximum quantity preselected. To add more instance sizes, choose
   **Add instance size**.
4. Specify the instance quantity and note the capacity that is displayed for that instance
   size.
5. View the message at the end of each instance-type section that informs you if you are
   over or under capacity. Make adjustments at the instance size or quantity level to optimize
   your total available capacity.
6. You can also request AWS Outposts to optimize the instance quantity for a specific instance
   size. To do so:

   1. Choose the instance size.
   2. Choose **Auto-balance** at the end of the related instance-type
      section.

7. For each instance type, ensure that the instance quantity is specified for at least one
   instance size.
8. Choose **Next**.
9. On the **Review and create** page, verify the updates that you are
   requesting.
10. Choose **Create**. AWS Outposts creates a capacity task.
11. On the capacity task page, monitor the status of the task.

###### Note

AWS Outposts might request you to stop one or more running instances to enable running the
capacity task. After you stop these instances, AWS Outposts will run the task.

Upload JSON file

1. Choose **Upload a capacity configuration**.
2. Choose **Next**.
3. On the **Upload capacity configuration plan** page, upload the JSON
   file that specifies the instance type, size, and quantity.

###### Example

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

4. Review the contents of the JSON file in the **Capacity configuration
   plan** section.
5. Choose **Next**.
6. On the **Review and create** page, verify the updates that you are
   requesting.
7. Choose **Create**. AWS Outposts creates a capacity task.
8. On the capacity task page, monitor the status of the task.

###### Note

AWS Outposts might request you to stop one or more running instances to enable running the
capacity task. After you stop these instances, AWS Outposts will run the task.

## Next steps

You can view the status of your order using the AWS Outposts console. The initial status of
your order is **Created**. If you have any questions about your order, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

To fulfill the order, AWS will schedule a delivery date.

You are responsible for all installation tasks, including physical installation and network
configuration. You can contract a third-party to perform these tasks for you. Whether you do the
installation or contract to a third-party, installation requires IAM credentials in the
AWS account that contains the Outpost to verify the identity of the new device. You are
responsible for providing and managing this access. For more information, see the [Server installation guide](../install-server/install-server.md "../install-server/install-server.md").

The installation is complete when Amazon EC2 capacity for your Outpost is available from your
AWS account. After the capacity is available, you can launch Amazon EC2 instances on your Outposts server.
For more information, see [Launch an instance on your Outposts server](launch-instance.md "launch-instance.md").

###### Note

You won't be able to modify the service link configuration after you complete the
order.
