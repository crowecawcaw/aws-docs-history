

# Design
<a name="rd-design"></a>

## Substrate: MQTT over AWS IoT Core
<a name="rd-substrate"></a>

The vehicle establishes a persistent outbound TLS connection to AWS IoT Core, authenticated with a device certificate provisioned at manufacture or first boot. One property of that connection enables everything that follows: **the vehicle opens it, outbound**.
+  **Reachability** — no inbound path is required. NAT, carrier CGNAT, and corporate firewalls are non-issues.
+  **Identity** — the client certificate identifies the device to the broker. Every publish and subscribe carries that identity.
+  **Authorisation** — AWS IoT policies attached to the certificate constrain which topics the device may publish and subscribe to. A compromised device cannot publish on another vehicle’s response topic; the topic-level authorisation is enforced by the broker.
+  **Session semantics** — MQTT sessions carry keep-alive, last-will, and clean-session behaviour. QoS 1 delivers at-least-once, which is the correct guarantee for a diagnostic command that must not silently disappear.
+  **Namespacing** — the topic tree is a hierarchical namespace with wildcards, so a single certificate policy can grant access to a scoped subtree without enumerating individual topics.

For any vehicle running the AWS IoT-based telemetry stack in this guidance, this connection already exists. Adding a diagnostic surface does not add a connection; it adds a subscription.

## Coexistence with the AWS IoT FleetWise Edge Agent
<a name="rd-coexistence-fwe"></a>

The AWS IoT FleetWise Edge Agent (FWE) is an open-source vehicle-side agent distributed by AWS that handles telemetry campaign execution, DBC-decoded signal upload, and actuator command delivery via a protobuf request/response envelope. Source is at https://github.com/aws/aws-iot-fleetwise-edge under Apache 2.0.

The guidance treats FWE as an **unmodified component**. FWE is technically modifiable, but the guidance chooses not to fork it so upstream FWE releases flow into the fleet without requiring rebuilds or vendor-specific patch maintenance. This choice shapes the coexistence design.

FWE subscribes to a specific topic pattern with a **literal trailing segment** for its protobuf commands. The subscription filter takes a form similar to:

```
{prefix}/things/{ThingName}/executions/+/request/protobuf
```

Two properties of this shape drive the coexistence design:

1.  ** `/protobuf` is a literal MQTT topic segment.** MQTT’s `+` wildcard matches exactly one topic level; it does not wildcard within a level. A subscription filter ending in `/protobuf` receives only publishes whose final segment is literally `/protobuf`.

1.  **FWE’s protobuf schema is fixed.** Extending it with a `command_type` field so FWE dispatches JSON payloads would require regenerating FWE’s protobuf bindings on both vehicle and cloud sides; a field FWE does not know about is silently ignored.

The response is to run a second, small process on the vehicle — a **sidecar** — that owns the MQTT session for diagnostic operations, subscribes to a peer topic path in the same tree, and dispatches diagnostic requests to the vehicle bus over UDS (or DoIP, or whichever protocol the ECUs speak).

## Topic design: peer sub-path in the same tree
<a name="rd-topic-design"></a>

The diagnostic-operation topics are:

```
Request  (cloud → vehicle):
  {prefix}/things/{ThingName}/executions/{execId}/diag/request

Response (vehicle → cloud):
  {prefix}/things/{ThingName}/executions/{execId}/diag/response
```

The `diag/` sub-path sits in the same topic tree as FWE’s `/protobuf` — same prefix, same `things/{ThingName}/executions/{execId}/` structure — but the terminal segment differs. Three properties follow.

 **FWE does not consume diagnostic traffic, by construction.** FWE’s subscription filter ends in the literal `/protobuf` segment, so a publish ending in `diag/request` is not matched. This is a topic-level guarantee that survives FWE upgrades — no runtime discriminator can be misconfigured; the MQTT broker enforces the separation.

 **The existing IoT policy covers the new sub-path.** The policy that grants FWE access to `{prefix}/things//executions/ ` covers the peer sub-path without a policy version bump and without certificate rotation across the fleet.

 **The vehicle certificate covers both channels.** The sidecar uses the same certificate FWE uses (or one issued by the same CA, per the fleet’s provisioning model). Auth for both transports is the same auth.

The general pattern: when adding a new protocol alongside a prebuilt agent on the same IoT connection, choose a peer terminal segment in the same tree, positioned so the existing agent’s subscription filter naturally excludes it. MQTT’s non-crossing wildcard semantics make this a construction-time guarantee, not a runtime check.

## Reconnect discipline
<a name="rd-reconnect"></a>

Persistent MQTT clients disconnect eventually — cellular handoff, tower reboot, TCP timeout, roaming. Reconnect discipline is where MQTT command surfaces most commonly fail silently.

Two invariants hold the design together.

 **The MQTT client does not auto-resubscribe.** Common client libraries (paho-mqtt, AWS IoT SDKs, mosquitto) require the application to re-issue every SUBSCRIBE on the new session. A subscribe issued once at startup is silently dropped on the first reconnect; the underlying TCP/TLS connection is healthy but the vehicle stops receiving commands, and there is no visible signal that anything is wrong.

 **SUBACK, not CONNACK, is the point at which the session is safely established.** CONNACK confirms the transport is up; the broker’s SUBACK confirms the subscription is active. A presence signal that fires on CONNACK will lie whenever SUBACK is delayed or rejected.

The pattern in practice:

1. Subscribe inside the `on_connect` (or equivalent) callback — never once at startup.

1. Accumulate SUBACK grants in `on_subscribe`. When *all* required subscriptions are granted with a non-failure return code, and only then, emit a `connected` presence event.

1. If any SUBACK is rejected, the session is a partial outage. Do not emit `connected`; log the specific rejected topic; continue reconnect attempts.

When the vehicle carries both the actuator-command subscription (FWE side) and the diagnostic subscription (sidecar side), presence must gate on *both* SUBACKs. A vehicle whose FWE side is up but whose diagnostic side is down is a partial outage the operator UI must not paper over.

## Cloud-side dispatch
<a name="rd-cloud-dispatch"></a>

A small cloud handler — an AWS Lambda function in this guidance — receives a diagnostic request from the operator UI or partner API, authorises it, and publishes to the vehicle. The command record in DynamoDB serves three purposes — audit trail, response correlation, and the API surface for later "was this executed and what happened?" queries — carrying `execId`, `ThingName`, `vehicleId`, `command_type`, `caller`, `submittedAt`, `status`, and after response `respondedAt`, `latency_ms`, `resultRef`.

```
Client → HTTPS POST /vehicles/{vehicleId}/diagnostics
         Authorization: Bearer <token>
         Body: SOVD-shaped JSON

         ↓ handler validates + authorises

Handler → DynamoDB write   (command record, status=PENDING)
Handler → MQTT publish
          Topic:   {prefix}/things/{ThingName}/executions/{execId}/diag/request
          Payload: SOVD-shaped JSON
          QoS:     1
```

The response arrives on the vehicle → cloud direction and is caught by an IoT Rule:

```
Vehicle → MQTT publish
          Topic:   {prefix}/things/{ThingName}/executions/{execId}/diag/response
          Payload: SOVD-shaped result JSON, correlation_id=execId

          ↓ IoT Rule matches ".../executions/+/diag/response"

Rule    → invoke response handler Lambda
Handler → update command record (status, latency, resultRef)
Handler → write any resource-level records (per-fault rows, etc.)
```

Note what is not required: no bespoke session broker, no per-vehicle IP lookup, no VPN concentrator, no reverse-proxy fleet. The MQTT topic pattern and the IoT Rule do the routing.

## Edge-side dispatch: the sidecar
<a name="rd-edge-dispatch"></a>

On the vehicle, the diagnostic sidecar is a small process that establishes an MQTT connection to AWS IoT Core using the device certificate, subscribes to `{prefix}/things/{ThingName}/executions/+/diag/request` inside the `on_connect` callback, and dispatches incoming messages to a worker thread. The MQTT event loop must not be blocked by a synchronous multi-second UDS transaction — doing so times out MQTT keep-alive and produces spurious disconnects.

The worker performs the diagnostic operation against the vehicle bus. Where the vehicle speaks UDS over CAN, the worker uses an ISO 14229 implementation on top of an ISO 15765-2 (ISO-TP) transport, typically a library such as `python-can` combined with `python-udsoncan` or an equivalent C\+\+ stack.


|  `command_type`  | UDS service | Purpose | 
| --- | --- | --- | 
|  `read_dtcs`  |  `0x19 02 <mask>`  | ReadDTCInformation by status mask (per ECU, or across all addressable ECUs for a full scan) | 
|  `read_freeze_frames`  |  `0x19 04 <DTC>`  | DTC Snapshot Record — signal values at time of fault | 
|  `clear_dtcs`  |  `0x14 <group>`  | ClearDiagnosticInformation (group code selects scope). Requires an operator attestation on the request; audit trail records the caller identity, the attestation text, and the timestamp against every cleared DTC. | 
|  `read_identity`  |  `0x22 <DID>`  | ReadDataByIdentifier for VIN (`0xF190`), part numbers, software versions | 
|  `read_data`  |  `0x22 <DID>`  | Live data reads from a per-model DID allow-list | 
|  `run_routine`  |  `0x31 01 <RID>`  | RoutineControl start (safety-gated — see [Safety envelope for remote actuation](rd-safety.md)). Body carries a `routine_id` resolved against a per-powertrain catalog; the response carries a typed `result` and a `verdict` — see [Typed routine result contracts](rd-routine-results.md). | 

These are the on-wire `command_type` discriminators the cloud handler emits and the sidecar consumes. The command service in this guidance exposes them behind a single POST route (`/api/commands/{vehicleId}`); the request body’s `command_type` field selects which UDS service the sidecar issues.

For vehicles that speak DoIP over Ethernet (ISO 13400), the same operation set is delivered via the DoIP transport with the same UDS semantics; the sidecar’s dispatch layer is protocol-aware, and the wire operations differ only in the transport below UDS.

The worker marshals the ECU response into SOVD-shaped JSON and publishes on the response topic. What the sidecar is *not*: an HTTP server. It has no listening socket, no separately managed TLS certificate, and no inbound firewall requirement. The MQTT client is its only network I/O.

## Payload contract: SOVD data model, preserved
<a name="rd-payload-contract"></a>

The wire payload preserves the SOVD data model. A `read_dtcs` response takes the form:

```
{
  "correlation_id": "…",
  "status": "SUCCEEDED",
  "components": {
    "ECU_ENGINE": {
      "id": "ECU_ENGINE",
      "protocol": "ISO 15765-4",
      "dtcs": [
        {
          "code": "P0420",
          "status": "confirmed",
          "occurrence_count": 3,
          "first_seen_ms": 1735000000000,
          "last_seen_ms":  1735000000000,
          "freeze_frame": {
            "engineRpm":    { "value": 2800, "unit": "rpm",  "timestamp": "..." },
            "coolantTemp":  { "value":   88, "unit": "degC", "timestamp": "..." },
            "vehicleSpeed": { "value":   65, "unit": "km/h", "timestamp": "..." }
          }
        }
      ]
    }
  },
  "latency_ms": 3400,
  "storage_uri": null
}
```

Fields and their semantics track the SOVD standard’s schemas. What is not here — and what a REST-binding client would expect — is HTTP status code as the error carrier, hypermedia links to related resources, and self-describing discovery. Those are provided by the gateway in [REST interoperability via a gateway](rd-rest-gateway.md) when a client requires them.

## Payload size and the MQTT ceiling
<a name="rd-payload-size"></a>

AWS IoT Core, at time of writing, caps a single MQTT publish at 128 KB. QoS 1 envelope overhead and cellular-link retry budget reduce practical inline payload to approximately 80 KB. A worst-case full-fleet-diagnostic scan with freeze frames can exceed this bound: nine ECUs at ten faults each, twelve freeze-frame signals per fault at approximately ninety bytes each, is on the order of 95 KB.

The pattern is to size-check the encoded payload before publishing and split above a threshold:
+  **Below threshold** (approximately 80 KB): publish inline on the response topic.
+  **Above threshold**: upload the full payload to Amazon S3, publish a small summary message with a pointer.

```
{
  "correlation_id": "…",
  "status": "SUCCEEDED",
  "storage_uri": "s3://.../{ThingName}/{correlation_id}.json",
  "summary": { "componentCount": 9, "faultCount": 42, "hasFreezeFrame": true }
}
```

The cloud response handler generates a presigned GET URL, scoped to the caller, so the operator UI or gateway can fetch the full payload without a new authenticated path.

The threshold is measured, not asserted — a unit test constructs a synthetic 100 KB payload and verifies the S3 branch fires. A documented threshold that is not executable drifts silently; a threshold enforced by a test cannot. AWS IoT Core quotas may change over time; the pattern of size-check-then-fallback is stable regardless of the specific number.

The pattern generalises: any transport with a per-message ceiling should carry a pointer to large payloads, not the payload itself. The transport is optimised for control-plane traffic; the object store is optimised for bulk.