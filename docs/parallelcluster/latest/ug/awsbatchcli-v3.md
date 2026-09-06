

# Using AWS Batch (`awsbatch`) scheduler with AWS ParallelCluster
<a name="awsbatchcli-v3"></a>

**Warning**  
AWS CodeBuild is not supported in Asia Pacific (Malaysia) (`ap-southeast-5`) and Asia Pacific (Thailand) (`ap-southeast-7`) regions. Therefore, ParallelCluster AWS Batch integration is not supported in those regions.

AWS ParallelCluster also supports AWS Batch schedulers. The following topics describe how to use AWS Batch. For information about AWS Batch, see [AWS Batch](https://aws.amazon.com/batch/). For documentation, see the [AWS Batch User Guide](https://docs.aws.amazon.com/batch/latest/userguide/).

**AWS ParallelCluster CLI commands for AWS Batch**

When you use the `awsbatch` scheduler, the AWS ParallelCluster CLI commands for AWS Batch are automatically installed in the AWS ParallelCluster head node. The CLI uses AWS Batch API operations and permits the following operations:
+ Submit and manage jobs.
+ Monitor jobs, queues, and hosts.
+ Mirror traditional scheduler commands.

**Important**  
AWS ParallelCluster doesn't support GPU jobs for AWS Batch. For more information, see [GPU jobs](https://docs.aws.amazon.com/batch/latest/userguide/gpu-jobs.html).

This CLI is distributed as a separate package. For more information, see [Scheduler support](moving-from-v2-to-v3.md#scheduler_support).

**Topics**
+ [`awsbsub`](awsbatchcli.awsbsub-v3.md)
+ [`awsbstat`](awsbatchcli.awsbstat-v3.md)
+ [`awsbout`](awsbatchcli.awsbout-v3.md)
+ [`awsbkill`](awsbatchcli.awsbkill-v3.md)
+ [`awsbqueues`](awsbatchcli.awsbqueues-v3.md)
+ [`awsbhosts`](awsbatchcli.awsbhosts-v3.md)