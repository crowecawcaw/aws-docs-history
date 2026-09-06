# Create an order for an Outposts rack

To begin using AWS Outposts, you must create a site, create an Outpost, get a quote, and place
your order.

###### Prerequisites

- Review the [available
  configurations](https://aws.amazon.com/outposts/rack/pricing/ "https://aws.amazon.com/outposts/rack/pricing/") for your Outposts racks.
- An Outpost site is the physical location for your Outpost equipment. Before ordering
  capacity, verify that your site meets the requirements. For more information, see [Site requirements for Outposts racks](outposts-requirements.md "outposts-requirements.md").
- You must have an [AWS Enterprise Support](https://aws.amazon.com/premiumsupport/plans/enterprise/ "https://aws.amazon.com/premiumsupport/plans/enterprise/") plan or an [AWS Unified
  Operations](https://aws.amazon.com/premiumsupport/plans/unified-operations/ "https://aws.amazon.com/premiumsupport/plans/unified-operations/") plan.
- Determine which AWS account you will use to create the Outposts site, create the
  Outpost, and place the order. Monitor the email associated with this account for information
  from AWS.

###### Tasks

- [Step 1: Create a site](#create-site "#create-site")
- [Step 2: Create an Outpost](#create-outpost "#create-outpost")
- [Step 3: Create a quote](#create-quote "#create-quote")
- [Step 4: Place the order](#place-order "#place-order")
- [Step 5: Modify instance capacity](#modify-instance-capacity "#modify-instance-capacity")
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
     can support, in lbs. Check your floor's load rating with your facilities team or
     structural engineer and multiply it by the rack footprint (approximately 6 square feet
     for a 42U rack).
   - **Power draw** – The power draw available at the hardware
     placement position for the rack, in kVA. Check the capacity of the circuit breakers or
     power distribution units (PDUs) available for the rack.
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

Create an Outpost for your racks. You will specify this Outpost when you create a quote
and place your order.

###### Prerequisites

- Determine the AWS Availability Zone to associate with your site.

###### Unsupported Availability Zones

AWS Outposts doesn't support the following Availability Zones: use1-az3, usw1-az2, euw1-az2, and apne1-az3. To use
AWS Outposts in these AWS Regions, select a different Availability Zone.

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

## Step 3: Create a quote

A quote provides a cost estimate based on your Outpost configuration. It includes rack
configurations showing what your setup will look like if the order is placed. Quotes are
generated within seconds and are valid for 30 days.

###### To create a quote

1. From the navigation pane, choose **Quotes**.
2. Choose **Create quote**.
3. For **General information**, provide the following:

   - **Description** (optional) – Enter a description to help
     differentiate between quotes. For example, include the purpose, configuration, or
     specific requirements of the Outpost.
   - **Outpost type** – Select **New
     outpost** if you are creating a new Outpost, or **Existing
     outpost** if you are expanding the capacity of an already deployed
     Outpost.

###### Note

Outposts on a month-to-month subscription cannot be scaled. To scale, you must
first renew your term. 4. **Country** (new Outpost) – Select the country where your
Outpost will be installed. Not all Outpost configurations are available in all
countries.

**Outpost ID** (existing Outpost) – Select the Outpost ID for
the Outpost you want to add capacity to. 5. For **Select capacities**, choose the compute capacity for your
Outpost. You can select capacity in two ways:

    * **By capacity type** – Select the quantity of your desired
     Amazon EC2 instance types and sizes.
    * **By configuration** – Select from predefined
     configurations designed for common use cases, or previously used configurations from
     your account history.

###### Note

You can only select instance capacities supported by your chosen Outpost generation
and form factor. 6. For **Storage types**, select the storage capacity for your
Outpost:

    * **EBS storage (in TB)** – Select an Amazon EBS storage capacity
     tier to provide persistent block storage for your Amazon EC2 instances.
    * **S3 storage (in TB)** (optional) – Add Amazon S3 on Outposts
     capacity for local object storage.

###### Note

Your input will be rounded up to the nearest supported storage tier. Amazon S3 on Outposts
storage may not be available in all regions. 7. (Optional) For **Site details**, provide your site's power, space,
and weight limits. While optional for quotes, providing site details helps ensure the
recommended configuration is suitable for your facility and may affect your estimated
quote.

###### Note

Complete site information including operating address, shipping address, and rack
physical properties will be required to place your order. 8. Choose **Get quote**.

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
submission. If you need to change an order, contact your AWS Account Manager.

###### Prerequisites

- An active Enterprise Support or Unified Operations plan.
- An Outpost created with an associated site.
- Complete site details including operating address, shipping address, and rack physical
  properties.
- Determine how you will pay for the order. You can pay all upfront, partially upfront,
  or nothing upfront. If you choose partial upfront or no upfront, you'll pay monthly
  charges over the contract term.

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

    * **1-year contract** – Shorter commitment with higher
     overall costs.
    * **3-year contract** – Longer commitment with lower overall
     costs.

**Payment options** – Select how you want to pay:

    * **No upfront** – Pay nothing upfront and higher monthly
     charges throughout the contract term.
    * **Partial upfront** – Pay a portion upfront with reduced
     monthly charges for the remainder of the contract.
    * **All upfront** – Pay the entire contract amount upfront
     with no monthly charges.

###### Note

If you are adding capacity to an existing Outpost, your order will be prorated to
align with your existing Outpost's contract end date. 5. Choose **Next**. 6. On the **Review and order** page, verify that your information is
correct and edit as needed. 7. Choose **Place order**.

After placing your order, you'll receive an order confirmation with next steps via
email.

###### After placing your order

An AWS team will work with you to:

- Finalize site preparation requirements.
- Schedule a site assessment to verify site readiness.
- Coordinate installation scheduling.
- Complete any additional compliance or regulatory requirements for your region.

Once readiness is validated, your Outpost will be manufactured and delivered. An AWS
technician will arrive on-site to begin installation, which involves powering up the rack,
performing basic configuration, and validating that the Outpost networking devices can
establish encrypted connectivity to the AWS Region.

###### Note

At the end of your contract term, you must choose between the following options at least
5 business days before your current subscription ends: renew your subscription, prepare your
Outpost for return, or convert to month-to-month. If you take no action, your contract will
automatically convert to a month-to-month subscription at the No Upfront rate.

## Step 5: Modify instance capacity

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
your order is **Created**. If you have any questions about your order,
contact [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

To fulfill the order, AWS will schedule a date and time with you.

You will also receive a checklist of items to verify or provide before the installation.
The AWS installation team will arrive at your site at the scheduled date and time. The team
will roll the rack to the identified position and your electrician can power the rack. The
team will establish network connectivity for the rack over the uplink that you provide, and
will configure the rack's capacity. The installation is complete when you confirm that the
Amazon EC2 and Amazon EBS capacity for your Outpost is available from your AWS account.
