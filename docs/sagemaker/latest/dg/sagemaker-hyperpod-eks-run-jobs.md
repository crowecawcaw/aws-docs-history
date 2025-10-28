# Running jobs on SageMaker HyperPod clusters

orchestrated by Amazon EKS

The following topics provide procedures and examples of accessing compute nodes and
running ML workloads on provisioned SageMaker HyperPod clusters orchestrated with Amazon EKS. Depending
on how you have set up the environment on your HyperPod cluster, there are many
ways to run ML workloads on HyperPod clusters.

###### Note

When running jobs via the SageMaker HyperPod CLI or kubectl, HyperPod can track
compute utilization (GPU/CPU hours) across namespaces (teams). These metrics power usage
reports, which provide:

- Visibility into allocated vs. borrowed resource consumption
- Teams resource utilization for auditing (up to 180 days)
- Cost attribution aligned with Task Governance policies
  To use usage reports, you must install the usage report infrastructure. We strongly
  recommend configuring [Task
  Governance](sagemaker-hyperpod-eks-operate-console-ui-governance.md "sagemaker-hyperpod-eks-operate-console-ui-governance.md") to enforce compute quotas and enable granular cost
  attribution.

For more information about setting up and generating usage reports, see [Reporting Compute Usage in
HyperPod](sagemaker-hyperpod-usage-reporting.md "sagemaker-hyperpod-usage-reporting.md").

###### Tip

For a hands-on experience and guidance on how to set up and use a SageMaker HyperPod cluster
orchestrated with Amazon EKS, we recommend taking this [Amazon EKS Support in SageMaker HyperPod](https://catalog.us-east-1.prod.workshops.aws/workshops/2433d39e-ccfe-4c00-9d3d-9917b729258e "https://catalog.us-east-1.prod.workshops.aws/workshops/2433d39e-ccfe-4c00-9d3d-9917b729258e") workshop.

Data scientist users can train foundational models using the EKS cluster set as the
orchestrator for the SageMaker HyperPod cluster. Scientists leverage the [SageMaker HyperPod CLI](https://github.com/aws/sagemaker-hyperpod-cli "https://github.com/aws/sagemaker-hyperpod-cli") and the
native `kubectl` commands to find available SageMaker HyperPod clusters, submit
training jobs (Pods), and manage their workloads. The SageMaker HyperPod CLI enables job
submission using a training job schema file, and provides capabilities for job listing,
description, cancellation, and execution. Scientists can use [Kubeflow Training
Operator](https://www.kubeflow.org/docs/components/training/overview/ "https://www.kubeflow.org/docs/components/training/overview/") according to compute quotas managed by HyperPod, and [SageMaker AI-managed MLflow](mlflow.md "mlflow.md")
to manage ML experiments and training runs.

###### Topics

- [Installing the SageMaker HyperPod
  CLI](sagemaker-hyperpod-eks-run-jobs-access-nodes.md "sagemaker-hyperpod-eks-run-jobs-access-nodes.md")
- [SageMaker HyperPod CLI
  commands](sagemaker-hyperpod-eks-hyperpod-cli-reference.md "sagemaker-hyperpod-eks-hyperpod-cli-reference.md")
- [Running jobs using the
  SageMaker HyperPod CLI](sagemaker-hyperpod-eks-run-jobs-hyperpod-cli.md "sagemaker-hyperpod-eks-run-jobs-hyperpod-cli.md")
- [Running jobs using
  kubectl](sagemaker-hyperpod-eks-run-jobs-kubectl.md "sagemaker-hyperpod-eks-run-jobs-kubectl.md")
