# SageMaker HyperPod CLI

commands

The following table summarizes the SageMaker HyperPod CLI commands.

###### Note

For a complete CLI reference, see [README](https://github.com/aws/sagemaker-hyperpod-cli?tab=readme-ov-file#sagemaker-hyperpod-command-line-interface "https://github.com/aws/sagemaker-hyperpod-cli?tab=readme-ov-file#sagemaker-hyperpod-command-line-interface") in the [SageMaker HyperPod CLI GitHub
repository](https://github.com/aws/sagemaker-hyperpod-cli "https://github.com/aws/sagemaker-hyperpod-cli").

| SageMaker HyperPod CLI command | Entity         | Description                                                                                                                                                                                                                                                                                  |
| ------------------------------ | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `hyperpod get-clusters`        | cluster/access | Lists all clusters to which the user has been enabled with IAM permissions to submit training workloadsGives the current snapshot of whole available instances which are not running any workloads or jobs along with maximum capacity, grouping by health check statuses (ex: BurnInPassed) |
| `hyperpod connect-cluster`     | cluster/access | Configures `kubectl` to operate on the specified HyperPod cluster and namespace                                                                                                                                                                                                              |
| `hyperpod start-job`           | job            | Submits the job to targeted cluster-Job name will be unique at namespace level-Users will be able to override yaml spec by passing them as CLI arguments                                                                                                                                     |
| `hyperpod get-job`             | job            | Display metadata of the submitted job                                                                                                                                                                                                                                                        |
| `hyperpod list-jobs`           | job            | Lists all jobs in the connected cluster/namespace to which the user has been added with IAM permissions to submit training workloads                                                                                                                                                         |
| `hyperpod cancel-job`          | job            | Stops and deletes the job and gives up underlying compute resources. This job cannot be resumed again. A new job needs to be started, if needed.                                                                                                                                             |
| `hyperpod list-pods`           | pod            | Lists all the pods in the given job in a namespace                                                                                                                                                                                                                                           |
| `hyperpod get-log`             | pod            | Retrieves the logs of a particulat pod in a specified job                                                                                                                                                                                                                                    |
| `hyperpod exec`                | pod            | Run the bash command in the shell of the specified pod(s) and publishes the output                                                                                                                                                                                                           |
| `hyperpod --help`              | utility        | lists all supported commands                                                                                                                                                                                                                                                                 |
