# Do I need an AWS DataSync agent?

To use AWS DataSync, you might need an agent. An _agent_ is a virtual
machine (VM) appliance that you deploy in your storage environment for data transfers.

Whether you need an agent depends on several factors, including the type of storage you're
transferring to or from, if you're transferring across AWS accounts, and which
AWS Regions you're transferring between. Before reading further, [check that DataSync supports the transfer you're
interested in](working-with-locations.md "working-with-locations.md").

After you determine that DataSync supports your transfer scenario, review the following
information to help you understand whether you need an agent.

## Situations when you need a DataSync agent

Most situations that require a DataSync agent involve storage that's managed by you or
another cloud provider.

- Transferring between AWS storage services and on-premises storage
- Transferring between Amazon EFS or Amazon FSx and storage in other clouds
- Transferring between some AWS storage services [across AWS accounts](working-with-locations.md#working-with-locations-across-accounts "working-with-locations.md#working-with-locations-across-accounts") (when
  neither storage service is Amazon S3)
- Transferring between a commercial AWS Region and an AWS GovCloud (US) where the
  source and destination are either Amazon EFS or Amazon FSx

## Situations when you don't need a DataSync

agent

The situations that don't require an agent apply whether you're transferring in the
[same AWS Region](working-with-locations.md#working-with-locations-same-region "working-with-locations.md#working-with-locations-same-region") or [across Regions](working-with-locations.md#working-with-locations-cross-regions "working-with-locations.md#working-with-locations-cross-regions").

- Transferring between AWS storage services in the same AWS account
- Transferring between Amazon S3 and a different AWS storage service across
  AWS accounts
- Transferring between Amazon S3 and object storage in other clouds
- Transferring between a commercial AWS Region and an AWS GovCloud (US) where
  either the source or destination is Amazon S3

## Using multiple DataSync agents

While most transfers only need one agent, using multiple agents can speed up transfers
for large datasets with millions of files or objects. In these situations, we recommend
running transfer tasks in parallel. This approach spreads the transfer workload across
multiple tasks, with each task using its own agent. It also helps reduce the time it
takes DataSync to prepare and transfer your data. For more information, see [Partitioning large datasets with multiple
tasks](create-task-how-to.md#multiple-tasks-large-dataset "create-task-how-to.md#multiple-tasks-large-dataset").

Another option—especially if you have millions of small files—is to use
multiple agents with a transfer location. For example, you can connect up to four agents
to your on-premises Network File System (NFS) file service. This option might speed up
your transfer, although the time it takes DataSync to prepare the transfer doesn’t
change.

With either approach, be mindful that these can increase the I/O operations on your
storage and affect your network bandwidth. For more information on using multiple agents
for your DataSync transfers, see the [AWS Storage Blog](https://aws.amazon.com/blogs/storage/how-to-accelerate-your-data-transfers-with-aws-datasync-scale-out-architectures/ "https://aws.amazon.com/blogs/storage/how-to-accelerate-your-data-transfers-with-aws-datasync-scale-out-architectures/").

If you're thinking of using multiple agents, remember the following:

- Using multiple agents with a location doesn't provide high availability. All
  the agents associated with a location must be online before you can start your
  transfer task. If one of the agents is [offline](managing-agent.md#understand-agent-statuses "managing-agent.md#understand-agent-statuses"), you can't run your task.
- If you're [using a virtual private cloud (VPC)
  service endpoint](choose-service-endpoint.md#datasync-in-vpc "choose-service-endpoint.md#datasync-in-vpc") to communicate with the DataSync service, all the
  agents must use the same endpoint and subnet.

## Next steps

- If you need an agent, review the [agent
  requirements](agent-requirements.md "agent-requirements.md") to understand what makes sense for your storage
  environment.
- If you don't need an agent for your transfer, you
  can start
  [configuring your
  transfer](transferring-data-datasync.md "transferring-data-datasync.md").
