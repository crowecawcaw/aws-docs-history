# Orchestrating SageMaker HyperPod clusters with

Slurm

Slurm support in SageMaker HyperPod helps you provision resilient clusters for running machine
learning (ML) workloads and developing state-of-the-art models such as large language models
(LLMs), diffusion models, and foundation models (FMs). It accelerates development of FMs by
removing undifferentiated heavy-lifting involved in building and maintaining large-scale
compute clusters powered by thousands of accelerators such as AWS Trainium and NVIDIA A100
and H100 Graphical Processing Units (GPUs). When accelerators fail, the resiliency features
of SageMaker HyperPod monitors the cluster instances automatically detect and replace the faulty
hardware on the fly so that you can focus on running ML workloads. Additionally, with
lifecycle configuration support in SageMaker HyperPod, you can customize your computing
environment to best suit your needs and configure it with the Amazon SageMaker AI distributed training
libraries to achieve optimal performance on AWS.

**Operating clusters**

You can create, conﬁgure, and maintain SageMaker HyperPod clusters graphically through the
console user interface (UI) and programmatically through the AWS command line interface
(CLI) or AWS SDK for Python (Boto3). With Amazon VPC, you can secure the cluster network and also take
advantage of configuring your cluster with resources in your VPC, such as Amazon FSx for Lustre,
which offers the fastest throughput. You can also give different IAM roles to cluster
instance groups, and limit actions that your cluster resources and users can operate. To
learn more, see [SageMaker HyperPod Slurm cluster operations](sagemaker-hyperpod-operate-slurm.md "sagemaker-hyperpod-operate-slurm.md").

**Configuring your ML environment**

SageMaker HyperPod runs [SageMaker HyperPod DLAMI](sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-hyperpod-ami "sagemaker-hyperpod-ref.md#sagemaker-hyperpod-ref-hyperpod-ami"), which sets up an
ML environment on the HyperPod clusters. You can configure additional
customizations to the DLAMI by providing lifecycle scripts to support your use case. To
learn more about how to set up lifecycle scripts, see [Getting started with SageMaker HyperPod](smcluster-getting-started-slurm.md "smcluster-getting-started-slurm.md") and [Customizing SageMaker HyperPod
clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md "sagemaker-hyperpod-lifecycle-best-practices-slurm.md").

**Scheduling jobs**

After you successfully create a HyperPod cluster, cluster users can log into the
cluster nodes (such as head or controller node, log-in node, and worker node) and schedule
jobs for running machine learning workloads. To learn more, see [Jobs on SageMaker HyperPod clusters](sagemaker-hyperpod-run-jobs-slurm.md "sagemaker-hyperpod-run-jobs-slurm.md").

**Resiliency against hardware failures**

SageMaker HyperPod runs health checks on cluster nodes and provides a workload auto-resume
functionality. With the cluster resiliency features of HyperPod, you can resume
your workload from the last checkpoint you saved, after faulty nodes are replaced with
healthy ones in clusters with more than 16 nodes. To learn more, see [SageMaker HyperPod cluster
resiliency](sagemaker-hyperpod-resiliency-slurm.md "sagemaker-hyperpod-resiliency-slurm.md").

**Logging and managing clusters**

You can find SageMaker HyperPod resource utilization metrics and lifecycle logs in Amazon CloudWatch, and
manage SageMaker HyperPod resources by tagging them. Each `CreateCluster` API run
creates a distinct log stream, named in `<cluster-name>-<timestamp>`
format. In the log stream, you can check the host names, the name of failed lifecycle
scripts, and outputs from the failed scripts such as `stdout` and
`stderr`. For more information, see [SageMaker HyperPod cluster management](sagemaker-hyperpod-cluster-management-slurm.md "sagemaker-hyperpod-cluster-management-slurm.md").

**Compatible with SageMaker AI tools**

Using SageMaker HyperPod, you can configure clusters with AWS optimized collective
communications libraries offered by SageMaker AI, such as the [SageMaker AI
distributed data parallelism (SMDDP) library](data-parallel.md "data-parallel.md"). The SMDDP library implements the
`AllGather` operation optimized to the AWS compute and network
infrastructure for the most performant SageMaker AI machine learning instances powered by NVIDIA
A100 GPUs. To learn more, see [Running distributed training workloads with Slurm on HyperPod](sagemaker-hyperpod-run-jobs-slurm-distributed-training-workload.md "sagemaker-hyperpod-run-jobs-slurm-distributed-training-workload.md").

**Instance placement with UltraServers**

SageMaker AI automatically allocates jobs
to instances within your UltraServer based on a best effort strategy of using all of the instances in one UltraServer
before using another one. For example, if you request
14 instances and have 2 UltraServers in your training plan, SageMaker AI uses all of the instances in the
first UltraServer. If you requested 20 instances and have 2 UltraServers in your training plan, SageMaker AI
will will use all 17 instances in the first UltraServer and then use 3 from the second UltraServer.

###### Topics

- [Getting started with SageMaker HyperPod](smcluster-getting-started-slurm.md "smcluster-getting-started-slurm.md")
- [SageMaker HyperPod Slurm cluster operations](sagemaker-hyperpod-operate-slurm.md "sagemaker-hyperpod-operate-slurm.md")
- [Customizing SageMaker HyperPod
  clusters using lifecycle scripts](sagemaker-hyperpod-lifecycle-best-practices-slurm.md "sagemaker-hyperpod-lifecycle-best-practices-slurm.md")
- [SageMaker HyperPod multi-head node support](sagemaker-hyperpod-multihead-slurm.md "sagemaker-hyperpod-multihead-slurm.md")
- [Jobs on SageMaker HyperPod clusters](sagemaker-hyperpod-run-jobs-slurm.md "sagemaker-hyperpod-run-jobs-slurm.md")
- [SageMaker HyperPod cluster
  resources monitoring](sagemaker-hyperpod-cluster-observability-slurm.md "sagemaker-hyperpod-cluster-observability-slurm.md")
- [SageMaker HyperPod cluster
  resiliency](sagemaker-hyperpod-resiliency-slurm.md "sagemaker-hyperpod-resiliency-slurm.md")
- [SageMaker HyperPod cluster management](sagemaker-hyperpod-cluster-management-slurm.md "sagemaker-hyperpod-cluster-management-slurm.md")
- [SageMaker HyperPod FAQs](sagemaker-hyperpod-faq-slurm.md "sagemaker-hyperpod-faq-slurm.md")
