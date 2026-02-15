# Creating a compute node group in

AWS PCS

This topic provides an overview of available options and describes what to consider when you
create a compute node group in AWS Parallel Computing Service (AWS PCS). If this is your first time creating
a compute node group in AWS PCS, we recommend you follow the
tutorial in [Get started with AWS Parallel Computing Service](getting-started.md "getting-started.md").
The tutorial can help you create a working HPC
system without expanding into all the available options and system architectures that are
possible.

###### Note

You can configure custom Slurm settings on compute node groups to control resource utilization and node-level behaviors. For more information, see [Configuring custom Slurm settings in AWS PCS](slurm-custom-settings.md "slurm-custom-settings.md").

###### Important

AWS PCS currently requires a kernel with IPv4 support for local node
communication, even when you use AWS PCS in an IPv6-only network. For more information,
see [Custom Amazon Machine Images (AMIs) for
AWS PCS](working-with_ami_custom.md "working-with_ami_custom.md").

## Prerequisites

- Sufficient service quotas to launch the desired number of EC2 instances in your AWS Region.
  You can use the [AWS Management Console](https://console.aws.amazon.com/servicequotas "https://console.aws.amazon.com/servicequotas") to check and request
  increases to your service quotas.
- An existing VPC and subnet(s) that meet AWS PCS networking requirements.
  We recommend that you thoroughly understand these requirements before you deploy a
  cluster for production use. For more information, see
  [AWS PCS VPC and subnet requirements
  and considerations](working-with_networking_vpc-requirements.md "working-with_networking_vpc-requirements.md").
  You can also use a CloudFormation template to create a VPC and subnets. AWS provides
  an HPC recipe for the CloudFormation template. For more information, see
  [aws-hpc-recipes](https://github.com/aws-samples/aws-hpc-recipes/tree/main/recipes/net/hpc_large_scale "https://github.com/aws-samples/aws-hpc-recipes/tree/main/recipes/net/hpc_large_scale") on GitHub.
- An IAM instance profile with permissions to call the AWS PCS
  `RegisterComputeNodeGroupInstance` API action and access to any other AWS
  resources required for your node group instances. For more information,
  see [IAM instance profiles for AWS Parallel Computing Service](security-instance-profiles.md "security-instance-profiles.md").
- A launch template for your node group instances. For more information, see
  [Using Amazon EC2 launch templates
  with AWS PCS](working-with_launch-templates.md "working-with_launch-templates.md").
- To create a compute node group that uses Amazon EC2 **Spot**
  instances, you must have the **AWSServiceRoleForEC2Spot**
  service-linked role in your AWS account. For more information, see
  [Amazon EC2 Spot role for AWS PCS](spot-role.md "spot-role.md").

## Create a compute node group in

AWS PCS

You can create a compute node group using the AWS Management Console or the AWS CLI.

AWS Management Console

###### To create your compute node group using the console

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs/home#/clusters "https://console.aws.amazon.com/pcs/home#/clusters").
2. Select the cluster where you want to create a compute node group. Navigate to
   **Compute node groups** and choose **Create**.
3. In the **Compute node group setup** section, provide a name for your
   node group. The name can only contain case-sensitive alphanumeric characters and hyphens. It
   must start with an alphabetic character and can't be longer than 25 characters. The name
   must be unique within the cluster.
4. Under **Computing configuration**, enter or select these
   values:
   1. **EC2 launch template** – Select a custom launch template to
      use for this node group. Launch templates can be used to customize network settings such
      as subnet, and security groups, monitoring configuration, and instance-level storage. If
      you don't have a launch template prepared, see [Using Amazon EC2 launch templates
      with AWS PCS](working-with_launch-templates.md "working-with_launch-templates.md") to learn how to
      create one.

   ###### Important

   AWS PCS creates a managed launch template for each compute node group.
   These are named `pcs-`identifier`-do-not-delete`. Don't
   select these when you create or update a compute node group, or the node group won't function
   correctly. 2. **EC2 launch template version** – You must select a version of your
   custom launch template. If you change the version later, you must update the compute
   node group to detect changes in the launch template. For more information, see
   [Updating an AWS PCS compute node group](working-with_cng_update.md "working-with_cng_update.md"). 3. **AMI ID** – if your launch template doesn't include an AMI
   ID, or if you want to override the value in the launch template, provide an AMI ID here.
   Note that the AMI used for the node group must be compatible with AWS PCS. You can
   also select a sample AMI provided by AWS. For more information on this topic, see [Amazon Machine Images (AMIs) for AWS PCS](working-with_ami.md "working-with_ami.md"). 4. **IAM instance profile** – Choose an instance profile for
   the node group. An instance profile grants the instance permissions to access AWS
   resources and services securely. If you don't have one prepared, you can select **Create a basic profile** to have AWS PCS create one for you with the minimum policy, or see [IAM instance profiles for AWS Parallel Computing Service](security-instance-profiles.md "security-instance-profiles.md"). 5. **Subnets** – Choose one or more subnets in the VPC where
   your AWS PCS cluster is deployed. If you select multiple subnets, EFA communications
   won't be available between nodes, and communication between nodes in different subnets
   might have increased latency. Make sure the subnets you specify here match any that you define in
   the EC2 launch template. 6. **Instances** – Choose one or more instance types to fulfill
   scaling requests in the node group. All instance types must have the same processor
   architecture (x86_64 or arm64) and number of vCPUs. If the instances have
   GPUs, all instance types must have the same number of GPUs. 7. **Scaling configuration** – Specify the minimum and maximum
   number of instances for the node group. You can define either a static configuration,
   where there is a fixed number of nodes running, or a dynamic configuration, where up to
   the maximum count of nodes can run. For a static configuration, set minimum and maximum to
   the same, greater than zero number. For a dynamic configuration, set minimum instances to
   zero and maximum instances to a number greater than zero. AWS PCS doesn't support
   compute node groups with a mix of static and dynamic instances.

5. (Optional) Under **Additional settings**, specify the
   following:
   1. **Purchase option** – select On-Demand Instances,
      Spot Instances, or an existing Capacity Block. Also choose **On-Demand**
      if you plan to use an On-Demand Capacity Reservation (ODCR). For more information,
      see [Using ODCRs with AWS PCS](capacity-reservations-odcr.md "capacity-reservations-odcr.md").
      Choose **Capacity Block** to use an existing Amazon EC2 Capacity Blocks for ML
      reservation. For more information, see [Using Amazon EC2 Capacity Blocks for ML with AWS PCS](capacity-blocks.md "capacity-blocks.md").
   2. **Allocation strategy** – if you have selected the Spot
      purchase option, you can specify how Spot capacity pools are chosen when launching
      instances in the node group. For more information, see [Allocation strategies for Spot Instances](../../../AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.md "../../../AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.md") in the _Amazon Elastic Compute Cloud User Guide_.
      This option has no effect if you have
      selected the On-demand purchase option.

6. (Optional) In the **Slurm custom settings** section,
   you can add parameter name and value pairs to configure additional Slurm settings. For a complete list of supported parameters, see [Custom Slurm settings for AWS PCS compute node groups](slurm-custom-settings-cng.md "slurm-custom-settings-cng.md").
7. (Optional) Under **Tags**, add any tags to your compute node
   group.
8. Choose **Create compute node group**. The **Status**
   field shows `Creating` while AWS PCS provisions the node group.
   This can take several minutes.

###### Recommended next step

- Add your node group to a queue in AWS PCS to enable it to process jobs.

AWS CLI

###### To create your compute node group using AWS CLI

Create your queue with the command that follows. Before running the command, make the
following replacements:

1. Replace `region`with the ID of the AWS Region to create
   your cluster in, such as `us-east-1`.
2. Replace `my-cluster` with the name or `clusterId`of
   your cluster.
3. Replace `my-node-group`with the name for your compute node
   group. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It
   must start with an alphabetic character and can't be longer than 25 characters. The name
   must be unique within the cluster.
4. Replace `subnet-ExampleID1` with one or more subnets IDs from
   your cluster VPC.
5. Replace `lt-ExampleID1` with the ID for your custom launch
   template. If you don't have one prepared, see [Using Amazon EC2 launch templates
   with AWS PCS](working-with_launch-templates.md "working-with_launch-templates.md") to learn how to create
   one.

###### Important

AWS PCS creates a managed launch template for each compute node group.
These are named `pcs-`identifier`-do-not-delete`. Don't
select these when you create or update a compute node group, or the node group won't function
correctly. 6. Replace `launch-template-version` with a specific launch template version.
AWS PCS associates your node group with that specific version of the launch template. 7. Replace `arn:InstanceProfile`with the ARN of your IAM instance
profile. If you don't have one prepared, see [Using Amazon EC2 launch templates
with AWS PCS](working-with_launch-templates.md "working-with_launch-templates.md") for guidance. 8. Replace `min-instances` and
`max-instances` with integer values. You can define either a
static configuration, where there is a fixed number of nodes running, or a dynamic
configuration, where up to the maximum count of nodes can run. For a static configuration,
set minimum and maximum to the same, greater than zero number. For a dynamic configuration,
set minimum instances to zero and maximum instances to a number greater than zero.
AWS PCS doesn't support compute node groups with a mix of static and dynamic instances. 9. Replace `t3.large` with another instance type. You can add
more instance types by specifying a list of `instanceType` settings. For example,
`--instance-configs instanceType=c6i.16xlarge instanceType=c6a.16xlarge`.
All instance types must have the same processor architecture (x86_64 or arm64) and
number of vCPUs. If the instances have GPUs, all instance types must have the same
number of GPUs.

```
aws pcs create-compute-node-group --region `region` \
    --cluster-identifier `my-cluster` \
    --compute-node-group-name `my-node-group` \
    --subnet-ids `subnet-ExampleID1` \
    --custom-launch-template id=`lt-ExampleID1`,version='`launch-template-version`' \
    --iam-instance-profile-arn=`arn:InstanceProfile` \
    --scaling-config minInstanceCount=`min-instances`,maxInstanceCount=`max-instance` \
    --instance-configs instanceType=`t3.large`
```

###### Example– Creating a compute node group with custom Slurm settings

```
aws pcs create-compute-node-group --region `region` \
    --cluster-identifier `my-cluster` \
    --compute-node-group-name `my-node-group` \
    --subnet-ids `subnet-ExampleID1` \
    --custom-launch-template id=`lt-ExampleID1`,version='`launch-template-version`' \
    --iam-instance-profile-arn=`arn:InstanceProfile` \
    --scaling-config minInstanceCount=`min-instances`,maxInstanceCount=`max-instance` \
    --instance-configs instanceType=`t3.large` \
    --slurm-configuration \
    'slurmCustomSettings=[{parameterName=Features,parameterValue="`gpu,nvme`"}]'
```

For more information, see [Custom Slurm settings for AWS PCS compute node groups](slurm-custom-settings-cng.md "slurm-custom-settings-cng.md").

There are several optional configuration settings you can add to the
`create-compute-node-group` command.

- You can specify `--amiId` if your custom launch template doesn't include a
  reference to an AMI, or if you wish to override that value. Note that the AMI used for the
  node group must be compatible with AWS PCS. You can also select a sample AMI provided by
  AWS. For more information on this topic, see [Amazon Machine Images (AMIs) for AWS PCS](working-with_ami.md "working-with_ami.md").
- Use `--purchase-option` to choose the way AWS PCS purchases EC2 instances
  for your compute node group. On-Demand is the default.
  - `ONDEMAND` – Use On-Demand Instances. Also choose this option
    if you plan to use an On-Demand Capacity Reservation (ODCR).
    For more information, see [Using ODCRs with AWS PCS](capacity-reservations-odcr.md "capacity-reservations-odcr.md").
  - `SPOT` – Use Spot Instances. If you choose Spot instances,
    you can also use `--allocation-strategy` to define
    how AWS PCS chooses Spot capacity pools when it launches instances in the node group.
    For more information, see [Allocation strategies for Spot Instances](../../../AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.md "../../../AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.md") in the _Amazon Elastic Compute Cloud User
    Guide_.
  - `CAPACITY_BLOCK` – Use an existing Amazon EC2 Capacity Blocks for ML
    reservation. For more information, see [Using Amazon EC2 Capacity Blocks for ML with AWS PCS](capacity-blocks.md "capacity-blocks.md").

- It is possible to provide Slurm configuration options for the nodes in
  the node group using `--slurm-configuration`. You can set the weight (scheduling
  priority) and real memory. Nodes with lower weights have higher priority, and the units are
  arbitrary. For more information, see [Weight](https://slurm.schedmd.com/slurm.conf.html#OPT_Weight "https://slurm.schedmd.com/slurm.conf.html#OPT_Weight")
  in the Slurm documentation.
  Real memory sets the size (in GB) of real memory on nodes in the node
  group. It is meant to be used in conjunction with the `CR_CPU_Memory` option for
  the cluster in AWS PCS in your Slurm configuration. For more information,
  see [RealMemory](https://slurm.schedmd.com/slurm.conf.html#OPT_RealMemory "https://slurm.schedmd.com/slurm.conf.html#OPT_RealMemory") in the Slurm documentation.

###### Important

It can take several minutes to create the compute node group.

You can query the status of your node group with the following command. You won’t be able
to associate the node group with a queue until its status reaches `ACTIVE`.

```
aws pcs get-compute-node-group --region `region` \
    --cluster-identifier `my-cluster` \
    --compute-node-group-identifier `my-node-group`
```
