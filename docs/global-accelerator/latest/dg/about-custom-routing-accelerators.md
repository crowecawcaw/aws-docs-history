

# Custom routing accelerators in AWS Global Accelerator
<a name="about-custom-routing-accelerators"></a>

A *custom routing accelerator* in AWS Global Accelerator lets you use custom application logic to direct one or more users to a specific destination among many destinations, while using the AWS global network to improve the availability and performance of your application. 

A custom routing accelerator routes traffic only to ports on Amazon EC2 instances that are running in virtual private cloud (VPC) subnets. With a custom routing accelerator, Global Accelerator does not route traffic based on the geoproximity or health of the endpoint. To learn more, see [How custom routing accelerators work in Global Accelerator](about-custom-routing-how-it-works.md).

When you create an accelerator, by default, Global Accelerator provides you with a set of two static IPv4 addresses. Custom routing accelerators support only the IPv4 IP address type. If you bring your own IP address range to AWS (BYOIP), you can assign static IPv4 addresses from your own pool to use with your accelerator. For more information, see [Bring your own IP addresses (BYOIP) in Global Accelerator](using-byoip.md).

**Important**  
The IP addresses are assigned to your accelerator for as long as it exists, even if you disable the accelerator and it no longer accepts or routes traffic. However, when you *delete* an accelerator, you lose the Global Accelerator static IP addresses that are assigned to the accelerator, so you can no longer route traffic by using them. As a best practice, ensure that you have permissions in place to avoid inadvertently deleting accelerators. You can use IAM policies such as tag-based permissions with Global Accelerator to limit the users who have permissions to delete an accelerator. For more information, see [ABAC with Global Accelerator](security_iam_service-with-iam.md#security_iam_service-with-iam-tags).

This section explains how to work with a custom routing accelerator on the Global Accelerator console. To learn about using API operations with Global Accelerator, see the [AWS Global Accelerator API Reference](https://docs.aws.amazon.com/global-accelerator/latest/api/Welcome.html).

**Topics**
+ [Create a custom routing accelerator](about-custom-routing-accelerators.creating-editing.md)
+ [Edit a custom routing accelerator](about-custom-routing-accelerators.editing.md)
+ [View custom routing accelerators](about-custom-routing-accelerators.viewing.md)
+ [Delete a custom routing accelerator](about-custom-routing-accelerators.deleting.md)