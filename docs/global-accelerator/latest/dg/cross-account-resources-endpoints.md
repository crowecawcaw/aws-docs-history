#

Responsibilities and permissions for cross-account resources in Global Accelerator

The following sections list the permissions you have as a resource owner or as a principal
for cross-account access in AWS Global Accelerator.

## Permissions for resource owners

When you, as a resource owner, authorize principals to add resources from your AWS account to their accelerators, or
to a specific accelerator, principals can add any resources that you have listed in the cross-account attachment.

As a resource owner, you are responsible for creating, managing, and deleting your resources.
You can't add or remove resources in accelerators unless you have a role that is authorized to do so.

If you have an accelerator and you need to add or remove cross-account resources, a principal can set up a
role in IAM with permission to access the resources, and add your account to the role.

You can add or remove principals or resources from a cross-account attachment, to manage whether
resources that you own are used as endpoints or shared IP address pools for accelerators.

## Permissions for principals

In general, principals can add resources that are listed in a cross-account
attachment for an accelerator that the attachment provides permission for.
They can only view, add, or remove endpoints, or select shared IP addresses from BYOIP address pools,
for the cross-account resources that they have permission for.

The following applies for principals:

- Principals can only view, add, or remove resources as endpoints or shared IP address pools for an accelerator
  that they have been granted permission for in a cross-account attachment.
- Principals can only modify resources, such as load balancers, that they own themselves.
  They cannot modify resources specified in a cross-account attachment, because the resources
  belong to the resource owner.

Although principals cannot modify the actual cross-account resources, based on a cross-account attachment,
the resource owner can create an IAM role that provides permission to access the resource. Then,
the owner can grant a principal permissions to assume the role, so that the principal can access the resource,
however the owner has specified through the role's permissions.
