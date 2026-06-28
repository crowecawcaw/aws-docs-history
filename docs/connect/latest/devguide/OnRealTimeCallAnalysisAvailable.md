# OnRealTimeCallAnalysisAvailable

## RealTimeCall words or phrases - Exact match

###### Parameters

- Operator - "CONTAINS\_ANY"
- Operands – A list of strings
- ComparisonValue –
  "$.ContactLens.RealTimeCall.ExactMatch.Transcript"
- FilterClause –

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

- Negate - false.

## RealTimeCall words or phrases - Pattern match

###### Parameters

- Operator - "CONTAINS\_ANY"
- Operands – A list of pattern match objects. See [PatternMatch Operands](../adminguide/patternmatch-operands.md "../adminguide/patternmatch-operands.md").
- ComparisonValue –
  "$.ContactLens.RealTimeCall.PatternMatch.Transcript"
- FilterClause –

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

- Negate - false

## RealTimeCall agent condition

###### Parameters

- Operator - "CONTAINS\_ANY"
- Operands – A list of agent IDs
- ComparisonValue – "$.ContactLens.RealTimeCall.Agent.AgentId"
- Negate - false

## RealTimeCall queue condition

###### Parameters

- Operator - "CONTAINS\_ANY"
- Operands – A list of queue IDs
- ComparisonValue – "$.ContactLens.RealTimeCall.Queue.QueueId"
- Negate - true/false. If set to true, it means _If queue is
  not any of the queues mentioned in the Operands_.

## RealTimeCall contact attributes condition

###### Parameters

- Operator - "EQUALS"
- Operands – An array of string, array length can only be 1. Value is
  the contact attribute value.
- ComparisonValue –
  "$.ContactLens.RealTimeCall.ContactAttribute.`YOUR_ATTRIBUTE_KEY`"
- Negate - true/false. If set to true, it means
  _`YOUR_ATTRIBUTE_KEY` does not
  equal to the attribute value specified in the Operands_ .

## RealTimeCall sentiment state condition

###### Parameters

- Operator - "EQUALS"
- Operands – An array of string, array length can only be 1. Value is
  one of "POSITIVE", "NEGATIVE", "NEUTRAL".
- ComparisonValue – "$.ContactLens.RealTimeCall.Sentiment.State"
- FilterClause –

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

- Negate - false
