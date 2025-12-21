#

Edit a listener for a custom routing accelerator in Global Accelerator

This section explains how to edit a listener for a custom routing accelerator on the AWS Global Accelerator console. To learn about
using API operations with AWS Global Accelerator, see the [AWS Global Accelerator API Reference](../api/Welcome.md "../api/Welcome.md").

# To edit a listener for a custom routing accelerator

When you edit a listener for a custom routing accelerator, be aware that you can add additional port ranges and associated protocols,
increase existing port ranges, or change protocols, but you can't decrease existing port ranges.

1. Open the Global Accelerator console at [https://console.aws.amazon.com/globalaccelerator/home](https://console.aws.amazon.com/globalaccelerator/home "https://console.aws.amazon.com/globalaccelerator/home").
2. On the **Accelerators** page, choose an accelerator.
3. Choose a listener, and then choose **Edit listener**.
4. On the **Edit listener** page, make the changes that you want
   to existing port ranges or protocols, or add new port ranges.

Be aware that you cannot decrease the range of an existing port range. 5. Choose **Save**.
