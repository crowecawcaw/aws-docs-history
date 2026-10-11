

# Server-side persona inference
<a name="pt-persona-inference"></a>

## Why inference is server-side
<a name="pt-inference-why"></a>

AVX never accepts a persona identifier from the client. Persona is a privilege boundary: the `technician` persona has access to parts catalog and DTC diagnostic guide content; the `fleet_driver` persona has access to a different set of tabular records and operational tools. Allowing the client to supply a persona identifier would allow any caller to claim a higher-privilege persona, bypassing the grounding and tool restrictions the persona model enforces.

Server-side inference closes this attack surface. The persona is derived exclusively from verified identity claims extracted by the API Gateway authorizer or the Connect contact flow Lambda — neither of which is accessible to the end user. Invalid or absent persona identifiers always default to the most-constrained persona.

## Inference flow
<a name="pt-inference-flow"></a>

The server-side persona inference path proceeds as follows:

1. The client or Connect channel presents a bearer token (Cognito IdToken) or a set of Connect contact attributes. No persona value is read from the request body.

1. The API Gateway Cognito authorizer validates the token and injects the decoded claims into the route Lambda’s invocation context. Claims include `sub`, `custom:tenantId`, `cognito:groups`, and `custom:role`. For scoped reads, additional standing claims identify who is asking: `custom:customerId` (owner), `custom:vehicleId` (driver of a specific vehicle), `custom:fleetIds` (manager of one or more fleets). Trust for each claim is attested per-stage in SSM — a claim’s presence in the token is necessary but not sufficient; the fail-closed authorization gate that reads Findings and Actions requires the corresponding trust flag as well.

1. The route Lambda calls `infer_persona()`, the authoritative mapping function in `lambdas/api-assistant-chat/persona_map.py`. This function reads the injected claims and applies the mapping rules:


<table>
<thead>
  <tr><th>Identity signal</th><th>Condition</th><th>Persona assigned</th></tr>
</thead>
<tbody>
  <tr><td> <code>cognito:groups</code> or <code>custom:role</code> </td><td>Contains <code>platform-admin</code> or <code>fleet-operator</code> </td><td> <code>fleet_driver</code> </td></tr>
  <tr><td> <code>custom:role</code> </td><td> <code>service-advisor</code> </td><td> <code>service_advisor</code> </td></tr>
  <tr><td>Any other value, or absent</td><td>Default fallback</td><td> <code>fleet_driver</code> </td></tr>
</tbody>
</table>


1. The inferred `personaId` is validated against the set of known persona slugs. An unrecognized value is rejected and replaced with `fleet_driver`.

1. The validated `personaId` is passed to the AVX runtime entry point as part of the session payload. The supervisor reads it at session initialization to select the persona’s system prompt, grounding surface, and tool factory set from the registry in `agents/supervisor/persona_definitions.py`.

**Note**  
The mapping table above reflects the web-chat integration through the CMS Cognito User Pool. Additional claims and mapping rules — for example, inferring `technician` from a service-portal SSO attribute — can be added to `persona_map.py` without changes to the supervisor or the persona definitions. The unit tests in `tests/test_persona_map.py` cover the canonical mapping cases and must be kept up to date as new mappings are added.

## Default to most-constrained
<a name="pt-inference-default"></a>

The inference rule defaults to the most-constrained persona available for the operating context. For the web-chat integration this is `fleet_driver`; for a service-portal integration it might be `service_advisor`. The most-constrained persona is the one with the narrowest tool access appropriate to the channel — it ensures that an unauthenticated or under-authenticated session cannot accidentally access grounding data or tools that belong to a higher-trust role.

This default-to-constrained rule applies at every point where persona resolution might fail: missing claims, unrecognized role values, token validation errors that allow the session to proceed in a degraded mode, or any code path that does not explicitly infer a persona. Every persona resolution path must produce a valid, non-escalating result.