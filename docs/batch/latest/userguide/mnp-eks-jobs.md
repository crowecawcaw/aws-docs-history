# Multi-node parallel jobs on Amazon EKS

You can use AWS Batch on Amazon Elastic Kubernetes Service to run multi-node parallel (MNP) jobs (also known as
_gang scheduling_) on your managed Kubernetes clusters. This option is commonly
used for large, tightly-coupled, high-performance jobs that can’t be run on a single Amazon Elastic Compute Cloud
instance. For more information, see [Multi-node parallel jobs](multi-node-parallel-jobs.md "multi-node-parallel-jobs.md").

You can use this feature to run Amazon EKS managed Kubernetes-specific high-performance computing
applications, large language model training, and other Artificial Intelligence (AI)/Machine
Learning (ML) jobs.

###### Topics

- [Running MNP jobs](mnp-eks-running-mnp-jobs.md "mnp-eks-running-mnp-jobs.md")
- [Create an Amazon EKS MNP job
  definition](mnp-eks-create-eks-mnp-job-definition.md "mnp-eks-create-eks-mnp-job-definition.md")
- [Submit an Amazon EKS MNP job](mnp-eks-submit-eks-mnp-job.md "mnp-eks-submit-eks-mnp-job.md")
- [Override an Amazon EKS MNP job
  definition](mnp-eks-override-eks-mnp-job-definition.md "mnp-eks-override-eks-mnp-job-definition.md")
