# Creating

a SageMaker HyperPod cluster with Amazon EKS orchestration

The following tutorial demonstrates how to create a new SageMaker HyperPod cluster and
set it up with Amazon EKS orchestration through the SageMaker AI console UI.

###### In this topic:

- [Create cluster](#smcluster-getting-started-eks-console-create-cluster-page "#smcluster-getting-started-eks-console-create-cluster-page")
- [Deploy resources](#smcluster-getting-started-eks-console-create-cluster-deploy "#smcluster-getting-started-eks-console-create-cluster-deploy")

## Create cluster

To navigate to the **SageMaker HyperPod Clusters** page and choose
Amazon EKS orchestration, follow these steps.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Choose **HyperPod Clusters** in the left
   navigation pane and then **Cluster Management**.
3. On the **SageMaker HyperPod Clusters** page, choose
   **Create HyperPod cluster**.
4. On the **Create HyperPod cluster**
   drop-down, choose **Orchestrated by Amazon EKS**.
5. On the EKS cluster creation page, you will see two options, choose the
   option that best fits your needs.
   1. **Quick setup** - To get started immediately
      with default settings, choose **Quick setup**.
      With this option, SageMaker AI will create new resources such as VPC,
      subnets, security groups, Amazon S3 bucket, IAM role, and
      FSx for Lustre in the process of creating your cluster.
   2. **Custom setup** - To integrate with existing
      AWS resources or have specific networking, security, or
      storage requirements, choose **Custom setup**.
      With this option, you can choose to use the existing resources
      or create new ones, and you can customize the configuration that
      best fits your needs.

On the **Quick setup** section, follow these steps to
create your HyperPod cluster with Amazon EKS orchestration.

### General settings

Specify a name for the new cluster. You can’t change the name after
the cluster is created.

### Instance groups

To add an instance group, choose **Add group**. Each
instance group can be configured differently, and you can create a
heterogeneous cluster that consists of multiple instance groups with
various instance types. To deploy a cluster, you must add at least one
instance group. Follow these steps to add an instance group.

1. For **Instance group type**, choose
   **Standard** or **Restricted
   Instance Group (RIG)**. Typically, you will choose
   **Standard**, which provides a general
   purpose computing environment without additional security
   restrictions. **Restricted Instance Group
   (RIG)** is a specialized environment for
   foundational models customization such as Amazon Nova. For more
   information about setting up RIG for Amazon Nova model customization,
   see [Amazon Nova customization on Amazon SageMaker HyperPod](nova-hp.md "nova-hp.md").
2. For **Name**, specify a name for the instance
   group.
3. For **Instance capacity**, choose either
   on-demand capacity or a training plan to reserve your compute
   resources.
4. For **Instance type**, choose the instance
   for the instance group.

###### Important

Ensure that you choose an instance type with sufficient
quotas and enough unassigned IP addresses for your account.
To view or request additional quotas, see [SageMaker HyperPod quotas](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas"). 5. For **Instance quantity**, specify an integer
not exceeding the instance quota for cluster usage. For this
tutorial, enter **1** for all three
groups. 6. For **Target Availability Zone**, choose the
Availability Zone where your instances will be provisioned. The
Availability Zone should correspond to the location of your
accelerated compute capacity. 7. For **Additional storage volume per instance (GB) -
optional**, specify an integer between 1 and 16384
to set the size of an additional Elastic Block Store (EBS)
volume in gigabytes (GB). The EBS volume is attached to each
instance of the instance group. The default mount path for the
additional EBS volume is `/opt/sagemaker`. After the
cluster is successfully created, you can SSH into the cluster
instances (nodes) and verify if the EBS volume is mounted
correctly by running the `df -h` command. Attaching
an additional EBS volume provides stable, off-instance, and
independently persisting storage, as described in the [Amazon EBS volumes](../../../ebs/latest/userguide/ebs-volumes.md "../../../ebs/latest/userguide/ebs-volumes.md") section in the _Amazon Elastic Block Store
User Guide_. 8. For **Instance deep health checks**, choose
your option. Deep health checks monitor instance health during
creation and after software updates, automatically recovering
faulty instances through reboots or replacements when
enabled. 9. If your instance type supports GPU partitioning with Multi-Instance GPU
(MIG), you can enable GPU partition configuration for the instance group.
GPU partitioning allows you to divide GPUs into smaller, isolated partitions
for improved resource utilization. For more information, see [Using GPU partitions in Amazon SageMaker HyperPod](sagemaker-hyperpod-eks-gpu-partitioning.md "sagemaker-hyperpod-eks-gpu-partitioning.md").

    1. Toggle **Use GPU partition** to enable
     GPU partitioning for this instance group.
    2. Select a **GPU partition profile** from
     the available options for your instance type. Each profile
     defines the GPU slice configuration and memory allocation.

10. Choose **Add instance group**.

### Quick setup defaults

This section lists all the default settings for your cluster creation,
including all the new AWS resources that will be created during the
cluster creation process. Review the default settings.

On the **Custom setup** section, follow these steps to
create your first HyperPod cluster with Amazon EKS orchestration.

### General settings

Specify a name for the new cluster. You can’t change the name after
the cluster is created.

For **Instance recovery**, choose \*\*Automatic

- \*recommended**\* or
  **None\*\*.

### Networking

Configure network settings within the cluster and in-and-out of the
cluster. For orchestration of SageMaker HyperPod cluster with Amazon EKS, the VPC
is automatically set to the one configured with the EKS cluster you
selected.

1. For **VPC**, choose your own VPC if you
   already have one that gives SageMaker AI access to your VPC. To create a
   new VPC, follow the instructions at [Create a
   VPC](../../../vpc/latest/userguide/create-vpc.md "../../../vpc/latest/userguide/create-vpc.md") in the _Amazon Virtual Private Cloud User
   Guide_. You can leave it as **None**
   to use the default SageMaker AI VPC.
2. For **VPC IPv4 CIDR block**, enter the
   starting IP of your VPC.
3. For **Availability Zones**, choose the
   Availability Zones (AZ) where HyperPod will create
   subnets for your cluster. Choose AZs that match the location of
   your accelerated compute capacity.
4. For **Security group(s)**, choose security
   groups that are either attached to the Amazon EKS cluster or whose
   inbound traffic is permitted by the security group associated
   with the Amazon EKS cluster. To create new security groups, go to the
   Amazon VPC console.

### Orchestration

Follow these steps to create or select an Amazon EKS cluster to use as an
orchestrator.

1. For **EKS cluster**, choose either create a
   new Amazon EKS cluster or use an existing one.

If you need to create a new EKS cluster, you can create it
from the EKS cluster section without having to open the Amazon EKS
console.

###### Note

The VPC subnet you choose for HyperPod has to be
private.

After submitting a new EKS cluster creation request, wait
until the EKS cluster becomes `Active`. 2. For **Kubernetes version**, choose a version
from the drop-down menu. For more information about Kubernetes
versions, see [Understand the Kubernetes version lifecycle on EKS](../../../eks/latest/userguide/kubernetes-versions.md "../../../eks/latest/userguide/kubernetes-versions.md")
from the _Amazon EKS User
Guide_. 3. For **Operators**, choose **Use
default Helm charts and add-ons** or
**Don't install operators**. The option
defaults to **Use default Helm charts and
add-ons**, which will be used to install operators
on the EKS cluster. For more information about the default Helm
charts and add-ons, see [`helm_chart`](https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart/HyperPodHelmChart "https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart/HyperPodHelmChart") from the GitHub
repository. For more information, see [Installing
packages on the Amazon EKS cluster using Helm](sagemaker-hyperpod-eks-install-packages-using-helm-chart.md "sagemaker-hyperpod-eks-install-packages-using-helm-chart.md"). 4. For **Enabled operators**, view the list of
enabled operators. To edit the operators, uncheck the box at top
and choose operators to enable for the EKS cluster.

###### Note

To use HyperPod with EKS, you must install Helm
charts and add-ons that enable operators on the EKS cluster.
These components configure EKS as the control plane for
HyperPod and provide the necessary setup for
workload management and orchestration.

### Instance groups

To add an instance group, choose **Add group**. Each
instance group can be configured differently, and you can create a
heterogeneous cluster that consists of multiple instance groups with
various instance types. To deploy a cluster, you must add at least one
instance group. Follow these steps to add an instance group.

1. For **Instance group type**, choose
   **Standard** or **Restricted
   Instance Group (RIG)**. Typically, you will choose
   **Standard**, which provides a general
   purpose computing environment without additional security
   restrictions. **Restricted Instance Group
   (RIG)** is a specialized environment for
   foundational models customization such as Amazon Nova. For more
   information about setting up RIG for Amazon Nova model customization,
   see [Amazon Nova customization on Amazon SageMaker HyperPod](nova-hp.md "nova-hp.md").
2. For **Name**, specify a name for the instance
   group.
3. For **Instance capacity**, choose either
   on-demand capacity or a training plan to reserve your compute
   resources.
4. For **Instance type**, choose the instance
   for the instance group.

###### Important

Ensure that you choose an instance type with sufficient
quotas and enough unassigned IP addresses for your account.
To view or request additional quotas, see [SageMaker HyperPod quotas](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas"). 5. For **Instance quantity**, specify an integer
not exceeding the instance quota for cluster usage. For this
tutorial, enter **1** for all three
groups. 6. For **Target Availability Zone**, choose the
Availability Zone where your instances will be provisioned. The
Availability Zone should correspond to the location of your
accelerated compute capacity. 7. For **Additional storage volume per instance (GB) -
optional**, specify an integer between 1 and 16384
to set the size of an additional Elastic Block Store (EBS)
volume in gigabytes (GB). The EBS volume is attached to each
instance of the instance group. The default mount path for the
additional EBS volume is `/opt/sagemaker`. After the
cluster is successfully created, you can SSH into the cluster
instances (nodes) and verify if the EBS volume is mounted
correctly by running the `df -h` command. Attaching
an additional EBS volume provides stable, off-instance, and
independently persisting storage, as described in the [Amazon EBS volumes](../../../ebs/latest/userguide/ebs-volumes.md "../../../ebs/latest/userguide/ebs-volumes.md") section in the _Amazon Elastic Block Store
User Guide_. 8. For **Instance deep health checks**, choose
your option. Deep health checks monitor instance health during
creation and after software updates, automatically recovering
faulty instances through reboots or replacements when enabled.
To learn more, see [Deep health
checks](sagemaker-hyperpod-eks-resiliency-deep-health-checks.md "sagemaker-hyperpod-eks-resiliency-deep-health-checks.md") 9. For **Use GPU partition - optional**, if your
instance type supports GPU partitioning with Multi-Instance GPU
(MIG), you can enable this option to configure the GPU partition
profile for the instance group. GPU partitioning allows you to
divide GPUs into smaller, isolated partitions for improved resource
utilization. For more information, see [Using GPU partitions in Amazon SageMaker HyperPod](sagemaker-hyperpod-eks-gpu-partitioning.md "sagemaker-hyperpod-eks-gpu-partitioning.md").

    1. Toggle **Use GPU partition** to enable
     GPU partitioning for this instance group.
    2. Select a **GPU partition profile** from
     the available options for your instance type. Each profile
     defines the GPU slice configuration and memory allocation.

10. Choose **Add instance group**.

### Lifecycle scripts

You can choose to use the default lifecycle scripts or the custom
lifecycle scripts, which will be stored in your Amazon S3 bucket. You can
view the default lifecycle scripts in the [Awesome Distributed Training GitHub repository](https://github.com/aws-samples/awsome-distributed-training/tree/main/1.architectures/7.sagemaker-hyperpod-eks/LifecycleScripts "https://github.com/aws-samples/awsome-distributed-training/tree/main/1.architectures/7.sagemaker-hyperpod-eks/LifecycleScripts"). To learn
more about the lifecycle scripts, see [Customizing SageMaker HyperPod
clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md "sagemaker-hyperpod-lifecycle-best-practices-slurm.md").

1. For **Lifecycle scripts**, choose to use
   default or custom lifecycle scripts.
2. For **S3 bucket for lifecycle scripts**,
   choose to create a new bucket or use an existing bucket to store
   the lifecycle scripts.

### Permissions

Choose or create an IAM role that allows HyperPod to run
and access necessary AWS resources on your behalf. For more
information, see [IAM role for
SageMaker HyperPod](sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod "sagemaker-hyperpod-prerequisites-iam.md#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod").

### Storage

Configure the FSx for Lustre file system to be provisioned on the
HyperPod cluster.

1. For **File system**, choose an existing
   FSx for Lustre file system, to create a new FSx for Lustre file
   system, or don't provision an FSx for Lustre file system.
2. For **Throughput per unit of storage**,
   choose the throughput that will be available per TiB of
   provisioned storage.
3. For **Storage capacity**, enter a capacity
   value in TB.
4. For **Data compression type**, choose
   **LZ4** to enable data compression.
5. For **Lustre version**, view the value that's
   recommended for the new file systems.

### Tags - optional

For **Tags - _optional_**, add key and value pairs to the new
cluster and manage the cluster as an AWS resource. To learn more, see
[Tagging your AWS
resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").

## Deploy resources

After you complete the cluster configurations using either **Quick
setup** or **Custom setup**, choose the following
option to start resource provisioning and cluster creation.

- **Submit** - SageMaker AI will start provisioning the default
  configuration resources and creating the cluster.
- **Download CloudFormation template parameters** - You
  will download the configuration parameter JSON file and run AWS CLI
  command to deploy the CloudFormation stack to provision the configuration
  resources and creating the cluster. You can edit the downloaded
  parameter JSON file if needed. If you choose this option, see more
  instructions in [Creating
  SageMaker HyperPod clusters using CloudFormation templates](smcluster-getting-started-eks-console-create-cluster-cfn.md "smcluster-getting-started-eks-console-create-cluster-cfn.md").
