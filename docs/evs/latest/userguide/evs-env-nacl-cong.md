# Configure a network access control list to control Amazon EVS VLAN subnet traffic

A network access control list (ACL) allows or denies specific inbound or outbound traffic at the subnet level.
You can use network ACLs to control inbound and outbound traffic for your Amazon EVS VLAN subnets.
For more information, see [Create a network ACL for your VPC](../../../vpc/latest/userguide/create-network-acl.md "../../../vpc/latest/userguide/create-network-acl.md") in the _Amazon VPC User Guide_.

###### Important

EC2 security groups do not function on elastic network interfaces that are attached to Amazon EVS VLAN subnets.
To control traffic to and from Amazon EVS VLAN subnets, you must use a network access control list.

###### Warning

Amazon EVS requires access to your VCF deployment.
You must configure your security groups and network access control lists (ACLs) to allow Amazon EVS to communicate with:

- DNS servers over TCP/UDP port 53.
- Host management VLAN subnet over HTTPS and SSH.
- Management VM VLAN subnet over HTTPS and SSH.
  If your security groups and network ACLs do not allow this access, Amazon EVS environment deployment will fail and existing environments may have a degraded compliance status.
