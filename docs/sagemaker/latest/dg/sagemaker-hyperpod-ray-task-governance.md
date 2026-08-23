# Queueing with task governance

SageMaker HyperPod task governance streamlines resource allocation and keeps compute used
efficiently across teams and projects on your Amazon EKS clusters. Administrators set priority
levels for tasks, compute allocation for each team, how teams lend and borrow idle compute,
and whether a team preempts its own tasks.

Task Governance holds a workload until the team compute allocation has room, then starts
the head and workers together.

For the general concepts and the console setup, see [SageMaker HyperPod task governance](sagemaker-hyperpod-eks-operate-console-ui-governance.md "sagemaker-hyperpod-eks-operate-console-ui-governance.md").

###### Topics

- [Setting up task governance for Ray](sagemaker-hyperpod-ray-task-governance-setup.md "sagemaker-hyperpod-ray-task-governance-setup.md")
- [Quota and scheduling behavior for Ray workloads](sagemaker-hyperpod-ray-task-governance-quota.md "sagemaker-hyperpod-ray-task-governance-quota.md")
