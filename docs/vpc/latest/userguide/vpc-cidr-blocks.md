# VPC CIDR blocks

The IP addresses for your virtual private cloud (VPC) are represented using Classless
Inter-Domain Routing (CIDR) notation. A VPC must have an associated IPv4 CIDR block.
You can optionally associate additional IPv4 CIDR blocks and one or more IPv6 CIDR blocks.
For more information, see [IP addressing for your VPCs and subnets](vpc-ip-addressing.md "vpc-ip-addressing.md").

###### Contents

- [IPv4 VPC CIDR blocks](#vpc-sizing-ipv4 "#vpc-sizing-ipv4")
- [Manage IPv4 CIDR blocks for a VPC](#vpc-resize "#vpc-resize")
- [IPv4 CIDR block association restrictions](#add-cidr-block-restrictions "#add-cidr-block-restrictions")
- [IPv6 VPC CIDR blocks](#vpc-sizing-ipv6 "#vpc-sizing-ipv6")

## IPv4 VPC CIDR blocks

When you create a VPC, you must specify an IPv4 CIDR block for the VPC. The allowed
block size is between a `/16` netmask (65,536 IP addresses) and
`/28` netmask (16 IP addresses). After you've created your VPC, you
can associate additional IPv4 CIDR blocks with the VPC. For more information, see [Add or remove a CIDR block from your VPC](add-ipv4-cidr.md "add-ipv4-cidr.md").

When you create a VPC, we recommend that you specify a CIDR block from the private IPv4
address ranges as specified in [RFC 1918](http://www.faqs.org/rfcs/rfc1918.html "http://www.faqs.org/rfcs/rfc1918.html").

| RFC 1918 range                                       | Example CIDR block |
| ---------------------------------------------------- | ------------------ |
| 10.0.0.0<br>• 10.255.255.255 (10/8 prefix)           | 10.0.0.0/16        |
| 172.16.0.0<br>• 172.31.255.255 (172.16/12 prefix)    | 172.31.0.0/16      |
| 192.168.0.0<br>• 192.168.255.255 (192.168/16 prefix) | 192.168.0.0/20     |

###### Considerations

- You can't specify the following CIDR blocks for your VPCs:
  - 0.0.0.0/8
  - 127.0.0.0/8 (internal host loopback address range)
  - 169.254.0.0/16 ([link-local address range](../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#link-local-addresses "../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#link-local-addresses"))
  - 224.0.0.0/4 (multicast address range)

- When you create a VPC for use with an AWS service, check the service documentation
  to verify if there are specific requirements for its configuration.
- Some AWS services use the `172.17.0.0/16` CIDR range. Services can experience
  IP address conflicts if the IP address range is already in use in your network. For
  example, AWS Cloud9 and Amazon SageMaker AI use `172.17.0.0/16`. To avoid conflicts, don't
  use this range when creating your VPC. For more information, see [Can't connect to EC2 environment because VPC's IP addresses are used by Docker](../../../cloud9/latest/user-guide/troubleshooting.md#docker-bridge "../../../cloud9/latest/user-guide/troubleshooting.md#docker-bridge")
  in the _AWS Cloud9 User Guide_.
- You can create a VPC with a publicly routable CIDR block that falls outside of the private
  IPv4 address ranges specified in RFC 1918. However, for the purposes of this documentation,
  we refer to _private IP addresses_ as the IPv4 addresses that are within
  the CIDR range of your VPC.
- If you create a VPC using a command line tool or the Amazon EC2 API, the CIDR block is
  automatically modified to its canonical form. For example, if you specify 100.68.0.18/18 for the
  CIDR block, we create a CIDR block of 100.68.0.0/18.

## Manage IPv4 CIDR blocks for a VPC

You can associate secondary IPv4 CIDR blocks with your VPC. When you associate a CIDR block
with your VPC, a route is automatically added to your VPC route tables to enable
routing within the VPC (the destination is the CIDR block and the target is
`local`).

In the following example, the VPC has both a primary and a secondary CIDR block.
The CIDR blocks for Subnet A and Subnet B are from the primary VPC CIDR block.
The CIDR block for Subnet C is from the secondary VPC CIDR block.

![VPCs with single and multiple CIDR blocks](images/vpc-multiple-cidrs.png)

The following route table shows the local routes for the VPC.

| Destination | Target |
| ----------- | ------ |
| 10.0.0.0/16 | Local  |
| 10.2.0.0/16 | Local  |

To add a CIDR block to your VPC, the following rules apply:

- The allowed block size is between a `/28` netmask and
  `/16` netmask.
- The CIDR block must not overlap with any existing CIDR block that's associated with the
  VPC.
- There are restrictions on the ranges of IPv4 addresses you can use. For more information,
  see [IPv4 CIDR block association restrictions](#add-cidr-block-restrictions "#add-cidr-block-restrictions").
- You cannot increase or decrease the size of an existing CIDR block.
- You have a quota on the number of CIDR blocks you can associate with a VPC and the number
  of routes you can add to a route table. You cannot associate a CIDR block if
  this results in you exceeding your quotas. For more information, see [Amazon VPC quotas](amazon-vpc-limits.md "amazon-vpc-limits.md").
- The CIDR block must not be the same or larger than a destination CIDR range in a route in
  any of the VPC route tables. For example, in a VPC where the primary CIDR
  block is `10.2.0.0/16`, you have an existing route in a route
  table with a destination of `10.0.0.0/24` to a virtual private
  gateway. You want to associate a secondary CIDR block in the
  `10.0.0.0/16` range. Because of the existing route, you
  cannot associate a CIDR block of `10.0.0.0/24` or larger.
  However, you can associate a secondary CIDR block of
  `10.0.0.0/25` or smaller.
- The following rules apply when you add IPv4 CIDR blocks to a VPC that's part of a VPC
  peering connection:
  - If the VPC peering connection is `active`, you can add CIDR blocks to a VPC
    provided they do not overlap with a CIDR block of the peer
    VPC.
  - If the VPC peering connection is `pending-acceptance`, the owner of the
    requester VPC cannot add any CIDR block to the VPC, regardless of
    whether it overlaps with the CIDR block of the accepter VPC. Either
    the owner of the accepter VPC must accept the peering connection, or
    the owner of the requester VPC must delete the VPC peering
    connection request, add the CIDR block, and then request a new VPC
    peering connection.
  - If the VPC peering connection is `pending-acceptance`, the owner of the
    accepter VPC can add CIDR blocks to the VPC. If a secondary CIDR
    block overlaps with a CIDR block of the requester VPC, the VPC
    peering connection request fails and cannot be accepted.

- If you're using Direct Connect to connect to multiple VPCs through a Direct
  Connect gateway, the VPCs that are associated with the Direct Connect
  gateway must not have overlapping CIDR blocks. If you add a CIDR block to
  one of the VPCs that's associated with the Direct Connect gateway, ensure
  that the new CIDR block does not overlap with an existing CIDR block of any
  other associated VPC. For more information, see [Direct Connect
  gateways](../../../directconnect/latest/UserGuide/direct-connect-gateways.md "../../../directconnect/latest/UserGuide/direct-connect-gateways.md") in the _Direct Connect User Guide_.
- When you add or remove a CIDR block, it can go through various states:
  `associating` | `associated` |
  `disassociating` | `disassociated` |
  `failing` | `failed`. The CIDR block is ready for
  you to use when it's in the `associated` state.

You can disassociate a CIDR block that you've associated with your VPC; however, you cannot
disassociate the CIDR block with which you originally created the VPC (the primary
CIDR block). To view the primary CIDR for your VPC in the Amazon VPC console, choose
**Your VPCs**, select the checkbox for your VPC, and choose the
**CIDRs** tab. To view the primary CIDR using the AWS CLI, use the
[describe-vpcs](../../../cli/latest/reference/ec2/describe-vpcs.md "../../../cli/latest/reference/ec2/describe-vpcs.md") command
as follows. The primary CIDR is returned in the top-level `CidrBlock element`.

```
aws ec2 describe-vpcs --vpc-id `vpc-1a2b3c4d` --query Vpcs[*].CidrBlock --output text
```

The following is example output.

```
10.0.0.0/16
```

## IPv4 CIDR block association restrictions

The following table provides an overview of permitted and restricted VPC CIDR block
associations for existing VPC CIDR blocks. The reason for restrictions is that some AWS services make use of
cross-VPC and cross-account features that require non-conflicting CIDR blocks on
the AWS service side.

| Existing IPv4 address range                                                                  | Restricted associations                                                                                                                                                                                                                                                                                                             | Permitted associations                                                                                                                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 10.0.0.0/8                                                                                   | CIDR blocks from other RFC 1918\<br>• ranges (172.16.0.0/12 and 192.168.0.0/16).<br>If any of the CIDR blocks associated with the VPC are from the 10.0.0.0/15 range (10.0.0.0 to 10.1.255.255),<br>you cannot add a CIDR block from the 10.0.0.0/16 range (10.0.0.0 to 10.0.255.255).<br>CIDR blocks from the 198.19.0.0/16 range. | Any other CIDR block from the 10.0.0.0/8 range between a /16 netmask and /28 netmask that's not restricted.<br>Any publicly routable IPv4 CIDR block (non-RFC 1918) between a /16 netmask and /28 netmask or a CIDR block between a /16 netmask and /28 netmask from the<br>100.64.0.0/10 range.                                                                         |
| 169.254.0.0/16                                                                               | CIDR blocks from the "link local" block are reserved as described in [RFC 5735](https://www.rfc-editor.org/rfc/rfc5735 "https://www.rfc-editor.org/rfc/rfc5735") and cannot be<br>assigned to VPCs.                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                          |
| 172.16.0.0/12                                                                                | CIDR blocks from other RFC 1918\<br>• ranges (10.0.0.0/8 and 192.168.0.0/16).<br>CIDR blocks from the 172.31.0.0/16 range.<br>CIDR blocks from the 198.19.0.0/16 range.                                                                                                                                                             | Any other CIDR block from the 172.16.0.0/12 range between a /16 netmask and /28 netmask that's not restricted.<br>Any publicly routable IPv4 CIDR block (non-RFC 1918) between a /16 netmask and /28 netmask or a CIDR block between a /16 netmask and /28 netmask from the<br>100.64.0.0/10 range.                                                                      |
| 192.168.0.0/16                                                                               | CIDR blocks from other RFC 1918\<br>• ranges (10.0.0.0/8 and 172.16.0.0/12).<br>CIDR blocks from the 198.19.0.0/16 range.                                                                                                                                                                                                           | Any other CIDR block from the 192.168.0.0/16 range between a /16 netmask and /28 netmask.<br>Any publicly routable IPv4 CIDR block (non-RFC 1918) between a /16 netmask and /28 netmask or a CIDR block from the<br>100.64.0.0/10 range between a /16 netmask and /28 netmask.                                                                                           |
| 198.19.0.0/16                                                                                | CIDR blocks from the RFC 1918\<br>• ranges.                                                                                                                                                                                                                                                                                         | Any publicly routable IPv4 CIDR block (non-RFC 1918) between a /16 netmask and /28 netmask or a CIDR block from the<br>100.64.0.0/10 range between a /16 netmask and /28 netmask.                                                                                                                                                                                        |
| Publicly routable CIDR block (non-RFC 1918), or a CIDR block from the 100.64.0.0/10<br>range | CIDR blocks from the RFC 1918\<br>• ranges.<br>CIDR blocks from the 198.19.0.0/16 range.                                                                                                                                                                                                                                            | Any other publicly routable IPv4 CIDR block (non-RFC 1918) between a /16 netmask and /28 netmask or a CIDR block between a /16 netmask and /28 netmask from the<br>100.64.0.0/10 range.<br>You can also associate a CIDR in one of the RFC 1918 ranges, but to do this<br>you have to add that CIDR first when you create the VPC and then add the non-RFC<br>1918 CIDR. |

\* RFC 1918 ranges are the private IPv4 address ranges specified in [RFC 1918](http://www.faqs.org/rfcs/rfc1918.html "http://www.faqs.org/rfcs/rfc1918.html").

## IPv6 VPC CIDR blocks

You can associate a single IPv6 CIDR block when
you create a new VPC or you can associate up to five IPv6 CIDR blocks from `/44` to `/60` in increments of `/4`.
You can request an IPv6 CIDR block from Amazon's pool of IPv6 addresses. For more information, see [Add or remove a CIDR block from your VPC](add-ipv4-cidr.md "add-ipv4-cidr.md").

If you've associated an IPv6 CIDR block with your VPC, you can associate an IPv6 CIDR
block with an existing subnet in your VPC or when you create a new subnet. For
more information, see [Subnet sizing for IPv6](subnet-sizing.md#subnet-sizing-ipv6 "subnet-sizing.md#subnet-sizing-ipv6").

For example, you create a VPC and specify that you want to associate an Amazon-provided
IPv6 CIDR block with the VPC. Amazon assigns the following IPv6 CIDR block to your
VPC: `2001:db8:1234:1a00::/56`. You cannot choose the range of IP
addresses yourself. You can create a subnet and associate an IPv6 CIDR block from
this range; for example, `2001:db8:1234:1a00::/64`.

You can disassociate an IPv6 CIDR block from a VPC. After you've disassociated an
IPv6 CIDR block from a VPC, you cannot expect to receive the same CIDR if you associate
an IPv6 CIDR block with your VPC again later.
