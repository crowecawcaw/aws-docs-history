

# The STAR Booking Contract
<a name="extend-star-contract"></a>

Every booking-shaped artifact AVX produces — service request tickets, appointment proposals, warranty pre-checks — is emitted as **STAR-shaped JSON**. The structure maps 1:1 to the Standards for Technology in Automotive Retail (STAR) XML message types, so tenants already consuming STAR XML can receive a JSON equivalent and enable an optional XML converter via the `booking.starXmlConversion` tenant config flag.

## Message envelope
<a name="extend-star-envelope"></a>

Every STAR-JSON message shares a common outer envelope:

```
{
  "schemaVersion": "1.0.0",
  "messageType": "ServiceRequestAdd",
  "messageId": "msg-<uuid>",
  "sessionId": "vsa-sess-<id>",
  "tenantId": "<tenant-slug>",
  "createdAt": "<ISO 8601 UTC>",
  "createdBy": "vsa-supervisor-v1",
  "correlation": {
    "triageDecisionId": "<triage-uuid>",
    "vin": "<vin>",
    "customerId": "<customer-id or null>"
  },
  "payload": {},
  "signature": {
    "algo": "HMAC-SHA256",
    "keyId": "<signing-key-id>",
    "value": "<base64>"
  }
}
```

The three message types and their scope are:


|  `messageType`  | Scope | Triggered by | 
| --- | --- | --- | 
|  `ServiceRequestAdd`  | Implemented — emitted by every `book()` call | P0 (automatic) or P1/P2/P3 on customer confirmation via `book()` tool | 
|  `AppointmentAdd`  | Extension point — not emitted by the current `book()` implementation |  `book()` when extended to read a calendar feed (slot proposal) or call a DMS API (confirmed booking) | 
|  `WarrantyClaimPreCheck`  | Extension point — not emitted by the current `book()` implementation |  `book()` or a dedicated warranty-lookup tool when triage surfaces a component likely under warranty | 

## Booking behavior and extension points
<a name="extend-star-booking-phases"></a>

The `book()` tool creates a `ServiceRequestAdd` envelope with the triage classification, recommended action, and session context. When the CMS write is enabled (`VSA_BOOK_WRITE_CMS=true`), the booking is persisted as a scheduled row in the CMS service-history table so the iOS app and the CMS Fleet Intelligence portal can surface it alongside completed service records. The envelope is returned to the caller with `status: "sink-accepted"` (CMS write succeeded) or `"draft-created"` (CMS write skipped or unavailable).

 `AppointmentAdd` and `WarrantyClaimPreCheck` message types are defined in the STAR schema but are not emitted by the current `book()` implementation. To extend:

 **To add calendar slot proposal:** extend `book()` to read a tenant calendar-availability feed and propose concrete slots. Emit an `AppointmentAdd` message with `status: "proposed"` and populated `proposedSlots`. Transition to `"confirmed"` when the customer accepts a slot. Gate this path on `features.calendarSlotProposal: true` in the tenant config.

 **To add DMS booking:** extend `book()` to call a tenant DMS API and receive a confirmed booking number. Emit `AppointmentAdd` with `status: "confirmed"` from the live DMS response. Gate this path on `features.dmsBooking: true` in the tenant config.

## Consuming STAR-JSON messages
<a name="extend-star-integration"></a>

STAR-JSON messages are delivered to the tenant’s configured sink. Tenants that process STAR XML can enable the converter:

```
{
  "booking": {
    "starXmlConversion": true,
    "starVersion": "5.6.4"
  }
}
```

When enabled, a thin Lambda (`vsa-star-xml-converter`) converts the JSON envelope to STAR 5.x XML. To add the converter, implement a Lambda that:
+ Maps the `ServiceRequestAdd` JSON envelope to STAR 5.x XML.
+ Validates output against the STAR XSD and fails hard on any mapping error — never silently emits invalid XML.
+ Is invoked after every `book()` call when `booking.starXmlConversion: true` is set in the tenant configuration.

Fields not present in the STAR schema are emitted inside a STAR `UserArea` extension block to preserve round-trip integrity. XML conversion is opt-in; the default behavior emits JSON only.

The full field reference for all three message types, including the `ServiceRequestAdd`, `AppointmentAdd`, and `WarrantyClaimPreCheck` payloads, enumerations, and STAR XML mapping principles, is defined in `docs/VSA_STAR_JSON_SCHEMA.md` in the AVX repository.

## Emitting a booking artifact from a custom tool
<a name="extend-star-write-tool"></a>

If a custom tool needs to produce a STAR message — for example, a partner DMS tool that generates a repair order — it should call the `book()` tool rather than constructing the envelope directly. Pass the structured service request data and let `book()` assign the `messageId`, `sessionId`, and `signature`:

```
# Inside a custom partner-DMS tool
from agents.supervisor.tools.book import make_book_tool

# The supervisor registers book() normally; the custom tool delegates
# to it rather than constructing the STAR envelope itself.
# This preserves the HMAC signature and sink delivery logic.
```

Custom message types not in the STAR set should be emitted inside the `payload._extensions` field to preserve round-trip integrity if a STAR XML converter is added later.