

# Examples of object type mappings in Connect Customer Customer Profiles
<a name="examples-object-type-mappings"></a>

This topic builds a mapping from the ground up. Each example builds on the one before it.


| Example | What it adds | 
| --- | --- | 
| [1. The smallest valid mapping](#example-smallest-valid-mapping) | The two required keys: UNIQUE and PROFILE | 
| [2. Populate the standard profile](#example-populate-standard-profile) | Target, ContentType, search-only keys | 
| [3. Populate a standard object](#example-populate-standard-object) | Standard object identifiers and targets (ASSET, \_asset.\*) | 
| [4. Link two object types together](#example-link-object-types) | Shared key names, one key serving two roles | 

## The shape of a mapping
<a name="shape-of-a-mapping"></a>

Every mapping is a set of `Fields` and a set of `Keys`. Fields pull values out of the incoming object. Keys combine fields into identifiers that Customer Profiles uses to match and search.

```
{
    "Fields": {
        "{fieldName}": {                     <-- your name for this value
            "Source": "{source}",            <-- where to read it from the incoming object
            "Target": "{target}",            <-- optional: where to write it on a standard object
            "ContentType": "{contentType}"   <-- optional: how to normalize it (default STRING)
        }
    },
    "Keys": {
        "{keyName}": [                       <-- an array, so one key name can have several definitions
            {
                "StandardIdentifiers": [...],  <-- optional: the key's role during ingestion
                "FieldNames": ["{fieldName}"]  <-- one or more fields defined above
            }
        ]
    }
}
```

**Note**  
**Fields and keys are separate namespaces**  
A field name is a local label used only inside this mapping. A key name is global to the domain and shared with every other object type that uses the same name. The examples below use different names for the two so the distinction stays visible.

## How to build a mapping
<a name="how-to-build-a-mapping"></a>

Work through these five questions in order. The answers become the mapping.

1. **What makes one incoming record distinct from the next?** That value becomes your `UNIQUE` key. Every object type needs exactly one. Re-ingesting a record with the same `UNIQUE` value replaces the previous one.

1. **What ties the record to a person?** A customer ID, email, phone, or account number. That becomes a `PROFILE` key. Every object type needs at least one.

1. **Which values do you want to appear on the customer's profile?** Give each one a field with a `Target` on the standard profile object, such as `_profile.FirstName`.

1. **Does the record also describe an asset, order, case, or similar record?** Those are other **standard objects**—predefined records with fixed schemas. If your record describes one, target it (`_asset.*`) and add its standard identifier (`ASSET`) to a key.

1. **Which other values do you want to be searchable?** Add a key for each, with no standard identifiers.

**Note**  
**Profile objects and standard objects behave differently**  
The record you ingest is a *profile object*. It's identified by its `UNIQUE` key and is replaced wholesale when the same `UNIQUE` value arrives again. A `Target` writes into a *standard object* (the standard profile, an asset, an order). Standard objects are never replaced wholesale—they accumulate field values from many profile objects over time. For more information, see [Reference for standard objects in Customer Profiles](standard-objects.md).

**Note**  
**Every key is searchable**  
Matching is only half of what a key does. Each key is also indexed for the [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) API, so you can find a profile after ingestion by passing a key name and a value. Because key names are global to the domain, searching one name finds profiles across every object type that defines it. Only stored keys stay searchable—see [Standard identifiers in Customer Profiles](standard-identifiers.md) to control when keys are stored.

**Tip**  
**Choose distinctive key values**  
Choose key values distinctive enough to identify a profile: a customer ID, an email address, an order number, a serial number. Low-cardinality values such as gender, state, country, status, or loyalty tier make poor keys—avoid them.

## Example 1: The smallest valid mapping
<a name="example-smallest-valid-mapping"></a>

A mapping needs one `UNIQUE` key and one `PROFILE` key. Nothing else is required. A single key can carry both roles.

Incoming object:

```
{
  "customerId": "C-10045",
  "signupDate": "2025-01-14"
}
```

Mapping:

```
{
    "Fields": {
        "customerId": {
            "Source": "_source.customerId"
        }
    },
    "Keys": {
        "crmCustomerId": [
            {
                "StandardIdentifiers": ["PROFILE", "UNIQUE"],
                "FieldNames": ["customerId"]
            }
        ]
    }
}
```

What happens at ingestion:
+ Customer Profiles looks for a profile whose `crmCustomerId` key equals `C-10045`. If it finds exactly one, the record attaches to it. If it finds none and `AllowProfileCreation = true`, a new inferred profile is created.
+ The whole incoming record is stored as a profile object, including `signupDate`—storage doesn't require a field definition. Only the values you want indexed or written to a standard object need fields.
+ Nothing appears on the standard profile, because no field has a `Target`. Agents looking at the profile would see an empty record.

Example 2 addresses that last point.

## Example 2: Populate the standard profile
<a name="example-populate-standard-profile"></a>

Adding a `Target` to a field writes its value onto the standard profile, where agents and downstream applications can read it.

Incoming object:

```
{
  "customerId": "C-10045",
  "email": "john@example.com",
  "phone": "+15551234567",
  "firstName": "John",
  "lastName": "Doe",
  "address": {
    "street": "123 Main St",
    "city": "Seattle",
    "zip": "98101"
  }
}
```

Mapping:

```
{
    "Fields": {
        "customerId": {
            "Source": "_source.customerId",
            "Target": "_profile.AccountNumber"
        },
        "emailAddress": {
            "Source": "_source.email",
            "Target": "_profile.EmailAddress",
            "ContentType": "EMAIL_ADDRESS"
        },
        "phoneNumber": {
            "Source": "_source.phone",
            "Target": "_profile.PhoneNumber",
            "ContentType": "PHONE_NUMBER"
        },
        "firstName": {
            "Source": "_source.firstName",
            "Target": "_profile.FirstName",
            "ContentType": "NAME"
        },
        "lastName": {
            "Source": "_source.lastName",
            "Target": "_profile.LastName",
            "ContentType": "NAME"
        },
        "fullName": {
            "Source": "{{#removeExtraSpace}}{{_source.firstName}} {{_source.lastName}}{{/removeExtraSpace}}",
            "ContentType": "NAME"
        },
        "mailingAddress.address1": {
            "Source": "_source.address.street",
            "Target": "_profile.MailingAddress.Address1"
        },
        "mailingAddress.city": {
            "Source": "_source.address.city",
            "Target": "_profile.MailingAddress.City"
        },
        "mailingAddress.postalCode": {
            "Source": "_source.address.zip",
            "Target": "_profile.MailingAddress.PostalCode"
        }
    },
    "Keys": {
        "crmCustomerId": [
            {
                "StandardIdentifiers": ["PROFILE", "UNIQUE"],
                "FieldNames": ["customerId"]
            }
        ],
        "_email": [
            {
                "FieldNames": ["emailAddress"]
            }
        ],
        "_phone": [
            {
                "FieldNames": ["phoneNumber"]
            }
        ],
        "_fullName": [
            {
                "FieldNames": ["fullName"]
            }
        ]
    }
}
```

What's new here:
+ **`Target`**: each targeted field writes to the standard profile. Untargeted fields (`fullName`) still exist for use in keys.
+ **`ContentType`**: normalizes the value before it's indexed and matched. `EMAIL_ADDRESS` and `NAME` are both case-insensitive, and `NAME` also collapses repeated spaces, so `John SMITH` matches `john smith`. `PHONE_NUMBER` ignores formatting, so `+1 (206) 345-7890` matches `2063457890`. Set it on every email, phone, name, and numeric field you index. Omit it and the value is treated as `STRING` and matched exactly as written.
+ **Search-only keys**: `_email`, `_phone`, and `_fullName` have no `StandardIdentifiers`. They're indexed for `SearchProfiles` but take no part in matching this record to a profile. Only `crmCustomerId` does that.
+ **Dotted field names**: `mailingAddress.city` mirrors the target path. This is a readability convention, not a requirement; field names allow letters, digits, underscores, dots, and hyphens.
+ **Handlebars**: `fullName` combines two source values. `removeExtraSpace` collapses the gap if one part is missing. Most fields need only a plain accessor like `_source.email`; reach for Handlebars only when you're combining or transforming values. For more information, see [Field definitions in Customer Profiles object type mappings](mapping-field-definitions.md).

**Tip**  
**Naming your keys**  
Use the predefined domain keys as-is when the value means what they mean: `_email`, `_phone`, `_fullName`, `_account`.
Give keys you invent a plain name with no leading underscore, such as `crmCustomerId`.
`_profileId`, `_orderId`, `_caseId`, and `_assetId` are reserved. If you use them, they must be `LOOKUP_ONLY`, which means they aren't stored. Pick a different name if you want the value searchable.

**Tip**  
**Custom values**  
Every `Target` must name a field that actually exists on the standard object. For a value that does not map to a standard field, map it to a custom attribute instead: give it any name you like under `Attributes`, such as `_profile.Attributes.LoyaltyTier`. Other standard objects work the same way, as in `_asset.Attributes.InstallerName`.  
Check the standard object definition for the exact field names—see [Reference for standard objects in Customer Profiles](standard-objects.md).

## Example 3: Populate a standard object
<a name="example-populate-standard-object"></a>

When a record describes an asset, order, case, loyalty membership, or travel booking, you can route values into that standard object as well as the standard profile. This example ingests product registrations.

Incoming object:

```
{
  "customerEmail": "jane@example.com",
  "serialNumber": "SN-987654",
  "productName": "Examplecorp AC 2200",
  "sku": "AC-2200",
  "purchaseDate": "2025-03-12",
  "status": "ACTIVE",
  "price": 449.00
}
```

Mapping:

```
{
    "Fields": {
        "emailAddress": {
            "Source": "_source.customerEmail",
            "Target": "_profile.PersonalEmailAddress",
            "ContentType": "EMAIL_ADDRESS"
        },
        "assetName": {
            "Source": "_source.productName",
            "Target": "_asset.AssetName"
        },
        "serialNumber": {
            "Source": "_source.serialNumber",
            "Target": "_asset.SerialNumber"
        },
        "productSKU": {
            "Source": "_source.sku",
            "Target": "_asset.ProductSKU"
        },
        "purchaseDate": {
            "Source": "_source.purchaseDate",
            "Target": "_asset.PurchaseDate"
        },
        "status": {
            "Source": "_source.status",
            "Target": "_asset.Status"
        },
        "price": {
            "Source": "_source.price",
            "Target": "_asset.Price",
            "ContentType": "NUMBER"
        }
    },
    "Keys": {
        "_email": [
            {
                "StandardIdentifiers": ["PROFILE"],
                "FieldNames": ["emailAddress"]
            }
        ],
        "productSerialNumber": [
            {
                "StandardIdentifiers": ["ASSET", "UNIQUE"],
                "FieldNames": ["serialNumber"]
            }
        ]
    }
}
```

What's new here:
+ **Two destinations.** One field targets `_profile.*`, the rest target `_asset.*`. A single mapping can write to the profile and to other standard objects at the same time.
+ **The pairing rule.** Because fields target `_asset.*`, at least one key must carry the `ASSET` identifier. Miss this and the mapping is rejected. The rule holds for every standard object.
+ **What `ASSET` does.** It tells Customer Profiles to look up the asset record whose `productSerialNumber` equals this value. One match, and the record attaches to that asset. More than one, and the ingestion is rejected as ambiguous. None, and a new asset record can be created.
+ **Two identifiers on one key.** `productSerialNumber` is both `ASSET` (which asset) and `UNIQUE` (which registration record). Re-registering the same serial number replaces the registration profile object and updates the same asset.
+ **Assets accumulate.** Another object type—warranty claims, service history—can target `_asset.*` too. Its values land alongside these on the same asset record.

Every standard object follows this pattern. Swap the identifier and the target prefix:


| To populate | Add this identifier to a key | Target fields at | 
| --- | --- | --- | 
| An asset | ASSET | \_asset.\* | 
| An order | ORDER | \_order.\* | 
| A case | CASE | \_case.\* | 
| A device | DEVICE | \_device.\* | 
| A loyalty membership | LOYALTY | \_loyalty.\* | 
| An air booking | AIR\_BOOKING | \_airBooking.\* | 

For the full list of standard objects and their identifiers, see [Reference for standard objects in Customer Profiles](standard-objects.md).

## Example 4: Link two object types together
<a name="example-link-object-types"></a>

Key names are global to the domain. Two object types that use the same key name for the same real-world identifier are linked—matching values put their data on the same profile and the same standard object. This example ingests service tickets that reference the assets registered in Example 3.

Incoming object:

```
{
  "ticketId": "SR-55021",
  "customerEmail": "jane@example.com",
  "assetSerialNumber": "SN-987654",
  "subject": "Unit not cooling",
  "description": "Customer reports the unit runs but does not cool.",
  "state": "Open",
  "openedAt": "2025-06-02T14:05:00.000Z"
}
```

Mapping:

```
{
    "Fields": {
        "emailAddress": {
            "Source": "_source.customerEmail",
            "ContentType": "EMAIL_ADDRESS"
        },
        "assetSerialNumber": {
            "Source": "_source.assetSerialNumber",
            "Target": "_case.Attributes.SerialNumber"
        },
        "ticketId": {
            "Source": "_source.ticketId"
        },
        "title": {
            "Source": "_source.subject",
            "Target": "_case.Title"
        },
        "summary": {
            "Source": "_source.description",
            "Target": "_case.Summary"
        },
        "status": {
            "Source": "_source.state",
            "Target": "_case.Status"
        },
        "createdDate": {
            "Source": "_source.openedAt",
            "Target": "_case.CreatedDate"
        }
    },
    "Keys": {
        "_email": [
            {
                "StandardIdentifiers": ["PROFILE"],
                "FieldNames": ["emailAddress"]
            }
        ],
        "productSerialNumber": [
            {
                "StandardIdentifiers": ["ASSET"],
                "FieldNames": ["assetSerialNumber"]
            }
        ],
        "serviceTicketId": [
            {
                "StandardIdentifiers": ["CASE", "UNIQUE"],
                "FieldNames": ["ticketId"]
            }
        ]
    }
}
```

What's new here:
+ **A shared key name links the two object types.** `productSerialNumber` is the same key name Example 3 used. When a ticket arrives with `SN-987654`, it attaches to the asset that the registration created. Had this mapping called the key `ticketSerialNumber`, the two would never connect.
+ **An identifier without a target.** This key carries `ASSET` but no field targets `_asset.*`. The pairing rule runs one way only: targeting a standard object requires its identifier, but carrying the identifier doesn't require targeting. Use it this way to associate a record with an existing entity without writing to it.
+ **Three standard objects, three roles.** `_email` finds the profile, `productSerialNumber` finds the asset, and `serviceTicketId` both identifies the case and identifies this profile object.
+ **Content types must agree.** `assetSerialNumber` has no `ContentType`, so it's `STRING`—the same as the field behind `productSerialNumber` in Example 3. A key name reused with a different content type is rejected.
+ **One field can do both jobs.** `assetSerialNumber` feeds the `productSerialNumber` key and writes to `_case.Attributes.SerialNumber`. A field carrying a `Target` can still be referenced by a key, so you don't need a second field for that. You would need one only if the same value had to reach two standard objects, since a field has exactly one `Target`.

**Important**  
**Share key names deliberately**  
A key name is a domain-wide index: two objects with the same key name and the same value land on the same profile, even when they come from different object types.  
So before reusing a name, ask whether a shared value really means a shared identity. An email address on a Salesforce contact and the same address on a ServiceNow user belong to one person, so use `_email` for both. But a Salesforce record ID of `12345` and a Marketo record ID of `12345` are unrelated records that happen to share a number—give those distinct names such as `salesforceContactId` and `marketoLeadId`, or you collapse two unrelated customers into one profile. For more information, see [Key definitions in Customer Profiles object type mappings](mapping-key-definitions.md).

## Before you submit
<a name="before-you-submit"></a>

Check your mapping against both lists. The first group is rejected when you create the object type. The second group is accepted, so nothing tells you it's wrong—the cost shows up later as poor matching.

**Rules the mapping must satisfy**


| Rule | Why | 
| --- | --- | 
| Exactly one key carries UNIQUE | It identifies the profile object instance. If no single value is distinct, list several fields in FieldNames so their combination is unique. | 
| At least one key carries PROFILE | Without it, an ingested object has no way to reach a profile. | 
| At least one PROFILE key has neither LOOKUP\_ONLY nor NEW\_ONLY | Guarantees an object can always be durably associated with a profile. Waived when AllowProfileCreation = false, and the \_profileId key is exempt. | 
| UNIQUE is not combined with LOOKUP\_ONLY or NEW\_ONLY | A key that identifies the object instance has to be stored, and those two identifiers prevent storage. | 
| Every standard object you target has its identifier on a key | Targeting \_asset.\* requires an ASSET key, \_case.\* requires CASE, and so on. The reverse isn't required. | 
| Every Target names a real field on the standard object | Check the standard object definition rather than guessing from the source field name. Values with no standard field go under Attributes. | 
| No Target is a system-managed ID | \_profile.ProfileId, \_asset.AssetId, \_case.CaseId, and the equivalent ID on every other standard object are assigned by Customer Profiles. Put your source's own ID in Attributes. | 
| Not both Gender and GenderString, or both PartyType and PartyTypeString | Each pair is mutually exclusive. Choose one of each. | 
| Every FieldNames entry names a field defined in this mapping | Keys can only reference fields from their own object type. | 
| A reused key name's field content types match the existing definition | Key names are domain-wide, so the same name must normalize values the same way everywhere it's used. | 
| 250 fields or fewer | Per-object-type limit. See [Quotas and data limits in Customer Profiles](customer-profiles-data-limits.md). | 

**Choices that are accepted but cause problems**


| Choice | What it costs | 
| --- | --- | 
| An indexed email, phone, name, or number with no ContentType | The value is treated as STRING and matched exactly as written, so the same phone number or address in another format won't match. | 
| A PROFILE key on a low-cardinality value | A value shared by many profiles matches ambiguously, gets discarded, and tends to produce inferred profiles instead. | 

Creating the object type successfully confirms it's structurally valid. To confirm it does what you intended, ingest a few representative records and check the results with `SearchProfiles` before pointing a full integration at it. For more information, see [Update and validate an object type mapping in Customer Profiles](update-and-validate-mapping.md). For error messages and the symptoms of a mapping that's already ingesting, see [Troubleshoot object type mappings in Customer Profiles](object-type-mapping-troubleshooting.md).