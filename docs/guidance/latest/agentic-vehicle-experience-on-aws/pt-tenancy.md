

# Multi-tenancy model
<a name="pt-tenancy"></a>

## Tenancy as a first-class dimension
<a name="pt-tenancy-first-class"></a>

AVX treats tenancy as a first-class architectural dimension, not an afterthought. One AVX deployment serves multiple automotive organizations — a fleet operator, an OEM, a rental company, or any combination — with complete isolation between them. Tenant identity is resolved at session start and carried through every downstream call in the agent mesh.

The current tenant deployment is fleets-first: initial deployments target commercial fleet operators. The architecture supports fleet, OEM, and rental tenants equally; all three can be deployed and configured independently.

**Note**  
 **Cards-first user experience.** AVX prioritizes asynchronous card-driven interactions over conversational voice or chat. Findings (diagnoses, alerts, insights) are proactively pushed to the customer’s device as cards, and the customer interacts with them on their own timeline by tapping a call-to-action button. This is especially valuable for fleet operators, where a fleet\_owner persona may review dozens of vehicle Findings across a cohort without waiting for a voice call. See [Card-Driven Delivery](ap-card-driven-delivery.md) for the design-level card pattern and rendering contract.

## Tenant resolution at session start
<a name="pt-tenant-resolution"></a>

Tenant identity is resolved from verifiable session signals before the supervisor agent receives any customer input. Two paths, one per channel:

Voice session  
The companion app opens the voice session with the user’s Cognito token and the tenant, vehicle and driver at session start, as AgentCore custom headers or a `session.start` message.

Text and web chat  
 `POST /assistant/chat` sits behind a Cognito authorizer, and the Lambda function takes the tenant from the caller’s `custom:tenantId` claim before the session reaches the supervisor.

 `/escalate` checks the caller’s `custom:tenantId` claim again before it opens a Connect contact.

Once resolved, the `tenantId` is set on the session context and is immutable for the lifetime of the session. It cannot be overridden by the customer, the LLM, or any downstream tool call.

## Tenant configuration record
<a name="pt-tenant-config"></a>

A tenant is defined by a single JSON configuration record stored in DynamoDB. The record encodes every tenant-specific parameter; no code changes are required to onboard, modify, or disable a tenant. The table key is `tenantId` (a short slug, such as `fleet-ops-north` or `oem-brand-us`), and versioning is immutable — updates create a new version row so that every triage decision and booking action can reference the exact policy version in effect at the time.

The configuration record is cached in ElastiCache with a 60-second TTL. Reads go to the cache first and fall back to DynamoDB, keeping per-session latency below 5 ms for the config fetch.

A tenant configuration record covers the following concern areas:


| Configuration area | What it controls | 
| --- | --- | 
| Identity and identity provider | Caller resolution mode (`phone-lookup`, `account-number`, `sso`, `vin-prompt`); optional Cognito User Pool or OIDC endpoint for SSO tenants; consent requirements (SMS outreach). | 
| Branding and voice | Logo URL, primary and secondary colors, font, map style, and per-channel greeting copy (voice TTS, chat opener, companion-app hero text); Nova 2 Sonic voice profile and locale. | 
| Knowledge base | IDs of the shared KB (cross-tenant content such as NHTSA recalls and VSS catalog) and the tenant overlay KB (proprietary content such as fleet SLA documents, OEM service bulletins, rental policy). See [Knowledge and Grounding](knowledge-and-grounding.md) for the KB layout. | 
| Tenant-specific tools | Lambda ARNs of tenant-specific tools in `tenantSpecialists` (for example, a fleet SLA check or a rental swap-vehicle flow). Each persona’s built-in tools come from `PERSONA_TOOL_FACTORIES` in `agents/supervisor/persona_definitions.py`; to load the tenant’s tools as well, extend `build_supervisor` to read this list. | 
| Triage policy overrides | Tenant-specific thresholds for coolant temperature, tire pressure delta, and brake wear at each criticality level; escalation rules that trigger forced tier-2 transfer or roadside dispatch for specific classification outcomes. The `downgradeForbidden` flag prevents the LLM from overriding a deterministically computed P0 classification. | 
| Booking | Calendar slot proposal feed; DMS integration endpoint and provider. | 
| Escalation | Amazon Connect instance, chat contact flow and chat queue; optional P0 callback flow, queue and caller ID; `escalation.autoOpenHumanChatOnP0` and `escalation.autoRequestRoadsideOnP0`, both default `false`. | 
| Data policies | Audit log retention; PII redaction field list; per-session and monthly token budgets. | 
| Observability | CloudWatch log group prefix (default `/aws/vsa/{tenantId}`); metrics namespace; alarm SNS topic. | 
| Feature flags | Enable image input (Nova Pro vision); enable calendar slot proposal; enable DMS booking. | 

## Data isolation between tenants
<a name="pt-tenant-isolation"></a>

AVX enforces tenant isolation at multiple layers to ensure that data, content, and conversational context cannot cross tenant boundaries.

IAM conditions  
Every AWS API call that touches tenant-scoped data — DynamoDB reads, Bedrock Retrieve calls against the tenant overlay KB, Athena queries via Lake Formation — is issued with an IAM session policy that includes a condition key binding the call to the resolved `tenantId`. A session scoped to tenant A cannot issue a DynamoDB query or KB Retrieve call that returns tenant B’s records, even if the underlying Lambda execution role would otherwise permit it.

DynamoDB partition-key prefixing  
All DynamoDB tables used by AVX use a composite primary key in which the first element is a tenant-prefixed key (for example, `{tenantId}#{vin}` for vehicle state records, `{tenantId}#{sessionId}` for session context). Queries issued in a session always include an equality condition on the tenant prefix, preventing cross-tenant row access.

Separate Knowledge Bases per tenant  
The tenant overlay Knowledge Base is a separate Bedrock Knowledge Base per tenant. Cross-tenant KB reads are structurally impossible: the tenant config record carries only the IDs of the shared and tenant-overlay KBs that belong to that tenant.

Observability isolation  
CloudWatch logs and metrics are dimensioned by `tenantId`. A fleet operator’s operations team can be granted read access to their tenant’s log groups and metric namespace without visibility into any other tenant’s operational data.

## Config-driven tenant onboarding
<a name="pt-tenant-onboarding"></a>

Onboarding a new tenant requires no code changes to AVX. The operator:

1. Provisions the tenant overlay Knowledge Base in the ADP account and syncs the tenant’s proprietary content (SLA documents, brand-specific service bulletins, rental policies). See [Knowledge and Grounding](knowledge-and-grounding.md) for KB provisioning guidance.

1. Authors the tenant configuration record (JSON) using the schema described in [Tenant configuration record](#pt-tenant-config) and writes it to DynamoDB `vsa-tenant-config` with `status: active`.

1. Sets `custom:tenantId` on the tenant’s users in the Cognito user pool, and wires the tenant’s Connect instance, chat flow and queue into its config (see [Tenant-branded contact flows](connect-tenant-branded-flows.md)).

1. (Optional) Registers any tenant-specific tools as Lambda ARNs in the config’s `tenantSpecialists` list.

Once the config record is active and the ElastiCache TTL has expired (up to 60 seconds), new sessions for that tenant resolve correctly without any Lambda redeployment or CDK synthesis. The config version stamp ensures the policy applied at onboarding is auditable.