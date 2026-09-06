

# OnEmailAnalysisAvailable
<a name="OnEmailAnalysisAvailable"></a>

## Agent Hierarchy
<a name="agent-hierarchy-email"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - Agent hierarchy ARNs.
+ ComparisonValue - "$.ContactLens.Email.Agent.HierarchyGroup.ARN"
+ Negate - false

## Initiation Method
<a name="initiation-method-email"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - A validated enum set of possible values. Possible values are as follows:
  + 'INBOUND'
  + 'OUTBOUND'
  + 'AGENT\_REPLY'
  + 'FLOW'
+ ComparisonValue - "$.ContactLens.Email.InitiationMethod"
+ Negate - false

## DisconnectReason
<a name="disconnect-reason-email"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - A validated enum set of possible values. Possible values are as follows:
  + 'AGENT\_DISCONNECT'
  + 'CONTACT\_FLOW\_DISCONNECT'
  + 'EXPIRED'
  + 'DISCARDED'
  + 'OTHER'
  + 'API'
  + 'TRANSFERRED'
+ ComparisonValue - "$.ContactLens.Email.DisconnectReason"
+ Negate - false

## After Contact Work Duration
<a name="after-contact-work-duration-email"></a>

**Parameters**
+ Operator - "NumberGreaterOrEqualTo" \| "NumberLessOrEqualTo"
+ Operands - A positive integer or zero.
+ ComparisonValue - "$.ContactLens.Email.Agent.AfterContactWorkDurationSecs"
+ Negate - false

## Routing Profile
<a name="routing-profile-email"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - Routing profile ARNs.
+ ComparisonValue - "$.ContactLens.Email.Agent.RoutingProfile"
+ Negate - false

## Custom User-Defined Segment Attribute
<a name="custom-user-defined-segment-attribute-email"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands - A list of segment attribute values. The values must be a value in the pre-defined attribute resource.
+ ComparisonValue - "$.ContactLens.Email.SegmentAttributes.UserDefined.[KEY]"

  The KEY must be an instance pre-defined attribute resource.
+ Negate - false or true

## Email agent condition
<a name="email-agentcondition"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of agent IDs 
+ ComparisonValue – "$.ContactLens.Email.Agent.AgentId"
+ Negate - false

## Email queue condition
<a name="email-queuecondition"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of queue IDs.
+ ComparisonValue – "$.ContactLens.Email.Queue.QueueId"
+ Negate - false

## Email no queue condition
<a name="email-noqueuecondition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – No value.
+ ComparisonValue – "$.ContactLens.Email.Queue.QueueId"
+ Negate - false

## Email contact attributes condition
<a name="email-attributescondition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is the contact attribute value. 
+ ComparisonValue – "$.ContactLens.Email.ContactAttribute.{{YOUR\_ATTRIBUTE\_KEY}}"
+ Negate - true/false. If set to true, it means *{{YOUR\_ATTRIBUTE\_KEY}} does not equal to the attribute value specified in the Operands *.

## Email agent interaction duration condition
<a name="email-agentinteractiondurationcondition"></a>

**Parameters**
+ Operator - "NumberLessOrEqualTo" \| "NumberGreaterOrEqualTo"
+ Operands – An array of number, array length can only be 1. Value is an integer with minimum value 1. 
+ ComparisonValue – "$.ContactLens.Email.Agent.AgentInteractionDurationSecs"
+ Negate - false