

# Understanding CSV profiles
<a name="data-transformation-csv-yaml-reference"></a>

A CSV transformation profile is a declarative YAML document that tells Data Transformation Agent how to turn your relational CSV tables into FHIR R4 resources. You can have the Data Transformation AI agent generate this for you from sample files, or author and edit it by hand. This section explains the structure and every building block so you can write or refine a mapping yourself.

## The big picture
<a name="csv-yaml-big-picture"></a>

Your CSV data is relational: patients in one file, their phone numbers in another, encounters in a third, diagnoses in a fourth. FHIR resources are hierarchical: a Patient has a telecom[] array, an Encounter references a Patient and has a diagnosis[] array. A mapping profile bridges the two by declaring:
+ Which table becomes which FHIR resource (for example, PT\_DEM -> Patient).
+ Which column fills which FHIR field (for example, LAST\_NM -> name[0].family), and how to transform the value.
+ How child-table rows fold into a parent resource: either as array entries (telecom[]) or merged in place (aggregation).
+ How tables reference each other so the generated FHIR resources link correctly.

## Profile structure overview
<a name="csv-yaml-profile-structure"></a>

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


**Top-level fields**  

| Field | Required | Description | 
| --- | --- | --- | 
| sourceSystemId | Yes | A short identifier for the source system. Used internally to namespace generated resource IDs so they are unique across sources. | 
| tables | Yes | An ordered list of table definitions. Each entry describes one CSV file and how it maps to one or more FHIR resources. | 

## Table definition
<a name="csv-yaml-table-definition"></a>

Each entry in the `tables` list describes a single CSV file:

```
- tableName: PT_DEM
  primaryKeyColumn: PAT_ID
  foreignKeys:
    - column: PROV_ID
      referencedTable: PROVIDERS
      referencedColumn: PROV_ID
  resourceMappings:
    - targetResourceType: Patient
      fieldMappings: [...]
```


**Table definition fields**  

| Field | Required | Description | 
| --- | --- | --- | 
| tableName | Yes | Name of the CSV file without the .csv extension. See [Table names and CSV files](#csv-yaml-table-naming). | 
| primaryKeyColumn | Yes | The column whose values uniquely identify a row. Used to generate stable FHIR resource IDs and to join child tables. | 
| foreignKeys | No | Documents how this table relates to other tables. See [Foreign keys](#csv-yaml-foreign-keys). | 
| resourceMappings | Yes | One or more resource mappings that describe which FHIR resources are produced from this table. See [Resource mapping](#csv-yaml-resource-mapping). | 

### Table names and CSV files
<a name="csv-yaml-table-naming"></a>

Data Transformation Agent matches each table definition to a CSV file in your input Amazon S3 location by file name:
+ The `tableName` is the file name without the `.csv` extension. For example, `PT_DEM.csv` matches `tableName: PT_DEM`. Matching is case-sensitive.
+ Each `tableName` in the profile can contain only letters, digits, and underscores (`[A-Za-z0-9_]`), or the job fails.
+ Files are discovered recursively under the input Amazon S3 prefix. Only non-empty files whose name ends in `.csv` (in any letter case) are used. Because only the file name is used, two files with the same name in different folders fail the job.
+ Every table declared in `tables` must have a matching CSV file, or the job fails. CSV files that don't match a declared table are ignored, unless a parent uses them as an aggregation child table (see [Child-only tables](#csv-yaml-child-only-tables)). If a child table's CSV file is missing, no child rows are aggregated and a warning is recorded.
+ The first row of each file must be a header row, and every column must have a name. The delimiter (comma, tab, or pipe) is detected automatically.
+ The job fails before conversion if any of these columns is missing from its file's header row: the `primaryKeyColumn` of a declared table, and the `sourceColumn` or `sourceColumns` of a `fieldMappings` or `childFieldMappings` entry. Other column references (`joinColumn`, `conditionColumn`, `${COLUMN}` placeholders in `expression`, and `arrayFieldMappings` columns) aren't checked up front. If one is missing, the affected values are omitted and warnings are recorded.

## Foreign keys
<a name="csv-yaml-foreign-keys"></a>

Foreign keys document how a column in this table relates to a column in another table:

```
foreignKeys:
  - column: PAT_ID
    referencedTable: PT_DEM
    referencedColumn: PAT_ID
  - column: PROV_ID
    referencedTable: PROVIDERS
    referencedColumn: PROV_ID
```


**Foreign key fields**  

| Field | Required | Description | 
| --- | --- | --- | 
| column | Yes | The column in this table that holds the foreign key value. | 
| referencedTable | Yes | The tableName of the table this key points to. Must match a table declared in the profile, or the job fails. | 
| referencedColumn | Yes | The column in the referenced table that this key matches against. | 

**Important**  
Foreign keys don't join tables or create references on their own. To fold child rows into a parent resource, use `aggregationMappings` with a `joinColumn` (see [Aggregation](#csv-yaml-aggregation)). To link one resource to another, use the `resourceReference` transform (see [resourceReference](#csv-yaml-transform-resourcereference)).

## Resource mapping
<a name="csv-yaml-resource-mapping"></a>

A resource mapping declares the FHIR resource type to produce and how to populate it:

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
      - childTable: PT_PHONE
        joinColumn: PAT_ID
        targetFhirArray: telecom
        childFieldMappings: [...]
```

## Field mappings
<a name="csv-yaml-field-mappings"></a>

Each field mapping connects one FHIR element path to one or more source columns:

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
      separator: " "
  - fhirPath: birthDate
    sourceColumn: DOB
    transform:
      type: dateFormat
      fromPattern: MM/dd/yyyy
      toPattern: yyyy-MM-dd
```


**Field mapping fields**  

| Field | Required | Description | 
| --- | --- | --- | 
| fhirPath | Yes | The dot-notation path within the FHIR resource where the value will be placed (for example, name[0].family, telecom[0].value). | 
| sourceColumn | Conditional | The single CSV column to read. Every field mapping must set exactly one of sourceColumn or sourceColumns. Use sourceColumn unless the transform uses concat, either directly or as the innerTransform of a conditional (see sourceColumns). Constant expression mappings also use sourceColumn, even though its value isn't used. The column must exist in the CSV header row. | 
| sourceColumns | Conditional | A list of CSV columns to read. Required when the transform is concat, or a conditional whose innerTransform is (or contains) a concat. Not allowed for any other transform. Mutually exclusive with sourceColumn. | 
| transform | No | An object with a type field and the type-specific parameters as siblings of type. If omitted, the direct transform is used. See [Transform types](#csv-yaml-transform-types). | 
| targetFhirType | No | Overrides the default string type for the output value. See [targetFhirType](#csv-yaml-target-fhir-type). | 

### targetFhirType
<a name="csv-yaml-target-fhir-type"></a>

By default, every mapped value is emitted as a JSON string. Use `targetFhirType` to emit a different JSON type:

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
- fhirPath: multipleBirthInteger
  sourceColumn: BIRTH_ORDER
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

```
# JSON example
- fhirPath: address[0]
  sourceColumn: ADDRESS_JSON
  transform:
    type: direct
  targetFhirType: json
```


**Accepted targetFhirType values**  

| Value | Behavior | 
| --- | --- | 
| boolean | Converts true, TRUE, or 1 to JSON true, and false, FALSE, or 0 to JSON false. Any other value is a conversion failure. | 
| integer | Parses the value as a whole number. | 
| decimal | Parses the value as a floating-point number. | 
| json | Parses the value as JSON and embeds it as a structured object or array instead of a string. See [Embedding JSON with targetFhirType: json](#csv-yaml-target-fhir-type-json). | 

The service handles conversion failures differently depending on the type. For `boolean`, `integer`, and `decimal`, if the service can't convert a value, it emits the original string and records a warning. For `json`, if the service can't parse a value, it omits the field from the output resource and records a warning.

When do I need it?
+ The FHIR element is defined as `boolean`, `integer`, or `decimal` in the spec and your source data stores it as a string.
+ You are populating an `extension` with a `valueInteger` or `valueDecimal` element. Map the extension's `url` in the same resource, because FHIR requires it.
+ You want JSON-native types for downstream consumers that parse the JSON strictly.

#### Embedding JSON with targetFhirType: json
<a name="csv-yaml-target-fhir-type-json"></a>

Some FHIR elements are objects or arrays rather than scalars. If your source column already holds a JSON fragment, set `targetFhirType: json` to embed it as structure. Without it, the service emits the fragment as a quoted string and FHIR validation rejects the resource.

Given this field mapping:

```
- fhirPath: address[0]
  sourceColumn: ADDRESS_JSON
  transform:
    type: direct
  targetFhirType: json
```

And this value in the `ADDRESS_JSON` column:

```
{"city":"Seattle","state":"WA","line":["123 Main St"]}
```

The conversion produces:

```
{
  "address": [
    {
      "city": "Seattle",
      "state": "WA",
      "line": ["123 Main St"]
    }
  ]
}
```

You can also map a sub-path of an embedded object to override one of its fields. Mapping `address[0]` as `json` and `address[0].city` as a scalar in the same table replaces `city` and leaves the other fields intact. The result doesn't depend on the order you list the mappings in.

The following table describes the requirements for using `targetFhirType: json`.


| Requirement | Detail | 
| --- | --- | 
| Must be an object or array | JSON scalars such as 42, "hello", true, and null are rejected. Use integer, decimal, or boolean for those. | 
| Maximum value size | 1,048,576 characters per cell. | 
| Maximum nesting depth | 20 levels. | 
| Must parse cleanly | Trailing characters after the JSON value are rejected. | 

If a value doesn't meet these requirements, the service omits the field and records a warning. The service also omits empty cells.

**Note**  
You can combine `targetFhirType: json` with any transform type. The service parses the value as JSON after the transform runs.

## Transform types
<a name="csv-yaml-transform-types"></a>

The engine supports 8 transform types.

### direct
<a name="csv-yaml-transform-direct"></a>

Copies the source value as-is into the target field with no modification:

```
- fhirPath: name[0].family
  sourceColumn: LAST_NM
  transform:
    type: direct
```

Example: if the CSV column `LAST_NM` contains `Smith`, the output is `"family": "Smith"`.

### concat
<a name="csv-yaml-transform-concat"></a>

Joins multiple source columns into a single string:

```
- fhirPath: name[0].text
  sourceColumns:
    - FIRST_NM
    - LAST_NM
  transform:
    type: concat
    separator: " "
```


**concat parameters**  

| Parameter | Required | Description | 
| --- | --- | --- | 
| separator | Yes | The string placed between each column value. To join values with nothing between them, set it to an empty string (separator: ""). Empty column values are skipped, so the separator never appears twice in a row. | 

### dateFormat
<a name="csv-yaml-transform-dateformat"></a>

Parses a date/time string in the source format and re-formats it for FHIR:

```
- fhirPath: birthDate
  sourceColumn: DOB
  transform:
    type: dateFormat
    fromPattern: MM/dd/yyyy
    toPattern: yyyy-MM-dd
```


**dateFormat parameters**  

| Parameter | Required | Description | 
| --- | --- | --- | 
| fromPattern | Yes | The Java DateTimeFormatter pattern that matches your source data. | 
| toPattern | Yes | The Java DateTimeFormatter pattern for the output. Use FHIR-compatible patterns. | 

Common patterns:
+ `yyyy-MM-dd` – FHIR date (2024-03-15)
+ `yyyy-MM-dd'T'HH:mm:ssXXX` – FHIR dateTime with timezone (2024-03-15T10:30:00-05:00)
+ `MM/dd/yyyy` – US date (03/15/2024)
+ `yyyyMMdd` – compact date (20240315)

**Important**  
A FHIR dateTime that includes a time must include a time zone. A `toPattern` with a time but no zone, such as `yyyy-MM-dd'T'HH:mm:ss`, produces values that can fail FHIR validation. If your source values include an offset, parse it in `fromPattern` (for example, `XX`) and emit it with `XXX`. If they have no offset but are recorded in UTC, append a literal `'Z'` to `toPattern`. Using `XXX` when the source value has no offset fails the transform, and the field is omitted with a warning.

### valueMap
<a name="csv-yaml-transform-valuemap"></a>

Maps discrete source values to FHIR values using a lookup table:

```
- fhirPath: gender
  sourceColumn: SEX_CD
  transform:
    type: valueMap
    mappings:
      M: male
      F: female
      U: unknown
      O: other
```


**valueMap parameters**  

| Parameter | Required | Description | 
| --- | --- | --- | 
| mappings | Yes | A key-value map where the key is the source value and the value is the FHIR output value. | 

If the source value does not match any key in `mappings`, the field is omitted from the output resource and a warning is recorded.

### expression
<a name="csv-yaml-transform-expression"></a>

Builds a string from a template. Each `${COLUMN_NAME}` placeholder is replaced with that column's value from the current row. All other text is copied as-is, so a template with no placeholders produces a constant value:

```
# Constant value
- fhirPath: identifier[0].system
  sourceColumn: MRN
  transform:
    type: expression
    expression: http://hospital.example.org/mrn
```

```
# Value built from source columns
- fhirPath: identifier[0].value
  sourceColumn: MRN
  transform:
    type: expression
    expression: "urn:mrn:${MRN}"
```

The following table describes the `expression` parameters.


**expression parameters**  

| Parameter | Required | Description | 
| --- | --- | --- | 
| expression | Yes | The template string. ${COLUMN\_NAME} placeholders can reference any column in the same table. | 

**Important**  
The template is not evaluated as code. Quotes, `+`, and `$value` are copied into the output literally. For example, `"'phone'"` produces `'phone'` (with the single quotes), not `phone`.  
Every field mapping must set `sourceColumn` or `sourceColumns`, including `expression` mappings that produce a constant. The value of `sourceColumn` isn't used by the template, but the column must exist in the CSV header. Use any column of the table, such as its primary key column.  
If a placeholder names a column that isn't in the CSV, the placeholder is replaced with an empty string and a warning is recorded. If the result is an empty string, the field is omitted.

### conditional
<a name="csv-yaml-transform-conditional"></a>

Chooses the emitted value based on whether a named column is present (non-null and non-empty). If the column is absent and no `absentValue` is set, the element is omitted:

```
- fhirPath: deceasedBoolean
  sourceColumn: DEATH_DT
  transform:
    type: conditional
    conditionColumn: DEATH_DT
    presentValue: "true"
    absentValue: "false"
  targetFhirType: boolean
```


**conditional parameters**  

| Parameter | Required | Description | 
| --- | --- | --- | 
| conditionColumn | Yes | The CSV column whose presence is tested. The condition is met when this column's value is non-null and non-empty. | 
| presentValue | No | A static value to emit when the condition is met. Ignored when innerTransform is set. If neither presentValue nor innerTransform is set, the value of conditionColumn is emitted unchanged. | 
| absentValue | No | A static value to emit when the condition is not met. If omitted, the field is omitted from the output. | 
| innerTransform | No | A nested transform applied when the condition is met. Takes precedence over presentValue. The nested transform reads the field mapping's sourceColumn, or its sourceColumns when the nested transform is concat. | 

Example: if `DEATH_DT` has a value, `deceasedBoolean` is `true`; if `DEATH_DT` is empty, `deceasedBoolean` is `false`.

To transform the value instead of emitting a static one, nest a transform under `innerTransform`. It runs only when `conditionColumn` is present:

```
# DISCH_DT values are recorded in UTC, so a literal 'Z' is appended
- fhirPath: period.end
  sourceColumn: DISCH_DT
  transform:
    type: conditional
    conditionColumn: DISCH_DT
    innerTransform:
      type: dateFormat
      fromPattern: "yyyy-MM-dd HH:mm"
      toPattern: "yyyy-MM-dd'T'HH:mm:ss'Z'"
```

### resourceReference
<a name="csv-yaml-transform-resourcereference"></a>

Generates a FHIR Reference to another resource produced by the mapping:

```
- fhirPath: subject.reference
  sourceColumn: PAT_ID
  transform:
    type: resourceReference
    referencedTable: PT_DEM
    referencedResourceType: Patient
```


**resourceReference parameters**  

| Parameter | Required | Description | 
| --- | --- | --- | 
| referencedTable | Yes | The tableName of the table that produces the target resource. | 
| referencedResourceType | Yes | The FHIR resource type of the target (for example, Patient, Practitioner). | 

The referenced table must be declared in the same mapping profile, and the source column value must match a primary key value in the referenced table. The engine generates a relative reference in the form `ResourceType/generated-id`.

### regex
<a name="csv-yaml-transform-regex"></a>

Applies a Java regular expression to the source value and returns the text captured by one of its groups. Use it to extract a portion of a value:

```
- fhirPath: identifier[0].value
  sourceColumn: RAW_ID
  transform:
    type: regex
    pattern: "^[A-Z]+-(\\d+)$"
    group: 1
```


**regex parameters**  

| Parameter | Required | Description | 
| --- | --- | --- | 
| pattern | Yes | A Java-style regular expression applied to the source value. Define at least one capture group to extract. | 
| group | Yes | The 1-based index of the capturing group whose matched text is returned. Must be 1 or greater. | 

The pattern is matched against the source value, and the text of the capturing group named by `group` is returned. If the pattern does not match, or `group` is greater than the number of capturing groups in the pattern, the field is omitted from the output and a warning is recorded. If the group exists but captures nothing (for example, an optional group that did not participate in the match), the field is omitted without a warning.

More examples:

```
# Extract the code from a prefixed value like "ICD-10:E11.9"
- fhirPath: code.coding[0].code
  sourceColumn: DIAG_CD
  transform:
    type: regex
    pattern: "^[A-Z]+-\\d+:(.+)$"
    group: 1
```

```
# Keep the 5-digit ZIP code from a ZIP+4 value like "62701-1234"
- fhirPath: address[0].postalCode
  sourceColumn: ZIP_RAW
  transform:
    type: regex
    pattern: "^(\\d{5})"
    group: 1
```

## Aggregation
<a name="csv-yaml-aggregation"></a>

Aggregation is how child-table rows fold into a parent resource. A parent table declares which child table to pull from, which column joins it to the parent, and which FHIR path to target. By default each matching child row becomes an array entry. Set `mergeIntoParent` to fold a single child row directly into the parent instead.

### Array aggregation
<a name="csv-yaml-aggregation-array"></a>

Each matching child row becomes a new entry in the target array:

```
aggregationMappings:
  - childTable: PT_PHONE
    joinColumn: PAT_ID
    targetFhirArray: telecom
    childFieldMappings:
      - fhirPath: value
        sourceColumn: PHONE_NUM
        transform:
          type: direct
      - fhirPath: system
        sourceColumn: PHONE_NUM
        transform:
          type: expression
          expression: phone
      - fhirPath: use
        sourceColumn: PHONE_TYPE
        transform:
          type: valueMap
          mappings:
            H: home
            W: work
            M: mobile
```


**Array aggregation fields**  

| Field | Required | Description | 
| --- | --- | --- | 
| childTable | Yes | The tableName of the child table. | 
| joinColumn | Yes | The column in the child table whose value matches the parent row's primaryKeyColumn. Child rows whose joinColumn equals the parent's primary key are collected. | 
| targetFhirArray | Yes | The array field in the parent resource (for example, telecom, address). | 
| childFieldMappings | Yes | Field mappings applied to each child row. Paths are relative to one array entry. | 

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
<a name="csv-yaml-aggregation-merge"></a>

Set `mergeIntoParent: true` for a 1:1 relationship. The child row's fields are written directly onto the parent resource instead of being appended to an array. Only the first matching child row is used. If more than one child row matches the parent's primary key, the additional rows are ignored and a warning is emitted. Each child field mapping's `fhirPath` is a full dot-notation path from the parent resource root, so include the target element in the path (for example, `maritalStatus.text`). Merge paths address singular nested elements. They don't use array index notation such as `[0]`.

```
aggregationMappings:
  - childTable: PT_SUPPLEMENT
    joinColumn: PAT_ID
    mergeIntoParent: true
    childFieldMappings:
      - fhirPath: maritalStatus.text
        sourceColumn: MARITAL_DESC
        transform:
          type: direct
      - fhirPath: managingOrganization.reference
        sourceColumn: ORG_REF
        transform:
          type: direct
```


**Merge aggregation fields**  

| Field | Required | Description | 
| --- | --- | --- | 
| childTable | Yes | The tableName of the child table. | 
| joinColumn | Yes | The column in the child table whose value matches the parent row's primaryKeyColumn. | 
| mergeIntoParent | Yes, for merge mode | Set to true to select merge mode. The field is optional overall and defaults to false; when it is omitted or false, the mapping is treated as array aggregation and targetFhirArray is required. | 
| childFieldMappings | Yes | Field mappings applied to the first matching child row. Each fhirPath is a full path from the parent resource root. | 

Example output (JSON):

```
{
  "resourceType": "Patient",
  "maritalStatus": {
    "text": "Married"
  },
  "managingOrganization": {
    "reference": "Organization/org-123"
  }
}
```

### Rules for aggregation
<a name="csv-yaml-aggregation-rules"></a>
+ Child rows are matched to a parent row when the child's `joinColumn` value equals the parent's `primaryKeyColumn` value. No foreign key declaration is needed.
+ The `childTable` must match the name of a CSV file (without the `.csv` extension) in the input Amazon S3 location. The child table doesn't need to be declared in `tables`.
+ Array aggregation (the default) creates one array entry per matching child row. Merge aggregation (`mergeIntoParent: true`) is for 1:1 relationships: only the first matching child row is used, and any additional matches are ignored with a warning.
+ In array aggregation, each child field path is relative to one array entry. In merge aggregation, each child field path is a full path from the parent resource root.
+ A single resource can have multiple aggregation mappings (for example, one for `telecom` and another for `address`).

## groupByPk
<a name="csv-yaml-group-by-pk"></a>

When a single table contains multiple rows per logical entity (for example, a conditions table with one row per code, where a condition coded in both ICD-10 and SNOMED CT has two rows that share a `COND_ID`), use `groupByPk` to group rows by the primary key and produce array fields from the grouped rows:

```
- tableName: CONDITION_CODES
  primaryKeyColumn: COND_ID
  groupByPk: true
  resourceMappings:
    - targetResourceType: Condition
      fieldMappings:
        - fhirPath: subject.reference
          sourceColumn: PAT_ID
          transform:
            type: resourceReference
            referencedTable: PT_DEM
            referencedResourceType: Patient
      arrayFieldMappings:
        - fhirPath: code.coding[].code
          sourceColumn: CODE
          transform:
            type: direct
        - fhirPath: code.coding[].system
          sourceColumn: CODE_SYSTEM
          transform:
            type: valueMap
            mappings:
              ICD10: http://hl7.org/fhir/sid/icd-10-cm
              SNOMED: http://snomed.info/sct
```

When `groupByPk` is `true`, all rows sharing the same primary key value are collapsed into a single resource. Scalar fields (in `fieldMappings`) take the value from the first row. Array fields (in `arrayFieldMappings`) accumulate one entry per row.

**Important**  
Set `groupByPk` at the table level, as a sibling of `tableName` and `primaryKeyColumn`, not inside a resource mapping. Array fields must be declared in `arrayFieldMappings`, not in `fieldMappings`. Each entry in `arrayFieldMappings` is a single field mapping whose `fhirPath` contains a `[]` placeholder. The engine replaces `[]` with the row index (`[0]`, `[1]`, and so on) for each row in the group, producing one array element per row. Exactly one `[]` placeholder is allowed per path.


**groupByPk vs aggregation**  

| Feature | groupByPk | Aggregation | 
| --- | --- | --- | 
| Data source | Multiple rows in the same table | Rows from a different (child) table | 
| Declared in | The table definition itself (a table-level groupByPk flag) | aggregationMappings in the parent table's resource mapping | 
| Array fields | arrayFieldMappings | childFieldMappings (array mode is the default) | 
| Use when | One CSV file has repeating rows for the same entity | A separate CSV file contains the child data | 

## Child-only tables
<a name="csv-yaml-child-only-tables"></a>

Some tables exist only to provide data that is aggregated into a parent resource, and don't produce FHIR resources of their own. Don't add these tables to the `tables` list. Every entry in `tables` requires at least one `resourceMappings` entry, so a table declared without one fails validation.

Instead, upload the child table's CSV file to the same input Amazon S3 location and reference it by name from the parent's `aggregationMappings`. The value of `childTable` is the CSV file name without the `.csv` extension:

```
# PT_PHONE.csv is uploaded alongside PT_DEM.csv but is not listed under tables
- tableName: PT_DEM
  primaryKeyColumn: PAT_ID
  resourceMappings:
    - targetResourceType: Patient
      fieldMappings: [...]
      aggregationMappings:
        - childTable: PT_PHONE
          joinColumn: PAT_ID
          targetFhirArray: telecom
          childFieldMappings: [...]
```

If a child table should also produce its own resources (for example, an ENCOUNTERS table that is aggregated into Patient and also produces Encounter resources), declare it in `tables` with its own `resourceMappings`.

## Complete example
<a name="csv-yaml-complete-example"></a>

This example converts 4 CSV files (`PT_DEM`, `PT_PHONE`, `PROVIDERS`, and `ENCOUNTERS`) into Patient, Practitioner, and Encounter resources with cross-table references and aggregation. `PT_PHONE` is a child-only table, so it is not listed under `tables`:

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
              fromPattern: MM/dd/yyyy
              toPattern: yyyy-MM-dd
          - fhirPath: gender
            sourceColumn: SEX_CD
            transform:
              type: valueMap
              mappings:
                M: male
                F: female
                U: unknown
          - fhirPath: deceasedBoolean
            sourceColumn: DEATH_DT
            transform:
              type: conditional
              conditionColumn: DEATH_DT
              presentValue: "true"
              absentValue: "false"
            targetFhirType: boolean
        aggregationMappings:
          - childTable: PT_PHONE
            joinColumn: PAT_ID
            targetFhirArray: telecom
            childFieldMappings:
              - fhirPath: value
                sourceColumn: PHONE_NUM
                transform:
                  type: direct
              - fhirPath: system
                sourceColumn: PHONE_NUM
                transform:
                  type: expression
                  expression: phone
              - fhirPath: use
                sourceColumn: PHONE_TYPE
                transform:
                  type: valueMap
                  mappings:
                    H: home
                    W: work
                    M: mobile

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
            sourceColumn: NPI
            transform:
              type: expression
              expression: http://hl7.org/fhir/sid/us-npi

  # Encounters
  - tableName: ENCOUNTERS
    primaryKeyColumn: ENC_ID
    foreignKeys:
      - column: PAT_ID
        referencedTable: PT_DEM
        referencedColumn: PAT_ID
      - column: PROV_ID
        referencedTable: PROVIDERS
        referencedColumn: PROV_ID
    resourceMappings:
      - targetResourceType: Encounter
        fieldMappings:
          - fhirPath: status
            sourceColumn: ENC_ID
            transform:
              type: expression
              expression: finished
          - fhirPath: class.code
            sourceColumn: ENC_TYPE
            transform:
              type: valueMap
              mappings:
                I: IMP
                O: AMB
                E: EMER
          - fhirPath: subject.reference
            sourceColumn: PAT_ID
            transform:
              type: resourceReference
              referencedTable: PT_DEM
              referencedResourceType: Patient
          - fhirPath: participant[0].individual.reference
            sourceColumn: PROV_ID
            transform:
              type: resourceReference
              referencedTable: PROVIDERS
              referencedResourceType: Practitioner
          - fhirPath: period.start
            sourceColumn: ADMIT_DT
            transform:
              type: dateFormat
              # Source values include a UTC offset, for example 202601151430-0500
              fromPattern: yyyyMMddHHmmXX
              toPattern: "yyyy-MM-dd'T'HH:mm:ssXXX"
          - fhirPath: period.end
            sourceColumn: DISCH_DT
            transform:
              type: dateFormat
              fromPattern: yyyyMMddHHmmXX
              toPattern: "yyyy-MM-dd'T'HH:mm:ssXXX"
```

## Tips
<a name="csv-yaml-tips"></a>
+ Start with the Data Transformation AI agent to generate an initial profile from your sample CSV files, then refine it by hand using this reference.
+ Validate your YAML syntax before uploading. A misplaced indent can cause silent mapping failures.
+ Use `direct` transforms wherever possible — they are the fastest and simplest to debug.
+ Keep resource IDs stable. Each resource ID is derived from the data store, `sourceSystemId`, `tableName`, the row's `primaryKeyColumn` value, and `targetResourceType`. Changing any of these after data has been loaded (including renaming a CSV file, which changes its `tableName`) produces new IDs, so the same records are loaded again as duplicate resources.
+ Test with a small subset of data (10–20 rows per table) before running a full transformation to catch mapping errors early.
+ When in doubt about a FHIR path, consult the FHIR R4 resource definitions at `https://hl7.org/fhir/R4/` to confirm the correct element names and cardinalities.