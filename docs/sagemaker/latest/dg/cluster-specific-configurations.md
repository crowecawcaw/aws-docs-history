# Cluster-specific

configurations

SageMaker HyperPod offers flexibility in running training jobs across different cluster
environments. Each environment has its own configuration requirements and setup process.
This section outlines the steps and configurations needed for running training jobs in
SageMaker HyperPod Slurm, SageMaker HyperPod k8s, and SageMaker training jobs. Understanding these
configurations is crucial for effectively leveraging the power of distributed training
in your chosen environment.

You can use a recipe in the following cluster environments:

- SageMaker HyperPod Slurm Orchestration
- SageMaker HyperPod Amazon Elastic Kubernetes Service Orchestration
- SageMaker training jobs
  To launch a training job in a cluster, set and install the corresponding cluster
  configuration and environment.

###### Topics

- [Running a training job on HyperPod Slurm](cluster-specific-configurations-run-training-job-hyperpod-slurm.md "cluster-specific-configurations-run-training-job-hyperpod-slurm.md")
- [Running a training job on HyperPod k8s](cluster-specific-configurations-run-training-job-hyperpod-k8s.md "cluster-specific-configurations-run-training-job-hyperpod-k8s.md")
- [Running
  a SageMaker training job](cluster-specific-configurations-run-sagemaker-training-job.md "cluster-specific-configurations-run-sagemaker-training-job.md")
