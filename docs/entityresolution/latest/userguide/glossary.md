# AWS Entity Resolution Glossary

## Amazon Resource Name (ARN)

A unique identifier for AWS resources. ARNs are required when you need to specify a
resource unambiguously across all of AWS Entity Resolution, such as in AWS Entity Resolution policies, Amazon Relational Database Service (Amazon RDS)
tags, and API calls.

## Attribute type

The type of the attribute for the input field. When you [create a schema
mapping](create-schema-mapping.md "create-schema-mapping.md"), you select the **Attribute type** from a pre-configured list of
values such as **Name**, **Address**, **Phone
number**, or **Email address**. Attribute type tells AWS Entity Resolution what
kind of data that you're presenting it, allowing it to be classified and normalized
properly.

## Automatic processing

A processing cadence option for a matching workflow job that enables it to be run on
automatically when your data input changes.

This option is available for [rule-based matching](#rule-based-matching-defn "#rule-based-matching-defn") only.

By default, the processing cadence for a matching workflow job is set to [Manual](#manual-processing "#manual-processing"), which enables it to be run on demand. You can set up
**Automatic** processing to run your matching workflow job automatically when
your data input changes. This keeps your matching workflow output up-to-date.

## AWS KMS key ARN

This is your AWS KMS Amazon Resource Name (ARN) for encryption at rest. If not provided,
system will use an AWS Entity Resolution managed KMS key.

## Batch workflow

A process that runs at scheduled intervals to match and resolve data across an entire
dataset. Batch workflows in AWS Entity Resolution are best used for initial setup, periodic full refreshes, and
scenarios with significant changes in both source and target datasets.

## Cleartext

Data that isn't cryptographically protected.

## Confidence level (ConfidenceLevel)

For ML matching, this is the confidence level applied by AWS Entity Resolution when ML identifies a
matched record set. This is part of the [matching
workflow metadata](#matching-workflow-metadata "#matching-workflow-metadata") that will be included in output.

## Decryption

The process of transforming encrypted data back to its original form. Decryption can only be
performed if you have access to the secret key.

## Encryption

The process of encoding data into a form that appears random using a secret value called a
key. It's impossible to determine the original plaintext without access to the key.

## Group name

The **Group name** references the entire group of input fields and can help
you to group parsed data together for matching purposes.

For example, if there are three input fields: `first_name`,
`middle_name`, and `last_name`, you can group them
together by entering in the **Group name** as `full_name`
for matching and output.

## Hash

Hashing means applying a cryptographic algorithm that produces an irreversible and unique
string of characters of a fixed size—called a hash. AWS Entity Resolution uses Secure Hash Algorithm
256-bit (SHA256) hash protocol and will output a 32-byte character string. In AWS Entity Resolution, you can
choose whether to hash data values in your output.

## Hash protocol (HashingProtocol)

AWS Entity Resolution uses Secure Hash Algorithm 256-bit (SHA256) hash protocol and will output a
32-byte character string. This is part of the [matching
workflow metadata](#matching-workflow-metadata "#matching-workflow-metadata") that will be included in output.

## ID mapping method

How you want the ID mapping to be performed.

There are two ID mapping methods:

- Rule-based – The method by which you use matching rules to translate first-party
  data from a source to a target in an ID mapping workflow.
- Provider services – The method by which you use a provider service to translate
  third party-encoded data from a source to a target in an ID mapping workflow.

AWS Entity Resolution currently supports LiveRamp as the provider services-based ID mapping method. You
must have a subscription to LiveRamp through AWS Data Exchange to use this method. For more information,
see [Step 1: Subscribe to a provider service on
AWS Data Exchange](prepare-third-party-input-data.md#subscribe-provider-service "prepare-third-party-input-data.md#subscribe-provider-service").

## ID mapping workflow

A data processing job that maps data from an input data source to an input data target based
on the specified ID mapping method. It produces an ID mapping table. This workflow requires you
to specify the [ID
mapping method](#id-mapping-method-defn "#id-mapping-method-defn") and the input data you want to translate from a source to a target.

You can set up an ID mapping workflow to run in your own AWS account or across two
AWS accounts.

## ID namespace

A resource in AWS Entity Resolution that contains metadata explaining datasets across multiple AWS accounts
and how to use these datasets in an [ID mapping
workflow](#id-mapping-workflow-defn "#id-mapping-workflow-defn").

There are two types of ID namespaces: `SOURCE` and `TARGET`. The
`SOURCE` contains configurations for the source data that will be processed in an ID
mapping workflow. The `TARGET` contains a configuration of the target data to which
all sources will resolve to. To deﬁne the input data that you want to resolve across two
AWS accounts, create an ID namespace source and an ID namespace target to translate your data
from one set (`SOURCE`) to another (`TARGET`).

After you and another member create ID namespaces and run an ID mapping workflow, you can
join a collaboration in AWS Clean Rooms to run a multi table join on the ID mapping table, and analyze the
data.

For more information, see the [AWS Clean Rooms User Guide](../../../clean-rooms/latest/userguide/what-is.md "../../../clean-rooms/latest/userguide/what-is.md").

## Incremental workflow

A process that only matches and resolves new or updated records since the last run, rather
than processing the entire dataset. Incremental workflows in AWS Entity Resolution are best used for frequent
updates to maintain data freshness when only a small portion of the dataset has changed.

## Input field

An input field corresponds to a column name from your AWS Glue input data table.

## Input Source ARN (InputSourceARN)

The Amazon Resource Name (ARN) that was generated for an AWS Glue table input. This is part of
[matching workflow metadata](#matching-workflow-metadata "#matching-workflow-metadata") that will be
included in output.

## Machine learning-based matching

Machine learning-based matching (ML matching) finds matches across your data that might be
incomplete or might not look exactly the same. ML matching is a preset process that will attempt
to match records across all of the data you input. ML matching returns a [match ID](#match-id-defin "#match-id-defin") and a [confidence level](#confidence-level-defn "#confidence-level-defn")
for each matched set of data.

## Manual processing

A processing cadence option for a matching workflow job that enables it to be run on demand.

This option is set by default and is available for both [rule-based
matching](#rule-based-matching-defn "#rule-based-matching-defn") and [machine
learning -based matching](#ml-matching-defn "#ml-matching-defn").

## Many-to-Many matching

Many-to-many matching compares multiple instances of similar data. Values in input fields
that have been assigned the same match key will be matched against each other, regardless of
whether they are in the same input field or different input fields.

For example, you might have multiple phone number input fields like
`mobile_phone` and `home_phone` that have the same match key “Phone”. Use
many-to-many matching to compare data in the `mobile_phone` input field with data in
the `mobile_phone` input field and data in the `home_phone` input field.

Matching rules evaluate data in multiple input fields with the same match key with an (or)
operation, and one-to-many matching compares values across multiple input fields. This means that
if any combination of `mobile_phone` or `home_phone` matches between two
records, the “Phone” match key will return a match. For match key “Phone” to find a match,
`Record One mobile_phone = Record Two mobile_phone` OR `Record One mobile_phone
 = Record Two home_phone` OR `Record One home_phone = Record Two home_phone` OR
`Record One home_phone = Record Two mobile_phone`.

## Match ID (MatchID)

For rule-based matching and ML matching, this is the ID generated by AWS Entity Resolution and applied
to each matched record set. This is part of the [matching workflow metadata](#matching-workflow-metadata "#matching-workflow-metadata") that will be included in output.

## Match key (MatchKey)

Match key instructs AWS Entity Resolution which input fields to consider as similar data and which to
consider as different data. This helps AWS Entity Resolution automatically configure rule-based matching
rules and compare similar data stored in different input fields.

If there are multiple types of phone number information like a `mobile_phone`
input field and a `home_phone` input field in your data that you would like compared
together, you could give them both the match key “Phone”. Then rule-based matching can be
configured to compare data using “or” statements in all input fields with the “Phone” match key
(see [One-to-One Matching](#one-to-one-matching-defn "#one-to-one-matching-defn") and [Many-to-Many Matching](#many-to-many-defin "#many-to-many-defin") definitions in Matching Workflow
section).

If you want rule-based matching to consider different types of phone number information
completely separately, you can create more specific match keys like “Mobile_Phone” and
“Home_Phone”. Then, when setting up a matching workflow, you can specify how each phone match key
will be used in rule-based matching.

If no MatchKey is specified for a particular input field, it can't be used in matching but
can be carried through the matching workflow process and can be output if desired.

## Match key name

The name assigned to a Match key.

## Match rule (MatchRule)

For rule-based matching, this is the rule number applied that generated a matched record
set. This is part of the [matching workflow
metadata](#matching-workflow-metadata "#matching-workflow-metadata") that will be included in output.

## Matching

The process of combining and comparing data from different input fields, tables, or
databases and determining which of it is alike – or “matches” – based upon
satisfying certain matching criteria (for example, either through matching rules or
models).

## Matching workflow

The process that you set up to specify the input data to match together and how the matching
should be performed.

## Matching workflow description

An optional description of the matching workflow that you might choose to enter.
Descriptions help you differentiate between matching workflows if you create more than
one.

## Matching workflow name

The name for the matching workflow that you specify.

###### Note

Matching workflow names must be unique. They can't have the same name or an error will be
returned.

## Matching workflow metadata

Information generated and output by AWS Entity Resolution during a matching workflow job. This
information is required on output.

## Normalization (ApplyNormalization)

Choose whether to normalize input data as defined in the schema. Normalization standardizes
data by removing extra spaces and special characters and standardizing to lowercase format.

For example, if an input field has an attribute type of [Full phone](#normalization-rule-phone "#normalization-rule-phone"), and the values in the input table are
formatted as `(123) 456-7890`, AWS Entity Resolution will normalize the values to
`1234567890`.

###### Note

Normalization is only supported the group type for [Name](#normalization-rule-name "#normalization-rule-name"), [Address](#normalization-rule-address "#normalization-rule-address"), [Phone](#normalization-rule-phone "#normalization-rule-phone"), and [Email](#normalization-rule-email "#normalization-rule-email").

The following sections describe our standard normalization rules.

For ML-based matching specifically, see [Normalization (ApplyNormalization) – ML-based
only](#normalization-ML-defn "#normalization-ML-defn").

###### Topics

- [Name](#normalization-rule-name "#normalization-rule-name")
- [Email](#normalization-rule-email "#normalization-rule-email")
- [Phone](#normalization-rule-phone "#normalization-rule-phone")
- [Address](#normalization-rule-address "#normalization-rule-address")
- [Hashed](#normalization-rule-hashed "#normalization-rule-hashed")
- [Source_ID](#normalization-rule-source-id "#normalization-rule-source-id")

### Name

###### Note

Normalization is only supported for the **Name** group type.

The **Name** group type appears as **Full name** in the
console and as `NAME` in the API.

If you want to normalize the sub-types of the **Name** group type:

- In the console, assign the following subtypes to the **Full name**
  group: **First name**, **Middle name**, and **Last
  name**.
- In the [CreateSchemaMapping](../apireference/API_CreateSchemaMapping.md "../apireference/API_CreateSchemaMapping.md") API, assign the following
  **Types** to the `NAME`
  **groupName**: `NAME_FIRST`, `NAME_MIDDLE`, and
  `NAME_LAST`.

- **TRIM** = Trims leading and trailing whitespace
- **LOWERCASE** = Lowercases all alpha characters
- **CONVERT_ACCENT** = Covert accented letter to regular
  letter
- **REMOVE_ALL_NON_ALPHA** = Removes all non-alpha characters
  [a-zA-Z]

### Email

###### Note

Normalization is supported for the **Email** group type.

The **Email** group type appears as **Email address** in
the console and as `EMAIL_ADDRESS` in the API.

- **TRIM** = Trims leading and trailing whitespace
- **LOWERCASE** = Lowercases all alpha characters
- **CONVERT_ACCENT** = Covert accented letter to regular
  letter
- **EMAIL_ADDRESS_UTIL_NORM** = Removes any dots (.) from the
  username, removes anything after a plus sign (+) in the username, and standardizes common
  domain variations
- **REMOVE_ALL_NON_EMAIL_CHARS** = Removes all
  non-alpha-numeric characters [a-zA-Z0-9] and [.@-]

### Phone

###### Note

Normalization only supported for the **Phone** group type.

The **Phone** group type appears as **Full phone** in
the console and as `PHONE` in the API.

If you want to normalize the sub-types of the **Phone** group type:

- In the console, assign the following sub-types to the **Full phone**
  group: **Phone number**, and **Phone country code**.
- In the [CreateSchemaMapping](../apireference/API_CreateSchemaMapping.md "../apireference/API_CreateSchemaMapping.md") API, assign the following
  **Types** to the `PHONE`
  **groupName**: `PHONE_NUMBER` and
  `PHONE_COUNTRYCODE`.

- **TRIM** = Trims leading and trailing whitespace
- **REMOVE_ALL_NON_NUMERIC** = Removes all non-numeric
  characters [0-9]
- **REMOVE_ALL_LEADING_ZEROES** = Removes all leading
  zeroes
- **ENSURE_PREFIX_WITH_MAP, "phonePrefixMap"** = Examines each
  phone number and tries to match it against patterns in the phonePrefixMap. If a match is
  found, the rule will add or modify the prefix of the phone number to ensure it conforms to the
  standardized format specified in the map.

### Address

###### Note

Normalization only supported for the **Address** group type.

The **Address** group type appears as **Full address**
in the console and as `ADDRESS` in the API.

If you want to normalize the sub-types of the **Address** group type:

- In the console, assign the following sub-types to the **Full address**
  group: **Street address 1**, **Street address 2**:
  **Street address 3 name**, **City name**,
  **State**, **Country**, and **Postal
  code** t
- In the [CreateSchemaMapping](../apireference/API_CreateSchemaMapping.md "../apireference/API_CreateSchemaMapping.md") API, assign the following
  **Types** to the `ADDRESS`
  **groupName**: `ADDRESS_STREET1`, `ADDRESS_STREET2`,
  `ADDRESS_STREET3`, `ADDRESS_CITY`, `ADDRESS_STATE`,
  `ADDRESS_COUNTRY`, and `ADDRESS_POSTALCODE`.

- **TRIM** = Trims leading and trailing whitespace
- **LOWERCASE** = Lowercases all alpha characters
- **CONVERT_ACCENT** = Covert accented letter to regular
  letter
- **REMOVE_ALL_NON_ALPHA** = Removes all non-alpha characters
  [a-zA-Z]
- **RENAME_WORDS using ADDRESS_RENAME_WORD_MAP** = replace
  words in Address string with words from[ADDRESS_RENAME_WORD_MAP](#ADDRESS_RENAME_WORD_MAP "#ADDRESS_RENAME_WORD_MAP")
- **RENAME_DELIMITERS using ADDRESS_RENAME_DELIMITER_MAP** =
  replace delimiters in Address string with string from [ADDRESS_RENAME_DELIMITER_MAP](#ADDRESS_RENAME_DELIMITER_MAP "#ADDRESS_RENAME_DELIMITER_MAP")
- **RENAME_DIRECTIONS using ADDRESS_RENAME_DIRECTION_MAP**=
  replace delimiters in Address string with string from [ADDRESS_RENAME_DIRECTION_MAP](#ADDRESS_RENAME_DIRECTION_MAP "#ADDRESS_RENAME_DIRECTION_MAP")
- **RENAME_NUMBERS using ADDRESS_RENAME_NUMBER_MAP** = replace
  numbers in Address string with string from [ADDRESS_RENAME_NUMBER_MAP](#ADDRESS_RENAME_NUMBER_MAP.title "#ADDRESS_RENAME_NUMBER_MAP.title")
- **RENAME_SPECIAL_CHARS using
  ADDRESS_RENAME_SPECIAL_CHAR_MAP** = replace special characters in Address string
  with string from [ADDRESS_RENAME_SPECIAL_CHAR_MAP](#ADDRESS_RENAME_SPECIAL_CHAR_MAP.title "#ADDRESS_RENAME_SPECIAL_CHAR_MAP.title")

#### ADDRESS_RENAME_WORD_MAP

These are the words that will be renamed when normalizing the address string.

```
"avenue": "ave",
 "bouled": "blvd",
 "circle": "cir",
 "circles": "cirs",
 "court": "ct",
 "centre": "ctr",
 "center": "ctr",
 "drive": "dr",
 "freeway": "fwy",
 "frwy": "fwy",
 "highway": "hwy",
 "lane": "ln",
 "parks": "park",
 "parkways": "pkwy",
 "pky": "pkwy",
 "pkway": "pkwy",
 "pkwys": "pkwy",
 "parkway": "pkwy",
 "parkwy": "pkwy",
 "place": "pl",
 "plaza": "plz",
 "plza": "plz",
 "road": "rd",
 "square": "sq",
 "squ": "sq",
 "sqr": "sq",
 "street": "st",
 "str": "st",
 "str.": "strasse"
```

#### ADDRESS_RENAME_DELIMITER_MAP

These are the delimiters that will be renamed when normalizing the address string.

```
",": " ",
".": " ",
"[": " ",
"]": " ",
"/": " ",
"-": " ",
"#": " number "
```

#### ADDRESS_RENAME_DIRECTION_MAP

These are the direction identifiers that will be renamed when normalizing the address
string.

```
"east": "e",
"north": "n",
"south": "s",
"west": "w",
"northeast": "ne",
"northwest": "nw",
"southeast": "se",
"southwest": "sw"
```

#### ADDRESS_RENAME_NUMBER_MAP

These are the number strings that will be renamed when normalizing the address
string.

```
"número": "number",
 "numero": "number",
 "no": "number",
 "núm": "number",
 "num": "number"
```

#### ADDRESS_RENAME_SPECIAL_CHAR_MAP

These are the special characters string that will be renamed when normalizing the address
string.

```
"ß": "ss",
 "ä": "ae",
 "ö": "oe",
 "ü": "ue",
 "ø": "o",
 "æ": "ae"
```

### Hashed

- **TRIM** = Trims leading and trailing whitespace

### Source_ID

- **TRIM** = Trims leading and trailing whitespace

## Normalization (ApplyNormalization) – ML-based

only

Choose whether to normalize input data as defined in the schema. Normalization standardizes
data by removing extra spaces and special characters and standardizing to lowercase format.

For example, if an input field has an attribute type of `NAME`, and the values in
the input table are formatted as `Johns Smith`, AWS Entity Resolution will normalize the values to
`john smith`.

The following sections describe the normalization rules for [machine learning-based matching workflows](#ml-matching-defn "#ml-matching-defn").

###### Topics

- [Name](#normalization-ML-defn-name "#normalization-ML-defn-name")
- [Email](#normalization-ML-defn-email "#normalization-ML-defn-email")
- [Phone](#normalization-ML-defn-phone "#normalization-ML-defn-phone")

### Name

- **TRIM** = Trims leading and trailing whitespace
- **LOWERCASE** = Lowercases all alpha characters

### Email

- **LOWERCASE** = Lowercases all alpha characters
- Replaces only (at)(case sensitive) with an @ symbol
- Removes all whitespace, anywhere in the value
- Removes everything that's outside of the first `"<`
  `>"` if it exists

### Phone

- **TRIM** = Trims leading and trailing whitespace
- **REMOVE_ALL_NON_NUMERIC** = Removes all non-numeric
  characters [0-9]
- **REMOVE_ALL_LEADING_ZEROES** = Removes all leading
  zeroes
- **ENSURE_PREFIX_WITH_MAP, "phonePrefixMap"** = Examines each
  phone number and tries to match it against patterns in the phonePrefixMap. If a match is
  found, the rule will add or modify the prefix of the phone number to ensure it conforms to the
  standardized format specified in the map.

## One-to-One matching

One-to-one matching compares single instances of similar data. Input fields with the same
match key and values in the same input field will be matched against each other.

For example, you might have multiple phone number input fields like
`mobile_phone` and `home_phone` that have the same match key “Phone”. Use
one-to-one matching to compare data in the `mobile_phone` input field with data in the
`mobile_phone` input field and to compare data in the `home_phone` input
field with data in the `home_phone` input field. Data in the `mobile_phone`
input field won't be compared with data in the `home_phone` input field.

Matching rules evaluate data in multiple input fields with the same match key with an (or)
operation, and one-to-many matching compares values within a single input field. This means that
if `mobile_phone` or `home_phone` matches between two records, the “Phone”
match key will return a match. For match key “Phone” to find a match, `Record One
 mobile_phone = Record Two mobile_phone` OR `Record One home_phone = Record Two
 home_phone`.

Matching rules evaluate data in input fields with different match keys with an (and)
operation. If you want rule-based matching to consider different types of phone number
information completely separately, you can create more specific match keys like “mobile_phone”
and “home_phone”. If you want to use both match keys in a rule to find matches, `Record One
 mobile_phone = Record Two mobile_phone` AND `Record One home_phone = Record Two
 home_phone`.

## Output

A list of **OutputAttribute** objects, each of which have the fields
**Name** and **Hashed**. Each of these objects represent a
column to be included in the AWS Glue output table and whether you want the values in the column to
be hashed.

## OutputS3Path

The S3 destination to which AWS Entity Resolution will write the output table.

## OutputSourceConfig

A list of OutputSource objects, each of which have the fields
**OutputS3Path**, **ApplyNormalization**, and
**Output**.

## Provider service-based matching

Provider service-based matching is process designed to match, link, and enhance your records
with preferred data service providers and licensed data sets. You must have a subscription
through AWS Data Exchange with the provider service to use this matching technique.

AWS Entity Resolution currently integrates with the following data service providers:

- LiveRamp
- TransUnion
- UID 2.0

## Rule-based matching

Rule-based matching is process designed to find exact matches. Rule-based matching is a
hierarchical set of waterfall matching rules, suggested by AWS Entity Resolution, based upon the data that
you input and completely configurable by you. All match keys provided within rule criteria must
match exactly for compared data to be declared a match and for associated metadata to be output.
Rule-based matching returns a [Match
ID](#match-id-defin "#match-id-defin") and a rule number for each matched set of data.

We recommend defining rules that can uniquely identify an entity. Order your rules to find
more precise matches first.

For example, let's say you have two rules, **Rule 1** and
**Rule 2**.

These rules have the following match keys:

- **Rule 1** includes Full name and Address
- **Rule 2** includes Full name, Address, and Phone

Because **Rule 1** runs first, no matches will be found by
**Rule 2** because they would have all been found by **Rule 1**.

To find matches that are differentiated by Phone, reorder the rules, like this:

- **Rule 2** includes Full name, Address, and Phone
- **Rule 1** includes Full name and Address

## Schema

The term used for a structure or layout defining how a set of data is organized and
connected.

## Schema description

An optional description of the schema that you can choose to enter. Descriptions help you
differentiate between schema mappings if you create more than one.

## Schema name

The name of the schema.

###### Note

Schema names must be unique. They can't have the same name or an error will be
returned.

## Schema mapping

Schema mapping in AWS Entity Resolution is the process by which you tell AWS Entity Resolution how to interpret your
data for matching. You define the schema of the input data table that you want AWS Entity Resolution to read
into a matching workflow.

## Schema mapping ARN

The Amazon Resource Name (ARN) generated for the [schema mapping](#schema-mapping-definition "#schema-mapping-definition").

## Unique ID

A unique identifier that you designate and that must be assigned to each row of input data
that AWS Entity Resolution reads.

###### Example

For example: `Primary_key`, `Row_ID`, or
`Record_ID`.

The **Unique ID** column is required.

The **Unique ID** must be a unique identifier within a single table.

The **Unique ID** must satisfy this pattern:
`[a-zA-Z0-9_-]`

Across different tables, the **Unique ID** can have duplicate values.

The maximum **Unique ID** length is 38 for a [matching
workflow](#matching-workflow-definition "#matching-workflow-definition")

The maximum **Unique ID** length 257 characters for a [ID mapping workflow](#id-mapping-workflow-defn "#id-mapping-workflow-defn")

When the [matching workflow](#matching-workflow-definition "#matching-workflow-definition") is run, the record will be
rejected if the **Unique ID**:

- isn't specified
- isn't unique within the same table
- overlaps in terms of attribute name across sources
- exceeds 38 characters (rule-based matching workflows only)
