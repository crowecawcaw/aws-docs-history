# Public and private replication

instances

You can specify if a replication instance has a public or private IP address that the
instance uses to connect to the source and target databases.

A _private replication instance_ has a private IP
address that you can't access outside the replication network. You use a private
instance when both source and target databases are in the same network that is connected
to the virtual private cloud (VPC) of the replication instance. The network can be
connected to the VPC by using a virtual private network (VPN), Direct Connect, or VPC
peering.

A _VPC peering_ connection is a networking connection between two
VPCs. It allows routing using each VPC's private IP addresses as if they were in
the same network. For more information about VPC peering, see [VPC peering](../../../vpc/latest/userguide/vpc-peering.md "../../../vpc/latest/userguide/vpc-peering.md") in the _Amazon VPC
User Guide_.

A _public replication instance_ can use the VPC
security group of the replication instance, and the replication instance's public
IP address or the NAT gateway's public IP address. These connections form a network
that you use for data migration.
