

# PII, consent, and log redaction
<a name="sec-pii-consent"></a>

AVX handles personally identifiable information — caller identity, vehicle location, call recordings, and conversation transcripts — as regulated data. The handling posture is: collect the minimum required for service delivery, redact by default in logs, and gate session recordings on explicit per-tenant consent configuration.

## PII redaction in logs
<a name="sec-pii-redaction"></a>

AVX Lambda handlers and the AgentCore supervisor follow a redact-by-default discipline:
+ Phone numbers and account IDs extracted during caller resolution are masked in all CloudWatch log messages. Logs reference the resolved `sub` (Cognito subject) and `tenantId` rather than the raw contact identifier.
+ Vehicle location coordinates (latitude/longitude) from live telemetry are never written to application logs. The AgentCore supervisor prompt instructs the model to omit raw coordinates from any text it generates; coordinate data is consumed by tool logic and surfaced only as a human-readable location description (city/region level or service-center proximity, not GPS-exact).
+ Transcripts of Connect chats are stored in Connect’s managed storage. AVX does not copy raw transcript content to application logs; references in logs use the session ID only.

## Data residency
<a name="sec-consent-config"></a>

A tenant’s data lives in the Region where AVX is deployed; no tenant setting moves it. To keep a tenant’s data in another Region, deploy AVX in that Region.