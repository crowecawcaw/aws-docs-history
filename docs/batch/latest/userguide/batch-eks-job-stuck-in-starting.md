# AWS Batch on Amazon EKS job is stuck in

`STARTING` status

A Job may remain in `STARTING` status when the Pod is stuck in `PENDING` on `ContainerCreating`
for any long running requests from the kubelet (`pull`, `log`, `exec`, and `attach`) until the Pod
startup issue is resolved or the Job is terminated. In the qualifying scenarios below AWS Batch will
terminate the job on your behalf, otherwise the job must be terminated manually using the
[TerminateJob API](../APIReference/API_TerminateJob.md "../APIReference/API_TerminateJob.md").

To verify the reason a Job may be stuck in `STARTING`, use [Tutorial: Map a running job to a pod and a node](eks-jobs-map-running-job.md "eks-jobs-map-running-job.md") to find the `podName`, and describe the Pod:

```
`% kubectl describe pod aws-batch.000c8190-87df-31e7-8819-176fe017a24a -n my-aws-batch-namespace
Name: aws-batch.000c8190-87df-31e7-8819-176fe017a24a
Namespace: my-aws-batch-namespace
...
Containers:
 default:
...
 State: Waiting
 Reason: ContainerCreating
 Ready: False
...
Conditions:
 Type Status
 PodReadyToStartContainers False
 Initialized True
 Ready False
 ContainersReady False
 PodScheduled True
...
Events:
 Type Reason Age From Message
 ---- ------ ---- ---- -------
 Warning FailedMount 2m32s kubelet Unable to attach or mount volumes: ...`
```

Consider configuring your EKS cluster to [Send control plane logs to CloudWatch Logs](../../../eks/latest/userguide/control-plane-logs.md "../../../eks/latest/userguide/control-plane-logs.md") for full visibility.

## Scenario: Persisted Volume Claim Attach or Mount Failure

Jobs using Persistent Volume Claims where the volume fails to attach or mount are
candidates for termination. This can be a result of an incorrectly configured Job Definition.
See [Create a single-node job definition on Amazon EKS
resources](create-job-definition-eks.md "create-job-definition-eks.md") for more
details.
