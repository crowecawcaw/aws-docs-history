

# AWS Services Used
<a name="reference-aws-services"></a>

The following AWS services are used in the Agentic Vehicle Experience. Each service fulfills a distinct role in the agentic, data, and channel layers.


**AWS services used in the Agentic Vehicle Experience**  

| Service | Role | 
| --- | --- | 
|  **Amazon Bedrock**  | Hosts the foundation models (Claude Sonnet for conversational reasoning and task orchestration; Titan for embeddings used in knowledge-base indexing). Provides the `InvokeModel` and `Converse`/`ConverseStream` APIs consumed by the Strands supervisor agent. | 
|  **Amazon Bedrock AgentCore**  | Managed agent runtime that hosts the Strands supervisor agent. Provides the bidirectional voice channel via Nova 2 Sonic (speech-to-speech, sub-400 ms latency target) and the HTTP text channel for web and mobile clients. Also hosts the AgentCore Memory resource (Long-Term Memory) that stores per-persona tabular context between sessions. | 
|  **Amazon Connect**  | Contact-center platform for all voice and chat channels. Receives inbound customer calls, runs tenant-branded contact flows, and routes escalations to the tenant’s chat queue, with P0 on a high-priority branch. Places the P0 callback to the assigned driver when the tenant configures one. | 
|  **Amazon Bedrock Knowledge Bases**  | Provides retrieval-augmented generation (RAG) over the automotive reference corpus: DTC diagnostic guides, technical service bulletins, NHTSA recall documents, owner manuals, and service-policy documents. Supports cross-account `Retrieve` calls from the Agentic Vehicle Experience (AVX) agent into the Automotive Data Platform (ADP) knowledge base, scoped by `source_category` metadata filter. | 
|  **Amazon Cognito**  | Multi-tenant authentication layer. One user pool per tenant provides OEM-branded or fleet-branded sign-in. Pool IDs and client IDs are emitted as CloudFormation outputs and bundled into the client-side configuration at deploy time. The API Gateway custom authorizer validates Cognito ID tokens and enforces per-tenant claim isolation (`custom:tenantId`). | 
|  **Amazon API Gateway**  | Exposes the AVX REST API (HTTP) and the WebSocket API. The REST API hosts endpoints for triage classification, vehicle context, service history, trips, safety events, bookings, and escalations. The WebSocket API carries server-push messages (telemetry stream, reasoning drawer) to connected clients. | 
|  **Amazon DynamoDB**  | Stores tenant configuration (`vsa-{stage}-tenant-config`), triage decisions, action queues, and WebSocket connection records. Also serves as the vehicle-state and service-history data store provided by the Connected Mobility (CMS) layer that AVX reads. | 
|  **AWS Lambda**  | Implements all API handlers (vehicle context, live state, service history, trips, safety events, triage, escalation, booking) and the deterministic triage classifier. Also hosts the WebSocket authorizer Lambda that validates Cognito tokens on connect. | 