# Create an order for an Outposts rack

To begin using AWS Outposts, you must create an Outpost and order Outpost capacity.

###### Prerequisites

- Review the [available
  configurations](https://aws.amazon.com/outposts/rack/pricing/ "https://aws.amazon.com/outposts/rack/pricing/") for your Outposts racks.
- An Outpost site is the physical location for your Outpost equipment. Before ordering
  capacity, verify that your site meets the requirements. For more information, see [Site requirements for Outposts racks](outposts-requirements.md "outposts-requirements.md").
- You must have an AWS Enterprise Support plan or an AWS Enterprise On-Ramp Support
  plan.
- Determine which AWS account you will use to create the Outposts site, create the
  Outpost, and place the order. Monitor the email associated with this account for information
  from AWS.

###### Tasks

- [Step 1: Create a site](#create-site "#create-site")
- [Step 2: Create an Outpost](#create-outpost "#create-outpost")
- [Step 3: Place the order](#place-order "#place-order")
- [Step 4: Modify instance capacity](#modify-instance-capacity "#modify-instance-capacity")
- [Next steps](#order-fulfillment "#order-fulfillment")

## Step 1: Create a site

Create a site to specify the operating address. The operating address is the physical
location for your Outposts racks.

###### Prerequisites

- Determine the operating address.

###### To create a site

1. Sign in to AWS.
2. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
3. To select the parent AWS Region, use the Region selector in the upper-right corner
   of the page.
4. In the navigation pane, choose **Sites**.
5. Choose **Create site**.
6. For **Supported hardware type**, choose **Racks and
   servers**.
7. Enter a name, description, and operating address for your site.
8. For **Site details**, provide the requested information about the
   site.
   - **Max weight** – The maximum rack weight that this site
     can support, in lbs.
   - **Power draw** – The power draw available at the hardware
     placement position for the rack, in kVA.
   - **Power option** – The power option that you can provide
     for the hardware.
   - **Power connector** – The power connector that AWS
     should plan to provide for connections to the hardware.
   - **Power feed drop** – Indicate whether the power feed
     comes above or below the rack.
   - **Uplink speed** – The uplink speed the rack should
     support for the connection to the Region, in Gbps.
   - **Number of uplinks** – The number of uplinks for each
     Outpost networking device that you intend to use to connect the rack to your
     network.
   - **Fiber type** – The type of fiber that you will use to
     attach the rack to your network.
   - **Optical standard** – The type of optical standard that
     you will use to attach the rack to your network.

9. (Optional) For **Site notes**, enter any other information that might
   be useful for AWS to know about the site.
10. Read the facility requirements, and then select **I have read the facility
    requirements**.
11. Choose **Create site**.

## Step 2: Create an Outpost

Create an Outpost for your racks. Then, specify this Outpost when you place your
order.

###### Prerequisites

- Determine the AWS Availability Zone to associate with your site.

###### To create an Outpost

1. In the navigation pane, choose **Outposts**.
2. Choose **Create Outpost**.
3. Choose **Racks**.
4. Enter a name and description for your Outpost.
5. Choose an Availability Zone for your Outpost.
6. (Optional) To configure private connectivity, select **Use Private
   connectivity**. Choose a VPC and subnet in the same AWS account and
   Availability Zone as your Outpost. For more information, see [Prerequisites](private-connectivity.md#private-connectivity-prerequisites "private-connectivity.md#private-connectivity-prerequisites").

###### Note

If you need to remove the private connectivity for your Outpost, you must contact
[AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/"). 7. For **Site ID**, choose your site. 8. Choose **Create Outpost**.

###### Note

You won't be able to modify the AZ anchor or physical location of your Outpost after
you complete the order.

## Step 3: Place the order

Place an order for the Outposts racks that you need.

###### Important

You can't edit an order after you submit it so review all details carefully before
submission. If you need to change an order, contact your AWS Account Manager.

###### Prerequisites

- Determine how you will pay for the order. You can pay all upfront, partially upfront,
  or nothing upfront. If you do not choose to pay all upfront, you'll pay monthly charges
  over the contract term.

The pricing includes delivery, installation, infrastructure service maintenance, and
software patches and upgrades.

- Determine whether the delivery address is different than the operating address that
  you specified for the site.

###### To place an order

1. From the navigation pane, choose **Orders**.
2. Choose **Place order**.
3. For **Supported hardware type**, choose
   **Racks**.
4. For **Configurations**, specify the quantity for each
   resource that you need. If the available configurations do not meet your
   capacity needs, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") to request a custom capacity
   configuration.
5. For **Storage**:
   - Choose an Amazon EBS storage tier.
   - (Optional) Choose an Amazon S3 storage tier.

6. Choose **Next**.
7. Choose **Use an existing Outpost** and select your Outpost.
8. Choose **Next**.
9. Enter the name and number of the contact person at the operating site.
10. Specify the shipping address. You can specify a new address or select the site's
    operating address. If you select the operating address, be aware that any future change to
    the site's operating address will not propagate to existing orders. If you need to change
    the name and address of the shipping location on an existing order, contact your AWS
    Account Manager.
11. For **Site details**, specify your site information for each field.
12. Review the **Facility requirements**.
13. Select **I have read the facility requirements**.
14. Choose **Next**.
15. Select a contract term and payment option.
16. Choose **Next**.
17. On the **Review and order** page, verify that your information is
    correct and edit as needed. You will not be able to edit the order after you submit
    it.
18. Choose **Place order**.

## Step 4: Modify instance capacity

An Outpost provides a pool of AWS compute and storage capacity at your
site as a private extension of an Availability Zone in an AWS Region. Because the compute
and storage capacity available in the Outpost is finite and determined by the size and number
of racks that AWS installs at your site, you get to decide how much Amazon EC2, Amazon EBS, and Amazon S3
on AWS Outposts capacity you need to run your initial workloads, accommodate future growth, and to
provide extra capacity to mitigate server failures and maintenance events.

The capacity of each new Outpost order is configured with a default capacity
configuration. You can convert the default configuration to create various instances to meet
your business needs. To do so, you create a capacity task, specify the instance sizes and
quantity, and run the capacity task to implement the changes.

###### Note

- You can change the quantity of instance sizes after you place the order for your
  Outposts.
- Instances sizes and quantities are defined at the Outpost level.
- Instances are placed automatically based on best practices.

###### To modify instance capacity

1. From the [AWS Outposts console's](https://console.aws.amazon.com/outposts/ "https://console.aws.amazon.com/outposts/")
   left navigation pane, choose **Capacity tasks**.
2. On the **Capacity tasks** page, choose **Create capacity
   task**.
3. On the **Getting started** page, choose the order.
4. To modify capacity, you can use the steps in the console or upload a JSON file.

Console steps

1. Choose **Modify an Outpost capacity configuration**.
2. Choose **Next**.
3. On the **Configure instance capacity** page, each instance type
   shows one instance size with the maximum quantity preselected. To add more instance
   sizes, choose **Add instance size**.
4. Specify the instance quantity and note the capacity that is displayed for that
   instance size.
5. View the message at the end of each instance-type section that informs you if
   you are over or under capacity. Make adjustments at the instance size or quantity
   level to optimize your total available capacity.
6. You can also request AWS Outposts to optimize the instance quantity for a specific
   instance size. To do so:
   1. Choose the instance size.
   2. Choose **Auto-balance** at the end of the related
      instance-type section.

7. For each instance type, ensure that the instance quantity is specified for at
   least one instance size.
8. Choose **Next**.
9. On the **Review and create** page, verify the updates that you
   are requesting.
10. Choose **Create**. AWS Outposts creates a capacity task.
11. On the capacity task page, monitor the status of the task.

###### Note

    * AWS Outposts might request you to stop one or more running instances to enable
     running the capacity task. After you stop these instances, AWS Outposts will run the
     task.
    * If you need to change your capacity after you complete your order, contact
     [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") to make the changes.

Upload a JSON file

1. Choose **Upload a capacity configuration**.
2. Choose **Next**.
3. On the **Upload capacity configuration plan** page, upload the
   JSON file that specifies the instance type, size, and quantity.

###### Example

Example JSON file:

```
{
    "InstancePools": [
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
6. On the **Review and create** page, verify the updates that you
   are requesting.
7. Choose **Create**. AWS Outposts creates a capacity task.
8. On the capacity task page, monitor the status of the task.

###### Note

    * AWS Outposts might request you to stop one or more running instances to enable
     running the capacity task. After you stop these instances, AWS Outposts will run the
     task.
    * If you need to change your capacity after you complete your order, contact
     [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") to make the changes.
    * To troubleshoot issues, see [Troubleshooting
     capacity task issues](order-troubleshooting.md "order-troubleshooting.md").

## Next steps

You can view the status of your order using the AWS Outposts console. The initial status of
your order is **Order received**. If you have any questions about your order,
contact [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

To fulfill the order, AWS will schedule a date and time with you.

You will also receive a checklist of items to verify or provide before the installation.
The AWS installation team will arrive at your site at the scheduled date and time. The team
will roll the rack to the identified position and your electrician can power the rack. The
team will establish network connectivity for the rack over the uplink that you provide, and
will configure the rack's capacity. The installation is complete when you confirm that the
Amazon EC2 and Amazon EBS capacity for your Outpost is available from your AWS account.
