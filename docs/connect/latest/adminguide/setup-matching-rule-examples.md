# Set up matching rules for rule-based

Identity Resolution in Amazon Connect

## Limits

You can select any attribute from the standard profile to compare similar
profiles. For example, you might choose phone number, email address, and
name, as well as custom attributes.

You can create a rule-based matching rule with the following limitations:

- 15 rule levels
- Each rule level can contain up to 15 profile attributes

## Tips

To improve the targeting of unique profiles and to avoid consolidating
profiles that are not duplicates, the following tips are recommended:

- Include at least one high cardinality attribute that can uniquely
  identify a customer and that is not likely to be the same across
  customers, such as a phone number, an email address or an account
  number.
- Avoid using profile attributes that can belong to different
  identities without a high cardinality attribute.
  - **Phone number** with **First
    name**, **Last name** is a
    stronger rule than the combination of **First
    name**, **Last name**
    alone.

- If at one rule level, all of the profile attributes of that rule
  are low cardinality attributes (the attribute that can belong to
  more than 500 different profiles), Customer Profiles does not attempt to match
  the profile. You will receive the following SQS message in your DLQ
  if you setup one during the domain creation:
  - All attributes at rule level x are associated with more
    than 500 records.

- Always enable **Match only** first, check the
  match results, and only enable the merging by setting the
  **MaxAllowedRuleLevelForMerging** if you are
  satisfied with the match results.

## Resolve

profile conflicts for profile merging

You can define which record to use when the value of an attribute from two
or more similar profiles is different, such as conflicting address
records.

**Last updated timestamp**

By default, profile conflicts are managed by recency. When there is a
conflict between the values of two or more similar profiles, the most
recently updated attribute will be chosen.

**Source with last updated timestamp**

Allows you to prioritize records from a specific object type as your data
source for managing profile conflicts. When there is a conflict between the
values of two or more similar profiles, the most recently updated attribute
from the specified object type will be chosen.

If a timestamp is not specified in your object type, the date the record
was ingested into Customer Profiles will be used. Source with last updated timestamp is
unavailable when you don't have any integrations set up. When you add an
integration, your object types will be available as a source for this
option.

## Missing timestamp for profile conflicts

The Missing timestamp message is displayed if you have custom object type
mappings.

Use the [PutProfileObjectType](../../../customerprofiles/latest/APIReference/API_PutProfileObjectType.md "../../../customerprofiles/latest/APIReference/API_PutProfileObjectType.md") API to add the following new attributes to
your custom object type:

- `Fields.sourceLastUpdatedTimestamp`
- `sourceLastUpdatedTimestampFormat`

If the timestamp attribute is not specified, you can continue to create
consolidation criteria, however, a default timestamp of when the records
were ingested into Customer Profiles is used. It is recommended to add the new attributes
before creating your consolidation criteria.

If you have already defined a custom object type and want to update your
custom object type, we run a scheduled backfill every week to update your
existing profiles with the `Fields.sourceLastUpdatedTimestamp`.
To opt in to the scheduled backfill, use the following steps:

1. Update your custom profile object type by using the [PutProfileObjectType](../../../customerprofiles/latest/APIReference/API_PutProfileObjectType.md "../../../customerprofiles/latest/APIReference/API_PutProfileObjectType.md") API.
2. After you update your custom profile object type, open an [AWS Support
   ticket](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home").
3. AWS will schedule the backfill on your behalf. The
   scheduled backfill runs until end of February 2022.

Alternatively, you can delete and then re-create the ingestion/connector
you have for your domain that uses the custom object type. All of your data
will be re-ingested using your updated object type and
`Fields.sourceLastUpdatedTimestamp` will be parsed from
it.

## Example:

How matching works

### Example for

ONE_TO_ONE

You can choose `ONE_TO_ONE` as the
`AttributeMatchingModel`. When choosing
`ONE_TO_ONE` the system can only match if the sub-types
are exact matches.

**For example**:

You are using the `EmailAddress` and
`BusinessEmailAddress` to represent the
`EmailAddress` types. The
`AttributeMatchingModel` is
`ONE_TO_ONE`.

**Your matching rule is**:

```

Rule Level 1: EmailAddress, LastName, FirstName
Rule Level 2: AccountNumber

```

```

Profile A:
EmailAddress: 1@email.com
BusinessEmailAddress: john@company.com
LastName: Doe
FirstName: John
AccountNumber: account1234

```

```

Profile B:
EmailAddress: 2@email.com
BusinessEmailAddress: john@company.com
LastName: Doe
FirstName: John
AccountNumber: account1234

```

The Profile A and Profile B matches at rule level 1 since the
`EmailAddress` type, `LastName`, and
`FirstName` match.

### Example for

MANY_TO_MANY

You can choose `MANY_TO_MANY` as the
`AttributeMatchingModel`. When choosing
`MANY_TO_MANY`, the system can match attributes across
the sub-types of an attribute type.

**For example**:

You are using the `EmailAddress` and
`BusinessEmailAddress` to represent the
`EmailAddress` types. The
`AttributeMatchingModel` is
`MANY_TO_MANY`.

**Your matching rule is**:

```

Rule Level 1: EmailAddress, LastName, FirstName
Rule Level 2: AccountNumber

```

```

Profile A:
EmailAddress: 1@email.com  (match with Profile B’s BusinessEmailAddress)
BusinessEmailAddress: john@company.com
LastName: Doe
FirstName: John
AccountNumber: account1234


```

```

Profile B:
EmailAddress: 2@email.com
BusinessEmailAddress: 1@email.com (match with Profile A's EmailAddress)
LastName: Doe
FirstName: John
AccountNumber: account1234


```

The Profile A and Profile B matches at rule level 1 since the
`EmailAddress` type, `LastName`, and
`FirstName` match.
