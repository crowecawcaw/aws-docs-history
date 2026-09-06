

# Customer pattern catalog
<a name="ae-pattern-catalog"></a>

This catalog grows over time. Each entry documents one recurring customer question and the AWS architectural answer for building on top of ADP’s governed data products. The structure is intentionally stable — new entries append at the end without changing earlier ones.

## Pattern: Grounding a customer-facing agent on governed vehicle knowledge
<a name="pattern-grounding-a-customer-facing-agent-on-governed-vehicle-knowledge"></a>

Context  
An automotive OEM or fleet operator wants to deploy a conversational AI agent that can answer customer or driver questions about vehicle issues, recalls, DTC codes, warranty coverage, and service procedures. The agent must draw from governed, up-to-date vehicle knowledge rather than language model training data alone — and the operator must be able to tell, from the agent’s own responses, whether a given answer was retrieved from the knowledge base or recalled from the model.

What customers ask  
How do we connect an AI agent to ADP’s `vehicle_knowledge_base` data product across an AWS account boundary? How do we prevent the agent from presenting model-recalled facts as if they came from a governed knowledge source?

The AWS pattern  
The agent is built with the Strands agentic framework backed by Amazon Bedrock (a cross-region inference profile for a Claude model). A `retrieve` tool calls Amazon Bedrock’s Knowledge Base Retrieve API against ADP’s `vehicle_knowledge_base` product, hosted in the ADP account. Three environment variables configure the cross-account connection: the knowledge base ID, the ADP region, and the ADP account ID (which can be resolved via STS `GetCallerIdentity` at startup rather than hardcoded). The account ID is treated as sensitive configuration and excluded from log output. The agent’s system prompt encodes a grounding-transparency rule as a hard constraint: any factual answer given without calling a KB-backed retrieval tool in the same turn must be explicitly flagged as non-grounded — a short disclosure phrase that appears in the response text itself. The agent narrates tool results; the tools make grounding decisions.

Demonstrated in CVX  
The Connected Vehicle Experience (CVX) accelerator (`agents/supervisor/supervisor.py` and `agents/supervisor/config.py`) demonstrates this exact pattern — cross-account Bedrock KB Retrieve wired through three environment variables, a grounding-transparency hard rule in the system prompt, and Strands \+ Amazon Bedrock as the agent runtime. This is a reference implementation of the pattern; it is not the only way to build an agent on ADP.

Open extensions  
A production deployment of this pattern would also address: agent session management and memory (per-session vs. per-tenant memory, long-term memory for returning customers), multi-product retrieval (joining `service_records` and `customer_360` alongside the knowledge base for richer context), retrieval-quality tuning (chunk size, embedding model, hybrid retrieval), observability for grounded vs. non-grounded answer rates, and cost attribution per consuming team via DataZone subscription metadata.

## Pattern: Natural-language business queries over governed automotive data
<a name="pattern-natural-language-business-queries-over-governed-automotive-data"></a>

Context  
An automotive OEM’s business and executive stakeholders need to answer operational questions — fleet health trends, OTA campaign outcomes, customer service gaps — without analyst support or SQL knowledge. The underlying data exists in the ADP lake but is inaccessible to non-technical users through standard Athena interfaces.

What customers ask  
How do we give a business executive self-service access to ADP’s governed data products for ad hoc questions in plain English, without bypassing the access controls that DataZone enforces?

The AWS pattern  
Amazon Quick Suite (including Amazon Quick Desktop) connects to Amazon DataZone as a data source, inheriting DataZone’s subscription and access-control model. A business user who has been granted access to the relevant ADP consumer project through DataZone can ask natural-language questions; Quick Suite translates them to SQL against the underlying Athena tables and returns the result, using the schema metadata and descriptions ADP publishes when registering each product in the DataZone domain. The same `adp-{stage}-data-consumers` IAM Identity Center group that governs Athena and notebook access also governs Quick Suite subscription eligibility — one access-control model serves all consumption patterns. Example queries answerable through this pattern: "Which vehicles have degraded battery SoH after winter?" (requires `vehicle_telemetry_aggregated` \+ `vehicle_identity`); "Which customers have open service records and unresolved OTA failures?" (requires `customer_360` \+ `service_records` \+ `ota_campaigns`).

Demonstrated in [repo]  
Not yet demonstrated in a reference implementation as a deployed Quick Suite configuration. The ADP data products (`vehicle_telemetry_aggregated`, `customer_360`, `service_records`, `ota_campaigns`) required by the example queries are deployed and verified as part of the standard ADP foundation deploy — the Quick Suite subscription layer is the unimplemented consumer step.

Open extensions  
A production deployment would need IAM Identity Center group-to-Quick-reader-group mapping, DataZone producer-to-consumer subscription approvals for each product the executive team needs, a naming and description review of each data product’s DataZone catalog entry to ensure Quick Suite can generate accurate natural-language summaries, and cost allocation tags on the Athena workgroup used by Quick Suite queries. The pattern also extends naturally to scheduled reports (Quick Suite can push refreshed answers to email or Slack on a schedule) without changing the underlying data subscription model.

## Pattern: Proactive executive briefing agent, not a scheduled dashboard export
<a name="pattern-proactive-executive-briefing-agent-not-a-scheduled-dashboard-export"></a>

Context  
An automotive OEM’s executives and directors want a recurring answer to the same handful of operational questions every day or every week — fleet health, warranty exposure, OTA campaign outcomes — without opening a dashboard and re-deriving what changed since last time. A traditional BI approach schedules the same visual for email delivery on a cadence; the executive still has to look at it and notice the change themselves.

What customers ask  
Can we get a standing morning or weekly briefing that tells us what changed and what needs our attention, instead of a dashboard we have to remember to check?

The AWS pattern  
Amazon Quick Desktop’s scheduled-agent capability lets an executive describe a recurring briefing once, in plain English — the questions to check, the cadence, and the delivery channel. The agent queries the relevant ADP governed data products through the same DataZone-governed Athena access as the ad hoc natural-language pattern, but on a schedule rather than on demand, and compares each cycle’s answer to the prior cycle so the delivered brief leads with what changed rather than repeating the full picture every time. The underlying data-access and governance model is identical to the ad hoc pattern; what changes is that the consumer is a standing scheduled agent instead of a person asking a question in the moment.

Demonstrated in [repo]  
Not yet demonstrated in a reference implementation as a deployed scheduled-agent configuration. The pattern depends on the same ADP data products already deployed and verified for the ad hoc natural-language-query pattern above — the scheduled-agent and comparison-against-prior-cycle layer is the unimplemented consumer step.

Open extensions  
A production deployment would need the same IAM Identity Center / DataZone subscription prerequisites as the ad hoc pattern, plus a data-freshness contract per product (a weekly OTA-campaign briefing needs data no staler than the executive’s tolerance for "last week’s news"), a policy for how many prior cycles the agent retains for comparison, and a decision on delivery channel per executive (email, Slack, or another surface they already check first).