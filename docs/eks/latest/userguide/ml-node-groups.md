

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Manage compute for AI/ML workloads on Amazon EKS with node groups
<a name="ml-node-groups"></a>

**Tip**  
 [Register](https://events.eksworkshop.com/workshops/genai/) for upcoming Amazon EKS AI/ML workshops.

This section covers how to manage accelerated compute (AWS Trainium, NVIDIA GPUs) for AI training and inference workloads using Amazon EKS managed node groups or self-managed nodes.

EKS managed node groups and self-managed nodes use EC2 Auto Scaling Groups (ASG). EKS managed node groups have dedicated EKS APIs for creating, updating, and deleting nodes, and also have node repair functionality and lifecycle termination hooks built-in. EKS self-managed nodes are deployed and managed directly through EC2 APIs.

With these options, you define the instance type, desired count, scaling boundaries, and EC2 launch template upfront. Consider using EKS managed node groups or self-managed nodes if you also have non-EKS workloads and prefer configuration consistency through EC2 launch templates. EKS node groups are a fit for training and fine-tuning workloads where the accelerated compute footprint is known in advance. Note, both EKS Auto Mode and Karpenter also support static capacity provisioning, see [Manage compute for AI/ML workloads with EKS Auto Mode and Karpenter](ml-node-pools.md) for more information.

EKS managed node groups and self-managed nodes support all accelerated compute purchase options (On-Demand, Spot, On-Demand Capacity Reservations, Capacity Blocks for ML). You create a separate managed or self-managed node group per capacity type, each with its own launch template, instance types, and scaling configuration. This gives you explicit, ASG-backed control over each capacity pool without heterogeneous dynamic provisioning logic.

## EKS managed node groups vs. self-managed nodes
<a name="eks-ng-mng-vs-self-managed"></a>

Choosing between EKS managed node groups and self-managed nodes depends on the level of customization and control you require. EKS managed node groups allow for a subset of EC2 launch template customization, whereas self-managed nodes support the full breadth of the EC2 launch template. If you don’t have a specific reason to customize and manage the node lifecycle yourself, start with EKS managed node groups and only move to self-managed nodes when a specific requirement forces it.

 **Use managed node groups when:** You want EKS to handle AMI selection, node bootstrapping, rolling updates, node repair, and graceful drain workflows on your behalf. EKS managed node groups are the recommended starting point if you do not prefer to use EKS Auto Mode or Karpenter for training and inference workloads. When using Capacity Blocks for ML, EKS managed node groups automatically create a scheduled scaling policy that drains the node group 40 minutes before the reservation ends, removing the need to use the [AWS Node Termination Handler](https://github.com/aws/aws-node-termination-handler) or your own scale-down automation. Use EKS managed node groups when you’re using a supported EKS-optimized AMI, when you don’t need kernel-level or deep EC2 launch template customizations, and when you want a simpler node upgrade path for Kubernetes versions.

 **Use self-managed node groups when:** You need full control over the EC2 launch template, AMI, kernel parameters, container runtime configuration, or custom bootstrap scripts. Common ML scenarios include tuning kernel and NIC settings for distributed training with Elastic Fabric Adapter (EFA), or integrating with a custom node lifecycle controller. Self-managed nodes give you the flexibility to ship any user data and IAM instance profile you need, but you take on responsibility for updates, scheduled scaling policies, and lifecycle hooks such as the [AWS Node Termination Handler](https://github.com/aws/aws-node-termination-handler).

## Reserve GPUs with Capacity Blocks for ML
<a name="eks-ng-capacity-blocks-for-ml"></a>

Capacity Blocks for machine learning (ML) allow you to reserve GPU instances on a future date for time-bound training or inference workloads. For more information, see [Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html) in the Amazon EC2 User Guide.

You can use Capacity Block reservations through EKS managed node groups and self-managed nodes. The EC2 launch template configuration is the same in both cases. The node creation workflow, scale-down behavior, and lifecycle hooks for workload termination differ across the provisioning options.

## Considerations
<a name="eks-ng-capacity-block-considerations"></a>
+ Capacity Blocks are only available for certain Amazon EC2 instance types and AWS Regions. See [Work with Capacity Blocks Prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-using.html#capacity-blocks-prerequisites) for more information.
+ Capacity Blocks are zonal. During node group creation, you must use the subnet in the same Availability Zone (AZ) as the Capacity Block reservation.
+ If you create a node group before the Capacity Block reservation becomes active, set the desired capacity to `0` during node group creation.
+ To allow time for graceful workload draining, schedule scale-to-zero more than 30 minutes before the Capacity Block reservation ends. EC2 begins shutting down instances 30 minutes before the reservation ends.

## Create node groups with Capacity Blocks for ML
<a name="eks-ng-capacity-block-procedure"></a>

EKS managed node groups and self-managed nodes require using a custom EC2 launch template that targets the Capacity Block reservation. The following shows the minimal required fields for EKS managed node groups and self-managed nodes. Additional fields are required for self-managed nodes as shown in the Self-managed nodes steps below.

The `LaunchTemplateData` must include:
+  `InstanceMarketOptions` with `MarketType` set to `"capacity-block"` 
+  `CapacityReservationSpecification: CapacityReservationTarget` with `CapacityReservationId` set to the Capacity Block ID. For example, {{cr-0123456789abcdef0}}.
+  `InstanceType` set to the instance type of your Capacity Block reservation. For example, {{p5.48xlarge}}.

These requirements are shown in the examples below for creating the launch template for EKS managed node groups and self-managed nodes.

------
#### [ Managed node groups ]

1. Create a file named `eks-capacity-block-lt.json` with the following contents.

   Replace the contents for `CapacityReservationId` and `InstanceType` with the values for your Capacity Block. For more information on the additional EC2 launch template fields, see [Customize managed nodes with launch templates](launch-templates.md) and [Use Capacity Blocks for machine learning workloads](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-template-capacity-blocks.html).

   ```
   {
     "LaunchTemplateData": {
       "InstanceMarketOptions": {
         "MarketType": "capacity-block"
       },
       "CapacityReservationSpecification": {
         "CapacityReservationTarget": {
           "CapacityReservationId": {{"cr-0123456789abcdef0"}}
         }
       },
       "InstanceType": {{"p5.48xlarge"}}
     }
   }
   ```

1. Create the launch template.

   ```
   aws ec2 create-launch-template \
       --launch-template-name EKS-Capacity-Block-Launch-Template \
       --launch-template-data file://eks-capacity-block-lt.json
   ```

1. Use the launch template to create an EKS managed node group. Replace the placeholders in the command below with values applicable to your environment. The command below sets `--ami-type` to the AL2023 EKS-optimized NVIDIA AMIs. See [Use EKS-optimized accelerated AMIs for GPU instances](ml-eks-optimized-ami.md) for more information on the available EKS-optimized AMIs. If you are using a custom AMI with EKS managed node groups, specify your AMI ID in the launch template.

   When creating an EKS managed node group that uses Capacity Blocks, do the following:
   + Set `--capacity-type` to `"CAPACITY_BLOCK"`.
   + Only specify the subnet in the same Availability Zone as the capacity reservation.
   + If you specify a non-zero `desiredSize` before the reservation is active, the Auto Scaling Group reports launch errors until the reservation becomes active. Once active, instances launch and the ASG scales up to the requested `desiredSize`.

     ```
     aws eks create-nodegroup \
         --cluster-name {{my-eks-cluster}} \
         --nodegroup-name {{eks-cb-nodes}} \
         --node-role {{"arn:aws:iam::111122223333:role/myNodeRole"}} \
         --region {{region-code}} \
         --subnets {{subnet-ExampleID1}} \
         --ami-type {{"AL2023_x86_64_NVIDIA"}} \
         --scaling-config minSize=0,maxSize=2,desiredSize=0 \
         --capacity-type "CAPACITY_BLOCK" \
         --launch-template name="EKS-Capacity-Block-Launch-Template"
     ```

1. If you set `desiredSize` to `0` at create time, scale up the node group when the reservation becomes active using one of:
   + A scheduled scaling policy on the ASG aligned to the reservation start time. For more information, see [Scheduled scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html) in the *Amazon EC2 Auto Scaling User Guide*.
   + The Amazon EKS console or `aws eks update-nodegroup-config` to update the scaling config.

1. Verify nodes join the cluster after scale-up.

1. EKS automatically creates a scheduled scaling policy named **Amazon EKS Node Group Capacity Scaledown Before Reservation End** to scale the node group down to `0` 40 minutes before the reservation ends. This gives Pods time to be gracefully drained before EC2 begins terminating instances at the 30-minute mark. Don’t edit or delete this scheduled action.

------
#### [ Self-managed nodes ]

1. Create a file named `eks-capacity-block-lt.json` with the following contents.

   Replace the contents for `CapacityReservationId` and `InstanceType` with the values for your Capacity Block. For more information on the additional EC2 launch template fields, see [Customize managed nodes with launch templates](launch-templates.md) and [Use Capacity Blocks for machine learning workloads](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-template-capacity-blocks.html).

   Replace the contents for `IamInstanceProfile`, `ImageId`, `SecurityGroupIds`, `UserData`, `KeyName` with the values for your environment.

   ```
   {
     "LaunchTemplateData": {
       "InstanceMarketOptions": {
         "MarketType": "capacity-block"
       },
       "CapacityReservationSpecification": {
         "CapacityReservationTarget": {
           "CapacityReservationId": {{"cr-0123456789abcdef0"}}
         }
       },
       "IamInstanceProfile": {
         "Arn": {{"arn:aws:iam::111122223333:role/myNodeRole"}}
       },
       "ImageId": {{"image-id"}},
       "InstanceType": {{"p5.48xlarge"}},
       "KeyName": {{"key-name"}},
       "SecurityGroupIds": "sg-05b1d815d1EXAMPLE"
       ],
       "UserData": {{"user-data"}}
     }
   }
   ```

1. Create the launch template.

   ```
   aws ec2 create-launch-template \
       --launch-template-name EKS-Capacity-Block-Launch-Template \
       --launch-template-data file://eks-capacity-block-lt.json
   ```

1. Use the launch template to create the Auto Scaling Group following the steps in [Create self-managed Amazon Linux nodes](launch-workers.md). If the reservation isn’t active yet, set `DesiredCapacity` to `0`. Only specify the subnet in the Availability Zone where the capacity is reserved.

1. After your self-managed nodes are created with `DesiredCapacity` set to `0`, create a scheduled scaling policy on the Auto Scaling group aligned to the Capacity Block reservation times. For more information, see [Scheduled scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html).

   You can use the reserved instances until 30 minutes before the reservation end time. Schedule scale-to-zero more than 30 minutes before the end time so Pods have time to drain.

   If you prefer to scale manually, update the ASG’s desired capacity at the reservation start time and again more than 30 minutes before the end time.

1. To gracefully drain Pods, set up the AWS Node Termination Handler. It watches for ASG scale-in lifecycle events from Amazon EC2 Auto Scaling using EventBridge and lets the Kubernetes control plane act before the instance becomes unavailable. Without it, Pods and Kubernetes objects can get stuck in a pending state. For more information, see [AWS Node Termination Handler](https://github.com/aws/aws-node-termination-handler) on GitHub.

   If you don’t set up the Node Termination Handler, manually drain Pods before the 30-minute window so they have time to be gracefully drained.

------