Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Billing for autonomics operations

By default, Amazon Redshift will not bill you for resources used for autonomics.
If you choose to allocate extra compute resources for more consistent autonomics,
Amazon Redshift will bill you only for autonomics operations that actually use additional resources,
such as concurrency-scaling clusters (or additional RPUs), which are allocated only when main cluster
or base RPUs are fully utilized running user workload. For more information, see
[Allocating extra compute resources for automatic database optimization](t_extra-compute-autonomics.md "t_extra-compute-autonomics.md") and
[Concurrency scaling](concurrency-scaling.md "concurrency-scaling.md").

##

Autonomics billing for provisioned clusters

On provisioned clusters, billing for autonomics operations adheres to the following logic:

| Autonomics operation type                                                        | Billing behavior                                               |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Amazon Redshift runs an autonomics operation on the main cluster.                | Amazon Redshift doesn't bill you for the autonomics operation. |
| Amazon Redshift runs an autonomics operation on the concurrency-scaling cluster. | Amazon Redshift bills you for the autonomics operation.        |

For more information, see [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing/ "https://aws.amazon.com/redshift/pricing/").

##

Autonomics billing for serverless workgroups

On serverless workgroups, billing for autonomics operations adheres to the following logic:

| Autonomics operation type                                                                                                                                                                | Billing behavior                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Amazon Redshift runs a user query and meanwhile finishes an autonomics operation.                                                                                                        | Amazon Redshift doesn't bill you for the autonomics operation.                          |
| Amazon Redshift has to allocate additional compute capacity for autonomics execution<br>during periods of high system load.                                                              | Amazon Redshift bills you for additional compute capacity used on autonomics execution. |
| Amazon Redshift begins running an autonomics operation while no user queries are running.<br>Amazon Redshift will only do this if you've enabled extra compute resources for autonomics. | Amazon Redshift bills you for the autonomics operation.                                 |

You are only billed once for overlapping activity from user or autonomics workload. For example,
suppose Amazon Redshift initiates an autonomic operation while no user queries are running, and a user query
begins during that operation. In that case, billing is applied once for the interval in which the
workgroup is active.

For more information, see
[Billing for Amazon Redshift Serverless](../mgmt/serverless-billing.md "../mgmt/serverless-billing.md")  
 in the _Amazon Redshift Management Guide_.
