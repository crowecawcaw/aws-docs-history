# Amazon EKS jobs

A job is the smallest unit of work in AWS Batch. An AWS Batch job on Amazon EKS has a one-to-one mapping to a Kubernetes pod.
An AWS Batch job definition is a template for an AWS Batch job. When you submit an AWS Batch job, you reference a job
definition, target a job queue, and provide a name for a job. In the job definition of an AWS Batch job on Amazon EKS, the
[eksProperties](../APIReference/API_EksProperties.md "../APIReference/API_EksProperties.md") parameter
defines the set of parameters that an AWS Batch on Amazon EKS job supports. In a [SubmitJob](../APIReference/API_SubmitJob.md "../APIReference/API_SubmitJob.md") request, the [eksPropertiesOverride](../APIReference/API_EksPropertiesOverride.md "../APIReference/API_EksPropertiesOverride.md") parameter allows for
overrides to some common parameters. This way, you can use templates of job definitions for multiple jobs. When a job
is dispatched to your Amazon EKS cluster, AWS Batch transforms the job into a `podspec` (`Kind: Pod`).
The `podspec` uses some additional AWS Batch parameters to ensure that jobs are scaled and scheduled
correctly. AWS Batch combines labels and taints to ensure jobs run only on AWS Batch managed nodes and that other pods
don't run on those nodes.

###### Important

- If the `hostNetwork` parameter isn't explicitly set in an Amazon EKS job definition, the pod
  networking mode in AWS Batch defaults to host mode. More specifically, the following settings are applied:
  `hostNetwork=true` and `dnsPolicy=ClusterFirstWithHostNet`.
- AWS Batch cleans up job pods soon after a pod completes its job. To see pod application logs, configure a
  logging service for your cluster. For more information, see [Use CloudWatch Logs to monitor AWS Batch on Amazon EKS jobs](batch-eks-cloudwatch-logs.md "batch-eks-cloudwatch-logs.md").

###### Topics

- [Tutorial: Map a running job to a pod and a node](eks-jobs-map-running-job.md "eks-jobs-map-running-job.md")
- [Tutorial: Map a running pod back to its job](eks-jobs-map-running-pod-to-job.md "eks-jobs-map-running-pod-to-job.md")

###### Features that AWS Batch Amazon EKS jobs support

These are the AWS Batch specific features that are also common to Kubernetes jobs that run on Amazon EKS:

- [Job dependencies](job_dependencies.md "job_dependencies.md")
- [Array jobs](array_jobs.md "array_jobs.md")
- [Job timeouts](job_timeouts.md "job_timeouts.md")
- [Automated job retries](job_retries.md "job_retries.md")
- [Use fair-share scheduling to help schedule jobs](fair-share-scheduling.md "fair-share-scheduling.md")

###### Kubernetes`Secrets` and `ServiceAccounts`

AWS Batch supports referencing Kubernetes `Secrets` and `ServiceAccounts`. You can configure
pods to use Amazon EKS IAM roles for service accounts. For more information, see [Configuring pods to use a Kubernetes service account](../../../eks/latest/userguide/pod-configuration.md "../../../eks/latest/userguide/pod-configuration.md") in the
[_Amazon EKS User Guide_](../../../eks/latest/userguide.md "../../../eks/latest/userguide.md").

###### Related documents

- [Memory and vCPU considerations for AWS Batch on Amazon EKS](memory-cpu-batch-eks.md "memory-cpu-batch-eks.md")
- [Run GPU jobs](gpu-jobs.md "gpu-jobs.md")
- [Jobs stuck in a RUNNABLE status](job_stuck_in_runnable.md "job_stuck_in_runnable.md")
