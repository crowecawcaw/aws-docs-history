# Example

HyperPod task governance AWS CLI commands

You can use HyperPod with EKS through Kubectl or through HyperPod
custom CLI. You can use these commands through Studio or AWS CLI. The following
provides SageMaker HyperPod task governance examples, on how to view cluster details using the
HyperPod AWS CLI commands. For more information, including how to install, see
the [HyperPod CLI
Github repository](https://github.com/aws/sagemaker-hyperpod-cli "https://github.com/aws/sagemaker-hyperpod-cli").

###### Topics

- [Get cluster accelerator device quota
  information](#hp-eks-cli-get-clusters "#hp-eks-cli-get-clusters")
- [Submit a job to SageMaker AI-managed queue and
  namespace](#hp-eks-cli-start-job "#hp-eks-cli-start-job")
- [List jobs](#hp-eks-cli-list-jobs "#hp-eks-cli-list-jobs")
- [Get job detailed information](#hp-eks-cli-get-job "#hp-eks-cli-get-job")
- [Suspend and unsuspend jobs](#hp-eks-cli-patch-job "#hp-eks-cli-patch-job")
- [Debugging jobs](#hp-eks-cli-other "#hp-eks-cli-other")

## Get cluster accelerator device quota

information

The following example command gets the information on the cluster accelerator
device quota.

```
hyperpod get-clusters -n hyperpod-ns-test-team
```

The namespace in this example, `hyperpod-ns-test-team`, is created in
Kubernetes based on the team name provided, `test-team`, when the compute
allocation is created. For more information, see [Edit policies](sagemaker-hyperpod-eks-operate-console-ui-governance-policies-edit.md "sagemaker-hyperpod-eks-operate-console-ui-governance-policies-edit.md").

Example response:

```
[
    {
        "Cluster": "hyperpod-eks-test-`cluster-id`",
        "InstanceType": "ml.g5.xlarge",
        "TotalNodes": 2,
        "AcceleratorDevicesAvailable": 1,
        "NodeHealthStatus=Schedulable": 2,
        "DeepHealthCheckStatus=Passed": "N/A",
        "Namespaces": {
            "hyperpod-ns-test-team": {
                "TotalAcceleratorDevices": 1,
                "AvailableAcceleratorDevices": 1
            }
        }
    }
]
```

## Submit a job to SageMaker AI-managed queue and

namespace

The following example command submits a job to your HyperPod cluster. If
you have access to only one team, the HyperPod AWS CLI will automatically
assign the queue for you in this case. Otherwise if multiple queues are discovered,
we will display all viable options for you to select.

```
hyperpod start-job --job-name hyperpod-cli-test --job-kind kubeflow/PyTorchJob --image docker.io/kubeflowkatib/pytorch-mnist-cpu:v1beta1-bc09cfd --entry-script /opt/pytorch-mnist/mnist.py --pull-policy IfNotPresent --instance-type ml.g5.xlarge --node-count 1 --tasks-per-node 1 --results-dir ./result --priority training-priority
```

The priority classes are defined in the **Cluster policy**, which
defines how tasks are prioritized and idle compute is allocated. When a data
scientist submits a job, they use one of the priority class names with the format
``priority-class-name`-priority`. In
 this example, `training-priority` refers to the priority class named
“training”. For more information on policy concepts, see [Policies](sagemaker-hyperpod-eks-operate-console-ui-governance-policies.md "sagemaker-hyperpod-eks-operate-console-ui-governance-policies.md").

If a priority class is not specified, the job is treated as a low priority job,
with a task ranking value of 0.

If a priority class is specified, but does not correspond to one of the priority
classes defined in the **Cluster policy**, the submission fails and
an error message provides the defined set of priority classes.

You can also submit the job using a YAML configuration file using the following
command:

```
hyperpod start-job --config-file ./`yaml-configuration-file-name`.yaml
```

The following is an example YAML configuration file that is equivalent to
submitting a job as discussed above.

```
defaults:
  - override hydra/job_logging: stdout
hydra:
  run:
    dir: .
  output_subdir: null
training_cfg:
  entry_script: /opt/pytorch-mnist/mnist.py
  script_args: []
  run:
    name: hyperpod-cli-test
    nodes: 1
    ntasks_per_node: 1
cluster:
  cluster_type: k8s
  instance_type: ml.g5.xlarge
  custom_labels:
    kueue.x-k8s.io/priority-class: training-priority
  cluster_config:
    label_selector:
      required:
        sagemaker.amazonaws.com/node-health-status:
          - Schedulable
      preferred:
        sagemaker.amazonaws.com/deep-health-check-status:
          - Passed
      weights:
        - 100
    pullPolicy: IfNotPresent
base_results_dir: ./result
container: docker.io/kubeflowkatib/pytorch-mnist-cpu:v1beta1-bc09cfd
env_vars:
  NCCL_DEBUG: INFO
```

Alternatively, you can submit a job using `kubectl` to ensure the task
appears in the **Dashboard** tab. The following is an example
kubectl command.

```
kubectl apply -f ./`yaml-configuration-file-name`.yaml
```

When submitting the job, include your queue name and priority class labels. For
example, with the queue name
`hyperpod-ns-`team-name`-localqueue` and
priority class ``priority-class-name`-priority`,
you must include the following labels:

- `kueue.x-k8s.io/queue-name:
hyperpod-ns-`team-name`-localqueue`
- `kueue.x-k8s.io/priority-class:
`priority-class-name`-priority`

The following YAML configuration snippet demonstrates how to add labels to your
original configuration file to ensure your task appears in the
**Dashboard** tab:

```
metadata:
    name: `job-name`
    namespace: hyperpod-ns-`team-name`
    labels:
        kueue.x-k8s.io/queue-name: hyperpod-ns-`team-name`-localqueue
        kueue.x-k8s.io/priority-class: `priority-class-name`-priority
```

## List jobs

The following command lists the jobs and their details.

```
hyperpod list-jobs
```

Example response:

```
{
    "jobs": [
        {
            "Name": "hyperpod-cli-test",
            "Namespace": "hyperpod-ns-test-team",
            "CreationTime": "2024-11-18T21:21:15Z",
            "Priority": "training",
            "State": "Succeeded"
        }
    ]
}
```

## Get job detailed information

The following command provides a job’s details. If no namespace is specified,
HyperPod AWS CLI will fetch a namespace managed by SageMaker AI that you have access
to.

```
hyperpod get-job --job-name hyperpod-cli-test
```

Example response:

```
{
    "Name": "hyperpod-cli-test",
    "Namespace": "hyperpod-ns-test-team",
    "Label": {
        "app": "hyperpod-cli-test",
        "app.kubernetes.io/managed-by": "Helm",
        "kueue.x-k8s.io/priority-class": "training"
    },
    "CreationTimestamp": "2024-11-18T21:21:15Z",
    "Status": {
        "completionTime": "2024-11-18T21:25:24Z",
        "conditions": [
            {
                "lastTransitionTime": "2024-11-18T21:21:15Z",
                "lastUpdateTime": "2024-11-18T21:21:15Z",
                "message": "PyTorchJob hyperpod-cli-test is created.",
                "reason": "PyTorchJobCreated",
                "status": "True",
                "type": "Created"
            },
            {
                "lastTransitionTime": "2024-11-18T21:21:17Z",
                "lastUpdateTime": "2024-11-18T21:21:17Z",
                "message": "PyTorchJob hyperpod-ns-test-team/hyperpod-cli-test is running.",
                "reason": "PyTorchJobRunning",
                "status": "False",
                "type": "Running"
            },
            {
                "lastTransitionTime": "2024-11-18T21:25:24Z",
                "lastUpdateTime": "2024-11-18T21:25:24Z",
                "message": "PyTorchJob hyperpod-ns-test-team/hyperpod-cli-test successfully completed.",
                "reason": "PyTorchJobSucceeded",
                "status": "True",
                "type": "Succeeded"
            }
        ],
            "replicaStatuses": {
                "Worker": {
                    "selector": "training.kubeflow.org/job-name=hyperpod-cli-test,training.kubeflow.org/operator-name=pytorchjob-controller,training.kubeflow.org/replica-type=worker",
                    "succeeded": 1
                }
            },
        "startTime": "2024-11-18T21:21:15Z"
    },
    "ConsoleURL": "https://us-west-2.console.aws.amazon.com/sagemaker/home?region=us-west-2#/cluster-management/hyperpod-eks-test-`cluster-id`“
}
```

## Suspend and unsuspend jobs

If you want to remove some submitted job from the scheduler, HyperPod
AWS CLI provides `suspend` command to temporarily remove the job from
orchestration. The suspended job will no longer be scheduled unless the job is
manually unsuspended by the `unsuspend` command

To temporarily suspend a job:

```
hyperpod patch-job suspend --job-name hyperpod-cli-test
```

To add a job back to the queue:

```
hyperpod patch-job unsuspend --job-name hyperpod-cli-test
```

## Debugging jobs

The HyperPod AWS CLI also provides other commands for you to debug job
submission issues. For example `list-pods` and `get-logs` in
the HyperPod AWS CLI Github repository.
