

# Shared multicast domains in AWS Transit Gateway
<a name="multicast-share-domain"></a>

With multicast domain sharing, multicast domain owners can share the domain with other AWS accounts inside its organization or across organizations in AWS Organizations. As the multicast domain owner, you can create and manage the multicast domain centrally. Once shared, those users can perform the following operations on a shared multicast domain:
+ Register and deregister group members or group sources in the multicast domain
+ Associate a subnet with the multicast domain, and disassociate subnets from the multicast domain

A multicast domain owner can share a multicast domain with:
+ AWS accounts inside its organization or across organizations in AWS Organizations
+ An organizational unit inside its organization in AWS Organizations
+ Its entire organization in AWS Organizations
+ AWS accounts outside of AWS Organizations. 

  To share a multicast domain with an AWS account outside of your Organization, you must create a resource share using AWS Resource Access Manager, and then choose **Allow sharing with anyone** when selecting the Principals to share the multicast domain with. For more information on creating a resource share, see [Creating a resource share in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-create.html) in the *AWS RAM User Guide*

**Topics**
+ [Prerequisites for sharing a multicast domain](#sharing-prereqs)
+ [Related services](#sharing-related)
+ [Shared multicast domain permissions](#sharing-perms)
+ [Billing and metering](#sharing-billing)
+ [Quotas](#sharing-quotas)
+ [Share resources across Availability Zones](sharing-azs.md)
+ [Share a multicast domain](sharing-share.md)
+ [Unshare a shared multicast domain](sharing-unshare.md)
+ [Identify a shared multicast domain](sharing-identify.md)

## Prerequisites for sharing a multicast domain
<a name="sharing-prereqs"></a>
+ To share a multicast domain, you must own it in your AWS account. You cannot share a multicast domain that has been shared with you.
+ To share a multicast domain with your organization or an organizational unit in AWS Organizations, you must enable sharing with AWS Organizations. For more information, see [ Enable Sharing with AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the *AWS RAM User Guide*.

## Related services
<a name="sharing-related"></a>

Multicast domain sharing integrates with AWS Resource Access Manager (AWS RAM). AWS RAM is a service that enables you to share your AWS resources with any AWS account or through AWS Organizations. With AWS RAM, you share resources that you own by creating a *resource share*. A resource share specifies the resources to share, and the users with whom to share them. Consumers can be individual AWS accounts, or organizational units or an entire organization in AWS Organizations.

For more information about AWS RAM, see the *[AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/)*.

## Shared multicast domain permissions
<a name="sharing-perms"></a>

### Permissions for owners
<a name="perms-owner"></a>

Owners are responsible for managing the multicast domain and the members and attachments that they register or associate with the domain. Owners can change or revoke shared access at any time. They can use AWS Organizations to view, modify, and delete resources that consumers create on shared multicast domains.

### Permissions for consumers
<a name="perms-consumer"></a>

Users of the shared multicast domain can perform the following operations on shared multicast domains in the same way that they would on multicast domains that they created:
+ Register and deregister group members or group sources in the multicast domain
+ Associate a subnet with the multicast domain, and disassociate subnets from the multicast domain

Consumers are responsible for managing the resources that they create on the shared multicast domain.

Customers cannot view or modify resources owned by other consumers or by the multicast domain owner, and they cannot modify multicast domains that are shared with them. 

## Billing and metering
<a name="sharing-billing"></a>

There are no additional charges for sharing multicast domains for either the owner, or consumers. 

## Quotas
<a name="sharing-quotas"></a>

A shared multicast domain counts toward the owner's and shared user's multicast domain quotas.