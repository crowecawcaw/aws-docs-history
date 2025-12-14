# Manually quarantine, replace,

or reboot a node

Learn how to manually quarantine, replace, and reboot a faulty node in SageMaker HyperPod
clusters orchestrated with Amazon EKS.

**To quarantine a node and force delete a training
pod**

```
`kubectl cordon `<node-name>``
```

After quarantine, force ejecting the Pod. This is useful when you see a pod is stuck
in termination for more than 30min or `kubectl describe pod` shows ‘Node is
not ready’ in Events

```
`kubectl delete pods `<pod-name>` --grace-period=0 --force`
```

SageMaker HyperPod offers two methods for manual node recovery. The preferred
approach is using the SageMaker HyperPod Reboot and Replace APIs, which provides a faster and more transparent
recovery process that works across all orchestrators. Alternatively, you can use kubectl commands
to label nodes for reboot and replace operations. Both methods activate the same SageMaker HyperPod recovery
processes.

**To reboot a node using the Reboot API**

To reboot a node you can use the BatchRebootClusterNodes API.

Here is an example of running the reboot operation on two Instances of a cluster using the AWS Command Line Interface:

```
 aws sagemaker-dev batch-reboot-cluster-nodes \
        --cluster-name arn:aws:sagemaker:ap-northeast-1:123456789:cluster/test-cluster \
        --node-ids i-abc123 i-def456
```

**To replace a node using the Replace API**

To replace a node you can use the BatchReplaceClusterNodes API as follows

Here is an example of running the replace operation on two Instances of a cluster using the AWS Command Line Interface:

```
 aws sagemaker-dev batch-replace-cluster-nodes \
        --cluster-name arn:aws:sagemaker:ap-northeast-1:123456789:cluster/test-cluster \
        --node-ids i-abc123 i-def456
```

**To replace a node using kubectl**

Label the node to replace with
`sagemaker.amazonaws.com/node-health-status=UnschedulablePendingReplacement`,
which triggers the SageMaker HyperPod [Automatic node
recovery](sagemaker-hyperpod-eks-resiliency-node-recovery.md "sagemaker-hyperpod-eks-resiliency-node-recovery.md"). Note that you also need
to activate automatic node recovery during cluster creation or update.

```
`kubectl label nodes `<node-name>` \
 sagemaker.amazonaws.com/node-health-status=UnschedulablePendingReplacement`
```

**To reboot a node using kubectl**

Label the node to reboot with
`sagemaker.amazonaws.com/node-health-status=UnschedulablePendingReboot`,
which triggers the SageMaker HyperPod [Automatic node
recovery](sagemaker-hyperpod-eks-resiliency-node-recovery.md "sagemaker-hyperpod-eks-resiliency-node-recovery.md"). Note that you also need
to activate automatic node recovery during cluster creation or update.

```
`kubectl label nodes <node-name> \
 sagemaker.amazonaws.com/node-health-status=UnschedulablePendingReboot`
```

After the labels `UnschedulablePendingReplacement` or
`UnschedulablePendingReboot` are applied, you should be able to see the
node is terminated or rebooted in a few minutes.
