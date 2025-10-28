# Amazon SageMaker HyperPod quickstart

This quickstart guides you through creating your first HyperPod cluster with
Slurm and Amazon EKS (EKS) orchestrations. Choose the orchestration that best fits your
infrastructure needs to get started with SageMaker HyperPod.

###### In this topic:

- [Create a Slurm-orchestrated
  SageMaker HyperPod cluster](#sagemaker-hyperpod-quickstart-slurm "#sagemaker-hyperpod-quickstart-slurm")
- [Create an EKS-orchestrated
  SageMaker HyperPod cluster](#sagemaker-hyperpod-quickstart-eks "#sagemaker-hyperpod-quickstart-eks")
- [Submit workloads](#sagemaker-hyperpod-quickstart-workload "#sagemaker-hyperpod-quickstart-workload")

## Create a Slurm-orchestrated

SageMaker HyperPod cluster

Follow these steps to create your first SageMaker HyperPod cluster with Slurm
orchestration.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Choose **HyperPod Clusters** in the left
   navigation pane and then **Cluster
   Management**.
3. On the **SageMaker HyperPod Clusters** page, choose
   **Create HyperPod cluster**.
4. On the **Create HyperPod cluster** drop-down,
   choose **Orchestrated by Slurm**.
5. On the cluster creation page, choose **Quick setup**.
   With this option, you get started immediately with default settings. SageMaker AI will
   create new resources such as VPC, subnets, security groups, Amazon S3 bucket, IAM
   role, and FSx for Lustre in the process of creating your cluster.
6. On **General settings**, specify a name for the new
   cluster. You can’t change the name after the cluster is created.
7. On **Instance groups**, choose **Add
   group**. Each instance group can be configured differently, and you
   can create a heterogeneous cluster that consists of multiple instance groups
   with various instance types. To deploy a cluster, you must add at least one
   instance group. You can add one instance group at a time. To create multiple
   instance groups, repeat the process for each instance group.

Follow these steps to add an instance group.

    1. For **Instance group type**, choose a type for
     your instance group. For this quickstart, choose **Controller
     (head)** for `my-controller-group`,
     **Login** for `my-login-group`, and
     **Compute (worker)** for
     `worker-group-1`.
    2. For **Name**, specify a name for the instance
     group. For this quickstart, create three instance groups named
     `my-controller-group`, `my-login-group`, and
     `worker-group-1`.
    3. For **Instance capacity**, choose either on-demand
     capacity or a training plan to reserve your compute
     resources.
    4. For **Instance type**, choose the instance for
     the instance group. For this quickstart, select
     `ml.c5.xlarge` for `my-controller-group`,
     `ml.m5.4xlarge` for `my-login-group`, and
     `ml.trn1.32xlarge` for `worker-group-1`.


    Ensure that you choose the instance type with sufficient quotas in
     your account, or request additional quotas by following the instructions
     at [SageMaker HyperPod quotas](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas").
    5. For **Instance quantity**, specify an integer not
     exceeding the instance quota for cluster usage. For this quickstart,
     enter **1** for all three groups.
    6. For **Target Availability Zone**, choose the
     Availability Zone where your instances will be provisioned. The
     Availability Zone should correspond to the location of your
     accelerated compute capacity.
    7. For **Additional storage volume per instance (GB) -
     optional**, specify an integer between 1 and 16384 to
     set the size of an additional Elastic Block Store (EBS) volume in
     gigabytes (GB). The EBS volume is attached to each instance of the
     instance group. The default mount path for the additional EBS volume
     is `/opt/sagemaker`. After the cluster is successfully
     created, you can SSH into the cluster instances (nodes) and verify
     if the EBS volume is mounted correctly by running the `df
     -h` command. Attaching an additional EBS volume provides
     stable, off-instance, and independently persisting storage, as
     described in the [Amazon EBS volumes](../../../ebs/latest/userguide/ebs-volumes.md "../../../ebs/latest/userguide/ebs-volumes.md") section in the *Amazon Elastic Block Store User
     Guide*.
    8. Choose **Add instance group**.

8. On **Quick configuration defaults**, review the default
   settings. This section lists all the default settings for your cluster creation,
   including all the new AWS resources that will be created during the cluster
   creation process.
9. Choose **Submit**.

For more information, see [Getting started with
SageMaker HyperPod using the SageMaker AI console](smcluster-getting-started-slurm-console.md "smcluster-getting-started-slurm-console.md").

## Create an EKS-orchestrated

SageMaker HyperPod cluster

Follow these steps to create your first SageMaker HyperPod cluster with Amazon EKS
orchestration.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Choose **HyperPod Clusters** in the left
   navigation pane and then **Cluster
   Management**.
3. On the **SageMaker HyperPod Clusters** page, choose
   **Create HyperPod cluster**.
4. On the **Create HyperPod cluster** drop-down, choose
   **Orchestrated by Amazon EKS**.
5. On the cluster creation page, choose **Quick configuration**.
   With this option, you can get started immediately with default settings. SageMaker AI
   will create new resources such as VPC, subnets, security groups, Amazon S3 bucket,
   IAM role, and FSx for Lustre in the process of creating your cluster.
6. On **General settings**, specify a name for the new cluster. You can’t change the name after the
   cluster is created.
7. On **Instance groups**, choose **Add
   group**. Each instance group can be configured differently, and you can
   create a heterogeneous cluster that consists of multiple instance groups with
   various instance types. To deploy a cluster, you must add at least one instance
   group. You can add one instance group at a time. To create multiple instance
   groups, repeat the process for each instance group.

Follow these steps to add an instance group.

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
    3. For **Instance capacity**, choose either on-demand
     capacity or a training plan to reserve your compute
     resources.
    4. For **Instance type**, choose the instance for the
     instance group. Ensure that you choose the instance type with
     sufficient quotas in your account, or request additional quotas
     by following at [SageMaker HyperPod quotas](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-quotas").
    5. For **Instance quantity**, specify an integer not
     exceeding the instance quota for cluster usage. For this quickstart,
     enter **1** for all three groups.
    6. For **Target Availability Zone**, choose the
     Availability Zone where your instances will be provisioned. The
     Availability Zone should correspond to the location of your
     accelerated compute capacity.
    7. For **Additional storage volume per instance (GB) -
     optional**, specify an integer between 1 and 16384 to
     set the size of an additional Elastic Block Store (EBS) volume in
     gigabytes (GB). The EBS volume is attached to each instance of the
     instance group. The default mount path for the additional EBS volume
     is `/opt/sagemaker`. After the cluster is successfully
     created, you can SSH into the cluster instances (nodes) and verify
     if the EBS volume is mounted correctly by running the `df
     -h` command. Attaching an additional EBS volume provides
     stable, off-instance, and independently persisting storage, as
     described in the [Amazon EBS volumes](../../../ebs/latest/userguide/ebs-volumes.md "../../../ebs/latest/userguide/ebs-volumes.md") section in the *Amazon Elastic Block Store User
     Guide*.
    8. For **Instance deep health checks**, choose your
     option. Deep health checks monitor instance health during creation
     and after software updates, automatically recovering faulty
     instances through reboots or replacements when enabled.
    9. Choose **Add instance group**.

8. On **Quick configuration defaults**, review the default
   settings. This section lists all the default settings for your cluster creation,
   including all the new AWS resources that will be created during the cluster
   creation process.
9. Choose **Submit**.

For more information, see [Creating
a SageMaker HyperPod cluster with Amazon EKS orchestration](sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md "sagemaker-hyperpod-eks-operate-console-ui-create-cluster.md").

## Submit workloads

Follow these workshop tutorials to submit sample workloads.

- [Amazon SageMaker HyperPod for Slurm](https://catalog.workshops.aws/sagemaker-hyperpod/en-US "https://catalog.workshops.aws/sagemaker-hyperpod/en-US")
- [Amazon SageMaker HyperPod for Amazon EKS](https://catalog.workshops.aws/sagemaker-hyperpod-eks/en-US "https://catalog.workshops.aws/sagemaker-hyperpod-eks/en-US")
