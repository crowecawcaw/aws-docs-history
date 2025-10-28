# Troubleshoot compute node bootstrap and

registration problems in AWS PCS

When compute nodes fail to bootstrap or register properly with your AWS PCS cluster, you might
experience the following symptoms:

- Jobs don't start
- You can't connect to instances in AWS Systems Manager
- Instances shut down unexpectedly
- Instances are continuously replaced
  These failures can be caused by problems during EC2 instance launch or during the AWS PCS
  compute node bootstrap process. This topic describes procedures to help you troubleshoot problems
  during the AWS PCS node bootstrap process. For more information about troubleshooting EC2 instance
  launch, see [Troubleshoot Amazon EC2 instance launch problems](../../../AWSEC2/latest/UserGuide/troubleshooting-launch.md "../../../AWSEC2/latest/UserGuide/troubleshooting-launch.md") in the _Amazon Elastic Compute Cloud User
  Guide_.

Bootstrap failures occur when an EC2 instance launches successfully but fails during the
process of joining the AWS PCS cluster. The bootstrap process includes two main phases:

- **Node registration** – The EC2 instance calls the
  [RegisterComputeNodeGroupInstance](../APIReference/API_RegisterComputeNodeGroupInstance.md "../APIReference/API_RegisterComputeNodeGroupInstance.md") AWS PCS API action to register with the AWS PCS service.
  Failures can occur due to problems in the following:
  - Permissions
    - [Wrong instance
      profile](#troubleshooting-compute-node-bootstrap-wrong-instance-profile "#troubleshooting-compute-node-bootstrap-wrong-instance-profile")

  - Networking
    - [Can't
      connect to AWS PCS endpoints](#troubleshooting-compute-node-bootstrap-connect-to-endpoints "#troubleshooting-compute-node-bootstrap-connect-to-endpoints")
    - [Misconfigured AWS PCS endpoint](#troubleshooting-compute-node-bootstrap-misconfigured-pcs-endpoint "#troubleshooting-compute-node-bootstrap-misconfigured-pcs-endpoint")
    - [Instance in
      a public subnet without public IP](#troubleshooting-compute-node-bootstrap-public-subnet-no-public-ip "#troubleshooting-compute-node-bootstrap-public-subnet-no-public-ip")
    - [Multi-NIC
      instance in a public subnet](#troubleshooting-compute-node-bootstrap-multi-nic-public-subnet "#troubleshooting-compute-node-bootstrap-multi-nic-public-subnet")

- **Slurm integration** – The instance runs
  `slurmd` and joins the Slurm cluster. Failures can occur due to problems in the
  following:
  - Permissions
    - [Security group
      configuration](#troubleshooting-compute-node-bootstrap-security-groups "#troubleshooting-compute-node-bootstrap-security-groups")
    - [Slurmctld unable
      to ping compute node](#troubleshooting-compute-node-bootstrap-slurmctld-ping-issue "#troubleshooting-compute-node-bootstrap-slurmctld-ping-issue")

  - Custom AMI setup
    - [Missing NVIDIA
      drivers](#troubleshooting-compute-node-bootstrap-missing-nvidia-drivers "#troubleshooting-compute-node-bootstrap-missing-nvidia-drivers")
    - [ResumeTimeout
      reached](#troubleshooting-compute-node-bootstrap-resume-timeout "#troubleshooting-compute-node-bootstrap-resume-timeout")

## How Slurm works on

AWS PCS

It might help you to compare the standard way Slurm works to the way Slurm works on
AWS PCS.

###### Standard Slurm job processing

The following steps occur in standard Slurm job processing:

1. When you submit a job, `slurmctld` validates and queues the job.
2. When resources become available, `slurmctld` allocates existing nodes.
3. `slurmd` daemons run jobs on allocated nodes.

###### Slurm job processing on AWS PCS

The following steps occur in AWS PCS job processing:

1. When you submit a job, `slurmctld` validates and queues the job.
2. **When additional capacity is needed, AWS PCS uses the launch template
   for the compute node group to launch new EC2 instances.**
3. **New instances bootstrap into the cluster:**
   1. **Instances register with AWS PCS.**
   2. **Instances join the Slurm cluster.**

4. When resources are ready, `slurmctld` allocates nodes (including newly
   bootstrapped ones).
5. `slurmd` daemons run jobs on allocated nodes.

## Retrieve instance

logs

The first step in troubleshooting compute node bootstrap problems is to retrieve the
instance logs. You can use one of the following methods:

AWS CLI
Retrieve the console output from the compute node using the following command:

```
aws ec2 get-console-output --region `us-east-1` --instance-id `i-1234567890abcdef0` --output text
```

Replace `us-east-1` with your AWS Region and
`i-1234567890abcdef0` with your instance ID.

AWS Systems Manager
If you can connect to the instance using Systems Manager, you can view the bootstrap log file
directly:

1. Connect to the instance using Systems Manager. For more information, see [Starting a session](../../../systems-manager/latest/userguide/session-manager-working-with-sessions-start.md#start-ec2-console "../../../systems-manager/latest/userguide/session-manager-working-with-sessions-start.md#start-ec2-console") in the _Systems Manager User Guide_.
2. View the bootstrap log file:

```
sudo cat /var/log/amazon/pcs/bootstrap.log
```

###### Note

If there's an issue during the initialization phase, you might need to wait
approximately 20 minutes before you can connect to the instance. Systems Manager and SSH services start
only after initialization is completed or when bootstrap execution reaches a timeout in case
of failure.

## Retrieve

VPC/Subnet/Security Groups from an instance ID

To troubleshoot problems with your compute nodes, you might need to retrieve information
about the VPC, subnet, and security groups associated with your instances. If you don't know your
instance IDs, see [Finding compute node group instances in
AWS PCS](working-with_compute-instances.md "working-with_compute-instances.md").

AWS Management Console

###### To get VPC, subnet, and security groups

1. Open the [Amazon EC2 console](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2").
2. Choose **Instances**.
3. In the **Instances** table, choose the instance ID.
4. Find the **VPC ID** and **Subnet ID** in the
   displayed instance summary for the instance.
5. In the instance summary, choose the **Security** tab.
6. Find the **Security groups** in the **Security**
   tab.

AWS CLI
Use the following command to retrieve VPC, subnet, and security group information for
your instance:

```
aws ec2 describe-instances --instance-ids `i-1234567890abcdef0` --query 'Reservations[*].Instances[*].{InstanceId:InstanceId,VpcId:VpcId,SubnetId:SubnetId,SecurityGroups:SecurityGroups[*].GroupId}' --output table
```

## Node registration

problems

Node registration is the first action executed by a compute node during bootstrap. The node
calls the AWS PCS API endpoint to register itself with AWS PCS.
Registration failures usually show error messages similar to the following:

```
<13>Nov  5 08:10:27 user-data: Recipe: aws-pcs-environment::node_registration
<13>Nov  5 08:10:27 user-data:   * ruby_block[Register NodeGroup Instance] action run[2024-11-05T08:10:27+00:00] INFO: Processing ruby_block[Register NodeGroup Instance] action run (aws-pcs-environment::node_registration line 19)
<13>Nov  5 08:15:46 user-data:
<13>Nov  5 08:15:46 user-data:
<13>Nov  5 08:15:46 user-data:     ================================================================================
<13>Nov  5 08:15:46 user-data:     Error executing action `run` on resource 'ruby_block[Register NodeGroup Instance]'
<13>Nov  5 08:15:46 user-data:     ================================================================================
<13>Nov  5 08:15:46 user-data:
<13>Nov  5 08:15:46 user-data:     EOFError
```

### Wrong instance

profile

If the instance is unable to register, verify that the instance profile associated with the
compute node has the `pcs:RegisterComputeNodeGroupInstance` permission.

For more information about how to create a valid instance profile, see [Create an instance profile for AWS PCS](getting-started_create-cng_instance-profile.md "getting-started_create-cng_instance-profile.md").

### Can't

connect to AWS PCS endpoints

If your compute nodes are in a private subnet, make sure that you have configured VPC
endpoints for AWS PCS or that your subnet has a route to a NAT gateway for internet access.
For more information, see the following:

- [Access
  an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the _Amazon Virtual Private Cloud AWS PrivateLink_ guide.
- [Endpoints and service quotas for
  AWS PCS](service-endpoints-quotas.md "service-endpoints-quotas.md").
- [Connect
  your VPC to other networks](../../../vpc/latest/userguide/extend-intro.md "../../../vpc/latest/userguide/extend-intro.md") in the _Amazon Virtual Private Cloud User Guide_
- [AWS PCS Networking](working-with_networking.md "working-with_networking.md")

### Misconfigured AWS PCS endpoint

If you see an error message similar to the following, verify the policy associated with
your AWS PCS VPC endpoint:

```
com.amazon.coral.security.AccessDeniedException: User: arn:aws:sts::xxx:assumed-role/rolename/i-instanceid is not authorized to perform: pcs:RegisterComputeNodeGroupInstance on resource: arn:aws:pcs:us-west-2:xxx:cluster/cluster-id as either the resource does not exist, some policy explicitly denies access, or no policy grants access
```

For more information about how to configure VPC interface endpoints for AWS PCS, see [Access AWS Parallel Computing Service using an interface endpoint (AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md").

### Instance in

a public subnet without public IP

If your subnet doesn't have **auto-assign public IP** enabled
and your route configuration uses an internet gateway, instances can't communicate with the
AWS PCS API.

Instances in a subnet with an internet gateway must have a public IP address. To resolve
this issue, choose one of the following options:

- Add a VPC endpoint for AWS PCS to your cluster VPC. This enables instances to communicate
  with AWS PCS without the need for a public IP address to pass through the internet
  gateway.
- Use a private subnet with a NAT gateway, so that a public IP address is not
  required.
- Enable automatic public IP address assignment through your subnet or launch template so
  that instances can contact the API through the internet gateway. Note that this option is not
  valid for multi-network interface instances.

### Multi-NIC

instance in a public subnet

You must use a private subnet if you use an instance type that has multiple network
interfaces (NICs).

AWS public IP addresses can only be assigned to instances launched with a single network
interface. For more information about IP addresses, see [Assign a
public IPv4 address during instance launch](../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#public-ip-addresses "../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#public-ip-addresses") in the _Amazon EC2 User Guide for Linux
Instances_.

Multi-NIC instance types require a NAT gateway or an internal proxy in the subnet to access
the AWS PCS endpoint. Alternatively, you can add a VPC endpoint for AWS PCS to your cluster
VPC.

## Slurm cluster join

problems

After successful node registration, the compute node attempts to join the Slurm cluster. The
`slurmd` daemon on the node contacts the Slurm controller to register with the
cluster. Slurm join failures usually show error messages similar to the following:

```
<13>Nov  5 17:20:29 user-data: [2024-11-05T17:20:28+00:00] FATAL: Mixlib::ShellOut::ShellCommandFailed: service[slurmd] (aws-pcs-slurm::finalize_slurm line 18) had an error: Mixlib::ShellOut::ShellCommandFailed: Expected process to exit with [0], but received '1'
<13>Nov  5 17:20:29 user-data: ---- Begin output of ["/usr/bin/systemctl", "--system", "start", "slurmd"] ----
<13>Nov  5 17:20:29 user-data: STDOUT:
<13>Nov  5 17:20:29 user-data: STDERR: Job for slurmd.service failed because the control process exited with error code. See "systemctl status slurmd.service" and "journalctl -xe" for details.
<13>Nov  5 17:20:29 user-data: ---- End output of ["/usr/bin/systemctl", "--system", "start", "slurmd"] ----
```

### Security group

configuration

Verify that your security groups are configured correctly to allow communication between
compute nodes and the Slurm controller. The security groups must allow the following
traffic:

- Port 6817 for `slurmd` to communicate with `slurmctld`
- Port 6818 for `slurmctld` to ping `slurmd`

For more information about security group requirements, see the following topics:

- [Create security groups for AWS PCS](getting-started_create-sg.md "getting-started_create-sg.md")
- [Create launch templates for AWS PCS](getting-started_create-cng_launch-templates.md "getting-started_create-cng_launch-templates.md")
- [Security group requirements
  and considerations](working-with_networking_sg.md#working-with_networking_sg-requirements "working-with_networking_sg.md#working-with_networking_sg-requirements")

###### Important

The cluster security group that you associated with your cluster during cluster creation
must also be configured in your compute node group security groups to allow compute nodes to
communicate with the controller.

### Missing NVIDIA

drivers

If the instance bootstraps correctly but jobs don't start, and you see error messages
similar to the following in your instance logs, you might be missing NVIDIA drivers:

```
<13>Dec  2 13:52:00 user-data: [2024-12-02T13:52:00.094+00:00] - /opt/aws/pcs/bin/pcs_bootstrap_config_always.sh: INFO: nvidia-smi not found!
...
<13>Dec  2 13:54:10 user-data: Job for slurmd.service failed because the control process exited with error code. See "systemctl status slurmd.service" and "journalctl -xe" for details.
<13>Dec  2 13:54:12 user-data: [2024-12-02T13:54:12.718+00:00] - /opt/aws/pcs/bin/pcs_bootstrap_finalize.sh: INFO: systemctl could not start slurmd!
```

If you connect to the instance and check the `slurmd` daemon status, you might
see an error similar to the following:

```
$ systemctl status slurmd
...
fatal: can't stat gres.conf file /dev/nvidia0: No such file or directory
```

To resolve this issue, install NVIDIA drivers on your custom AMI. For more information, see
[Step 4 – (Optional) Install
additional drivers, libraries, and application software](working-with_ami_custom_install-software.md "working-with_ami_custom_install-software.md").

### ResumeTimeout

reached

If a compute node and its EC2 instance are terminated because the node is unhealthy, AWS PCS
might not support the AMI or there might be network problems. The EC2 instance runs for
approximately 30 minutes until Slurm's ResumeTimeout is reached and marks the node as
`DOWN`.

If the instance doesn't bootstrap correctly and isn't registered with AWS PCS (no
`RegisterComputeNodeGroupInstance` call for the EC2 instance), check your instance
logs for error messages similar to the following:

```
/opt/aws/pcs/bin/pcs_bootstrap_init.sh: No such file or directory
```

This error indicates that the AWS PCS bootstrap software is not part of the AMI. To resolve
this issue, ensure that your custom AMI includes the AWS PCS bootstrap software. For more
information, see [Custom Amazon Machine Images (AMIs) for
AWS PCS](working-with_ami_custom.md "working-with_ami_custom.md").

### Slurmctld unable

to ping compute node

If the instance correctly executes the bootstrap procedure and is registered with AWS PCS,
but `slurmctld` is unable to see it and submit jobs to it, the instance is set to
`DOWN` after some time and then terminated.

This might be caused by misconfigured security groups. For example, if port 6817 is enabled
to allow `slurmd` to communicate with `slurmctld`, but port 6818 is
missing to allow `slurmctld` to ping `slurmd`.

Verify that your security groups include all required rules as documented in [Security group requirements
and considerations](working-with_networking_sg.md#working-with_networking_sg-requirements "working-with_networking_sg.md#working-with_networking_sg-requirements").
