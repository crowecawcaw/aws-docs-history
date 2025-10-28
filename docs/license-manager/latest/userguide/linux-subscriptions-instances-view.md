# View discovered instance data in

License Manager

After License Manager completes the initial resource discovery process in your selected
AWS Regions, you can view the results in the console. If you chose to link AWS Organizations,
License Manager aggregates data from accounts across your organization. To view a list of
instances with subscriptions that meet your filter criteria, navigate to the
**Instances** section of the AWS License Manager console. The list displays
the following key fields.

- **Instance ID** – The ID of the instance.
- **Status** – The status of the instance.
- **Instance type** – The type of instance.
- **Subscription** – The name of the license
  subscription that the instance uses.
- **Duplicates alert** – Indicates that you have
  two different license subscriptions for the same software on your instance.
- **Account ID** – The ID of the account which owns the
  instance.
- **Region** – The AWS Region in which the instance
  resides.
- **AMI ID** – The ID of the AMI used to launch the
  instance.
- **Usage operation** – The operation of the instance
  and the billing code that is associated with the AMI. For more information, see
  [Usage operation values](conversion-types-windows.md#usage-operation-values "conversion-types-windows.md#usage-operation-values").
- **Product code** – The product code associated with
  the AMI used to launch the instance. For more information, see [AMI product
  codes](../../../marketplace/latest/userguide/ami-getting-started.md#ami-product-codes "../../../marketplace/latest/userguide/ami-getting-started.md#ami-product-codes").
- **LastUpdatedTime** – The time in which the last
  discovery updated the instance details.

###### Topics

- [View data for all instances](#linux-subscriptions-instances-view-all "#linux-subscriptions-instances-view-all")
- [View data for instances by
  subscription](#linux-subscriptions-instances-view-subscription "#linux-subscriptions-instances-view-subscription")

## View data for all instances

You can view and filter Linux subscription data that License Manager discovered for the instances
in your account or AWS Organizations, as follows.

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, under Linux subscriptions, choose
   **Instances**. This displays a list of instances with
   Linux subscription data.
3. (Optional) You can use the following filters to streamline your results:
   - Account
   - AMI ID
   - Duplicate subscription
   - Instance ID
   - Region
   - Product code
   - Usage operation

4. (Optional) Choose **Export view to CSV** to export data for all of your
   instances as a comma-separated values file (CSV).

## View data for instances by

subscription

You can view data for all instances has have been aggregated across accounts in your
organization within the chosen Regions.

###### To view discovered data for instances with a specific subscription

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, under Linux subscriptions, choose
   **Subscriptions**.
3. Under the **Subscription name** column, choose the subscription you
   would like to view data for.
4. Choose the **Instances** tab and review the data as needed in the
   console. You can filter the data by:
   - Instance ID
   - Account
   - Region
   - AMI ID
   - Usage operation
   - Product code

5. (Optional) Choose **Export view to CSV** to export data for your
   instances with this subscription as a comma-separated values file (CSV).
