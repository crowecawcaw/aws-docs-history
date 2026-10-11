

# API Contract Summary
<a name="reference-api-contract"></a>

This section summarizes the primary integration surface for clients of the Agentic Vehicle Experience. Complete endpoint specifications are in `docs/VSA_API_CONTRACT.md` in the AVX repository.

## POST /assistant/chat
<a name="reference-api-contract-assistant-chat"></a>

The primary web and mobile client entry point. Sends a conversational turn to the AVX agent and receives a text response with optional citations and classification metadata.

 **Authentication:** Cognito ID token in the `Authorization: Bearer` header. Persona is inferred server-side from the token’s Cognito group claims; no persona parameter is required from the client.

 **Request body:** 

```
{
  "prompt": "What does DTC P0420 mean for my vehicle?",
  "sessionId": "session_ms1719340_r8abc123xyz",
  "vin": "1AAAA00A0AA000123"
}
```


**POST /assistant/chat request fields**  

| Field | Required | Description | 
| --- | --- | --- | 
|  `prompt`  | Yes | The conversational utterance from the user. | 
|  `sessionId`  | Yes | Client-generated session identifier. Must be at least 33 characters to satisfy the AgentCore session-ID minimum length requirement. Recommended format: `session_{timestamp}_{randomSuffix}` where `timestamp` is an epoch-ms string. | 
|  `vin`  | No | Vehicle Identification Number for context scoping. When present, the agent resolves vehicle identity, live state, and service history for this VIN. Use a synthetic value (`1AAAA00A0AA000123`) for integration testing. | 

 **Response body (200):** 

```
{
  "result": "DTC P0420 indicates catalyst system efficiency is below the threshold ...",
  "sessionId": "session_ms1719340_r8abc123xyz",
  "classification": "P2",
  "vin": "1AAAA00A0AA000123",
  "citations": ["dtc-P0420.md", "tsb-2024-en-0298.md"]
}
```


**POST /assistant/chat response fields**  

| Field | Description | 
| --- | --- | 
|  `result`  | The agent’s natural-language response to the prompt. | 
|  `sessionId`  | Echoed from the request; use for multi-turn continuity. | 
|  `classification`  | Triage severity assigned by the classifier: `P0` (safety-critical), `P1` (service-now), `P2` (service-soon), `P3` (monitor). Present when the conversation surfaces a diagnosable condition; `null` for general queries. | 
|  `vin`  | Echoed from the request when present. | 
|  `citations`  | Array of knowledge-base document references that grounded the response. Empty array when no KB retrieval occurred. | 

 **Error codes:** 


**POST /assistant/chat error codes**  

| HTTP Status | Meaning | 
| --- | --- | 
| 400 | Malformed request body or missing required fields. | 
| 401 | Missing or invalid Cognito ID token. | 
| 403 | Authenticated but not authorized for this tenant (token `custom:tenantId` mismatch). | 
| 429 | Rate limit exceeded (API Gateway default throttle: 100 req/s steady, 50 burst). | 
| 500 | Agent runtime error. Check CloudWatch logs for the `api-assistant-chat` Lambda log group. | 

## REST Endpoints
<a name="reference-api-contract-rest-endpoints"></a>

All REST endpoints share the same Cognito JWT authentication and error model as `/assistant/chat`. The base URL is the `prod` stage of the AVX `vsa-{stage}-api` API Gateway, emitted as a CloudFormation output.


**AVX REST API endpoints**  

| Endpoint | Method | Purpose | 
| --- | --- | --- | 
|  `/assistant/chat`  | POST | Conversational agent entry point (see above). | 
|  `/triage`  | POST | Deterministic P0–P3 triage classifier. Request: `{"vin": "1AAAA00A0AA000123", "sessionId": "…​"}`. Response: `{"classification": "P1", "decidedAt": "…​", "latencyMs": 642}`. | 
|  `/vehicles/{vehicleId}/live-state`  | GET | Returns the last-known state of a vehicle: odometer, fuel/charge level, active DTCs, and location. Backed by the CMS Redis live-key-state store. | 
|  `/vehicles/{vehicleId}/service-history`  | GET | Returns the ordered list of service events for a vehicle from the CMS DynamoDB service-history table. | 
|  `/vehicles/{vehicleId}/trips`  | GET | Returns recent trip records for a vehicle. Supports `limit` and `startAfter` pagination parameters. | 
|  `/vehicles/{vehicleId}/safety-events`  | GET | Returns safety-event records (hard braking, collision signals, geofence violations) for a vehicle. | 
|  `/drivers/me`  | GET | Returns the profile and linked vehicles for the authenticated driver, resolved from the Cognito token `sub`. | 
|  `/escalate`  | POST | Initiates a human handoff. Starts an Amazon Connect chat (`StartChatContact`) on the tenant’s chat queue with the triage context in contact attributes and returns the participant credentials. On a verified P0 it can also write a roadside request to `vsa-{stage}-rsa-dispatch` and place a callback to the assigned driver. | 
|  `/tenants/{tenantId}/config`  | GET | Returns the public subset of tenant configuration (branding, feature flags, voice settings). Internal fields such as ARNs, queue IDs, and triage-policy thresholds are not returned. | 

## WebSocket API
<a name="reference-api-contract-websocket"></a>

The WebSocket API provides server-push messaging to connected clients.

 **Connect URL:** `wss://{wsApiId}.execute-api.{region}.amazonaws.com/prod?token={cognitoIdToken}` 

The Lambda authorizer validates the Cognito ID token on connect; the connection is rejected with HTTP 401 if validation fails. On successful connect, the connection ID is recorded in the `vsa-{stage}-ws-connections` DynamoDB table alongside the resolved `tenantId`.

 **Server-to-client messages:** the deployed platform does not push server-initiated messages. To add streaming telemetry or reasoning events, implement a publisher Lambda that reads the CMS Redis live-key-state layer and posts to connected WebSocket clients via the API Gateway Management API `@connections` endpoint.

 **Client-to-server messages:** any message sent by the client is acknowledged with `{"ack": true}` and otherwise ignored at present.

## Authentication Summary
<a name="reference-api-contract-auth"></a>


**Authentication mechanisms by channel**  

| Channel | Mechanism | 
| --- | --- | 
| REST API |  `Authorization: Bearer {cognitoIdToken}` header. Validated by API Gateway custom Lambda authorizer. | 
| WebSocket |  `?token={cognitoIdToken}` query parameter on connect URL. Validated by the same Lambda authorizer. | 
| Voice (Nova 2 Sonic / bidirectional) | SigV4-signed WebSocket upgrade to the AgentCore runtime endpoint. The Cognito ID token is forwarded in the request payload (`payload.jwt`) because the AgentCore HTTP layer does not forward custom headers to the handler. | 
| AgentCore text runtime | HTTP POST to the AgentCore runtime endpoint, SigV4-signed. Cognito token forwarded in payload. | 