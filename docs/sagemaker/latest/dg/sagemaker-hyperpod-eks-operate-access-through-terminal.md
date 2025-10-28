# Accessing

SageMaker HyperPod cluster nodes

You can directly access the nodes of a SageMaker HyperPod cluster in service using the
AWS CLI commands for AWS Systems Manager (SSM). Run `aws ssm start-session` with
the host name of the node in format of
`sagemaker-cluster:[cluster-id]_[instance-group-name]-[instance-id]`.
You can retrieve the cluster ID, the instance ID, and the instance group name from
the [SageMaker HyperPod console](sagemaker-hyperpod-operate-slurm-console-ui.md#sagemaker-hyperpod-operate-slurm-console-ui-view-details-of-clusters "sagemaker-hyperpod-operate-slurm-console-ui.md#sagemaker-hyperpod-operate-slurm-console-ui-view-details-of-clusters") or by running `describe-cluster` and
`list-cluster-nodes` from the [AWS CLI
commands for SageMaker HyperPod](sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-list-cluster-nodes "sagemaker-hyperpod-operate-slurm-cli-command.md#sagemaker-hyperpod-operate-slurm-cli-command-list-cluster-nodes"). For example, if your cluster ID is
`aa11bbbbb222`, the cluster node name is
`controller-group`, and the cluster node ID is
`i-111222333444555aa`, the SSM `start-session` command
should be the following.

###### Note

If you haven't set up AWS Systems Manager, follow the instructions provided at [Setting up AWS Systems Manager and Run As
for cluster user access control](sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-ssm "sagemaker-hyperpod-prerequisites.md#sagemaker-hyperpod-prerequisites-ssm").

```
`$` `aws ssm start-session \
 --target sagemaker-cluster:`aa11bbbbb222`_`controller-group`-`i-111222333444555aa` \
 --region `us-west-2``
`Starting session with SessionId: s0011223344aabbccdd`
`root@ip-111-22-333-444:/usr/bin#`
```
