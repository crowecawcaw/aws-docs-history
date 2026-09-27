

# Object type mapping terminology and concepts
<a name="customer-profiles-terminology"></a>

The following terms are central to understanding object type mapping in Connect Customer Customer Profiles. Each term links to the topic where it's covered in depth.

**Domain**  
A *domain* is the top-level container for your unified customer data. Each domain belongs to a single AWS account and holds its own profiles, object types, keys, encryption settings, and retention configuration. You must create a domain before you can create object types or ingest data. All object types and keys you define are scoped to that domain.

**Profile**  <a name="Profile"></a>
A *profile* contains all the information known about a specific customer or contact. Each profile includes a single standard profile object and any number of additional profile objects.

**Standard profile object**  <a name="StandardProfileObject"></a>
A *standard profile object* is a predefined object that every profile contains. It holds standard fields such as `FirstName`, `LastName`, `PhoneNumber`, `EmailAddress`, `ShippingAddress`, and custom `Attributes`. Because the format is fixed, applications can read profile data the same way regardless of the original source (for example, Salesforce, ServiceNow, or Marketo).

**Standard object**  
A *standard object* is a predefined record with a fixed schema that Customer Profiles maintains alongside (or as part of) a profile. The standard profile object is one example; other standard objects represent business entities like assets, orders, cases, loyalty memberships, and travel records. Field `Target` values write into a standard object—for example, `_asset.SerialNumber` or `_case.Reason`. For more information, see [Reference for standard objects in Customer Profiles](standard-objects.md).

**Profile object**  <a name="ProfileObject"></a>
A *profile object* is a single unit of source data attached to a profile—for example, a phone call, a support ticket, or a click-stream record. A profile object can be up to 250 KB and can be any structured JSON document. Profile objects are what you ingest with [PutProfileObject](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_PutProfileObject.html).  
+ Every profile object has a type, such as an Connect Customer contact record, a ServiceNow user, or a Marketo lead.
+ The type refers to an object type mapping.
+ The object type mapping defines how that object is ingested into Customer Profiles.
+ A profile object is identified by its `UNIQUE` key. Re-ingesting an object with the same `UNIQUE` value replaces the previous profile object wholesale.

**Object type mapping**  <a name="ObjectTypeMapping"></a>
An *object type mapping* tells Customer Profiles how to ingest a specific type of data: how source values populate the standard profile object and standard objects, and which fields are indexed and used to assign objects to a profile. For more information, see [Field definitions in Customer Profiles object type mappings](mapping-field-definitions.md) and [Key definitions in Customer Profiles object type mappings](mapping-key-definitions.md).

**Field**  
A *field* defines a single piece of data extracted from a source object. Each field specifies a **source** (where to read the value), an optional **target** (where to write it in the standard profile object), and a **content type** (how to normalize it for search and matching). For more information, see [Field definitions in Customer Profiles object type mappings](mapping-field-definitions.md).

**Key**  
A *key* is a named combination of one or more fields used to find profiles or objects. Keys are global to a domain, so the same key name in two object type mappings refers to the same logical identifier. Keys drive profile matching during ingestion and power lookups with the [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) API. For more information, see [Key definitions in Customer Profiles object type mappings](mapping-key-definitions.md).

**Standard identifier**  
A *standard identifier* is a tag applied to a key that defines its role during ingestion—for example, `UNIQUE` (identifies the object instance), `PROFILE` (used to match a profile), or `LOOKUP_ONLY` (used to match but not stored). For the full list and combination rules, see [Standard identifiers in Customer Profiles](standard-identifiers.md).

**Content type**  
A *content type* tells Customer Profiles how to normalize a field value so searches and matches work across formats. Supported values are `STRING`, `NUMBER`, `PHONE_NUMBER`, `EMAIL_ADDRESS`, and `NAME`. For example, a `PHONE_NUMBER` field is normalized so `+15551234567` matches `(555)-123-4567`.

**Inferred profile**  
An *inferred profile* is a profile that Customer Profiles creates automatically when an ingested object can't be matched to any existing profile. Its standard profile object starts mostly empty—only fields Customer Profiles can populate from the ingested object (such as phone or email) are filled in. For more information, see [Profile matching and inferred profiles in Customer Profiles](profile-matching.md).

**Mapping template**  <a name="MappingTemplate"></a>
A *mapping template* is a predefined object type mapping that ships with Customer Profiles for well-known source objects, such as Connect Customer contact records, Salesforce accounts, ServiceNow users, and Marketo leads. Templates let you ingest data from these sources without defining fields or keys yourself. For the complete list, use the [ListProfileObjectTypeTemplates](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjectTypeTemplates.html) API. For more information, see [Mapping templates and implicit object types in Customer Profiles](templates-and-implicit-types.md).