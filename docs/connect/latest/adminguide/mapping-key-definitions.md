

# Key definitions in Customer Profiles object type mappings
<a name="mapping-key-definitions"></a>

A key contains one or more fields that together form an identifier you can use to search for objects (or the profiles they belong to) with the [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) API. A key can also be defined to uniquely identify a profile or the object itself. For field definitions, see [Field definitions in Customer Profiles object type mappings](mapping-field-definitions.md).

```
"Keys": {
    "{keyName}": [{
        "StandardIdentifiers": [...],
        "FieldNames": [ "{fieldName}", ...]
    }], ...
}, ...
```

## How keys are used
<a name="how-keys-are-used"></a>

Key definitions are used in two ways:
+ **During ingestion**: Customer Profiles uses keys to decide which profile an object attaches to, or whether to create a new profile. For more information, see [How object type mapping works in Customer Profiles](how-object-type-mapping-works.md).
+ **After ingestion**: you can use keys with the [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) API to find a profile by value.

## Key names are global to a domain
<a name="key-names-global-to-domain"></a>

If you have two keys with the same name in two different object type mappings:
+ They share the same namespace.
+ They can link profiles together across object types. If they match between objects, Customer Profiles places the two objects in the same profile.

The rule for naming keys: use the **same key name** across object types only when matching values mean the objects belong to the same profile. Use **different key names** when matching values are coincidental.

Two examples:
+ **Same name.** A phone number on a Salesforce contact and the same phone number on a ServiceNow user identify the same person, so name both keys `_phone`. Customer Profiles places both objects on the same profile.
+ **Different names.** A Salesforce internal record ID and a Marketo internal record ID happen to be numbers, but a match is coincidental—the records aren't related. Give them different key names (for example, `salesforceId` and `marketoId`) so Customer Profiles doesn't merge unrelated profiles.

## Multiple definitions for one key name
<a name="multiple-key-definitions"></a>

The value of a key is an array of definitions, so the same key name can have more than one entry, each with its own `FieldNames` and `StandardIdentifiers`. Multiple definitions are useful when you want the same logical key to be populated from different field combinations or behave differently in different scenarios.

**Note**  
Each entry in a key's array counts toward your account's per-object-type key limit. For more information, see [Quotas and data limits in Customer Profiles](customer-profiles-data-limits.md).

## Default search keys
<a name="object-type-mapping-default-search-keys"></a>

Default search keys, such as `_phone` and `_email`, are predefined by the [Standard Profile](standard-profile-definition.md), [Standard Asset](standard-asset-definition.md), [Standard Order](standard-order-definition.md), and [Standard Case](standard-case-definition.md) object templates. You can use them as a key name with the [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) API to find a profile.

## Key naming and structural rules
<a name="key-naming-rules"></a>
+ Key names must start with a letter (same character set as field names) *or* start with an underscore for predefined system keys.
+ Underscore-prefixed key names must already be defined as a domain key (for example, `_phone`, `_email`).
+ `Tags` and `tags` can't be used as key names.
+ Each key must reference at least one field, and every referenced field must be defined in the same object type.
+ If a key name already exists in the domain, the new definition's field content types must match the existing definition.
+ Each object type must have exactly one key with a `UNIQUE` identifier and at least one key with a `PROFILE` identifier. For more information, see [Standard identifiers in Customer Profiles](standard-identifiers.md).