

# Server-side persona inference as a privilege boundary
<a name="sec-persona-privilege"></a>

The persona shapes which agent tools, which grounding surfaces, and which data products a session can access. It is therefore a security boundary, not merely a UI-framing decision. For this reason, the persona is always inferred server-side and is never accepted from the client.

## Inference flow
<a name="sec-persona-inference-flow"></a>

1. The caller’s bearer token arrives at the API Gateway Cognito authorizer.

1. The authorizer validates the token and injects verified claims into the downstream Lambda’s context object (not the request body).

1. The route Lambda reads `custom:role` and `cognito:groups` from the authorizer context and calls the authoritative mapping function (`infer_persona()`).

1. The resolved `personaId` — an enumerated value from the AVX persona set — is passed to the AgentCore runtime as a trusted input from the server layer, not from the client.

1. The AVX entrypoint validates the `personaId` against the known persona set and defaults to the most-constrained persona (`fleet_driver`) if the value is absent, unrecognized, or not among the personas permitted for the caller’s tenant.

The mapping is canonical and resides in a single location (`lambdas/api-assistant-chat/ persona_map.py`) to prevent drift between routes. For the full persona catalog and role-to-persona mapping table, see [Personas and Tenancy](personas-and-tenancy.md).

## Default to most-constrained
<a name="sec-persona-constraint-default"></a>

The fail-secure default is intentional: if the persona cannot be confidently inferred from claims, the session proceeds under the most-constrained persona (`fleet_driver`) rather than failing closed or, worse, elevating to a more privileged persona. The `fleet_driver` persona has the narrowest grounding surface and the most conservative tool access, so the customer still receives a usable response — reduced in scope — while any privilege-escalation risk is eliminated. A `service_advisor` or `technician` session, which carries access to DTC guides, TSBs, and parts-catalog retrieval, can only be reached when the `custom:role=service-advisor` claim is present and verified.