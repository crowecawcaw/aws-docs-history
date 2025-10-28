# Optimizing Flink job restart times for task

recovery and scaling operations with Amazon EMR on EKS

When a task fails or when a scaling operation occurs, Flink attempts to re-execute the
task from the last completed checkpoint. The restart process could take a minute or
longer to execute, depending on the size of the checkpoint state and the number of
parallel tasks. During the restart period, backlog tasks can accumulate for the job.
There are some ways though, that Flink optimizes the speed of recovery and restart of
execution graphs to improve job stability.

This page describes some of the ways that Amazon EMR Flink can improve the job restart time
during task recovery or scaling operations on spot instances. Spot instances are unused compute capacity that's available at a discount. It has unique behaviors, including occasional
interruptions, so it's important to understand how Amazon EMR on EKS handles these, including how Amazon EMR on EKS carries out decommissioning and job restarts.

###### Topics

- [Task-local recovery](#flink-restart-task-local "#flink-restart-task-local")
- [Task-local recovery by Amazon EBS volume
  mount](#flink-restart-task-local-ebs "#flink-restart-task-local-ebs")
- [Generic log-based incremental
  checkpoint](#flink-restart-log-check "#flink-restart-log-check")
- [Fine-grained recovery](#flink-restart-fine-grained "#flink-restart-fine-grained")
- [Combined restart mechanism in adaptive
  scheduler](#flink-restart-combined "#flink-restart-combined")

## Task-local recovery

###### Note

Task-local recovery is supported with Flink on Amazon EMR on EKS 6.14.0 and
higher.

With Flink checkpoints, each task produces a snapshot of its state that Flink
writes to distributed storage like Amazon S3. In cases of recovery, the tasks restore
their state from the distributed storage. Distributed storage provides fault
tolerance and can redistribute the state during rescaling because it's accessible to
all nodes.

However, a remote distributed store also has a disadvantage: all tasks must read
their state from a remote location over the network. This can result in long
recovery times for large states during task recovery or scaling operations.

This problem of long recovery time is solved by _task-local
recovery_. Tasks write their state on checkpoint into a secondary
storage that is local to the task, such as on a local disk. They also store their
state in the primary storage, or Amazon S3 in our case. During recovery, the scheduler
schedules the tasks on the same Task Manager where the tasks ran earlier so that
they can recover from the local state store instead of reading from the remote state
store. For more information, see [Task-Local Recovery](https://nightlies.apache.org/flink/flink-docs-master/docs/ops/state/large_state_tuning/#task-local-recovery "https://nightlies.apache.org/flink/flink-docs-master/docs/ops/state/large_state_tuning/#task-local-recovery") in the _Apache Flink
Documentation_.

Our benchmark tests with sample jobs have shown that the recovery time has been
reduced from minutes to a few seconds with task-local recovery enabled.

To enable task-local recovery, set the following configurations in your
`flink-conf.yaml` file. Specify the checkpointing interval
value in milliseconds.

```
    state.backend.local-recovery: true
    state.backend: `hasmap or rocksdb`
    state.checkpoints.dir: s3://`STORAGE-BUCKET-PATH`/checkpoint
    execution.checkpointing.interval: `15000`
```

## Task-local recovery by Amazon EBS volume

mount

###### Note

Task-local recovery by Amazon EBS is supported with Flink on Amazon EMR on EKS 6.15.0 and
higher.

With Flink on Amazon EMR on EKS, you can automatically provision Amazon EBS volumes to the
TaskManager pods for task local recovery. The default overlay
mount comes with 10 GB volume, which is sufficient for jobs with a lower state.
Jobs with large states can enable the _automatic EBS volume
mount_ option. The TaskManager pods are automatically
created and mounted during pod creation and removed during pod deletion.

Use the following steps to enable automatic EBS volume mount for Flink in
Amazon EMR on EKS:

1. Export the values for the following variables that you'll use in upcoming
   steps.

```
export AWS_REGION=`aa-example-1`
export FLINK_EKS_CLUSTER_NAME=`my-cluster`
export AWS_ACCOUNT_ID=`111122223333`
```

2. Create or update a `kubeconfig` YAML file for your
   cluster.

```
aws eks update-kubeconfig --name $FLINK_EKS_CLUSTER_NAME --region $AWS_REGION
```

3. Create an IAM service account for the Amazon EBS Container Storage Interface
   (CSI) driver on your Amazon EKS cluster.

```
eksctl create iamserviceaccount \
   --name ebs-csi-controller-sa \
   --namespace kube-system \
   --region $AWS_REGION \
   --cluster $FLINK_EKS_CLUSTER_NAME\
   --role-name TLR_${AWS_REGION}_${FLINK_EKS_CLUSTER_NAME} \
   --role-only \
   --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
   --approve
```

4. Create the Amazon EBS CSI driver with the following command:

```
eksctl create addon \
   --name aws-ebs-csi-driver \
   --region $AWS_REGION \
   --cluster $FLINK_EKS_CLUSTER_NAME \
   --service-account-role-arn arn:aws:iam::${AWS_ACCOUNT_ID}:role/TLR_${AWS_REGION}_${FLINK_EKS_CLUSTER_NAME}
```

5. Create the Amazon EBS storage class with the following command:

```
cat ≪ EOF ≫ storage-class.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: ebs-sc
provisioner: ebs.csi.aws.com
volumeBindingMode: WaitForFirstConsumer
EOF
```

And then apply the class:

```
kubectl apply -f storage-class.yaml
```

6. Helm install the Amazon EMR Flink Kubernetes operator with options to create a
   service account. This creates the `emr-containers-sa-flink` to
   use in the Flink deployment.

```
helm install flink-kubernetes-operator flink-kubernetes-operator/ \
   --set jobServiceAccount.create=true \
   --set rbac.jobRole.create=true \
   --set rbac.jobRoleBinding.create=true
```

7. To submit the Flink job and enable the automatic provision of EBS volumes
   for task-local recovery, set the following configurations in your
   `flink-conf.yaml` file. Adjust the size limit for the
   state size of the job. Set `serviceAccount` to
   `emr-containers-sa-flink`. Specify the checkpointing interval
   value in milliseconds. And omit the `executionRoleArn`.

```
flinkConfiguration:
    task.local-recovery.ebs.enable: true
    kubernetes.taskmanager.local-recovery.persistentVolumeClaim.sizeLimit: 10Gi
    state.checkpoints.dir: s3://`BUCKET-PATH`/checkpoint
    state.backend.local-recovery: true
    state.backend: `hasmap or rocksdb`
    state.backend.incremental: "true"
    execution.checkpointing.interval: `15000`
  serviceAccount: emr-containers-sa-flink

```

When you're ready to delete the Amazon EBS CSI driver plugin, use the following
commands:

```
  # Detach Attached Policy
  aws iam detach-role-policy --role-name TLR_${$AWS_REGION}_${FLINK_EKS_CLUSTER_NAME} --policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy
  # Delete the created Role
  aws iam delete-role --role-name TLR_${$AWS_REGION}_${FLINK_EKS_CLUSTER_NAME}
  # Delete the created service account
  eksctl delete iamserviceaccount --name ebs-csi-controller-sa --namespace kube-system --cluster $FLINK_EKS_CLUSTER_NAME --region $AWS_REGION
  # Delete Addon
  eksctl delete addon --name aws-ebs-csi-driver --cluster $FLINK_EKS_CLUSTER_NAME --region $AWS_REGION
  # Delete the EBS storage class
  kubectl delete -f storage-class.yaml
```

## Generic log-based incremental

checkpoint

###### Note

Generic log-based incremental checkpointing is supported with Flink on
Amazon EMR on EKS 6.14.0 and higher.

Generic log-based incremental checkpointing was added in Flink 1.16 to improve the
speed of checkpoints. A faster checkpoint interval often results in a reduction of
recovery work because fewer events need to be reprocessed after recovery. For more
information, see [Improving speed and stability of checkpointing with generic log-based
incremental checkpoints](https://flink.apache.org/2022/05/30/improving-speed-and-stability-of-checkpointing-with-generic-log-based-incremental-checkpoints/ "https://flink.apache.org/2022/05/30/improving-speed-and-stability-of-checkpointing-with-generic-log-based-incremental-checkpoints/") on the _Apache Flink
Blog_.

With sample jobs, our benchmark tests have shown that the checkpoint time reduced
from minutes to a few seconds with the generic log-based incremental
checkpoint.

To enable generic log-based incremental checkpoints, set the following
configurations in your `flink-conf.yaml` file. Specify the
checkpointing interval value in milliseconds.

```
    state.backend.changelog.enabled: true
    state.backend.changelog.storage: filesystem
    dstl.dfs.base-path: s3://`bucket-path`/changelog
    state.backend.local-recovery: true
    state.backend: rocksdb
    state.checkpoints.dir: s3://`bucket-path`/checkpoint
    execution.checkpointing.interval: `15000`
```

## Fine-grained recovery

###### Note

Fine-grained recovery support for the default scheduler is supported with
Flink on Amazon EMR on EKS 6.14.0 and higher. Fine-grained recovery support in the
adaptive scheduler is available with Flink on Amazon EMR on EKS 6.15.0 and
higher.

When a task fails during execution, Flink resets the entire execution graph and
triggers complete re-execution from the last completed checkpoint. This is more
expensive than just re-executing the failed tasks. Fine-grained recovery restarts
only the pipeline-connected component of the failed task. In the following example,
the job graph has 5 vertices (`A` to `E`). All connections
between the vertices are pipelined with pointwise distribution, and the
`parallelism.default` for the job is set to `2`.

```
A → B → C → D → E
```

For this example, there are a total of 10 tasks running. The first pipeline
(`a1` to `e1`) runs on a TaskManager
(`TM1`), and the second pipeline (`a2` to `e2`)
runs on another TaskManager (`TM2`).

```
a1 → b1 → c1 → d1 → e1
a2 → b2 → c2 → d2 → e2
```

There are two pipelined connected components: `a1 → e1`, and `a2 →
 e2`. If either `TM1` or `TM2` fails, the failure
impacts only the 5 tasks in the pipeline where the TaskManager was
running. The restart strategy only starts the affected pipelined component.

Fine-grained recovery works only with perfectly parallel Flink jobs. It's not
supported with `keyBy()` or `redistribute()` operations. For
more information, see [FLIP-1: Fine Grained Recovery from Task Failures](https://cwiki.apache.org/confluence/display/FLINK/FLIP-1%3A+Fine+Grained+Recovery+from+Task+Failures "https://cwiki.apache.org/confluence/display/FLINK/FLIP-1%3A+Fine+Grained+Recovery+from+Task+Failures") in the _Flink
Improvement Proposal_ Jira project.

To enable fine-grained recovery, set the following configurations in your
`flink-conf.yaml` file.

```
jobmanager.execution.failover-strategy: region
restart-strategy: `exponential-delay or fixed-delay`
```

## Combined restart mechanism in adaptive

scheduler

###### Note

The combined restart mechanism in adaptive scheduler is supported with Flink
on Amazon EMR on EKS 6.15.0 and higher.

Adaptive scheduler can adjust the parallelism of the job based on available slots.
It automatically reduces the parallelism if not enough slots are available to fit
the configured job parallelism. If new slots become available, the job is scaled up
again to the configured job parallelism. An adaptive scheduler avoids downtime on
the job when there are not enough resources available. This is the supported
scheduler for Flink Autoscaler. We recommend adaptive scheduler with Amazon EMR Flink for
these reasons. However, adaptive schedulers might do multiple restarts within a
short period of time, one restart for every new resource added. This could lead to a
performance drop in the job.

With Amazon EMR 6.15.0 and higher, Flink has a combined restart mechanism in adaptive
scheduler that opens a restart window when the first resource is added, and then
waits until the configured window interval of the default 1 minute. It performs
a single restart when there are sufficient resources available to run the job with
configured parallelism or when the interval times out.

With sample jobs, our benchmark tests have shown that this feature processes 10%
of records more than the default behavior when you use adaptive scheduler and Flink
autoscaler.

To enable the combined restart mechanism, set the following configurations in your
`flink-conf.yaml` file.

```
jobmanager.adaptive-scheduler.combined-restart.enabled: true
jobmanager.adaptive-scheduler.combined-restart.window-interval: 1m
```
