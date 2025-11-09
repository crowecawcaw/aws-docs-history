# Security groups in AWS PCS

Security groups in Amazon EC2 act as virtual firewalls to control inbound and outbound traffic to
instances. Use a launch template for an AWS PCS compute node group to add or remove security
groups to its instances. If your launch template doesn't contain any network interfaces, use
`SecurityGroupIds` to provide a list of security groups. If your launch template
defines network interfaces, you must use the `Groups` parameter to assign security
groups to each network interface. For more information about launch templates, see
[Using Amazon EC2 launch templates
with AWS PCS](working-with_launch-templates.md "working-with_launch-templates.md").

###### Note

Changes to the security group configuration in the launch template only affects new
instances launched after the compute node group is updated.

## Security group requirements

and considerations

AWS PCS creates a cross-account [Elastic Network Interface (ENI)](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in the
subnet you specify when creating a cluster. This provides the HPC scheduler, which is running in
an account managed by AWS, a path to communicate with EC2 instances launched by
AWS PCS. You must provide a security group for that ENI that allows 2-way
communication between the scheduler ENI and your cluster EC2 instances.

A straightforward way to accomplish this is to create a permissive self-referencing security
group that permits TCP/IP traffic on all ports between all members of the group. You can attach
this to both the cluster and to node group EC2 instances.

### Example

permissive security group configuration

IPv4

| Rule type | Protocols | Ports | Source | Destination |
| --------- | --------- | ----- | ------ | ----------- |
| Inbound   | All       | All   | Self   |             |
| Outbound  | All       | All   |        | 0.0.0.0/0   |
| Outbound  | All       | All   |        | Self        |

IPv6

| Rule type | Protocols | Ports | Source | Destination |
| --------- | --------- | ----- | ------ | ----------- |
| Inbound   | All       | All   | Self   |             |
| Outbound  | All       | All   |        | ::/0        |
| Outbound  | All       | All   |        | Self        |

These rules allow all traffic to flow freely between the Slurm controller and nodes, allows
all outbound traffic to any destination, and enables [EFA traffic](../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security "../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security").

### Example restrictive security group configuration

You can also limit the open ports between the cluster and its compute nodes. For the Slurm
scheduler, the security group attached to your cluster must allow the following ports:

- 6817 – enable inbound connections to `slurmctld` from EC2
  instances
- 6818 – enable outbound connections from `slurmctld` to
  `slurmd` running on EC2 instances

The security group attached to your compute nodes must allow the following ports:

- 6817 – enable outbound connections to `slurmctld` from EC2
  instances.
- 6818 – enable inbound and outbound connections to `slurmd` from
  `slurmctld` and from `slurmd` on node group instances
- 60001–63000 – inbound and outbound connections between node group instances
  to support `srun`
- EFA traffic between node group instances. For more information, see [Prepare
  an EFA-enabled security group](../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security "../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security") in the _User Guide for Linux
  Instances_
- Any other inter-node traffic required by your workload
