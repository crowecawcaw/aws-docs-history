# Job lifecycle for MNP jobs

When you submit a multi-node parallel job, the job enters the `SUBMITTED` status.
Then, the job waits for any job dependencies to finish. The job also moves to the
`RUNNABLE` status. Last, AWS Batch provisions the instance capacity that's required to
run your job and launches these instances.

Each multi-node parallel job contains a **main node**. The main node is a single
subtask that AWS Batch monitors to determine the outcome of the submitted multi node job. The main node is launched
first and it moves to the `STARTING` status. The timeout value specified in the
`attemptDurationSeconds` parameter applies to the whole job and not to the nodes.

When the main node reaches the `RUNNING` status after the node's container is running, the child
nodes are launched and they also move to the `STARTING` status. The child nodes come up in random order.
There are no guarantees on the timing or ordering of child node launch. To ensure that the all the nodes of the jobs
are in the `RUNNING` status after the node's container is running, your application code can query the
AWS Batch API to get the main node and child node information. Alternatively, the application code can wait until all
nodes are online before starting any distributed processing task. The private IP address of the main node is
available as the `AWS_BATCH_JOB_MAIN_NODE_PRIVATE_IPV4_ADDRESS` environment variable in each child node.
Your application code may use this information to coordinate and communicate data between each task.

As individual nodes exit, they move to `SUCCEEDED` or `FAILED`,
depending on their exit code. If the main node exits, the job is considered finished, and all of
the child nodes are stopped. If a child node dies, AWS Batch doesn't take any action on the other
nodes in the job. If you don't want your job to continue with a reduced number of nodes, you must
factor this into your application code. Doing this terminates or cancels the job.
