

# Auditability
<a name="sec-auditability"></a>

Every significant decision made by AVX — triage classification, booking action, escalation — is logged with the full set of inputs and context that produced it. The audit log is the evidentiary record that allows an automotive organization to reconstruct why a particular recommendation was made, which model generated it, and what data it was grounded in.

## What every classification and booking decision logs
<a name="sec-audit-what-is-logged"></a>

The AVX supervisor logs the following fields for every classification event (triage output) and every booking action (STAR service request creation):


| Field | Content | 
| --- | --- | 
|  `session_id`  | Unique AgentCore session ID, scoped to `{tenantId}/{sub}`. | 
|  `tenant_id`  | Tenant identifier from the validated Cognito claim. | 
|  `event_type`  | One of `triage_classification`, `booking_ticket_created`, `escalation_initiated`. | 
|  `inputs_consulted`  | Structured summary of the data inputs read before the decision: DTC codes and severity assignments, telemetry values compared to thresholds, recall IDs open at classification time, and tenant policy override keys that fired. | 
|  `tool_calls`  | Ordered list of tool invocations issued during the decision turn, each with the tool name, input parameters (PII-redacted), response status, and latency in milliseconds. | 
|  `tenant_config_version`  | Version identifier of the tenant config record loaded at session start. Allows post-incident reconstruction of which policy overrides were active. | 
|  `model_ids`  | Model ID strings of every Bedrock model invoked in the session up to the event: the supervisor LLM and the triage classifier LLM if different. | 
|  `prompt_hash`  | SHA-256 hash of the system prompt (persona \+ tenant policy injection) active at the time of the decision. Allows detection of prompt drift between sessions. | 
|  `classification_result`  | For triage events: the `P0`–`P3` level, reason trace, and recommended action. For booking events: the STAR ticket ID and the booking phase (`ticket_recommend`, `slot_propose`, `dms_book`). | 
|  `timestamp_utc`  | ISO-8601 timestamp in UTC. | 

These fields are written to a structured CloudWatch Logs log group (`/cvx/{stage}/audit/{tenantId}`) with a minimum retention of 90 days. The log group is separate from the application debug log group and is subject to its own IAM access policy — read access is restricted to the tenant’s designated audit principals, not to the broader engineering team.

## Log immutability
<a name="sec-audit-immutability"></a>

Audit logs written to CloudWatch Logs are exported to an S3 audit bucket with Object Lock enabled in Compliance mode. Once written, a log record cannot be deleted or overwritten for the duration of the retention period, regardless of IAM permissions. This provides tamper-evident storage suitable for regulatory review.

## CloudTrail complement
<a name="sec-audit-cloudtrail"></a>

The CloudWatch audit log captures application-level decisions. AWS CloudTrail captures the corresponding control-plane and data-plane API calls — DynamoDB reads, Bedrock Retrieve calls, AgentCore Memory operations — with the IAM principal, source IP, and request ID for each call. The two streams together allow a complete reconstruction of any AVX session from the identity layer down to the data access layer.

For CloudTrail data-event configuration in the cross-account grant topology, see [CloudTrail data-event audit](sec-cross-account-grants.md#sec-cloudtrail-data-events).