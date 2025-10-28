# How rule-based Identity Resolution works

in Amazon Connect

This topic describes how rule-based Identity Resolution performs automatic profile matching and how
it automatically merges similar profiles.

## Automatic profile

matching

To identify similar profiles, the rule-based Identity Resolution uses a list of
[matching rule attributes](../../../customerprofiles/latest/APIReference/API_MatchingRule.md "../../../customerprofiles/latest/APIReference/API_MatchingRule.md") to match each profile. Up to 15
MatchingRule attributes are supported in the [MatchingRules](../../../customerprofiles/latest/APIReference/API_RuleBasedMatchingRequest.md#customerprofiles-Type-RuleBasedMatchingRequest-MatchingRules "../../../customerprofiles/latest/APIReference/API_RuleBasedMatchingRequest.md#customerprofiles-Type-RuleBasedMatchingRequest-MatchingRules").

### Matching rules

The following is a list of the [MatchingRule](../../../customerprofiles/latest/APIReference/API_MatchingRule.md "../../../customerprofiles/latest/APIReference/API_MatchingRule.md") attributes that can be used. You can configure
up to 15 matching rule levels. For each matching rule, you can use the
following Personal Identifiable Information (PII) attributes in each
profile:

- **AccountNumber**
- **Address.Address**: All
  addresses specified in the [Attribute Type
  Selector](#rule-based-attribute-type-selector "#rule-based-attribute-type-selector") are
  reviewed for similarity, including Address, BusinessAddress,
  MaillingAddress, and ShippingAddress
- **Address.City**: All addresses
  specified in the [Attribute Type
  Selector](#rule-based-attribute-type-selector "#rule-based-attribute-type-selector") are
  reviewed for similarity, including Address, BusinessAddress,
  MaillingAddress, and ShippingAddress
- **Address.Country**: All
  addresses specified in the [Attribute Type
  Selector](#rule-based-attribute-type-selector "#rule-based-attribute-type-selector") are
  reviewed for similarity, including Address, BusinessAddress,
  MaillingAddress, and ShippingAddress
- **Address.County**: All addresses
  specified in the [Attribute Type
  Selector](#rule-based-attribute-type-selector "#rule-based-attribute-type-selector") are
  reviewed for similarity, including Address, BusinessAddress,
  MaillingAddress, and ShippingAddress
- **Address.PostalCode**: All
  addresses specified in the [Attribute Type
  Selector](#rule-based-attribute-type-selector "#rule-based-attribute-type-selector") are
  reviewed for similarity, including Address, BusinessAddress,
  MaillingAddress, and ShippingAddress
- **Address.State**: All addresses
  specified in the [Attribute Type
  Selector](#rule-based-attribute-type-selector "#rule-based-attribute-type-selector") are
  reviewed for similarity, including Address, BusinessAddress,
  MaillingAddress, and ShippingAddress
- **Address.Province**: All
  addresses specified in the [Attribute Type
  Selector](#rule-based-attribute-type-selector "#rule-based-attribute-type-selector") are
  reviewed for similarity, including Address, BusinessAddress,
  MaillingAddress, and ShippingAddress
- **PhoneNumber**: The phone
  numbers specified in the [Attribute Type
  Selector](#rule-based-attribute-type-selector "#rule-based-attribute-type-selector") are
  reviewed for similarity, including PhoneNumber, HomePhoneNumber,
  and MobilePhoneNumber.
- **EmailAddress**: All email
  addresses specified in the [Attribute Type
  Selector](#rule-based-attribute-type-selector "#rule-based-attribute-type-selector") are
  reviewed for similarity, including EmailAddress,
  BusinessEmailAddress, and PersonalEmailAddress
- **BirthDate**
- **BusinessName**
- **FirstName**
- **LastName**
- **MiddleName**
- **Gender**
- **Any customized profile attributes with
  the _Attributes_ prefix**

Matching rules are processed by priority. For example, the first rule
should be the most optimized rule you want to define and should be used
to achieve the most accurate result.

### Attribute Type

Selector

The Attribute Types Selector holds vital configuration information for
rule-based identity resolution, facilitating profile matching. This allows you
to fine-tune the comparison of profiles across attribute types and
select the key attributes for matching within each type. Within this
feature, you have the flexibility to configure three distinct attribute
types, enabling precise control over the matching process.

- **Email type**
  - You can choose from EmailAddress,
    BusinessEmailAddress, and PersonalEmailAddress

- **PhoneNumber type**
  - You can choose from PhoneNumberNumber,
    HomePhoneNumber, and MobilePhoneNumber

- **Address type**
  - You can choose from Address, BusinessAddress,
    MaillingAddress, and ShippingAddress

You can either choose `ONE_TO_ONE` or
`MANY_TO_MANY` as the AttributeMatchingModel. When
choosing `MANY_TO_MANY`, the system can match attributes
across the sub-types of an attribute type. For example, if the value of
the EmailAddress field of Profile A and the value of
BusinessEmailAddress field of Profile B matches, the two profiles are
matched on the EmailAddress type. When choosing `ONE_TO_ONE`,
the system can only match if the sub-types are exact matches. For
example, only when the value of the EmailAddress field of Profile A and
the value of the EmailAddress field of Profile B matches, the two
profiles are matched on the EmailAddress type.

**Max allowed rule level for
matching**

You can configure the max rule level you want to use to match similar
profiles. For example, if your max allowed rule level for matching is 5,
the system will not find similar profiles using the rule level 6.

### Match groups

A match group consists of all similar profiles which represent a
customer. Each match group contains the following information:

- A match ID, which uniquely identifies the group of two or more
  similar profiles that represent a contact
- The number of profile IDs in the match group

### Match status

- **PENDING**

The first status after the configuration of a rule-based Matching
rule. If it is an existing domain, the rule-based Identity Resolution
waits 1 hour before creating the matching rule. If it is a new
domain, the system will skip the **PENDING**
stage.

- **IN_PROGRESS**

The system is creating the rule-based Matching rule. Under this
status, the system is evaluating the existing data and you can
no longer change the rule-based matching configuration.

- **ACTIVE**

The rule is ready to use. You can change the rule a day after
the status is in an **ACTIVE** state.

### How the

auto-matching process works

After you create a new Amazon Connect Customer Profiles domain with the rule-based matching rule,
the rule-based Identity Resolution will match similar profiles based on the
rule you specified while you are ingesting the profiles. If you update
the configuration of the rule-based matching, Customer Profiles will start to re-evaluate
the profiles in your domain using the new configuration in an
hour.

If you are enabling the rule-based matching with an existing domain, the
system will move to a **PENDING** state and will start
to evaluate the existing profiles in your domain using the new
configuration in an hour. The time it takes to finish evaluating
profiles is dependant on how many profiles exist.

- **By default, the default rule will be
  applied if no custom rule specified.**
  - Amazon Connect Customer Profiles provides a default matching rule if you do
    not provide a custom matching rule. You can check the
    custom matching rule here.

- **All the records will go through the rule-based
  matching rules.**
  - The system assesses each matching rule level until a
    match is identified or until the maximum allowed rule
    level for matching is reached. The evaluation process
    commences at rule level 1, where the record is analyzed.
    If no matching group is discovered, the system proceeds
    to evaluate the subsequent rule levels, searching for a
    match group until either a match is found or the maximum
    allowed rule level for matching is reached.

- **All attributes in a single matching rule
  level are connected using an _AND_
  relationship**
  - When multiple attributes are present within a single
    rule level, they are interconnected by an AND
    relationship. During profile matching, all attribute
    values must align for profiles to be assigned to the
    same match group. For example, only when the values of
    all attributes are identical, profiles are considered as
    matches and grouped together for further
    processing.

- **All attributes in an attribute type
  selector are connected with an _OR_
  relationship**
  - When specifying attributes within the attribute type
    selector, attributes of the same type are linked through
    an OR relationship. For instance, consider the
    PhoneNumber Type where HomePhoneNumber and
    BusinessPhoneNumber are used. In this scenario, two
    profiles can be matched if either their HomePhoneNumber
    or BusinessPhoneNumber aligns. Consequently, the
    matching process allows for flexible matches based on
    either home or business phone numbers.

- **The match result is eventually
  optimized.**
  - Due to the near real-time nature of profile matching
    in the system, there is a possibility that a match group
    for your profile may be found at a lower (less
    optimized) rule level. Nevertheless, if a match is
    available at a higher (more optimized) rule level, the
    system will assign the profile to that particular
    group.

###### Note

When Identity Resolution performs rule-based matching, the order in which the rules
that you have configured will be processed is dependant on how the
data is ingested. For example, If you configure rules 1 and 2, rule
2 might be processed before rule 1. The processing order might
change, but the end result will always be the same.

## Automatic

merging of similar profiles

After the profiles are matched, the Identity Resolution Job can optionally merge similar
profiles based on the [MaxAllowedRuleLevelForMerging](../../../customerprofiles/latest/APIReference/API_RuleBasedMatchingRequest.md "../../../customerprofiles/latest/APIReference/API_RuleBasedMatchingRequest.md") you specify in the rule-based matching
configuration.

###### Important

You cannot undo the consolidation process. It is recommended to turn
on matching only first to evaluate the match result using the
ListMatches and GetSimiliarProfiles APIs. You can turn on merging by
setting the [MaxAllowedRuleLevelForMerging](../../../customerprofiles/latest/APIReference/API_RuleBasedMatchingRequest.md "../../../customerprofiles/latest/APIReference/API_RuleBasedMatchingRequest.md") using the [UpdateDomain](../../../customerprofiles/latest/APIReference/API_UpdateDomain.md "../../../customerprofiles/latest/APIReference/API_UpdateDomain.md") API.

###### Note

When merging two profiles, profile fields manually populated through
an API call or the Agent Workspace will not be overwritten by profile
fields automatically ingested from an integration or custom object type
mapping.

For example, suppose a profile is created with FirstName “John”
manually by an agent in the Agent Workspace. Another profile is created
using an S3 integration with FirstName “Peter”. If these profiles are
automatically merged, the FirstName “John” will be preserved.
