# Node groups

A node group is an identical group of job nodes that all share the same container
properties. You can use AWS Batch to specify up to five distinct node groups for each job.

Each group can have its own container images, commands, environment variables, and so on. For example, you can
submit a job that requires a single `c5.xlarge` instance for the main node and five `c5.xlarge`
instance child nodes. Each of these distinct node groups may specify different container images or commands to run
for each job.

Alternatively, all of the nodes in your job can use a single node group. Moreover, your
application code can differentiate node roles such as the main node and child node. It does this
by comparing the `AWS_BATCH_JOB_MAIN_NODE_INDEX` environment variable against its own
value for `AWS_BATCH_JOB_NODE_INDEX`. You can have up to 1,000 nodes in a single job.
This is the default limit for instances in an Amazon ECS cluster. You can [request to increase this limit](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

###### Note

Currently all node groups in a multi-node parallel job must use the same instance type.
