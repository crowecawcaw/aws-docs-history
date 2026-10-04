

# Standards references
<a name="rd-standards-refs"></a>
+  **ASAM SOVD** — Service-Oriented Vehicle Diagnostics. The ASAM specification defines the resource model, JSON schemas, and REST binding. Currently in the process of ISO standardisation as ISO 17978 (multi-part series, in development).
+  **ISO 14229 (UDS)** — Unified Diagnostic Services. The application-layer diagnostic protocol that SOVD servers typically front on the vehicle side.
+  **ISO 15765-2** — Diagnostic communication over CAN: Transport protocol and network layer services. The ISO-TP layer that carries UDS PDUs over CAN frames.
+  **ISO 13400 (DoIP)** — Diagnostic communication over Internet Protocol. Alternative to ISO 15765-2 where the vehicle bus is Ethernet rather than CAN. The pattern in this chapter works identically over DoIP; only the sidecar’s bus-side implementation differs.
+  **MQTT 3.1.1 and 5.0** — In particular the topic-filter matching rules (which make peer-topic coexistence with FWE a construction-time guarantee) and the SUBSCRIBE / SUBACK semantics (which are the correct presence signal).
+  **AWS IoT Core** — MQTT broker with mTLS device authentication, IoT Rules for topic-triggered handlers, and IoT Policies for topic-level authorisation.
+  **AWS IoT FleetWise Edge Agent (FWE)** — Open-source vehicle-side agent for telemetry campaign execution and remote actuator commands. Source at https://github.com/aws/aws-iot-fleetwise-edge under Apache 2.0. In this pattern, FWE owns the `…​/request/protobuf` half of the topic tree; the diagnostic sidecar owns the `…​/diag/*` half.