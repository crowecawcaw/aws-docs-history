# Control traffic to VPC Lattice using network ACLs

A network access control list (ACL) allows or denies specific inbound or outbound
traffic at the subnet level. The default network ACL allows all inbound and outbound
traffic. You can create custom network ACLs for your subnets to provide an additional
layer of security. For more information, see [Network ACLs](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md") in the
_Amazon VPC User Guide_.

###### Contents

- [Network ACLs for your client
  subnets](#network-acl-client-subnets "#network-acl-client-subnets")
- [Network ACLs for your target
  subnets](#network-acl-target-subnets "#network-acl-target-subnets")

## Network ACLs for your client

subnets

The network ACLs for client subnets must allow traffic between clients and
VPC Lattice. You can get the IP address ranges to allow from the [managed prefix list](security-groups.md#managed-prefix-list "security-groups.md#managed-prefix-list") for VPC Lattice.

The following is an example inbound rule.

| Source                   | Protocol | Port range | Comment                                   |
| ------------------------ | -------- | ---------- | ----------------------------------------- |
| `vpc_lattice_cidr_block` | TCP      | 1025-65535 | Allow traffic from VPC Lattice to clients |

The following is an example outbound rule.

| Destination              | Protocol   | Port range | Comment                                   |
| ------------------------ | ---------- | ---------- | ----------------------------------------- |
| `vpc_lattice_cidr_block` | `listener` | `listener` | Allow traffic from clients to VPC Lattice |

## Network ACLs for your target

subnets

The network ACLs for target subnets must allow traffic between targets and
VPC Lattice on both the target port and the health check port. You can get the IP
address ranges to allow from the [managed prefix
list](security-groups.md#managed-prefix-list "security-groups.md#managed-prefix-list") for VPC Lattice.

The following is an example inbound rule.

| Source                   | Protocol       | Port range     | Comment                                                |
| ------------------------ | -------------- | -------------- | ------------------------------------------------------ |
| `vpc_lattice_cidr_block` | `target`       | `target`       | Allow traffic from VPC Lattice to targets              |
| `vpc_lattice_cidr_block` | `health check` | `health check` | Allow health check traffic from VPC Lattice to targets |

The following is an example outbound rule.

| Destination              | Protocol       | Port range | Comment                                                |
| ------------------------ | -------------- | ---------- | ------------------------------------------------------ |
| `vpc_lattice_cidr_block` | `target`       | 1024-65535 | Allow traffic from targets to VPC Lattice              |
| `vpc_lattice_cidr_block` | `health check` | 1024-65535 | Allow health check traffic from targets to VPC Lattice |
