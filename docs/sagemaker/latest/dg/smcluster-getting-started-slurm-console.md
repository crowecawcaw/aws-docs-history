# Getting started with

SageMaker HyperPod using the SageMaker AI console

The following tutorial demonstrates how to create a new SageMaker HyperPod cluster and set
it up with Slurm through the SageMaker AI console UI. Following the tutorial, you'll create a
HyperPod cluster with three Slurm nodes, `my-controller-group`,
`my-login-group`, and `worker-group-1`.

###### Topics

- [Create
  cluster](#smcluster-getting-started-slurm-console-create-cluster-page "#smcluster-getting-started-slurm-console-create-cluster-page")
- [Deploy resources](#smcluster-getting-started-slurm-console-create-cluster-deploy "#smcluster-getting-started-slurm-console-create-cluster-deploy")
- [Delete the cluster and clean resources](#smcluster-getting-started-slurm-console-delete-cluster-and-clean "#smcluster-getting-started-slurm-console-delete-cluster-and-clean")

## Create

cluster

To navigate to the **SageMaker HyperPod Clusters** page and choose
**Slurm** orchestration, follow these steps.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Choose **HyperPod Clusters** in the left
   navigation pane and then **Cluster Management**.
3. On the **SageMaker HyperPod Clusters** page, choose
   **Create HyperPod cluster**.
4. On the **Create HyperPod cluster** drop-down,
   choose **Orchestrated by Slurm**.
5. On the Slurm cluster creation page, you will see two options. Choose the
   option that best fits your needs.
   1. **Quick setup** - To get started immediately with
      default settings, choose **Quick setup**. With this
      option, SageMaker AI will create new resources such as VPC, subnets,
      security groups, Amazon S3 bucket, IAM role, and FSx for Lustre in the
      process of creating your cluster.
   2. **Custom setup** - To integrate with existing
      AWS resources or have specific networking, security, or storage
      requirements, choose **Custom setup**. With this
      option, you can choose to use the existing resources or create new
      ones, and you can customize the configuration that best fits your
      needs.

On the **Quick setup** section, follow these steps to create
your HyperPod cluster with Slurm orchestration.

### General settings

Specify a name for the new cluster. You can’t change the name after the
cluster is created.

### Instance groups

To add an instance group, choose **Add group**. Each
instance group can be configured differently, and you can create a
heterogeneous cluster that consists of multiple instance groups with various
instance types. To deploy a cluster, you must add at least one instance
group for Controller and Compute group types.

###### Important

You can add one instance group at a time. To create multiple instance
groups, repeat the process for each instance group.

Follow these steps to add an instance group.

1. For **Instance group type**, choose a type for
   your instance group. For this tutorial, choose **Controller
   (head)** for `my-controller-group`,
   **Login** for `my-login-group`, and
   **Compute (worker)** for
   `worker-group-1`.
2. For **Name**, specify a name for the instance
   group. For this tutorial, create three instance groups named
   `my-controller-group`, `my-login-group`,
   and `worker-group-1`.
3. For **Instance capacity**, choose either
   on-demand capacity or a training plan to reserve your compute
   resources.
4. For **Instance type**, choose the instance for
   the instance group. For this tutorial, select
   `ml.c5.xlarge` for `my-controller-group`,
   `ml.m5.4xlarge` for `my-login-group`, and
   `ml.trn1.32xlarge` for `worker-group-1`.

###### Important

Ensure that you choose an instance type with sufficient quotas
and enough unassigned IP addresses for your account. To view or
request additional quotas, see [SageMaker HyperPod quotas](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas"). 5. For **Instance quantity**, specify an integer not
exceeding the instance quota for cluster usage. For this tutorial,
enter **1** for all three groups. 6. For **Target Availability Zone**, choose the
Availability Zone where your instances will be provisioned. The
Availability Zone should correspond to the location of your
accelerated compute capacity. 7. For **Additional storage volume per instance (GB) -
optional**, specify an integer between 1 and 16384 to
set the size of an additional Elastic Block Store (EBS) volume in
gigabytes (GB). The EBS volume is attached to each instance of the
instance group. The default mount path for the additional EBS volume
is `/opt/sagemaker`. After the cluster is successfully
created, you can SSH into the cluster instances (nodes) and verify
if the EBS volume is mounted correctly by running the `df
 -h` command. Attaching an additional EBS volume provides
stable, off-instance, and independently persisting storage, as
described in the [Amazon EBS volumes](../../../ebs/latest/userguide/ebs-volumes.md "../../../ebs/latest/userguide/ebs-volumes.md") section in the _Amazon Elastic Block Store User
Guide_. 8. Choose **Add instance group**.

### Quick setup defaults

This section lists all the default settings for your cluster creation,
including all the new AWS resources that will be created during the
cluster creation process. Review the default settings.

On the **Custom setup** section, follow these steps to create
your HyperPod cluster with Slurm orchestration.

### General settings

Specify a name for the new cluster. You can’t change the name after the
cluster is created.

For **Instance recovery**, choose **Automatic -
_recommended_** or
**None**.

### Networking

Configure your network settings for the cluster creation. These settings
can't be changed after the cluster is created.

1. For **VPC**, choose your own VPC if you already
   have one that gives SageMaker AI access to your VPC. To create a new VPC,
   follow the instructions at [Create a VPC](../../../vpc/latest/userguide/create-vpc.md "../../../vpc/latest/userguide/create-vpc.md")
   in the _Amazon Virtual Private Cloud User Guide_. You can leave it
   as **None** to use the default SageMaker AI VPC.
2. For **VPC IPv4 CIDR block**, enter the starting
   IP of your VPC.
3. For **Availability Zones**, choose the
   Availability Zones (AZ) where HyperPod will create subnets
   for your cluster. Choose AZs that match the location of your
   accelerated compute capacity.
4. For **Security groups**, create a security group
   or choose up to five security groups configured with rules to allow
   inter-resource communication within the VPC.

### Instance groups

To add an instance group, choose **Add group**. Each
instance group can be configured differently, and you can create a
heterogeneous cluster that consists of multiple instance groups with various
instance types. To deploy a cluster, you must add at least one instance
group.

###### Important

You can add one instance group at a time. To create multiple instance
groups, repeat the process for each instance group.

Follow these steps to add an instance group.

1. For **Instance group type**, choose a type for
   your instance group. For this tutorial, choose **Controller
   (head)** for `my-controller-group`,
   **Login** for `my-login-group`, and
   **Compute (worker)** for
   `worker-group-1`.
2. For **Name**, specify a name for the instance
   group. For this tutorial, create three instance groups named
   `my-controller-group`, `my-login-group`,
   and `worker-group-1`.
3. For **Instance capacity**, choose either
   on-demand capacity or a training plan to reserve your compute
   resources.
4. For **Instance type**, choose the instance for
   the instance group. For this tutorial, select
   `ml.c5.xlarge` for `my-controller-group`,
   `ml.m5.4xlarge` for `my-login-group`, and
   `ml.trn1.32xlarge` for `worker-group-1`.

###### Important

Ensure that you choose an instance type with sufficient quotas
and enough unassigned IP addresses for your account. To view or
request additional quotas, see [SageMaker HyperPod quotas](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas"). 5. For **Instance quantity**, specify an integer not
exceeding the instance quota for cluster usage. For this tutorial,
enter **1** for all three groups. 6. For **Target Availability Zone**, choose the
Availability Zone where your instances will be provisioned. The
Availability Zone should correspond to the location of your
accelerated compute capacity. 7. For **Additional storage volume per instance (GB) -
optional**, specify an integer between 1 and 16384 to
set the size of an additional Elastic Block Store (EBS) volume in
gigabytes (GB). The EBS volume is attached to each instance of the
instance group. The default mount path for the additional EBS volume
is `/opt/sagemaker`. After the cluster is successfully
created, you can SSH into the cluster instances (nodes) and verify
if the EBS volume is mounted correctly by running the `df
 -h` command. Attaching an additional EBS volume provides
stable, off-instance, and independently persisting storage, as
described in the [Amazon EBS volumes](../../../ebs/latest/userguide/ebs-volumes.md "../../../ebs/latest/userguide/ebs-volumes.md") section in the _Amazon Elastic Block Store User
Guide_. 8. Choose **Add instance group**.

### Lifecycle scripts

You can choose to use the default lifecycle scripts or the custom
lifecycle scripts, which will be stored in your Amazon S3 bucket. You can view
the default lifecycle scripts in the [Awesome Distributed Training GitHub repository](https://github.com/aws-samples/awsome-distributed-training/tree/main/1.architectures/7.sagemaker-hyperpod-eks/LifecycleScripts "https://github.com/aws-samples/awsome-distributed-training/tree/main/1.architectures/7.sagemaker-hyperpod-eks/LifecycleScripts"). To learn more
about the lifecycle scripts, see [Customizing SageMaker HyperPod
clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md "sagemaker-hyperpod-lifecycle-best-practices-slurm.md").

1. For **Lifecycle scripts**, choose to use default
   or custom lifecycle scripts.
2. For **S3 bucket for lifecycle scripts**, choose
   to create a new bucket or use an existing bucket to store the
   lifecycle scripts.

### Permissions

Choose or create an IAM role that allows HyperPod to run and
access necessary AWS resources on your behalf.

### Storage

Configure the FSx for Lustre file system to be provisioned on the
HyperPod cluster.

1. For **File system**, choose an existing
   FSx for Lustre file system, to create a new FSx for Lustre file system, or
   don't provision an FSx for Lustre file system.
2. For **Throughput per unit of storage**, choose
   the throughput that will be available per TiB of provisioned
   storage.
3. For **Storage capacity**, enter a capacity value
   in TB.
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
- **Download CloudFormation template parameters** - You will
  download the configuration parameter JSON file and run AWS CLI command to
  deploy the CloudFormation stack to provision the configuration resources and
  creating the cluster. You can edit the downloaded parameter JSON file if
  needed. If you choose this option, see more instructions in [Creating
  SageMaker HyperPod clusters using CloudFormation templates](smcluster-getting-started-slurm-console-create-cluster-cfn.md "smcluster-getting-started-slurm-console-create-cluster-cfn.md").

## Delete the cluster and clean resources

After you have successfully tested creating a SageMaker HyperPod cluster, it continues
running in the `InService` state until you delete the cluster. We
recommend that you delete any clusters created using on-demand SageMaker AI instances when
not in use to avoid incurring continued service charges based on on-demand pricing.
In this tutorial, you have created a cluster that consists of two instance groups.
One of them uses a C5 instance, so make sure you delete the cluster by following the
instructions at [Delete a
SageMaker HyperPod cluster](sagemaker-hyperpod-operate-slurm-console-ui.md#sagemaker-hyperpod-operate-slurm-console-ui-delete-cluster "sagemaker-hyperpod-operate-slurm-console-ui.md#sagemaker-hyperpod-operate-slurm-console-ui-delete-cluster").

However, if you have created a cluster with reserved compute capacity, the status
of the clusters does not affect service billing.

To clean up the lifecycle scripts from the S3 bucket used for this tutorial, go to
the S3 bucket you used during cluster creation and remove the files entirely.

If you have tested running any workloads on the cluster, make sure if you have
uploaded any data or if your job saved any artifacts to different S3 buckets or file
system services such as Amazon FSx for Lustre and Amazon Elastic File System. To prevent any incurring
charges, delete all artifacts and data from the storage or file system.
