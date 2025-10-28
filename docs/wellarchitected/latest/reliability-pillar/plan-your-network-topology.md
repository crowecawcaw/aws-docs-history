# Plan your network topology

Workloads often exist in multiple environments. These include multiple cloud environments
(both publicly accessible and private) and possibly your existing data center infrastructure.
Plans must include network considerations, such as intrasystem and intersystem connectivity,
public IP address management, private IP address management, and domain name resolution.

When architecting systems using IP address-based networks, you must plan network topology
and addressing in anticipation of possible failures, and to accommodate future growth and
integration with other systems and their networks.

Amazon Virtual Private Cloud (Amazon VPC) lets you provision a private, isolated section of the AWS Cloud where
you can launch AWS resources in a virtual network.

###### Best practices

- [REL02-BP01 Use highly available network connectivity for your
  workload public endpoints](rel_planning_network_topology_ha_conn_users.md "rel_planning_network_topology_ha_conn_users.md")
- [REL02-BP02 Provision redundant connectivity between private
  networks in the cloud and on-premises environments](rel_planning_network_topology_ha_conn_private_networks.md "rel_planning_network_topology_ha_conn_private_networks.md")
- [REL02-BP03 Ensure IP subnet
  allocation accounts for expansion and availability](rel_planning_network_topology_ip_subnet_allocation.md "rel_planning_network_topology_ip_subnet_allocation.md")
- [REL02-BP04 Prefer hub-and-spoke topologies over many-to-many
  mesh](rel_planning_network_topology_prefer_hub_and_spoke.md "rel_planning_network_topology_prefer_hub_and_spoke.md")
- [REL02-BP05 Enforce non-overlapping private IP address ranges in
  all private address spaces where they are connected](rel_planning_network_topology_non_overlap_ip.md "rel_planning_network_topology_non_overlap_ip.md")
