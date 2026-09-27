

# Troubleshoot object type mappings in Customer Profiles
<a name="object-type-mapping-troubleshooting"></a>

This topic covers common issues when creating mappings, ingesting objects, and generating mappings with AI.

## Mapping creation and validation errors
<a name="mapping-validation-errors"></a>

Connect Customer Customer Profiles validates a mapping when you create or update it and rejects an invalid one before any data is ingested. The error message names the specific problem—a missing or wrongly combined identifier, an unsupported target, a name that breaks the character rules, or a quota you've reached.

For the rules a mapping has to satisfy, and for the choices that are accepted but quietly degrade matching, see [Before you submit](examples-object-type-mappings.md#before-you-submit). For the syntax behind each part of a mapping, see [Field definitions in Customer Profiles object type mappings](mapping-field-definitions.md), [Key definitions in Customer Profiles object type mappings](mapping-key-definitions.md), [Standard identifiers in Customer Profiles](standard-identifiers.md), and [Reference for standard objects in Customer Profiles](standard-objects.md).

## Object ingestion errors
<a name="object-ingestion-errors"></a>


| Symptom | Likely cause and fix | 
| --- | --- | 
| Object rejected as invalid | The submitted object isn't valid JSON, or it can't be parsed against the object type's fields. Verify the request body is well-formed JSON matching the field Source paths. | 
| Missing unique or profile key | Every field that makes up the UNIQUE key, or every PROFILE key, resolved to empty for this object. Ensure the source data contains the values those keys depend on. See [Field definitions in Customer Profiles object type mappings](mapping-field-definitions.md). | 
| Standard object type rejected at ingestion | PutProfileObject can't be called with a standard object type name (such as \_profile, \_asset, or \_order). Standard objects aren't ingested directly—they're populated as a result of ingesting a custom object type whose fields target them. To create or update a profile directly, use CreateProfile or UpdateProfile. See [Reference for standard objects in Customer Profiles](standard-objects.md). | 

## An object wasn't associated with the expected profile
<a name="object-not-associated-expected-profile"></a>

If an ingested object landed on the wrong profile or created a new one unexpectedly, check the following:
+ **Ambiguous match**: If a `PROFILE` key value matched more than one profile, Customer Profiles discards that key. Make sure the key you rely on for matching is unique enough to identify a single profile. See [Profile matching and inferred profiles in Customer Profiles](profile-matching.md).
+ **Normalization mismatch**: Matching uses the field's `ContentType`. A phone or email that isn't tagged with the right content type might not match a value stored in another format. See [Field definitions in Customer Profiles object type mappings](mapping-field-definitions.md).
+ **LOOKUP\_ONLY / NEW\_ONLY keys**: A key with `LOOKUP_ONLY` is never stored, and `NEW_ONLY` is stored only on newly created profiles. If you expected to match on such a key later, it might not have been saved. See [Standard identifiers in Customer Profiles](standard-identifiers.md).
+ **Ingestion timing**: Ingestion takes a short time to complete. If you searched immediately after ingesting, the association might not have finished yet. See [Profile matching and inferred profiles in Customer Profiles](profile-matching.md).
+ **Profile creation disabled**: If `AllowProfileCreation` is `false` and no profile matched, the object was sent to the domain dead-letter queue instead of creating a profile.

You can use [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) to confirm which key values are associated with which profiles.

## Old field values are still on a standard object after ingestion
<a name="stale-standard-object-values"></a>

Standard objects (such as the standard profile, `_asset`, or `_order`) are not replaced wholesale on ingestion—they accumulate field values across many profile objects. Re-ingesting a profile object with the same `UNIQUE` key replaces only that profile object; the standard object keeps every field that was previously written and updates only the fields the new ingestion targets.

If a standard field looks "stale," check:
+ **Targeting**: Make sure the field you want to overwrite is actually targeted in the new ingestion's mapping. A field with no `Target` doesn't write to the standard object.
+ **SourcePriority**: When several object types target the same standard field, `SourcePriority` decides which value wins. A lower-priority source can't overwrite a higher-priority one. See [Merging behavior and source priority](profile-matching.md#source-priority).
+ **Manual overrides**: By default, values set with [UpdateProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateProfile.html) or in the Connect Customer agent workspace aren't overwritten by ingestion. If you need an ingested value to win, configure `SourcePriority` on the object type. See [Manual updates are protected by default](profile-matching.md#manual-updates-protected).
+ **Empty source values**: A field whose `Source` resolves to empty is treated as absent—it won't blank out an existing value on the standard object.

To explicitly clear a profile field, use `UpdateProfile`. For more information, see [How object type mapping works in Customer Profiles](how-object-type-mapping-works.md) and [Reference for standard objects in Customer Profiles](standard-objects.md).

## Generative AI mapping errors
<a name="genai-powered-data-mapping-troubleshooting"></a>

These errors and warnings can appear when generating a mapping with generative AI. For more information, see [Generate a mapping with generative AI in Customer Profiles](genai-powered-data-mapping.md).

### Error: Could not parse object string into JSON
<a name="genai-powered-data-mapping-parse-object-error"></a>

The object string in the request isn't valid JSON. Review it and verify that it's valid JSON.

### Error: Value at 'objects' failed to satisfy constraint: Member must have length less than or equal to 5
<a name="genai-powered-data-mapping-failed-constraint-error"></a>

There are too many objects in the request. Up to five are allowed. Reduce the number of objects to five or fewer.

### Error: Breached limit of 120 attributes
<a name="genai-powered-data-mapping-breached-limit"></a>

Up to 120 attributes are allowed in a JSON object, including nested attributes. Remove attributes that don't need to be mapped.

![Up to 120 attributes are allowed in a JSON object, including nested JSON attributes.](https://docs.aws.amazon.com/connect/latest/adminguide/images/genai-augmented-data-mapping-breached-limit.png)


### Warning: We couldn't find a **unique key**, which distinguishes your data. We couldn't find a **profile key**, which identifies your profiles.
<a name="genai-powered-data-mapping-unique-key-warning"></a>

The model couldn't determine a valid object type from the given object. Change the input or use the manual mapping approach. For more information, see [Create an object type mapping in the Connect Customer console](create-mapping-console.md).

![The model could not find a valid object type from given object. Change the input or use manual mapping approach as suggested.](https://docs.aws.amazon.com/connect/latest/adminguide/images/genai-augmented-data-mapping-unique-key-warning.png)
