# Querying HealthLake data with SQL

When you import your FHIR data into HealthLake data store, the nested JSON FHIR data
simultaneously undergoes an ETL process and is stored in Apache Iceberg open table format in
Amazon S3. Each FHIR resource type from your HealthLake data store is converted into a table, where
it can be queried using Amazon Athena. The tables can be queried individually or as group using
SQL-based queries. Because of the structure of data stores, your data is imported into Athena
as multiple different data types. To learn more about creating SQL queries that can access
these data types, see [Query arrays with complex types and nested
structures](../../../athena/latest/ug/rows-and-structs.md "../../../athena/latest/ug/rows-and-structs.md") in the _Amazon Athena User Guide_.

###### Note

All examples in this topic use fictionalized data created using Synthea. To learn more
about creating a data store preloaded with Synthea data, see [Creating a HealthLake data store](managing-data-stores-create.md "managing-data-stores-create.md").

For each element in a resource type, the FHIR specification defines a cardinality. The
cardinality of an element defines the lower and upper bounds of how many times this element
can appear. When constructing a SQL query, you must take this into account. For example,
let's look at some elements in [Resource type:
Patient](https://hl7.org/fhir/R4/patient.html "https://hl7.org/fhir/R4/patient.html").

- **Element: Name** The FHIR specification sets the
  cardinality as `0..*`.

The element is captured as an array.

```
[{
	id = null,
	extension = null,
	use = official,
	_use = null,
	text = null,
	_text = null,
	family = Wolf938,
	_family = null,
	given = [Noel608],
	_given = null,
	prefix = null,
	_prefix = null,
	suffix = null,
	_suffix = null,
	period = null
}]
```

In Athena, to see how a resource type has been ingested, search for it under
**Tables and views**. To access elements in this array, you can
use dot notation. Here's a simple example that would access the values for
`given` and `family`.

```
SELECT
    name[1].given as FirstName,
    name[1].family as LastName
FROM Patient
```

- **Element: MaritalStatus** The FHIR specification
  sets the cardinality as `0..1`.

This element is captured as JSON.

```
{
	id = null,
	extension = null,
	coding = [
		{
			id = null,
			extension = null,
			system = http: //terminology.hl7.org/CodeSystem/v3-MaritalStatus,
				_system = null,
			version = null,
			_version = null,
			code = S,
			_code = null,
			display = Never Married,
			_display = null,
			userSelected = null,
			_userSelected = null
		}

	],
	text = Never Married,
	_text = null
}
```

In Athena, to see how a resource type has been ingested, search for it under
**Tables and views**. To access key-value pairs in the JSON,
you can use dot notation. Because it isn't an array, no array index is required.
Here's a simple example that would access the value for `text`.

```
SELECT
    maritalstatus.text as MaritalStatus
FROM Patient
```

To learn more about accessing and searching JSON, see [Querying JSON](../../../athena/latest/ug/querying-JSON.md "../../../athena/latest/ug/querying-JSON.md") in the _Athena
User Guide_.

Athena Data Manipulation Language (DML) query statements are based on Trino. Athena does not
support all of Trino's features, and there are _significant_ differences.
To learn more, see [DML queries,
functions, and operators](../../../athena/latest/ug/functions-operators-reference-section.md "../../../athena/latest/ug/functions-operators-reference-section.md") in the _Amazon Athena User
Guide_.

Furthermore, Athena supports multiple data types that you may encounter when creating
queries of your HealthLake data store. To learn more about data types in Athena, see [Data types in
Amazon Athena](../../../athena/latest/ug/data-types.md "../../../athena/latest/ug/data-types.md") in the _Amazon Athena User Guide_.

To learn more about how SQL queries work in Athena, see [SQL reference for Amazon Athena](../../../athena/latest/ug/ddl-sql-reference.md "../../../athena/latest/ug/ddl-sql-reference.md") in
the _Amazon Athena User Guide_.

Each tab shows examples of how to search on the specified resource types and associated
elements using Athena.

Element: Extension
The element `extension` is used to create custom fields in a data
store.

This example shows you how to access the features of the
`extension` element found in the `Patient` resource
type.

When your HealthLake data store is imported into Athena, the elements of a resource
type are parsed differently. Because the structure of the `element`
is variable, it cannot be fully specified in the schema. To handle that
variability, the elements inside the array are passed as strings.

In the table description of `Patient`, you can see the element
`extension` described as `array<string>`, which
means you can access the elements of array by using an index value. To access
the elements of the string, however, you must use
`json_extract`.

Here is a single entry from the `extension` element found in the
patient table.

```
[{
		"valueString": "Kerry175 Cummerata161",
		"url": "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName"
	},
	{
		"valueAddress": {
			"country": "DE",
			"city": "Hamburg",
			"state": "Hamburg"
		},
		"url": "http://hl7.org/fhir/StructureDefinition/patient-birthPlace"
	},
	{
		"valueDecimal": 0.0,
		"url": "http://synthetichealth.github.io/synthea/disability-adjusted-life-years"
	},
	{
		"valueDecimal": 5.0,
		"url": "http://synthetichealth.github.io/synthea/quality-adjusted-life-years"
	}
]
```

Even though this is valid JSON, Athena treats it as a string.

This SQL query example demonstrates how you can create a table that contains
the `patient-mothersMaidenName` and `patient-birthPlace`
elements. To access these elements, you need to use different array indices and
`json_extract.`

```
SELECT
    extension[1],
    json_extract(extension[1], '$.valueString') AS MothersMaidenName,
    extension[2],
    json_extract(extension[2], '$.valueAddress.city') AS birthPlace
FROM patient
```

To learn more about queries that involve JSON, see [Extracting data from
JSON](../../../athena/latest/ug/extracting-data-from-JSON.md "../../../athena/latest/ug/extracting-data-from-JSON.md") in the _Amazon Athena User Guide_.

Element: birthDate (Age)
Age is _not_ an element of the Patient resource type in
FHIR. Here are two examples for searches that filter based on age.

Because age is not an element, we use the `birthDate` for the SQL
queries. To see how an element has been ingested into FHIR, search for the table
name under **Tables and views**. You can see that it is of type
**string**.

**Example 1**: Calculating a value for age

In this sample SQL query, we use a built-in SQL tool,
`current_date` and `year` to extract those components.
Then, we subtract them to return a patient's actual age as a column called
`age`.

```
SELECT
	(year(current_date) - year(date(birthdate))) as age
FROM patient
```

**Example 2**: Filtering for patients who are
born before `2019-01-01` and are `male`.

The SQL query shows you how to use the `CAST` function to cast the
`birthDate` element as type `DATE`, and how to filter
based on two criteria in the `WHERE` clause. Because the element is
ingested as type **string** by default, we must
`CAST` it as type `DATE`. Then you can use the
`<` operator to compare it to a different date,
`2019-01-01`. By using `AND`, you can add a second
criteria to the `WHERE` clause.

```
SELECT birthdate
FROM patient
-- we convert birthdate (varchar) to date  > cast that as date too
WHERE CAST(birthdate AS DATE) < CAST('2019-01-01' AS DATE) AND gender = 'male'
```

Resource type: Location
This example shows searches for locations within the Location resource type
where the city name is Attleboro.

```
SELECT *
FROM Location
WHERE address.city='ATTLEBORO'
LIMIT 10;
```

Element: Age

```
SELECT birthdate
FROM patient
-- we convert birthdate (varchar) to date  > cast that as date too
WHERE CAST(birthdate AS DATE) < CAST('2019-01-01' AS DATE) AND gender = 'male'
```

Resource type: Condition
The resource type condition stores diagnosis data related to issues that have
risen to a level of concern. HealthLake's integrated medical natural language
processing (NLP) generates _new_ `Condition` resources based
on details found in the DocumentReference resource type. When new resource are
generated, HealthLake appends the tag `SYSTEM_GENERATED` to the
`meta` element. This sample SQL query demonstrates how you can
search the condition table and return results where the
`SYSTEM_GENERATED` results have been removed.

To learn more about HealthLake's integrated natural language processing (NLP), see
[Integrated natural language processing (NLP) for HealthLake](integrating-nlp.md "integrating-nlp.md").

```
SELECT *
FROM condition
WHERE meta.tag[1] is NULL
```

You can also search within a specified string element to filter your query
further. The `modifierextension` element contains details about which
`DocumentReference` resource was used to generate a set of conditions. Again, you must use
`json_extract` to access the nested JSON elements that are
brought into Athena as a string.

This sample SQL query demonstrates how you can search for all the `Condition`
that has been generated based off of a specific `DocumentReference`. Use `CAST`
to set the JSON element as a string so that you can use `LIKE` to
compare.

```
SELECT
    meta.tag[1].display as SystemGenerated,
    json_extract(modifierextension[4], '$.valueReference.reference') as DocumentReference
FROM condition
WHERE meta.tag[1].display = 'SYSTEM_GENERATED'

AND CAST(json_extract(modifierextension[4], '$.valueReference.reference') as VARCHAR) LIKE '%DocumentReference/67aa0278-8111-40d0-8adc-43055eb9d18d%'
```

Resource type: Observation
The resource type, Observation stores measurements and simple assertions made
about a patient, device, or other subject. HealthLake's integrated natural language
processing (NLP) generates _new_ `Observation` resources
based on details found in a `DocumentReference` resource. This sample SQL query includes
`WHERE meta.tag[1] is NULL` commented out, which means that the
`SYSTEM_GENERATED` results are included.

```
SELECT valueCodeableConcept.coding[1].code
FROM Observation
WHERE  valueCodeableConcept.coding[1].code = '266919005'
-- WHERE meta.tag[1] is NULL
```

This column was imported as an [`struct`](https://iceberg.apache.org/spec/#schemas-and-data-types "https://iceberg.apache.org/spec/#schemas-and-data-types"). Therefore, you can access elements inside
it using dot notation.

Resource type: MedicationStatement
MedicationStatement is a FHIR resource type that you can use to store details
about medications a patient has taken, is taking, or will take in the future.
HealthLake's integrated medical natural language processing (NLP) generates new
MedicationStatement resources based on documents found in the DocumentReference
resource type. When new resources are generated, HealthLake appends the tag
`SYSTEM_GENERATED` to the `meta` element. This sample
SQL query demonstrates how to create a query that filters based off of a single
patient by using their identifier and finds resources that have been added by
HealthLake's integrated NLP.

```
SELECT *
FROM medicationstatement
WHERE meta.tag[1].display = 'SYSTEM_GENERATED' AND subject.reference = 'Patient/0679b7b7-937d-488a-b48d-6315b8e7003b';
```

To learn more about HealthLake's integrated natural language processing (NLP), see
[Integrated natural language processing (NLP) for HealthLake](integrating-nlp.md "integrating-nlp.md").
