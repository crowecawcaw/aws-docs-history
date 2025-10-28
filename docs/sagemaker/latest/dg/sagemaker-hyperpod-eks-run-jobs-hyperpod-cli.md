# Running jobs using the

SageMaker HyperPod CLI

To run jobs, make sure that you installed Kubeflow Training Operator in the EKS
clusters. For more information, see [Installing
packages on the Amazon EKS cluster using Helm](sagemaker-hyperpod-eks-install-packages-using-helm-chart.md "sagemaker-hyperpod-eks-install-packages-using-helm-chart.md").

Run the `hyperpod get-cluster` command to get the list of available
HyperPod clusters.

```
hyperpod get-clusters
```

Run the `hyperpod connect-cluster` to configure the SageMaker HyperPod CLI with
the EKS cluster orchestrating the HyperPod cluster.

```
hyperpod connect-cluster --cluster-name <hyperpod-cluster-name>
```

Use the `hyperpod start-job` command to run a job. The following command
shows the command with required options.

```
hyperpod start-job \
    --job-name `<job-name>`
    --image `<docker-image-uri>`
    --entry-script `<entrypoint-script>`
    --instance-type `<ml.instance.type>`
    --node-count `<integer>`
```

The `hyperpod start-job` command also comes with various options such as
job auto-resume and job scheduling.

## Enabling job auto-resume

The `hyperpod start-job` command also has the following options to
specify job auto-resume. For enabling job auto-resume to work with the SageMaker HyperPod
node resiliency features, you must set the value for the `restart-policy`
option to `OnFailure`. The job must be running under the
`kubeflow` namespace or a namespace prefixed with
`hyperpod`.

- [--auto-resume <bool>] #Optional, enable job auto resume after fails,
  default is false
- [--max-retry <int>] #Optional, if auto-resume is true, max-retry
  default value is 1 if not specified
- [--restart-policy <enum>] #Optional, PyTorchJob restart policy.
  Available values are `Always`, `OnFailure`,
  `Never` or `ExitCode`. The default value is
  `OnFailure`.

```
hyperpod start-job \
    ... // required options \
    --auto-resume true \
    --max-retry 3 \
    --restart-policy OnFailure
```

## Running

jobs with scheduling options

The `hyperpod start-job` command has the following options to set up
the job with queuing mechanisms.

###### Note

You need [Kueue](https://kueue.sigs.k8s.io/docs/overview/ "https://kueue.sigs.k8s.io/docs/overview/")
installed in the EKS cluster. If you haven't installed, follow the instructions
in [Setup for
SageMaker HyperPod task governance](sagemaker-hyperpod-eks-operate-console-ui-governance-setup.md "sagemaker-hyperpod-eks-operate-console-ui-governance-setup.md").

- [--scheduler-type <enum>] #Optional, Specify the scheduler type. The
  default is `Kueue`.
- [--queue-name <string>] #Optional, Specify the name of the [Local
  Queue](https://kueue.sigs.k8s.io/docs/concepts/local_queue/ "https://kueue.sigs.k8s.io/docs/concepts/local_queue/") or [Cluster
  Queue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/ "https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/") you want to submit with the job. The queue should be
  created by cluster admins using `CreateComputeQuota`.
- [--priority <string>] #Optional, Specify the name of the [Workload Priority
  Class](https://kueue.sigs.k8s.io/docs/concepts/workload_priority_class/ "https://kueue.sigs.k8s.io/docs/concepts/workload_priority_class/"), which should be created by cluster admins.

```
hyperpod start-job \
    ... // required options
    --scheduler-type Kueue \
    --queue-name high-priority-queue \
    --priority high
```

## Running

jobs from a configuration file

As an alternative, you can create a job configuration file containing all the
parameters required by the job and then pass this config file to the `hyperpod
 start-job` command using the --config-file option. In this case:

1. Create your job configuration file with the required parameters. Refer to
   the job configuration file in the SageMaker HyperPod CLI GitHub repository for a
   [baseline configuration file](sagemaker-hyperpod-eks-run-jobs-hyperpod-cli.md#sagemaker-hyperpod-eks-hyperpod-cli-from-config "sagemaker-hyperpod-eks-run-jobs-hyperpod-cli.md#sagemaker-hyperpod-eks-hyperpod-cli-from-config").
2. Start the job using the configuration file as follows.

```
hyperpod start-job --config-file `/path/to/test_job.yaml`
```

###### Tip

For a complete list of parameters of the `hyperpod start-job`
command, see the [Submitting a Job](https://github.com/aws/sagemaker-hyperpod-cli?tab=readme-ov-file#submitting-a-job "https://github.com/aws/sagemaker-hyperpod-cli?tab=readme-ov-file#submitting-a-job") section in the `README.md` of the
SageMaker HyperPod CLI GitHub repository.
