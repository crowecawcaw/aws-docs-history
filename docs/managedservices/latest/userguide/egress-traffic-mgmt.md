# AMS egress traffic management

By default, the route with a destination CIDR of 0.0.0.0/0 for AMS private and customer-applications subnets has a
network address translation (NAT) gateway as the target.
AMS services, TrendMicro and patching, are components that must have egress access to the Internet so that
AMS is able to provide its service, and TrendMicro and operating systems can obtain updates.

AMS supports diverting the egress traffic to the internet through a customer-managed
egress device as long as:

- It acts as an implicit (for example, transparent) proxy.

and

- It allows AMS HTTP and HTTPS dependencies (listed in this section) in order to allow ongoing patching and
  maintenance of AMS managed infrastructure.
  Some examples are:

- The transit gateway (TGW) has a default route pointing to the customer-managed, on-premises
  firewall over the AWS Direct Connect connection in the Multi-Account Landing Zone Networking
  account.
- The TGW has a default route pointing to an AWS endpoint in the Multi-Account Landing Zone egress VPC leveraging
  AWS PrivateLink, pointing to a customer-managed proxy in another AWS account.
- The TGW has a default route pointing to a customer-managed firewall in another AWS account,
  with site-to-site VPN connection as an attachment to the Multi-Account Landing Zone TGW.
  AMS has identified the corresponding AMS HTTP and HTTPS dependencies, and develops and refines these dependencies on an
  ongoing basis. See
  [egressMgmt.zip](samples/egressMgmt.md "samples/egressMgmt.md"). Along with the JSON file,
  the ZIP contains a README.

###### Note

- This information isn't comprehensive--some required external sites aren't listed here.
- Do not use this list under a deny list or blocking strategy.
- This list is meant as a starting point for an egress filtering rule set, with the expectation that reporting tools will be used to
  determine precisely where the actual traffic diverges from the list.
  To ask for information about filtering egress traffic, email your CSDM: ams-csdm@amazon.com.
