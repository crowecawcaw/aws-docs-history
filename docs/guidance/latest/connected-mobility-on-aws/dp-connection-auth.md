

# Connection type and authentication are separate axes
<a name="dp-connection-auth"></a>

Connection type is an enum with genuinely different fields per value, and both the definition flow and the product detail view branch on it:


| Connection type | Type-specific fields | What the endpoint means | 
| --- | --- | --- | 
|  `rest_polling`  | Polling interval | The base URL to poll | 
|  `grpc_streaming`  | Service name, method name | The gRPC target | 
|  `kafka`  | Topic, consumer group | Comma-separated bootstrap servers | 
|  `websocket_inbound`  | Listen endpoint, allowed origin | Inverted — the platform owns the endpoint the producer connects **to**  | 

A single generic "connection string" field would have been faster to build and impossible to validate, and a detail view could not have explained to an operator what the string meant. The enum is what allows a Kafka product to require both a topic **and** a consumer group before it can be saved.

 **The consumer group is a captured field rather than a derived one.** It is the platform’s own identity for offset tracking, and two subscribers sharing a group share offsets and silently take records from each other — a failure that presents as data loss rather than as misconfiguration. Making it explicit and required puts the decision in front of the operator instead of defaulting it.

Authentication is a separate axis — OAuth 2.0, API key, mTLS, or SASL/SCRAM — because the real combinations cross: mTLS fronts inbound WebSocket, sometimes gRPC, sometimes Kafka; SASL/SCRAM is standard for cloud-deployed Kafka; OAuth and API keys dominate REST. Folding the two axes into one enum would produce a cross-product whose cells are mostly nonsense.