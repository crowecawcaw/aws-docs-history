

# Add a Persona
<a name="extend-persona"></a>

A **persona** in AVX is a named interaction role that determines which data products load into AgentCore Memory at session start, which KB source categories are pre-scoped for retrieval, which tool factories are registered on the agent, and which system prompt body the supervisor uses.

The four files to edit when adding a persona are:
+  `agents/supervisor/persona_definitions.py` — data bindings and prompt
+  `agents/supervisor/tools/init.py` — tool factory list
+  `lambdas/api-assistant-chat/persona_map.py` — inference from Cognito claims
+  `scripts/seed-personas.py` — seed the new persona’s tenant config and demo user

## Step 1 — Add product bindings and KB filters
<a name="extend-persona-bindings"></a>

 `persona_definitions.py` contains two config dicts the runtime reads:

 `PERSONA_PRODUCT_BINDINGS` maps each persona slug to the ordered list of ADP data products that `persona_loader` fetches into AgentCore Memory at session start. `PERSONA_KB_FILTERS` maps persona slugs that need a pre-scoped KB tool to a `source_category` filter dict that is passed to the `bedrock-agent-runtime:Retrieve` call.

```
# agents/supervisor/persona_definitions.py  (additions only)

PERSONA_PRODUCT_BINDINGS: dict[str, list[str]] = {
    # ... existing personas ...
    "finance_advisor": [           # <-- new persona slug
        "vehicle_identity",
        "customer_360",
        "customer_interactions",
    ],
}

PERSONA_KB_FILTERS: dict[str, dict] = {
    # ... existing entries ...
    "finance_advisor": {
        "source_category": [
            "service_policy",      # warranty and finance policy docs
        ],
    },
}
```

If the persona does not need a pre-scoped KB tool, omit it from `PERSONA_KB_FILTERS`. All personas that have `make_retrieve_tool` in their `PERSONA_TOOL_FACTORIES` list can still call the unfiltered `retrieve` tool regardless.

## Step 2 — Write the system prompt
<a name="extend-persona-prompt"></a>

Add a prompt constant and register it in `PERSONA_PROMPTS`. The prompt body must include `{tenant_display}`, `{vin}`, and `{persona_id}` — these are substituted by `supervisor.build_system_prompt` via `dataclasses.asdict(session)`:

```
# agents/supervisor/persona_definitions.py  (additions only)

FINANCE_ADVISOR_PROMPT = """\
You are the {tenant_display} finance advisor co-pilot, serving persona \
`{persona_id}` for vehicle {vin}.

Your driver is a dealership finance manager. They need fast access to \
customer credit profile, warranty terms, and connected-service subscription \
status to structure deals and answer customer questions at point of contact.

Grounding tools:
- `vehicle_identity`    — VIN, make, model, year, warranty status
- `customer_profile`    — customer tier, contact preferences
- `interaction_history` — prior support and sales interactions
- `retrieve`            — warranty coverage, service policy, finance terms
- `book`                — create a follow-up appointment or support ticket
- `escalate`            — escalate to brand finance support

Session context:
  - Persona: {persona_id}
  - Known VIN: {vin}\
"""

PERSONA_PROMPTS: dict[str, str] = {
    # ... existing entries ...
    "finance_advisor": FINANCE_ADVISOR_PROMPT,
}
```

Keep each prompt under 2 500 characters. Hard rules (triage-before-narrate, retrieve-before-citing, P0 mandatory book) are prepended automatically by `build_system_prompt` via `_HARD_RULES` — do not duplicate them in the persona body.

## Step 3 — Register tool factories
<a name="extend-persona-tools"></a>

Add the new persona slug to `PERSONA_TOOL_FACTORIES` in `agents/supervisor/tools/init.py`:

```
PERSONA_TOOL_FACTORIES: dict[str, list] = {
    # ... existing personas ...
    "finance_advisor": [
        make_triage_tool,
        make_retrieve_tool,
        make_book_tool,
        make_escalate_tool,
        make_vehicle_identity_tool,
        make_customer_profile_tool,
        make_interaction_history_tool,
    ],
}
```

## Step 4 — Wire persona inference
<a name="extend-persona-inference"></a>

 `lambdas/api-assistant-chat/persona_map.py` contains `infer_persona`, the function that maps Cognito authorizer claims to a valid persona slug for the web-chat path. Add the new slug to `_ROLE_MAP` if it maps from a `custom:role` Cognito attribute:

```
# lambdas/api-assistant-chat/persona_map.py

_ROLE_MAP: dict[str, str] = {
    "service-advisor":  "service_advisor",
    "service_advisor":  "service_advisor",
    "finance-advisor":  "finance_advisor",   # <-- new mapping
    "finance_advisor":  "finance_advisor",
}
```

The function is named `infer_persona` (not `map_persona_from_claims`). The default for any unrecognized claim is `fleet_driver`.

For the AgentCore text-runtime path, `agentcore_app.py:_resolve_persona` reads `personaId` directly from the request payload and validates it against `PERSONA_PRODUCT_BINDINGS`. No changes are needed there — the new slug is automatically valid once it appears in `PERSONA_PRODUCT_BINDINGS`.