

# Add a Tenant-Specific Agent
<a name="extend-tenant-agent"></a>

Some tenants need behavior that differs enough from the shared supervisor that a per-tenant agent variant is the cleaner approach — for example, a fleet operator that requires a fully custom routing policy, a DMS integration unavailable to other tenants, or an OEM persona not present in the shared persona set.

## Tenant config record
<a name="extend-tenant-config"></a>

The tenant configuration record in DynamoDB controls which agent variant a session resolves to. The `lambdas/shared/tenant_config.py` `TenantConfig` loader reads the record keyed by `tenantId`; the `lambdas/tenant-config-loader/handler.py` Lambda populates it from the JSON schema at `schemas/vsa-tenant-config.schema.json`.

A tenant-specific agent variant is selected by adding an `agentVariant` field to the tenant config record:

```
{
  "tenantId": "example-fleet-operator",
  "version": "1.0.0",
  "status": "active",
  "segment": "fleet",
  "agentVariant": "fleet-dms-v1",
  "features": {
    "dmsBooking": true,
    "calendarSlotProposal": true
  }
}
```

## Tenant entrypoint and supervisor construction
<a name="extend-tenant-entrypoint"></a>

The `agentcore_app.py` entrypoint reads `tenantId` from the request payload, loads the tenant config, and passes it to `build_supervisor`. To load a variant agent, extend `build_supervisor` to accept an optional `agent_variant` parameter that selects a different tool set or system prompt:

```
# agents/supervisor/supervisor.py  (excerpt — illustrative extension)

def build_supervisor(
    ctx: SessionContext,
    config: Config,
    *,
    tenant_display: str = "Fleet Services",
    tenant_segment: str = "fleet",
    agent_variant: str | None = None,      # <-- new
) -> Agent:
    model = BedrockModel(
        model_id=config.supervisor_model_id,
        region_name=config.aws_region,
        max_tokens=config.supervisor_max_tokens,
    )

    # Select tool set based on variant
    if agent_variant == "fleet-dms-v1":
        from agents.supervisor.tools import make_dms_booking_tool
        persona_tools = PERSONA_TOOL_FACTORIES.get(ctx.persona_id, []) + [
            make_dms_booking_tool,
        ]
    else:
        persona_tools = PERSONA_TOOL_FACTORIES.get(ctx.persona_id, [])

    tools = [f(ctx, config) for f in persona_tools]
    system_prompt = build_system_prompt(ctx.persona_id, ctx)

    return Agent(
        model=model,
        tools=tools,
        system_prompt=system_prompt,
        name=f"vsa-supervisor-{agent_variant or 'default'}",
    )
```

**Note**  
 `build_supervisor` registers a fixed tool set per persona from `PERSONA_TOOL_FACTORIES`. To add config-driven tool registration, extend `build_supervisor` to read an `enabled_advisors` list from the tenant config record in DynamoDB at session start, filtering `PERSONA_TOOL_FACTORIES.get(ctx.persona_id, [])` to only the tools the tenant has opted into. This removes the need for a code change to onboard a new tenant or modify its tool set.

## Deploy a variant runtime
<a name="extend-tenant-deploy"></a>

Each agent variant that runs in Bedrock AgentCore needs its own runtime registration. The `.bedrock_agentcore.yaml` at the repo root lists one entry per runtime; add a new entry for the variant:

```
# .bedrock_agentcore.yaml  (excerpt — new variant entry)
runtimes:
  - name: vsa_supervisor_fleet_dms_staging
    entrypoint: agents/supervisor/agentcore_app.py
    # execution_role, environment variables, etc.
```

Then deploy with `agentcore deploy` targeting the new entry. The `vsa-core-stack.ts` CDK stack maps runtime ARNs to DynamoDB tenant config records via the `agentRuntimeArn` field; update the CDK context variables after deployment to wire the new ARN to the tenant record.