

# Agent evaluation form output in Connect Customer
<a name="evaluationforms-example-output-file"></a>

This section shows the export output path for evaluations, provides an example of evaluation form scores, and describes the evaluation form metadata.

**Topics**
+ [Verify your S3 bucket](#verify-evaluation-s3bucket)
+ [Example output locations](#example-evaluationform-output-locations)
+ [Known issue](#release-note-evaluation-output)
+ [Example scores](#example-evaluation-output-file)
+ [Evaluation form metadata definitions](#evaluation-form-metadata)
+ [Sample exported evaluation](#exported-evaluation)

## Verify your S3 bucket
<a name="verify-evaluation-s3bucket"></a>

When you enable **Contact evaluations** in the Connect Customer console, you are prompted to create or choose an S3 bucket to store the evaluations. To verify the name of the bucket, navigate to your instance alias, choose **Data storage**, **Contact evaluations**, then **Edit**.

## Example output locations
<a name="example-evaluationform-output-locations"></a>

Following is the output file path for evaluation forms:
+ {{contact\_evaluations\_S3\_bucket}}/Evaluations/{{YYYY/MM/DD/hh:mm:ss.sTZD}}-{{evaluation\_id}}.json

For example:

`amazon-connect-s3/Evaluations/2022/04/14/05:04:20.869Z-11111111-2222-3333-4444-555555555555.json`

## Known issue: Two output files for the same evaluation
<a name="release-note-evaluation-output"></a>

Conversational analytics generates two output files for the same evaluation form.
+ One file is written to the new default S3 path. You can configure the path in the AWS console.
+ Another file, which will be deprecated, is written to a different, previous S3 path. You can disregard this file.

  The previous S3 path looks like the following:
  + {{s3\_bucket}}/Evaluations/contact\_{{contactId}}/evaluation\_{{evaluationId}}/YYYY-MM-DDThh:mm:ss.sTZD.json

## Example scores
<a name="example-evaluation-output-file"></a>

The following example shows a typical score.

```
{
  "schemaVersion": "3.5",
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
    "evaluationStartTimestamp": "2025-11-14T17:57:08.649Z",
    "evaluationSubmitTimestamp": "2025-11-14T17:59:29.052Z",
    "score": {
      "percentage": 100
    },
    "creator": "jane.doe@acme.com",
    "autoEvaluated": false,
    "resubmitted": false,
    "evaluationSource": "ASSISTED_BY_AUTOMATION",
    "evaluationType": "CONTACT_EVALUATION",
    "evaluationAcknowledgerComment": "The Acknowledgment comment",
    "evaluationAcknowledgedTimestamp": "2025-12-22T05:20:39.297Z",
    "evaluationAcknowledgedByUserName": "john",
    "evaluationAcknowledgedByUserId": "286bcec0-e722-4166-865f-84db80252218"
  },
  "sections": [
    {
      "sectionRefId": "s1a1b58d6",
      "sectionTitle": "The title of the section",
      "notes": "Section note",
      "score": {
        "percentage": 100
      }
    },
    {
      "sectionRefId": "s46661c49",
      "sectionTitle": "The title of the subsection",
      "parentSectionRefId": "s1a1b58d6",
      "score": {
        "percentage": 100
      }
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
        "metadata": {
          "notApplicable": true
        }
      },
      "score": {
        "notApplicable": true
      }
    },
    {
      "questionRefId": "q73bc5b9d",
      "sectionRefId": "s46661c49",
      "questionType": "SINGLESELECT",
      "questionText": "Did the agent introduce themselves?",
      "answer": {
        "values": [
          {
            "valueText": "Yes",
            "valueRefId": "o6999aa94",
            "selected": true
          },
          {
            "valueText": "No",
            "valueRefId": "o284e4d9e",
            "selected": false
          },
          {
            "valueText": "Maybe",
            "valueRefId": "o1b2f0a14",
            "selected": false
          }
        ],
        "notes": "Add more information here",
        "automation": {
          "status": "SYSTEM_ANSWER",
          "systemSuggestedValue": "Yes"
        },
        "metadata": {
          "notApplicable": false
        }
      },
      "score": {
        "percentage": 100
      }
    },
    {
      "questionRefId": "h89bc7a9t",
      "sectionRefId": "s46661c49",
      "questionType": "SINGLESELECT",
      "questionText": "Did the agent offer a promotion?",
      "answer": {
        "values": [
          {
            "valueText": "Yes",
            "valueRefId": "p7888bb85",
            "selected": false
          },
          {
            "valueText": "No",
            "valueRefId": "p395f5e8f",
            "selected": true
          },
          {
            "valueText": "Maybe",
            "valueRefId": "p2c3g1b25",
            "selected": false
          }
        ],
        "notes": "Add more information here",
        "assistedSuggestion": {
          "value": "No. A promotion was not offered by the agent."
        },
        "metadata": {
          "notApplicable": false
        }
      },
      "score": {
        "percentage": 100
      }
    },
    {
      "questionRefId": "qc2effc9d",
      "sectionRefId": "s46661c49",
      "questionType": "TEXT",
      "questionText": "Describe the outcome.",
      "answer": {
        "value": "Example answer text",
        "notes": "Add more information here",
        "metadata": {
          "notApplicable": false
        }
      },
      "score": {
        "percentage": 50
      }
    }
  ]
}
```

## Evaluation form metadata definitions
<a name="evaluation-form-metadata"></a>

The following list describes the fields in the evaluation form.

**evaluationId**  
A unique identifier for the contact evaluation  
*Type* – String  
*Length constraints* – Minimum length of 1. Maximum length of 500

**metadata**    
**contactId**  
The identifier of the contact in this instance of Amazon Connect.  
*Type* – String  
*Length constraints* – Minimum length of 1, maximum length of 256  
**accountId**  
The identifier of AWS account running the instance of Connect Customer.  
*Type* – String  
*Length constraints* – Constraints: 12 digits  
*Pattern* – `^\d{12}$`  
**instanceId**  
The identifier of the Amazon Connect instance. You can [find the instance ID](find-instance-arn.md) in the Amazon Resource Name (ARN) of the instance.  
*Length constraints* – Minimum length of 1, maximum length of 100  
**agentId**  
The identifier of the agent who performed the contact.  
*Type* – String  
*Length constraints* – Minimum length of 1, maximum length of 500  
**evaluationDefinitionTitle**  
The title of the evaluation form.  
*Type* – String  
*Length constraints* – Minimum length of 1, maximum length of 128  
**evaluator**  
Name of the user who last updated the evaluation.  
*Type* – String  
**evaluationDefinitionId**  
The unique identifier for the evaluation form.  
*Type* – String  
*Length constraints* – Minimum length of 1, maximum length of 500  
**evaluationDefinitionVersion**  
The version of the evaluation form.  
*Type* – Integer  
*Valid range* – Minimum value of 1  
**evaluationStartTimestamp**  
The evaluation's creation timestamp.  
*Type* – Timestamp  
*Example* – 2025-11-14T17:57:08.649Z  
**evaluationSubmitTimestamp**  
The evaluation's submission timestamp.  
*Type* – Timestamp  
*Example* – 2025-11-14T17:59:29.052Z  
**score**  
The evaluation's score.  
**creator**  
 The entity that created the evaluation the very first time (as opposed to "evaluator" which represents the entity that last submitted the evaluation). When the call is made from the Connect Customer admin website it contains the username. When the call comes from the API it contains the ARN of the caller.   
*Type* – String  
**autoEvaluated **  
 Indicates whether the evaluation was submitted using fully automated evaluations.  
*Type* – Boolean  
**resubmitted **  
 Indicates whether the evaluation has been re-submitted (edited and submitted again).  
*Type* – Boolean  
**evaluationSource **  
The type of evaluation answer source.  
*Type* – String  
Valid values:  
+ `ASSISTED_BY_AUTOMATION` - indicates that [question automation](create-evaluation-forms.md#step-automate) was used to answer some of the questions.
+ `MANUAL` - indicates that the evaluation was performed manually.
+ `AUTOMATED` - indicates that the evaluation was submitted using fully automated evaluations (see "autoEvaluated" field).  
**evaluationType**  
The type of evaluation.  
*Type* – String  
Valid values:  
+ `CONTACT_EVALUATION` - evaluation of a contact.  
**calibrationSessionId**  
The identifier of the calibration session associated with this evaluation.  
*Type* – String  
*Length constraints* – Minimum length of 1, maximum length of 500  
**evaluatedParticipantId**  
The identifier of the participant being evaluated.  
*Type* – String  
*Length constraints* – Minimum length of 1, maximum length of 256  
**evaluatedParticipantRole**  
The role of the participant being evaluated.  
*Type* – String  
Valid values:  
+ `AGENT` - the agent participant.
+ `CUSTOMER` - the customer participant.
+ `SYSTEM` - the system participant.  
**acknowledgerComment**  
Comment left by the user who acknowledged the evaluation.  
*Type* – String  
*Length constraints* – Minimum length of 0, maximum length of 3072  
**evaluationAcknowledgedByUserId**  
The identifier of the person who acknowledged the evaluation.  
*Type* – String  
*Length constraints* – Minimum length of 1, maximum length of 500  
**evaluationAcknowledgedByUserName**  
The name of the person who acknowledged the evaluation.  
*Type* – String  
**evaluationAcknowledgedTimestamp**  
The evaluation's acknowledgment timestamp.   
*Type* – Timestamp  
*Example* – 2025-12-24T15:45:56.662Z

**sections**  
Array of the sections of the evaluation.    
**sectionRefId**  
The identifier of the section. An identifier must be unique within the evaluation form.   
*Type* – String  
*Length constraints* – Minimum length of 1, maximum length of 40  
**parentSectionRefId**  
The identifier of the parent section.  
*Type* – String  
*Length constraints* – Minimum length of 1, maximum length of 40  
**sectionTitle**  
The title of the section.  
*Type* – String  
*Length constraints* – Constraints: Minimum length of 0, maximum length of 128  
**notes**  
The notes left for the section.  
*Type* – String  
*Length constraints* – Minimum length of 0, maximum length of 3072  
Notes have the following limits:  
+ Individual notes have a limit of 3072 characters. 
+ The combined notes in an evaluation have a limit of *N* x 1024 characters, where *N* is the number of questions in the evaluation.  
**score**  
The score for the section.    
**percentage**  
The score percentage for an item in a contact evaluation.  
*Type* – Double  
*Valid range* – Minimum value of 0, maximum value of 100  
**automaticFail**  
The flag that marks the item as automatic fail. If the item or a child item gets an automatic fail answer, this flag will be true.  
*Type* – Boolean  
**notApplicable**  
The flag that marks the item as automatic fail. If the item or a child item gets an automatic fail answer, this flag will be true.  
*Type* – Boolean

**questions**  
Array of the questions of the evaluation.    
**questionRefId**  
The identifier of the question. An identifier must be unique within the evaluation form.  
*Type* – String  
*Length constraints* – Minimum length of 1, maximum length of 40.  
**sectionRefId**  
The identifier of the parent section.   
*Type* – String  
*Length constraints* – Minimum length of 1, maximum length of 40  
**questionType**  
The type of the question.  
*Type* – String  
*Valid values* – `TEXT | SINGLESELECT | NUMERIC`  
**questionText**  
The title of the question.  
*Type* – String  
*Length constraints* – Minimum length of 0, maximum length of 350  
**answer**  
The answer for the question.    
**value**  
The string/numeric value for an answer in a contact evaluation.  
*Type* – String/Double  
*Length constraints* – String: Minimum length of 0, maximum length of 128  
**notes**  
The notes left for the section.  
*Type* – String  
*Length constraints* – Minimum length of 0. Maximum length of 3072  
Notes have two character limits. Individual notes have a limit of 3072 characters. The combined notes in an evaluation have a limit of N x 1024 characters, where N is the number of questions in the evaluation.  
**metadata**  
**notApplicable **  
Flag that marks the question as not applicable.  
*Type* – Boolean  
**assistedSuggestion**  
Answer suggested by the [generative AI](generative-ai-performance-evaluations.md).  
*Type* – String  
**automation**    
**status**  
The status of the automation answer.  
*Type* – String  
*Valid values* – `UNAVAILABLE | SYSTEM_ANSWER | OVERRIDDEN_ANSWER`  
**systemSuggestedValue**  
The string or numeric value for an automation answer in a contact evaluation.  
*Type* – String or Double  
*Length constraints* – String: Minimum length of 0, maximum length of 128  
**score**  
The [score](#score) for the question.  
+ automaticFail - The flag that marks the item as critical for the form and the full form will fail (marked with zero score) when the item fails. If the item or a child item gets an automatic fail answer, this flag will be true and the full form will also fail.

  *Type* – Boolean
+ notApplicable - The flag that marks the item as not applicable for scoring, it will be excluded from scoring calculations.

  *Type* – Boolean

## Sample exported evaluation
<a name="exported-evaluation"></a>

The following example shows a typical exported evaluation.

```
{
  "schemaVersion": "3.5",
  "evaluationId": "fb90de35-4507-479a-8b57-970290fd5c2c",
  "metadata": {
    "accountId": "874551140838",
    "instanceId": "8f753c94-9cd2-4f16-85eb-945f7f0d559a",
    "contactId": "badd4896-75f7-43b3-bee6-c617ed3d04cb",
    "agentId": "286bcec0-e722-4166-865f-84db80252218",
    "evaluationDefinitionTitle": "Legal Compliance Evaluation Form",
    "evaluator": "jane",
    "evaluationDefinitionId": "15d8fbf1-b4b2-4ace-869b-82714e2f6e3e",
    "evaluationDefinitionVersion": 2,
    "evaluationStartTimestamp": "2022-11-14T17:57:08.649Z",
    "evaluationSubmitTimestamp": "2022-11-14T17:59:29.052Z",
    "score": {
      "percentage": 85
    },
    "autoEvaluated": false,
    "creator": "john",
    "resubmitted": false,
    "evaluationSource": "ASSISTED_BY_AUTOMATION",
    "evaluationType": "CONTACT_EVALUATION",
    "calibrationSessionId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "evaluationAcknowledgedByUserId": "286bcec0-e722-4166-865f-84db80252218",
    "evaluationAcknowledgedByUserName": "mike",
    "evaluationAcknowledgedTimestamp": "2022-12-24T15:45:56.662Z",
    "evaluationAcknowledgerComment": "Manager walked through the evaluation during coaching",
    "evaluatedParticipantId": "participant-123",
    "evaluatedParticipantRole": "AGENT"
  },
  "sections": [
    {
      "sectionRefId": "s1a1b58d6",
      "sectionTitle": "Communication Skills",
      "notes": "Overall communication was professional",
      "score": {
        "percentage": 90
      }
    },
    {
      "sectionRefId": "s46661c49",
      "sectionTitle": "Greeting and Introduction",
      "parentSectionRefId": "s1a1b58d6",
      "notes": "Agent followed proper greeting protocol",
      "score": {
        "percentage": 100
      }
    }
  ],
  "questions": [
    {
      "questionRefId": "q570b206a",
      "sectionRefId": "s46661c49",
      "questionType": "NUMERIC",
      "questionText": "How many times did agent interrupt the customer",
      "answer": {
        "value": "2",
        "notes": "Interruptions were minimal and appropriate",
        "metadata": {
          "notApplicable": false,
          "automation": {
            "status": "OVERRIDDEN_ANSWER",
            "systemSuggestedValue": "3"
          }
        }
      },
      "score": {
        "percentage": 80
      }
    },
    {
      "questionRefId": "q73bc5b9d",
      "sectionRefId": "s46661c49",
      "questionType": "SINGLESELECT",
      "questionText": "Did the agent introduce themselves?",
      "answer": {
        "values": [
          {
            "valueText": "Yes",
            "valueRefId": "o6999aa94",
            "selected": true
          },
          {
            "valueText": "No",
            "valueRefId": "o284e4d9e",
            "selected": false
          },
          {
            "valueText": "N/A",
            "valueRefId": "system_default_null_value",
            "selected": false
          }
        ],
        "notes": "Agent provided clear introduction with name and department",
        "metadata": {
          "notApplicable": false,
          "assistedSuggestion": {
            "value": "The agent introduced themselves at the beginning of the call."
          }
        }
      },
      "score": {
        "percentage": 100
      }
    },
    {
      "questionRefId": "h89bc7a9t",
      "sectionRefId": "s46661c49",
      "questionType": "SINGLESELECT",
      "questionText": "Did the agent ask for consent to perform a credit check",
      "answer": {
        "values": [
          {
            "valueText": "Yes",
            "valueRefId": "o6999aa94",
            "selected": false
          },
          {
            "valueText": "No",
            "valueRefId": "o284e4d9e",
            "selected": true
          },
          {
            "valueText": "N/A",
            "valueRefId": "system_default_null_value",
            "selected": false
          }
        ],
        "notes": "Agent failed to obtain consent before credit check",
        "metadata": {
          "notApplicable": false
        }
      },
      "score": {
        "percentage": 0,
        "automaticFail": true
      }
    },
    {
      "questionRefId": "qc2effc9d",
      "sectionRefId": "s46661c49",
      "questionType": "MULTISELECT",
      "questionText": "What topics were discussed during the call",
      "answer": {
        "values": [
          {
            "valueText": "Account balance",
            "valueRefId": "topic_balance",
            "selected": true
          },
          {
            "valueText": "Payment options",
            "valueRefId": "topic_payment",
            "selected": true
          },
          {
            "valueText": "Account closure",
            "valueRefId": "topic_closure",
            "selected": false
          }
        ],
        "notes": "Customer inquired about balance and payment plans",
        "metadata": {
          "notApplicable": false
        }
      },
      "score": {
        "notApplicable": true
      }
    },
    {
      "questionRefId": "q8a9b0c1d",
      "sectionRefId": "s46661c49",
      "questionType": "TEXT",
      "questionText": "What was your general impression about the customer's satisfaction",
      "answer": {
        "value": "The customer seemed satisfied with the resolution and thanked the agent",
        "notes": "Positive customer sentiment throughout the call",
        "metadata": {
          "notApplicable": false
        }
      },
      "score": {
        "notApplicable": true
      }
    },
    {
      "questionRefId": "q2b3c4d5e",
      "sectionRefId": "s46661c49",
      "questionType": "DATETIME",
      "questionText": "What time was the follow-up scheduled",
      "answer": {
        "value": "2024-04-16T14:30:00+01:00",
        "notes": "Follow-up appointment confirmed with customer",
        "metadata": {
          "notApplicable": false
        }
      },
      "score": {
        "notApplicable": true
      }
    }
  ]
}
```