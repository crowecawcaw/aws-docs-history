

# Booking (STAR-JSON)
<a name="booking-agent"></a>

The `book` tool creates service requests as **STAR-shaped JSON** `ServiceRequestAdd` messages, and the companion app books appointment times through `POST /book`. `AppointmentAdd` and `WarrantyClaimPreCheck` are the STAR message types to emit when extending `book()` to a dealer DMS. Tenants that already use STAR integrate without a translation layer.

## STAR-JSON payload structure
<a name="star-json-payload-structure"></a>

Every booking action produces a STAR-shaped envelope:

```
{
  "messageType": "ServiceRequestAdd",
  "header": {
    "tenantId": "fleet-operator-example",
    "sessionId": "vsa-session-abc123",
    "timestamp": "2026-07-14T17:00:00Z"
  },
  "body": {
    "vin": "1AAAA00A0AA000123",
    "criticality": "P1",
    "dtcCodes": ["P0420"],
    "recommendedAction": "Catalyst efficiency — schedule service within 48h.",
    "ticketId": "VSA-4821",
    "status": "DRAFT"
  }
}
```

For legacy DMS consumers that do not accept JSON, add a per-tenant STAR XML converter.

## Booking levels
<a name="booking-levels"></a>


| Level | Capability | Customer experience | Tenant integration required | 
| --- | --- | --- | --- | 
|  **STAR service request**  | Builds a STAR-JSON `ServiceRequestAdd` envelope with a request number (`VSA-<date>-<seq>`) and writes a `scheduled` row to the CMS service-history table, which the app’s Service tab and the CMS portal both show | "I’ve created service request VSA-2026-10-08-4F2A for your service center. It’s in the Service tab of your app." | None beyond CMS. To deliver the envelope to a dealer system, add a delivery step after the CMS write | 
|  **Appointment time**  | In the companion app the customer picks a service, a nearby dealer and a time; `POST /book` (`lambdas/api-book/handler.py`) writes a `scheduled` row to the CMS service-history table, which the app’s Service tab and the CMS portal both show. For the voice agent to offer times, add a `calendar_slot_proposal` tool that reads a tenant availability feed. | "Tire pressure check at your dealer, Tuesday at 10 am — booked." | A dealer list with appointment times for the app to offer | 
|  **DMS repair-order creation**  | Agent 2 (Vehicle Health & Service) plans the service visit — component bundling, coverage application, slot and parts availability — and writes the plan to `vsa-{stage}-service-plans`. When the customer approves the Finding on their iOS card or in Tier 1, the `dms` executor creates the repair order in the DMS and stores `avx_action_id` for status callbacks. The `book` tool’s STAR `ServiceRequestAdd` ticket feeds the booking record; `AppointmentAdd` and `WarrantyClaimPreCheck` are the STAR types for DMS write integrations. | "Tire and brake inspection booked at Meridian Service, Tuesday 10 am — confirmation DMS-RO-12345. Status updates appear in the app." | Agent 2 enabled; `dms` executor configured with DMS connector endpoint in tenant config | 

## Escalation path
<a name="escalation-path"></a>

On a P0 or P1 classification the supervisor recommends speaking with an agent, and the app shows a card with **Talk to an agent** (plus **Request roadside** on P0). The supervisor does not open the handoff itself and does not describe one as done. The driver’s tap, or a request for a person at any priority, reaches `/escalate`, which starts a Connect chat on the tenant’s chat queue. On P0, a tenant can set `escalation.autoOpenHumanChatOnP0` to open the chat without the tap.

The handoff carries the triage classification and its reason, the VIN and vehicle, the driver, and a conversation summary, in the contact attributes and the chat’s first message. See [Contact Center Integration](contact-center-integration.md).