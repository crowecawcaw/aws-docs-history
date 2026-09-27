

# Reference for standard objects in Customer Profiles
<a name="standard-objects"></a>

Connect Customer Customer Profiles defines a set of **standard objects** that represent common business entities—profiles, orders, cases, loyalty records, travel records, and others. Each standard object is a structured record with a fixed schema that downstream applications (such as the Connect Customer agent workspace) can read without knowing the original format of your data.

This topic describes each standard object, its object type name, the standard identifier you use to associate ingested data with it, and how matching works at ingestion time. The topics in this section provide the full definition of each standard object and the object type mappings from external applications to it. For the identifiers themselves, see [Standard identifiers in Customer Profiles](standard-identifiers.md). For the field syntax used to populate them, see [Field definitions in Customer Profiles object type mappings](mapping-field-definitions.md).

## Profile objects compared with standard objects
<a name="profile-objects-vs-standard-objects"></a>

Profile objects and standard objects sound similar but behave differently:
+ A **profile object** is the raw record you ingest with [PutProfileObject](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_PutProfileObject.html). Each profile object is identified by its `UNIQUE` key. Re-ingesting an object with the same `UNIQUE` value **replaces the previous profile object wholesale**—the new record's contents fully overwrite the old one.
+ A **standard object** is a structured record with a fixed schema (the standard profile, an asset, an order, a loyalty membership, and so on). Standard objects are **not** replaced wholesale by ingestion. Instead, each ingested profile object contributes only the fields its mapping targets at that standard object. Multiple object types can write to the same standard object over time, so a single asset record can accumulate fields from registration data, warranty data, and service-history data—each ingested as a separate profile object type.

**Note**  
**Standard profile objects can't be ingested directly**  
You can't call `PutProfileObject` with `_profile` or any other standard object type name. To create or update a profile directly, use [CreateProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateProfile.html) or [UpdateProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateProfile.html). To populate any other standard object, ingest a custom object type whose fields target it (for example, `_asset.SerialNumber`) and whose keys carry the matching standard identifier (for example, `ASSET`).

## How fields and keys work with standard objects
<a name="how-fields-keys-work-standard-objects"></a>

A field's `Target` places the field's value into a standard object. For example, `"Target": "_asset.SerialNumber"` stores the field on the asset record associated with the ingested object.

A key's standard identifier (such as `ASSET`, `ORDER`, or `LOYALTY`) tells Customer Profiles which standard object that key looks up. At ingestion, Customer Profiles uses the key value to find the matching record:
+ If exactly one record is found, the object is associated with it.
+ If more than one record is found, the match is ambiguous and is rejected.
+ If no record is found, a new record can be created (depending on the object type).

**Note**  
**Required identifiers when targeting a standard object**  
If any field targets a standard object type—for example, `_asset.SerialNumber`—at least one key must carry that object type's standard identifier (in this case, `ASSET`). For more information, see [Standard identifiers in Customer Profiles](standard-identifiers.md).

For the complete list of templates that ingest into standard objects, call [ListProfileObjectTypeTemplates](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjectTypeTemplates.html).

## System-managed ID fields
<a name="system-managed-id-fields"></a>

Every standard object has an ID field that Customer Profiles owns and assigns. These ID fields can't be set with a field `Target`:
+ `_profile.ProfileId`
+ `_asset.AssetId`, `_case.CaseId`, `_order.OrderId`
+ `_communicationRecord.CommunicationRecordId`
+ `_airPreference.PreferenceId`, `_hotelPreference.PreferenceId`
+ `_airBooking.BookingId`, `_airSegment.SegmentId`
+ `_hotelReservation.ReservationId`, `_hotelStayRevenue.StayRevenueId`
+ `_loyalty.LoyaltyId`, `_loyaltyTransaction.TransactionId`, `_loyaltyPromotion.PromotionId`
+ `_device.DeviceId`, `_webAnalytics.EventId`

## Profile
<a name="standard-object-profile-summary"></a>


|  |  | 
| --- |--- |
| Object type name | \_profile | 
| Standard identifier | PROFILE | 
| ID field | \_profile.ProfileId (system-managed) | 
| Represents | The unified customer profile—the central record that other standard objects attach to. | 

Most mappings populate the standard profile. Common targets include `FirstName`, `LastName`, `EmailAddress`, `PhoneNumber`, `AccountNumber`, `ShippingAddress.*`, and custom values under `_profile.Attributes.{name}`. For more information, see [Field definitions in Customer Profiles object type mappings](mapping-field-definitions.md).

**Matching:** A key marked `PROFILE` looks up the profile the object belongs to. If no profile matches and `AllowProfileCreation = true`, an inferred profile is created. For more information, see [Profile matching and inferred profiles in Customer Profiles](profile-matching.md).

## Customer engagement records
<a name="customer-engagement-records"></a>

### Asset
<a name="standard-object-asset-summary"></a>


|  |  | 
| --- |--- |
| Object type name | \_asset | 
| Standard identifier | ASSET | 
| ID field | \_asset.AssetId (system-managed) | 
| Represents | A product the customer owns or has purchased—for example, an appliance, a subscription, or a vehicle. | 

Use an asset record when an ingested object describes something the customer owns and you want agents and downstream systems to see that asset on the customer's profile. Typical targets are values like a serial number, model, purchase date, or status, mapped under `_asset.{field}`.

**Matching:** A key marked `ASSET` looks up the asset record. If exactly one asset matches the key value, the ingested object is associated with that asset. Multiple matches reject the ingestion.

### Order
<a name="standard-object-order-summary"></a>


|  |  | 
| --- |--- |
| Object type name | \_order | 
| Standard identifier | ORDER | 
| ID field | \_order.OrderId (system-managed) | 
| Represents | A purchase or order the customer placed. | 

Use an order record for purchase data—order number, line items, totals, status, dates—so the order appears on the customer's profile in agent-facing tools.

**Matching:** A key marked `ORDER` looks up the order record by the key's value (for example, an order number).

### Case
<a name="standard-object-case-summary"></a>


|  |  | 
| --- |--- |
| Object type name | \_case | 
| Standard identifier | CASE | 
| ID field | \_case.CaseId (system-managed) | 
| Represents | A support case opened on behalf of a customer. | 

Use a case record for ticketing or support-case data—case number, subject, status, severity, opened/closed timestamps. Cases let agents see existing case context when a customer contacts you.

**Matching:** A key marked `CASE` looks up the case record by the key's value.

### Communication record
<a name="standard-object-communication-record-summary"></a>


|  |  | 
| --- |--- |
| Object type name | \_communicationRecord | 
| Standard identifier | — | 
| ID field | \_communicationRecord.CommunicationRecordId (system-managed) | 
| Represents | A communication event with a profile—email opens, clicks, message receipts, and similar events. | 

Communication record targets follow a special pattern: `_communicationRecord.Events.{eventType}.Attributes.{attribute}`. For example, `_communicationRecord.Events.EmailOpen.Attributes.Subject` records an email-open event with a subject attribute.

Communication records are populated through marketing-tool templates (such as Marketo) rather than by attaching a generic key identifier.

## Travel records
<a name="standard-object-travel-records"></a>

Travel records form a related set covering preferences, bookings, segments, reservations, and stays. Each has its own standard identifier and ID field.


| Object type | Identifier | ID field | Represents | 
| --- | --- | --- | --- | 
| \_airPreference | AIR\_PREFERENCE | PreferenceId | A traveler's preferences for air travel (seat, meal, cabin, frequent-flyer numbers). | 
| \_hotelPreference | HOTEL\_PREFERENCE | PreferenceId | A traveler's preferences for hotel stays (room type, floor, smoking preference). | 
| \_airBooking | AIR\_BOOKING | BookingId | A complete air booking (passenger name record, or PNR), including ticket numbers and passenger information. | 
| \_airSegment | AIR\_SEGMENT | SegmentId | A single flight segment within a booking (origin, destination, departure, arrival). | 
| \_hotelReservation | HOTEL\_RESERVATION | ReservationId | A hotel reservation (property, dates, room, rate). | 
| \_hotelStayRevenue | HOTEL\_STAY\_REVENUE | StayRevenueId | Revenue and charges associated with a completed hotel stay. | 

**Matching:** Each travel identifier behaves the same way as `ASSET` and `ORDER`—the key value is used to look up exactly one record of that type. Multiple matches reject the ingestion.

## Loyalty records
<a name="standard-object-loyalty-records"></a>


| Object type | Identifier | ID field | Represents | 
| --- | --- | --- | --- | 
| \_loyalty | LOYALTY | LoyaltyId | A customer's loyalty program membership (program name, tier, points balance). | 
| \_loyaltyTransaction | LOYALTY\_TRANSACTION | TransactionId | A points-earning or points-redeeming event on a loyalty membership. | 
| \_loyaltyPromotion | LOYALTY\_PROMOTION | PromotionId | A promotion or campaign tied to a loyalty program. | 

**Matching:** A loyalty identifier looks up its record by the key's value. Use `LOYALTY` for membership-level data, `LOYALTY_TRANSACTION` for individual point events, and `LOYALTY_PROMOTION` for promotion definitions.

## Other standard objects
<a name="other-standard-objects"></a>

### Device
<a name="standard-object-device-summary"></a>


|  |  | 
| --- |--- |
| Object type name | \_device | 
| Standard identifier | DEVICE | 
| ID field | \_device.DeviceId (system-managed) | 
| Represents | A device associated with a profile—mobile phone, app install, browser fingerprint, or IoT device. | 

**Matching:** A key marked `DEVICE` looks up the device record by the key's value (for example, a device ID or advertising identifier).

### Web analytics
<a name="standard-object-web-analytics-summary"></a>


|  |  | 
| --- |--- |
| Object type name | \_webAnalytics | 
| Standard identifier | WEB\_ANALYTICS | 
| ID field | \_webAnalytics.EventId (system-managed) | 
| Represents | A web-analytics event such as a page view, click, or conversion. | 

**Matching:** A key marked `WEB_ANALYTICS` looks up the event record by the key's value.

## Identifier compatibility at a glance
<a name="identifier-compatibility-at-a-glance"></a>

Standard object identifiers can be combined with `PROFILE` and `UNIQUE` as needed on the same key. They can't replace `UNIQUE` or `PROFILE`, which remain required on every object type.
+ Every object type still needs exactly one `UNIQUE` key and at least one `PROFILE` key.
+ If fields target a standard object type, at least one key must also carry that object type's identifier.
+ Reserved key names `_profileId`, `_orderId`, `_caseId`, and `_assetId` must be declared `LOOKUP_ONLY`. For more information, see [Standard identifiers in Customer Profiles](standard-identifiers.md).

**Topics**
+ [Profile objects compared with standard objects](#profile-objects-vs-standard-objects)
+ [How fields and keys work with standard objects](#how-fields-keys-work-standard-objects)
+ [System-managed ID fields](#system-managed-id-fields)
+ [Profile](#standard-object-profile-summary)
+ [Customer engagement records](#customer-engagement-records)
+ [Travel records](#standard-object-travel-records)
+ [Loyalty records](#standard-object-loyalty-records)
+ [Other standard objects](#other-standard-objects)
+ [Identifier compatibility at a glance](#identifier-compatibility-at-a-glance)
+ [Object type mapping for the standard profile in Connect Customer Customer Profiles](object-type-mapping-standard-profile.md)
+ [Object type mapping for the standard order in Connect Customer Customer Profiles](object-type-mapping-standard-order.md)
+ [Object type mapping for the standard communication record](object-type-mapping-standard-communiction-record.md)
+ [Object type mapping for the standard asset in Customer Profiles](object-type-mapping-standard-asset.md)
+ [Object type mapping for the standard case in Customer Profiles](object-type-mapping-standard-case.md)
+ [Object type mapping for the standard air preference](object-type-mapping-standard-air-preference.md)
+ [Object type mapping for the standard hotel preference](object-type-mapping-standard-hotel-preference.md)
+ [Object type mapping for the standard air booking](object-type-mapping-standard-air-booking.md)
+ [Object type mapping for the standard air segment](object-type-mapping-standard-air-segment.md)
+ [Object type mapping for the standard hotel reservation](object-type-mapping-standard-hotel-reservation.md)
+ [Object type mapping for the standard loyalty](object-type-mapping-standard-loyalty.md)
+ [Object type mapping for the standard loyalty transaction](object-type-mapping-standard-loyalty-transaction.md)
+ [Object type mapping for the standard loyalty promotion](object-type-mapping-standard-loyalty-promotion.md)
+ [Object type mapping for the standard web analytics](standard-loyalty-promotion-object-mapping-web-analytics.md)
+ [Object type mapping for Item Catalog](standard-loyalty-promotion-object-mapping-item-catalog.md)
+ [Object type mapping for the standard hotel stay revenue](object-type-mapping-standard-hotel-stay-revenue.md)