# Understanding CSV profiles

A CSV transformation profile is a declarative YAML document that tells Data Transformation Agent how to turn
your relational CSV tables into FHIR R4 resources. You can have the Data Transformation AI agent
generate this for you from sample files, or author and edit it by hand. This section
explains the structure and every building block so you can write or refine a mapping
yourself.

## The big picture

Your CSV data is relational: patients in one file, their phone numbers in another,
encounters in a third, diagnoses in a fourth. FHIR resources are hierarchical: a
Patient has a telecom[] array, an Encounter references a Patient and has a diagnosis[]
array. A mapping profile bridges the two by declaring:

- Which table becomes which FHIR resource (for example, PT\_DEM ->
  Patient).
- Which column fills which FHIR field (for example, LAST\_NM ->
  name[0].family), and how to transform the value.
- How child-table rows fold into a parent resource: either as array entries
  (telecom[]) or merged in place (aggregation).
- How tables reference each other so the generated FHIR resources link
  correctly.

## Profile structure overview

A CSV mapping profile is a YAML file with two top-level fields:

```
sourceSystemId: my-hospital-ehr
tables:
  - tableName: PATIENTS
    primaryKeyColumn: PAT_ID
    foreignKeys: [...]
    resourceMappings:
      - targetResourceType: Patient
        fieldMappings: [...]
        aggregationMappings: [...]
  - tableName: ENCOUNTERS
    ...
```

Top-level fields| Field | Required | Description |
| --- | --- | --- |
| `sourceSystemId` | Yes | A short identifier for the source system. Used internally to<br>namespace generated resource IDs so they are unique across<br>sources. |
| `tables` | Yes | An ordered list of table definitions. Each entry describes one CSV<br>file and how it maps to one or more FHIR resources. |

## Table definition

Each entry in the `tables` list describes a single CSV file:

```
- tableName: PT_DEM
  primaryKeyColumn: PAT_ID
  foreignKeys:
    - columnName: PROV_ID
      referenceTableName: PROVIDERS
      referenceColumnName: PROV_ID
  resourceMappings:
    - targetResourceType: Patient
      fieldMappings: [...]
```

Table definition fields| Field | Required | Description |
| --- | --- | --- |
| `tableName` | Yes | Logical name of the CSV file (without the .csv extension). Must<br>match the filename you upload to Amazon S3. |
| `primaryKeyColumn` | Yes | The column whose values uniquely identify a row. Used to generate<br>stable FHIR resource IDs and to join child tables. |
| `foreignKeys` | No | Declares how this table joins to other tables. See [Foreign keys](#csv-yaml-foreign-keys "#csv-yaml-foreign-keys"). |
| `resourceMappings` | Yes | One or more resource mappings that describe which FHIR resources<br>are produced from this table. See [Resource mapping](#csv-yaml-resource-mapping "#csv-yaml-resource-mapping"). |

## Foreign keys

Foreign keys tell the engine how rows in one table relate to rows in another:

```
foreignKeys:
  - columnName: PAT_ID
    referenceTableName: PT_DEM
    referenceColumnName: PAT_ID
  - columnName: PROV_ID
    referenceTableName: PROVIDERS
    referenceColumnName: PROV_ID
```

Foreign key fields| Field | Required | Description |
| --- | --- | --- |
| `columnName` | Yes | The column in this table that holds the foreign key value. |
| `referenceTableName` | Yes | The `tableName` of the parent table this key points<br>to. |
| `referenceColumnName` | Yes | The column in the parent table that this key matches<br>against. |

###### Important

Foreign key references must be single-hop. Table A can reference Table B, and
Table B can reference Table C, but Table A cannot directly reference Table C
through Table B. Each relationship must be declared explicitly in the table that
holds the foreign key column.

## Resource mapping

A resource mapping declares the FHIR resource type to produce and how to populate
it:

```
resourceMappings:
  - targetResourceType: Patient
    fieldMappings:
      - fhirPath: name[0].family
        sourceColumn: LAST_NM
        transform:
          type: direct
      - fhirPath: name[0].given[0]
        sourceColumn: FIRST_NM
        transform:
          type: direct
    aggregationMappings:
      - sourceTableName: PT_PHONE
        targetFhirPath: telecom
        aggregationType: array
        fieldMappings: [...]
```

## Field mappings

Each field mapping connects one FHIR element path to one or more source
columns:

```
fieldMappings:
  - fhirPath: name[0].family
    sourceColumn: LAST_NM
    transform:
      type: direct
  - fhirPath: name[0].text
    sourceColumns:
      - FIRST_NM
      - LAST_NM
    transform:
      type: concat
      params:
        separator: " "
  - fhirPath: birthDate
    sourceColumn: DOB
    transform:
      type: dateFormat
      params:
        inputFormat: MM/dd/yyyy
        outputFormat: yyyy-MM-dd
```

Field mapping fields| Field | Required | Description |
| --- | --- | --- |
| `fhirPath` | Yes | The dot-notation path within the FHIR resource where the value<br>will be placed (for example, `name[0].family`,<br>`telecom[0].value`). |
| `sourceColumn` | Conditional | The single CSV column to read. Required unless<br>`sourceColumns` is provided or the transform type does<br>not need input (for example, `expression` with a<br>constant). |
| `sourceColumns` | Conditional | A list of CSV columns to read, used by multi-input transforms such<br>as `concat`. Mutually exclusive with<br>`sourceColumn`. |
| `transform` | Yes | An object with a `type` field and optional<br>`params`. See [Transform types](#csv-yaml-transform-types "#csv-yaml-transform-types"). |
| `targetFhirType` | No | Overrides the default string type for the output value. See [targetFhirType](#csv-yaml-target-fhir-type "#csv-yaml-target-fhir-type"). |

### targetFhirType

By default, every mapped value is emitted as a JSON string. Use
`targetFhirType` to emit a different JSON type:

```
# Boolean example
- fhirPath: active
  sourceColumn: IS_ACTIVE
  transform:
    type: direct
  targetFhirType: boolean
```

```
# Integer example
- fhirPath: extension[0].valueInteger
  sourceColumn: VISIT_COUNT
  transform:
    type: direct
  targetFhirType: integer
```

```
# Decimal example
- fhirPath: valueQuantity.value
  sourceColumn: LAB_RESULT
  transform:
    type: direct
  targetFhirType: decimal
```

Accepted targetFhirType values| Value | Behavior |
| --- | --- |
| `boolean` | Converts `"true"`/`"1"` to JSON<br>`true`, everything else to<br>`false`. |
| `integer` | Parses the value as a whole number. Non-numeric values are<br>skipped. |
| `decimal` | Parses the value as a floating-point number. Non-numeric values<br>are skipped. |

If the source value cannot be converted to the requested type (for example, the
string `"abc"` with `targetFhirType: integer`), the field is
silently omitted from the output resource rather than producing an error.

When do I need it?

- The FHIR element is defined as `boolean`,
  `integer`, or `decimal` in the spec and your
  source data stores it as a string.
- You are populating an `extension` with a
  `valueInteger` or `valueDecimal` element.
- You want JSON-native types for downstream consumers that parse the JSON
  strictly.

## Transform types

The engine supports 8 transform types.

### direct

Copies the source value as-is into the target field with no
modification:

```
- fhirPath: name[0].family
  sourceColumn: LAST_NM
  transform:
    type: direct
```

Example: if the CSV column `LAST_NM` contains
`Smith`, the output is
`"family": "Smith"`.

### concat

Joins multiple source columns into a single string:

```
- fhirPath: name[0].text
  sourceColumns:
    - FIRST_NM
    - LAST_NM
  transform:
    type: concat
    params:
      separator: " "
```

concat parameters| Parameter | Required | Description |
| --- | --- | --- |
| `separator` | No | The string placed between each column value. Defaults to empty<br>string (`""`) if omitted. |

### dateFormat

Parses a date/time string in the source format and re-formats it for
FHIR:

```
- fhirPath: birthDate
  sourceColumn: DOB
  transform:
    type: dateFormat
    params:
      inputFormat: MM/dd/yyyy
      outputFormat: yyyy-MM-dd
```

dateFormat parameters| Parameter | Required | Description |
| --- | --- | --- |
| `inputFormat` | Yes | The Java `DateTimeFormatter` pattern that matches<br>your source data. |
| `outputFormat` | Yes | The Java `DateTimeFormatter` pattern for the output.<br>Use FHIR-compatible patterns. |

Common patterns:

- `yyyy-MM-dd` – FHIR date (2024-03-15)
- `yyyy-MM-dd'T'HH:mm:ssXXX` – FHIR dateTime with timezone
  (2024-03-15T10:30:00-05:00)
- `MM/dd/yyyy` – US date (03/15/2024)
- `yyyyMMdd` – compact date (20240315)

### valueMap

Maps discrete source values to FHIR values using a lookup table:

```
- fhirPath: gender
  sourceColumn: SEX_CD
  transform:
    type: valueMap
    params:
      mapping:
        M: male
        F: female
        U: unknown
        O: other
```

valueMap parameters| Parameter | Required | Description |
| --- | --- | --- |
| `mapping` | Yes | A key-value map where the key is the source value and the value<br>is the FHIR output value. |

If the source value does not match any key in the mapping, the field is silently
omitted from the output resource.

### expression

Evaluates an inline expression. Use it to inject constants or compute values from
source columns:

```
# Constant value (no sourceColumn needed)
- fhirPath: resourceType
  transform:
    type: expression
    params:
      expression: "'Patient'"
```

```
# Dynamic value using source column
- fhirPath: identifier[0].value
  sourceColumn: MRN
  transform:
    type: expression
    params:
      expression: "'urn:mrn:' + $value"
```

###### Important

Expressions are evaluated in a sandboxed environment. Only string
concatenation and the `$value` variable (which holds the current
source column value) are supported. Complex logic should be handled by using
multiple field mappings or a different transform type.

### conditional

Emits different values depending on whether the source column is present (non-null
and non-empty) or absent:

```
- fhirPath: deceasedBoolean
  sourceColumn: DEATH_DT
  transform:
    type: conditional
    params:
      condition: present
      presentValue: "true"
      absentValue: "false"
  targetFhirType: boolean
```

conditional parameters| Parameter | Required | Description |
| --- | --- | --- |
| `condition` | Yes | The condition to evaluate. Currently only<br>`present` is supported (checks that the value is<br>non-null and non-empty). |
| `presentValue` | Yes | The value to emit when the condition is true (source column has<br>a value). |
| `absentValue` | No | The value to emit when the condition is false (source column is<br>null or empty). If omitted, the field is omitted from the<br>output. |

Example: if `DEATH_DT` has a value, `deceasedBoolean` is
`true`; if `DEATH_DT` is empty,
`deceasedBoolean` is `false`.

### resourceReference

Generates a FHIR Reference to another resource produced by the mapping:

```
- fhirPath: subject.reference
  sourceColumn: PAT_ID
  transform:
    type: resourceReference
    params:
      referenceTableName: PT_DEM
      referenceResourceType: Patient
```

resourceReference parameters| Parameter | Required | Description |
| --- | --- | --- |
| `referenceTableName` | Yes | The `tableName` of the table that produces the<br>target resource. |
| `referenceResourceType` | Yes | The FHIR resource type of the target (for example,<br>`Patient`, `Practitioner`). |

The referenced table must be declared in the same mapping profile, and the source
column value must match a primary key value in the referenced table. The engine
generates a relative reference in the form
`ResourceType/generated-id`.

### regex

Applies a regular expression to extract or transform part of the source
value:

```
- fhirPath: telecom[0].value
  sourceColumn: PHONE_RAW
  transform:
    type: regex
    params:
      pattern: "\\(?(\\d{3})\\)?[-.\\s]?(\\d{3})[-.\\s]?(\\d{4})"
      replacement: "$1-$2-$3"
```

regex parameters| Parameter | Required | Description |
| --- | --- | --- |
| `pattern` | Yes | A Java-style regular expression applied to the source value.<br>Use capture groups to extract portions. |
| `replacement` | Yes | The replacement string. Use `$1`, `$2`,<br>etc. to reference capture groups. |

More examples:

```
# Extract numeric portion from a code like "ICD-10:E11.9"
- fhirPath: code.coding[0].code
  sourceColumn: DIAG_CD
  transform:
    type: regex
    params:
      pattern: "^[A-Z]+-\\d+:(.+)$"
      replacement: "$1"
```

```
# Remove all non-alphanumeric characters
- fhirPath: identifier[0].value
  sourceColumn: RAW_ID
  transform:
    type: regex
    params:
      pattern: "[^a-zA-Z0-9]"
      replacement: ""
```

## Aggregation

Aggregation is how child-table rows fold into a parent resource. A parent table
declares which child table to pull from, which FHIR path to target, and what type of
aggregation to perform.

### Array aggregation

Each matching child row becomes a new entry in the target array:

```
aggregationMappings:
  - sourceTableName: PT_PHONE
    targetFhirPath: telecom
    aggregationType: array
    fieldMappings:
      - fhirPath: value
        sourceColumn: PHONE_NUM
        transform:
          type: direct
      - fhirPath: system
        transform:
          type: expression
          params:
            expression: "'phone'"
      - fhirPath: use
        sourceColumn: PHONE_TYPE
        transform:
          type: valueMap
          params:
            mapping:
              H: home
              W: work
              M: mobile
```

Array aggregation fields| Field | Required | Description |
| --- | --- | --- |
| `sourceTableName` | Yes | The `tableName` of the child table. |
| `targetFhirPath` | Yes | The array field in the parent resource (for example,<br>`telecom`, `address`). |
| `aggregationType` | Yes | Must be `array`. |
| `fieldMappings` | Yes | Field mappings applied to each child row. Paths are relative to<br>one array entry. |

Example output (JSON):

```
{
  "resourceType": "Patient",
  "telecom": [
    { "value": "555-0100", "system": "phone", "use": "home" },
    { "value": "555-0101", "system": "phone", "use": "work" }
  ]
}
```

### Merge aggregation

All matching child rows are merged into the parent resource at the target path.
Only the last matching row's values win for each field:

```
aggregationMappings:
  - sourceTableName: PT_ADDRESS
    targetFhirPath: address[0]
    aggregationType: merge
    fieldMappings:
      - fhirPath: line[0]
        sourceColumn: STREET
        transform:
          type: direct
      - fhirPath: city
        sourceColumn: CITY
        transform:
          type: direct
      - fhirPath: state
        sourceColumn: STATE
        transform:
          type: direct
      - fhirPath: postalCode
        sourceColumn: ZIP
        transform:
          type: direct
```

Merge aggregation fields| Field | Required | Description |
| --- | --- | --- |
| `sourceTableName` | Yes | The `tableName` of the child table. |
| `targetFhirPath` | Yes | The path in the parent resource where values are merged (for<br>example, `address[0]`). |
| `aggregationType` | Yes | Must be `merge`. |
| `fieldMappings` | Yes | Field mappings applied to each child row. Paths are relative to<br>the `targetFhirPath`. |

Example output (JSON):

```
{
  "resourceType": "Patient",
  "address": [
    {
      "line": ["123 Main St"],
      "city": "Springfield",
      "state": "IL",
      "postalCode": "62701"
    }
  ]
}
```

### Rules for aggregation

- The child table must declare a foreign key that references the parent
  table's primary key column.
- The `sourceTableName` must match a `tableName`
  declared elsewhere in the profile.
- Array aggregation creates one array entry per child row. Merge
  aggregation overwrites the same fields — last row wins.
- Field paths inside an aggregation are relative to the
  `targetFhirPath`, not the resource root.
- A single resource can have multiple aggregation mappings (for example,
  one for `telecom` and another for
  `address`).

## groupByPk

When a single table contains multiple rows per logical entity (for example, a
diagnosis table where each patient has multiple diagnosis rows), use
`groupByPk` to group rows by the primary key and produce array fields
from the grouped rows:

```
- tableName: DIAGNOSES
  primaryKeyColumn: PAT_ID
  resourceMappings:
    - targetResourceType: Condition
      groupByPk: true
      fieldMappings:
        - fhirPath: subject.reference
          sourceColumn: PAT_ID
          transform:
            type: resourceReference
            params:
              referenceTableName: PT_DEM
              referenceResourceType: Patient
      arrayFieldMappings:
        - fhirPath: code.coding
          fieldMappings:
            - fhirPath: code
              sourceColumn: DIAG_CD
              transform:
                type: direct
            - fhirPath: system
              transform:
                type: expression
                params:
                  expression: "'http://hl7.org/fhir/sid/icd-10-cm'"
```

When `groupByPk` is `true`, all rows sharing the same primary
key value are collapsed into a single resource. Scalar fields (in
`fieldMappings`) take the value from the first row. Array fields (in
`arrayFieldMappings`) accumulate one entry per row.

###### Important

When using `groupByPk`, array fields must be declared in
`arrayFieldMappings`, not in `fieldMappings`. The
`arrayFieldMappings` block has a `fhirPath` for the
target array and a nested `fieldMappings` for each entry.

groupByPk vs aggregation| Feature | groupByPk | Aggregation |
| --- | --- | --- |
| Data source | Multiple rows in the same table | Rows from a different (child) table |
| Declared in | The resource mapping of the table itself | `aggregationMappings` in the parent table's resource<br>mapping |
| Array fields | `arrayFieldMappings` | `fieldMappings` with<br>`aggregationType: array` |
| Use when | One CSV file has repeating rows for the same entity | A separate CSV file contains the child data |

## Child-only tables

Some tables exist solely to provide data that is aggregated into a parent resource.
These tables do not produce standalone FHIR resources. Declare them without
`resourceMappings`:

```
- tableName: PT_PHONE
  primaryKeyColumn: PHONE_ID
  foreignKeys:
    - columnName: PAT_ID
      referenceTableName: PT_DEM
      referenceColumnName: PAT_ID
```

A child-only table still needs `tableName`, `primaryKeyColumn`,
and `foreignKeys`. The foreign key connects it to the parent table. The
parent table's `aggregationMappings` pulls data from this table by
referencing its `tableName` in `sourceTableName`.

## Complete example

This example converts 4 CSV files into Patient, Practitioner, Encounter, and
Condition resources with cross-table references and aggregation:

```
sourceSystemId: acme-hospital

tables:
  # Patient demographics
  - tableName: PT_DEM
    primaryKeyColumn: PAT_ID
    resourceMappings:
      - targetResourceType: Patient
        fieldMappings:
          - fhirPath: name[0].family
            sourceColumn: LAST_NM
            transform:
              type: direct
          - fhirPath: name[0].given[0]
            sourceColumn: FIRST_NM
            transform:
              type: direct
          - fhirPath: birthDate
            sourceColumn: DOB
            transform:
              type: dateFormat
              params:
                inputFormat: MM/dd/yyyy
                outputFormat: yyyy-MM-dd
          - fhirPath: gender
            sourceColumn: SEX_CD
            transform:
              type: valueMap
              params:
                mapping:
                  M: male
                  F: female
                  U: unknown
          - fhirPath: deceasedBoolean
            sourceColumn: DEATH_DT
            transform:
              type: conditional
              params:
                condition: present
                presentValue: "true"
                absentValue: "false"
            targetFhirType: boolean
        aggregationMappings:
          - sourceTableName: PT_PHONE
            targetFhirPath: telecom
            aggregationType: array
            fieldMappings:
              - fhirPath: value
                sourceColumn: PHONE_NUM
                transform:
                  type: direct
              - fhirPath: system
                transform:
                  type: expression
                  params:
                    expression: "'phone'"
              - fhirPath: use
                sourceColumn: PHONE_TYPE
                transform:
                  type: valueMap
                  params:
                    mapping:
                      H: home
                      W: work
                      M: mobile

  # Patient phone numbers (child-only, no resourceMappings)
  - tableName: PT_PHONE
    primaryKeyColumn: PHONE_ID
    foreignKeys:
      - columnName: PAT_ID
        referenceTableName: PT_DEM
        referenceColumnName: PAT_ID

  # Providers
  - tableName: PROVIDERS
    primaryKeyColumn: PROV_ID
    resourceMappings:
      - targetResourceType: Practitioner
        fieldMappings:
          - fhirPath: name[0].family
            sourceColumn: PROV_LAST
            transform:
              type: direct
          - fhirPath: name[0].given[0]
            sourceColumn: PROV_FIRST
            transform:
              type: direct
          - fhirPath: identifier[0].value
            sourceColumn: NPI
            transform:
              type: direct
          - fhirPath: identifier[0].system
            transform:
              type: expression
              params:
                expression: "'http://hl7.org/fhir/sid/us-npi'"

  # Encounters
  - tableName: ENCOUNTERS
    primaryKeyColumn: ENC_ID
    foreignKeys:
      - columnName: PAT_ID
        referenceTableName: PT_DEM
        referenceColumnName: PAT_ID
      - columnName: PROV_ID
        referenceTableName: PROVIDERS
        referenceColumnName: PROV_ID
    resourceMappings:
      - targetResourceType: Encounter
        fieldMappings:
          - fhirPath: status
            transform:
              type: expression
              params:
                expression: "'finished'"
          - fhirPath: class.code
            sourceColumn: ENC_TYPE
            transform:
              type: valueMap
              params:
                mapping:
                  I: IMP
                  O: AMB
                  E: EMER
          - fhirPath: subject.reference
            sourceColumn: PAT_ID
            transform:
              type: resourceReference
              params:
                referenceTableName: PT_DEM
                referenceResourceType: Patient
          - fhirPath: participant[0].individual.reference
            sourceColumn: PROV_ID
            transform:
              type: resourceReference
              params:
                referenceTableName: PROVIDERS
                referenceResourceType: Practitioner
          - fhirPath: period.start
            sourceColumn: ADMIT_DT
            transform:
              type: dateFormat
              params:
                inputFormat: yyyyMMddHHmm
                outputFormat: "yyyy-MM-dd'T'HH:mm:ss"
          - fhirPath: period.end
            sourceColumn: DISCH_DT
            transform:
              type: dateFormat
              params:
                inputFormat: yyyyMMddHHmm
                outputFormat: "yyyy-MM-dd'T'HH:mm:ss"
```

## Tips

- Start with the Data Transformation AI agent to generate an initial profile from your sample
  CSV files, then refine it by hand using this reference.
- Validate your YAML syntax before uploading. A misplaced indent can cause
  silent mapping failures.
- Use `direct` transforms wherever possible — they are the fastest
  and simplest to debug.
- Keep `sourceSystemId` short and stable. Changing it after data has
  been loaded will cause duplicate resources because resource IDs will
  change.
- Test with a small subset of data (10–20 rows per table) before running a
  full transformation to catch mapping errors early.
- When in doubt about a FHIR path, consult the FHIR R4 resource
  definitions at `https://hl7.org/fhir/R4/` to confirm the correct
  element names and cardinalities.
