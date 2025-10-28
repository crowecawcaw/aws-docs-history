# Agent evaluation form output in

Amazon Connect

This section shows the export output path for evaluations, provides an example of
evaluation form scores, and describes the evaluation form metadata.

###### Contents

- [Verify your S3
  bucket](#verify-evaluation-s3bucket "#verify-evaluation-s3bucket")
- [Example output
  locations](#example-evaluationform-output-locations "#example-evaluationform-output-locations")
- [Known
  issue](#release-note-evaluation-output "#release-note-evaluation-output")
- [Example
  scores](#example-evaluation-output-file "#example-evaluation-output-file")
- [Evaluation form metadata
  definitions](#evaluation-form-metadata "#evaluation-form-metadata")
- [Sample exported evaluation](#exported-evaluation "#exported-evaluation")

## Verify your S3 bucket

When you enable **Contact evaluations** in the Amazon Connect
console, you are prompted to create or choose an S3 bucket to store the evaluations.
To verify the name of the bucket, go to your instance alias, choose **Data
storage**, **Contact evaluations**, then
**Edit**.

## Example output

locations

Following is the output file path for evaluation forms:

- `contact_evaluations_S3_bucket`/Evaluations/`YYYY/MM/DD/hh:mm:ss.sTZD`-`evaluation_id`.json

For example:

`amazon-connect-s3/Evaluations/2022/04/14/05:04:20.869Z-11111111-2222-3333-4444-555555555555.json`

## Known issue: Two output files for

the same evaluation

Contact Lens generates two output files for the same evaluation
form.

- One file is written to the new default S3 path. You can configure the path
  in the AWS console.
- Another file, which will be deprecated, is written to a different,
  previous S3 path. You can disregard this file.

The previous S3 path looks like the following:

    + `s3_bucket`/Evaluations/contact\_`contactId`/evaluation\_`evaluationId`/YYYY-MM-DDThh:mm:ss.sTZD.json

## Example scores

The following example shows a typical score.

```
 {
"schemaVersion": "3.1",
"evaluationId": "fb90de35-4507-479a-8b57-970290fd5c2c",
 "metadata": {
    "contactId": "badd4896-75f7-43b3-bee6-c617ed3d04cb",
    "accountId": "874551140838",
    "instanceId": "8f753c94-9cd2-4f16-85eb-945f7f0d559a",
    "agentId": "286bcec0-e722-4166-865f-84db80252218",
    "evaluationDefinitionTitle": "`Compliance Evaluation Form`",
    "evaluator": "jane",
    "evaluationDefinitionId": "15d8fbf1-b4b2-4ace-869b-82714e2f6e3e",
    "evaluationDefinitionVersion": 2,
    "evaluationStartTimestamp": "2022-11-14T17:57:08.649Z",
    "evaluationSubmitTimestamp": "2022-11-14T17:59:29.052Z",
    "score": { "percentage": 100 },
    "creator": "jane.doe@acme.com",
    "autoEvaluated": false,
    "resubmitted": false,
    "evaluationSource": "ASSISTED_BY_AUTOMATION",
    "acknowledgerComment": "The Acknowledgment comment",
         "acknowledgedTimestamp": "2022-12-22T05:20:39.297Z",
         "acknowledgedByUserName": "john",
         "acknowledgedByUserId": "286bcec0-e722-4166-865f-84db80252218"
  },
"sections": [
    {
      "sectionRefId": "s1a1b58d6",
      "sectionTitle": "`The title of the section`",
      "notes": "Section note",
      "score": { "percentage": 100 }
    },
    {
      "sectionRefId": "s46661c49",
      "sectionTitle": "`The title of the subsection`",
      "parentSectionRefId": "s1a1b58d6",
      "score": { "percentage": 100 }
    }
  ],
"questions": [
    {
      "questionRefId": "q570b206a",
      "sectionRefId": "s46661c49",
      "questionType": "NUMERIC",
      "questionText": "`How do you rate the contact between 1 and 10?`",
      "answer": {
        "value": "",
        "notes": "`Add more information here`",
        "metadata": { "notApplicable": true }
      },
      "score": { "notApplicable": true }
    },
    {
      "questionRefId": "q73bc5b9d",
      "sectionRefId": "s46661c49",
      "questionType": "SINGLESELECT",
      "questionText": "`Did the agent introduce themselves?`",
      "answer": {
        "values": [
          { "valueText": "`Yes`", "valueRefId": "o6999aa94", "selected": true },
          { "valueText": "`No`", "valueRefId": "o284e4d9e", "selected": false },
          { "valueText": "`Maybe`", "valueRefId": "o1b2f0a14", "selected": false }
        ],
        "notes": "`Add more information here`",
        "automation": {
            "status": "SYSTEM_ANSWER",
            "systemSuggestedValue": "Yes"
        },
        "metadata": { "notApplicable": false }
      },
      "score": { "percentage": 100 }
    },
    {
      "questionRefId": "h89bc7a9t",
      "sectionRefId": "s46661c49",
      "questionType": "SINGLESELECT",
      "questionText": "`Did the agent offer a promotion?`",
      "answer": {
        "values": [
          { "valueText": "`Yes`", "valueRefId": "o6999aa94", "selected": false },
          { "valueText": "`No`", "valueRefId": "o284e4d9e", "selected": true },
          { "valueText": "`Maybe`", "valueRefId": "o1b2f0a14", "selected": false }
        ],
        "notes": "`Add more information here`",
        "assistedSuggestion": {
            value: "`No. A promotion was not offered by the agent.`"
        },
        "metadata": { "notApplicable": false }
      },
      "score": { "percentage": 100 }
    },
    {
      "questionRefId": "qc2effc9d",
      "sectionRefId": "s46661c49",
      "questionType": "TEXT",
      "questionText": "`Describe the outcome.`",
      "answer": {
        "value": "`Example answer text`",
        "notes": "`Add more information here`",
        "metadata": { "notApplicable": false }
      },
      "score": { "notApplicable": true }
    }
  ]
}
```

## Evaluation form metadata

definitions

The following list describes the fields in the evaluation form.

**evaluationId**

A unique identifier for the contact evaluation

_Type_ – String

_Length constraints_ – Minimum length of 1.
Maximum length of 500

**metadata**

**contactId**

The identifier of the contact in this instance of Amazon
Connect.

_Type_ – String

_Length constraints_ – Minimum
length of 1, maximum length of 256

**accountId**

The identifier of AWS account running the instance of
Amazon Connect.

_Type_ – String

_Length constraints_ –
Constraints: 12 digits

_Pattern_ –
`^\d{12}$`

**instanceId**

The identifier of the Amazon Connect instance. You can
[find the instance
ID](find-instance-arn.md "find-instance-arn.md") in the Amazon Resource Name (ARN) of the
instance.

_Length constraints_ – Minimum
length of 1, maximum length of 100

**agentId**

The identifier of the agent who performed the
contact.

_Type_ – String

_Length constraints_ – Minimum
length of 1, maximum length of 500

**evaluationDefinitionTitle**

The title of the evaluation form.

_Type_ – String

_Length constraints_ – Minimum
length of 1, maximum length of 128

**evaluator**

Name of the user who last updated the evaluation.

_Type_ – String

**evaluationDefinitionId**

The unique identifier for the evaluation form.

_Type_ – String

_Length contraints_ – Minimum
length of 1, maximum length of 500

**evaluationDefinitionVersion**

The version of the evaluation form.

_Type_ – Integer

_Valid range_ – Minimum value of
1

**evaluationStartTimestamp**

The evaluation's creation timestamp.

_Type_ – Timestamp

**score**

The evaluation's score.

**creator**

The entity that created the evaluation the very first
time (as opposed to "evaluator" which represents the entity
that last submitted the evaluation). When the call is made
from the Amazon Connect admin website it contains the username. Wen the call comes
from the API it contains the ARN of the caller.

_Type_ – String

**autoEvaluated**

Indicates whether the evaluation was submitted using
fully automated evaluations.

_Type_ – Boolean

**resubmitted**

Indicates whether the evaluation has been re-submitted
(edited and submitted again).

_Type_ – Boolean

**evaluationSource**

The type of evaluation answer source.

_Type_ – String

Valid values:

- `ASSISTED_BY_AUTOMATION` - indicates
  that [question
  automation](create-evaluation-forms.md#step-automate "create-evaluation-forms.md#step-automate") was used to answer some of the
  questions.
- `MANUAL` - indicates that the
  evaluation was performed manually.
- `AUTOMATED` - indicates that the
  evaluation was submitted using fully automated
  evaluations (see "autoEvaluated" field).

**acknowledgerComment**

Comment left by the user who acknowledged the
evaluation.

_Type_ – String

_Length constraints_ – Minimum
length of 0, maximum length of 3072

**evaluationAcknowledgedByUserId**

The identifier of the person who acknowledged the
evaluation.

_Type_ – String

_Length constraints_ – Minimum
length of 1, maximum length of 500

**evaluationAcknowledgedByUserName**

The name of the person who acknowledged the
evaluation.

_Type_ – String

**evaluationAcknowledgedTimestamp**

The evaluation's acknowledgment timestamp.

_Type_ – Timestamp

**sections**

Array of the sections of the evaluation.

**sectionRefId**

The identifier of the section. An identifier must be
unique within the evaluation form.

_Type_ – String

_Length constraints_ – Minimum
length of 1, maximum length of 40

**parentSectionRefId**

The identifier of the parent section.

_Type_ – String

_Length constraints_ – Minimum
length of 1, maximum length of 40

**sectionTitle**

The title of the section.

_Type_ – String

_Length constraints_ –
Constraints: Minimum length of 0, maximum length of
128

**notes**

The notes left for the section.

_Type_ – String

_Length constraints_ – Minimum
length of 0, maximum length of 3072

###### Note

Notes have the following limits:

- Individual notes have a limit of 3072
  characters.
- The combined notes in an evaluation have a
  limit of _N_ x
  1024 characters, where _N_ is the number of questions in the
  evaluation.

**score**

The score for the section.

**percentage**

The score percentage for an item in a contact
evaluation.

_Type_ –
Double

_Valid range_ –
Minimum value of 0, maximum value of 100

**automaticFail**

The flag that marks the item as automatic
fail. If the item or a child item gets an
automatic fail answer, this flag will be
true.

_Type_ –
Boolean

**notApplicable**

The flag that marks the item as automatic
fail. If the item or a child item gets an
automatic fail answer, this flag will be
true.

_Type_ –
Boolean

**questions**

Array of the questions of the evaluation.

**questionRefId**

The identifier of the question. An identifier must be
unique within the evaluation form.

_Type_ – String

_Length constraints_ – Minimum
length of 1, maximum length of 40.

**sectionRefId**

The identifier of the parent section.

_Type_ – String

_Length constraints_ – Minimum
length of 1, maximum length of 40

**questionType**

The type of the question.

_Type_ – StrThe combined notes
in an evaluation have a limit of _N_ x 1024 characters, where _N_ is the number of questions in
the evaluation.ing

_Valid values_ – `TEXT |
 SINGLESELECT | NUMERIC`

**questionText**

The title of the question.

_Type_ – String

_Length constraints_ – Minimum
length of 0, maximum length of 350

**answer**

The answer for the question.

**value**

The string/numeric value for an answer in a
contact evaluation.

_Type_ –
String/Double

_Length constraints_
– String: Minimum length of 0, maximum
length of 128

**notes**

The notes left for the section.

_Type_ –
String

_Length constraints_
– Minimum length of 0. Maximum length of
3072

###### Note

Notes have two character limits. Individual
notes have a limit of 3072 characters. The
combined notes in an evaluation have a limit of N
x 1024 characters, where N is the number of
questions in the evaluation.

**metadata**

**notApplicable**

Flag that marks the question as not
applicable.

_Type_ –
Boolean

**assistedSuggestion**

Answer suggested by the [generative AI](generative-ai-performance-evaluations.md "generative-ai-performance-evaluations.md").

_Type_ –
String

**automation**

**status**

The status of the automation answer.

_Type_ –
String

_Valid values_ –
`UNAVAILABLE | SYSTEM_ANSWER |
 OVERRIDDEN_ANSWER`

**systemSuggestedValue**

The string or numeric value for an
automation answer in a contact evaluation.

_Type_ – String or
Double

_Length constraints_
– String: Minimum length of 0, maximum
length of 128

**score**

The [score](#score "#score") for
the question.

- automaticFail - The flag that marks the item as
  critical for the form and the full form will fail
  (marked with zero score) when the item fails. If the
  item or a child item gets an automatic fail answer,
  this flag will be true and the full form will also
  fail.

_Type_ – Boolean

- notApplicable - The flag that mark the item as not
  applicable for scoring, it will be excluded from
  scoring calculations.

_Type_ – Boolean

## Sample exported evaluation

The following example shows a typical exported evaluation.

```
{
"schemaVersion": "3.1",
"evaluationId": "fb90de35-4507-479a-8b57-970290fd5c2c",
 "metadata": {
    "contactId": "badd4896-75f7-43b3-bee6-c617ed3d04cb",
    "accountId": "874551140838",
    "instanceId": "8f753c94-9cd2-4f16-85eb-945f7f0d559a",
    "agentId": "286bcec0-e722-4166-865f-84db80252218",
    "evaluationDefinitionTitle": "Compliance Evaluation Form",
    "evaluator": "jane",
    "evaluationDefinitionId": "15d8fbf1-b4b2-4ace-869b-82714e2f6e3e",
    "evaluationDefinitionVersion": 2,
    "evaluationStartTimestamp": "2022-11-14T17:57:08.649Z",
    "evaluationSubmitTimestamp": "2022-11-14T17:59:29.052Z",
    "score": { "percentage": 100 },
    "creator": "john",
    "autoEvaluated": false,
    "resubmitted": false,
    "evaluationSource": "ASSISTED_BY_AUTOMATION",
     "acknowledgerComment": "Manager walked through the evaluation during coaching",
    "evaluationAcknowledgedByUserId": "286bcec0-e722-4166-865f-84db80252218",
     "evaluationAcknowledgedByUserName": "mike",
     "evaluationAcknowledgedTimestamp": "2022-12-24T15:45:56.662Z"
  },
  },
"sections": [
    {
      "sectionRefId": "s1a1b58d6",
      "sectionTitle": "The title of the section",
      "notes": "Section note",
      "score": { "percentage": 100 }
    },
    {
      "sectionRefId": "s46661c49",
      "sectionTitle": "The title of the subsection",
      "parentSectionRefId": "s1a1b58d6",
      "score": { "percentage": 100 }
    }
  ],
"questions": [
    {
      "questionRefId": "q570b206a",
      "sectionRefId": "s46661c49",
      "questionType": "NUMERIC",
      "questionText": "How do you rate the contact between 1 and 10?",
      "answer": {
        "value": "",
        "notes": "Add more information here",
        "metadata": { "notApplicable": true }
      },
      "score": { "notApplicable": true }
    },
    {
      "questionRefId": "q73bc5b9d",
      "sectionRefId": "s46661c49",
      "questionType": "SINGLESELECT",
      "questionText": "Did the agent introduce themselves?",
      "answer": {
        "values": [
          { "valueText": "Yes", "valueRefId": "o6999aa94", "selected": true },
          { "valueText": "No", "valueRefId": "o284e4d9e", "selected": false },
          { "valueText": "Maybe", "valueRefId": "o1b2f0a14", "selected": false }
        ],
        "notes": "Add more information here",
        "automation": {
            "status": "SYSTEM_ANSWER",
            "systemSuggestedValue": "Yes"
        },
        "metadata": { "notApplicable": false }
      },
      "score": { "percentage": 100 }
    },
    {
      "questionRefId": "h89bc7a9t",
      "sectionRefId": "s46661c49",
      "questionType": "SINGLESELECT",
      "questionText": "Did the agent offer a promotion?",
      "answer": {
        "values": [
          { "valueText": "Yes", "valueRefId": "o6999aa94", "selected": false },
          { "valueText": "No", "valueRefId": "o284e4d9e", "selected": true },
          { "valueText": "Maybe", "valueRefId": "o1b2f0a14", "selected": false }
        ],
        "notes": "Add more information here",
        "assistedSuggestion": {
            value: "No. A promotion was not offered by the agent."
        },
        "metadata": { "notApplicable": false }
      },
      "score": { "percentage": 100 }
    },
    {
      "questionRefId": "qc2effc9d",
      "sectionRefId": "s46661c49",
      "questionType": "TEXT",
      "questionText": "Describe the outcome.",
      "answer": {
        "value": "Example answer text",
        "notes": "Add more information here",
        "metadata": { "notApplicable": false }
      },
      "score": { "notApplicable": true }
    }
  ]
}
```
