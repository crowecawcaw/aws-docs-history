# HealthLake integrated NLP example requests

**Example 1: `Patient` record ingested into a HealthLake data
store**

Following is an example of a clinical note based on of a `Patient` encounter
with a health care professional.

###### Synthetic data

The text in the following example is synthetic content and does not contain
protected health information (PHI).

```
1991-08-31

# Chief Complaint
- Headache
- Sinus Pain
- Nasal Congestion
- Sore Throat
- Pain with Bright Lights
- Nasal Discharge
- Cough

# History of Present Illness
Jerónimo599 is a 4 month-old non-hispanic white male.

# Social History
Patient has never smoked.

Patient comes from a middle socioeconomic background.

Patient currently has Aetna.

# Allergies
No Known Allergies.

# Medications
No Active Medications.

# Assessment and Plan
Patient is presenting with bee venom (substance), mold (organism), house dust mite (organism), animal dander (substance), grass pollen (substance), tree pollen (substance), lisinopril, sulfamethoxazole / trimethoprim, fish (substance).

## Plan

The patient was prescribed the following medications:
- astemizole 10 mg oral tablet
- nda020800 0.3 ml epinephrine 1 mg/ml auto-injector
The patient was placed on a careplan:
- self-care interventions (procedure)

```

As a reminder, this information is encoded in base64 format in the
`DocumentReference` resource. When this document is ingested into HealthLake and the
Amazon Comprehend Medical API operations are complete, to see the results, you can start with the
`GET`request on the `DocumentReference` resource type.

```
GET https://https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/`eeb8005725ae22b35b4edbdc68cf2dfd`/r4/DocumentReference
```

When the Amazon Comprehend Medical API operations are successful, look for these key-value pairs inside the
`extension` linked to the following `"url":
 "http://healthlake.amazonaws.com/aws-cm/"`

```
{
		"url": "http://healthlake.amazonaws.com/aws-cm/status/",
		"valueString": "SUCCESS"
	},
	{
		"url": "http://healthlake.amazonaws.com/aws-cm/message/",
		"valueString": "The AWS HealthLake integrated medical NLP operation was successful."
	}
```

The following tabs show you how the ingested medical record is reported in your HealthLake data
store based on the resource type.

DocumentReference
To the see the results for a single `DocumentReference` resource type,
make a `GET` request where the `id` of a specific resource is
provided.

```
GET https://https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/`eeb8005725ae22b35b4edbdc68cf2dfd`/r4/DocumentReference/`0e938f03-da7f-4178-acd8-eea9586c46ed`
```

When successful, you get a `200` HTTP response code, and the following
JSON response (that has been truncated for clarity).

Here is the `http://healthlake.amazonaws.com/system-generated-resources/`
portion. You can see that a new
`Linkage/`e366d29f-2c22-4c19-866e-09603937935a`` has been added. You can also see where HealthLake has added inference-based findings to
 specific`Observation`and`Condition` resource types.

To see how these resource types have been amended, choose the related tabs.

```
{
		"extension": [
			{
				"url": "http://healthlake.amazonaws.com/linkage",
				"valueReference": {
					"reference": "Linkage/e366d29f-2c22-4c19-866e-09603937935a"
				}
			},
			{
				"url": "http://healthlake.amazonaws.com/nlp-entity",
				"valueReference": {
					"reference": "Observation/c6e0a3ff-7a17-4d8b-bfd0-d02d7da090c5"
				}
			},
			{
				"url": "http://healthlake.amazonaws.com/nlp-entity",
				"valueReference": {
					"reference": "Condition/0854e1f3-894d-448e-a8d9-3af5b9902baf"
				}
			}
		],
		"url": "http://healthlake.amazonaws.com/system-generated-resources/"
	}
```

Linkage
To the see the results for a single `Linkage` resource type, make a
`GET` request where the `ID` of a specific resource is provided.

```
GET https://https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/`eeb8005725ae22b35b4edbdc68cf2dfd`/r4/Linkage/`e366d29f-2c22-4c19-866e-09603937935a`
```

When successful, you get a `200` HTTP response code, and the following
truncated JSON response.

The response contains the `item` element. In it, the key-value pair
`"type": "source"` indicates the specific `DocumentReference`
entry used to modify the `Condition` and `Observations` listed
under the `"type": "alternate"` key-value pair.

_You also see the `meta` element, and a corresponding key-value
pair, `"tag": [{"display": "SYSTEM_GENERATED"}]`, indicating these
resources were created by HealthLake._

```
{
		"resourceType": "Linkage",
		"id": "e366d29f-2c22-4c19-866e-09603937935a",
		"active": true,
		"item":
		[
			{
				"type": "alternate",
				"resource": {
					"reference": "Observation/c6e0a3ff-7a17-4d8b-bfd0-d02d7da090c5",
					"type": "Observation"
				}
			},
			{
				"type": "alternate",
				"resource": {
					"reference": "Condition/9d5c1ef6-f822-4faf-b55f-7c70f2a4aa8d",
					"type": "Condition"
				}
			},
			{
				"type": "source",
				"resource": {
					"reference": "DocumentReference/0e938f03-da7f-4178-acd8-eea9586c46ed",
					"type": "DocumentReference"
				}
			}
		],
		"meta": {
			"lastUpdated": "2022-10-21T19:38:31.327Z",
			"tag": [{
				"display": "SYSTEM_GENERATED"
			}]
		}
	}
```

Resource type: Observation
To the see the results for a single `Observation` resource type, make a
`GET` request where the `ID` of a specific resource is provided.

```
GET https://https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/`eeb8005725ae22b35b4edbdc68cf2dfd`/r4/Observation/`e366d29f-2c22-4c19-866e-09603937935a`
```

The results of the Amazon Comprehend Medical API operations are amended to the following elements:
`code`, `meta`, and `modifierExtension`.

###### `code`

An element of type `CodeableConcept`. To learn more, see [`CodeableConcept`](https://hl7.org/fhir/R4/datatypes.html#CodeableConcept "https://hl7.org/fhir/R4/datatypes.html#CodeableConcept") in the
**FHIR R4 documentation**.

HealthLake appends the following three key-value pairs.

- `"system": "http://healthlake.amazonaws.com/aws-cm/infer-icd10/"`:
  Where the URL refers to a specific Amazon Comprehend Medical API operation. In this case,
  InferICD10CM.
- `"code": "A52.06"`: Where `A52.06` is the ICD-10-CM code
  that identifies the concept found in the knowledge base from the Centers for Disease
  Control.
- `"display": "Other syphilitic heart involvement"`: Where `"Other
syphilitic heart involvement"` is the long description of the ICD-10-CM code
  in the ontology.

The following truncated JSON response contains only the `code`
element.

```
"code": {
		"coding":
		[
		  {
			"system": "http://healthlake.amazonaws.com/aws-cm/infer-icd10/",
			"code": "A52.06",
			"display": "Other syphilitic heart involvement"
		  }
		],
		"text": "Other syphilitic heart involvement"
	}
```

To understand the model's confidence that the assigned ICD-10-CM code is correct,
use the `modifierExtension` element.

###### `meta`

The `meta` element contains metadata that indicates whether the
`code` element contains details that have been added by the Amazon Comprehend Medical API
operations.

The following truncated JSON response contains only the `meta`
element.

```
"meta": {
		"lastUpdated": "2022-10-21T19:38:30.879Z",
		"tag": [{
			"display": "SYSTEM_GENERATED"
		}]
	}
```

###### `modifierExtension`

The `modifierExtension` element contains more details about the level
of confidence of the assigned codes found in the `code` element. It also
has key-value pairs that provide a link back to the original DocumentReference used to
generate the results and the related Linkage resource type.

For each `coding` element added, you will see an
`entity-score` and an `entity-Concept-Score` added to the
modifierExtension. For each value in the key-value pair, you see a score. For
`entity-score`, this score is the level of confidence that Amazon Comprehend Medical has in
the accuracy of the detection. For `entity-Concept-Score`, this score is the
level of confidence that Amazon Comprehend Medical has that the entity is accurately linked to an ICD-10-CM
concept.

The following truncated JSON response contains only the
`modifierExtension` element.

```
"modifierExtension": [{
			"url": "http://healthlake.amazonaws.com/aws-cm/infer-icd10/aws-cm-icd10-entity-score",
			"valueDecimal": 0.45005733
		},
		{
			"url": "http://healthlake.amazonaws.com/aws-cm/infer-icd10/aws-cm-icd10-entity-Concept-Score",
			"valueDecimal": 0.1111792
		},
		{
			"url": "http://healthlake.amazonaws.com/system-generated-linkage",
			"valueReference": {
				"reference": "Linkage/e366d29f-2c22-4c19-866e-09603937935a"
			}
		},
		{
			"url": "http://healthlake.amazonaws.com/source-document-reference",
			"valueReference": {
				"reference": "DocumentReference/0e938f03-da7f-4178-acd8-eea9586c46ed"
			}
		}
	]
```

**Full JSON Response**

```
{
		"subject": {
			"reference": "Patient/0679b7b7-937d-488a-b48d-6315b8e7003b"
		},
		"resourceType": "Observation",
		"status": "unknown",
		"code": {
			"coding": [{
				"system": "http://healthlake.amazonaws.com/aws-cm/infer-icd10/",
				"code": "A52.06",
				"display": "Other syphilitic heart involvement"
			}],
			"text": "Other syphilitic heart involvement"
		},
		"meta": {
			"lastUpdated": "2022-10-21T19:38:30.879Z",
			"tag": [{
				"display": "SYSTEM_GENERATED"
			}]
		},
		"modifierExtension": [{
				"url": "http://healthlake.amazonaws.com/aws-cm/infer-icd10/aws-cm-icd10-entity-score",
				"valueDecimal": 0.45005733
			},
			{
				"url": "http://healthlake.amazonaws.com/aws-cm/infer-icd10/aws-cm-icd10-entity-Concept-Score",
				"valueDecimal": 0.1111792
			},
			{
				"url": "http://healthlake.amazonaws.com/system-generated-linkage",
				"valueReference": {
					"reference": "Linkage/e366d29f-2c22-4c19-866e-09603937935a"
				}
			},
			{
				"url": "http://healthlake.amazonaws.com/source-document-reference",
				"valueReference": {
					"reference": "DocumentReference/0e938f03-da7f-4178-acd8-eea9586c46ed"
				}
			}
		],
		"id": "7e88c7c5-21a5-4dd7-8fc2-a02474fba583"
	}
```

Condition
To the see the results for a single `Condition` resource type, make a
`GET` request where the `ID` of a specific resource is provided.

```
GET https://https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/`eeb8005725ae22b35b4edbdc68cf2dfd`/r4/Condition/`b06d343d-ddb8-4f36-82cb-853fcd434dfd`
```

The results of the Amazon Comprehend Medical API operations are amended to the following elements:
`code`, `meta`, and `modifierExtension`.

###### `code`

An element of type `CodeableConcept`. To learn more, see [`CodeableConcept`](https://hl7.org/fhir/R4/datatypes.html#CodeableConcept "https://hl7.org/fhir/R4/datatypes.html#CodeableConcept") in the
**FHIR R4 documentation**.

HealthLake appends the following three key-value pairs.

- `"system": "http://healthlake.amazonaws.com/aws-cm/infer-icd10/"`:
  Where the URL refers to a specific Amazon Comprehend Medical API operation. In this case,
  InferICD10CM.
- `"code": "I70.0"`: Where `A52.06` is the ICD-10-CM code
  that identifies the concept found in the knowledge base from the Centers for Disease
  Control.
- `"display": "Atherosclerosis of aorta"`: Where `"Other
syphilitic heart involvement"` is the long description of the ICD-10-CM code
  in the ontology.

The following truncated JSON response contains only the `code`
element.

```
"code": {
		"coding":
		[
		  {
			"system": "http://healthlake.amazonaws.com/aws-cm/infer-icd10/",
			"code": "I70.0",
			"display": "Atherosclerosis of aorta"
		  }
		],
		"text": "Atherosclerosis of aorta"
	}
```

To understand the model's confidence that the assigned ICD-10-CM code is correct,
use the `modifierExtension` element.

###### `meta`

The `meta` element contains metadata that indicates whether the
`code` element contains details that have been added by the Amazon Comprehend Medical API
operations.

The following truncated JSON response contains only the `meta`
element.

```
"meta": {
		"lastUpdated": "2022-10-21T19:38:30.877Z",
		"tag": [{
			"display": "SYSTEM_GENERATED"
		}]
	}
```

###### `modifierExtension`

The `modifierExtension` element contains more details about the level
of confidence of the assigned codes found in the `code` element. It also
has key-value pairs that provide a link back to the original DocumentReference used to
generate the results and the related Linkage resource type.

For each `coding` element added, you will see an
`entity-score` and an `entity-Concept-Score` added to the
modifierExtension. For each value in the key-value pair, you see a score. For
`entity-score`, this score is the level of confidence that Amazon Comprehend Medical has in
the accuracy of the detection. For `entity-Concept-Score`, this score is the
level of confidence that Amazon Comprehend Medical has that the entity is accurately linked to an ICD-10-CM
concept.

The following truncated JSON response contains only the
`modifierExtension` element.

```
"modifierExtension": [{
			"url": "http://healthlake.amazonaws.com/aws-cm/infer-icd10/aws-cm-icd10-entity-score",
			"valueDecimal": 0.94417894
		},
		{
			"url": "http://healthlake.amazonaws.com/aws-cm/infer-icd10/aws-cm-icd10-entity-Concept-Score",
			"valueDecimal": 0.8458298
		},
		{
			"url": "http://healthlake.amazonaws.com/system-generated-linkage",
			"valueReference": {
				"reference": "Linkage/e366d29f-2c22-4c19-866e-09603937935a"
			}
		},
		{
			"url": "http://healthlake.amazonaws.com/source-document-reference",
			"valueReference": {
				"reference": "DocumentReference/0e938f03-da7f-4178-acd8-eea9586c46ed"
			}
		}
	]
```

**Full JSON Response**

```
{
		"subject": {
			"reference": "Patient/0679b7b7-937d-488a-b48d-6315b8e7003b"
		},
		"resourceType": "Condition",
		"code": {
			"coding": [{
				"system": "http://healthlake.amazonaws.com/aws-cm/infer-icd10/",
				"code": "I70.0",
				"display": "Atherosclerosis of aorta"
			}],
			"text": "Atherosclerosis of aorta"
		},
		"meta": {
			"lastUpdated": "2022-10-21T19:38:30.877Z",
			"tag": [{
				"display": "SYSTEM_GENERATED"
			}]
		},
		"modifierExtension": [{
				"url": "http://healthlake.amazonaws.com/aws-cm/infer-icd10/aws-cm-icd10-entity-score",
				"valueDecimal": 0.94417894
			},
			{
				"url": "http://healthlake.amazonaws.com/aws-cm/infer-icd10/aws-cm-icd10-entity-Concept-Score",
				"valueDecimal": 0.8458298
			},
			{
				"url": "http://healthlake.amazonaws.com/system-generated-linkage",
				"valueReference": {
					"reference": "Linkage/e366d29f-2c22-4c19-866e-09603937935a"
				}
			},
			{
				"url": "http://healthlake.amazonaws.com/source-document-reference",
				"valueReference": {
					"reference": "DocumentReference/0e938f03-da7f-4178-acd8-eea9586c46ed"
				}
			}
		],
		"id": "b06d343d-ddb8-4f36-82cb-853fcd434dfd"
	}
```

**Example 2: A `DocumentReference` that contains
`MedicationStatement` resource type**

Here is an example of a clinical note based off of a patient's encounter with a medical
professional.

###### Synthetic data

The text in this example is synthetic content and does not contain protected health information (PHI).

```
Tom is not prescribed Advil
```

The following tabs show how the ingested medical record is reported in your HealthLake data
store based on the resource type.

DocumentReference
To the see the results for a single `DocumentReference` resource type,
make a `GET` request where the `ID` of a specific resource is
provided.

```
GET https://https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/`eeb8005725ae22b35b4edbdc68cf2dfd`/r4/DocumentReference/`c549125d-a218-421f-b8bf-23614c5e796c`
```

When successful, you get a `200` HTTP response code and the following
truncated JSON response.

The key-value pair, `"url":
 "http://healthlake.amazonaws.com/system-generated-resources/"`, indicates that
the resource types inside this `extension` have been added by Amazon Comprehend Medical API
operations. You can see the new `Linkage` resource type, and multiple
`MedicationStatement` resources.

```
"extension": [{
			"extension": [{
					"url": "http://healthlake.amazonaws.com/linkage",
					"valueReference": {
						"reference": "Linkage/394bb244-177b-4409-8657-26b20ed56dd7"
					}
				},
				{
					"url": "http://healthlake.amazonaws.com/nlp-entity",
					"valueReference": {
						"reference": "MedicationStatement/cbf6af10-b0b9-451c-bdde-99611e3498a8"
					}
				},
				{
					"url": "http://healthlake.amazonaws.com/nlp-entity",
					"valueReference": {
						"reference": "MedicationStatement/9a89b0d3-6681-45ca-9926-27951edce5c7"
					}
				},
				{
					"url": "http://healthlake.amazonaws.com/nlp-entity",
					"valueReference": {
						"reference": "MedicationStatement/4a01f6c8-5f3a-4122-80ab-405312f96aa2"
					}
				},
				{
					"url": "http://healthlake.amazonaws.com/nlp-entity",
					"valueReference": {
						"reference": "MedicationStatement/fbfb77d8-70cf-4579-b4c0-d6fe3c01656b"
					}
				},
				{
					"url": "http://healthlake.amazonaws.com/nlp-entity",
					"valueReference": {
						"reference": "MedicationStatement/1340c9ce-9c48-4bf9-9b2f-d0ab027f5e0b"
					}
				}
			],
			"url": "http://healthlake.amazonaws.com/system-generated-resources/"
		}
```

Linkage
To the see the results for a single `Linkage` resource type, make a
`GET` request where the `ID` of a specific resource is provided.

```
GET https://https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/`eeb8005725ae22b35b4edbdc68cf2dfd`/r4/Linkage/`394bb244-177b-4409-8657-26b20ed56dd7`
```

When successful, you get a `200` HTTP response code and the following
JSON response.

The response contains the `item` element. In it, the key-value pair
`"type": "source"` indicates the specific `DocumentReference`
entry used to modify the `MedicationStatement` resource types.

You can also see the `meta` element and a corresponding key-value pair,
`"tag": [{"display": "SYSTEM_GENERATED"}]`, indicating that these resources
were created by HealthLake.

```
{
		"resourceType": "Linkage",
		"id": "394bb244-177b-4409-8657-26b20ed56dd7",
		"active": true,
		"item": [{
				"type": "alternate",
				"resource": {
					"reference": "MedicationStatement/cbf6af10-b0b9-451c-bdde-99611e3498a8",
					"type": "MedicationStatement"
				}
			},
			{
				"type": "alternate",
				"resource": {
					"reference": "MedicationStatement/9a89b0d3-6681-45ca-9926-27951edce5c7",
					"type": "MedicationStatement"
				}
			},
			{
				"type": "alternate",
				"resource": {
					"reference": "MedicationStatement/4a01f6c8-5f3a-4122-80ab-405312f96aa2",
					"type": "MedicationStatement"
				}
			},
			{
				"type": "alternate",
				"resource": {
					"reference": "MedicationStatement/fbfb77d8-70cf-4579-b4c0-d6fe3c01656b",
					"type": "MedicationStatement"
				}
			},
			{
				"type": "alternate",
				"resource": {
					"reference": "MedicationStatement/1340c9ce-9c48-4bf9-9b2f-d0ab027f5e0b",
					"type": "MedicationStatement"
				}
			},
			{
				"type": "source",
				"resource": {
					"reference": "DocumentReference/c549125d-a218-421f-b8bf-23614c5e796c",
					"type": "DocumentReference"
				}
			}
		],
		"meta": {
			"lastUpdated": "2022-10-24T20:05:03.501Z",
			"tag": [{
				"display": "SYSTEM_GENERATED"
			}]
		}
	}
```

MedicationStatement
To the see the results for a single `MedicationStatement` resource type,
make a `GET` request where the `ID` of a specific resource is
provided.

```
GET https://https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/`eeb8005725ae22b35b4edbdc68cf2dfd`/r4/MedicationStatement/`9a89b0d3-6681-45ca-9926-27951edce5c7`
```

The `MedicationStatement` resource type is where the results of the
Amazon Comprehend Medical InferRxNorm API operation are found. The results are amended to the following
elements: `medicationCodeableConcept`, `meta`, and
`modifierExtension`.

###### medicationCodeableConcept

An element of type `CodeableConcept`. To learn more, see [`CodeableConcept`](https://hl7.org/fhir/R4/datatypes.html#CodeableConcept "https://hl7.org/fhir/R4/datatypes.html#CodeableConcept") in the
**FHIR R4 documentation**.

HealthLake appends the following three key-value pairs.

- `"system": ""http://healthlake.amazonaws.com/aws-cm/infer-rxnorm/`:
  Where the URL refers to a specific Amazon Comprehend Medical API operation. In this case,
  InferRxNorm.
- `"code": "731533"`: Where `731533` is an RxNorm concept
  ID, also known as the RxCUI.
- `"display": "ibuprofen 200 MG Oral Capsule [Advil]"`: Where
  `ibuprofen 200 MG Oral Capsule [Advil]` is the description of the
  RxNorm concept.

The following truncated JSON response contains only the
`MedicationStatement` element.

```
"medicationCodeableConcept": {
		"coding": [
			{
				"system": "http://healthlake.amazonaws.com/aws-cm/infer-rxnorm/",
				"code": "731533",
				"display": "ibuprofen 200 MG Oral Capsule [Advil]"
			}
		]
	}
```

###### `meta`

The `meta` element contains metadata that indicates whether the
`code` element contains details that have been added by the Amazon Comprehend Medical API
operations.

The following truncated JSON response contains only the `meta`
element.

```
"meta": {
		"lastUpdated": "2022-10-24T20:05:02.800Z",
		"tag": [
			{
				"display": "SYSTEM_GENERATED"
			}
		]
	}
```

###### `modifierExtension`

The `modifierExtension` element contains key-value pairs that provide a
link back to the original `DocumentReference` used to generate the results
and the related Linkage resource type.

```
"modifierExtension": [
			{
				"url": "http://healthlake.amazonaws.com/system-generated-linkage",
				"valueReference": {
					"reference": "Linkage/394bb244-177b-4409-8657-26b20ed56dd7"
				}
			},
			{
				"url": "http://healthlake.amazonaws.com/source-document-reference",
				"valueReference": {
					"reference": "DocumentReference/c549125d-a218-421f-b8bf-23614c5e796c"
				}
			}
	]
```
