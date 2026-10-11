

# Cost Model
<a name="plan-cost"></a>

## Overview
<a name="plan-cost-overview"></a>

AVX is a Bedrock-first, AgentCore-first workload. The cost profile differs materially from a traditional microservices deployment: the dominant cost drivers are model invocation tokens and voice-streaming minutes, not compute instance hours or database storage.

**Important**  
All figures in this section are **approximate estimates** at list price as of mid-2026, based on the AVX staging workload. They are illustrative of relative cost drivers and order-of-magnitude budgeting. Actual costs depend on your workload, region, negotiated pricing, and current AWS list rates. Verify against the [AWS pricing pages](https://aws.amazon.com/pricing/) for each service before committing to a deployment budget.

Use [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) and [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) to monitor and govern costs in your account. Set per-tenant budget alerts — AVX tenant configuration supports per-tenant monthly token caps and per-session token limits as a cost guardrail.

## Primary cost drivers
<a name="plan-cost-drivers"></a>

AVX cost is dominated by two usage dimensions. All other line items are minor by comparison at typical scale.


| Driver | What generates cost | Cost lever | 
| --- | --- | --- | 
|  **Bedrock model invocation — Claude Sonnet**  | Every text turn and every voice tool-dispatch triggers a supervisor agent synthesis pass. The first turn of a session is the most expensive: the persona-loader output (up to \~100 KiB of structured ADP data) flows into context before synthesis. Cost scales linearly with session volume × average turns × average context size. | Tune per-session token caps in tenant config. Cache persona context across turns using AgentCore Memory rather than re-loading on every tool call. Short sessions cost less than long sessions. | 
|  **Amazon Nova 2 Sonic — voice minutes**  | Bidirectional voice streaming is billed per minute of streamed audio. Average voice session duration at staging is approximately 8 minutes. Doubling average session duration approximately doubles this line item. | Set a per-session duration cap in the Connect contact flow. Use the P0/P1 handoff card to shorten sessions that need human handoff rather than continuing a long autonomous session. | 

## Illustrative monthly cost table
<a name="plan-cost-table"></a>

The table below uses the AVX staging workload as the reference scale: approximately 30,000 text turns per month, 3,000 voice sessions per month at approximately 8 minutes each, and 21,000 Bedrock Knowledge Base retrieve calls per month.


| AWS service | Cost dimensions | Approximate monthly range (estimate) | 
| --- | --- | --- | 
|  **Amazon Bedrock — Claude Sonnet** (supervisor agent) | \~120M input tokens \+ \~30M output tokens/month via cross-region inference profile | \~$700–$900 | 
|  **Amazon Bedrock — Amazon Nova 2 Sonic** (bidi voice) | \~24,000 voice-minutes/month via `InvokeModelWithBidirectionalStream`  | \~$400–$700 | 
|  **Amazon Bedrock AgentCore Runtime** (text \+ voice runtimes) | \~15,000 text invocations \+ \~3,000 voice sessions/month; billed on vCPU-seconds and memory-GB-seconds per invocation | \~$200–$400 | 
|  **Amazon Bedrock AgentCore Memory**  | \~18,000 session-init writes \+ \~500,000 retrieve operations/month; <1 GiB memory storage | \~$50–$150 | 
|  **Amazon Bedrock Knowledge Base — Retrieve** (cross-account) | \~21,000 `Retrieve` calls/month. Note: vector storage and ingestion costs are invoiced against the ADP account (KB owner), not the AVX account. | \~$5–$30 (AVX account only) | 
|  **Amazon Connect**  | Chat messages proportional to escalation volume; outbound voice minutes and a claimed number for the P0 callback | Usage-based; see [Amazon Connect pricing](https://aws.amazon.com/connect/pricing/)  | 
|  **AWS Lambda, API Gateway, Amazon CloudWatch, Amazon S3, AWS KMS**  | Supporting infrastructure — API calls, logging, key operations, query result storage | \~$5–$10 (aggregate) | 
|  **Cross-region data transfer**  | Athena result payloads and Nova 2 Sonic bidi audio (for cross-region staging topology only) | \~$2–$5 | 
|  **Amazon Bedrock Guardrails** (production recommended) | Optional at deployment — recommended for production deployments handling PII and safety-critical classifications. | Variable (add \~$0.75 per 1,000 text units if enabled) | 

 **Approximate monthly total at staging scale:** $1,400–$2,200.

**Note**  
The ADP-side cost of the cross-account Bedrock Knowledge Base — including Amazon S3 Vectors storage, embedding ingestion jobs, and KB API costs — is invoiced against the ADP account owner, not the AVX account. Budget for this separately when planning a split-account deployment. See the [ADP guidance](https://github.com/aws-solutions-library-samples/guidance-for-automotive-data-platform-on-aws) for ADP-side cost documentation.

## Amazon Connect cost considerations
<a name="plan-cost-amazon-connect"></a>

Amazon Connect usage cost in AVX is driven by escalation volume — the fraction of sessions that escalate from the agent to a tier-2 human agent. A well-tuned triage configuration (appropriate P0/P1/P2 thresholds) keeps escalation rates low and Connect costs proportionally small. P3 (monitor) and resolved P2 sessions complete within the AVX agent without consuming Connect agent-handle time.

Plan for:
+  **Chat messages** — billed per message for the Connect chat that every handoff opens.
+  **Voice minutes** — billed per minute for P0 callbacks to the assigned driver.
+  **Phone number** — a claimed number for the P0 callback’s caller ID is a recurring charge.

Consult the [Amazon Connect pricing page](https://aws.amazon.com/connect/pricing/) for current per-minute and per-message rates. Use the Connect cost estimation tool linked from that page to model your projected escalation volume.