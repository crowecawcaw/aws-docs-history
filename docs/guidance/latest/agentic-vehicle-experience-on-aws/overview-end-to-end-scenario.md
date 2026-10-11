

# An Illustrative End-to-End Scenario
<a name="overview-end-to-end-scenario"></a>

The following scenario shows how AVX works for a driver in the **Service** stage. It illustrates the full chain of agent tool calls, data sources, and channels that AVX orchestrates in a single voice conversation.

## The Situation
<a name="the-situation"></a>

A driver with a fleet vehicle says to the AVX voice assistant: **"My check engine light just came on and the car feels sluggish — what should I do?"** 

## What Happens
<a name="what-happens"></a>

The AVX supervisor agent runs the following sequence. Each step is a tool call, not a free-form LLM inference, ensuring the answer is grounded in actual vehicle data.


| Step | Agent action | Data source | 
| --- | --- | --- | 
| 1. **Decode the VIN**  | At session start, AVX resolves the caller’s authenticated session to a VIN. The `vehicle_identity()` tool fetches vehicle attributes: a 2022 compact SUV, 1.5L turbocharged engine, fleet-enrolled, 38,400 miles. | ADP Vehicle Identity Graph | 
| 2. **Read active DTCs**  | The `triage()` tool queries CMS live vehicle state for active diagnostic trouble codes. The vehicle reports P0299 — Turbocharger Underboost. | CMS live vehicle state (Redis LKS) | 
| 3. **Look up the DTC**  | The `knowledge()` tool retrieves the P0299 guide from the Bedrock Knowledge Base: severity P2 (service soon), probable causes include boost leak or wastegate actuator failure, safe to drive short distances at reduced power. | ADP Bedrock Knowledge Base (DTC guides) | 
| 4. **Check for matching TSBs**  | A second `knowledge()` call searches the TSB corpus. A 2024 technical service bulletin matches this vehicle’s engine code and describes a known wastegate actuator defect affecting a production window. | ADP Bedrock Knowledge Base (TSBs) | 
| 5. **Quote the repair**  | The `parts_lookup()` tool retrieves the wastegate actuator part from the ADP Parts Catalog: list price, fleet-tier price, and estimated labor hours. | ADP Parts Catalog | 
| 6. **Find a service center**  | The `service_network()` tool queries the ADP Service Network for dealers near the vehicle’s current GPS position, filtered by the capability to perform turbocharged engine repairs. It returns the nearest authorized facility with current wait times. | ADP Service Network | 
| 7. **Book the appointment**  | The `book()` tool creates a STAR-shaped service request (severity P2, DTC P0299, TSB reference, parts pre-listed) and writes it to the CMS service history as a scheduled visit, which shows in the app’s Service tab. | AVX `book` tool (STAR-JSON → CMS service history) | 
| 8. **Check warranty coverage**  | The `knowledge()` tool retrieves the vehicle’s warranty record from the ADP Vehicle Lifecycle product. The powertrain warranty covers the wastegate actuator at 38,400 miles — no out-of-pocket cost for the driver. | ADP Vehicle Lifecycle (warranty) | 

The agent delivers a single, coherent voice response: the vehicle is safe to drive to the nearest authorized dealer, a TSB matches the fault, the repair is covered under the powertrain warranty, and the nearest authorized service center can take the vehicle. The driver confirms, the ticket is created, and the call ends — no hold time, no call transfers, no re-explaining the situation.

## Escalation Path
<a name="escalation-path"></a>

If at any step the triage classification is P0 (stop-driving — for example, brake failure or overheating), the supervisor agent immediately initiates an escalation to the Amazon Connect tier-2 queue. The session cannot proceed to booking until a human agent confirms the situation. This safety guardrail is enforced deterministically — the LLM cannot downgrade a P0 classification.