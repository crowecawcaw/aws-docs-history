

# Adding and restricting AMI instances for AWS Marketplace

As an AWS Marketplace seller, you can manage which instances buyers can use for your single Amazon Machine Imagine (AMI) product. You can add a new instance for your single AMI product that buyers can use. Similarly, if you want to prevent new buyers from using your single AMI product from a specific instance, you can restrict the instance. 

For more information about the Amazon EC2 instance types, see [Available instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes) in the *Amazon EC2 User Guide*.

The following sections explain how to add and restrict instances.

**Topics**
+ [Adding an instance](#single-ami-adding-instance-types)
+ [Restricting an instance](#single-ami-restricting-instance-types)

## Adding an instance
<a name="single-ami-adding-instance-types"></a>

You can add a new instance which buyers can use as a single-AMI.

**To add instance types**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. On the **Delivery** tab, in the **Instance type configuration** section, choose **Add instance types**.

   For a new product, you can instead choose **Start** on the **Add instance types** card under **Step 2: Delivery configuration**. On a new product, **Add instance types** and this card are available after you complete the **Add Regions** card.

1. If your product doesn't have a version yet, under **Architecture**, for **AMI architecture**, choose **x86\_64** or **arm64**.

   After your product has a version, this section doesn't appear, and the console uses the architecture of your product's AMI.

1. In the **All instance types** table, select the instance types to add.

   You can't select instance types marked **Incompatible AMI architecture**, **Incompatible Virtualization type**, or **Existing In Product**.

1. (Optional) Under **Tags**, add tags to the change request.

1. Choose **Save instance types**.

   If your public offer has usage-based prices, such as **Hourly**, choose **Next** instead, and then complete the following procedure.

**To set prices for new instance types**

1. On the **Set prices** step, enter the **Price/hr** for each new instance type.

   If the offer has an annual pricing term, also enter the **Annual upfront commitment price**. To use one price for every new instance type, enter it under **Pricing tool**, and then choose **Apply to all**.

1. Choose **Next**.

1. On the **Review and submit** step, choose **Submit**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

**Note**  
Prices are in the currency of your public offer. Hourly prices can have up to 8 decimal places, and annual prices up to 3. Instance types already on the offer keep their prices, which appear read-only under **Public offer price**. If the offer has a free trial, the request also adds the new instance types to the trial.
When you add support for a new instance type, customers already subscribed to private offers for your product can't launch the newly added instance type automatically. You must create another private offer that includes it. For more information, see [Amending agreements in AWS Marketplace](private-offers-upgrades-and-renewals.md).

**Note**  
**FPGA Instance Type Support**  
Products with AFI IDs support F2 instance types only. You can offer your AMI on other instance types, however, the AFIs will not be loaded on other instance types. When buyers launch your product on non-F2 instances, the AMI will function without the FPGA acceleration capabilities provided by the AFI IDs.

## Restricting an instance
<a name="single-ami-restricting-instance-types"></a>

To prevent new buyers from using an instance of an AMI product, you can restrict the instance. You can add the instance back at a later time, if needed. Existing users of the single AMI on the restricted instance can continue to use the product from the Region for the length of their subscriptions.

**To restrict instance types**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Instance type configuration** section, in the **Instance types** table, select the instance types to restrict.

   You can't select an instance type that a version recommends. The **Vendor recommendation** column shows how many versions recommend it. To restrict it, first choose a different recommended instance type in each of those versions. For more information, see [Update version information](single-ami-versions.md#single-ami-updating-version).

1. Choose **Restrict instance types**.

   This button is available after your product has at least one version. You must keep at least one instance type available.

1. In the confirmation dialog box, choose **Restrict instance types**.

   If you selected one instance type, the button is **Restrict instance type**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.