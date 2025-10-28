# Create an Outpost and order Outpost capacity

To begin using AWS Outposts, log in with your AWS account. Create a
site and an Outpost. Then, place an order for the Outposts servers that you require.

###### Prerequisites

- Review the [available
  configurations](https://aws.amazon.com/outposts/servers/pricing/ "https://aws.amazon.com/outposts/servers/pricing/") for your Outposts servers.
- An Outpost site is the physical location for your Outpost equipment. Before ordering
  capacity, verify that your site meets the requirements. For more information, see [Site requirements for Outposts servers](outposts-requirements.md "outposts-requirements.md").
- You must have an AWS Enterprise Support plan or an AWS Enterprise On-Ramp Support plan.
- Determine which AWS account you will use to create the
  Outposts site, create the Outpost, and place the order. Monitor the email associated with
  this account for information from AWS.

###### Tasks

- [Step 1: Create a site](#create-site "#create-site")
- [Step 2: Create an Outpost](#create-outpost "#create-outpost")
- [Step 3: Place the order](#place-order "#place-order")
- [Step 4: Modify instance capacity](#modify-instance-capacity "#modify-instance-capacity")
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
You'll specify this Outpost when you place the order.

###### Prerequisites

- Determine the AWS Availability Zone to associate with your site.

###### To create an Outpost

1. In the navigation pane, choose **Outposts**.
2. Choose **Create Outpost**.
3. Choose **Servers**.
4. Enter the name and a description for your Outpost.
5. Choose an Availability Zone for your Outpost.
6. For **Site ID**, choose your site.
7. Choose **Create Outpost**.

## Step 3: Place the order

Place an order for the Outposts servers that you need.

###### Important

You can't edit an order after you submit it so review all details carefully before
submission. If you need to change an order, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

###### Prerequisites

- Determine how you will pay for the order. You can pay all upfront, partially upfront, or
  nothing upfront. If you choose the partial-upfront or no-upfront payment option, you'll pay
  monthly charges over the term.

The pricing includes delivery, infrastructure service maintenance, and software patches
and upgrades.

- Determine whether the shipping address is different from the operating address that you
  specified for the site.

###### To place an order

1. In the navigation pane, choose **Orders**.
2. Choose **Place order**.
3. For **Supported hardware type**, choose
   **Servers**.
4. To add capacity, choose a configuration.
5. Choose **Next**.
6. Choose **Use an existing Outpost** and select your Outpost.
7. Choose **Next**.
8. Select a contract term and payment option.
9. Specify the shipping address. You can specify a new address or select the site's operating
   address. If you select the operating address, be aware that any future change to the site's
   operating address will not propagate to existing orders. If you need to change the shipping
   address on an existing order, contact your AWS Account Manager.
10. Choose **Next**.
11. On the **Review and order** page, verify that your information is correct
    and edit as needed. You will not be able to edit the order after you submit it.
12. Choose **Place order**.

## Step 4: Modify instance capacity

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
   console's](https://console.aws.amazon.com/outposts/ "https://console.aws.amazon.com/outposts/")AWS Outposts left navigation pane, choose **Capacity tasks**.
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
your order is **Order received**. If you have any questions about your order, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

To fulfill the order, AWS will schedule a delivery date.

You are responsible for all installation tasks, including physical installation and network
configuration. You can contract a third-party to perform these tasks for you. Whether you do the
installation or contract to a third-party, installation requires IAM credentials in the
AWS account that contains the Outpost to verify the identity of the new device. You are
responsible for providing and managing this access. For more information, see the [Server installation guide](../install-server/install-server.md "../install-server/install-server.md").

The installation is complete when Amazon EC2 capacity for your Outpost is available from your
AWS account. After the capacity is available, you can launch Amazon EC2 instances on your Outposts server.
For more information, see [Launch an instance on your Outposts server](launch-instance.md "launch-instance.md").
