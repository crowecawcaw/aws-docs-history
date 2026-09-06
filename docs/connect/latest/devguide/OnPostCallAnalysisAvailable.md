

# OnPostCallAnalysisAvailable
<a name="OnPostCallAnalysisAvailable"></a>

## Agent Hierarchy
<a name="agent-hierarchy"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - Agent hierarchy ARNs.
+ ComparisonValue - "$.ContactLens.PostCall.Agent.HierarchyGroup.ARN"
+ Negate - false

## NonTalkTimePct
<a name="non-talk-time-pct"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands - An array of numbers, array length can only be 1. Value is an integer between 0 and 100.
+ ComparisonValue - "$.ContactLens.PostCall.Agent.NonTalkTimePct"
+ Negate - false

## Customer Hold Duration Pct
<a name="customer-hold-duration-pct"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands - An array of number, array length can only be 1. Value is an integer between 0 and 100.
+ ComparisonValue - "$.ContactLens.PostCall.Agent.CustomerHoldDurationPct"
+ Negate - false

## Initiation Method
<a name="initiation-method"></a>

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
+ ComparisonValue - "$.ContactLens.PostCall.InitiationMethod"
+ Negate - false

## DisconnectReason
<a name="disconnect-reason"></a>

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
+ ComparisonValue - "$.ContactLens.PostCall.DisconnectReason"
+ Negate - false

## Absolute Talk Time
<a name="absolute-talk-time"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands - An integer.
+ ComparisonValue - "$.ContactLens.PostCall.TalkTime.TotalTimeSecs"
+ FilterClause - 

  ```
  { // required!!
          LogicOperator: 'AND', // has to be 'AND'
          Filters: [ // only allows one of the object
            {
              Type: 'ParticipantRole',
              Data: 'AGENT', // 'AGENT' or 'CUSTOMER'
            },
          ],
        },
  ```
+ Negate - false

## Maximum (Highest) Loudness Score
<a name="max-loudness-score"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands - an integer (decibels). 
+ ComparisonValue - "$.ContactLens.PostCall.Loudness.HighestLoudnessScore"
+ FilterClause - 

  ```
  {
          LogicOperator: 'AND', // has to be AND
          Filters: [ // only one object
            {
              Type: 'ParticipantRole',
              Data: 'CUSTOMER', // or 'AGENT'
            },
          ],
        },
  ```
+ Negate - false

## After Contact Work Duration
<a name="after-contact-work-duration"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands - A positive integer or zero.
+ ComparisonValue - "$.ContactLens.PostCall.Agent.AfterContactWorkDurationSecs"
+ Negate - false

## Routing profile
<a name="routing-profile"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - Routing profile ARNs:
+ ComparisonValue - "$.ContactLens.PostCall.Agent.RoutingProfile"
+ Negate - false

## PotentialDisconnectIssue
<a name="potential-disconnect-issue"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY" \| "EQUALS"
+ Operands - A validated enum of possible values.
+ ComparisonValue - "$.ContactLens.PostCall.PotentialDisconnectIssue"
+ Negate - false

## Custom User-Defined Segment Attribute
<a name="custom-user-defined-segment-attribute"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - A list of segment attribute values. The values must be a value in the pre-defined attribute resource.
+ ComparisonValue - "$.ContactLens.PostCall.SegmentAttributes.UserDefined.[KEY]"

  The KEY must be an instance pre-defined attribute resource.
+ Negate - false or true

## Connect AI Agent
<a name="connect-ai-agent"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - A list of strings. Strings are either a list of different UUIDs by themselves or a list of strings prefixed with the same UUID, with different possible version numbers uuid:2 and uuid:3. For example:
  + Different UUIDs by themselves: ['30682191-2312-4c27-9fc1-752e7a399d52', '2b81c7d5-85bc-459f-b605-0f5280a4301e']
  + Prefixed with the same UUID with different possible version numbers: ['30682191-2312-4c27-9fc1-752e7a399d52:1', '30682191-2312-4c27-9fc1-752e7a399d52:2']
+ ComparisonValue - "$.ContactLens.PostCall.AiAgent.IdWithVersion"
+ FilterClause - 

  ```
  [
            { // REQUIRED filter 
              Type: 'AiAgentUseCase',
              Data: {
                Value: 'SelfService', // or 'AgentAssistance'
              },
            },
            { // OPTIONAL filter
              Type: 'AiAgentEscalatedToHuman',
              Data: 'TRUE', // or 'FALSE'
            },
          ],
        },
  ```
+ Negate - false

## PostCall words or phrases - Exact match
<a name="postcall-exactmatch"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of strings
+ ComparisonValue – "$.ContactLens.PostCall.ExactMatch.Transcript"
+ FilterClause –

  ```
  {
      "LogicOperator": "AND", // Only "AND" is supported
      "Filters": [
          {
              "Type": "PostCallContactPeriodSeconds", // Optional filter type. If omitted, the rule applies to the full contact
              "Data": { // Either "First" or "Last" needs to be specified. 
                  "First": number
               }
          },
          {
              "Type": "ParticipantRole",
              "Data": "CUSTOMER" | "AGENT" | "ANY"
          }
      ]
  }
  ```
+ Negate - true or false. If set to true, it means *If transcript does not contain any of the words mentioned in the Operands*.

## PostCall words or phrases - Semantic match
<a name="postcall-semanticmatch"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of strings
+ ComparisonValue – "$.ContactLens.PostCall.SemanticMatch.Transcript"
+ FilterClause –

  ```
  {
      "LogicOperator": "AND", // Only "AND" is supported
      "Filters": [
          {
              "Type": "PostCallContactPeriodSeconds", // Optional filter type. If omitted, the rule applies to the full contact
              "Data": { // Either "First" or "Last" needs to be specified. 
                  "First": number
               }
          },
          {
              "Type": "ParticipantRole",
              "Data": "CUSTOMER" | "AGENT" | "ANY"
          }
      ]
  }
  ```
+ Negate - true or false. If set to true, it means *If transcript does not contain any of the words mentioned in the Operands*.

## PostCall natural language - Semantic match
<a name="postcall-semanticmatch-nl"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – A list with a single string
+ ComparisonValue – "$.ContactLens.PostCall.SemanticMatch.Phrase"
+ FilterClause –

  ```
  {
       Operator: "EQUALS",
       Operands: [
            "Customer called to change their address and agent proceeded with the address change during the call."
       ],
       ComparisonValue: "$.ContactLens.PostCall.SemanticMatch.Phrase",
       Negate: true or false
  },
  ```
+ Negate - true or false. If set to true, it means *If transcript does not contain any of the words mentioned in the Operands*.

## PostCall words or phrases - Pattern match
<a name="postcall-patternmatch"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of pattern match objects. See [PatternMatch Operands](https://docs.aws.amazon.com/connect/latest/adminguide/patternmatch-operands.html). 
+ ComparisonValue – "$.ContactLens.PostCall.PatternMatch.Transcript"
+ FilterClause –

  ```
  {
      "LogicOperator": "AND", // Only "AND" is supported
      "Filters": [
          {
              "Type": "PostCallContactPeriodSeconds", // Optional filter type. If omitted, the rule applies to the full contact
              "Data": { // Either "First" or "Last" needs to be specified. 
                  "First": number
               }
          },
          {
              "Type": "ParticipantRole",
              "Data": "CUSTOMER" | "AGENT" | "ANY"
          },
          {
              "Type": "PatternMatchLanguageFilter",
              "Data": "EN"|"ES"|"AR"|"DE"|"FR"|"HI"|"IT"|"PT"|"KO"|"JA"|"ZH"
          }
      ]
  }
  ```
+ Negate - true or false. If set to true, it means *If transcript does not contain any of the words mentioned in the Operands*.

## PostCall agent condition
<a name="postcall-agentcondition"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of agent IDs
+ ComparisonValue – "$.ContactLens.PostCall.Agent.AgentId"
+ Negate - false

## PostCall queue condition
<a name="postcall-queuecondition"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of queue IDs.
+ ComparisonValue – "$.ContactLens.PostCall.Queue.QueueId"
+ Negate - false

## PostCall no queue condition
<a name="postcall-noqueuecondition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – No value.
+ ComparisonValue – "$.ContactLens.PostCall.Queue.QueueId"
+ Negate - false

## PostCall contact attributes condition
<a name="postcall-attributescondition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is the contact attribute value. 
+ ComparisonValue – "$.ContactLens.PostCall.ContactAttribute.{{YOUR\_ATTRIBUTE\_KEY}}"
+ Negate - true/false. If set to true, it means *{{YOUR\_ATTRIBUTE\_KEY}} does not equal to the attribute value specified in the Operands. *.

## PostCall sentiment state condition
<a name="postcall-sentimentstatecondition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is one of "POSITIVE", "NEGATIVE", "NEUTRAL". 
+ ComparisonValue – "$.ContactLens.PostCall.Sentiment.State"
+ FilterClause – 

  ```
  {
      "LogicOperator": "AND", // Only "AND" is supported
      "Filters": [
          {
              "Type": "ParticipantRole",
              "Data": "CUSTOMER" | "AGENT" | "ANY"
          },
      ]
  }
  ```
+ Negate - false

## PostCall sentiment overall score condition
<a name="postcall-sentimentoverallscorecondition"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer between -5 and 5, inclusive. 
+ ComparisonValue – "$.ContactLens.PostCall.Sentiment.OverallScore"
+ FilterClause – 

  ```
  {
      "LogicOperator": "AND", // Only "AND" is supported
      "Filters": [
          {
              "Type": "ParticipantRole",
              "Data": "CUSTOMER" | "AGENT" | "ANY"
          },
      ]
  }
  ```
+ Negate - false

## PostCall sentiment score shift condition
<a name="postcall-sentimentscoreshiftcondition"></a>

PostCall sentiment score shift condition has a compound condition format where Operator is an AND condition and its operands consist of two conditions that represent beginning and end score respectively. 

**Parameters that represent the beginning score**
+ Operator - "NumberLessOrEqualTo \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer between -5 and 5, inclusive. 
+ ComparisonValue – "$.ContactLens.PostCall.Sentiment.Score.Beginning"
+ FilterClause – 

  ```
  {
      "LogicOperator": "AND", // Only "AND" is supported
      "Filters": [
          {
              "Type": "ParticipantRole",
              "Data": "CUSTOMER" | "AGENT" | "ANY"
          },
      ]
  }
  ```
+ Negate - false

**Parameters that represent the end score**
+ Operator - "NumberLessOrEqualTo \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer between -5 and 5, inclusive. 
+ ComparisonValue – "$.ContactLens.PostCall.Sentiment.Score.End"
+ FilterClause – 

  ```
  {
      "LogicOperator": "AND", // Only "AND" is supported
      "Filters": [
          {
              "Type": "ParticipantRole",
              "Data": "CUSTOMER" | "AGENT" | "ANY"
          },
      ]
  }
  ```
+ Negate - false

Following is an example:

```
{
        "Operator": "AND",
        "Operands": [
          {
            "Operator": "NumberGreaterOrEqualTo",
            "Operands": [
              2
            ],
            "ComparisonValue": "$.ContactLens.PostCall.Sentiment.Score.Beginning",
            "FilterClause": {
              "LogicOperator": "AND",
              "Filters": [
                {
                  "Type": "ParticipantRole",
                  "Data": "AGENT"
                }
              ]
            },
            "Negate": false
          },
          {
            "Operator": "NumberGreaterOrEqualTo",
            "Operands": [
              3
            ],
            "ComparisonValue": "$.ContactLens.PostCall.Sentiment.Score.End",
            "FilterClause": {
              "LogicOperator": "AND",
              "Filters": [
                {
                  "Type": "ParticipantRole",
                  "Data": "AGENT"
                }
              ]
            },
            "Negate": false
          }
        ]
      }
```

**Parameters for overall score**
+ Operator - "NumberLessOrEqualTo \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer between -5 and 5, inclusive. 
+ ComparisonValue – "$.ContactLens.PostCall.Sentiment.OverallScore"
+ FilterClause – 

  ```
  {
      "LogicOperator": "AND", // Only "AND" is supported
      "Filters": [
          {
              "Type": "ParticipantRole",
              "Data": "CUSTOMER" | "AGENT" | "ANY"
          },
      ]
  }
  ```
+ Negate - false

## PostCall total non-talk time condition
<a name="postcall-nontalktimecondition"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer with minimum value 1. 
+ ComparisonValue – "$.ContactLens.PostCall.NonTalkTime.TotalTimeSecs"
+ Negate - false

## PostCall longest non-talk time condition
<a name="postcall-longestnontalktimecondition"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer with minimum value 1. 
+ ComparisonValue – "$.ContactLens.PostCall.NonTalkTime.LongestTimeSecs"
+ Negate - false

## PostCall interruption condition
<a name="postcall-interruptioncondition"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer with minimum value 1. 
+ ComparisonValue – "$.ContactLens.PostCall.Interruptions.Instances"
+ Negate - false

## PostCall total hold time condition
<a name="postcall-holdtimecondition"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer with minimum value 1. 
+ ComparisonValue – "$.ContactLens.PostCall.Agent.CustomerHoldDurationSecs"
+ Negate - false

## PostCall longest hold time condition
<a name="postcall-longholdcondition"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer with minimum value 1. 
+ ComparisonValue – "$.ContactLens.PostCall.Agent.LongestHoldDurationSecs"
+ Negate - false

## PostCall number of holds condition
<a name="postcall-numberholdcondition"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer with minimum value 1. 
+ ComparisonValue – "$.ContactLens.PostCall.Agent.NumberOfHolds"
+ Negate - false

## PostCall agent interaction duration condition
<a name="postcall-agentinteractiondurationcondition"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer with minimum value 1. 
+ ComparisonValue – "$.ContactLens.PostCall.Agent.AgentInteractionDurationSecs"
+ Negate - false