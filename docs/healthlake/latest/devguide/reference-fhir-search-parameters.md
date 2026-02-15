# FHIR R4 search parameters for HealthLake

Use FHIR [`search`](https://hl7.org/fhir/R4/http.html#search "https://hl7.org/fhir/R4/http.html#search")
interaction to search a set of FHIR resources in a HealthLake data store based on some filter
criteria. The `search` interaction can be performed using either a `GET`
or `POST` request. For searches that involve personally identifiable information (PII) or protected health information (PHI), it's recommended
to use `POST` requests, as PII and PHI is added as part of the request body and is
encrypted in transit.

###### Note

The FHIR `search` interaction described in this chapter is built in
conformance to the HL7 FHIR R4 standard for health care data exchange. Because it is a
representation of a HL7 FHIR service, it is not offered through AWS CLI and AWS SDKs. For
more information, see [`search`](https://hl7.org/fhir/R4/http.html#search "https://hl7.org/fhir/R4/http.html#search") in the **FHIR R4 RESTful API documentation**.

You can also query HealthLake data stores with SQL using Amazon Athena. For more information, see
Integrating.

HealthLake supports the following subset of FHIR R4 search parameters. For more information,
see FHIR R4 search parameters for HealthLake.

## Supported search parameter types

The following table shows the supported search parameter types in HealthLake.

| Supported search parameters types | Search parameter                                                    | Description |
| --------------------------------- | ------------------------------------------------------------------- | ----------- |
| \_id                              | Resource id (not a full URL)                                        |
| \_lastUpdated                     | Date last updated. Server has discretion on the boundary precision. |
| \_tag                             | Search by a resource tag.                                           |
| \_profile                         | Search for all resources tagged with a profile.                     |
| \_security                        | Search on security labels applied to this resource.                 |
| \_source                          | Search on where the resource comes from.                            |
| \_text                            | Search on the narrative of the resource.                            |
| createdAt                         | Search on custom extension createdAt.                               |

###### Note

The following search parameters are only supported for datastores created after December 09, 2023 : \_security, \_source, \_text, createdAt.

The following table shows examples of how to modify query strings based on specified data
types for a given resource type. For clarity, special characters in the examples column have
not been encoded. To make a successful query, ensure that the query string has been properly
encoded.

| Search parameter examples | Search Parameter Types                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Details                                                                                              | Examples                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------- | ------------------------- | --------------------------------------------- | ------------------------- | ----------------------------------------------- | ------------------------- | --- |
| Number                    | Searches for a numerical value in a specified resource. Significant figures<br>are observed. The number of significant digits are specific in by search parameter<br>value, excluding leading zeros. Comparison prefixes are allowed.                                                                                                                                                                                                                                                                                      | `[parameter]=100`<br>`[parameter]=1e2`<br>`[parameter]=lt100`                                        |
| Date/DateTime             | Searches for a specific date or time. The expected format is<br>`yyyy-mm-ddThh:mm:ss[Z                                                                                                                                                                                                                                                                                                                                                                                                                                     | (+                                                                                                   | -)hh:mm]`but can vary.<br>Accepts the following data types:`date`, `dateTime`,<br>`instant`, `Period`, and `Timing`. For more<br>details using these data types in searches, see [date](https://www.hl7.org/fhir/search.html#date "https://www.hl7.org/fhir/search.html#date") in the<br>**FHIR R4 RESTful API documentation**.<br>Comparison prefixes are allowed. | `[parameter]=eq2013-01-14`<br>`[parameter]=gt2013-01-14T10:00`<br>`[parameter]=ne2013-01-14`                                                                                                                                 |
| String                    | Searches for a sequence of characters in a case-sensitive manner.<br>Supports both `HumanName` and `Address` types. For more<br>details, see the [HumanName data type](https://www.hl7.org/fhir/datatypes.html#HumanName "https://www.hl7.org/fhir/datatypes.html#HumanName") entry and the [`Address` data<br>type](https://www.hl7.org/fhir/datatypes.html#Address "https://www.hl7.org/fhir/datatypes.html#Address") entries in the **FHIR R4 documentation**.<br>Advanced search is supported using `:text` modifiers. | `[base]/Patient?given=eve`<br>`[base]/Patient?given:contains=eve`                                    |
| Token                     | Searches for a close-to-exact match against a string of characters, often<br>compared to a pair of medical code values.<br>Case sensitivity is linked to the code system used when creating a<br>query.Subsumption-based queries can help reduce issues linked to case sensitivity.<br>For clarity the `                                                                                                                                                                                                                   | ` has not been encoded.                                                                              | `[parameter]=[system]                                                                                                                                                                                                                                                                                                                                               | [code]`: Here `[system]`refers a<br>coding system, and`[code]` refers to code value found within that<br>specific system.<br>`[parameter]=[code]`: Here your input will match either a code or a<br>system.<br>`[parameter]= | [code]`: Here your input will match a code, and the<br>system property has no identifier. |
| Composite                 | Searches for multiple parameters within a single resource type, using the<br>modifiers`$` and `,` operation.<br>Comparison prefixes are allowed.                                                                                                                                                                                                                                                                                                                                                                           | `/Patient?language=FR,NL&language=EN`<br>`Observation?component-code-value-quantity=http://loinc.org | 8480-6$lt60`<br>`[base]/Group?characteristic-value=gender$mixed`                                                                                                                                                                                                                                                                                                    |
| Quantity                  | Searches for a number, system, and code as values. A number is required, but<br>system and code are optional. Based on the Quantity data type. For more details, see<br>[Quantity](https://www.hl7.org/fhir/datatypes.html#Quantity "https://www.hl7.org/fhir/datatypes.html#Quantity") in<br>the **FHIR R4 documentation**.<br>Uses the following assumed syntax<br>`[parameter]=[prefix][number]                                                                                                                         | [system]                                                                                             | [code]`                                                                                                                                                                                                                                                                                                                                                             | `[base]/Observation?value-quantity=5.4                                                                                                                                                                                       | http://unitsofmeasure.org                                                                 | mg`<br>`[base]/Observation?value-quantity=5.4 | http://unitsofmeasure.org | mg`<br>`[base]/Observation?value-quantity=5.4 | http://unitsofmeasure.org | mg`<br>`[base]/Observation?value-quantity=le5.4 | http://unitsofmeasure.org | mg` |
| Reference                 | Searches for references to other resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `[base]/Observation?subject=Patient/23`<br>`test`                                                    |
| URI                       | Searches for a string of characters that unambiguously identifies a particular<br>resource.                                                                                                                                                                                                                                                                                                                                                                                                                                | `[base]/ValueSet?url=http://acme.org/fhir/ValueSet/123`                                              |
| Special                   | Searches based on integrated medical NLP extensions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Advanced search parameters supported by

HealthLake

HealthLake supports the following advanced search parameters.

| Name                      | Description                                                                                                                                                                                       | Example                                                          | Capability                                                                                                                                                                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_include`                | Used to request that additional resources be returned in a search request. It<br>returns resources which are referenced by the target resource instance.                                          | `Encounter?_include=Encounter:subject`                           |                                                                                                                                                                                                          |
| `_revinclude`             | Used to request that additional resources be returned in a search request. It<br>returns resources that reference the primary resource instance.                                                  | `Patient?_id=`patient-identifier`&_revinclude=Encounter:patient` |                                                                                                                                                                                                          |
| `_summary`                | Summary can be used to request a subset of the resource.                                                                                                                                          | `Patient?_summary=text`                                          | The following summary parameters are supported: `_summary=true`,<br>`_summary=false`, `_summary=text`,<br>`_summary=data`.                                                                               |
| `_elements`               | Request a specific set of elements to be returned as part of a resource in the<br>search results.                                                                                                 | `Patient?_elements=identifier,active,link`                       |                                                                                                                                                                                                          |
| `_total`                  | Returns the number of resources that match the search parameters.                                                                                                                                 | `Patient?_total=accurate`                                        | Support `_total=accurate`, `_total=none`.                                                                                                                                                                |
| `_sort`                   | Indicate the sort order of the returned search results using a comma-separated<br>list. The `-` prefix can be used for any sort rule in the comma-separated<br>list to indicate descending order. | `Observation?_sort=status,-date`                                 | Support sort by fields with types `Number, String, Quantity, Token, URI,<br>Reference`. Sort by `Date` is only supported for data stores<br>created after December 09, 2023. Support up to 5 sort rules. |
| `_count`                  | Control how many resources are returned per page of the search bundle.                                                                                                                            | `Patient?_count=100`                                             | Maximum page size is 100.                                                                                                                                                                                |
| `chaining`                | Search elements of referenced resources. The `.` directs the chained<br>search to the element within the referenced resource.                                                                     | `DiagnosticReport?subject:Patient.name=peter`                    |                                                                                                                                                                                                          |
| `reverse chaining (_has)` | Search for a resource based on the elements of resources that refer to them.                                                                                                                      | `Patient?_has:Observation:patient:code=1234-5`                   |                                                                                                                                                                                                          |

`**\_include**`

Using `_include` in a search query allows for additional specified FHIR
resources to also be returned. Use `_include` to include resources that are linked
forward.

###### Example– To use `_include` to find the patients or the group of patients who

have been diagnosed with a cough

You would search on the `Condition` resource type specifying the diagnostic
code for cough, and then using `_include` specify that you want the
`subject` of that diagnosis returned too. In the `Condition`
resource type `subject` refers to either the patient resource type or the group
resource type.

For clarity, special characters in the example have not been encoded. To make a
successful query ensure that the query string has been properly encoded.

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/
Condition?code=`49727002`&_include=Condition:subject
```

`**\_revinclude**`

Using `_revinclude` in a search query allows for additional specified FHIR
resources to also be returned. Use `_revinclude` to include resources that are
linked backwards.

###### Example– To use `_revinclude` to include related Encounter and Observation

resource types linked to a specific Patient

To make this search, you would first define the individual `Patient` by
specifying their identifier in the `_id` search parameter. Then you would specify
additional FHIR resources using the structure `Encounter:patient` and
`Observation:patient`.

For clarity, special characters in the example have not been encoded. To make a
successful query ensure that the query string has been properly encoded.

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/
Patient?_id=`patient-identifier`&_revinclude=Encounter:patient&_revinclude=Observation:patient
```

`**\_summary**`

Using `_summary` in a search query allows user to request a subset of the FHIR
resource. It can contain one of the following values: `true, text, data, false`.
Any other values will be treated as invalid. The returned resources will be marked with
`'SUBSETTED'` in meta.tag, to indicate that resources are incomplete.

- `true`: Return all supported elements that are marked as 'summary' in the
  base definition of the resource(s).
- `text`: Return only the 'text', 'id', 'meta' elements, and only top-level
  mandatory elements.
- `data`: Return all parts except the 'text' element.
- `false`: Return all parts of the resource(s)

In a single search request, `_summary=text` cannot be combined with
`_include` or `_revinclude` search parameters.

###### Example– Get “text” element of Patient resources in a data store.

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient?_summary=text
```

`**\_elements**`

Using `_elements` in a search query allows for specific FHIR resource elements
to be requested. The returned resources will be marked with `'SUBSETTED'` in
meta.tag, to indicate that resources are incomplete.

The `_elements` parameter consists of a comma-separated list of base element
names such as elements defined at the root level in the resource. Only elements that are
listed are to be returned. If `_elements` parameter values contain invalid
elements, server will ignore them and return mandatory elements and valid elements.

`_elements` will not be applicable to included resources(returned resources
whose search mode is `include`).

In a single search request, `_elements` cannot be combined with
`_summary` search parameters.

###### Example– Get “identifier”, “active”, “link” elements of Patient resources in your

HealthLake data store.

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient?_elements=identifier,active,link
```

`**\_total**`

Using `_total` in a search query will return number of resources that match the
requested search parameters. HealthLake will return the total number of matched
resources(returned resources whose search mode is `match`) in the
`Bundle.total` of search response.

`_total` supports the `accurate`, `none` parameter
values. `_total=estimate` is not supported. Any other values will be treated as
invalid. `_total` is not applicable to the included resources(returned resources
whose search mode is `include`).

###### Example– Get the total number of Patient resources in a data store:

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient?_total=accurate
```

`**\_sort**`

Using `_sort` in the search query arranges the results in a specific order. The
results are ordered based on the comma-separated list of sort rules in priority order. The
sort rules should be valid search parameters. Any other values will be treated as invalid.

In a single search request, you can use up to 5 sort search parameters. You can optionally
use a `-` prefix to indicate descending order. Server will sort on ascending order
by default.

The supported sort search parameter types are: `Number, String, Date, Quantity,
 Token, URI, Reference`. If a search parameter refers to an element that is nested,
this search parameter is not supported for sort. For example, search on 'name' of resource
type Patient refers to Patient.name element with HumanName data type is considered as nested.
Thus, sort on Patient resources by 'name' is not supported.

###### Example– Get Patient resources in a data store and sort them by birthdate in ascending

order:

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient?_sort=birthdate
```

`**\_count**`

The parameter `_count` is defined as an instruction to the server regarding how
many resources should be returned in a single page.

The maximum page size is 100. Any values greater than 100 is invalid.
`_count=0` is not supported.

###### Example– Search for the Patient resource and set search page size to 25:

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient?_count=25
```

`**Chaining and Reverse Chaining(\_has)**`

Chaining and reverse chaining in FHIR provide a more efficient and compact way to obtain
interconnected data, reducing the need for multiple separate queries and making data retrieval
more convenient for developers and users.

If any level of recursion return more than 100 results, HealthLake will return 4xx to
protect data store from being overloaded and causing multiple paginations.

###### Example– Chaining - Gets all DiagnosticReport which refer to a Patient where Patient

name is peter.

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/DiagnosticReport?subject:Patient.name=peter
```

###### Example– Reverse Chaining - Get Patient resources, where the patient resource is

referred to by at least one Observation where the observation has a code of 1234, and where
the Observation refers to the patient resource in the patient search parameter.

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient?_has:Observation:patient:code=1234
```

## Supported search modifiers

Search modifiers are used with string-based fields. All search modifiers in HealthLake use
Boolean-based logic. For example, you could specify `:contains` to specify that
larger string field should include a small string in order for it to be included in your
search results.

| Supported search modifiers | Search modifier                   | Type |
| -------------------------- | --------------------------------- | ---- |
| :missing                   | All parameters except `Composite` |
| :exact                     | String                            |
| :contains                  | String                            |
| :not                       | Token                             |
| :text                      | Token                             |
| :identifier                | Reference                         |
| :below                     | URI                               |

## Supported search comparators

You can use search comparators to control the nature of the matching in a search. You can
use comparators when searching on number, date, and quantity fields. The following table lists
search comparators and their definitions that are supported by HealthLake.

| Supported search comparators | Search comparator                                                                         | Description |
| ---------------------------- | ----------------------------------------------------------------------------------------- | ----------- |
| eq                           | The value for the parameter in the resource is equal to the provided<br>value.            |
| ne                           | The value for the parameter in the resource is not equal to the provided<br>value.        |
| gt                           | The value for the parameter in the resource is greater than the provided<br>value.        |
| lt                           | The value for the parameter in the resource is less than the provided<br>value.           |
| ge                           | The value for the parameter in the resource is greater or equal to the provided<br>value. |
| le                           | The value for the parameter in the resource is less or equal to the provided<br>value.    |
| sa                           | The value for the parameter in the resource starts after the provided<br>value.           |
| eb                           | The value for the parameter in the resource ends before the provided<br>value.            |

## FHIR search parameters not supported by HealthLake

HealthLake supports all FHIR search parameters with the exception of those listed in the
following table. For a full list of FHIR search parameters, see the [FHIR search parameter
registry.](https://hl7.org/fhir/R4/searchparameter-registry.html "https://hl7.org/fhir/R4/searchparameter-registry.html")

Unsupported search parameters| Bundle-composition | Location-near |
| Bundle-identifier | Consent-source-reference |
| Bundle-message | Contract-patient |
| Bundle-type | Resource-content |
| Bundle-timestamp | Resource-query |
