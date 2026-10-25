

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Differentiating agentless and agent-based servers
<a name="differences-vcenter-aws"></a>

**Important**  
Agentless replication is no longer available for new deployments. We recommend agent-based replication for all migrations. To learn more, see [Why we recommend agent-based replication](installing-vcenter-overview-mgn.md#why-agent-based).

You can differentiate an agentless vCenter VM that's replicating through snapshot shipping and an agent-based server (from any source infrastructure) through several ways:



1. On the **Source servers** page, under the **Replication type** column, the MGN console identifies the replication type, whether it is through **Snapshot shipping** (agentless) or **Agent based**. 

1. In the server details view, under the **Migration dashboard**, agentless servers that are replicated through snapshot shipping have an additional **Lifecycle** step – **Not started.**

1. Similarly, in the server details view, under the **Migration dashboard**, the **Data replication status** box shows the **Replication type** as **Snapshot shipping**. 