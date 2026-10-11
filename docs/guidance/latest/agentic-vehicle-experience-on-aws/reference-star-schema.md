

# STAR-JSON Booking Schema
<a name="reference-star-schema"></a>

AVX emits booking-shaped artifacts as **STAR-JSON**: a JSON representation of the Standards for Technology in Automotive Retail (STAR) XML message types. This enables tenants already consuming STAR XML to receive an equivalent JSON payload and activate an optional XML converter if their downstream dealer management system requires XML.

 **Complete field-level specification:** `docs/VSA_STAR_JSON_SCHEMA.md` in the AVX repository.

## Message Types
<a name="reference-star-schema-message-types"></a>


**STAR-JSON message types**  

| Message Type | Triggered By | Purpose | 
| --- | --- | --- | 
|  `ServiceRequestAdd`  | P0 or P1 triage classification; P2 when tenant policy requires | Primary service-request ticket. Carries vehicle state, symptoms, DTC observations, recommended inspections, service-center preference, warranty pre-check result, cost estimate, and the actions offered to and chosen by the customer. This is the message type produced by every `book()` call. | 
|  `AppointmentAdd`  | Extension: `book()` when extended to propose or confirm a calendar slot | Appointment record linked to a parent `ServiceRequestAdd`. Emitted with `status: "proposed"` when a calendar feed integration returns available slots, or `status: "confirmed"` when a DMS API confirms the booking. | 
|  `WarrantyClaimPreCheck`  | Extension: `book()` or a dedicated warranty-lookup tool when triage surfaces a component likely under warranty | Advisory pre-check record for the receiving dealer or warranty system. Carries coverage type, expiry, deductible, suspected component, and recall linkage. | 

## Common Envelope
<a name="reference-star-schema-envelope"></a>

Every STAR-JSON message shares a common outer envelope:

```
{
  "schemaVersion": "1.0.0",
  "messageType": "ServiceRequestAdd",
  "messageId": "msg-aabbccdd-eeff-1122-3344-55aa66bb77cc",
  "sessionId": "session_ms1719340_r8abc123xyz",
  "tenantId": "example-fleet-operator",
  "createdAt": "2026-07-14T12:00:00.000Z",
  "createdBy": "vsa-supervisor-v1",
  "correlation": {
    "triageDecisionId": "triage-2026-07-14-0001",
    "vin": "1AAAA00A0AA000123",
    "customerId": "cust-example-001"
  },
  "payload": {},
  "signature": {
    "algo": "HMAC-SHA256",
    "keyId": "vsa-msg-signing-key-2026-q3",
    "value": "base64-encoded-hmac-value"
  }
}
```

The `payload` object contains the message-type-specific fields described in full in `docs/VSA_STAR_JSON_SCHEMA.md`.

## Optional STAR XML Converter
<a name="reference-star-schema-xml-converter"></a>

Tenants with `booking.starXmlConversion: true` in their tenant configuration receive an additional XML artifact alongside every STAR-JSON message. The converter is a pure, idempotent Lambda function (`vsa-star-xml-converter`) that maps the JSON envelope to STAR 5.x XML. Fields not present in the STAR schema are emitted inside a STAR `UserArea` extension block to preserve round-trip integrity. XML conversion is opt-in; by default AVX emits JSON only.

The full field reference for all three message types, including the `ServiceRequestAdd`, `AppointmentAdd`, and `WarrantyClaimPreCheck` payloads, enumerations, and STAR XML mapping principles, is defined in `docs/VSA_STAR_JSON_SCHEMA.md` in the AVX repository.

## Key Enumerations
<a name="reference-star-schema-key-enumerations"></a>


**STAR-JSON key enumeration values**  

| Field | Values | 
| --- | --- | 
|  `messageType`  |  `ServiceRequestAdd` \| `AppointmentAdd` \| `WarrantyClaimPreCheck`  | 
|  `priority`  |  `P0` (safety-critical, stop driving) \| `P1` (service-now, ≤48 h) \| `P2` (service-soon, ≤2 weeks) \| `P3` (monitor, next scheduled service) | 
|  `urgency.classification`  |  `stop-driving` \| `service-now` \| `service-soon` \| `monitor`  | 
|  `safetyAssessment.safeToDrive`  |  `yes` \| `limited` \| `no`  | 
|  `AppointmentAdd.status`  |  `draft` \| `proposed` \| `confirmed` \| `cancelled`  | 
|  `WarrantyClaimPreCheck.determination.result`  |  `covered` \| `partially-covered` \| `not-covered` \| `indeterminate`  | 