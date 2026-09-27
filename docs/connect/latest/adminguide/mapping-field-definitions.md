

# Field definitions in Customer Profiles object type mappings
<a name="mapping-field-definitions"></a>

An object type mapping has two parts: field definitions and key definitions. This topic covers field definitions. For keys, see [Key definitions in Customer Profiles object type mappings](mapping-key-definitions.md).

A field defines a single piece of data extracted from a source object. Each field specifies a source, an optional target, and a content type:

```
"Fields": {
    "{fieldName}": {
        "Source": "{source}",
        "Target": "{target}",
        "ContentType": "{contentType}"
    }, ...
}, ...
```

**Tip**  
To learn how to build a mapping end to end, see this blog post: [Unify and organize customer information with Connect Customer Customer Profiles with the pre-built Amazon S3 connector](https://aws.amazon.com/blogs/contact-center/unify-and-organize-customer-information-with-amazon-connect-customer-profiles-with-the-pre-built-amazon-s3-connector/).

## Source
<a name="mapping-field-source"></a>

The `Source` tells Customer Profiles where to read the field's value from the incoming object. Customer Profiles parses the source object as `_source`, so all source paths must be prefaced by this name. Only the `_source` object is supported.

Most fields use a simple JSON accessor:

```
"FirstName": {
    "Source": "_source.FirstName",
    "Target": "_profile.FirstName",
    "ContentType": "STRING"
}
```

Nested paths work the same way—for example, `_source.Address.City`. JSON accessors cover the majority of mapping use cases.

**Advanced: Handlebars expressions**

The `Source` field also accepts Handlebars expressions, written between double curly braces. Use Handlebars when you need to:
+ Combine multiple source fields into one value (for example, building a key from email and timestamp).
+ Insert a constant or apply conditional logic.
+ Iterate over an array in the source.

Supported expressions:
+ **Variable interpolation**: `{{_source.FirstName}}`
+ **Nested paths**: `{{_source.Address.City}}`
+ **String concatenation**: `{{_source.FirstName}} {{_source.LastName}}`
+ **Conditional rendering**: `{{#if _source.MiddleName}}...{{/if}}`
+ **Iteration**: `{{#each _source.items}}...{{/each}}`
+ **Inverse conditional**: `{{#unless _source.OptOut}}...{{/unless}}`
+ **Context switching**: `{{#with _source.Address}}...{{/with}}`
+ **`removeExtraSpace` block helper**: collapses extra whitespace when some inputs might be missing. For example, `{{#removeExtraSpace}}{{_source.FirstName}} {{_source.MiddleName}} {{_source.LastName}}{{/removeExtraSpace}}` produces a clean full name even when `MiddleName` is empty.

**Note**  
A `Source` with invalid Handlebars syntax is rejected when the object type is created. If a source path doesn't exist in an incoming object at ingestion time, the field's value is treated as empty. If every field that makes up a `UNIQUE` or `PROFILE` key is empty, the object is rejected. For more information, see [Troubleshoot object type mappings in Customer Profiles](object-type-mapping-troubleshooting.md).

## Target
<a name="mapping-field-target"></a>

The `Target` specifies which **standard object** the field's value writes to (for example, `_profile.FirstName` or `_asset.SerialNumber`). Standard objects are predefined records with fixed schemas, so applications built on Customer Profiles can read your data without needing to know its original format. For more information, see [Reference for standard objects in Customer Profiles](standard-objects.md).

Fields targeting a standard object don't replace that standard object wholesale—each ingestion updates only the fields it carries. Many profile objects (across one or more object types) can contribute to the same standard object over time. The profile object itself, however, is identified by its `UNIQUE` key and is replaced wholesale on re-ingestion.

`Target` is optional. You might define fields solely for use inside a key. The format is always a JSON accessor.

**Supported target object types**
+ `_profile` (the standard profile object)
+ `_asset`, `_case`, `_order`, `_communicationRecord`
+ `_airPreference`, `_hotelPreference`, `_airBooking`, `_airSegment`, `_hotelReservation`, `_hotelStayRevenue`
+ `_loyalty`, `_loyaltyTransaction`, `_loyaltyPromotion`
+ `_device`, `_webAnalytics`

**Common \_profile targets**
+ `_profile.FirstName`, `_profile.LastName`
+ `_profile.PhoneNumber`, `_profile.EmailAddress`, `_profile.PersonalEmailAddress`
+ `_profile.AccountNumber`
+ `_profile.ShippingAddress.Address1`, `_profile.ShippingAddress.PostalCode`, `_profile.ShippingAddress.City` (the `MailingAddress` block follows the same pattern)
+ `_profile.Gender` or `_profile.GenderString` (mutually exclusive)
+ `_profile.PartyType` or `_profile.PartyTypeString` (mutually exclusive)
+ `_profile.SourceLastUpdatedTimestamp`
+ `_profile.Attributes.{customName}` for custom attributes

**Targets that are not allowed**

The following targets are reserved for system use and can't be specified as a field target:
+ Any standard object ID, such as `_profile.ProfileId`, `_asset.AssetId`, `_case.CaseId`, `_order.OrderId`, `_communicationRecord.CommunicationRecordId`, and the equivalent ID field on every other standard object type.
+ `_profile.ImportIds`
+ `_profile.FoundByItems[]`

**Note**  
You can't map fields to both `_profile.PartyType` and `_profile.PartyTypeString`, or to both `_profile.Gender` and `_profile.GenderString`. Choose one of each pair.

## ContentType
<a name="mapping-field-contenttype"></a>

The supported values are `STRING`, `NUMBER`, `PHONE_NUMBER`, `EMAIL_ADDRESS`, and `NAME`. If no `ContentType` is specified, `STRING` is assumed.

`ContentType` determines how the value is normalized for indexing and matching. For example, when `ContentType` is `PHONE_NUMBER`, agents can search in any format—`+15551234567` matches `(555)-123-4567`. When `ContentType` is `EMAIL_ADDRESS`, matches are case-insensitive.

A `ContentType` on its own doesn't write anything to the standard profile—only a `Target` does. The one exception is inferred profile creation, where `EMAIL_ADDRESS` and `PHONE_NUMBER` values populate the new profile automatically. For more information, see [Profile matching and inferred profiles in Customer Profiles](profile-matching.md).

## Field naming and structural rules
<a name="mapping-field-naming-rules"></a>
+ Field names must start with a letter and contain only letters, digits, underscores, dots, or hyphens.
+ `Tags` and `tags` can't be used as field names.
+ An object type can define up to 250 fields. For more information, see [Quotas and data limits in Customer Profiles](customer-profiles-data-limits.md).
+ If any field targets `_profile.SourceLastUpdatedTimestamp`, you must also provide `SourceLastUpdatedTimestampFormat`—either the literal `EpochMilli` or a valid `SimpleDateFormat` pattern. Only that exact target requires the format; targeting another standard object's `SourceLastUpdatedTimestamp` does not.