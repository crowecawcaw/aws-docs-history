# Tutorial: Create a managed compute

environment using Amazon EKS resources

Complete the following steps to create a managed compute environment using Amazon Elastic Kubernetes Service
(Amazon EKS) resources.

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. From the navigation bar, select the AWS Region to use.
3. In the navigation pane, choose **Compute environments**.
4. Choose **Create**.
5. For **Compute environment configuration**, choose **Amazon Elastic Kubernetes Service
   (Amazon EKS)**.
6. For **Name**, specify a unique name for your compute environment. The
   name can be up to 128 characters in length. It can contain uppercase and lowercase
   letters, numbers, hyphens (-), and underscores (\_).
7. For **Instance role**, choose an existing instance profile that has
   the required IAM permissions attached.

###### Note

To create a compute environment in the AWS Batch console, choose an instance profile
that has the `eks:ListClusters` and `eks:DescribeCluster`
permissions. 8. For **EKS cluster**, choose an existing Amazon EKS cluster. 9. For **Namespace**, enter a Kubernetes namespace to group your AWS Batch
processes in the cluster. 10. (Optional) Expand **Tags**. Choose **Add tag** and
then enter a key-value pair. 11. Choose **Next page**. 12. (Optional) For **Use EC2 Spot Instances**, turn on **Enable
using Spot instances** to use Amazon EC2 Spot Instances. 13. (Spot only) For **Maximum % on-demand price**, choose the maximum
percentage that a Spot Instance price can be when compared with the On-Demand price for
that instance type before instances are launched. For example, if your maximum price is
20%, then the Spot price must be less than 20% of the current On-Demand price for that EC2
instance. You always pay the lowest (market) price and never more than your maximum
percentage. If you leave this field empty, the default value is 100% of the On-Demand
price. 14. (Spot only) For **Spot fleet role**, choose the Amazon EC2 Spot fleet
IAM role for the `SPOT` compute environment.

###### Important

This role is required if the allocation strategy is set to `BEST_FIT` or
not specified. 15. (Optional) For **Minimum vCPUs**, choose the minimum number of vCPUs
that your compute environment maintains, regardless of job queue demand. 16. (Optional) For **Maximum vCPUs**, choose the maximum number of vCPUs
that your compute environment can scale out to, regardless of job queue demand. 17. For **Allowed instance types**, choose the Amazon EC2 instance types
that can be launched. You can specify instance families to launch any instance type
within those families (for example, `c5`, `c5n`, or
`p3`). Or, you can specify specific sizes within a family (such as
`c5.8xlarge`). Metal instance types aren't in the instance families. For
example, `c5` doesn't include `c5.metal`.

AWS Batch can select the instance type for you if you choose one of the following:

    * `optimal` to select instance types (from the `c4`, `m4`,
     `r4`, `c5`, `m5`, and `r5`
     instance families) that match the demand of your job queues.
    * `default_x86_64` to choose x86 based instance types (from the m6i,
     c6i, r6i, and c7i instance families) that
     matches the resource demands of the job queue.
    * `default_arm64` to choose x86 based instance types (from the m6g,
     c6g, r6g, and c7g instance families) that
     matches the resource demands of the job queue.

###### Note

Starting on 11/01/2025 the behavior of `optimal` is going to be changed to
match `default_x86_64`. During the change your instance families could be
updated to a newer generation. You do not need to perform any actions for the upgrade to
happen. For more information about change, see [Optimal instance type configuration to
receive automatic instance family updates](optimal-default-instance-troubleshooting.md "optimal-default-instance-troubleshooting.md").

###### Note

    * Instance family availability varies by AWS Region. For example, some AWS Regions may not
     have any fourth generation instance families but have fifth and sixth generation
     instance families.
    * When using `default_x86_64` or `default_arm64` instance
     bundles, AWS Batch selects instance families based on a balance of cost-effectiveness
     and performance. While newer generation instances often provide better
     price-performance, AWS Batch may choose an earlier generation instance family if it
     provides the optimal combination of availability, cost, and performance for your
     workload. For example, in an AWS Region where both c6i and c7i instances are
     available, AWS Batch might select c6i instances if they offer better
     cost-effectiveness for your specific job requirements. For more information on
     AWS Batch instance types and AWS Region availability, see [Instance type compute table](instance-type-compute-table.md#instance-type-compute-table.title "instance-type-compute-table.md#instance-type-compute-table.title").
    * AWS Batch periodically updates your instances in default bundles to newer, more cost-effective
     options. Updates happen automatically without requiring any action from you. Your
     workloads continue running during updates with no interruption

###### Note

When you create a compute environment, the instance types that you select for the compute environment must share
the same architecture. For example, you can't mix x86 and ARM instances in the same compute environment.

###### Note

AWS Batch will scale GPUs based on the required amount in your job queues. To use
GPU scheduling, the compute environment must include instance types from the
`p3`, `p4`, `p5`, `p6`, `g3`, `g3s`,
`g4`, `g5`, or `g6` families. 18. (Optional) Expand **Additional configuration**.

    1. (Optional) For **Placement group**, enter a placement group name
     to group resources in the compute environment.
    2. For **Allocation strategy**, choose
     **BEST\_FIT\_PROGRESSIVE**.
    3. (Optional) For **Amazon Machine Images (AMIs) Configuration**,
     choose **Add amazon machine images (amis) configuration**.


    You can use either an Amazon EKS-optimized Amazon Linux AMI or a custom AMI.


    	1. To use an [Amazon EKS-optimized Amazon Linux
    	 AMI](../../../eks/latest/userguide/eks-optimized-ami.md "../../../eks/latest/userguide/eks-optimized-ami.md"):


    		1. For **Image type** choose one of the following:




    			* [Amazon Linux
    			 2](../../../eks/latest/userguide/eks-optimized-ami.md "../../../eks/latest/userguide/eks-optimized-ami.md"): Default for all AWS Graviton-based instance families (for
    			 example, `C6g`, `M6g`, `R6g`, and
    			 `T4g`) and can be used for all non-GPU instance types.
    			* [Amazon Linux 2
    			 (accelerated)](../../../eks/latest/userguide/eks-optimized-ami.md "../../../eks/latest/userguide/eks-optimized-ami.md"): Default for all GPU instance families (for example, `P4`
    			 and `G4`) and can be used for all non AWS Graviton-based
    			 instance types.
    			* [Amazon Linux
    			 2023](../../../eks/latest/userguide/eks-optimized-ami.md "../../../eks/latest/userguide/eks-optimized-ami.md"): AWS Batch supports Amazon Linux 2023 (AL2023).
    			* [Amazon Linux 2023
    			 (accelerated)](../../../eks/latest/userguide/eks-optimized-ami.md "../../../eks/latest/userguide/eks-optimized-ami.md"): GPU instance families and can be used for all non AWS
    			 Graviton-based instance types.
    		2. For **Kubernetes version** enter in a [Kubernetes version
    		 number](supported_kubernetes_version.md#supported_kubernetes_version.title "supported_kubernetes_version.md#supported_kubernetes_version.title").
    	2. To use a custom AMI:


    		1. For **Image type** choose the AMI type that the custom AMI is based off
    		 of:




    			* [Amazon Linux
    			 2](../../../eks/latest/userguide/eks-optimized-ami.md "../../../eks/latest/userguide/eks-optimized-ami.md"): Default for all AWS Graviton-based instance families (for
    			 example, `C6g`, `M6g`, `R6g`, and
    			 `T4g`) and can be used for all non-GPU instance
    			 types.
    			* [Amazon Linux 2
    			 (accelerated)](../../../eks/latest/userguide/eks-optimized-ami.md "../../../eks/latest/userguide/eks-optimized-ami.md"): Default for all GPU instance families (for example, `P4`
    			 and `G4`) and can be used for all non AWS Graviton-based
    			 instance types.
    			* [Amazon Linux
    			 2023](../../../eks/latest/userguide/eks-optimized-ami.md "../../../eks/latest/userguide/eks-optimized-ami.md"): AWS Batch supports AL2023.
    			* [Amazon Linux 2023
    			 (accelerated)](../../../eks/latest/userguide/eks-optimized-ami.md "../../../eks/latest/userguide/eks-optimized-ami.md"): GPU instance families and can be used for all non AWS
    			 Graviton-based instance types.
    		2. For **Image ID override** enter the custom AMI ID.
    		3. For **Kubernetes version** enter in a [Kubernetes version
    		 number](supported_kubernetes_version.md#supported_kubernetes_version.title "supported_kubernetes_version.md#supported_kubernetes_version.title").
    4. (Optional) For **Launch template**, choose an existing [launch template](eks-launch-templates.md#eks-launch-templates.title "eks-launch-templates.md#eks-launch-templates.title").
    5. (Optional) For **Launch template version**, enter
     `$Default`, `$Latest`, or a version
     number.
    6. (Optional) For **Override launch template**, to add an override
     choose **Add override Launch template**:


    	1. (Optional) For **Launch template** choose the launch template
    	 to add the override to.
    	2. (Optional) For **Launch template version** choose the version
    	 number of the launch template, `$Default`, or
    	 `$Latest`.
    	3. (Optional) For **Target instances types** choose the instance
    	 type or family that this override should be applied to. This can target only
    	 instance types and families that are included in **Allowed instance
    	 types**.
    	4. (Optional) For **userdataType** choose the EKS node
    	 initialization. Only use this field if you have an AMI specified in either the
    	 Launch Template or as a Launch Template Override. Choose
    	 **EKS\_NODEADM** for custom AMIs based on
    	 `EKS_AL2023` or `EKS_AL2023_NVIDIA` or
    	 **EKS\_BOOSTRAP\_SH** for `EKS_AL2` and
    	 `EKS_AL_NVIDIA`. The default value is
    	 **EKS\_BOOSTRAP\_SH**.


    	You would use **userdataType** when you have a [mixed
    	 environment](mixed-ami-environments.md#mixed-ami-environments.title "mixed-ami-environments.md#mixed-ami-environments.title") where you're using both AL2 and AL2023-based custom AMIs in the same
    	 compute environment.

19. Choose **Next page**.
20. For **Virtual Private Cloud (VPC) ID**, choose a VPC where to launch
    the instances.
21. For **Subnets**, choose the subnets to use. By default, all subnets
    within the selected VPC are available.

###### Note

AWS Batch on Amazon EKS supports Local Zones. For more information, see [Amazon EKS and AWS Local
Zones](../../../eks/latest/userguide/local-zones.md "../../../eks/latest/userguide/local-zones.md") in the _Amazon EKS User Guide_. 22. (Optional) For **Security groups**, choose a security group to attach
to your instances. By default, the default security group for your VPC is selected. 23. Choose **Next page**. 24. For **Review**, review the configuration steps. If you
need to make changes, choose **Edit**. When you're finished,
choose **Create compute environment**.
