

# How object type mapping works in Customer Profiles
<a name="how-object-type-mapping-works"></a>

This topic describes what happens to your data from the moment it's ingested to the moment it becomes part of a unified, searchable profile. Understanding this flow helps you design mappings that match objects to the right profiles and avoid unwanted duplicate profiles.

## How your data flows through Customer Profiles
<a name="object-type-mapping-data-flow"></a>

An object type mapping is the bridge between your raw data and a unified profile. At a high level, data moves through four stages:

1. **Source data** arrives from a connector (Salesforce, Zendesk, Amazon S3, Connect Customer contact records, your own application, and so on).

1. The **object type mapping** defines fields that extract values from the source object and keys that identify which profile (and which standard objects, if any) the data belongs to.

1. Customer Profiles uses the keys to look up an existing profile or create a new one, populates the **standard profile object** (and any other targeted standard objects, such as `_asset` or `_order`) from the field targets, and stores the original source data as a profile object.

1. The resulting **unified profile** is searchable by every key you defined and is available to downstream applications.

![A flow diagram showing four stages: source data from Salesforce, Zendesk, S3, and contact records flows into an object type mapping of fields and keys, then to profile matching to find or create a profile, resulting in a unified, searchable profile with a standard profile object and indexed keys.](https://docs.aws.amazon.com/connect/latest/adminguide/images/object-type-mapping-overview.png)


## The ingestion sequence
<a name="otm-ingestion-sequence"></a>

Each ingested object moves through three conceptual stages:

1. **Field extraction**: Customer Profiles reads each field's `Source` expression from the object type mapping and pulls the corresponding value out of the incoming JSON. Fields that define a `Target` are written to the standard object the target points to—the standard `_profile`, or another standard object such as `_asset`, `_order`, or `_loyalty`. For most fields, the `Source` is a JSON accessor (for example, `_source.FirstName`); advanced cases can use Handlebars to combine or transform values. For more information, see [Field definitions in Customer Profiles object type mappings](mapping-field-definitions.md) and [Reference for standard objects in Customer Profiles](standard-objects.md).

1. **Key computation**: For each key defined in the mapping, Customer Profiles combines the referenced field values and normalizes them according to each field's `ContentType` (for example, phone numbers and email addresses are normalized so different formats match). This produces a comparable value for each key, categorized by its standard identifier role—`UNIQUE`, `PROFILE`, `SECONDARY`, and so on. For more information, see [Standard identifiers in Customer Profiles](standard-identifiers.md).

1. **Profile resolution**: Customer Profiles uses the computed key values to decide which profile the object belongs to, following the decision tree below.

## Profile resolution decision tree
<a name="profile-resolution-decision-tree"></a>

Customer Profiles resolves the target profile in this order:

1. Evaluate each primary `PROFILE` key against the domain's existing keys:
   + If exactly one profile matches, the object is attached to that profile.
   + If more than one profile matches, the match is **ambiguous**—that key is discarded and the next key is tried.
   + If no profile matches, the next `PROFILE` key is tried.

1. If no primary `PROFILE` key produces an unambiguous match, repeat the evaluation with any secondary keys—keys whose standard identifiers include both `PROFILE` and `SECONDARY`.

1. If no key—primary or secondary—produces a single match, the outcome depends on the object type's `AllowProfileCreation` setting:
   + `AllowProfileCreation = true`: a new inferred profile is created and the object is attached to it.
   + `AllowProfileCreation = false`: the object is rejected and sent to the domain dead-letter queue.

![A decision flow chart for profile resolution. Compute PROFILE keys, then match primary PROFILE keys: exactly one match attaches to that profile; none or ambiguous continues to match SECONDARY keys. Exactly one secondary match attaches to that profile; none or ambiguous continues to the AllowProfileCreation decision. If true, a new inferred profile is created; if false, the object is rejected to the dead-letter queue.](https://docs.aws.amazon.com/connect/latest/adminguide/images/profile-resolution-decision-flow-chart.png)


**Note**  
An *ambiguous* match (a key value that points to more than one profile) is never used to attach an object. This prevents a common value—such as a shared email address—from silently writing to unrelated profiles. For more information, see [Profile matching and inferred profiles in Customer Profiles](profile-matching.md).

## What happens after a profile is resolved
<a name="after-profile-resolved"></a>
+ The source object is stored as a profile object on the resolved profile. This profile object is identified by its `UNIQUE` key—re-ingesting an object with the same `UNIQUE` value replaces the previous profile object wholesale.
+ Field values that define a `Target` are written to the corresponding standard object (the standard profile, or a non-profile standard object such as `_asset`, `_order`, or `_loyalty`). Standard objects are not replaced wholesale—each ingestion contributes only the fields it carries, and many profile objects can write to the same standard object over time.
+ Targets that were set manually by an agent or by the [UpdateProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateProfile.html) API aren't overwritten by ingestion by default. To let an ingested value take precedence over a manual update, configure `SourcePriority` on the object type. When several sources write to the same standard field, `SourcePriority` determines which value wins. For more information, see [Merging behavior and source priority](profile-matching.md#source-priority).
+ All `PROFILE` and `SECONDARY` keys are stored so the profile can be found by those values later. `LOOKUP_ONLY` keys are not stored.

**Note**  
**Wholesale replace compared with incremental update**  
A *profile object* (what you ingested) is replaced wholesale by the next object with the same `UNIQUE` key. A *standard object* (such as `_profile`, `_asset`, or `_order`) accumulates: it keeps fields previously written and updates only the fields the new object provides. This is why the same asset can be enriched over time by data from multiple object types.

For details on the merge and overwrite rules, see [Profile matching and inferred profiles in Customer Profiles](profile-matching.md).