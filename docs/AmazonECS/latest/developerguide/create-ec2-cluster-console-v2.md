# Creating an Amazon ECS cluster for Amazon EC2 workloads

You create a cluster to define the infrastructure your tasks and services run on.

Before you begin, be sure that you've completed the steps in [Set up to use Amazon ECS](get-set-up-for-amazon-ecs.md "get-set-up-for-amazon-ecs.md") and
assign the appropriate IAM permission. For more information, see [Amazon ECS cluster examples](security_iam_id-based-policy-examples.md#IAM_cluster_policies "security_iam_id-based-policy-examples.md#IAM_cluster_policies"). The Amazon ECS console provides a simple way to create the
resources that are needed by an Amazon ECS cluster by creating a CloudFormation stack.

To make the cluster creation process as easy as possible, the console has default
selections for many choices which we describe below. There are also help panels available
for most of the sections in the console which provide further context.

You can register Amazon EC2 instances when you create the cluster or register additional
instances with the cluster after it has been created.

You can modify the following default options:

- Change the subnets where your instances launch.
- Change the security groups used to control traffic to the container
  instances.
- Add a namespace to the cluster.

A namespace allows services that you create in the cluster can connect to the
other services in the namespace without additional configuration. For more
information, see [Interconnect Amazon ECS services](interconnecting-services.md "interconnecting-services.md").

- Enable task events to receive EventBridge notifications for task state changes.
- Assign a AWS KMS key for your managed storage. For information about how to create a
  key, see [Create a KMS key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
  _AWS Key Management Service User Guide_.
- Assign a AWS KMS key for your Fargate ephemeral storage. For information about how
  to create a key, see [Create a KMS key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
  _AWS Key Management Service User Guide_.
- Configure the AWS KMS key and logging for ECS Exec.
- Add tags to help you identify your cluster.

## Amazon EC2 Auto Scaling group options

When you use Amazon EC2 instances, you must specify an Amazon EC2 Auto Scaling group to manage the infrastructure
that your tasks and services run on.

When you choose to create a new Amazon EC2 Auto Scaling group, it is automatically configured for the
following behavior:

- Amazon ECS manages the scale-in and scale-out actions of the Amazon EC2 Auto Scaling group.
- Amazon ECS will not prevent Amazon EC2 instances that contain tasks and that are in an Amazon EC2 Auto Scaling
  group from being terminated during a scale-in action. For more information, see
  [Instance Protection](../../../autoscaling/ec2/userguide/as-instance-termination.md#instance-protection "../../../autoscaling/ec2/userguide/as-instance-termination.md#instance-protection") in the
  _AWS Auto Scaling User Guide_.
  You configure the following Amazon EC2 Auto Scaling group properties which determine the type and number of
  instances to launch for the group:

- The Amazon ECS-optimized AMI.
- The instance type.
- The SSH key pair that proves your identity when you connect to the instance. For
  information about how to create SSH keys, see [Amazon EC2 key pairs and Linux
  instances](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") in the _Amazon EC2 User Guide_.
- The minimum number of instances to launch for the Amazon EC2 Auto Scaling group.
- The maximum number of instances that are started for the Amazon EC2 Auto Scaling group.

In order for the group to scale out, the maximum must be greater than 0.
Amazon ECS creates an Amazon EC2 Amazon EC2 Auto Scaling launch template and Amazon EC2 Auto Scaling group on your behalf as part of the CloudFormation
stack. The values that you specified for the AMI, the instance types, and the SSH key pair
are part of the launch template. The templates are prefixed with
`EC2ContainerService-<`ClusterName`>`, which
makes them easy to identify. The Amazon EC2 Auto Scaling groups are prefixed with
`<`ClusterName`>-ECS-Infra-ECSAutoScalingGroup`.

Instances launched for the Amazon EC2 Auto Scaling group use the launch template.

## Networking options

By default instances are launched into the default subnets for the
Region. The security groups, which control the traffic to your container
instances, currently associated with the subnets are used. You can changed the subnets
and security groups for the instances.

You can choose an existing subnet. You can either use an existing security group, or
create a new one. To create tasks in an IPv6-only configuration, use subnets that
include only an IPv6 CIDR block.

When you create a new security group, you need to specify at least one inbound rule.

The inbound rules determine what traffic can reach your container instances and
include the following properties:

- The protocol to allow
- The range of ports to allow
- The inbound traffic (source)

To allow inbound traffic from a specific address or CIDR block, use
**Custom** for **Source** with the allowed CIDR.

To allow inbound traffic from all destinations, use **Anywhere** for
**Source**. This automatically adds the 0.0.0.0/0 IPv4 CIDR block
and ::/0 IPv6 CIDR block.

To allow inbound traffic from your local computer, use **Source
group** for **Source**. This automatically adds the
current IP address of your local computer as the allowed source.

###### To create a new cluster (Amazon ECS console)

Before you begin, assign the appropriate IAM permission. For more information, see
[Amazon ECS cluster examples](security_iam_id-based-policy-examples.md#IAM_cluster_policies "security_iam_id-based-policy-examples.md#IAM_cluster_policies").

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. From the navigation bar, select the Region to use.
3. In the navigation pane, choose **Clusters**.
4. On the **Clusters** page, choose **Create
   cluster**.
5. Under **Cluster configuration**, configure the following:
   - For **Cluster name**, enter a unique name.

   The name can contain up to 255 letters (uppercase and lowercase), numbers,
   and hyphens.
   - (Optional) To have the namespace used for Service Connect be different
     from the cluster name, under **Service Connect defaults**, for **Default namespace**, choose or enter a namespace
     name. To use a shared namespace, choose or enter a namespace ARN. For more information about using shared namespaces, see [Amazon ECS Service Connect with shared
     AWS Cloud Map namespaces](service-connect-shared-namespaces.md "service-connect-shared-namespaces.md").

6. Add Amazon EC2 instances to your cluster, expand **Infrastructure**
   and then select **Fargate and Self-managed instances**.

Next, configure the Amazon EC2 Auto Scaling group which acts as the capacity provider:

    1. To using an existing Amazon EC2 Auto Scaling group, from **Auto Scaling group
     (ASG)**, select the group.
    2. To create a Amazon EC2 Auto Scaling group, from **Auto Scaling group
     (ASG)**, select **Create new group**, and then
     provide the following details about the group:




    	* For **Provisioning model**, choose whether to use
    	 **On-demand** instances or
    	 **Spot** Instances.
    	* If you choose to use Spot Instances, for **Allocation
    	 Strategy**, choose what Spot capacity pools (instance
    	 types and Availability Zones) are used for the instances.


    	For most workloads, you can choose **Price capacity
    	 optimized**.


    	For more information, see [Allocation strategies for Spot Instances](../../../AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.md "../../../AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.md") in the *Amazon EC2 User Guide*.
    	* For **Container instance Amazon Machine Image
    	 (AMI)**, choose the Amazon ECS-optimized AMI for the Amazon EC2 Auto Scaling
    	 group instances.
    	* For **EC2 instance type**, choose the instance
    	 type for your workloads.


    	 Managed scaling works best if your Amazon EC2 Auto Scaling group uses the same or
    	 similar instance types.
    	* For **EC2 instance role**, choose an existing
    	 container instance role, or you can create a new one.


    	For more information, see [Amazon ECS container instance IAM role](instance_IAM_role.md "instance_IAM_role.md").
    	* For **Capacity**, enter the minimum number and
    	 the maximum number of instances to launch in the Amazon EC2 Auto Scaling group.
    	* For **SSH key pair**, choose the pair that proves
    	 your identity when you connect to the instance.
    	* To allow for larger image and storage, for **Root EBS
    	 volume size**, enter the value in GiB.

7. (Optional) To change the VPC and subnets, under **Networking for Amazon EC2
   instances**, perform any of the following operations:
   - To remove a subnet, under **Subnets**, choose
     **X** for each subnet that you want to remove.
   - To change to a VPC other than the **default** VPC, under
     **VPC**, choose an existing **VPC**,
     and then under **Subnets**, choose the subnets. For an
     IPv6-only configuration, choose a VPC that has an IPv6 CIDR block and
     subnets that have only an IPv6 CIDR block.
   - Choose the security groups. Under **Security group**,
     choose one of the following options:
     - To use an existing security group, choose **Use an
       existing security group**, and then choose the security
       group.
     - To create a security group, choose **Create a new security
       group**. Then, choose **Add rule** for
       each inbound rule.

     For information about inbound rules, see [Networking options](#networking-options "#networking-options").

   - To automatically assign public IP addresses to your Amazon EC2 container
     instances, for **Auto-assign public IP**, choose one of the
     following options:
     - **Use subnet setting** – Assign a public IP
       address to the instances when the subnet that the instances launch
       in are a public subnet.
     - **Turn on** – Assign a public IP address to
       the instances.

8. (Optional) Use Container Insights, expand **Monitoring**, and then choose one
   of the following options:
   - To use the recommended Container Insights with enhanced observability, choose
     **Container Insights with enhanced observability**.
   - To use Container Insights, choose **Container Insights**.

9. (Optional) To enable task events, expand **Task events**, and then turn on **Enable task events**.

When you enable task events, Amazon ECS sends task state change events to EventBridge. This allows you to monitor and respond to task lifecycle changes automatically. 10. (Optional) To use ECS Exec to debug tasks in the cluster, expand **Troubleshooting configuration**, and then configure the following:

    * (Optional) For **AWS KMS key for ECS Exec**, enter the ARN of the AWS KMS key you want to use to encrypt the ECS Exec session data.
    * (Optional) For **ECS Exec logging**, choose the log destination:




    	+ To send logs to CloudWatch Logs, choose **Amazon CloudWatch**.
    	+ To send logs to Amazon S3, choose **Amazon S3**.
    	+ To disable logging, choose **None**.

11. (Optional)

If you use Runtime Monitoring with the manual option and you want to have this cluster
monitored by GuardDuty, choose **Add tag** and do the following:

    * For **Key**, enter
     `guardDutyRuntimeMonitoringManaged`
    * For **Value**, enter `true`.

12. (Optional) Encrypt the data on managed storage. Under
    **Encryption**, for **Managed storage**, enter
    the ARN of the AWS KMS key you want to use to encrypt the managed storage
    data.
13. (Optional) To manage the cluster tags, expand **Tags**, and then
    perform one of the following operations:

[Add a tag] Choose **Add tag** and do the following:

    * For **Key**, enter the key name.
    * For **Value**, enter the key value.

[Remove a tag] Choose **Remove** to the right of the tag’s Key
and Value. 14. Choose **Create**.

## Next steps

After you create the cluster, you can create task definitions for your applications and
then run them as standalone tasks, or as part of a service. For more information, see the
following:

- [Amazon ECS task definitions](task_definitions.md "task_definitions.md")
- [Running an application as an Amazon ECS task](standalone-task-create.md "standalone-task-create.md")
- [Creating an Amazon ECS rolling update
  deployment](create-service-console-v2.md "create-service-console-v2.md")
