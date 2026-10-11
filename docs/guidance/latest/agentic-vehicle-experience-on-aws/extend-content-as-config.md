

# Content-as-Config
<a name="extend-content-as-config"></a>

AVX uses file-based corpora: adding a new DTC guide, owner manual, or service bulletin requires editing files in `corpora/`, committing the change, and redeploying the full agent runtime. To update content without a code deploy, move the corpora into a Bedrock Knowledge Base backed by an S3 source bucket.

## Updating KB content without a code deploy
<a name="extend-content-kb-update"></a>

Once a Bedrock Knowledge Base is in place, the workflow to add or update a document is:

```
# 1. Upload the new or revised document to the KB source bucket
aws s3 cp my-new-dtc-guide.md \
  s3://<kb-source-bucket>/technical-reference/my-new-dtc-guide.md

# 2. Start a sync job to re-ingest the changed documents
aws bedrock-agent start-ingestion-job \
  --knowledge-base-id <kb-id> \
  --data-source-id <data-source-id>

# 3. Poll for completion (typically 60-90 seconds for small corpora)
aws bedrock-agent get-ingestion-job \
  --knowledge-base-id <kb-id> \
  --data-source-id <data-source-id> \
  --ingestion-job-id <job-id>
```

The agent runtime reads from the KB at request time; no agent redeploy is needed. The KB-ID is wired to the agent via the `VSA_KB_ID` environment variable in the AgentCore runtime configuration (set in `.bedrock_agentcore.yaml` and the CDK stack).

**Source-category metadata**  
Each document should be uploaded with a `source_category` metadata attribute so that persona-scoped KB filters work correctly:  

```
# Upload with metadata sidecar (S3 object metadata)
aws s3 cp my-new-dtc-guide.md \
  s3://<kb-source-bucket>/technical-reference/my-new-dtc-guide.md \
  --metadata source_category=dtc_guide
```
The `PERSONA_KB_FILTERS` dict in `persona_definitions.py` uses `source_category` values to pre-scope retrieval for the `service_advisor` (categories: `tsb_recall`, `owner_manual`, `service_policy`, `charging_narrative`) and `technician` (categories: `dtc_guide`, `parts_catalog`, `service_policy`) personas.

## Externalizing the system prompt
<a name="extend-content-prompt-externalize"></a>

To externalize the system prompt and routing rules from Python string literals, store them as versioned S3 objects, enabling per-tenant prompt overrides and A/B testing without code changes.

The target shape is a YAML routing config stored in S3 and loaded at session start:

```
# s3://<config-bucket>/tenants/<tenant-id>/routing.yaml
intents:
  - id: tire_pressure_low
    triggers: ["tire pressure low", "TPMS warning"]
    advisors_offered:
      - {id: diy_repair_advisor, label: "walk through it yourself"}
      - {id: find_service_center, label: "book service"}
    default_when_critical: find_service_center
  - id: brake_warning
    triggers: ["brake warning", "ABS fault"]
    advisors_offered: [find_service_center]   # safety: never DIY
```

A rule engine reads this config at session time. Routing decisions otherwise encoded as English prose in the `FLEET_DRIVER_PROMPT` become versioned, diffable YAML that can be A/B tested per tenant without touching the agent codebase.

**Note**  
The system prompt lives in `PERSONA_PROMPTS` in `agents/supervisor/persona_definitions.py` as Python string constants. A prompt change requires a code commit and full agent redeploy. To support per-tenant overrides and A/B testing without code changes, extend `supervisor.build_system_prompt` to read from S3 when a `PROMPT_CONFIG_BUCKET` environment variable is set, falling back to the in-code constants otherwise.

## Per-tenant knowledge bases
<a name="extend-content-per-tenant-kb"></a>

Each tenant can have its own KB for proprietary content — OEM-specific service policies, brand-confidential TSBs, or fleet operator SLA documents — alongside the shared cross-tenant KB for public reference content.

The `config.py` `Config` dataclass exposes `adp_kb_id` (the shared ADP KB) and can be extended with a `tenant_kb_id` field populated from the tenant config record. The `make_knowledge_tool` and `make_retrieve_tool` factories in `agents/supervisor/tools/knowledge.py` and `agents/supervisor/tools/retrieve.py` accept an optional `kb_id` override; pass the tenant KB ID when it is present:

```
# agents/supervisor/supervisor.py  (illustrative extension)
def build_supervisor(ctx, config, *, tenant_config=None, ...):
    tenant_kb_id = (tenant_config or {}).get("kbId") or config.adp_kb_id
    retrieve = make_retrieve_tool(ctx, config, kb_id=tenant_kb_id)
    knowledge = make_knowledge_tool(ctx, config, kb_id=tenant_kb_id)
    ...
```

Cross-account KB access follows the same grant model as the shared ADP KB: the AgentCore execution role needs an `AmazonBedrockAgentCoreSDKRuntime-*` IAM role name (required for Nova 2 Sonic model access) and a `bedrock:Retrieve` resource policy grant on the KB resource. See [Building on CMS and ADP](building-on-cms-and-adp.md) for the cross-account grant pattern.