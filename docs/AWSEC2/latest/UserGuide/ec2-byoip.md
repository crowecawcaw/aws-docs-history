# Bring your own IP addresses (BYOIP) to Amazon EC2

You can bring part or all of your publicly routable IPv4 or IPv6 address range from your
on-premises network to your AWS account. You continue to control the address range and you
can advertise the address range on the internet through AWS. After you bring the address
range to Amazon EC2, it appears in your AWS account as an address pool.

###### Note

This documentation describes how to bring your own IP address range for use
in Amazon EC2 only. To bring your own IP address range for use in AWS Global Accelerator, see
[Bring your own IP
addresses (BYOIP)](../../../global-accelerator/latest/dg/using-byoip.md "../../../global-accelerator/latest/dg/using-byoip.md") in the _AWS Global Accelerator Developer Guide_. To
bring your own IP address range for use with Amazon VPC IP Address Manager, see [Tutorial: Bring your IP addresses to IPAM](../../../vpc/latest/ipam/tutorials-byoip-ipam.md "../../../vpc/latest/ipam/tutorials-byoip-ipam.md") in the
_Amazon VPC IPAM User Guide_.

When you bring an IP address range to AWS, AWS validates that you control
the IP address range. There are two methods that you can use to show that you
control the range:

- If your IP address range is registered with an Internet Registry that
  supports RDAP (such as ARIN, RIPE and APNIC), you can verify control of
  your domain with an X.509 certificate by using the process on this page.
  The certificate must only be valid for the duration of the provisioning
  process. You can remove the certificate from your RIR's record after
  provisioning is complete.
- Regardless of whether your Internet Registry supports RDAP, you can
  use Amazon VPC IPAM to verify control of your domain with a DNS TXT
  record. That process is documented in [Tutorial: Bring your
  IP addresses to IPAM](../../../vpc/latest/ipam/tutorials-byoip-ipam.md "../../../vpc/latest/ipam/tutorials-byoip-ipam.md") in the _Amazon VPC IPAM User
  guide_.
  For more information, see the AWS Online Tech talk [Deep Dive on Bring Your Own IP](https://pages.awscloud.com/Deep-Dive-on-Bring-Your-Own-IP_1024-NET_OD.html "https://pages.awscloud.com/Deep-Dive-on-Bring-Your-Own-IP_1024-NET_OD.html").

###### Contents

- [BYOIP definitions](#byoip-definitions "#byoip-definitions")
- [Requirements and quotas](#byoip-requirements "#byoip-requirements")
- [Regional availability](#byoip-reg-avail "#byoip-reg-avail")
- [Local Zone availability](#byoip-zone-avail "#byoip-zone-avail")
- [Prerequisites](prepare-for-byoip.md "prepare-for-byoip.md")
- [Onboard your address range](byoip-onboard.md "byoip-onboard.md")
- [Use your address range](byoip-working-with.md "byoip-working-with.md")

## BYOIP definitions

- **X.509 Self-sign certificate** — A
  certificate standard most commonly used to encrypt and authenticate data within
  a network. It is a certificate used by AWS to validate control over IP space
  from an RDAP record. For more information about X.509 certificates, see [RFC 3280](https://datatracker.ietf.org/doc/html/rfc3280 "https://datatracker.ietf.org/doc/html/rfc3280").
- **Autonomous System Number (ASN)** – A globally
  unique identifier that defines a group of IP prefixes run by one or more network
  operators that maintain a single, clearly-defined routing policy.
- **Regional Internet Registry (RIR)** – An
  organization that manages allocation and registration of IP addresses and ASNs
  within a region of the world.
- **Registry Data Access Protocol (RDAP)** —
  A read-only protocol to query current registration data within a RIR. Entries
  within the queried RIR database are referred to as "RDAP records". Certain
  record types need to be updated by customers via a RIR-provided mechanism. These
  records are queried by AWS to verify control of an address space in the
  RIR.
- **Route Origin Authorization (ROA)** — An
  object created by RIRs for customers to authenticate IP advertisement in
  particular autonomous systems. For an overview, see [Route Origin
  Authorizations (ROAs)](https://www.arin.net/resources/manage/rpki/roa_request/ "https://www.arin.net/resources/manage/rpki/roa_request/") on the ARIN website.
- **Local Internet Registry (LIR)** —
  Organizations such as internet service providers that allocate a block of IP
  addresses from an RIR for their customers.

## Requirements and quotas

- The address range must be registered with your Regional Internet Registry (RIR). See your RIR for any policies regarding geographic regions. BYOIP currently supports registration in the American Registry for
  Internet Numbers (ARIN), Réseaux IP Européens Network Coordination
  Centre (RIPE), or Asia-Pacific Network Information Centre (APNIC). It must be
  registered to a business or institutional entity and cannot be registered to an
  individual person.
- The most specific IPv4 address range that you can bring is /24.
- The most specific IPv6 address range that you can bring is /48 for CIDRs that
  are publicly advertisable and /60 for CIDRs that are [not publicly
  advertisable](byoip-onboard.md#byoip-provision-non-public "byoip-onboard.md#byoip-provision-non-public").
- ROAs are not required for CIDR ranges that are not publicly advertisable, but
  the RDAP records still need to be updated.
- You can bring each address range to one AWS Region at a time.
- You can bring a total of five BYOIP IPv4 and IPv6 address ranges per AWS Region to
  your AWS account. You cannot adjust the quotas for BYOIP CIDRs using the Service Quotas
  console, but you can request a quota increase by contacting the AWS Support
  Center as described in [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md")
  in the _AWS General Reference_.
- You cannot share your IP address range with other accounts using AWS RAM unless you use
  Amazon VPC IP Address Manager (IPAM) and integrate IPAM with AWS Organizations. For more information,
  see [Integrate
  IPAM with AWS Organizations](../../../vpc/latest/ipam/enable-integ-ipam.md "../../../vpc/latest/ipam/enable-integ-ipam.md") in the _Amazon VPC IPAM User Guide_.
- The addresses in the IP address range must have a clean history. We might
  investigate the reputation of the IP address range and reserve the right to
  reject an IP address range if it contains an IP address that has a poor
  reputation or is associated with malicious behavior.
- Legacy address space, the IPv4 address space that was distributed by the
  Internet Assigned Numbers Authority's (IANA) central registry prior to the
  formation of the Regional Internet Registry (RIR) system, still requires a
  corresponding ROA object.
- For LIRs, it is common that they use a manual process to update their records.
  This can take days to deploy depending on the LIR.
- A single ROA object and RDAP record are needed for a large CIDR block. You can
  bring multiple smaller CIDR blocks from that range to AWS, even across
  multiple AWS Regions, using the single object and record.
- BYOIP is not supported for Wavelength Zones or on AWS Outposts.
- Do not make any manual changes for BYOIP in RADb or any other IRR. BYOIP will
  automatically update RADb. Any manual changes that include the BYOIP ASN will
  cause the BYOIP provision operation to fail.
- Once you bring an IPv4 address range to AWS, you can use all of the IP addresses in the range, including the first address (the network address) and the last address (the broadcast address).

## Regional availability

The BYOIP feature is currently available in all commercial [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/") except for
China Regions.

## Local Zone availability

A [Local Zone](../../../local-zones/latest/ug/how-local-zones-work.md "../../../local-zones/latest/ug/how-local-zones-work.md") is an extension of an AWS Region in geographic proximity to
your users. Local Zones are grouped into "network border groups". In AWS, a network
border group is a collection of Availability Zones (AZs), Local Zones, or Wavelength
Zones from which AWS advertises a public IP address. Local Zones may have different
network border groups than the AZs in an AWS Region to ensure minimum latency or physical
distance between the AWS network and the customers accessing the resources in these
Zones.

You can provision BYOIPv4 address ranges to and advertise them in the following Local
Zone network border groups using the `--network-border-group` option:

- af-south-1-los-1
- ap-northeast-1-tpe-1
- ap-south-1-ccu-1
- ap-south-1-del-1
- ap-southeast-1-bkk-1
- ap-southeast-1-mnl-1
- ap-southeast-2-akl-1
- ap-southeast-2-per-1
- eu-central-1-ham-1
- eu-central-1-waw-1
- eu-north-1-cph-1
- eu-north-1-hel-1
- me-south-1-mct-1
- us-east-1-atl-2
- us-east-1-bos-1
- us-east-1-bue-1
- us-east-1-chi-2
- us-east-1-dfw-2
- us-east-1-iah-2
- us-east-1-lim-1
- us-east-1-mci-1
- us-east-1-mia-2
- us-east-1-msp-1
- us-east-1-nyc-1
- us-east-1-nyc-2
- us-east-1-phl-1
- us-east-1-qro-1
- us-east-1-scl-1
- us-west-2-den-1
- us-west-2-hnl-1
- us-west-2-las-1
- us-west-2-lax-1
- us-west-2-pdx-1
- us-west-2-phx-2
- us-west-2-sea-1

If you have Local Zones enabled (see [Enable a Local Zone](../../../local-zones/latest/ug/getting-started.md#getting-started-find-local-zone "../../../local-zones/latest/ug/getting-started.md#getting-started-find-local-zone")), you can choose a network border group for Local Zones
when you provision and advertise a BYOIPv4 CIDR. Choose the network border group
carefully as the EIP and the AWS resource it is associated with must reside in the
same network border group.

###### Note

You cannot provision or advertise BYOIPv6 address ranges in Local Zones at this
time.
