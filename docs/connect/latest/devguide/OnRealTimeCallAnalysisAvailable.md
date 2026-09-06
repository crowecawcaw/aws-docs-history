

# OnRealTimeCallAnalysisAvailable
<a name="OnRealTimeCallAnalysisAvailable"></a>

## RealTimeCall words or phrases - Exact match
<a name="realtime-exactmatch"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of strings
+ ComparisonValue – "$.ContactLens.RealTimeCall.ExactMatch.Transcript"
+ FilterClause –

  ```
  {
      "LogicOperator": "AND", // Only "AND" is supported
      "Filters": [
          {
              "Type": "ParticipantRole",
              "Data": "CUSTOMER" | "AGENT" | "ANY"
          }
      ]
  }
  ```
+ Negate - false.

## RealTimeCall words or phrases - Pattern match
<a name="realtime-patternmatch"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of pattern match objects. See [PatternMatch Operands](https://docs.aws.amazon.com/connect/latest/adminguide/patternmatch-operands.html). 
+ ComparisonValue – "$.ContactLens.RealTimeCall.PatternMatch.Transcript"
+ FilterClause –

  ```
  {
      "LogicOperator": "AND", // Only "AND" is supported
      "Filters": [
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
+ Negate - false

## RealTimeCall agent condition
<a name="realtime-agentcondition"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of agent IDs 
+ ComparisonValue – "$.ContactLens.RealTimeCall.Agent.AgentId"
+ Negate - false

## RealTimeCall queue condition
<a name="realtime-queuecondition"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of queue IDs 
+ ComparisonValue – "$.ContactLens.RealTimeCall.Queue.QueueId"
+ Negate - true/false. If set to true, it means *If queue is not any of the queues mentioned in the Operands*.

## RealTimeCall contact attributes condition
<a name="realtime-attributescondition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is the contact attribute value. 
+ ComparisonValue – "$.ContactLens.RealTimeCall.ContactAttribute.{{YOUR\_ATTRIBUTE\_KEY}}"
+ Negate - true/false. If set to true, it means *{{YOUR\_ATTRIBUTE\_KEY}} does not equal to the attribute value specified in the Operands *.

## RealTimeCall sentiment state condition
<a name="realtime-sentimentstatecondition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is one of "POSITIVE", "NEGATIVE", "NEUTRAL". 
+ ComparisonValue – "$.ContactLens.RealTimeCall.Sentiment.State"
+ FilterClause – 

  ```
  {
      "LogicOperator": "AND", // Only "AND" is supported
      "Filters": [
          {
              "Type": "ParticipantRole",
              "Data": "CUSTOMER" | "AGENT" | "ANY"
          },
          {
              "Type": "RealTimeCallContactPeriodSeconds",
              "Data": {
                  "Past": number
              }
          }
      ]
  }
  ```
+ Negate - false