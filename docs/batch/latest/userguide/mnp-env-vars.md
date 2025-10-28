# Environment variables

At runtime, each node is configured the standard environment variables that all AWS Batch jobs
receive. In addition, the nodes are configured with the following environment variables that are
specific to multi-node parallel jobs:

`AWS_BATCH_JOB_MAIN_NODE_INDEX`

This variable is set to the index number of the job's main node. Your application code
can compare the `AWS_BATCH_JOB_MAIN_NODE_INDEX` to the
`AWS_BATCH_JOB_NODE_INDEX` on an individual node to determine if it's the main
node.

`AWS_BATCH_JOB_MAIN_NODE_PRIVATE_IPV4_ADDRESS`

This variable is only set in multi-node parallel job child nodes. This variable isn't
present on the main node. This variable is set to the private IPv4 address of the job's main
node. Your child node's application code can use this address to communicate with the main
node.

`AWS_BATCH_JOB_NODE_INDEX`

This variable is set to the node index number of the node. The node index begins at 0,
and each node receives a unique index number. For example, a multi-node parallel job with 10
children has index values of 0-9.

`AWS_BATCH_JOB_NUM_NODES`

This variable is set to the number of nodes that you have requested for your multi-node
parallel job.
