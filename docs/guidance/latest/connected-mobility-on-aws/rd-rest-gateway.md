

# REST interoperability via a gateway
<a name="rd-rest-gateway"></a>

Where a client requires the SOVD REST binding — a partner scan tool, a compliance-testing harness, an aftermarket diagnostic application — a REST-to-MQTT gateway provides it. The gateway is a distinct cloud-side component with its own operational envelope.

## What the gateway is not
<a name="rd-gateway-not"></a>

It is not a URL-rewrite proxy. A rewrite that mapped `GET /vehicles/{vin}/components/{id}/faults` to a `read_dtcs` publish and returned the correlated response would satisfy the simplest case, but it would not deliver SOVD REST semantics. SOVD REST clients rely on properties that require gateway state.

## What the gateway must do
<a name="rd-gateway-must"></a>

 **Resource discovery.** SOVD REST is self-describing via hypermedia links. A client discovers a vehicle’s component tree by walking `GET /vehicles/{vin}`, following links to components, following links from components to their data, faults, and routines resources. The MQTT protocol described earlier does not carry a component tree per request; the gateway synthesises discovery responses from a per-vehicle catalog (which model, which ECUs, which DIDs are supported, which routines are available). That catalog is state the gateway holds.

 **Error taxonomy translation.** SOVD REST expresses errors via HTTP status codes with SOVD-specific error resources in the body. The MQTT payloads carry error information inside the JSON. The gateway translates between the two, including generating the correct HTTP status code (400 vs 401 vs 403 vs 404 vs 409 vs 5xx) from the JSON error type.

 **Long-running-operation state.** SOVD REST expresses routine executions as first-class resources — `POST /routines/{id}/executions` returns a resource URI a client polls until completion. The MQTT protocol uses a correlation-ID model; the gateway holds the mapping from execution resource URI to correlation ID, holds the current execution state, and translates client polls into reads against the command-record store.

 **Pagination.** SOVD REST supports pagination cursors for large result sets. The gateway generates cursors, holds them for the client’s session, and translates cursor advances into filtered reads.

 **Authentication translation.** The vehicle certificate identifies the vehicle to the MQTT broker. The gateway maps the client’s authenticated identity to the fleet-scoped authorisation model — the same authorisation model the internal operator API uses.

 **Content-negotiation compatibility.** SOVD REST supports content negotiation. The gateway serves JSON by default, honours the standard’s `Accept` header for SOVD-defined content types, and returns appropriate 406 responses when negotiation fails.

## What the gateway costs
<a name="rd-gateway-cost"></a>

One additional stateful cloud component to build and operate. Its correctness governs whether standards-compliant clients can talk to the fleet. If the gateway is down, standards-compliant clients cannot reach the fleet, though internal callers that use the MQTT-binding API remain unaffected.

This is a real cost. It is stated openly rather than folded into "a URL rewrite" because it is the specific trade the design makes. In exchange, the transport layer — the connection from cloud to every vehicle — is not per-vehicle state, and is not per-client state; it is one broker with one namespace, and it scales as the MQTT broker scales.

For fleets whose ecosystem does not include SOVD REST clients, the gateway can be deferred and added when needed. The core design does not depend on it.