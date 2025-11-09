# SNOMED CT linking

Use **InferSNOMEDCT** to detect medical entities and link them to concepts from the 2022-03 version of the Systematized Nomenclature of Medicine, Clinical Terms (SNOMED CT). SNOMED CT provides you with a comprehensive vocabulary of medical concepts, including medical conditions and anatomy, medical tests, treatments, and procedures. To learn more about SNOMED CT, visit [SNOMED CT](https://www.snomed.org/value-of-snomedct "https://www.snomed.org/value-of-snomedct").

For each detected medical entity, Amazon Comprehend Medical lists the top five SNOMED CT concept IDs and descriptions associated with the medical concept, along with a confidence score to indicate the confidence of the model in its prediction. The SNOMED CT concept IDs are listed in descending order of confidence along with the confidence scores. The SNOMED CT concept IDs can then be used to structure patient clinical data for medical coding, reporting, or clinical analytics when you use them with the SNOMED CT poly-hierarchy.

**InferSNOMEDCT** is available for customers in the US. For information on SNOMED CT in other countries, and information on SNOMED CT licensing, see [SNOMED CT](https://www.snomed.org/value-of-snomedct "https://www.snomed.org/value-of-snomedct").

**InferSNOMEDCT** is well suited for the following scenarios:

- Assistance for professional medical coding in patient records
- Clinical studies and trials
- Population health management
  **InferSNOMEDCT** detects entities in the following categories.
  Additional contextual information is also detected and linked as attributes or
  traits.

- `MEDICAL_CONDITION`: The signs, symptoms, and diagnoses of medical conditions.
- `ANATOMY`: The parts of the body or body systems and the locations of those parts or systems.
- `TEST_TREATMENT_PROCEDURE`: The procedures that are used to determine a medical condition.

## Anatomy category

The `ANATOMY` category detects references to the parts of the body or body
systems and the locations of those parts or systems.

### Attributes

The following attributes are detected for the `ANATOMY`
category:

- `DIRECTION`: Directional terms. For example, left, right, medial, lateral, upper, lower, posterior, anterior, distal, proximal, contralateral, bilateral, ipsilateral, dorsal, or ventral.
- `SYSTEM_ORGAN_SITE`: Body systems, anatomic locations or
  regions, and body sites.

## Medical condition category

The `MEDICAL_CONDITION` category detects the signs, symptoms, and diagnoses of medical conditions.

### Type

For the **MEDICAL_CONDITION** category, the following type is detected:

- `DX_NAME:` An identification of a medical condition that is determined by evaluation of the symptoms.

### Attributes

The following attributes are detected for the `MEDICAL_CONDITION` category:

- `ACUITY:` Determination of disease instance, such as chronic, acute, sudden, persistent, or gradual.
- `QUALITY:` Any descriptive term of the medical condition, such as stage or grade.
- `DIRECTION`: Directional terms. For example, left, right medial, lateral, upper, lower, posterior, anterior, distal, proximal, contralateral, bilateral, ipsilateral, dorsal, or ventral.
- `SYSTEM_ORGAN_SITE`: Body systems, anatomic locations or regions, and body sites.

### Traits

The following traits are detected for the `MEDICAL_CONDITION` category:

- `DIAGNOSIS`: A medical condition that is determined as the cause or result of the symptoms. Symptoms can be found through physical findings, laboratory or radiological reports, or other means.
- `HYPOTHETICAL`: An indication that a medical condition is expressed as a hypothesis.
- `LOW_CONFIDENCE`: An indication that a medical condition is expressed as having high uncertainty. This is not directly related to the confidence scores provided.
- `NEGATION`: An indication that a medical condition is not present.
- `PERTAINS_TO_FAMILY`: An indication that a medical condition is relevant to the patient’s family, not the patient.
- `SIGN`: A medical condition that is reported by the physician.
- `SYMPTON`: A medical condition that is reported by the patient.

## Test, treatment, and procedure category

The `TEST_TREATMENT_PROCEDURE` category detects the procedures that are used to determine a medical condition.

### Type

For the **TEST_TREATMENT_PROCEDURE** category, the following types are detected:

- `PROCEDURE_NAME:` Interventions performed on the patient to
  treat a medical condition or to provide patient care.
- `TEST_NAME:` Procedures performed on a patient for diagnosis,
  measurement, screening, or a rating that might have a resulting value. This
  includes any procedure, process, evaluation, or rating to determine a
  diagnosis, to rule out or find a condition, or to scale or score a patient.
- `TREATMENT_NAME:` Interventions performed to combat a disease
  or disorder. This includes medications, such as antivirals and
  vaccinations.

### Attributes

For the **TEST_TREATMENT_PROCEDURE** category, the following attributes are detected:

- `TEST_NAME:` The diagnostic test performed.
- `TEST_VALUE:` The numeric results from a diagnostic test.
- `TEST_UNIT:` The units associated with a `TEST_VALUE:` result.
- `PROCEDURE_NAME:` The name of a surgery or medical procedure performed.
- `TREATMENT_NAME:` The name of a treatment administered to a patient.

### Traits

- `FUTURE`: An indication that a test, treatment, or procedure refers to an action or event that will occur after the subject of the notes.
- `HYPOTHETICAL`: An indication that a test, treatment, or procedure is expressed as a hypothesis
- `NEGATION`: An indication that a result or action is negative or not being performed.
- `PAST_HISTORY`: An indication that a test, treatment, or procedure is from the patient’s past (prior to the current encounter).

## SNOMED CT details

Included in the JSON response are the SNOMED CT details, which includes the following information:

- `EDITION:` Only the US edition is supported.
- `VERSIONDATE:` The date stamp of the SNOMED CT version used.
- `LANGUAGE:` Analysis on English (US-EN) language is supported.

## Input and response examples

###### Note

For specific API input and response syntax, see
[InferSNOMEDCT](../api/API_InferSNOMEDCT.md "../api/API_InferSNOMEDCT.md")
in the _Amazon Comprehend Medical API Reference_.

The following example input text shows how the `InferSNOMEDCT` operation works. To view all
input text, scroll over the **Copy** button.

```
"HEENT : Boggy inferior turbinates, No oropharyngeal lesion"
```

The `InferSNOMEDCT` operation returns the following output in JSON format.

```
{
    "Entities": [
        {
            "Category": "ANATOMY",
            "BeginOffset": 0,
            "EndOffset": 5,
            "Text": "HEENT",
            "Traits": [],
            "SNOMEDCTConcepts": [
                {
                    "Code": "69536005",
                    "Score": `Float`,
                    "Description": "Head structure (body structure)"
                },
                {
                    "Code": "429031000124106",
                    "Score": `Float`,
                    "Description": "Review of systems, head, ear, eyes, nose and throat (procedure)"
                },
                {
                    "Code": "385383008",
                    "Score": `Float`,
                    "Description": "Ear, nose and throat structure (body structure)"
                },
                {
                    "Code": "64237003",
                    "Score": `Float`,
                    "Description": "Structure of left half of head (body structure)"
                },
                {
                    "Code": "113028003",
                    "Score": `Float`,
                    "Description": "Ear, nose and throat examination (procedure)"
                }
            ],
            "Score": `Float`,
            "Attributes": [],
            "Type": "SYSTEM_ORGAN_SITE",
            "Id": 0
        },
        {
            "Category": "MEDICAL_CONDITION",
            "BeginOffset": 8,
            "EndOffset": 33,
            "Text": "Boggy inferior turbinates",
            "Traits": [
                {
                    "Score": `Float`,
                    "Name": "SIGN"
                }
            ],
            "SNOMEDCTConcepts": [
                {
                    "Code": "254477009",
                    "Score": `Float`,
                    "Description": "Tumor of inferior turbinate (disorder)"
                },
                {
                    "Code": "260762006",
                    "Score": `Float`,
                    "Description": "Choroidal invasion status (attribute)"
                },
                {
                    "Code": "2455009",
                    "Score": `Float`,
                    "Description": "Revision of lumbosubarachnoid shunt (procedure)"
                },
                {
                    "Code": "19883003",
                    "Score": `Float`,
                    "Description": "Atrophy of nasal turbinates (disorder)"
                },
                {
                    "Code": "256723009",
                    "Score": `Float`,
                    "Description": "Inferior turbinate flap (substance)"
                }
            ],
            "Score": `Float`,
            "Attributes": [
                {
                    "Category": "ANATOMY",
                    "RelationshipScore": `Float`,
                    "EndOffset": 5,
                    "Text": "HEENT",
                    "Traits": [],
                    "SNOMEDCTConcepts": [
                        {
                            "Code": "69536005",
                            "Score": `Float`,
                            "Description": "Head structure (body structure)"
                        },
                        {
                            "Code": "429031000124106",
                            "Score": `Float`,
                            "Description": "Review of systems, head, ear, eyes, nose and throat (procedure)"
                        },
                        {
                            "Code": "385383008",
                            "Score": `Float`,
                            "Description": "Ear, nose and throat structure (body structure)"
                        },
                        {
                            "Code": "64237003",
                            "Score": `Float`,
                            "Description": "Structure of left half of head (body structure)"
                        },
                        {
                            "Code": "113028003",
                            "Score": `Float`,
                            "Description": "Ear, nose and throat examination (procedure)"
                        }
                    ],
                    "Score": `Float`,
                    "RelationshipType": "SYSTEM_ORGAN_SITE",
                    "Type": "SYSTEM_ORGAN_SITE",
                    "Id": 0,
                    "BeginOffset": 0
                }
            ],
            "Type": "DX_NAME",
            "Id": 1
        },
        {
            "Category": "ANATOMY",
            "BeginOffset": 23,
            "EndOffset": 33,
            "Text": "turbinates",
            "Traits": [],
            "SNOMEDCTConcepts": [
                {
                    "Code": "310607007",
                    "Score": `Float`,
                    "Description": "Sarcoidosis of inferior turbinates (disorder)"
                },
                {
                    "Code": "80153006",
                    "Score": `Float`,
                    "Description": "Segmented neutrophil (cell)"
                },
                {
                    "Code": "46607005",
                    "Score": `Float`,
                    "Description": "Nasal turbinate structure (body structure)"
                },
                {
                    "Code": "6553002",
                    "Score": `Float`,
                    "Description": "Inferior nasal turbinate structure (body structure)"
                },
                {
                    "Code": "254477009",
                    "Score": `Float`,
                    "Description": "Tumor of inferior turbinate (disorder)"
                }
            ],
            "Score": `Float`,
            "Attributes": [],
            "Type": "SYSTEM_ORGAN_SITE",
            "Id": 3
        },
        {
            "Category": "ANATOMY",
            "BeginOffset": 39,
            "EndOffset": 52,
            "Text": "oropharyngeal",
            "Traits": [],
            "SNOMEDCTConcepts": [
                {
                    "Code": "31389004",
                    "Score": `Float`,
                    "Description": "Oropharyngeal structure (body structure)"
                },
                {
                    "Code": "33431000119109",
                    "Score": `Float`,
                    "Description": "Lesion of oropharynx (disorder)"
                },
                {
                    "Code": "263376008",
                    "Score": `Float`,
                    "Description": "Entire oropharynx (body structure)"
                },
                {
                    "Code": "716151000",
                    "Score": `Float`,
                    "Description": "Structure of oropharynx and/or hypopharynx and/or larynx (body structure)"
                },
                {
                    "Code": "764786007",
                    "Score": `Float`,
                    "Description": "Oropharyngeal (intended site)"
                }
            ],
            "Score": `Float`,
            "Attributes": [],
            "Type": "SYSTEM_ORGAN_SITE",
            "Id": 5
        },
        {
            "Category": "MEDICAL_CONDITION",
            "BeginOffset": 39,
            "EndOffset": 59,
            "Text": "oropharyngeal lesion",
            "Traits": [
                {
                    "Score": `Float`,
                    "Name": "SIGN"
                }
            ],
            "SNOMEDCTConcepts": [
                {
                    "Code": "31389004",
                    "Score": `Float`,
                    "Description": "Oropharyngeal structure (body structure)"
                },
                {
                    "Code": "33431000119109",
                    "Score": `Float`,
                    "Description": "Lesion of oropharynx (disorder)"
                },
                {
                    "Code": "764786007",
                    "Score": `Float`,
                    "Description": "Oropharyngeal (intended site)"
                },
                {
                    "Code": "418664002",
                    "Score": `Float`,
                    "Description": "Oropharyngeal route (qualifier value)"
                },
                {
                    "Code": "110162001",
                    "Score": `Float`,
                    "Description": "Abrasion of oropharynx (disorder)"
                }
            ],
            "Score": `Float`,
            "Attributes": [
                {
                    "Category": "ANATOMY",
                    "RelationshipScore": `Float`,
                    "EndOffset": 5,
                    "Text": "HEENT",
                    "Traits": [],
                    "SNOMEDCTConcepts": [
                        {
                            "Code": "69536005",
                            "Score": `Float`,
                            "Description": "Head structure (body structure)"
                        },
                        {
                            "Code": "429031000124106",
                            "Score": `Float`,
                            "Description": "Review of systems, head, ear, eyes, nose and throat (procedure)"
                        },
                        {
                            "Code": "385383008",
                            "Score": `Float`,
                            "Description": "Ear, nose and throat structure (body structure)"
                        },
                        {
                            "Code": "64237003",
                            "Score": `Float`,
                            "Description": "Structure of left half of head (body structure)"
                        },
                        {
                            "Code": "113028003",
                            "Score": `Float`,
                            "Description": "Ear, nose and throat examination (procedure)"
                        }
                    ],
                    "Score": `Float`,
                    "RelationshipType": "SYSTEM_ORGAN_SITE",
                    "Type": "SYSTEM_ORGAN_SITE",
                    "Id": 0,
                    "BeginOffset": 0
                }
            ],
            "Type": "DX_NAME",
            "Id": 4
        }
    ],
    "SNOMEDCTDetails": {
        "Edition": "US",
        "VersionDate": "20200901",
        "Language": "en"
    },
    "Characters": {
        "OriginalTextCharacters": 59
    },
    "ModelVersion": "3.2.0.20220301"
}

```
