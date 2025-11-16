#

Create a cross-account attachment in AWS Global Accelerator

Follow the steps in this section to create a cross-account attachment using
the AWS Global Accelerator console.

This section explains how to create a cross-acount attachment by using
the AWS Global Accelerator console. To learn about using API operations with Global Accelerator, see the [AWS Global Accelerator API Reference](../api/Welcome.md "../api/Welcome.md").

# To create a cross-account attachment

1. Open the Global Accelerator console at [https://console.aws.amazon.com/globalaccelerator/home](https://console.aws.amazon.com/globalaccelerator/home "https://console.aws.amazon.com/globalaccelerator/home").
2. Choose **Create cross-account attachment**.
3. On the **Create cross-account attachment** page, enter a name for the attachment.
4. Add the AWS accounts or the ARNs for the accelerators, or both, that you want to allow to
   add your resources.
5. Select the resources that you want to allow to be used. For example, to add resources that can added as endpoints,
   for each resource, choose an AWS Region. Then, from the drop-down menus, select an endpoint type (resource type) and the
   endpoint (resource) to add.
6. Choose **Create attachment**.
   Note: To see the new cross-account attachment in your list of attachments, refresh the **Cross-account
   attachments** page.
