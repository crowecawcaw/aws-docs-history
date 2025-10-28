#

Remove a VPC subnet endpoint for a custom routing accelerator

You can remove an Amazon Virtual Private Cloud (VPC) subnet endpoint from your custom routing accelerator so
that user traffic no longer goes to destination Amazon EC2 instances in the subnet.

The steps in this section explain how to remove a VPC subnet endpoint on the AWS Global Accelerator console. To learn about
using API operations with AWS Global Accelerator, see the [AWS Global Accelerator API Reference](../api/Welcome.md "../api/Welcome.md").

# To remove an endpoint

1. Open the Global Accelerator console at [https://console.aws.amazon.com/globalaccelerator/home](https://console.aws.amazon.com/globalaccelerator/home "https://console.aws.amazon.com/globalaccelerator/home").
2. On the **Accelerators** page, choose a custom routing accelerator.
3. In the **Listeners** section, for **Listener ID**,
   choose the ID of a listener.
4. In the **Endpoint groups** section, for **Endpoint group ID**, choose the
   ID of the endpoint group (AWS Region) of the VPC subnet endpoint that you want to remove.
5. Choose **Remove endpoint**.
6. In the confirmation dialog box, choose **Remove**.
