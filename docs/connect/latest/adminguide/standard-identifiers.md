

# Standard identifiers in Customer Profiles
<a name="standard-identifiers"></a>

Standard identifiers are tags applied to a key that describe its role during ingestion. They tell Customer Profiles how each key participates in matching an object to a profile and whether the key value is stored for future use. You set standard identifiers in the `StandardIdentifiers` array of a key definition. For more information, see [Key definitions in Customer Profiles object type mappings](mapping-key-definitions.md).

## Standard identifiers reference
<a name="standard-identifiers-reference"></a>


| Identifier | Purpose | 
| --- | --- | 
| UNIQUE | Identifies the specific object instance. Exactly one UNIQUE identifier is required per object type. When a new object arrives with the same UNIQUE value, it replaces the existing one. | 
| PROFILE | Used to look up the profile the object belongs to. At least one PROFILE identifier is required. The key is stored so it can also be used for future matching and for SearchProfiles queries. | 
| SECONDARY | A fallback profile-matching key. SECONDARY is always used in combination with PROFILE—the key's standard identifiers must include both. Secondary keys are only consulted when no primary PROFILE key produces an unambiguous match. The key is always stored. | 
| LOOKUP\_ONLY | Used only to match a profile during this ingestion. The key value is not stored afterward, so it can't be used for future matches or searches. Can't be combined with UNIQUE. | 
| NEW\_ONLY | The key is stored only when a new profile is created during this ingestion. If the object matches an existing profile, the key behaves like LOOKUP\_ONLY. Can't be combined with UNIQUE. | 
| ASSET, ORDER, CASE | Associates the object with a standard asset, order, or case record. | 
| AIR\_PREFERENCE, HOTEL\_PREFERENCE, AIR\_BOOKING, AIR\_SEGMENT, HOTEL\_RESERVATION, HOTEL\_STAY\_REVENUE | Associates the object with the corresponding travel record. | 
| LOYALTY, LOYALTY\_TRANSACTION, LOYALTY\_PROMOTION | Associates the object with a loyalty record, transaction, or promotion. | 
| DEVICE | Associates the object with a device record. | 
| WEB\_ANALYTICS | Associates the object with a web analytics event. | 

## PROFILE, SECONDARY, and LOOKUP\_ONLY compared
<a name="compare-matching-identifiers"></a>

All three identify the profile an object belongs to. They differ in when they're evaluated during matching and whether the key value is stored afterward. `SECONDARY` is not used on its own—a secondary key lists both `PROFILE` and `SECONDARY` in its standard identifiers:


| Aspect | `PROFILE` | `SECONDARY` | `LOOKUP_ONLY` | 
| --- | --- | --- | --- | 
| Required? | Yes—at least one per object type | No | No | 
| When it's used for matching | In the primary matching pass | Only as a fallback when primary PROFILE keys don't match | In the primary matching pass, alongside PROFILE keys | 
| Stored after ingestion? | Yes | Yes | No | 
| Available for future lookups and SearchProfiles? | Yes | Yes | No | 
| Best for | Durable identifiers that reliably locate the profile, such as a customer ID | Lower-priority identifiers that you still want saved for future use | Transient identifiers you don't want permanently associated | 

## NEW\_ONLY behavior
<a name="new-only-behavior"></a>

`NEW_ONLY` scopes a key so it's only attached to profiles this ingestion creates:
+ If the object matches an **existing** profile, the key is used for matching only and is not stored on that profile (same as `LOOKUP_ONLY`).
+ If the object causes a **new** profile to be created, the key is stored on the new profile (same as `PROFILE`).

Use `NEW_ONLY` when you want a value to help create and identify a new profile, but you don't want it added to an existing profile—where it could accidentally cause unrelated profiles to merge.

## Combination rules
<a name="standard-identifiers-combination-rules"></a>
+ `UNIQUE` can't be combined with `LOOKUP_ONLY` or `NEW_ONLY`.
+ If any key combines `PROFILE` with `LOOKUP_ONLY` or `NEW_ONLY`, at least one other key must use `PROFILE` on its own (without `LOOKUP_ONLY` or `NEW_ONLY`). This guarantees an ingested object can always be persistently associated with a profile. The `_profileId` key is exempt from this requirement.
+ Standard object identifiers (`ASSET`, `ORDER`, and so on) can be combined with `PROFILE` and `UNIQUE` as needed.
+ If your fields target a standard object type—for example, `_asset.SerialNumber`—at least one key must carry that object type's standard identifier (`ASSET`).
+ Reserved keys such as `_profileId`, `_orderId`, `_caseId`, and `_assetId` must be declared `LOOKUP_ONLY`.

## Required identifiers per object type
<a name="required-identifiers-per-object-type"></a>
+ Exactly one key with a `UNIQUE` identifier.
+ At least one key with a `PROFILE` identifier.
+ If fields target a standard object type, at least one key with that object type's standard identifier.