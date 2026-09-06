

# AGENTCOST06-BP01 Implement lightweight discovery and registry for cost-effective collaboration
<a name="agentcost06-bp01"></a>

 Deploying service-mesh infrastructure for agent discovery carries a fixed cost that doesn't scale down when traffic does. You can keep registry cost proportional to fleet size through managed discovery through tool exposure, consumption-based registries, and aggressive metadata caching. 

 **Desired outcome:** 
+  You use consumption-based infrastructure for agent discovery, charging only for actual operations. 
+  You serve repeated capability lookups from a metadata cache instead of the database. 
+  You keep costs proportional to fleet size through efficient indexing and batched writes. 
+  You monitor per-query costs so they don't grow silently as the fleet expands. 

 **Common anti-patterns:** 
+  Deploying managed service mesh for simple capability lookups when a NoSQL database with consumption-based pricing would suffice. 
+  Making repeated registry lookups for the same agent metadata on every invocation without caching. 
+  Using full-table scans instead of targeted queries with proper indexes, consuming unnecessary read capacity. 
+  Operating agent discovery registries without monitoring per-query costs, which scale with fleet size and grow silently as the fleet expands. 

 **Benefits of establishing this best practice:** 
+  Consumption-based registry avoids fixed infrastructure overhead, charging only for actual read and write operations. 
+  Metadata caching serves repeated capability lookups without database queries, avoiding most read charges. 
+  Batched capability updates reduce write costs by accumulating changes into single operations. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Agent discovery through [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) removes the need for custom registry infrastructure in many scenarios. When you expose specialized agents as tools through Gateway's MCP server capabilities, other agents discover and invoke them without a separate registry. AgentCore Gateway handles credential exchange, protocol translation, and composition of multiple tools into unified endpoints under consumption-based pricing. This approach fits when agents primarily interact through tool invocation patterns and Gateway's built-in discovery semantics match your collaboration requirements. 

 When those conditions don't hold, you can build a custom lightweight registry using [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) with on-demand capacity mode and global secondary indexes for filtered capability queries. Index agent capabilities by category and task type so discovery queries read only relevant partitions rather than scanning the full registry. As agent fleets grow, inefficient discovery queries that scan entire capability sets multiply costs and degrade latency at the same time, so targeted queries through global secondary indexes become the operational baseline, not an optimization. 

 Metadata caching helps you cost optimize a registry designed for scalability. A capability lookup that hits the cache costs effectively nothing, while a lookup that falls through to DynamoDB incurs a read charge. Configure TTLs that reflect how often capability metadata actually changes (typically hours, not seconds), and use the persistent filesystem on [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) to cache registry metadata across session stop and resume cycles. 

 Monitoring becomes increasingly important, as registry read costs scale with query volume, and per-query charges accumulate as the fleet grows. [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and Amazon CloudWatch track read costs, cache hit rates, and discovery API call volumes, with alarms for anomalous patterns before they become a line item worth investigating. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Evaluate Gateway-based discovery first:** Determine whether [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) semantic tool selection meets your discovery requirements. If so, expose agents through Gateway's MCP server capabilities and avoid the custom registry entirely. 

1.  **Use consumption-based storage with efficient indexing:** For custom registries, use [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) with on-demand capacity mode. Design a global secondary index on capability-category so filtered queries by capability type or task category read only relevant partitions. 

1.  **Deploy a metadata cache:** Configure TTLs appropriate to how often capability metadata changes, and use the [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) persistent filesystem to cache across session cycles. 

1.  **Monitor registry costs:** Track read costs and cache hit rates using [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and Amazon CloudWatch, with alarms for anomalous patterns. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [AGENTCOST02-BP03 Use intelligent caching to reduce redundant model invocations](agentcost02-bp03.html) 
+  [AGENTCOST06-BP02 Cost optimize versioning and deployment through efficient artifact management](agentcost06-bp02.html) 
+  [AGENTCOST06-BP03 Design cost-efficient initialization through warm pools and caching](agentcost06-bp03.html) 

 **Related documents:** 
+  [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) 
+  [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) 

 **Related videos:** 
+  [AWS 2025 - AgentCore Deep Dive: Gateway](https://www.youtube.com/watch?v=atWXM5lziY8) 
+  [AWS 2025 - AgentCore Registry: Discover, Govern, and Reuse AI Agents at Scale](https://www.youtube.com/watch?v=rIcOJrE-fTk) 

 **Related examples:** 
+  [GitHub: awslabs/amazon-bedrock-agentcore-samples - Gateway tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway) 

 **Related services:** 
+  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 