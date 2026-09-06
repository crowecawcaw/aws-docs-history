

# Sharing Route 53 Global Resolver DNS views between AWS accounts
<a name="gr-sharing-dns-views"></a>

You can share a Route 53 Global Resolver DNS view with other AWS accounts by using AWS Resource Access Manager (AWS RAM). AWS RAM lets you share your AWS resources with any AWS account or through AWS Organizations. For more information, see the [Resource Access Manager User Guide](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html).

When you share a DNS view, the receiving account (the *consumer*) can associate its own Route 53 private hosted zones with the view. The records in those zones then resolve through your global resolver. The consumer doesn't need to transfer ownership of the hosted zone or the DNS view. The account that owns the DNS view (the *owner*) keeps full control of the global resolver and the DNS view. The owner can stop sharing the view or remove any association at any time.

**Note**  
A shared DNS view applies the consumer's private hosted zone records to DNS resolution in every AWS Region where the owner's global resolver runs. Only share a DNS view with accounts that you trust.

Note the following:

**Permissions that the owner grants to the consumer**  
When you share a DNS view, you choose a AWS RAM managed permission that defines what the consumer can do with the view. Route 53 Global Resolver provides the following AWS managed permissions for the `route53globalresolver:dns-view` resource type:  
+ **AWSRAMDefaultPermissionDNSView** (default) – Lets the consumer view the shared DNS view and associate its own private hosted zones with the view. This permission allows the `AssociateHostedZone` and `GetDNSView` actions.
+ **AWSRAMPermissionDNSViewLifecycleManagement** – Lets the consumer view, update, enable, and disable the shared DNS view. Does not allow associating private hosted zones with the view.
+ **AWSRAMPermissionDNSViewFullAccess** – Lets the consumer both associate private hosted zones and manage the lifecycle of the shared DNS view.
You can also create a customer managed permission that grants only some of these actions. For more information, see [Creating customer managed permissions](https://docs.aws.amazon.com/ram/latest/userguide/create-customer-managed-permissions.html) in the *AWS Resource Access Manager User Guide*.

**Hosted zone associations are owned by the consumer**  
A private hosted zone association that a consumer creates on a shared DNS view belongs to the consumer's account. The owner of the DNS view can see and delete these associations. The consumer can manage the associations that it created.

**Stopping sharing (unsharing) a DNS view**  
If you stop sharing a DNS view, the consumer can no longer create new hosted zone associations on the view or update the view. However, existing associations are *not* removed automatically. They continue to affect DNS resolution until the owner or the consumer removes them. To stop a consumer's records from resolving right away, remove the consumer's hosted zone associations from the DNS view.

**Deleting a shared DNS view**  
You can't delete a DNS view while it's shared. Stop sharing the view first, and then delete it.

**Quotas**  
Hosted zone associations that a consumer creates on a shared DNS view count toward the owner's quota for associations per DNS view. For current Route 53 Global Resolver quotas, see [Quotas for Route 53 Global Resolver](gr-load-balancer-limits.md).

**Data in opt-in AWS Regions**  
The owner's global resolver might run in opt-in AWS Regions that the consumer hasn't turned on. When a consumer associates a private hosted zone with a shared DNS view, the hosted zone ID and domain name are copied to all Regions where the owner's global resolver runs. This includes opt-in Regions that the consumer hasn't turned on.