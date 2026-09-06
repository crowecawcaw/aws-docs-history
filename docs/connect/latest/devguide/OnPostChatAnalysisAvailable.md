

# OnPostChatAnalysisAvailable
<a name="OnPostChatAnalysisAvailable"></a>

## Agent Hierarchy
<a name="agent-hierarchy-chat"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - Agent hierarchy ARNs.
+ ComparisonValue - "$.ContactLens.PostChat.Agent.HierarchyGroup.ARN"
+ Negate - false

## Initiation Method
<a name="initiation-method-chat"></a>

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
+ ComparisonValue - "$.ContactLens.PostChat.InitiationMethod"
+ Negate - false

## DisconnectReason
<a name="disconnect-reason-chat"></a>

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
+ ComparisonValue - "$.ContactLens.PostChat.DisconnectReason"
+ Negate - false

## After Contact Work Duration
<a name="after-contact-work-duration-chat"></a>

**Parameters**
+ Operator - "NumberGreaterOrEqualTo" \| "NumberLessOrEqualTo"
+ Operands - A positive integer or zero.
+ ComparisonValue - "$.ContactLens.PostChat.Agent.AfterContactWorkDurationSecs"
+ Negate - false

## Routing Profile
<a name="routing-profile-chat"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - Routing profile ARNs.
+ ComparisonValue - "$.ContactLens.PostChat.Agent.RoutingProfile"
+ Negate - false

## PotentialDisconnectIssue
<a name="potential-disconnect-issue-chat"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY" where it is matched by a possible operand or "EQUALS" where the operand has to have no value.
+ Operands - A validated enum of possible values or no value.
+ ComparisonValue - "$.ContactLens.PostChat.PotentialDisconnectIssue"
+ Negate - false

## Custom User-Defined Segment Attribute
<a name="custom-user-defined-segment-attribute-chat"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - A list of segment attribute values. The values must be a value in the pre-defined attribute resource.
+ ComparisonValue - "$.ContactLens.PostChat.SegmentAttributes.UserDefined.[KEY]"

  The KEY must be an instance pre-defined attribute resource.
+ Negate - false

## Connect AI Agent
<a name="connect-ai-agent-chat"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - A list of strings. Strings are either a list of different UUIDs by themselves or a list of strings prefixed with the same UUID, with different possible version numbers uuid:2 and uuid:3. For example:
  + Different UUIDs by themselves: ['30682191-2312-4c27-9fc1-752e7a399d52', '2b81c7d5-85bc-459f-b605-0f5280a4301e']
  + Prefixed with the same UUID with different possible version numbers: ['30682191-2312-4c27-9fc1-752e7a399d52:1', '30682191-2312-4c27-9fc1-752e7a399d52:2']
+ ComparisonValue - "$.ContactLens.PostChat.AiAgent.IdWithVersion"
+ FilterClause - 

  ```
  {
          LogicOperator: 'AND', // has to be 'AND'
          Filters: [
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

## PostChat words or phrases - Exact match
<a name="postchat-exactmatch"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of strings
+ ComparisonValue – "$.ContactLens.PostChat.ExactMatch.Transcript"
+ FilterClause –

  ```
  {
      "LogicOperator": "AND", // Only "AND" is supported
      "Filters": [
          {
              "Type": "PostChatContactPeriodSeconds", // Optional filter type. If omitted, the rule applies to the full contact
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

## PostChat words or phrases - Semantic match
<a name="postchat-semanticmatch"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of strings
+ ComparisonValue – "$.ContactLens.PostChat.SemanticMatch.Transcript"
+ FilterClause –

  ```
  {
      "LogicOperator": "AND", // Only "AND" is supported
      "Filters": [
          {
              "Type": "PostChatContactPeriodSeconds", // Optional filter type. If omitted, the rule applies to the full contact
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

## PostChat natural language - Semantic match
<a name="postchat-semanticmatch-nl"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – A list with a single string
+ ComparisonValue – "$.ContactLens.PostChat.SemanticMatch.Phrase"
+ FilterClause –

  ```
  {
       Operator: "EQUALS",
       Operands: [
            "Customer called to change their address and agent proceeded with the address change during the call."
       ],
       ComparisonValue: "$.ContactLens.PostChat.SemanticMatch.Phrase",
       Negate: true or false
  },
  ```
+ Negate - true or false. If set to true, it means *If transcript does not contain any of the words mentioned in the Operands*.

## PostChat words or phrases - Pattern match
<a name="postchat-patternmatch"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of pattern match objects. See [PatternMatch Operands](https://docs.aws.amazon.com/connect/latest/adminguide/patternmatch-operands.html).
+ ComparisonValue – "$.ContactLens.PostChat.PatternMatch.Transcript"
+ FilterClause –

  ```
  {
      "LogicOperator": "AND", // Only "AND" is supported
      "Filters": [
          {
              "Type": "PostChatContactPeriodSeconds", // Optional filter type. If omitted, the rule applies to the full contact
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
+ Negate - true or false. If set to true, it means *If the transcript does not contain any of the words mentioned in the Operands*.

## PostChat agent condition
<a name="postchat-agentcondition"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of agent IDs 
+ ComparisonValue – "$.ContactLens.PostChat.Agent.AgentId"
+ Negate - false

## PostChat queue condition
<a name="postchat-queuecondition"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of queue IDs.
+ ComparisonValue – "$.ContactLens.PostChat.Queue.QueueId"
+ Negate - false

## PostChat no queue condition
<a name="postchat-noqueuecondition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – No value.
+ ComparisonValue – "$.ContactLens.PostChat.Queue.QueueId"
+ Negate - false

## PostChat contact attributes condition
<a name="postchat-attributescondition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is the contact attribute value. 
+ ComparisonValue – "$.ContactLens.PostChat.ContactAttribute.{{YOUR\_ATTRIBUTE\_KEY}}"
+ Negate - true/false. If set to true, it means *{{YOUR\_ATTRIBUTE\_KEY}} does not equal to the attribute value specified in the Operands *.

## PostChat sentiment state condition
<a name="postchat-sentimentstatecondition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is one of "POSITIVE", "NEGATIVE", "NEUTRAL". 
+ ComparisonValue – "$.ContactLens.PostChat.Sentiment.State"
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

## PostChat sentiment overall score condition
<a name="postchat-sentimentoverallscorecondition"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer between -5 and 5, inclusive. 
+ ComparisonValue – "$.ContactLens.PostChat.Sentiment.OverallScore"
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

## Postchat sentiment score shift condition
<a name="postchat-sentimentscoreshiftcondition"></a>

PostChat sentiment score shift condition has a compound condition format where Operator is an AND condition and its operands consist of two conditions that represent beginning and end score respectively. 

**Parameters that represent the beginning score**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer between -5 and 5, inclusive. 
+ ComparisonValue – "$.ContactLens.PostChat.Sentiment.Score.Beginning"
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
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer between -5 and 5, inclusive. 
+ ComparisonValue – "$.ContactLens.PostChat.Sentiment.Score.End"
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
            "ComparisonValue": "$.ContactLens.PostChat.Sentiment.Score.Beginning",
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
            "ComparisonValue": "$.ContactLens.PostChat.Sentiment.Score.End",
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

## PostChat agent first response time condition
<a name="postchat-firstresponsecondition"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer with minimum value 1. 
+ ComparisonValue – "$.ContactLens.PostChat.ResponseTime.Agent.FirstResponseTimeSecs"
+ Negate - false

## PostChat agent average response time condition
<a name="postchat-agentavgresponsecondition"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer with minimum value 1. 
+ ComparisonValue – "$.ContactLens.PostChat.ResponseTime.Agent.AverageTimeSecs"
+ Negate - false

## PostChat agent longest response time condition
<a name="postchat-agentlongestresponsecondition"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer with minimum value 1. 
+ ComparisonValue – "$.ContactLens.PostChat.ResponseTime.Agent.LongestTimeSecs"
+ Negate - false

## PostChat agent interaction duration condition
<a name="postchat-agentinteractiondurationcondition"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer with minimum value 1. 
+ ComparisonValue – "$.ContactLens.PostChat.Agent.AgentInteractionDurationSecs"
+ Negate - false