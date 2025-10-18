# Shared AWS Cloud Map namespaces

AWS Cloud Map allows namespace owners to share their
 namespaces with other AWS accounts or within an organization in AWS Organizations for simplified
 cross-account service discovery and service registry. This allows for easier use of
 namespaces managed by other AWS accounts or teams within an AWS Organization.

AWS Cloud Map integrates with AWS Resource Access Manager (AWS RAM) to enable resource sharing. AWS RAM is a
 service that enables you to share some AWS Cloud Map resources with other AWS accounts or
 through AWS Organizations. With AWS RAM, you share resources that you own by creating a
 *resource share*. A resource share specifies the resources to share,
 and the consumers with whom to share them. Consumers can include:


* Specific AWS accounts inside its organization in AWS Organizations
* An organizational unit inside its organization in AWS Organizations
* Its entire organization in AWS Organizations
For more information about AWS RAM, see the *[AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/ "https://docs.aws.amazon.com/ram/latest/userguide/")*.

This topic explains how to share resources that you own, and how to use resources that are
 shared with you.

###### Contents

* [Considerations for sharing namespaces](#sharing-considerations "#sharing-considerations")
* [Sharing an AWS Cloud Map namespace](sharing-share.md "sharing-share.md")
* [Stop sharing a AWS Cloud Map namespace](sharing-unshare.md "sharing-unshare.md")
* [Identifying a shared AWS Cloud Map namespace](sharing-identify.md "sharing-identify.md")
* [Granting permissions to share a
 namespace](#granting-perms-to-share "#granting-perms-to-share")
* [Responsibilities and permissions for shared
 namespaces](#sharing-perms "#sharing-perms")
* [Billing and metering](#sharing-billing "#sharing-billing")
* [Quotas](#sharing-quotas "#sharing-quotas")

## Considerations for sharing namespaces



* To share a namespace, you must own it in your AWS account. This means that
 the resource must be allocated or provisioned in your account. You can't share a
 namespace that has been shared with you.
* To share a namespace with your organization or an organizational unit in
 AWS Organizations, you must enable sharing with AWS Organizations. For more information, see
  [Enable Sharing with AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs "https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs") in the
 *AWS RAM User Guide*.
* For service discovery using DNS queries in a shared private DNS namespace,
 the namespace owner will need to call
 `create-vpc-association-authorization` with the ID of the private
 hosted zone associated with the namespace and the consumer's VPC.



```
aws route53 create-vpc-association-authorization --hosted-zone-id `Z1234567890ABC` --vpc VPCRegion=`us-east-1`,VPCId=`vpc-12345678`
```

The namespace consumer will need to call
 `associate-vpc-with-hosted-zone` with the ID of the private hosted
 zone.



```
aws route53 associate-vpc-with-hosted-zone --hosted-zone-id `Z1234567890ABC` --vpc VPCRegion=`us-east-1`,VPCId=`vpc-12345678`
```

For more information, see [Associating an Amazon VPC and a private hosted zone that you created with
 different AWS accounts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-associate-vpcs-different-accounts.html "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-associate-vpcs-different-accounts.html") in the *Amazon Route 53 Developer Guide*.
* After discovering up-to-date network locations of services associated with a
 shared DNS namespace, it may be necessary to configure inter-VPC connectivity to
 communicate with the services if they are in different VPCs. This can be
 achieved using a VPC Peering connection. For more information, see [Create or delete
 a VPC Peering connection](https://docs.aws.amazon.com/vpc/latest/peering/create-vpc-peering-connection.html "https://docs.aws.amazon.com/vpc/latest/peering/create-vpc-peering-connection.html") in the *Amazon Virtual Private Cloud VPC Peering
 guide*.
* You can't use `ListOperations` to list operations on shared
 namespaces that are performed by other accounts.
* Tagging isn't supported for shared namespaces.

## Granting permissions to share a
 namespace


A minimum set of permissions is required for an IAM principal to share a namespace.
 We recommend using the `AWSCloudMapFullAccess` and
 `AWSResourceAccessManagerFullAccess` managed policies to ensure your
 IAM principals have the required permissions to share and use shared
 namespaces.


If you use a custom IAM policy, the `servicediscovery:PutResourcePolicy`,
 `servicediscovery:GetResourcePolicy`, and
 `servicediscovery:DeleteResourcePolicy` actions are required for sharing
 namespaces. These are permission-only IAM actions. If an IAM principal doesn't have
 these permissions granted, an error will occur when attempting to share the namespace
 using AWS RAM.


For more information about how AWS RAM uses IAM, see [How AWS RAM uses IAM](https://docs.aws.amazon.com/ram/latest/userguide/security-iam-policies.html "https://docs.aws.amazon.com/ram/latest/userguide/security-iam-policies.html")
 in the *AWS RAM User Guide*.


## Responsibilities and permissions for shared
 namespaces


The namespace owner and consumer can perform different actions on a shared
 namespace.


### Permissions for owners


A namespace owner can perform the following actions on a shared
 namespace:



* Access services associated with the namespace, including services created
 by consumer accounts and instances registered to these services.
* Revoke access to the namespace, including access to services created by
 consumer accounts and instances registered to these services.
* Configure permissions for other accounts to register and deregister
 instances in services created in the shared namespace by consumers or the
 namespace owner.
* Delete services and deregister instances, including services created and
 instances registered by consumer accounts.
* Update or delete a shared namespace.

### Permissions for consumers


A namespace consumer can perform the following actions on a shared
 namespace:



* Create and delete services in the namespace.
* Register and deregister instances in services created in the
 namespace.
* Discover instances that are registered to services created in the
 namespace.

A consumer can't update or delete a shared namespace. After losing access to the
 shared namespace, the consumer accounts will also lose access to services that they
 created in the namespace.


## Billing and metering


Owners are billed for any instances that they register in the shared namespace and
 any Route 53 health checks that are created when they register these instances. Consumers
 are billed for any instances that they register in the namespace and any Route 53 health
 checks that are created when they register these instances. If the shared namespace is
 a DNS namespace, the namespace owner is billed for the Route 53 DNS records that are
 created when services are created in the namespace. Owners are billed for any
 `DiscoverInstances` and `DiscoverInstancesRevision` calls they
 make. Consumers are billed for any `DiscoverInstances` and
 `DiscoverInstancesRevision` calls they make.


## Quotas


Shared namespaces count towards only the namespace owner's namespaces per Region
 quota. Instances registered by a consumer in the shared namespace count towards the
 owner's instances per namespace quota. If a consumer creates a service in a shared
 namespace, any instances registered in the service count towards the consumer's
 instances per service quota. If an owner creates a service in a shared namespace, any
 instances registered in the service count towards the owner's instances per service
 quota.
