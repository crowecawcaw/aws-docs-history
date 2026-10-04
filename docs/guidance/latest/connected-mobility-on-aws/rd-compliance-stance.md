

# Compliance stance
<a name="rd-compliance-stance"></a>

The guidance’s remote-diagnostics implementation is not a standards-compliant SOVD REST implementation on the wire. It is deliberately stated that way so a reader building an interop story can plan accordingly. What follows is what is preserved, what is not, and how REST-client access is restored through a gateway component.

## What is preserved from ASAM SOVD
<a name="rd-preserved"></a>

 **The resource model.** Vehicles are modelled as sets of components. Components carry data, faults, and routines. Operations are expressed against components.

 **The JSON payload schemas.** Fault records carry the SOVD-defined fields — `code`, `status`, `occurrence_count`, `first_seen_ms`, `last_seen_ms`, and `freeze_frame` with signal name, value, unit, and timestamp. Component descriptors, data-identifier reads, and routine invocations follow the standard’s shape.

 **The protocol-independence of the client contract.** A caller does not know or care whether the vehicle-side implementation is UDS over CAN or DoIP over Ethernet.

 **The semantic operations.** Read DTCs, clear DTCs, read data by identifier, start routine, read snapshot — the operation set is SOVD’s operation set. Routine responses in this guidance are additionally typed with a per-routine result schema and a verdict — see [Typed routine result contracts](rd-routine-results.md).

## What is not preserved from ASAM SOVD
<a name="rd-not-preserved"></a>

 **The REST binding.** There are no HTTP verbs, no URI templates, no hypermedia discovery, and no HTTP status-code error taxonomy on the wire. The transport is MQTT topics carrying JSON payloads with a `command_type` discriminator.

 **Direct wire-compatibility with a SOVD REST client.** A client library built against the SOVD REST binding does not connect to a vehicle in this system.

 **The standard’s discovery semantics.** SOVD REST resources are self-describing via hypermedia; the JSON payloads in this system are not.

## How REST interoperability is recovered
<a name="rd-interop-gateway"></a>

Where a partner tool or ecosystem client requires the SOVD REST binding — a workshop scan tool, an aftermarket diagnostic application, a supplier’s compliance-testing harness — REST access is provided through a **REST-to-MQTT gateway**, described in [REST interoperability via a gateway](rd-rest-gateway.md). This gateway is treated as a separate stateful component rather than a URL rewrite. It synthesises resource discovery, translates the HTTP error taxonomy to and from the JSON error blocks used on the wire, holds long-running-operation state, manages pagination cursors, and translates the client’s authenticated identity to the fleet-scoped authorisation model the internal APIs use.

For operator UIs and integrations the guidance operates end-to-end, the gateway is not on the path; those clients call the MQTT-binding API directly.

## Why this trade-off
<a name="rd-tradeoff-rationale"></a>

For operators who own both ends of the client-vehicle relationship — a fleet’s operator UI, an OEM’s dashboard, a service company’s internal tooling — the loss of SOVD REST wire-compatibility on the vehicle side is not a cost, because those clients were never going to speak SOVD REST directly. They call an API the operator defines.

For ecosystem partners who do rely on SOVD REST wire-compatibility, the gateway restores it as one component to build and operate. In exchange, the entire fleet becomes reachable without solving inbound-addressability per vehicle, without provisioning a second TLS terminator per vehicle, and without introducing a transport that duplicates the substrate the vehicle already carries.