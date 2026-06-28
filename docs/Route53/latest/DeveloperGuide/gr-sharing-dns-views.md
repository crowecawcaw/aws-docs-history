# Sharing Route 53 Global Resolver DNS views between AWS accounts

You can share a Route 53 Global Resolver DNS view with other AWS accounts. To share a DNS view, you use
AWS Resource Access Manager (AWS RAM). AWS RAM is a service that enables you to share your AWS resources with any
AWS account or through AWS Organizations. For more information about AWS RAM, see the [Resource Access Manager User
Guide](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md").

When you share a DNS view, the account that you share it with (the _consumer_) can associate its own Route 53 private hosted zones with the view. This lets
the consumer make the records in its private hosted zones resolvable through your global resolver,
without transferring ownership of the hosted zone or the DNS view. The account that owns the DNS
view (the _owner_) keeps full control of the global resolver and
the DNS view, including the ability to stop sharing the view or to remove any hosted zone
association at any time.

###### Note

A shared DNS view applies the records in the consumer's private hosted zones to the DNS
resolution that the owner's global resolver performs in every AWS Region where the global
resolver runs. Share a DNS view only with accounts that you trust to influence your DNS
resolution.

Note the following:

**Permissions that the owner grants to the consumer**

When you share a DNS view, you choose a AWS RAM that defines what the consumer can do
with the view. Route 53 Global Resolver provides the following for the
`route53globalresolver:dns-view` resource type:

- **AWSRAMDefaultPermissionDNSView** (default) –
  Allows the consumer to view the shared DNS view and to associate its own private hosted zones
  with the view. This permission allows the `AssociateHostedZone` and
  `GetDNSView` actions.
- **AWSRAMPermissionDNSViewLifecycleManagement** –
  Allows the consumer to view, update, enable, and disable the shared DNS view, but not to
  associate private hosted zones with it.
- **AWSRAMPermissionDNSViewFullAccess** – Allows the
  consumer both to associate private hosted zones and to manage the lifecycle of the shared DNS
  view.

You can also create a that grants a subset of these actions. For more information,
see [Creating customer managed permissions](../../../ram/latest/userguide/create-customer-managed-permissions.md "../../../ram/latest/userguide/create-customer-managed-permissions.md") in the _AWS Resource Access Manager User
Guide_.

**Hosted zone associations are owned by the consumer**

A private hosted zone association that a consumer creates on a shared DNS view belongs to
the consumer's account. The owner of the DNS view can see and delete these associations, and
the consumer can manage the associations that it created.

**Stopping sharing (unsharing) a DNS view**

If you stop sharing a DNS view, the consumer can no longer create new hosted zone
associations on the view or update the view. The hosted zone associations that the consumer
already created are _not_ removed automatically. They continue to affect DNS
resolution until the owner or the consumer removes them. To stop a consumer's records from
resolving immediately, remove the consumer's hosted zone associations from the DNS view.

**Deleting a shared DNS view**

You can't delete a DNS view while it's shared. Stop sharing the view first, and then
delete it.

**Quotas**

Private hosted zone associations that a consumer creates on a shared DNS view count toward
the owner's quota for the number of associations per DNS view. For current Route 53 Global Resolver quotas, see
[Quotas for Route 53 Global Resolver](gr-load-balancer-limits.md "gr-load-balancer-limits.md").

**Data in opt-in AWS Regions**

The owner's global resolver might run in opt-in AWS Regions that the consumer hasn't
enabled. When a consumer associates a private hosted zone with a shared DNS view, the hosted
zone ID and domain name of the association are replicated to all AWS Regions where the
owner's global resolver runs, including opt-in Regions that the consumer hasn't enabled.
