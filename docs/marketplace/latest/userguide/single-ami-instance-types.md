# Adding and restricting AMI instances for

AWS Marketplace

As an AWS Marketplace seller, you can manage which instances buyers can use for your single
Amazon Machine Imagine (AMI) product. You can add a new instance for your single AMI
product that buyers can use. Similarly, if you want to prevent new buyers from using your
single AMI product from a specific instance, you can restrict the instance.

For more information about the Amazon EC2 instance types, see [Available instance types](../../../AWSEC2/latest/UserGuide/instance-types.md#AvailableInstanceTypes "../../../AWSEC2/latest/UserGuide/instance-types.md#AvailableInstanceTypes") in the
_Amazon EC2 User Guide_.

The following sections explain how to add and restrict instances.

###### Topics

- [Adding an instance](#single-ami-adding-instance-types "#single-ami-adding-instance-types")
- [Restricting an instance](#single-ami-restricting-instance-types "#single-ami-restricting-instance-types")

## Adding an instance

You can add a new instance which buyers can use as a single-AMI.

###### To add an instance

1. Open the AWS Marketplace Management Portal at [https://aws.amazon.com/marketplace/management/tour/](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/"), and then sign
   in to your seller account.
2. Go to the [**Server products**](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page, and on the
   **Current server product** tab, select the product that you
   want to modify.
3. From the **Request changes** dropdown, choose **Add
   instance**.
4. Select an instance architecture.
5. Select the instance types that you want to add from the list of available
   instances.
6. Choose **Submit request** to submit your request for
   review.
7. Verify that the **Requests** tab shows the **Request
   status** as **Under review**. When the request
   completes, the status becomes **Succeeded**.

###### Note

    * If your current pricing model is not free or uses a Bring Your Own License
     (BYOL) model, you must also add prices.
    * If you created an **Add instance** with a price for the
     new instance or **Update pricing** to increase a price, you
     can’t use self-service to **Add instance** in the 90 days
     starting from the day you made the change. To make these changes, contact
     the [AWS Marketplace Seller Operations team](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/").
    * When you add support for a new instance type, customers already subscribed
     to private offers for your product won't be able to launch the newly added
     instance automatically. You must create another private offer with the
     instance you want customers to access. After accepting the new offer,
     customers can launch the newly added instance. Customers who subscribe to
     your product at a future date can also launch the instance, as long as the
     instance is included in the private offer. For more information about how to
     create a new private offer, see [Amending agreements in AWS Marketplace](private-offers-upgrades-and-renewals.md "private-offers-upgrades-and-renewals.md") later in this guide.

###### Note

**FPGA Instance Type Support**

Products with AFI IDs support F2 instance types only. You can offer your AMI on
other instance types, however, the AFIs will not be loaded on other instance types.
When buyers launch your product on non-F2 instances, the AMI will function without
the FPGA acceleration capabilities provided by the AFI IDs.

## Restricting an instance

To prevent new buyers from using an instance of an AMI product, you can restrict the instance. You can add the instance back at a later time,
if needed. Existing users of the single AMI on the restricted instance can continue to
use the product from the Region for the length of their subscriptions.

###### To restrict an instance

1. Open the AWS Marketplace Management Portal at [https://aws.amazon.com/marketplace/management/tour/](https://aws.amazon.com/marketplace/management/tour/ "https://aws.amazon.com/marketplace/management/tour/"), and then sign
   in to your seller account.
2. Go to the [**Server products**](https://aws.amazon.com/marketplace/management/products/server "https://aws.amazon.com/marketplace/management/products/server") page, and on the
   **Current server product** tab, select the product that you
   want to modify.
3. From the **Request changes** dropdown, choose
   **Restrict instance**.
4. Select the instances that you want to restrict, and choose
   **Restrict**.
5. Choose **Submit change request** to submit your request for
   review.
6. Verify that the **Requests** tab shows the **Request
   status** as **Under review**. When the request
   completes, the status becomes **Succeeded**.

###### Note

If the check box is shaded, this means the instance is associated with one
to several versions as a recommended instance type. To restrict such
instances, use **Update versions** to choose a different
recommended instance type. After the change requests complete and the
instance you want to restrict is no longer a recommended instance type, you
can return to **Restrict instance** to restrict your chosen
instance.
