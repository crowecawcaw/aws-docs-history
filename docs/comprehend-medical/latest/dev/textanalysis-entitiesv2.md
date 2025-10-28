# Detect entities (Version 2)

Use the **DetectEntitiesV2** to detect entities in single files or **StartEntitiesDetectionV2Job** for batch analysis on multiple files. You can detect entities in the following categories:

- `ANATOMY:` Detects references to the parts of the body or body systems and the locations of those parts or systems.
- `BEHAVIORAL_ENVIRONMENTAL_SOCIAL`: Detects the behaviors and conditions in the environment that impact a person's health. This includes tobacco usage, alcohol consumption, recreational drug usage, allergies, gender, and race/ethnicity.
- `MEDICAL_CONDITION:` Detects the signs, symptoms, and diagnoses of medical conditions.
- `MEDICATION:` Detects medication and dosage information on the patient.
- `PROTECTED_HEALTH_INFORMATION:` Detects the patient's personal information.
- `TEST_TREATMENT_PROCEDURE:` Detects the procedures that are used to determine a medical condition.
- `TIME_EXPRESSION:` Detects entities related to time when they are associated with a detected entity.
  All six categories are detected by the **DetectEntitiesV2** operation. For analysis specific to detecting PHI, use **DetectPHI** on single files and **StartPHIDetectionJob** for batch analysis.

Amazon Comprehend Medical detects information in the following classes:

- _Entity:_ A text reference to the name of relevant objects, such as people, treatments, medications, and medical conditions. For example, `ibuprofen`.
- _Category:_ The generalized grouping to which an entity belongs. For example, ibuprofen is part of the `MEDICATION` category.
- _Type:_ The type of entity detected within a single category. For example, ibuprofen is in the `GENERIC_NAME` type in the `MEDICATION` category.
- _Attribute:_ Information related to an entity, such as the dosage of a medication. For example, `200 mg` is an attribute of the ibuprofen entity.
- _Trait:_ Something that Amazon Comprehend Medical understands about an entity, based on context. For example, a medication has the `NEGATION` trait if a patient is not taking it.
- _Relationship Type:_ The relationship between an entity and an attribute.
  Amazon Comprehend Medical provides you the location of an entity in the input text. In the Amazon Comprehend console, it shows you the location graphically. When you use the API, it shows you the location by numerical offset.

Each entity and attribute includes a score that indicates the confidence level that Amazon Comprehend Medical has in the accuracy of the detection. Each attribute also has a relationship score. The score indicates the confidence level that Amazon Comprehend Medical has in the accuracy of the relationship between the attribute and its parent entity. Identify the appropriate confidence threshold for your use case. Use high-confidence thresholds in situations that require great accuracy. Filter out data that doesn't meet the threshold.

## Anatomy category

The `ANATOMY` category detects references to the parts of the body or body systems and the locations of those parts or systems.

### Types

- `SYSTEM_ORGAN_SITE`: Body systems, anatomic locations or regions, and body sites.

### Attributes

- `DIRECTION`: Directional terms. For example, left, right, medial, lateral, upper, lower, posterior, anterior, distal, proximal, contralateral, bilateral, ipsilateral, dorsal, ventral, and so on.

## Behavioral, environmental, and social health category

The `BEHAVIORAL_ENVIRONMENTAL_SOCIAL` category detects references to behaviors and conditions in the environment that impact a person's health.

### Type

- `ALCOHOL_CONSUMPTION`: Defines the patient’s alcohol consumption in terms of use status, frequency, amount, and duration.
- `ALLERGIES`: Defines the patient’s allergies and responses to allergens.
- `GENDER`: An identification of the characteristics of gender identity.
- `RACE_ETHNICITY`: A social-political construct of a patient’s identification with particular racial and ethnic groups.
- `REC_DRUG_USE`: Defines the patient’s use of recreational drugs in terms of use status, frequency, amount, and duration.
- `TOBACCO_USE`: Defines the patient’s tobacco usage in terms of use status, frequency, amount, and duration.

The following detected attributes only apply to the types `ALCOHOL_CONSUMPTION`, `TOBACCO_USE`, and `REC_DRUG_USE`:

- `AMOUNT`: The amount of alcohol, tobacco, or recreational drug used.
- `DURATION`: How long the alcohol, tobacco, or recreational drug has been used.
- `FREQUENCY`: How often the alcohol, tobacco, or recreational drug is used.

### Traits

The following detected traits only apply to the types `ALCOHOL_CONSUMPTION`, `ALLERGIES`, `TOBACCO_USE`, and `REC_DRUG_USE`:

- `NEGATION`: An indication that a result or action is negative or not being performed.
- `PAST_HISTORY`: An indication that use of alcohol, tobacco, or recreational drugs is from the patient’s past (prior to the current encounter).

## Medical condition category

The `MEDICAL_CONDITION` category detects the signs, symptoms, and diagnoses of medical conditions. The category has one entity type, four attributes, and four traits. One or more traits can be associated with a type. Contextual information about attributes and their relationship to the diagnosis is detected and mapped to the `DX_NAME` through `RELATIONSHIP_EXTRACTION.` For instance, from the text "chronic pain in left leg", "chronic" is detected as the attribute `ACUITY`, "left" is detected as the attribute `DIRECTION`, and "leg" is detected as the attribute `SYSTEM_ORGAN_SITE`. The relationships of each of these attributes are mapped to the medical condition entity "pain," along with a confidence score.

### Types

- `DX_NAME`: All medical conditions listed. The `DX_NAME` type includes present illness, reason for visit, and medical history.

### Attributes

- `ACUITY`: Determination of disease instance, such as chronic,
  acute, sudden, persistent, or gradual.
- `DIRECTION`: Directional terms. For example, left, right, medial, lateral, upper, lower, posterior, anterior, distal, proximal, contralateral, bilateral, ipsilateral, dorsal, or ventral.
- `SYSTEM_ORGAN_SITE`: Anatomical location.
- `QUALITY`: Any descriptive term of the medical condition, such as stage or grade.

### Traits

- `DIAGNOSIS`: A medical condition that is determined as the cause or result of the symptoms. Symptoms can be found through physical findings, laboratory or radiological reports, or any other means.
- `HYPOTHETICAL`: An indication that a medical condition is expressed as a hypothesis.
- `LOW_CONFIDENCE`: An indication that a medical condition is expressed as having high uncertainty. This is not directly related to the confidence scores provided.
- `NEGATION`: An indication that a result or action is negative or not being performed.
- `PERTAINS_TO_FAMILY`: An indication that a medical condition is relevant to the patient’s family, not the patient.
- `SIGN`: A medical condition that the physician reported.
- `SYMPTOM`: A medical condition that the patient reported.

## Medication category

The `MEDICATION` category detects medication and dosage information for the
patient. One or more attributes can apply to a type.

### Types

- `BRAND_NAME`: The copyrighted brand name of the medication or therapeutic agent.
- `GENERIC_NAME`: The non-brand name, ingredient name, or formula mixture of the medication or therapeutic agent.

### Attributes

- `DOSAGE`: The amount of medication ordered.
- `DURATION`: How long the medication should be administered.
- `FORM`: The form of the medication.
- `FREQUENCY`: How often to administer the medication.
- `RATE`: The administration rate of the medication (primarily for medication infusions or IVs).
- `ROUTE_OR_MODE`: The administration method of the medication.
- `STRENGTH`: The medication strength.

### Traits

- `NEGATION`: Any indication that the patient is not taking a medication.
- `PAST_HISTORY`: An indication that a medication detected is from the patient’s past (prior to current encounter).

## Protected health information category

The `PROTECTED_HEALTH_INFORMATION` category detects the patient's personal
information. See [Detect PHI](textanalysis-phi.md "textanalysis-phi.md") to
learn more about this operation.

### Types

- `ADDRESS`: All geographical subdivisions of an address of any
  facility, units, or wards within a facility.
- `AGE`: All components of age, spans of age, or any age mentioned. This includes those of a patient, family members, or others. The default is in years, unless otherwise noted.
- `EMAIL`: Any email address.
- `ID`: Social Security number, medical record number, facility identification number, clinical trial number, certificate or license number, vehicle or device number, the place of care, or provider. This also includes any biometric number of the patient, such as height, weight, or a lab value.
- `NAME`: All names. Typically, names of the patient, family, or
  provider.
- `PHONE_OR_FAX`: Any phone, fax, or pager number. Excludes named
  phone numbers, such as 1-800-QUIT-NOW and 911.
- `PROFESSION`: Any profession or employer that pertains to the
  patient or the patient's family. It does not include the profession of the
  clinician mentioned in the note.

## Test, treatment, and procedure category

The `TEST_TREATMENT_PROCEDURE` category detects the procedures that are used to determine a medical condition. One or more attributes can be related to an entity of the `TEST_NAME` type.

### Types

- `PROCEDURE_NAME`: Interventions as a one-time action performed on the patient to treat a medical condition or to provide patient care.
- `TEST_NAME`: Procedures performed on a patient for diagnostic, measurement, screening, or rating that might have a resulting value. This includes any procedure, process, evaluation, or rating to determine a diagnosis, to rule out or find a condition, or to scale or score a patient.
- `TREATMENT_NAME`: Interventions performed over a span of time for combating a disease or disorder. This includes groupings of medications, such as antivirals and vaccinations.

### Attributes

- `TEST_VALUE`: The result of a test. Applies only to the `TEST_NAME` entity type.
- `TEST_UNIT`: The unit of measure that might accompany the value of the test. Applies only to the `TEST_NAME` entity type.

### Traits

- `FUTURE`: An indication that a test, treatment, or procedure refers to an action or event that will occur after the subject of the notes.
- `HYPOTHETICAL`: An indication that a test, treatment, or procedure is expressed as a hypothesis.
- `NEGATION`: An indication that a result or action is negative or not being performed.
- `PAST_HISTORY`: An indication that a test, treatment, or procedure is from the patient’s past (prior to current encounter).

## Time expression category

The `TIME_EXPRESSION` category detects entities related to time. This
includes entities such as dates and time expressions such as "three days ago," "today,"
"currently," "day of admission," "last month," or "16 days." Results in this category
are only returned if they are associated with an entity. For example, "Yesterday, the
patient took 200 mg of ibuprofen" would return
`Yesterday` as a `TIME_EXPRESSION` entity
that overlaps with `GENERIC_NAME` entity "ibuprofen." However, it would not
be recognized as an entity in "yesterday, the patient walked their dog."

### Types

- `TIME_TO_MEDICATION_NAME`: The date a medication was taken. The
  attributes specific to this type are `BRAND_NAME` and
  `GENERIC_NAME`.
- `TIME_TO_DX_NAME`: The date a medical condition occurred. The
  attribute for this type is `DX_NAME`.
- `TIME_TO_TEST_NAME`: The date a test was performed. The
  attribute for this type is `TEST_NAME`.
- `TIME_TO_PROCEDURE_NAME`: The date a procedure was performed.
  The attribute for this type is `PROCEDURE_NAME`.
- `TIME_TO_TREATMENT_NAME`: The date a treatment was
  administered. The attribute for this type is
  `TREATMENT_NAME`.

### Relationship type

- The relationship between an entity and an attribute. The recognized `Relationship_type` is the following:

`Overlap` – The `TIME_EXPRESSION` concurs with
the entity detected.
