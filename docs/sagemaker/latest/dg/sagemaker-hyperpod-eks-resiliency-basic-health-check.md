# Basic health

checks

SageMaker HyperPod performs a set of _basic health checks_ on cluster
instances during the creation and update of HyperPod clusters. These basic
health checks are orchestrator-agnostic, so these checks are applicable regardless of
the underlying orchestration platforms supported by SageMaker HyperPod (Amazon EKS or
Slurm).

The basic health checks monitor cluster instances for issues related to devices such
as accelerators (GPU and Trainium cores) and network devices (Elastic Fabric Adapter, or
EFA). To find the list of basic cluster health checks, see [Cluster health checks](sagemaker-hyperpod-resiliency-slurm.md#sagemaker-hyperpod-resiliency-slurm-cluster-health-check "sagemaker-hyperpod-resiliency-slurm.md#sagemaker-hyperpod-resiliency-slurm-cluster-health-check").
