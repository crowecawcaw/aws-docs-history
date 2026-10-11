

# Security Planning
<a name="plan-security-planning"></a>

Security for a multi-tenant, voice-capable AI platform requires deliberate planning across several dimensions before deployment begins. The full security design — covering multi-tenant Cognito authentication, tenant isolation via IAM conditions and DynamoDB partition-key prefixing, cross-account grant model, PII handling, consent and redaction, and the P0 safety guardrail — is covered in the [Security](security.md) chapter.

Key planning decisions to address before your first deployment:
+  **Tenant isolation boundary** — decide whether tenants share an AWS account (with logical isolation) or use separate accounts (with account-level isolation for highest-compliance deployments). The AVX CDK supports both topologies via parameterized context.
+  **PII consent and data residency** — identify which chat transcripts and session data are subject to consent requirements in your jurisdiction. AVX defaults to PII redaction in logs. A tenant’s data stays in the Region where AVX is deployed; to keep data in another Region, deploy AVX there.
+  **Cross-account grant scope** — if ADP is deployed in a separate account from AVX, plan the Lake Formation cross-account grants and Bedrock Knowledge Base resource policies before deploying. These grants are parameterized inputs to the AVX CDK stacks.
+  **P0 safety guardrail** — the deterministic P0 safety guardrail (stop-driving / brake failure / airbag fault) cannot be overridden by LLM output: the stop-driving instruction is always delivered, and the driver is one tap from a human agent (automatic if you enable `escalation.autoOpenHumanChatOnP0`). Confirm your Amazon Connect escalation queues and tier-2 staffing are in place before enabling voice intake for safety-critical vehicle contexts.

For the complete security implementation guide, see [Security](security.md).