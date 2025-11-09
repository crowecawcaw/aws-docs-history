# ICD-10-CM linking

Use InferICD10CM to detect possible medical conditions as entities and link them to codes from the 2026 version of the [International Classification of Diseases, 10th Revision, Clinical Modification (ICD-10-CM)](https://www.cdc.gov/nchs/icd/icd-10-cm/?CDC_AAref_Val=https://www.cdc.gov/nchs/icd/icd-10-cm.htm "https://www.cdc.gov/nchs/icd/icd-10-cm/?CDC_AAref_Val=https://www.cdc.gov/nchs/icd/icd-10-cm.htm"). The ICD-10-CM is provided by the US Centers for Disease Control and Prevention (CDC).

When medical conditions are detected, `InferICD10CM` returns the matching ICD-10-CM codes and descriptions. The detected conditions are listed in descending order of confidence. The scores indicate the confidence in the accuracy of the entities matched to the concepts found in the text. Related information such as family history, signs, symptoms, and negation are recognized as traits. Additional information such as anatomical designations and acuity are listed as attributes.

InferICD10CM is well-suited for the following scenarios:

- Assisting the professional medical coding of patient records
- Clinical studies and trials
- Integration with a medical software system
- Early detection and diagnosis
- Population health management

## ICD-10-CM category

**InferICD10CM** detects entities in the `MEDICAL_CONDITION` category. Additional related information is also detected and linked as attributes or traits.

## ICD-10-CM types

**InferICD10CM** detects entities of the types `DX_NAME` and `TIME_EXPRESSION`.

## ICD-10-CM traits

**InferICD10CM** detects the following contextual information as traits:

- `DIAGNOSIS`: An identification of a medical condition that is determined by evaluation of the symptoms.
- `HYPOTHETICAL`: An indication that a medical condition is expressed as a hypothesis.
- `LOW_CONFIDENCE`: An indication that a medical condition is expressed as having high uncertainty. This is not directly related to the confidence scores provided.
- `NEGATION`: An indication that a medical condition is not present.
- `PERTAINS_TO_FAMILY`: An indication that a medical condition is relevant to the patient’s family, not the patient.
- `SIGN`: A medical condition that is reported by the physician.
- `SYMPTOM`: A medical condition that is reported by the patient.

## ICD-10-CM attributes

**InferICD10CM** detects the following contextual information as attributes:

- `DIRECTION`: Directional terms. For example, left, right, medial, lateral, upper, lower, posterior, anterior, distal, proximal, contralateral, bilateral, ipsilateral, dorsal, or ventral.
- `SYSTEM_ORGAN_SITE`: Anatomical location.
- `ACUITY:` Determination of a disease instance, such as chronic, acute, sudden, persistent, or gradual. This only applies to the `MEDICAL_CONDITION` type.
- `QUALITY`: Any descriptive term of the medical condition, such as stage or grade.

## Time expression category

The `TIME_EXPRESSION` category detects entities related to time. This includes entities such as dates, and time expressions such as "three days ago," "today," "currently," "day of admission," "last month," or "16 days." Results in this category are only returned if they are associated with an entity. For example, the expression, "Yesterday, the patient was diagnosed with influenza" would return `Yesterday` as a `TIME_EXPRESSION` entity that overlaps with the `DX_NAME` entity, "influenza." However, "yesterday" would not be recognized as an entity in the expression, "yesterday, the patient walked their dog."

## Types

The recognized type of `TIME_EXPRESSION` is `TIME_TO_DX_NAME`: the date that a medical condition occurred. The attribute for this type is `DX_NAME`.

## Relationship type

The `RELATIONSHIP_TYPE` refers to the relationship between an entity and an attribute. The recognized `RELATIONSHIP_TYPE` is `OVERLAP`– the `TIME_EXPRESSION` concurs with the entity detected.

## Input and response examples

###### Note

For specific API input and response syntax, see
[InferICD10CM](../api/API_InferICD10CM.md "../api/API_InferICD10CM.md")
in the _Amazon Comprehend Medical API Reference_.

The following example input text shows how the `InferICD10CM` operation works. To view all
input text, scroll over the **Copy** button.

```
"The patient is a 71-year-old female patient of Dr. X. The patient presented to the emergency room last evening with approximately 7 to 8 day history of abdominal pain which has been persistent. She has had no nausea and vomiting, but has had persistent associated anorexia. She is passing flatus, but had some obstipation symptoms with the last bowel movement two days ago. She denies any bright red blood per rectum and no history of recent melena. Her last colonoscopy was approximately 5 years ago with Dr. Y. She has had no definite fevers or chills and no history of jaundice. The patient denies any significant recent weight loss."
```

The `InferICD10CM` operation returns the following output in JSON format (abbreviated for brevity).

```
{
    "Entities": [
        {
            "Id": 1,
            "Text": "abdominal pain",
            "Category": "MEDICAL_CONDITION",
            "Type": "DX_NAME",
            "Score": `Float`,
            "BeginOffset": 153,
            "EndOffset": 167,
            "Attributes": [
                {
                    "Type": "ACUITY",
                    "Score": `Float`,
                    "RelationshipScore": `Float`,
                    "Id": 2,
                    "BeginOffset": 183,
                    "EndOffset": 193,
                    "Text": "persistent",
                    "Traits": []
                }
            ],
            "Traits": [
                {
                    "Name": "SYMPTOM",
                    "Score": `Float`
                }
            ],
            "ICD10CMConcepts": [
                {
                    "Description": "Unspecified abdominal pain",
                    "Code": "R10.9",
                    "Score": `Float`
                },
                {
                    "Description": "Epigastric pain",
                    "Code": "R10.13",
                    "Score": `Float`
                },
                {
                    "Description": "Lower abdominal pain, unspecified",
                    "Code": "R10.30",
                    "Score": `Float`
                },
                {
                    "Description": "Generalized abdominal pain",
                    "Code": "R10.84",
                    "Score": `Float`
                },
                {
                    "Description": "Upper abdominal pain, unspecified",
                    "Code": "R10.10",
                    "Score": `Float`
                }
            ]
        }
...
    "ModelVersion": "3.2.0.20251001"
}

```

`InferICD10CM` also recognizes when an entity is negated in text. For instance,
if a patient is not experiencing a symptom, both the symptom and negation are identified as traits
and listed with a confidence score. Based on the input for the previous example, the symptom `Nausea`
will be listed under `NEGATION` because the patient isn't experiencing nausea.

```
{
    "Id": 3,
    "Text": "nausea",
    "Category": "MEDICAL_CONDITION",
    "Type": "DX_NAME",
    "Score": `Float`,
    "BeginOffset": 210,
    "EndOffset": 216,
    "Attributes": [],
    "Traits": [
        {
            "Name": "SYMPTOM",
            "Score": `Float`
        },
        {
            "Name": "NEGATION",
            "Score": `Float`
        }
    ],
    "ICD10CMConcepts": [
        {
            "Description": "Nausea with vomiting, unspecified",
            "Code": "R11.2",
            "Score": `Float`
        },
        {
            "Description": "Nausea",
            "Code": "R11.0",
            "Score": `Float`
        }
    ]
}

```
