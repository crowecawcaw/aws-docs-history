

# Update and validate an object type mapping in Customer Profiles
<a name="update-and-validate-mapping"></a>

This topic explains how object type mappings change over time and how Connect Customer Customer Profiles validates them, so you can update a mapping with confidence and avoid surprises in already-ingested data.

## Upsert semantics
<a name="mapping-upsert-semantics"></a>

Object type creation uses upsert semantics: creating an object type whose name already exists updates the existing definition rather than failing. The same [PutProfileObjectType](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_PutProfileObjectType.html) API (and the console's data-mapping editor) is used for both creating and updating.

## What happens to existing data when you update
<a name="mapping-update-behavior"></a>

**Important**  
Updating a mapping doesn't automatically reprocess data that was previously ingested. A new or changed mapping applies only to objects ingested after the update.

Keep these behaviors in mind when updating:
+ **Retention**: Changing `ExpirationDays` only affects newly ingested data. Existing objects keep the retention they were ingested with.
+ **Tags**: Tags can't be changed through the update path. Use [TagResource](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UntagResource.html) instead.
+ **Encryption key**: After Data store is enabled on the domain, the encryption key for an existing object type can't be changed.
+ **Unused keys**: If you remove a key reference and no other object type in the domain still references that key, Customer Profiles cleans up the unused domain key.
+ **Key consistency**: If a key name already exists in the domain, the updated definition's field content types must match the existing definition.

## Test a mapping before a full integration
<a name="test-mapping-before-integration"></a>

To validate your mapping against real data safely, we recommend the following:

1. Create the object type mapping. Successful creation confirms the mapping is structurally valid.

1. Ingest a small batch of representative source objects with [PutProfileObject](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_PutProfileObject.html).

1. Use [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) to confirm the objects landed on the expected profiles and that the standard profile fields were populated as intended.

1. Adjust the mapping and repeat before pointing a full integration at it.