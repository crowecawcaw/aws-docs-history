# AWS Cloud Map namespaces

A namespace is a logical entity in AWS Cloud Map that is used to group an application's services
 under a common name and level of discoverability. When you create a namespace, you specify the
 following:


* A name that you want your application to use to discover instances.
* The method by which service instances that you register with AWS Cloud Map can be discovered.
 You can decide whether your resources need to be discovered publicly over the internet,
 privately in a specific virtual private cloud (VPC), or by API calls only.
The following are general concepts about namespaces.


* Namespaces are specific to the AWS Region that they're created in. To use AWS Cloud Map in
 multiple regions, you'll need to create namespaces in each region.
* If you create a namespace to allow for instance discovery by DNS queries in a VPC, AWS Cloud Map
 automatically creates a private Route 53 hosted zone. This hosted zone can be associated with
 multiple VPCs. For more information, see [AssociateVPCWithHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AssociateVPCWithHostedZone.html "https://docs.aws.amazon.com/Route53/latest/APIReference/API_AssociateVPCWithHostedZone.html") in
 the *Amazon Route 53 API Reference*.
###### Topics

* [Creating an AWS Cloud Map namespace to group application
 services](creating-namespaces.md "creating-namespaces.md")
* [Listing AWS Cloud Map namespaces](listing-namespaces.md "listing-namespaces.md")
* [Deleting an AWS Cloud Map namespace](deleting-namespaces.md "deleting-namespaces.md")
* [Shared AWS Cloud Map namespaces](sharing-namespaces.md "sharing-namespaces.md")
