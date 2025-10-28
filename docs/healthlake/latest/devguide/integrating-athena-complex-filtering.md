# Example SQL queries with complex

filtering

The following examples demonstrate how to use Amazon Athena SQL queries with complex filtering
to locate FHIR data from a HealthLake data store.

###### Example Create filtering criteria based on demographic data

Identifying the correct patient demographics is important when creating a patient
cohort. This sample query demonstrates how you can use Trino dot notation and
`json_extract` to filter data in your HealthLake data store.

```
SELECT
    id
    , CONCAT(name[1].family, ' ', name[1].given[1]) as name
    , (year(current_date) - year(date(birthdate))) as age
    , gender as gender
    , json_extract(extension[1], '$.valueString') as MothersMaidenName
    , json_extract(extension[2], '$.valueAddress.city') as birthPlace
    , maritalstatus.coding[1].display as maritalstatus
    , address[1].line[1] as addressline
    , address[1].city as city
    , address[1].district as district
    , address[1].state as state
    , address[1].postalcode as postalcode
    , address[1].country as country
    , json_extract(address[1].extension[1], '$.extension[0].valueDecimal') as latitude
    , json_extract(address[1].extension[1], '$.extension[1].valueDecimal') as longitude
    , telecom[1].value as telNumber
    , deceasedboolean as deceasedIndicator
    , deceaseddatetime
FROM `database`.patient;
```

Using the Athena Console, you can further sort and download the results.

###### Example Create filters for a patient and their related conditions

The following example query demonstrates how you can find and sort all the related
conditions for the patients found in a HealthLake data store.

```
SELECT
	patient.id as patientId
    , condition.id  as conditionId
    , CONCAT(name[1].family, ' ', name[1].given[1]) as name
    , condition.meta.tag[1].display
    , json_extract(condition.modifierextension[1], '$.valueDecimal') AS confidenceScore
    , category[1].coding[1].code as categoryCode
    , category[1].coding[1].display as categoryDescription
    , code.coding[1].code as diagnosisCode
    , code.coding[1].display as diagnosisDescription
    , onsetdatetime
    , severity.coding[1].code as severityCode
    , severity.coding[1].display as severityDescription
    , verificationstatus.coding[1].display as verificationStatus
    , clinicalstatus.coding[1].display as clinicalStatus
    , encounter.reference as encounterId
    , encounter.type as encountertype
FROM `database`.patient, condition
WHERE CONCAT('Patient/', patient.id) = condition.subject.reference
ORDER BY name;
```

You can use the Athena console to further sort the results or download them for further
analysis.

###### Example Create filters for patients and their related observations

The following example query demonstrates how to find and sort all related observations
for patients found in a HealthLake data store.

```
SELECT
	patient.id as patientId
    , observation.id as observationId
    , CONCAT(name[1].family, ' ', name[1].given[1]) as name
    , meta.tag[1].display
    , json_extract(modifierextension[1], '$.valueDecimal') AS confidenceScore
    , status
    , category[1].coding[1].code as categoryCode
    , category[1].coding[1].display as categoryDescription
    , code.coding[1].code as observationCode
    , code.coding[1].display as observationDescription
    , effectivedatetime
    , CASE
		WHEN valuequantity.value IS NOT NULL THEN CONCAT(CAST(valuequantity.value AS VARCHAR),' ',valuequantity.unit)
      	WHEN valueCodeableConcept.coding [ 1 ].code IS NOT NULL THEN CAST(valueCodeableConcept.coding [ 1 ].code AS VARCHAR)
      	WHEN valuestring IS NOT NULL THEN CAST(valuestring AS VARCHAR)
      	WHEN valueboolean IS NOT NULL THEN CAST(valueboolean AS VARCHAR)
      	WHEN valueinteger IS NOT NULL THEN CAST(valueinteger AS VARCHAR)
      	WHEN valueratio IS NOT NULL THEN CONCAT(CAST(valueratio.numerator.value AS VARCHAR),'/',CAST(valueratio.denominator.value AS VARCHAR))
      	WHEN valuerange IS NOT NULL THEN CONCAT(CAST(valuerange.low.value AS VARCHAR),'-',CAST(valuerange.high.value AS VARCHAR))
      	WHEN valueSampledData IS NOT NULL THEN CAST(valueSampledData.data AS VARCHAR)
      	WHEN valueTime IS NOT NULL THEN CAST(valueTime AS VARCHAR)
      	WHEN valueDateTime IS NOT NULL THEN CAST(valueDateTime AS VARCHAR)
      	WHEN valuePeriod IS NOT NULL THEN valuePeriod.start
      	WHEN component[1] IS NOT NULL THEN CONCAT(CAST(component[2].valuequantity.value AS VARCHAR),' ',CAST(component[2].valuequantity.unit AS VARCHAR), '/', CAST(component[1].valuequantity.value AS VARCHAR),' ',CAST(component[1].valuequantity.unit AS VARCHAR))
    END AS observationvalue
	, encounter.reference as encounterId
    , encounter.type as encountertype
FROM `database`.patient, observation
WHERE CONCAT('Patient/', patient.id) = observation.subject.reference
ORDER BY name;

```

###### Example Create filtering conditions for a patient and their related procedures

Connecting procedures to patients is an important aspect of healthcare. The following
SQL example query demonstrates how to use FHIR `Patient` and
`Procedure` resource types to accomplish this. The following SQL query
will return all patients and their related procedures found in your HealthLake data
store.

```
SELECT
	patient.id  as patientId
	, PROCEDURE.id as procedureId
	, CONCAT(name[1].family, ' ', name[1].given[1]) as name
	, status
	, category.coding[1].code as categoryCode
	, category.coding[1].display as categoryDescription
	, code.coding[1].code as procedureCode
	, code.coding[1].display as procedureDescription
	, performeddatetime
	, performer[1]
	, encounter.reference as encounterId
	, encounter.type as encountertype
FROM `database`.patient, procedure
WHERE CONCAT('Patient/', patient.id) = procedure.subject.reference
ORDER BY name;
```

You can use the Athena console to download the results for further analysis or sort
them to better understand the results.

###### Example Create filtering conditions for a patient and their related prescriptions

Seeing a current list of medications that patients are taking is important. Using
Athena, you can write a SQL query that uses both the `Patient` and
`MedicationRequest` resource types found in your HealthLake data store.

The following SQL query joins the `Patient` and
`MedicationRequest` tables imported into Athena. It also organizes the
prescriptions into their individual entries by using dot notation.

```
SELECT
	patient.id  as patientId
	, medicationrequest.id  as medicationrequestid
	, CONCAT(name[1].family, ' ', name[1].given[1]) as name
	, status
	, statusreason.coding[1].code as categoryCode
	, statusreason.coding[1].display as categoryDescription
	, category[1].coding[1].code as categoryCode
	, category[1].coding[1].display as categoryDescription
	, priority
	, donotperform
	, encounter.reference as encounterId
	, encounter.type as encountertype
	, medicationcodeableconcept.coding[1].code as medicationCode
	, medicationcodeableconcept.coding[1].display as medicationDescription
	, dosageinstruction[1].text as dosage
FROM `database`.patient, medicationrequest
WHERE CONCAT('Patient/', patient.id ) = medicationrequest.subject.reference
ORDER BY name
```

You can use the Athena console to sort the results or download them for further
analysis.

###### Example See medications found in the `MedicationStatement` resource type

The following example query shows you how to organize the nested JSON imported into
Athena using SQL. The query uses the FHIR `meta` element to indicate when a
medication has been added by HealthLake's integrated natural language processing (NLP). It
also uses `json_extract` to search for data inside the array of JSON strings.
For more information, see [Natural language processing](integrating-nlp.md "integrating-nlp.md").

```
SELECT
	medicationcodeableconcept.coding[1].code as medicationCode
	, medicationcodeableconcept.coding[1].display as medicationDescription
	, meta.tag[1].display
	, json_extract(modifierextension[1], '$.valueDecimal') AS confidenceScore
FROM medicationstatement;
```

You can use the Athena console to download these results or sort them.

###### Example Filter for a specific disease type

The example shows how you can find a group of patients, aged 18 to 75, who have been
diagnosed with diabetes.

```
SELECT patient.id as patientId,
	condition.id as conditionId,
	CONCAT(name [ 1 ].family, ' ', name [ 1 ].given [ 1 ]) as name,
	(year(current_date) - year(date(birthdate))) AS age,
	CASE
		WHEN condition.encounter.reference IS NOT NULL THEN condition.encounter.reference
		WHEN observation.encounter.reference IS NOT NULL THEN observation.encounter.reference
	END as encounterId,
	CASE
		WHEN condition.encounter.type IS NOT NULL THEN observation.encounter.type
		WHEN observation.encounter.type IS NOT NULL THEN observation.encounter.type
	END AS encountertype,
	condition.code.coding [ 1 ].code as diagnosisCode,
	condition.code.coding [ 1 ].display as diagnosisDescription,
	observation.category [ 1 ].coding [ 1 ].code as categoryCode,
	observation.category [ 1 ].coding [ 1 ].display as categoryDescription,
	observation.code.coding [ 1 ].code as observationCode,
	observation.code.coding [ 1 ].display as observationDescription,
	effectivedatetime AS observationDateTime,
	CASE
      WHEN valuequantity.value IS NOT NULL THEN CONCAT(CAST(valuequantity.value AS VARCHAR),' ',valuequantity.unit)
      WHEN valueCodeableConcept.coding [ 1 ].code IS NOT NULL THEN CAST(valueCodeableConcept.coding [ 1 ].code AS VARCHAR)
      WHEN valuestring IS NOT NULL THEN CAST(valuestring AS VARCHAR)
      WHEN valueboolean IS NOT NULL THEN CAST(valueboolean AS VARCHAR)
      WHEN valueinteger IS NOT NULL THEN CAST(valueinteger AS VARCHAR)
      WHEN valueratio IS NOT NULL THEN CONCAT(CAST(valueratio.numerator.value AS VARCHAR),'/',CAST(valueratio.denominator.value AS VARCHAR))
      WHEN valuerange IS NOT NULL THEN CONCAT(CAST(valuerange.low.value AS VARCHAR),'-',CAST(valuerange.high.value AS VARCHAR))
      WHEN valueSampledData IS NOT NULL THEN CAST(valueSampledData.data AS VARCHAR)
      WHEN valueTime IS NOT NULL THEN CAST(valueTime AS VARCHAR)
      WHEN valueDateTime IS NOT NULL THEN CAST(valueDateTime AS VARCHAR)
      WHEN valuePeriod IS NOT NULL THEN valuePeriod.start
      WHEN component[1] IS NOT NULL THEN CONCAT(CAST(component[2].valuequantity.value AS VARCHAR),' ',CAST(component[2].valuequantity.unit AS VARCHAR), '/', CAST(component[1].valuequantity.value AS VARCHAR),' ',CAST(component[1].valuequantity.unit AS VARCHAR))
    END AS observationvalue,
	CASE
		WHEN condition.meta.tag [ 1 ].display = 'SYSTEM GENERATED' THEN 'YES'
		WHEN condition.meta.tag [ 1 ].display IS NULL THEN 'NO'
		WHEN observation.meta.tag [ 1 ].display = 'SYSTEM GENERATED' THEN 'YES'
		WHEN observation.meta.tag [ 1 ].display IS NULL THEN 'NO'
  	END AS IsSystemGenerated,
  CAST(
    json_extract(
      condition.modifierextension [ 1 ],
      '$.valueDecimal'
    ) AS int
  ) AS confidenceScore
FROM `database`.patient,
	`database`.condition,
	`database`.observation
WHERE CONCAT('Patient/', patient.id) = condition.subject.reference
	AND CONCAT('Patient/', patient.id) = observation.subject.reference
  	AND (year(current_date) - year(date(birthdate))) >= 18
  	AND (year(current_date) - year(date(birthdate))) <= 75
  	AND condition.code.coding [ 1 ].display like ('%diabetes%');
```

Now you can use the Athena console to sort the results or download them for further
analysis.
