

# What AVX Is
<a name="overview-what-cvx-is"></a>

AVX is the channel layer in a three-layer automotive data portfolio on AWS:


| Layer | Guidance | What it does | 
| --- | --- | --- | 
| Operational |  [Connected Mobility on AWS (CMS)](https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws)  | How the automotive organization runs the vehicle — real-time ingest, fleet operations UI, FleetWise telemetry, DynamoDB, MSK, Apache Flink | 
| Analytical |  [Automotive Data Platform on AWS (ADP)](https://github.com/aws-solutions-library-samples/guidance-for-automotive-data-platform-on-aws)  | How the automotive organization analyzes its data — governed lake, data products, DataZone catalog, Bedrock Knowledge Base | 
|  **Channel**  |  **AVX (this guidance)**  |  **How the automotive organization talks to customers — agentic AI, voice, multi-channel, multi-tenant**  | 

Each layer is independently deployable. Each delivers value on its own. Together they are additive: AVX draws live vehicle state from CMS and grounding data from ADP but takes no hard code or runtime dependency on either — the relationship is a documented subscription pattern.

AVX divides into two tiers. The **Tier 1 conversational layer** is the supervisor agent running in two AgentCore runtimes — one for voice, one for text — that responds to customers in real time by dispatching tools and synthesizing grounded responses. The **Tier 2 autonomous agent platform** is nine specialized agents (four loyalty-flywheel agents for vehicle owners and five Fleet Intelligence agents for fleet operators and product engineers) that run on schedules, events and requests, reason over ownership and fleet data without a customer waiting, and write evidence-carrying Findings to a shared DynamoDB table. The **outreach broker** reads the Findings stream and selects the delivery channel — push notification, in-app card, Connect voice, or SMS — applying consent, quiet-hours, frequency, and priority rules before dispatching. Tier 1 tools read Tier 2 Findings directly, so analysis that appeared in a proactive card is also available inside a live conversation without re-running the reasoning. See [Agentic Architecture](agentic-architecture.md) and [Tier 2 Autonomous Agents](avx-agent-pattern.md) for the design of each tier and its agents.

## Composition Over CMS and ADP
<a name="overview-architecture-composition"></a>

AVX composes data and capabilities from both foundation guidances:
+  **From CMS**: live vehicle telemetry (Redis LKS — sub-millisecond reads), DTC history, trip records, safety events, service history, and the escalation path to Amazon Connect.
+  **From ADP**: Vehicle Identity Graph (VIN decode and vehicle attributes), Parts Catalog (part numbers and pricing), Service Network (dealer and service center directory), Vehicle Lifecycle (warranty coverage), and the Bedrock Knowledge Base (DTC guides, technical service bulletins, NHTSA recalls, owner manuals, and service policy).

The agentic layer itself runs in the AVX account via **Amazon Bedrock AgentCore** — a managed runtime for hosting Strands-based agents. The supervisor agent delegates to specialist sub-agents through a tool-call mesh, grounding each answer in the appropriate data source before responding.

## Amazon Connect as the Contact Center Channel
<a name="overview-amazon-connect"></a>

Amazon Connect handles voice and chat channels. A Connect contact flow authenticates the caller, resolves them to a vehicle and tenant, and routes the session to the AVX supervisor agent via Lambda. For safety-critical situations (P0 — stop-driving events), escalation to a human tier-2 agent is mandatory and cannot be suppressed by the LLM. Tier-2 agents receive a pre-populated context view — vehicle state, triage classification, conversation transcript, and recommended action — so they can continue the conversation without re-collecting information from the customer.