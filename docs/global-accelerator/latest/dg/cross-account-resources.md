#

Work with cross-account attachments in Global Accelerator

To allow someone to add a resource from another account as an endpoint or a BYOIP address for an accelerator,
the owner of the resource must create a _cross-account attachment_ in Global Accelerator. In the attachment,
the resource owner specifies one or more accelerators or accounts—principals— that are allowed to add resources,
along with the specific resources that the principals can add to accelerators.

As a resource owner, be aware that to specify a resource in a cross-account attachment, you must own the resource in
your AWS account. That is, the resource must be allocated or provisioned in your account; you cannot
specify a resource that has been shared with _you_, such as a shared subnet.

###### Contents

- [Create cross-account attachments](cross-account-resources.md "cross-account-resources.md")
- [Edit cross-account attachments](cross-account-resources.md "cross-account-resources.md")
- [Delete cross-account attachments](cross-account-resources.md "cross-account-resources.md")
