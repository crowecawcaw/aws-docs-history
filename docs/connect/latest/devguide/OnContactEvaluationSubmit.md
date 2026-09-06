

# OnContactEvaluationSubmit
<a name="OnContactEvaluationSubmit"></a>

## Agent Hierarchy
<a name="agent-hierarchy-contact"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - Agent hierarchy ARNs.
+ ComparisonValue - "$.ContactLens.ContactEvaluation.Agent.HierarchyGroup.ARN"
+ Negate - false

## Initiation Method
<a name="initiation-method-contact"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - A validated enum set of possible values. Possible values are as follows:
  + 'INBOUND'
  + 'OUTBOUND'
  + 'TRANSFER'
  + 'QUEUE\_TRANSFER'
  + 'CALLBACK'
  + 'API'
  + 'DISCONNECT'
+ ComparisonValue - "$.ContactLens.ContactEvaluation.InitiationMethod"
+ Negate - false

## DisconnectReason
<a name="disconnect-reason-contact"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - A validated enum set of possible values. Possible values are as follows:
  + 'TELECOM\_BUSY'
  + 'TELECOM\_NUMBER\_INVALID'
  + 'TELECOM\_POTENTIAL\_BLOCKING'
  + 'TELECOM\_UNANSWERED'
  + 'TELECOM\_TIMEOUT'
  + 'TELECOM\_ORIGINATOR\_CANCEL'
  + 'TELECOM\_PROBLEM'
  + 'CUSTOMER\_NEVER\_ARRIVED'
  + 'THIRD\_PARTY\_DISCONNECT'
  + 'CUSTOMER\_DISCONNECT'
  + 'AGENT\_DISCONNECT'
  + 'BARGED'
  + 'CONTACT\_FLOW\_DISCONNECT'
  + 'OTHER'
  + 'OUTBOUND\_DESTINATION\_ENDPOINT\_ERROR'
  + 'OUTBOUND\_RESOURCE\_ERROR'
  + 'OUTBOUND\_ATTEMPT\_FAILED'
  + 'EXPIRED'
  + 'AGENT\_NETWORK\_DISCONNECT'
  + 'CUSTOMER\_CONNECTION\_NOT\_ESTABLISHED'
  + 'API'
  + 'IDLE\_DISCONNECT'
  + 'SYSTEM\_ERROR'
  + 'AGENT\_COMPLETED'
  + 'TRANSFERRED'
  + 'DISCARDED'
+ ComparisonValue - "$.ContactLens.ContactEvaluation.DisconnectReason"
+ Negate - false

## Routing Profile
<a name="routing-profile-contact"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - Routing profile ARNs.
+ ComparisonValue - "$.ContactLens.ContactEvaluation.Agent.RoutingProfile"
+ Negate - false

## PotentialDisconnectIssue
<a name="potential-disconnect-issue-contact"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY" or "EQUALS"
+ Operands - A validated enum of possible values.
+ ComparisonValue - "$.ContactLens.ContactEvaluation.PotentialDisconnectIssue"
+ Negate - false

## Custom User-Defined Segment Attribute
<a name="custom-user-defined-segment-attribute-contact"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - A list of segment attribute values. The values must be a value in the pre-defined attribute resource.
+ ComparisonValue - "$.ContactLens.ContactEvaluation.SegmentAttributes.UserDefined.[KEY]"

  The KEY must be an instance pre-defined attribute resource.
+ Negate - false or true

## ContactEvaluation - Results available condition
<a name="ContactEvaluation-results"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is the evaluation form ID. 
+ ComparisonValue – "$.ContactLens.ContactEvaluation.Form.FormId"
+ Negate - false

## ContactEvaluation - Form score condition
<a name="ContactEvaluation-formscore"></a>

ContactEvaluation form score condition has a compound condition format where Operator is an AND condition and its operands consist of two conditions that represent the form and the form score. 

**Parameters that represent the form**: See [ContactEvaluation - Results available condition](https://docs.aws.amazon.com/connect/latest/APIReference/OnContactEvaluationSubmit.html#ContactEvaluation-results)

**Parameters that represent the form score:**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is the form score. 
+ ComparisonValue – "$.ContactLens.ContactEvaluation.Form.Score"
+ Negate - false

Following is an example.

```
{
    "Operator": "AND",
    "Operands": [
        {
            "Operator": "EQUALS",
            "Operands": ["11111111-1234-5678-9123-12345678012"],
            "ComparisonValue": "$.ContactLens.ContactEvaluation.Form.FormId",
            "Negate": false
        },
        {
            "Operator": "NumberLessOrEqualTo",
            "Operands": [50],
            "ComparisonValue": "$.ContactLens.ContactEvaluation.Form.Score",
            "Negate":false
        },
    ]
}
```

## ContactEvaluation - Section Score
<a name="ContactEvaluation-sectionscore"></a>

ContactEvaluation section score condition has a compound condition format where Operator is an AND condition and its operands consist of three conditions that represent the form, section, and section score respectively.

**Parameters that represent the form**: See [ContactEvaluation - Results available condition](https://docs.aws.amazon.com/connect/latest/APIReference/OnContactEvaluationSubmit.html#ContactEvaluation-results)

**Parameters that represent the section:**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is the section reference ID. 
+ ComparisonValue – "$.ContactLens.ContactEvaluation.Section.SectionRefId"
+ Negate - false

**Parameters that represent the section score:**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is the section score. 
+ ComparisonValue – "$.ContactLens.ContactEvaluation.Section.Score"
+ Negate - false

Following is an example.

```
{
    "Operator": "AND",
    "Operands": [
        {
            "Operator": "EQUALS",
            "Operands": ["11111111-1234-5678-9123-12345678012"],
            "ComparisonValue": "$.ContactLens.ContactEvaluation.Form.FormId",
            "Negate": false
        },
        {
            "Operator": "EQUALS",
            "Operands": ["s12345678"],
            "ComparisonValue": "$.ContactLens.ContactEvaluation.Section.SectionRefId",
            "Negate":false
        },
        {
            "Operator": "NumberLessOrEqualTo",
            "Operands": [50],
            "ComparisonValue": "$.ContactLens.ContactEvaluation.Section.Score",
            "Negate":false
        },
    ]
}
```

## ContactEvaluation - Question and Answer
<a name="ContactEvaluation-qa"></a>

ContactEvaluation question and answer condition has a compound condition format where Operator is an AND condition and its operands consist of three conditions that represent the form, question, and answer value respectively.

**Parameters that represent the form**: See [ContactEvaluation - Results available condition](https://docs.aws.amazon.com/connect/latest/APIReference/OnContactEvaluationSubmit.html#ContactEvaluation-results)

**Parameters that represent the question:**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is the question reference ID. 
+ ComparisonValue – "$.ContactLens.ContactEvaluation.Question.QuestionRefId"
+ Negate - false

**Parameters that represent a numeric answer:**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is the answer value. 
+ ComparisonValue – "$.ContactLens.ContactEvaluation.Question.Answer.Value"
+ Negate - false

Following is an example for a numeric question type.

```
{
    "Operator": "AND",
    "Operands": [
        {
            "Operator": "EQUALS",
            "Operands": ["11111111-1234-5678-9123-12345678012"],
            "ComparisonValue": "$.ContactLens.ContactEvaluation.Form.FormId",
            "Negate": false
        },
        {
            "Operator": "EQUALS",
            "Operands": ["s12345678"],
            "ComparisonValue": "$.ContactLens.ContactEvaluation.Question.QuestionRefId",
            "Negate":false
        },
        {
            "Operator": "NumberLessOrEqualTo",
            "Operands": [5],
            "ComparisonValue": "$.ContactLens.ContactEvaluation.Question.Answer.Value",
            "Negate":false
        }
    ]
}
```

**Parameters that represent a single select answer:**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is the answer reference ID.
+ ComparisonValue – "$.ContactLens.ContactEvaluation.Question.Answer.ValueRefId"
+ Negate - true/false. If set to true, it means *The answer is not equal to the answer reference ID specified in the Operands*.

Following is an example for single select question type.

```
{
    "Operator": "AND",
    "Operands": [
        {
            "Operator": "EQUALS",
            "Operands": ["11111111-1234-5678-9123-12345678012"],
            "ComparisonValue": "$.ContactLens.ContactEvaluation.Form.FormId",
            "Negate": false
        },
        {
            "Operator": "EQUALS",
            "Operands": ["q12345678"],
            "ComparisonValue": "$.ContactLens.ContactEvaluation.Question.QuestionRefId",
            "Negate":false
        },
        { // for single select question type
            "Operator": "EQUALS",
            "Operands": ["o12345678"],
            "ComparisonValue": "$.ContactLens.ContactEvaluation.Question.Answer.ValueRefId",
            "Negate":false
       },
    ]
}
```

## ContactEvaluation - agent condition
<a name="ContactEvaluation-ac"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of agent IDs. 
+ ComparisonValue – "$.ContactLens.ContactEvaluation.Agent.AgentId"
+ Negate - false

## ContactEvaluation - queue condition
<a name="ContactEvaluation-qc"></a>

**Parameters**
+ Operator – "EQUALS"
+ Operands – No value 
+ ComparisonValue – "$.ContactLens.ContactEvaluation.Queue.QueueId"
+ Negate - false

## ContactEvaluation - contact attributes condition
<a name="ContactEvaluation-cac"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is the contact attribute value.
+ ComparisonValue – "$.ContactLens.ContactEvaluation.ContactAttribute.{{YOUR\_ATTRIBUTE\_KEY}}"
+ Negate - true/false. If set to true, it means {{YOUR\_ATTRIBUTE\_KEY}} does not equal to the attribute value specified in the Operands.