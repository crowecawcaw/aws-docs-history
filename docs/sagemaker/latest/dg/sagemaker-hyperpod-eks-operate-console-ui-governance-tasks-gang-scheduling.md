

# Using gang scheduling in Amazon SageMaker HyperPod task governance
<a name="sagemaker-hyperpod-eks-operate-console-ui-governance-tasks-gang-scheduling"></a>

In distributed ML training, a job often requires multiple pods running concurrently across nodes with pod-to-pod communication. HyperPod task governance uses Kueue's `waitForPodsReady` feature to implement gang scheduling. When enabled, the workload is monitored by Kueue until all of its pods are ready, meaning scheduled, running, and passing the optional readiness probe. If not all pods of the workload are ready within the configured timeout, the workload is evicted and requeued.

Gang scheduling provides the following benefits:
+ **Prevents resource waste** — Kueue evicts and requeues the workload if all pods do not become ready, ensuring resources are not held indefinitely by partially running workloads.
+ **Avoids deadlocks** — Prevents jobs from holding partial resources and blocking each other indefinitely.
+ **Automatic recovery** — If pods aren't ready within the timeout, the workload is evicted and requeued with configurable exponential backoff, rather than hanging indefinitely.

## Activate gang scheduling
<a name="sagemaker-hyperpod-eks-operate-console-ui-governance-tasks-gang-scheduling-activate"></a>

To activate gang scheduling, you must have a HyperPod Amazon EKS cluster with the task governance Amazon EKS add-on installed. The add-on status must be `Active` or `Degraded`.

**Note**  
Gang scheduling can also be configured directly using `kubectl` by editing the Kueue configuration on the cluster.

**Activate gang scheduling (SageMaker AI console)**

1. Open the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/) and navigate to your HyperPod cluster.

1. Choose the **Policy management** tab.

1. In the **Task governance** section, open **Actions**, then choose **Configure gang scheduling**.

1. Toggle gang scheduling on and configure the settings.

1. Choose **Save**. The Kueue controller restarts to apply the change.

## Gang scheduling configuration settings
<a name="sagemaker-hyperpod-eks-operate-console-ui-governance-tasks-gang-scheduling-settings"></a>

The following table describes the configuration settings for gang scheduling.


| Setting | Description | Default | 
| --- | --- | --- | 
| timeout | How long Kueue waits for all pods to become ready before evicting and requeuing the workload. | 5m | 
| recoveryTimeout | How long Kueue waits for a pod to recover after a node failure before requeuing the workload. Set to 0s to disable. Defaults to the value of timeout if not set. | 5m | 
| blockAdmission | When enabled, workloads are admitted sequentially. No new workload is admitted until all pods of the current one are ready. Prevents deadlocks on resource-constrained clusters. | Off | 
| requeuingStrategy timestamp | Whether requeue order uses Creation (original submission time, preserves queue position) or Eviction (time of last eviction, effectively deprioritizing repeatedly failing jobs). | Eviction | 
| requeuingStrategy backoffLimitCount | Maximum requeue attempts before Kueue permanently deactivates the workload. Leave empty for unlimited retries. | Unlimited | 
| requeuingStrategy backoffBaseSeconds | The base time in seconds for exponential backoff when requeuing a workload after each consecutive timeout. The exponent is 2. | 60s | 
| requeuingStrategy backoffMaxSeconds | Cap on the exponential backoff delay. Once reached, Kueue continues requeuing at this fixed interval. | 3600s | 

**Note**  
Modifying gang scheduling settings restarts the Kueue controller, which may temporarily delay job admission. This applies whether you are enabling, disabling, or updating any value. Running jobs are not interrupted.

**Note**  
Gang scheduling is cluster-wide. It applies to all Kueue-managed workloads on the cluster, not just specific teams or queues.