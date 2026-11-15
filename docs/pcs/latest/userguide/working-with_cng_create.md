

# Creating a compute node group in AWS PCS
<a name="working-with_cng_create"></a>

This topic describes how to create a compute node group in AWS Parallel Computing Service (AWS PCS). When you create a compute node group, you choose how to configure its compute nodes. With standard configuration, you specify the AMI, security groups, and SSH key pair on the compute node group. These are called instance settings. With launch template configuration, you also use a custom Amazon EC2 launch template, for Amazon EC2 settings that aren't available as instance settings, such as network interfaces or capacity reservations.

You can also configure custom Slurm settings, and node lifecycle actions that run scripts at defined points in a compute node's lifecycle, such as to mount file systems or install software. For more information, see [Configuring custom Slurm settings in AWS PCS](slurm-custom-settings.md) and [Node lifecycle actions](cng-node-lifecycle-actions.md).

If this is your first time creating a compute node group in AWS PCS, we recommend that you follow the tutorial in [Get started with AWS Parallel Computing Service](getting-started.md).

## Prerequisites
<a name="working-with_cng_create_prereq"></a>
+ Sufficient service quotas to launch the desired number of EC2 instances in your AWS Region. You can use the [Service Quotas console](https://console.aws.amazon.com/servicequotas) to check and request increases to your service quotas.
+ An existing VPC and subnets that meet AWS PCS networking requirements. We recommend that you understand these requirements before you deploy a cluster for production use. For more information, see [AWS PCS VPC and subnet requirements and considerations](working-with_networking_vpc-requirements.md). You can also use an AWS CloudFormation template to create a VPC and subnets. AWS provides an HPC recipe for the CloudFormation template. For more information, see [ aws-hpc-recipes](https://github.com/aws-samples/aws-hpc-recipes/tree/main/recipes/net/hpc_large_scale) on GitHub.
+ One or more security groups in your cluster VPC that allow traffic between compute nodes and the cluster. For more information, see [Security group requirements and considerations](working-with_networking_sg.md#working-with_networking_sg-requirements).
+ An AMI that is compatible with AWS PCS. For production workloads, you can use the AWS-maintained PCS-ready AWS Deep Learning AMI (DLAMI). If you're evaluating AWS PCS, you can use a sample AMI. You can also build your own AMI. For more information, see [Amazon Machine Images (AMIs) for AWS PCS](working-with_ami.md).
**Important**  
AWS PCS currently requires a kernel with IPv4 support for local node communication, even when you use AWS PCS in an IPv6-only network. For more information, see [Custom Amazon Machine Images (AMIs) for AWS PCS](working-with_ami_custom.md).
+ An IAM instance profile with permissions to call the AWS PCS `RegisterComputeNodeGroupInstance` API action and access to any other AWS resources that your compute nodes need. For more information, see [IAM instance profiles for AWS Parallel Computing Service](security-instance-profiles.md).
+ Permissions for the IAM identity that creates the compute node group. If you specify an SSH key pair, the identity also needs `ec2:DescribeKeyPairs`. For more information, see [Minimum permissions to use API actions](security-min-permissions.md#security-min-permissions_api).
+ The `AWSServiceRoleForEC2Spot` service-linked role in your AWS account, if you create a compute node group that uses Spot Instances. For more information, see [Amazon EC2 Spot role for AWS PCS](spot-role.md).
+ A custom launch template, only if you need Amazon EC2 settings that aren't available as instance settings, such as network interfaces or capacity reservations. A launch template can also provide the AMI, security groups, and SSH key pair. For more information, see [Using Amazon EC2 launch templates with AWS PCS](working-with_launch-templates.md) and [Configuring instance settings for compute node groups in AWS PCS](working-with_cng_instance-settings.md).

## How AWS PCS chooses the AMI, security groups, and SSH key pair
<a name="working-with_cng_create_instance-settings"></a>

If you don't use a custom launch template, AWS PCS uses the AMI, security groups, and SSH key pair that you specify on the compute node group.

If you use a custom launch template, you can specify each of these settings on the compute node group, in the launch template, or in both places. AWS PCS chooses each setting separately, as the following table shows. AWS PCS doesn't change your launch template.


**Instance settings with a custom launch template**  

| Setting | Specified on the compute node group | Specified only in the launch template | Not specified in either place | 
| --- | --- | --- | --- | 
| AMI ID | AWS PCS uses the AMI on the compute node group instead of any AMI in the launch template. | AWS PCS uses the AMI in the launch template. | AWS PCS rejects the request. | 
| Security groups | AWS PCS uses only the security groups on the compute node group. It doesn't add the security groups in the launch template. | AWS PCS uses the security groups in the launch template. | AWS PCS rejects the request. | 
| SSH key pair | AWS PCS uses the key pair on the compute node group instead of any key pair in the launch template. | AWS PCS uses the key pair in the launch template. | Compute nodes don't have a key pair. | 

For example, suppose that your launch template specifies an AMI and security group `sg-ExampleID1`, and you specify only security group `sg-ExampleID2` on the compute node group. Compute nodes use the AMI from the launch template and only `sg-ExampleID2`.

You can't specify security groups on the compute node group if your launch template defines network interfaces. Specify the security groups for each network interface in the launch template instead. For more information, see [Multiple network interfaces in AWS PCS](working-with_networking_multi-nic.md).

To change or remove these settings after you create the compute node group, see [Configuring instance settings for compute node groups in AWS PCS](working-with_cng_instance-settings.md).

## Launch templates that AWS PCS creates
<a name="working-with_cng_create_pcs-launch-templates"></a>

For each compute node group, AWS PCS creates a launch template of its own and uses it to launch compute nodes. AWS PCS creates this launch template whether or not you use a custom launch template. AWS PCS builds this launch template from the settings on the compute node group and, if you use one, your custom launch template. AWS PCS doesn't change your launch template.

The launch templates that AWS PCS creates are named `pcs-{{identifier}}-do-not-delete`. They appear with your own launch templates, for example, in the Amazon EC2 console.

**Important**  
Don't modify or delete a `pcs-{{identifier}}-do-not-delete` launch template, and don't choose one as the custom launch template for a compute node group. If you do, the compute node group won't work correctly.

## Create a compute node group in AWS PCS
<a name="working-with_cng_create_steps"></a>

You can create a compute node group by using the AWS Management Console or the AWS CLI.

------
#### [ AWS Management Console ]

**To create a compute node group (console)**

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs/home#/clusters).

1. Choose the cluster where you want to create a compute node group. Choose **Compute node groups**, and then choose **Create**.

1. Choose how to configure the compute nodes in the compute node group. **Standard configuration** is selected by default.
   + **Standard configuration** – Configure compute nodes without a launch template. You must provide an AMI ID and at least one security group. Compute nodes require Instance Metadata Service Version 2 (IMDSv2).
   + **Launch template configuration** – Use a custom Amazon EC2 launch template. A launch template can configure settings that aren't available as instance settings. Examples include network interfaces for EFA, capacity reservations, placement groups, block device mappings, and instance metadata options.

   For more information, see [Configuring instance settings for compute node groups in AWS PCS](working-with_cng_instance-settings.md).

1. In the **Compute node group setup** section, enter a name for your compute node group. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and be 3–25 characters long. The name must be unique within the cluster.

1. Under **Computing configuration**, enter or choose these values:

   1. **EC2 launch template** – If you chose **Launch template configuration**, choose a custom launch template to use for this node group. To learn how to create a launch template, see [Using Amazon EC2 launch templates with AWS PCS](working-with_launch-templates.md).

      Don't choose a launch template named `pcs-{{identifier}}-do-not-delete`. AWS PCS creates launch templates with this name for its own use. For more information, see [Launch templates that AWS PCS creates](#working-with_cng_create_pcs-launch-templates).

   1. **EC2 launch template version** – If you chose **Launch template configuration**, choose a version of your custom launch template. If you change the version later, you must update the compute node group to detect changes in the launch template. For more information, see [Updating a compute node group in AWS PCS](working-with_cng_update.md).

   1. **AMI ID** – Choose where to get the AMI, and then choose the AMI:
      + **PCS-ready AMIs** – AWS-maintained AMIs for production AI/ML and HPC workloads. This option is selected by default. For more information, see [Using PCS-ready DLAMI with AWS PCS](working-with_ami_pcs-ready-dlami.md).
      + **PCS sample AMIs** – Sample AMIs that AWS PCS provides, for evaluation only. For more information, see [Using sample Amazon Machine Images (AMIs) with AWS PCS](working-with_ami_samples.md).
      + **Shared AMIs** – AMIs that other AWS accounts share with you.
      + **Private AMIs** – AMIs that you created.
      + **Custom AMI** – Enter the ID of any AMI, such as an AMI from a third-party vendor or from AWS Marketplace.

      A shared, private, or custom AMI must be compatible with AWS PCS. For more information, see [Custom Amazon Machine Images (AMIs) for AWS PCS](working-with_ami_custom.md).

      Whether you must choose an AMI depends on how you configure the compute nodes:
      + **Standard configuration** – Required.
      + **Launch template configuration** – Optional. If you provide an AMI ID, AWS PCS uses it instead of the AMI in the launch template. If you leave this field empty, AWS PCS uses the AMI in the launch template. If neither the compute node group nor the launch template specifies an AMI, AWS PCS rejects the request.

   1. **IAM instance profile** – Choose an instance profile for the compute node group. An instance profile grants compute nodes permissions to access AWS resources and services. If you don't have an instance profile, choose **Create a basic profile**. AWS PCS creates one with the minimum policy. To create your own, see [IAM instance profiles for AWS Parallel Computing Service](security-instance-profiles.md).

   1. **Instances** – Choose one or more instance types to fulfill scaling requests in the node group. All instance types must have the same processor architecture (x86\_64 or arm64) and number of vCPUs. If the instance types have GPUs, all instance types must have the same number of GPUs.

   1. **Scaling configuration** – Specify the minimum and maximum number of instances for the node group. Set the minimum (min) equal to the maximum (max) for static capacity (for example, 5 min, 5 max). Set the minimum to 0 for fully dynamic scaling (for example, 0 min, 10 max). With Slurm 24.05 or later, you can set the minimum greater than 0 and less than the maximum for mixed capacity. This maintains a baseline number of instances and scales up as needed (for example, 2 min, 10 max).

1. Under **Network**, enter or choose these values:

   1. **Subnets** – Choose one or more subnets in the VPC where your AWS PCS cluster is deployed. If you choose multiple subnets, EFA communications won't be available between nodes, and communication between nodes in different subnets might have increased latency. If you use a launch template, make sure that the subnets you specify here match any subnets in the launch template. For On-Demand node groups with more than one subnet, the order in which you list the subnets sets the launch priority.

   1. **Security groups** – Choose one or more security groups in the VPC where your AWS PCS cluster is deployed. They must allow traffic between compute nodes and the cluster. For more information, see [Security group requirements and considerations](working-with_networking_sg.md#working-with_networking_sg-requirements).
      + **Standard configuration** – Required. Choose at least one security group.
      + **Launch template configuration** – Optional. If you choose security groups, AWS PCS uses only those security groups. It doesn't add the security groups in the launch template. If you don't choose any, AWS PCS uses the security groups in the launch template. If neither the compute node group nor the launch template specifies security groups, AWS PCS rejects the request. You can't choose security groups if your launch template defines network interfaces.

   1. **SSH key pair** – Optional. Choose an Amazon EC2 key pair for SSH connections to compute nodes.
      + **Standard configuration** – Choose a key pair, or choose not to use one. If you don't use a key pair, compute nodes don't have one.
      + **Launch template configuration** – If you choose a key pair, AWS PCS uses it instead of the key pair in the launch template. If you choose to use the key pair in the launch template, AWS PCS uses that key pair. If neither the compute node group nor the launch template specifies a key pair, compute nodes don't have one.

      For a summary of how AWS PCS chooses each setting, see [How AWS PCS chooses the AMI, security groups, and SSH key pair](#working-with_cng_create_instance-settings).

1. (Optional) Under **Additional settings**, specify the following:

   1. **Purchase option** – Choose On-Demand Instances, Spot Instances, an Interruptible Capacity Reservation, or an existing Capacity Block. Choose **On-Demand** if you plan to use an On-Demand Capacity Reservation (ODCR). For more information, see [Using ODCRs with AWS PCS](capacity-reservations-odcr.md). Choose **Interruptible Capacity Reservation** to use a shared interruptible ODCR (I-ODCR). For more information, see [Using I-ODCRs with AWS PCS](capacity-reservations-iodcr.md). Choose **Capacity Block** to use an existing Amazon EC2 Capacity Blocks for ML reservation. For more information, see [Using Amazon EC2 Capacity Blocks for ML with AWS PCS](capacity-blocks.md).

      To use an ODCR, an I-ODCR, or a Capacity Block, you must choose **Launch template configuration** and use a launch template that targets the reservation.

   1. **Allocation strategy** – If you chose the Spot purchase option, you can specify how AWS PCS chooses Spot capacity pools when it launches instances in the compute node group. For more information, see [Allocation strategies for Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.html) in the *Amazon Elastic Compute Cloud User Guide*. This option has no effect if you chose the On-Demand purchase option.

1. (Optional) In the **Scheduler configuration** section, you can specify the following:

   1. **Scale-down idle time** – The time in seconds before AWS PCS scales down an idle node in this compute node group. If you don't set it, AWS PCS uses the cluster-level value. This setting requires Slurm version 25.11 or later.

1. (Optional) In the **Slurm custom settings** section, you can add parameter name and value pairs to configure additional Slurm settings. For a complete list of supported parameters, see [Custom Slurm settings for AWS PCS compute node groups](slurm-custom-settings-cng.md).

1. (Optional) In the **Node lifecycle actions** section, you can add scripts that run at defined points in a compute node's lifecycle. Choose **Add script**. Choose the lifecycle stage, and specify the script location, a name, optional arguments, error handling behavior, and execution policy. To add more scripts, repeat these steps. Scripts run from top to bottom within a stage. To change the execution order, choose **Actions** for a script, and then choose **Move up** or **Move down**. For more information, see [Node lifecycle actions](cng-node-lifecycle-actions.md).

1. (Optional) Under **Tags**, add any tags to your compute node group.

1. Choose **Create compute node group**. The **Status** field shows `Creating` while AWS PCS provisions the compute node group. Provisioning can take several minutes.

**Recommended next step**
+ After the status is `ACTIVE`, add your compute node group to a queue so that it can run jobs. For more information, see [Creating a queue in AWS PCS](working-with_queues_create.md).

------
#### [ AWS CLI ]

**To create a compute node group (AWS CLI)**

The following command creates a compute node group without a custom launch template. It sets `--launch-template-mode` to `MANAGED`, which is the standard configuration in the console. You must specify `MANAGED` because the default mode is `CUSTOM`, which requires a custom launch template. To use a custom launch template, see the example that follows the procedure. Before you run the command, make the following replacements:

1. Replace {{region}} with the ID of the AWS Region where your cluster is, such as `us-east-1`.

1. Replace {{my-cluster}} with the name or `clusterId` of your cluster.

1. Replace {{my-node-group}} with the name for your compute node group. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and be 3–25 characters long. The name must be unique within the cluster.

1. Replace {{ami-ExampleID1}} with the ID of an AMI that is compatible with AWS PCS, such as the PCS-ready DLAMI. To get the ID of the current PCS-ready DLAMI, see [Find the current PCS-ready DLAMI](working-with_ami_pcs-ready-dlami.md#working-with_ami_pcs-ready-dlami_find). For other AMI options, see [Amazon Machine Images (AMIs) for AWS PCS](working-with_ami.md).

1. Replace {{subnet-ExampleID1}} with one or more subnet IDs from your cluster VPC. Separate multiple IDs with spaces. If you specify multiple subnets, EFA communications won't be available between nodes. For On-Demand node groups with more than one subnet, the order of the subnets sets the launch priority.

1. Replace {{sg-ExampleID1}} with one or more security group IDs from your cluster VPC. Separate multiple IDs with spaces. The security groups must allow traffic between compute nodes and the cluster. For more information, see [Security group requirements and considerations](working-with_networking_sg.md#working-with_networking_sg-requirements).

1. (Optional) Replace {{my-key-pair}} with the name of an Amazon EC2 key pair for SSH connections to compute nodes. If you omit `--ssh-key-name`, compute nodes don't have a key pair.

1. Replace {{arn:InstanceProfile}} with the ARN of your IAM instance profile. If you don't have one prepared, see [IAM instance profiles for AWS Parallel Computing Service](security-instance-profiles.md).

1. Replace {{min-instances}} and {{max-instances}} with integer values. Set the minimum (min) equal to the maximum (max) for static capacity (for example, 5 min, 5 max). Set the minimum to 0 for fully dynamic scaling (for example, 0 min, 10 max). With Slurm 24.05 or later, you can set the minimum greater than 0 and less than the maximum for mixed capacity. This maintains a baseline number of instances and scales up as needed (for example, 2 min, 10 max).

1. Replace {{t3.large}} with the instance type to use. To use more than one instance type, specify multiple `instanceType` settings separated by spaces, for example `--instance-configs instanceType=c6i.16xlarge instanceType=c6a.16xlarge`. All instance types must have the same processor architecture (x86\_64 or arm64) and number of vCPUs. If the instance types have GPUs, all instance types must have the same number of GPUs.

```
aws pcs create-compute-node-group --region {{region}} \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-name {{my-node-group}} \
    --launch-template-mode MANAGED \
    --ami-id {{ami-ExampleID1}} \
    --subnet-ids {{subnet-ExampleID1}} \
    --security-group-ids {{sg-ExampleID1}} \
    --ssh-key-name {{my-key-pair}} \
    --iam-instance-profile-arn {{arn:InstanceProfile}} \
    --scaling-configuration minInstanceCount={{min-instances}},maxInstanceCount={{max-instances}} \
    --instance-configs instanceType={{t3.large}}
```

**Example – Creating a compute node group with a custom launch template**  
Use a custom launch template if you need Amazon EC2 settings that aren't available as instance settings, such as network interfaces or capacity reservations. You don't need to specify `--launch-template-mode` because `CUSTOM` is the default. Replace {{lt-ExampleID1}} with the ID of your launch template, and {{launch-template-version}} with a specific version of it. AWS PCS associates your compute node group with that version of the launch template.  
If you don't have a launch template, see [Using Amazon EC2 launch templates with AWS PCS](working-with_launch-templates.md). Don't use a launch template named `pcs-{{identifier}}-do-not-delete`. AWS PCS creates launch templates with this name for its own use. For more information, see [Launch templates that AWS PCS creates](#working-with_cng_create_pcs-launch-templates).  

```
aws pcs create-compute-node-group --region {{region}} \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-name {{my-node-group}} \
    --subnet-ids {{subnet-ExampleID1}} \
    --custom-launch-template id={{lt-ExampleID1}},version='{{launch-template-version}}' \
    --iam-instance-profile-arn {{arn:InstanceProfile}} \
    --scaling-configuration minInstanceCount={{min-instances}},maxInstanceCount={{max-instances}} \
    --instance-configs instanceType={{t3.large}}
```
With a custom launch template, `--ami-id`, `--security-group-ids`, and `--ssh-key-name` are optional. For each option that you specify, AWS PCS uses your value instead of the value in the launch template. For each option that you omit, AWS PCS uses the value in the launch template. For example, suppose that you add `--security-group-ids {{sg-ExampleID2}}` to this command. Compute nodes use only {{sg-ExampleID2}}, not the security groups in the launch template. They still use the AMI and key pair in the launch template. If neither the command nor the launch template has an AMI or security groups, AWS PCS rejects the request. You can't specify `--security-group-ids` if your launch template defines network interfaces. For more information, see [How AWS PCS chooses the AMI, security groups, and SSH key pair](#working-with_cng_create_instance-settings).

**Example – Creating a compute node group with custom Slurm settings**  

```
aws pcs create-compute-node-group --region {{region}} \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-name {{my-node-group}} \
    --launch-template-mode MANAGED \
    --ami-id {{ami-ExampleID1}} \
    --subnet-ids {{subnet-ExampleID1}} \
    --security-group-ids {{sg-ExampleID1}} \
    --iam-instance-profile-arn {{arn:InstanceProfile}} \
    --scaling-configuration minInstanceCount={{min-instances}},maxInstanceCount={{max-instances}} \
    --instance-configs instanceType={{t3.large}} \
    --slurm-configuration \
    'slurmCustomSettings=[{parameterName=Features,parameterValue="{{gpu,nvme}}"}]'
```
For more information, see [Custom Slurm settings for AWS PCS compute node groups](slurm-custom-settings-cng.md).

**Example – Creating a compute node group with a scale-down idle time**  

```
aws pcs create-compute-node-group --region {{region}} \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-name {{my-gpu-nodes}} \
    --launch-template-mode MANAGED \
    --ami-id {{ami-ExampleID1}} \
    --subnet-ids {{subnet-ExampleID1}} \
    --security-group-ids {{sg-ExampleID1}} \
    --iam-instance-profile-arn {{arn:InstanceProfile}} \
    --scaling-configuration minInstanceCount={{0}},maxInstanceCount={{10}} \
    --instance-configs instanceType={{p4d.24xlarge}} \
    --slurm-configuration scaleDownIdleTimeInSeconds={{300}}
```
For nodes in this compute node group, AWS PCS uses this `scaleDownIdleTimeInSeconds` value instead of the cluster-level value. This setting requires Slurm version 25.11 or later.

You can add the following optional settings to the `create-compute-node-group` command.
+ Use `--purchase-option` to choose how AWS PCS purchases EC2 instances for your compute node group. On-Demand is the default. 
  +  `ONDEMAND` – Use On-Demand Instances. Also choose this option if you plan to use an On-Demand Capacity Reservation (ODCR). To use an ODCR, you need a custom launch template that targets it. For more information, see [Using ODCRs with AWS PCS](capacity-reservations-odcr.md). 
  +  `SPOT` – Use Spot Instances. If you choose Spot Instances, you can also use `--spot-options allocationStrategy={{strategy}}` to define how AWS PCS chooses Spot capacity pools when it launches instances in the node group. Valid values are `lowest-price`, `capacity-optimized`, and `price-capacity-optimized` (the default). For more information, see [Allocation strategies for Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.html) in the *Amazon Elastic Compute Cloud User Guide*.
  +  `CAPACITY_BLOCK` – Use an existing Amazon EC2 Capacity Blocks for ML reservation. You need a custom launch template that targets the Capacity Block. For more information, see [Using Amazon EC2 Capacity Blocks for ML with AWS PCS](capacity-blocks.md). 
  +  `INTERRUPTIBLE_CAPACITY_RESERVATION` – Use a shared interruptible ODCR (I-ODCR). You need a custom launch template that targets the I-ODCR. For more information, see [Using I-ODCRs with AWS PCS](capacity-reservations-iodcr.md). 
+ Use `--slurm-configuration` to set Slurm options for the nodes in the compute node group as custom Slurm settings. For example, set `Weight` to set scheduling priority. Nodes with lower weights have higher priority. Set `RealMemory` to set the memory on each node, for use with the `CR_CPU_Memory` option. For the parameters that AWS PCS supports, see [Custom Slurm settings for AWS PCS compute node groups](slurm-custom-settings-cng.md).
+ Use `--node-lifecycle-actions` to run custom scripts at defined points in a compute node's lifecycle, such as mounting file systems, installing software, or joining a directory service. For more information, see [Configure node lifecycle actions in AWS PCS](cng-node-lifecycle-actions-configure.md). For example commands, see [Node lifecycle action examples for AWS PCS](cng-node-lifecycle-actions-examples.md).
+ Use `--tags {{key1}}={{value1}},{{key2}}={{value2}}` to add tags to the compute node group.

It can take several minutes to create the compute node group. To check its status, run the following command. You can't add the compute node group to a queue until its status is `ACTIVE`. For more information, see [Creating a queue in AWS PCS](working-with_queues_create.md).

```
aws pcs get-compute-node-group --region {{region}} \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-identifier {{my-node-group}}
```

------