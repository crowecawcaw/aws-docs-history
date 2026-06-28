# OnEmailAnalysisAvailable

## Agent Hierarchy

###### Parameters

- Operator - "CONTAINS\_ANY"
- Operands - Agent hierarchy ARNs.
- ComparisonValue - "$.ContactLens.Email.Agent.HierarchyGroup.ARN"
- Negate - false

## Initiation Method

###### Parameters

- Operator - "CONTAINS\_ANY"
- Operands - A validated enum set of possible values. Possible values are as follows:

  - 'INBOUND'
  - 'OUTBOUND'
  - 'AGENT\_REPLY'
  - 'FLOW'

- ComparisonValue - "$.ContactLens.Email.InitiationMethod"
- Negate - false

## DisconnectReason

###### Parameters

- Operator - "CONTAINS\_ANY"
- Operands - A validated enum set of possible values. Possible values are as follows:

  - 'AGENT\_DISCONNECT'
  - 'CONTACT\_FLOW\_DISCONNECT'
  - 'EXPIRED'
  - 'DISCARDED'
  - 'OTHER'
  - 'API'
  - 'TRANSFERRED'

- ComparisonValue - "$.ContactLens.Email.DisconnectReason"
- Negate - false

## After Contact Work Duration

###### Parameters

- Operator - "NumberGreaterOrEqualTo" | "NumberLessOrEqualTo"
- Operands - A positive integer or zero.
- ComparisonValue - "$.ContactLens.Email.Agent.AfterContactWorkDurationSecs"
- Negate - false

## Routing Profile

###### Parameters

- Operator - "CONTAINS\_ANY"
- Operands - Routing profile ARNs.
- ComparisonValue - "$.ContactLens.Email.Agent.RoutingProfile"
- Negate - false

## Custom User-Defined Segment Attribute

###### Parameters

- Operator - "CONTAINS\_ANY"
- Operands - A list of segment attribute values. The values must be a value in the pre-defined attribute resource.
- ComparisonValue - "$.ContactLens.Email.SegmentAttributes.UserDefined.[KEY]"

The KEY must be an instance pre-defined attribute resource.

- Negate - false or true

## Email agent condition

###### Parameters

- Operator - "CONTAINS\_ANY"
- Operands – A list of agent IDs
- ComparisonValue – "$.ContactLens.Email.Agent.AgentId"
- Negate - false

## Email queue condition

###### Parameters

- Operator - "CONTAINS\_ANY"
- Operands – A list of queue IDs.
- ComparisonValue – "$.ContactLens.Email.Queue.QueueId"
- Negate - false

## Email no queue condition

###### Parameters

- Operator - "EQUALS"
- Operands – No value.
- ComparisonValue – "$.ContactLens.Email.Queue.QueueId"
- Negate - false

## Email contact attributes condition

###### Parameters

- Operator - "EQUALS"
- Operands – An array of string, array length can only be 1. Value is
  the contact attribute value.
- ComparisonValue –
  "$.ContactLens.Email.ContactAttribute.`YOUR_ATTRIBUTE_KEY`"
- Negate - true/false. If set to true, it means
  _`YOUR_ATTRIBUTE_KEY` does not
  equal to the attribute value specified in the Operands_ .

## Email agent interaction duration condition

###### Parameters

- Operator - "NumberLessOrEqualTo" | "NumberGreaterOrEqualTo"
- Operands – An array of number, array length can only be 1. Value is an
  integer with minimum value 1.
- ComparisonValue – "$.ContactLens.Email.Agent.AgentInteractionDurationSecs"
- Negate - false
