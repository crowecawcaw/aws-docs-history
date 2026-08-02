# Subnet compatibility for Resolver endpoints

We recommend using [VPC Resolver on AWS Outposts](outpost-resolver-getting-started.md "outpost-resolver-getting-started.md") to create endpoints on AWS Outposts Racks.

###### Important

Outposts subnets with [Local Network Interface (LNI)](../../../outposts/latest/server-userguide/local-network-interface.md "../../../outposts/latest/server-userguide/local-network-interface.md") enabled are not compatible with VPC Resolver endpoints.
If you enable LNI on a subnet that contains VPC Resolver endpoint elastic network interfaces (ENIs), those ENIs stop functioning.

To avoid this issue:

- Before creating a Resolver endpoint, verify that the target subnets don't have LNI enabled.
- Don't enable LNI on subnets that already contain Resolver endpoint ENIs.
- If you need both LNI and Resolver endpoints, use separate subnets for each.
  For more information about LNI, see
  [Local network interfaces](../../../outposts/latest/server-userguide/local-network-interface.md "../../../outposts/latest/server-userguide/local-network-interface.md")
  in the _AWS Outposts User Guide_.
