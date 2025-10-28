# Multi-node parallel jobs

You can use multi-node parallel jobs to run single jobs that span multiple Amazon EC2 instances. With AWS Batch
multi-node parallel jobs (also known as _gang scheduling_), you can run large-scale, high-performance computing applications and distributed GPU model
training without the need to launch, configure, and manage Amazon EC2 resources directly. An AWS Batch multi-node parallel
job is compatible with any framework that supports IP-based, inter-node communication. Examples include Apache MXNet,
TensorFlow, Caffe2, or Message Passing Interface (MPI).

Multi-node parallel jobs are submitted as a single job. However, your job definition (or job
submission node overrides) specifies the number of nodes to create for the job and what node
groups to create. Each multi-node parallel job contains a **main
node**, which is launched first. After the main node is up, the child nodes are launched
and started. The job is finished only if the main node exits. All child nodes are then stopped.
For more information, see [Node groups](mnp-node-groups.md "mnp-node-groups.md").

Multi-node parallel job nodes are single-tenant. This means that only a single job container
is run on each Amazon EC2 instance.

The final job status (`SUCCEEDED` or `FAILED`) is determined by the
final job status of the main node. To get the status of a multi-node parallel job, describe the
job by using the job ID that was returned when you submitted the job. If you need the details for
child nodes, describe each child node individually. You can address nodes using the
`#`N``notation (starting with 0). For example, to access
 the details of the second node of a job, describe`aws_batch_job_id`#1
 using the AWS Batch [DescribeJobs](../APIReference/API_DescribeJobs.md "../APIReference/API_DescribeJobs.md") API operation. The
 `started`, `stoppedAt`, `statusReason`, and `exit`
information for a multi-node parallel job is populated from the main node.

If you specify job retries, a main node failure causes another attempt to occur. Child node
failures don't cause more attempts to occur. Each new attempt of a multi-node parallel job updates
the corresponding attempt of its associated child nodes.

To run multi-node parallel jobs on AWS Batch, your application code must contain the frameworks
and libraries that are necessary for distributed communication.

###### Topics

- [Environment variables](mnp-env-vars.md "mnp-env-vars.md")
- [Node groups](mnp-node-groups.md "mnp-node-groups.md")
- [Job lifecycle for MNP jobs](job-lifecycle.md "job-lifecycle.md")
- [Compute environment considerations for MNP with AWS Batch](mnp-ce.md "mnp-ce.md")
