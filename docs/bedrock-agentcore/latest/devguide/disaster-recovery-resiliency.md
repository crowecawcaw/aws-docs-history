

# Building custom disaster recovery for Amazon Bedrock AgentCore
<a name="disaster-recovery-resiliency"></a>

 [Amazon Bedrock AgentCore](what-is-bedrock-agentcore.md) provides managed serverless hosting for AI agents. The [Amazon Bedrock SLA](https://aws.amazon.com/bedrock/sla/) applies to AgentCore, but it measures availability in each AWS Region separately. Recovery across Regions is yours to design and operate.

If your agents serve regulated industries or mission-critical workflows, you might need cross-Region disaster recovery (DR) with a bounded recovery time objective (RTO) and recovery point objective (RPO). The following pages show you how to build DR for AgentCore Runtime, AgentCore Memory, and failover routing, and for the regional dependencies that they use: identity, gateways and their targets, policy engines, and observability. They don’t cover every AgentCore component.

**Topics**
+ [What AgentCore manages and what you own](#managed-vs-customer-owned)
+ [The architecture: warm standby](#architecture-warm-standby)
+ [Replicating AgentCore Memory across Regions](disaster-recovery-memory.md)
+ [Operating disaster recovery: detection, response, and recovery](disaster-recovery-operate.md)
+ [Validating disaster recovery: checklist, go-live ramp, and failback](disaster-recovery-validate.md)

## What AgentCore manages and what you own
<a name="managed-vs-customer-owned"></a>

Within a Region, AgentCore manages the infrastructure. On the default microVM compute type, each session runs in its own microVM and scales automatically. On the Instances compute type, each session runs on an Amazon EC2 instance from a capacity provider in your account, so your account’s EC2 quotas also apply. If your runtimes connect to a VPC, place them in at least two private subnets in different Availability Zones.

Across Regions, you own the deployment, the health detection, the routing, and the failover decision. The following table shows what that means for each component. Check [Supported AWS Regions](agentcore-regions.md) for both Regions of your pair, because availability differs by component.


| Component | Coverage in these pages | What you own for DR | 
| --- | --- | --- | 
|  **AgentCore Runtime**  |  [Full guidance](disaster-recovery-operate.md)  | A standby runtime with matching endpoints and quotas, plus the routing and the agent invoker (the request layer you build between clients and AgentCore). On Instances, also the capacity provider and anything on its volumes. | 
|  **AgentCore Memory**  |  [Full guidance](disaster-recovery-memory.md)  | Long-term memory (LTM) and short-term memory (STM) replication, and failback. | 
|  **AgentCore Identity**  |  [Checklist of what to re-create](disaster-recovery-validate.md#dr-checklist)  | Credential providers, callback URLs, workload identities, and the token vault key in the standby. | 
|  **AgentCore Gateway**  |  [Checklist of what to re-create](disaster-recovery-validate.md#dr-checklist)  | Gateways, targets, rate limits, and inbound authorizers in the standby. | 
|  **Policy in AgentCore**  |  [Checklist of what to re-create](disaster-recovery-validate.md#dr-checklist)  | An equivalent policy engine for every gateway that references one. | 
|  **AgentCore Observability**  |  [Checklist of what to set up](disaster-recovery-validate.md#dr-checklist), and [alerts](disaster-recovery-operate.md#dr-alerts)  | Transaction Search, log delivery, trace destinations, and alarms in each Region. | 
|  **AgentCore Built-in Tools**  |  [Quotas](#dr-service-limits) only | Custom Browser and Code Interpreter resources, and their session quotas, in the standby. | 
|  **Other components**  | Not covered | AgentCore Evaluations, AgentCore payments, AgentCore harness, AgentCore optimization, AWS Agent Registry, and Web Search Tool. Plan their recovery separately. | 

**Important**  
 **Cross-Region inference (CRI) is not disaster recovery.** For AgentCore Memory, Policy in AgentCore, and AgentCore Evaluations, [CRI](cross-region-inference.md) changes where an inference request is processed, not where data is stored, and it replicates no resource. For Policy in AgentCore, only natural language policy generation uses inference. Policy management and authorization decisions stay in the Region that you call. Under global CRI, policy generation and Evaluations inference requests might be processed outside that Region’s geography. See [Global cross-region inference for Policy in AgentCore](cross-region-inference.md#cross-region-inference-policy-global) and [Global cross-region inference for AgentCore Evaluations](cross-region-inference.md#cross-region-inference-evaluations-global).

## The architecture: warm standby
<a name="architecture-warm-standby"></a>

The [four DR strategies](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html) in the *Disaster Recovery of Workloads on AWS: Recovery in the Cloud* whitepaper trade recovery time against cost.

![Comparison of four disaster recovery strategies by typical recovery time and relative cost](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/disaster-recovery-strategy-comparison.png)


The following table lists the same comparison as text.


| Strategy | Typical RTO | Relative cost | What recovery involves | 
| --- | --- | --- | --- | 
| Backup and restore | 24 hours or less | Lowest | Slowest recovery. You restore infrastructure, code, and state after the disruption. | 
| Pilot light | Tens of minutes | Low | You deploy and scale missing services before the standby serves traffic. | 
| Warm standby | Minutes | Medium | The standby is functional and continuously validated. The architecture here uses it. | 
| Multi-site active/active | Potentially zero | Highest | You synchronize state and resolve write conflicts between Regions. | 

Active-active needs conflict resolution. If two Regions accept writes independently, the agent in one Region doesn’t know what the agent in the other Region just discussed, so the two Regions hold conflicting versions of the same conversation. Warm standby avoids that by serving production from one Region at a time. It follows Well-Architected [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_disaster_recovery.html).

### How the architecture works
<a name="_how_the_architecture_works"></a>

The complete agentic solution runs in two AWS Regions: the Runtime, its Memory, and every regional dependency that it calls. In the example, the primary is us-west-2 and the standby is us-east-1. Production uses the primary. To fail over, you *promote* the standby: you make it the Region that serves production. The standby receives only synthetic canary traffic, which validates the application path but doesn’t pre-warm the microVMs that users get after failover.

The following diagram shows one implementation. In it, clients resolve one DNS name through a Route 53 failover record, and an ARC Region switch plan flips the record’s health checks to move traffic. Each Region runs the same stack: an agent invoker on Lambda or Amazon ECS, AgentCore Runtime with the same agent version, a gateway with its targets, rate limits, and inbound authorizer, an optional policy engine, AgentCore Identity, and single-Region AWS KMS keys. A canary Lambda function, CloudWatch alarms, and an Amazon SNS topic watch each Region. The primary Memory streams LTM changes through Kinesis to a replication Lambda function, which writes to the standby Memory. A reverse stream stays off until promotion. Replicated storage of your choice in both Regions holds the active-Region record, record-ID mappings, deduplication keys, and changes that wait for replay or review. The diagram omits the public entry point in front of each invoker, which the [disaster recovery checklist](disaster-recovery-validate.md#dr-checklist) covers.

![Warm standby for Amazon Bedrock AgentCore: Route 53 failover record, ARC Region switch plan, agent invoker, AgentCore Runtime, AgentCore Gateway, and AgentCore Memory replication](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/disaster-recovery-warm-standby-architecture.png)


Its parts work as follows:
+  **Routing.** Route 53 failover records send clients to the agent invoker in one Region. An Amazon Application Recovery Controller (ARC) [Region switch](https://docs.aws.amazon.com/r53recovery/latest/dg/region-switch.html) plan creates a health check for each Region’s record. When you execute the plan, it marks one healthy and the other unhealthy, so you don’t edit Route 53 records by hand. Plan execution runs in each Region, so it doesn’t depend on the Region you’re leaving. The plan only flips health checks, which is a Route 53 data plane action, so it doesn’t depend on the Route 53 control plane in us-east-1 either. Set a TTL of 60 seconds or less on non-alias failover records.
+  **Agent invoker.** Clients call AgentCore only through an invoker that you own. Each invoker sends requests to the Region named in the active-Region record: a small record that you update with a higher version number when you promote the standby. Invokers therefore switch within seconds instead of waiting for DNS caches to expire. See [Response: agent invoker layer](disaster-recovery-operate.md#response-agent-invoker-layer).
+  **Canary.** A synthetic probe in each Region provides the external health signal for failover decisions. See [Detection: synthetic canary](disaster-recovery-operate.md#detection-synthetic-canary).
+  **Memory replication.** You choose what to replicate: LTM changes stream to a Memory in the standby, STM turns are written to both Memories, or both. See [Replicating AgentCore Memory across Regions](disaster-recovery-memory.md).
+  **Region pair.** AgentCore Memory, not Runtime, usually limits which Region pairs you can use. If you use Instances compute or AgentCore payments, they narrow the choice further, because they’re available in even fewer Regions.

 **Measuring RTO.** Measure RTO from the first failed canary probe to the standby serving production. That span includes detection, your decision to promote the standby, and the switch itself. The decision usually takes longest. If your RTO is shorter than the time you need to decide, automate the whole promotion runbook in order, with the Memory steps (stop copying Memory to the standby, and start capturing the standby’s writes for failback) before traffic moves. Give the automation a guard that an operator sets for a planned change and that expires on its own, so that a deployment can’t trigger a promotion and a forgotten guard can’t block one. Don’t trigger only the Region switch from an alarm. It moves DNS but not the active-Region record that invokers follow, so traffic doesn’t fail over.

### Session storage and file systems
<a name="dr-session-storage"></a>

Runtime file systems don’t replace AgentCore Memory for DR. Plan for each one based on what it survives. The [file system options](runtime-filesystem-configurations.md) depend on the compute type:
+  **Managed session storage** (Preview, microVM runtimes) belongs to one session of one agent runtime, so the standby can’t read it. It holds up to 1 GB per session, is deleted after 14 days without an invocation, and is reset whenever you deploy a new agent runtime version. Checkpoint anything that must survive, as the session runs, to replicated storage of your choice, such as Amazon S3 with Cross-Region Replication.
+  **Capacity provider volumes** (Instances runtimes) persist across session stop and resume, but you can’t snapshot or export them. Build your agent to copy anything that must survive to the same checkpoint store.
+  **Amazon S3 Files** mounts are backed by an S3 bucket, which you can copy to the standby with S3 Cross-Region Replication. Run S3 Batch Replication once to copy objects that already exist.
+  **Amazon EFS** [replication](https://docs.aws.amazon.com/efs/latest/ug/efs-replication.html) aims to copy changes within 15 minutes for most file systems, and the copy isn’t consistent to a single point in time. The copy in the standby is read-only until you delete the replication configuration, which the [incident runbook](disaster-recovery-operate.md#incident-runbook) does at failover.

### Service quotas that limit a failover
<a name="dr-service-limits"></a>

At failover, the standby must absorb all production traffic at once. The following AgentCore quotas usually limit how fast it can. For current values, see [Quotas for Amazon Bedrock AgentCore](bedrock-agentcore-limits.md).
+  **Active session workloads per account.** Caps how many sessions the standby can run at once. The default is lower outside us-east-1 and us-west-2.
+  **New Runtime session creation rate.** Shared across every endpoint in the account and Region. On microVM compute, it’s the tightest Runtime quota when users reconnect after failover.
+  **Data plane API request rate.** Shared by `InvokeAgentRuntime` and the other data plane APIs. Invoker retries during a burst count against it.
+  **Memory record read rates** (`RetrieveMemoryRecords` and `ListMemoryRecords`). The standby’s LTM read rate. Every session that reloads its memory after failover uses it. For STM, `ListEvents` has its own quotas.
+  **Gateway tool call rates.** Can run out before the Runtime quotas when agents call tools right after failover.

Size the standby for 100% of production traffic, and request increases in the standby before you need them, because requests can take time. Some increases, such as Browser and Code Interpreter session quotas, need an AWS Support case.