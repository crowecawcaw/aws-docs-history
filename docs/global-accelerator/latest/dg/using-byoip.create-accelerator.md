

# Use your BYOIP address with an accelerator in Global Accelerator
<a name="using-byoip.create-accelerator"></a>

After you complete the steps to add an address range with BYOIP, you can create an accelerator with your BYOIP IP addresses, or you can use your BYOIP IP addresses with an existing accelerator. If you brought one address range to AWS, you can assign one IP address to your accelerator. If you brought two address ranges, you can assign one IP address from each address range to your accelerator.

You can also update an existing accelerator to use one or more of your BYOIP IP addresses. For more information, see [Update an accelerator to change your IP addresses](using-byoip.update-accelerator.md)

Another option is to use a shared BYOIP address. If one or more additional CIDR addresses have been shared with you from another account, you can choose from a shared BYOIP CIDR when you select one or both BYOIP IP addresses. Note that if you choose to use two shared BYOIP addresses, they must both come from CIDRs owned by the same account. For more information, see [Configure cross-account access in Global Accelerator](cross-account-resources.md).

You have several options for creating an accelerator using your own IP addresses for the static IP addresses: 
+ **Use Global Accelerator console to create an accelerator.** For more information, see the following:
  + [Create accelerator](about-accelerators.creating-editing.md)
  + [Create a custom routing accelerator in Global Accelerator](about-custom-routing-accelerators.creating-editing.md)
  + [Add cross-account endpoints in AWS Global Accelerator](cross-account-resources.add-endpoints.md)
+ **Use the Global Accelerator API to create an accelerator.** For more information, including examples of using the CLI, see the following in the AWS Global Accelerator API Reference:
  + [CreateAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateAccelerator.html)
  + [CreateCustomRoutingAccelerator](https://docs.aws.amazon.com/global-accelerator/latest/api/API_CreateCustomRoutingAccelerator.html)