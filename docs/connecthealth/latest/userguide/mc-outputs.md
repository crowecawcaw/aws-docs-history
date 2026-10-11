

# Medical coding outputs
<a name="mc-outputs"></a>

When a job reaches `SUCCEEDED`, medical coding writes a results file to the Amazon S3 output location you specified. The `GetMedicalCodingJob` response points to that file.

**Topics**
+ [Where results are stored](#mc-output-location)
+ [Results file structure](#mc-output-structure)
+ [Rendering the results](#mc-output-rendering)

## Where results are stored
<a name="mc-output-location"></a>


| Location | How to access | 
| --- | --- | 
|  `GetMedicalCodingJob` response | Returns the S3 URI of the results file in `medicalCodingOutput.uri`. | 
| Amazon S3 | Contains the results file at `{s3OutputPath}/{jobId}/medical-codes.json`, where `s3OutputPath` is the output location you provided when you started the job. The file has the content type `application/json`. | 

Medical coding writes the results file using the credentials of the caller that started the job, so that caller needs permission to write to the output location. If the domain uses a customer managed AWS KMS key, the file is encrypted with server-side encryption with AWS KMS keys (SSE-KMS). Otherwise, it is encrypted with server-side encryption with Amazon S3 managed keys (SSE-S3).

The following example shows a `GetMedicalCodingJob` response for a job that has succeeded:

```
{
  "jobId": "4f9c2e1a-7b3d-4e8a-9c21-5d6f0a1b2c3d",
  "jobArn": "arn:aws:health-agent:us-east-1:111122223333:domain/dom-a1b2c3d4e5f6g7h8/medical-coding-job/4f9c2e1a-7b3d-4e8a-9c21-5d6f0a1b2c3d",
  "jobStatus": "SUCCEEDED",
  "creationTime": "2026-10-03T14:05:12Z",
  "updatedTime": "2026-10-03T14:06:40Z",
  "medicalCodingOutput": {
    "uri": "s3://amzn-s3-demo-bucket/medical-coding/4f9c2e1a-7b3d-4e8a-9c21-5d6f0a1b2c3d/medical-codes.json"
  },
  "outputDataConfig": {
    "s3OutputPath": "s3://amzn-s3-demo-bucket/medical-coding/"
  },
  "encounterContext": {
    "encounterType": "IN_PERSON",
    "encounterReason": "Follow-up of diabetes and hypertension",
    "afterHours": false
  },
  "patientContext": {
    "sex": "FEMALE",
    "status": "ESTABLISHED",
    "dateOfBirth": "1961-04-12",
    "insurance": "Medicare"
  },
  "text": "Established patient seen in clinic for follow-up of type 2 diabetes and essential hypertension. ..."
}
```

The response also returns the inputs the job was submitted with. `medicalCodingOutput` is present only after the job succeeds. When `jobStatus` is `FAILED`, the response includes `statusDetails`, which describes the reason.

## Results file structure
<a name="mc-output-structure"></a>

The results file is a JSON object with one field, `medicalCodes`, which is an array of suggested codes:

```
{ "medicalCodes": [ ... ] }
```

Each code carries its own confidence score. The file has no overall confidence score for the encounter.

Except for `unit`, any field can be absent from a given code. Check that a field is present before you use it, and treat an absent array the same as an empty one.

### Suggested code
<a name="mc-output-medical-code"></a>

Each entry in `medicalCodes` has the following fields.


| Field | Type | Description | 
| --- | --- | --- | 
|  `sequence`  | Integer | The position of the code in the list, 0 or greater. | 
|  `system`  | String | The code set: `ICD10` for ICD-10-CM diagnosis codes, or `CPT` for procedure and service codes, including E/M codes. Modifiers are not a separate system. They appear in the `modifiers` array of a CPT code. | 
|  `version`  | String | The version of the code set. | 
|  `name`  | String | The code itself. | 
|  `description`  | String | A human-readable description of the code. | 
|  `unit`  | Integer | The number of units, 0 or greater. Defaults to 1. | 
|  `evidence`  | Array of evidence objects | The passages of the input clinical documentation that support the code. See [Evidence](#mc-output-evidence). | 
|  `linkedCodes`  | Array of linked code objects | For CPT codes, the ICD-10-CM codes that establish medical necessity for the service. See [Linked code](#mc-output-linked-code). | 
|  `modifiers`  | Array of modifier objects | CPT modifiers that apply to the code. Present only when modifiers apply. See [Modifier](#mc-output-modifier). | 
|  `confidence`  | Number | A score from 0 to 1 that reflects medical necessity, diagnosis-to-treatment alignment, and code specificity. | 

### Evidence
<a name="mc-output-evidence"></a>


| Field | Type | Description | 
| --- | --- | --- | 
|  `text`  | String | The supporting passage, copied from the input clinical documentation. This field can contain protected health information (PHI). Handle the results file with the same controls you apply to the clinical note. | 
|  `startOffset`  | Integer | The character position in the input `text` where the passage starts. | 
|  `endOffset`  | Integer | The character position in the input `text` where the passage ends. | 

### Linked code
<a name="mc-output-linked-code"></a>


| Field | Type | Description | 
| --- | --- | --- | 
|  `name`  | String | The linked code. | 
|  `system`  | String | The code set of the linked code: `ICD10` or `CPT`. | 
|  `sequence`  | Integer | The position of the link in the `linkedCodes` list. | 

### Modifier
<a name="mc-output-modifier"></a>


| Field | Type | Description | 
| --- | --- | --- | 
|  `code`  | String | The modifier code. | 
|  `description`  | String | A human-readable description of the modifier. | 

### Example results file
<a name="mc-output-example"></a>

The following example is for an office visit where an established patient presents with fever and sore throat, a rapid strep test is positive, and an intramuscular antibiotic injection is given. CPT codes and descriptions are shown as placeholders.

```
{
  "medicalCodes": [
    {
      "sequence": 1,
      "system": "ICD10",
      "name": "J02.0",
      "description": "Streptococcal pharyngitis",
      "unit": 1,
      "evidence": [
        {
          "text": "Physical exam revealed inflamed pharyngeal tissue with white exudate on tonsils.",
          "startOffset": 76,
          "endOffset": 156
        },
        {
          "text": "Rapid strep test positive.",
          "startOffset": 157,
          "endOffset": 183
        }
      ],
      "linkedCodes": [],
      "confidence": 0.98
    },
    {
      "sequence": 2,
      "system": "CPT",
      "name": "<E/M visit code>",
      "description": "<CPT description>",
      "unit": 1,
      "evidence": [
        {
          "text": "Patient presented with fever of 102F, sore throat, and fatigue for 3 days.",
          "startOffset": 0,
          "endOffset": 75
        }
      ],
      "linkedCodes": [
        { "name": "J02.0", "system": "ICD10", "sequence": 1 }
      ],
      "modifiers": [
        { "code": "<modifier>", "description": "<modifier description>" }
      ],
      "confidence": 0.62
    },
    {
      "sequence": 3,
      "system": "CPT",
      "name": "<laboratory test code>",
      "description": "<CPT description>",
      "unit": 1,
      "evidence": [
        {
          "text": "Rapid strep test positive.",
          "startOffset": 157,
          "endOffset": 183
        }
      ],
      "linkedCodes": [
        { "name": "J02.0", "system": "ICD10", "sequence": 1 }
      ],
      "confidence": 0.95
    },
    {
      "sequence": 4,
      "system": "CPT",
      "name": "<injection code>",
      "description": "<CPT description>",
      "unit": 1,
      "evidence": [
        {
          "text": "Administered penicillin IM injection in clinic today.",
          "startOffset": 226,
          "endOffset": 282
        }
      ],
      "linkedCodes": [
        { "name": "J02.0", "system": "ICD10", "sequence": 1 }
      ],
      "confidence": 0.88
    }
  ]
}
```

In this example, each CPT code links to the diagnosis that supports it. Only the E/M visit code has a modifier, so the other codes omit `modifiers`. The diagnosis code has an empty `linkedCodes` array. The E/M visit code has the lowest confidence, so a review interface would flag it first.

The following example shows how the codes for one encounter relate to each other and to the documentation:
+ Diagnosis code 1 cites passage 1, and diagnosis code 2 cites passage 2.
+ The E/M visit code cites passages 1 to 3 and links to both diagnoses.
+ The procedure code, with its modifier, cites passage 3 and links to diagnosis code 2.
+ Each code has its own confidence score. Together, the codes are the contents of the results file in Amazon S3.

![Example code set: codes cite evidence passages, and each CPT code links to the diagnoses that support it.](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/medical-coding-code-linkage.png)


The evidence references let a coder verify each suggestion against the source documentation rather than accepting it unseen. This is the same evidence-mapping approach used across Amazon Connect Health outputs.

## Rendering the results
<a name="mc-output-rendering"></a>

Medical coding returns structured data, not a finished user interface, so you control how suggestions appear in your coding workflow. A typical review experience:

1. Show each CPT code with the diagnoses in its `linkedCodes` array, the way the codes will appear on the claim.

1. Show the E/M level with the MDM evidence that supports it.

1. Use `startOffset` and `endOffset` to highlight each evidence passage in the source documentation, so coders can verify it in context.

1. Flag codes with a low `confidence` value for priority review.

1. Make each suggestion actionable. Render it as an element the coder can accept, reject, or modify, and record the decision.

For routing patterns that use confidence scores, see [Integrating medical coding into your workflows](mc-integration.md).

**Important**  
During the gated preview, a qualified coder should review every suggested code before claim submission. Suggested codes are not a substitute for professional coding judgment. In production, base your review policy on accuracy you measure on your own encounters, and keep audit sampling in place for any encounters that move forward with reduced review.