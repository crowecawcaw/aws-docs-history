

# Setting up task governance for Ray
<a name="sagemaker-hyperpod-ray-task-governance-setup"></a>

Set up Task Governance on your cluster first, then complete the Ray-specific steps on this page. For the concepts and the console setup, see [Setup for SageMaker HyperPod task governance](sagemaker-hyperpod-eks-operate-console-ui-governance-setup.md).

## Namespaces that need a compute allocation
<a name="sagemaker-hyperpod-ray-task-governance-setup-namespaces"></a>

Task Governance admits a Ray workload only in a namespace that has a compute allocation. Create an allocation for every namespace where you create Ray workloads. A workload in a namespace with no allocation stays pending and is never admitted. For the console steps, see [Policies](sagemaker-hyperpod-eks-operate-console-ui-governance-policies.md).

## Gang scheduling
<a name="sagemaker-hyperpod-ray-task-governance-setup-gang"></a>

Confirm that gang scheduling is enabled for your cluster. A Ray cluster needs its head and all of its workers running together, so without gang scheduling a partially scheduled cluster holds capacity without making progress. Task Governance implements gang scheduling with the Kueue `waitForPodsReady` feature, which evicts and requeues a workload whose pods do not all become ready within the configured timeout. For the configuration settings, see [Using gang scheduling in Amazon SageMaker HyperPod task governance](sagemaker-hyperpod-eks-operate-console-ui-governance-tasks-gang-scheduling.md).

## Verify
<a name="sagemaker-hyperpod-ray-task-governance-setup-verify"></a>

Create a small `RayCluster` in an allocated namespace and confirm it reaches a running state. If it stays pending, confirm the namespace has a compute allocation with room for the declared cluster size.