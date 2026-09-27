

# Profile matching and inferred profiles in Customer Profiles
<a name="profile-matching"></a>

This topic explains how Connect Customer Customer Profiles decides which profile an ingested object belongs to, when it creates a new profile, and how it protects manually entered data. For the end-to-end ingestion flow, see [How object type mapping works in Customer Profiles](how-object-type-mapping-works.md).

## How a profile is matched
<a name="how-a-profile-is-matched"></a>

An ingested object is validated and queued, and profile matching happens shortly afterward. Matching follows this order:

1. Customer Profiles evaluates each primary `PROFILE` key:
   + If exactly one profile matches, the object is attached to that profile.
   + If more than one profile matches, the match is ambiguous—that key is discarded and the next is tried.
   + If no profile matches, the next key is tried.

1. If no primary `PROFILE` key produces an unambiguous match, Customer Profiles repeats the process with any secondary keys (keys whose standard identifiers include both `PROFILE` and `SECONDARY`).

1. If no key produces a single match, the outcome depends on `AllowProfileCreation` (see [Controlling profile creation with AllowProfileCreation](#allow-profile-creation)).

**Note**  
An ambiguous match—a key value that points to more than one profile—is never used to attach an object. This prevents a shared value, such as a common email address, from silently merging unrelated profiles.

## Controlling profile creation with AllowProfileCreation
<a name="allow-profile-creation"></a>

`AllowProfileCreation` is a property of the object type that controls what happens when no profile matches:
+ **`true`**: a new inferred profile is created and the object is attached to it.
+ **`false`**: the object is rejected and sent to the domain dead-letter queue. Use this when you only want to enrich profiles that already exist, for example because they're created through a separate provisioning flow.

When you create an object type from a template, the template's `AllowProfileCreation` value is used and can't be overridden on the request.

## Inferred profiles
<a name="inferred-profiles"></a>

An inferred profile is a profile that Customer Profiles creates automatically when an ingested object can't be matched to any existing profile. Because the source object usually doesn't carry a full customer record, the standard profile object on an inferred profile starts mostly empty.

**What gets populated on an inferred profile**

When an inferred profile is created, the standard profile object is initialized from the fields in the object type mapping. Fields that define a `Target` are populated as usual. Two fields are also populated automatically, even when the field defines no `Target`:
+ A field with `ContentType` of `EMAIL_ADDRESS` populates `_profile.EmailAddress`.
+ A field with `ContentType` of `PHONE_NUMBER` populates `_profile.PhoneNumber`.

**Note**  
This automatic population happens only when an inferred profile is created, and it writes to the standard profile fields `_profile.EmailAddress` and `_profile.PhoneNumber`—not to the `_email` and `_phone` search keys. When an object matches an existing profile, a `ContentType` on its own writes nothing; only fields with a `Target` update the standard profile.

**Avoiding unwanted inferred profiles**

With inferred profiles, you can keep ingesting data even when the customer isn't already known, but they can accumulate when source data is sparse. To control this:
+ Set `AllowProfileCreation = false` if you only want to enrich existing profiles.
+ For contact records, choose a template that suppresses inferred profile creation. For more information, see [Contact record templates in Connect Customer Customer Profiles](ctr-contact-record-template.md).
+ Use `SECONDARY` and `NEW_ONLY` identifiers thoughtfully so a single weak signal (such as an email shared by many profiles) doesn't force a new profile. For more information, see [Standard identifiers in Customer Profiles](standard-identifiers.md).

## Merging behavior and source priority
<a name="source-priority"></a>

When an object matches an existing profile, its `Target` fields update the standard profile object. When multiple object types map to the same standard field—for example, both a Salesforce and a Marketo mapping populate `_profile.EmailAddress`—`SourcePriority` determines which value wins. `SourcePriority` is an integer where `1` is the highest priority—object types with lower values take precedence. An object type without a `SourcePriority` defaults to the lowest priority.

## Manual updates are protected by default
<a name="manual-updates-protected"></a>

**Note**  
By default, an ingested object that matches an existing profile doesn't overwrite fields populated manually through the [UpdateProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateProfile.html) API or the Connect Customer agent workspace. This protects intentional changes from being silently replaced by automated ingestion. Use `SourcePriority` when you do want a trusted ingestion source to take precedence over manual updates.

For example, suppose an agent creates a profile with `FirstName` set to `John`. Later, an object that maps to `_profile.FirstName` is ingested and matched to that profile. If the ingesting object type has no `SourcePriority` configured, the `FirstName` value remains `John`—the ingested value is stored on the profile object but doesn't replace the manually set standard field. If you configure `SourcePriority` to rank that object type above manual updates, the ingested value replaces `John` instead.