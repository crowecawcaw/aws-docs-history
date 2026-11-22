

# Security groups in AWS PCS

Security groups in Amazon EC2 control inbound and outbound traffic to instances. To set the security groups for a compute node group, specify `securityGroupIds` on the compute node group, in its custom launch template, or both. With standard configuration, you must specify `securityGroupIds`. If you specify security groups in both places, AWS PCS uses only the security groups on the compute node group. It doesn't add the security groups in the launch template. For more information, see [Configuring instance settings for compute node groups in AWS PCS](working-with_cng_instance-settings.md).

In a launch template that doesn't define network interfaces, use the launch template `SecurityGroupIds` parameter to provide a list of security groups. If your launch template defines network interfaces, use the `Groups` parameter to assign security groups to each network interface. In this case, you can't specify `securityGroupIds` on the compute node group. For more information about launch templates, see [Using Amazon EC2 launch templates with AWS PCS](working-with_launch-templates.md).

**Note**  
When you change the security groups of a compute node group, AWS PCS replaces its compute nodes after their running jobs finish. This also happens when you update the compute node group to a launch template version that has different security groups. If you edit the rules of a security group that a compute node group uses, the change takes effect immediately on running and future compute nodes. For more information, see [Updating a compute node group in AWS PCS](working-with_cng_update.md).

## Security group requirements and considerations
<a name="working-with_networking_sg-requirements"></a>

AWS PCS creates a cross-account [Elastic Network Interface (ENI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the subnet you specify when creating a cluster. This provides the HPC scheduler, which is running in an account managed by AWS, a path to communicate with EC2 instances launched by AWS PCS. You must provide a security group for that ENI that allows 2-way communication between the scheduler ENI and your cluster EC2 instances. 

A straightforward way to accomplish this is to create a permissive self-referencing security group that permits TCP/IP traffic on all ports between all members of the group. You can attach this to both the cluster and to node group EC2 instances. 

### Example permissive security group configuration
<a name="working-with_networking_sg-requirements_permissive-security-config"></a>

------
#### [ IPv4 ]


| Rule type | Protocols | Ports | Source | Destination  | 
| --- | --- | --- | --- | --- | 
| Inbound | All | All | Self |  | 
| Outbound | All | All |  | 0.0.0.0/0 | 
| Outbound | All | All |  | Self | 

------
#### [ IPv6 ]


| Rule type | Protocols | Ports | Source | Destination  | 
| --- | --- | --- | --- | --- | 
| Inbound | All | All | Self |  | 
| Outbound | All | All |  | ::/0 | 
| Outbound | All | All |  | Self | 

------

These rules allow all traffic to flow freely between the Slurm controller and nodes, allows all outbound traffic to any destination, and enables [EFA traffic](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html#efa-start-security).

### Example restrictive security group configuration
<a name="working-with_networking_sg-requirements_restrictive-security-config.title"></a>

You can also limit the open ports between the cluster and its compute nodes. For the Slurm scheduler, the security group attached to your cluster must allow the following ports:
+ 6817 – enable inbound connections to `slurmctld` from EC2 instances
+ 6818 – enable outbound connections from `slurmctld` to `slurmd` running on EC2 instances

The security group attached to your compute nodes must allow the following ports:
+ 6817 – enable outbound connections to `slurmctld` from EC2 instances.
+ 6818 – enable inbound and outbound connections to `slurmd` from `slurmctld` and from `slurmd` on node group instances 
+ AWS PCS doesn't set a fixed `srun` port range by default, so `srun` uses the operating system's ephemeral ports (on Linux, 32768–60999) unless you pin it with the [SrunPortRange](https://slurm.schedmd.com/slurm.conf.html#OPT_SrunPortRange) custom Slurm setting (for example, `SrunPortRange=60001-63000`) and allow that range in your security group rules. See [Custom Slurm settings for AWS PCS clusters](slurm-custom-settings-cluster.md).
+ EFA traffic between node group instances. For more information, see [Prepare an EFA-enabled security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html#efa-start-security) in the *User Guide for Linux Instances*
+ Any other inter-node traffic required by your workload