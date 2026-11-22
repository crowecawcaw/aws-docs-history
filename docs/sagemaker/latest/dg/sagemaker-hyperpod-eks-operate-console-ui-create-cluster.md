

# Creating a SageMaker HyperPod cluster with Amazon EKS orchestration

This tutorial shows how to create a new SageMaker HyperPod cluster with Amazon EKS orchestration in the SageMaker AI console.

**Note**  
The resources you create in this tutorial, such as the cluster instances, FSx for Lustre file system, and Amazon EBS volumes, might result in charges to your AWS account. For more information, see the [SageMaker AI pricing page](https://aws.amazon.com/sagemaker/pricing/).

**Topics**
+ [Create cluster](#smcluster-getting-started-eks-console-create-cluster-page)
+ [Configure cluster essentials](#smcluster-getting-started-eks-console-create-cluster-essentials)
+ [Optional settings](#smcluster-getting-started-eks-console-create-cluster-optional)
+ [Review and create](#smcluster-getting-started-eks-console-create-cluster-deploy)

## Create cluster
<a name="smcluster-getting-started-eks-console-create-cluster-page"></a>

To navigate to the **SageMaker HyperPod Clusters** page and choose Amazon EKS orchestration, follow these steps.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. Choose **HyperPod Clusters** in the left navigation pane and then **Cluster Management**.

1. On the **SageMaker HyperPod Clusters** page, choose **Create HyperPod cluster**. 

1. On the **Create HyperPod cluster** drop-down, choose **Orchestrated by Amazon EKS**.

The create cluster wizard opens with two configuration steps and a review page: **Configure cluster essentials**, **Optional settings**, and **Review and create**.

## Configure cluster essentials
<a name="smcluster-getting-started-eks-console-create-cluster-essentials"></a>

On the **Configure cluster essentials** step, set the core configuration for your HyperPod cluster with Amazon EKS orchestration.

### General settings
<a name="smcluster-getting-started-eks-console-create-cluster-essentials-general"></a>

Specify a name for the new cluster. The name is prefilled with a default that you can change. You can't change the name after the cluster is created.

### Networking
<a name="smcluster-getting-started-eks-console-create-cluster-essentials-network"></a>

Configure network settings within the cluster and for traffic in and out of the cluster. For orchestration of a SageMaker HyperPod cluster with Amazon EKS, HyperPod creates a new VPC for your cluster by default. You can instead use your own existing VPC.

The Networking section appears as a summary. To change it, choose **Edit**, and then choose **Save** or **Cancel**.

1. For **VPC**, HyperPod creates a new VPC for your cluster by default. To use your own existing VPC instead, select it. Your VPC must already give SageMaker AI access to it. To create a new VPC yourself, follow the instructions at [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html) in the *Amazon Virtual Private Cloud User Guide*.

1. For **VPC IPv4 CIDR block**, enter the starting IP of your VPC.

1. For **Availability Zones**, choose the Availability Zones (AZ) where HyperPod creates subnets for your cluster. Choose AZs that match the location of your accelerated compute capacity.

1. For **Security group(s)**, choose security groups that are either attached to the Amazon EKS cluster or whose inbound traffic is permitted by the security group associated with the Amazon EKS cluster. To create new security groups, go to the Amazon VPC console.

### Instance groups
<a name="smcluster-getting-started-eks-console-create-cluster-essentials-instance-groups"></a>

To add an instance group, choose **Add group**, which opens as a full page. You can configure each instance group differently and create a heterogeneous cluster that consists of multiple instance groups with various instance types. To deploy a cluster, you must add at least one instance group. Follow these steps to add an instance group.

1. For **Instance group type**, choose **Standard** or **Restricted Instance Group (RIG)**. Typically, you choose **Standard**, which provides a general purpose computing environment without additional security restrictions. **Restricted Instance Group (RIG)** is a specialized environment for foundational models customization such as Amazon Nova. For more information about setting up RIG for Amazon Nova model customization, see Amazon Nova customization on SageMaker HyperPod in the [Amazon Nova 1.0 user guide](https://docs.aws.amazon.com/nova/latest/userguide/nova-hp.html) or the [Amazon Nova 2.0 user guide](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-hp.html).

1. For **Name**, specify a name for the instance group.

1. For **Instance capacity**, choose **Flexible Training Plan** or **On-Demand or Reserved** to reserve your compute resources.

1. For **Instance type**, choose the instance for the instance group.
**Important**  
Ensure that you choose an instance type with sufficient quotas and enough unassigned IP addresses for your account. To view or request additional quotas, see [SageMaker HyperPod quotas](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas).

1. For **Instance quantity**, specify an integer not exceeding the instance quota for cluster usage.

1. For **Target Availability Zone**, choose the Availability Zone where your instances are provisioned. The Availability Zone should correspond to the location of your accelerated compute capacity.

1. For **Additional storage volume per instance (GB) - optional**, under **Advanced configuration**, specify an integer between 1 and 16384 to set the size of an additional Elastic Block Store (EBS) volume in gigabytes (GB). The default is 500 GB. The EBS volume is attached to each instance of the instance group. The default mount path for the additional EBS volume is `/opt/sagemaker`. After the cluster is created, you can SSH into the cluster instances (nodes) and verify that the EBS volume is mounted correctly by running the `df -h` command. Attaching an additional EBS volume provides stable, off-instance, and independently persisting storage, as described in the [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html) section in the *Amazon Elastic Block Store User Guide*.

1. If your instance type supports GPU partitioning with Multi-Instance GPU (MIG), you can enable GPU partition configuration for the instance group. GPU partitioning divides GPUs into smaller, isolated partitions to improve resource utilization. For more information, see [Using GPU partitions in Amazon SageMaker HyperPod](sagemaker-hyperpod-eks-gpu-partitioning.md).

   1. Toggle **Use GPU partition** to enable GPU partitioning for this instance group.

   1. Choose a **GPU partition profile** from the available options for your instance type. Each profile defines the GPU slice configuration and memory allocation.

1. Choose **Add instance group**.

### Storage
<a name="smcluster-getting-started-eks-console-create-cluster-essentials-storage"></a>

Configure the FSx for Lustre file system for your HyperPod cluster.

1. For **File system**, choose an existing FSx for Lustre file system, create a new one, or don't provision one.

1. For **Throughput per unit of storage**, choose the throughput that is available per TiB of provisioned storage.

1. For **Storage capacity**, review the capacity of the new file system. HyperPod creates the file system with 1,200 GiB (1.2 TiB) of storage. After you create the cluster, you can increase storage capacity and throughput from the Amazon FSx console. Total throughput grows with storage capacity. For more information, see [Increasing storage capacity](https://docs.aws.amazon.com/fsx/latest/LustreGuide/increase-storage-capacity.html) in the *Amazon FSx for Lustre User Guide*.

1. For **Data compression type**, choose **LZ4** to enable data compression.

1. For **Lustre version**, view the value that's recommended for the new file systems.

**Note**  
This step validates your account quotas. If a configured instance quantity might exceed a quota, a warning appears, and you must acknowledge it before you continue.

## Optional settings
<a name="smcluster-getting-started-eks-console-create-cluster-optional"></a>

Choose a workload profile to turn on a recommended set of add-ons, then adjust any section. Every setting stays editable.

### Workload profile
<a name="smcluster-getting-started-eks-console-create-cluster-optional-workload-profile"></a>

Choose a workload profile to turn on a recommended set of add-ons. The profiles are **All add-ons**, **Training**, **Inference**, and **No add-ons**. Each profile sets a recommended configuration for the autoscaler, operators, observability metrics, tiered storage, and task governance.

### Orchestration
<a name="smcluster-getting-started-eks-console-create-cluster-optional-orchestration"></a>

Follow these steps to create or choose an Amazon EKS cluster to use as an orchestrator.

1. For **EKS cluster**, choose whether to create a new Amazon EKS cluster or use an existing one.

   If you need to create a new Amazon EKS cluster, you can create it from the EKS cluster section without opening the Amazon EKS console.
**Note**  
The VPC subnet you choose for HyperPod must be private.  
After you submit a new EKS cluster creation request, wait until the EKS cluster becomes `Active`.

1. For **Kubernetes version**, choose a version from the drop-down menu. For more information about Kubernetes versions, see [Understand the Kubernetes version lifecycle on EKS](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html) from the *Amazon EKS User Guide*.

1. For **Operators**, choose **Use default Helm charts and add-ons** or **Don't install operators**. The option defaults to **Use default Helm charts and add-ons**, which installs operators on the EKS cluster. For more information about the default Helm charts and add-ons, see [`helm_chart`](https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart/HyperPodHelmChart) from the GitHub repository. For more information, see [Installing packages on the Amazon EKS cluster using Helm](sagemaker-hyperpod-eks-install-packages-using-helm-chart.md).

1. For **Enabled operators**, view the list of enabled operators. To edit the operators, clear the check box at the top and choose operators to enable for the EKS cluster.
**Note**  
To use HyperPod with EKS, you must install Helm charts and add-ons that enable operators on the EKS cluster. These components configure EKS as the control plane for HyperPod and set up workload management and orchestration.

### Permissions
<a name="smcluster-getting-started-eks-console-create-cluster-optional-permissions"></a>

Choose or create an IAM role that allows HyperPod to run and access the AWS resources it needs on your behalf. For more information, see [IAM role for SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod).

### HyperPod operators
<a name="smcluster-getting-started-eks-console-create-cluster-optional-hyperpod-operators"></a>

Install the HyperPod training operator and the HyperPod inference operator for training and inference workloads.

### Autoscaling
<a name="smcluster-getting-started-eks-console-create-cluster-optional-autoscaling"></a>

Turn on Karpenter node autoscaling. This option is available only when the cluster has at least one standard instance group.

### Resiliency
<a name="smcluster-getting-started-eks-console-create-cluster-optional-resiliency"></a>

For **Use automatic instance recovery**, choose whether SageMaker HyperPod recovers instances automatically. When automatic recovery is on, SageMaker HyperPod monitors instance health, and on failure labels the instance, attempts a reboot, and replaces the instance if needed. SageMaker HyperPod installs the health monitoring agent and deep health checks with every cluster.

### Observability
<a name="smcluster-getting-started-eks-console-create-cluster-optional-observability"></a>

Install the SageMaker HyperPod observability add-on for monitoring and workload metrics. This add-on requires an organization instance of IAM Identity Center in the Region. Without one, observability is off, but you can turn it on anyway.

### Additional Helm charts
<a name="smcluster-getting-started-eks-console-create-cluster-optional-helm-charts"></a>

Install optional additional Helm charts. No additional Helm charts are selected by default.

### Lifecycle scripts
<a name="smcluster-getting-started-eks-console-create-cluster-optional-lifecycle"></a>

You can use the default lifecycle scripts or custom lifecycle scripts stored in your Amazon S3 bucket. You can view the default lifecycle scripts in the [Awesome Distributed Training GitHub repository](https://github.com/aws-samples/awsome-distributed-training/tree/main/1.architectures/7.sagemaker-hyperpod-eks/LifecycleScripts). To learn more about the lifecycle scripts, see [Customizing SageMaker HyperPod clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md).

1. For **Lifecycle scripts**, choose default or custom lifecycle scripts.

1. For **S3 bucket for lifecycle scripts**, choose to create a new bucket or use an existing bucket to store the lifecycle scripts.

### Governance and access
<a name="smcluster-getting-started-eks-console-create-cluster-optional-governance"></a>

Enable task governance to set task priorities and allocate compute across teams.

### Tags - optional
<a name="smcluster-getting-started-eks-console-create-cluster-tags"></a>

For **Tags - *optional***, add key and value pairs to the new cluster and manage the cluster as an AWS resource. To learn more, see [Tagging your AWS resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html).

## Review and create
<a name="smcluster-getting-started-eks-console-create-cluster-deploy"></a>

On the **Review and create** step, review each section. To return to a section's step, choose **Edit** on that section. If validation finds errors, the console opens the step and section that contain them.

**Note**  
SageMaker HyperPod uses CloudFormation to provision the resources for your cluster.

Choose one of the following options to start resource provisioning and cluster creation.
+ **Create cluster** - SageMaker AI starts provisioning the resources and creates the cluster.
+ **Download CloudFormation template parameters** - You download the configuration parameter JSON file and run a AWS CLI command to deploy the CloudFormation stack that provisions the resources and creates the cluster. You can edit the downloaded parameter JSON file if needed. If you choose this option, see more instructions in [Creating SageMaker HyperPod clusters using CloudFormation templates](smcluster-getting-started-eks-console-create-cluster-cfn.md).