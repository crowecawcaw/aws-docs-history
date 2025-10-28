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

**To replace a node**

Label the node to replace with
`sagemaker.amazonaws.com/node-health-status=UnschedulablePendingReplacement`,
which triggers the SageMaker HyperPod [Automatic node
recovery](sagemaker-hyperpod-eks-resiliency-node-recovery.md "sagemaker-hyperpod-eks-resiliency-node-recovery.md"). Note that you also need
to activate automatic node recovery during cluster creation or update.

```
`kubectl label nodes `<node-name>` \
 sagemaker.amazonaws.com/node-health-status=UnschedulablePendingReplacement`
```

**To reboot a node**

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
node is terminated or reboot in few minutes.
