

# Persona and tenant interaction
<a name="pt-persona-tenant-interaction"></a>

Persona and tenant are orthogonal dimensions but they interact at session initialization. The supervisor’s system prompt is assembled from three inputs:

1.  **Hard rules** — immutable safety and grounding rules prepended by `build_system_prompt` regardless of persona or tenant: triage before narrating, retrieve before citing, P0 always delivers the stop-driving instruction and offers a human handoff, LLM cannot downgrade a deterministic classification.

1.  **Persona body** — the role framing, tool guidance, and behavioral instructions for the inferred persona, loaded from `PERSONA_PROMPTS` in `persona_definitions.py`. Each prompt template receives `{tenant_display}`, `{vin}`, and `{persona_id}` substitutions so the agent is correctly introduced to the caller in the tenant’s brand voice.

1.  **Tenant config overlays** — the tenant’s `systemPromptId` field in the config record can reference a Bedrock prompt management entry that appends tenant-specific instructions (for example, fleet operator service-level priorities, rental company escalation scripts, or OEM brand-voice guidelines) without modifying the persona body or the hard rules.

This layered composition means that adding a new tenant does not require editing agent code. The tenant branding, policy, and routing are entirely config-driven. The persona bodies and hard rules are code-controlled and tested in the eval harness; tenant-specific prompt overlays are content-controlled and versioned in DynamoDB.

For grounding surface details — which ADP data products are loaded per persona, which Knowledge Base source categories are available, and how source-category filtering prevents cross-tenant and cross-persona content leakage — see [Knowledge and Grounding](knowledge-and-grounding.md).