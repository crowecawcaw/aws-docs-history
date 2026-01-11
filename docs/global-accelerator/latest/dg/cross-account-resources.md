#

Edit a cross-account attachment in AWS Global Accelerator

Follow the steps in this section to edit a cross-account attachment using the AWS Global Accelerator console.

This section explains how to edit a cross-acount attachment by using
the AWS Global Accelerator console. To learn about using API operations with Global Accelerator, see the [AWS Global Accelerator API Reference](../api/Welcome.md "../api/Welcome.md").

You can edit a cross-account attachment to add or remove principals or resources, rename the attachment, or
delete the attachment.

Be aware of the following when you remove principals or resources, or delete an attachment:

- To remove a principal or CIDR from an attachment, the principal must first remove shared IP addresses
  from all accelerators that use them. Then, you can remove the principal, or CIDRs, from the attachment.
- Before you can remove shared IP addresses or remove authorization for principals to access a shared CIDR
  from an attachment, the shared IP addresses for the CIDR must not be currently used by any accelerators.
- If you remove a principal from a cross-account attachment that enables the principal to
  add one or more shared endpoints, Global Accelerator removes those cross-account endpoints from any accelerator that
  uses that permission for cross-account resources listed in the attachment.
- If you remove an endpoint resource from a cross-account attachment, Global Accelerator removes the cross-account
  endpoint from any accelerator where it was added as an endpoint based on the permissions in the attachment.
- If you delete a cross-account attachment, Global Accelerator removes all cross-account
  endpoints listed in the attachment from all accelerators where the resources were added as endpoints
  based on the permissions in the attachment.
- If there are multiple cross-account attachments that include a principal, or that include a resource,
  Global Accelerator continues to allow the access that any existing attachment provides. So, for example, if you remove a principal from
  one attachment but the principal still has permission to access a resource that's granted by a second
  attachment, Global Accelerator continues to allow the principal access to the cross-account resource.

# To edit a cross-account attachment

1. Open the Global Accelerator console at [https://console.aws.amazon.com/globalaccelerator/home](https://console.aws.amazon.com/globalaccelerator/home "https://console.aws.amazon.com/globalaccelerator/home").
2. Choose **Cross-account attachments**.
3. Choose a cross-account attachment to update, and then choose **Edit**.
4. Modify the attachment to make the desired changes. For example, you can add or remove principals,
   rename the attachment, or add or remove resources.
5. Choose **Save changes**.
