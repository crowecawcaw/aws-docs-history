

# Context
<a name="rd-context"></a>

## What ASAM SOVD standardises
<a name="rd-what-sovd-standardises"></a>

ASAM SOVD (Service-Oriented Vehicle Diagnostics), in the process of ISO standardisation as ISO 17978 (multi-part series, in development), defines two related things.

The first is a **service-oriented resource model** for vehicle diagnostics. Vehicles expose *components* (ECUs, subsystems), which carry *data* (readable identifiers), *faults* (DTCs and their snapshots), *routines* (invokable diagnostic sequences), and other resources. Operations are expressed against these resources — read a component’s faults, clear its faults, start a routine on it — without the client having to know which underlying protocol (UDS over CAN, DoIP over Ethernet, K-Line on older vehicles) actually implements the operation on the ECU.

The second is a **REST binding** that expresses the resource model over HTTP with JSON payloads. Resources become URIs; operations become HTTP verbs; state transitions and long-running operations follow REST conventions.

The value proposition is client portability: a diagnostic front end built against SOVD — a technician tablet, an OEM dashboard, a fleet-management console — does not need to know per-vehicle UDS byte layouts or per-model decoding. The SOVD server on the vehicle side owns that translation. The client sees resources and JSON.

## The reference deployment topology
<a name="rd-reference-topology"></a>

The most common deployment described in the standard places a **SOVD server on the vehicle’s central gateway ECU**, exposing REST endpoints on the vehicle’s internal network, reachable by:
+ A wired diagnostic tester connected to the OBD-II port or a service Ethernet connector.
+ A tablet on the vehicle’s local Wi-Fi in a service bay.
+ Onboard applications running elsewhere in the vehicle’s software stack.

This topology works well for its target use case — one vehicle, one client, local reachability. The client and server are on the same network segment, mTLS is bounded to that segment, and the SOVD server’s lifetime is tied to ignition or a service session.

## Where the topology stops fitting at fleet scale
<a name="rd-fleet-scale-mismatch"></a>

Extending the same topology to a connected fleet — a cloud-hosted operator UI, thousands to millions of vehicles distributed across mobile carrier networks — surfaces transport-level problems that the REST binding was not designed to solve, because they are outside the standard’s scope.

 **Inbound reachability.** Vehicles sit behind mobile-carrier CGNAT. The cloud has no route to publish a request to a specific vehicle’s HTTP endpoint, and the vehicle’s transient IP is neither stable nor knowable from outside.

 **TLS terminator per vehicle.** An HTTPS server per vehicle requires a TLS certificate per vehicle, whose renewal, revocation, and pinning become an ongoing operational surface distinct from any telemetry certificate already deployed.

 **Idle cost.** The SOVD server is running for events that occur intermittently. Every vehicle pays connectivity, memory, and battery cost for a listener that is silent the vast majority of the time.

 **Substrate duplication.** The vehicle already has a persistent, authenticated MQTT connection to AWS IoT Core, carrying telemetry and receiving actuator commands. An HTTPS server is a second transport, second authentication model, second failure mode.

 **Address brokering.** Cloud-to-vehicle addressing requires a broker that knows which IP a given vehicle currently holds on which carrier. That broker is a bespoke system, and its correctness governs whether SOVD requests reach the vehicle at all.

 **Ecosystem friction.** Both the mobile carrier and any corporate networks in the path must permit inbound HTTPS to vehicle endpoints. The permission surface is per-vehicle, not per-service, and both sides have reasons to say no.

None of these are diagnostics problems. They are properties of *request-response over HTTP with the server addressed by the client*, and they apply to any cloud-to-device protocol that inherits that assumption.