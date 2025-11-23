#

How cross-account works in Global Accelerator

With cross-account support in Global Accelerator, resource owners control whether their resources are shared with accelerators
owned by other accounts. To enable resource sharing for your resources, you—as a resource owner—create a Global Accelerator
_cross-account attachment_ to authorize resources in your account to be added
to an accelerator by another account.

You create the cross-account attachment in Global Accelerator. The attachment lists the _resources_
that you want to share, and the _principals_—other accounts or specific accelerator ARNs—
that are authorized to use the resources. Resources can be AWS resources, like Network Load Balancers, that you add as endpoints to accelerator
endpoint groups, or resources can be IP address ranges that you've brought to Global Accelerator with the bring your own IP address
(BYOIP) process.

###### Important

Before you can add a BYOIP IP address range to a cross-account attachment to share with principals, you
must complete the process to _provision_ and _advertise_ the address range.
For more information, see [Bring your own IP addresses (BYOIP) in Global Accelerator](using-byoip.md "using-byoip.md").

After you, as a resource owner, create an attachment, principals listed in the attachment can work with resources that are
listed in the attachment. That is, they can add as endpoints AWS resources that are listed, or select as a static
IP address a BYOIP address from CIDR prefixes that are listed. When a principal wants to add a cross-account resource for an accelerator,
they must specify the cross-account attachment that authorizes them as a principal with permission to use the resource.
