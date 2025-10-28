# Using AWS Batch (`awsbatch`) scheduler with

AWS ParallelCluster

###### Warning

AWS CodeBuild is not supported in Asia Pacific (Malaysia) (`ap-southeast-5`) and
Asia Pacific (Thailand) (`ap-southeast-7`) regions. Therefore, ParallelCluster AWS Batch
integration is not supported in those regions.

AWS ParallelCluster also supports AWS Batch schedulers. The following topics describe how to use
AWS Batch. For information about AWS Batch, see [AWS Batch](https://aws.amazon.com/batch/ "https://aws.amazon.com/batch/").
For documentation, see the [AWS Batch User Guide](../../../batch/latest/userguide.md "../../../batch/latest/userguide.md").

AWS ParallelCluster CLI commands for AWS Batch

When you use the `awsbatch` scheduler, the AWS ParallelCluster CLI commands for AWS Batch
are automatically installed in the AWS ParallelCluster head node. The CLI uses AWS Batch API operations
and permits the following operations:

- Submit and manage jobs.
- Monitor jobs, queues, and hosts.
- Mirror traditional scheduler commands.

###### Important

AWS ParallelCluster doesn't support GPU jobs for AWS Batch. For more information, see [GPU jobs](../../../batch/latest/userguide/gpu-jobs.md "../../../batch/latest/userguide/gpu-jobs.md").

This CLI is distributed as a separate package. For more information, see
[Scheduler support](moving-from-v2-to-v3.md#scheduler_support "moving-from-v2-to-v3.md#scheduler_support").

###### Topics

- [awsbsub](awsbatchcli.md "awsbatchcli.md")
- [awsbstat](awsbatchcli.md "awsbatchcli.md")
- [awsbout](awsbatchcli.md "awsbatchcli.md")
- [awsbkill](awsbatchcli.md "awsbatchcli.md")
- [awsbqueues](awsbatchcli.md "awsbatchcli.md")
- [awsbhosts](awsbatchcli.md "awsbatchcli.md")
