

# OnMetricDataUpdate
<a name="OnMetricDataUpdate"></a>

## Metric Data Update - Rule Conditions
<a name="OnMetricDataUpdate-ruleconditions"></a>

**Parameters**
+ Operator - "AND" or "OR"
+ Operands – An array of `MetricGroup`, can support up to two groups. 
+ FilterClause – Rule level metric filter for **End Dimension** or grouping. Choosing an End Dimension restricts the usage of metrics, as described in [Metric Data Update - MetricCondition](https://docs.aws.amazon.com/connect/latest/APIReference/OnMetricDataUpdate.html#OnMetricDataUpdate-MetricCondition). 

```
"Operator": "AND", // "AND or "OR"
"Operand": MetricGroup[], // Upto 2 array elements
"FilterClause" {
    "LogicOperator": "AND", // Only "AND" is supported
    "Filters": [
        {
            "Type": "MetricDataGrouping",
            "Data": ["AGENT" | "QUEUE" | "ROUTING_PROFILE" | "FLOW"] // // Only one is supported
        },
    ]
}
```

## Metric Data Update - MetricGroup
<a name="OnMetricDataUpdate-MetricGroup"></a>

Each MetricGroup can have up to compatible 10 MetricConditions grouped by an "AND" or "OR". Up to two MetricGroups are supported within the same Rule Condition.

```
"Operands": [
    {
        "Operator": "AND", // "AND or "OR"
        "Operands": MetricCondition[], // Upto 10 array elements
    },
    ...
]
```

## Metric Data Update - Metric Filters
<a name="OnMetricDataUpdate-MetricFilters"></a>

Every MetricCondition has a compound filter format, and requires a list of mandatory filters and some optional filters.

### Required filters
<a name="MetricGroup-requiredfilters"></a>

These filters are always required in MetricCondition for the when supported, but not supported in others.

#### MetricDataPeriodSeconds
<a name="MetricDataPeriodSeconds"></a>

The trailing time period window, in seconds, for which the metric is calculated. All MetricCondition within the same MetricGroup are required to have a consistent MetricDataPeriodSeconds, that is, the exact same filter in all of them, or none of them should have these filters. The time window has to less than 24 hours (< 86400).

```
{
    "Type": "MetricDataPeriodSeconds", // Required for Historical mertcis
    "Data": { "Past": 300} 
}
```

Supported metrics: `AVG_HANDLE_TIME`, `AVG_QUEUE_ANSWER_TIME`, `AVG_INTERACTION_TIME`, `AVG_HOLD_TIME`, `SERVICE_LEVEL_X`, `AGENT_OCCUPANCY`. These metrics cannot be clubbed with other metrics in the same MetricGroup.

#### AgentActivityDurationSeconds
<a name="AgentActivityDurationSeconds"></a>

This filter is only required for `AGENT_ACTIVITY` metric, and determines the time period window, in seconds, for which the Agent Activity status is held. It has to less than 24 hours (< 86400).

```
{
    "Type": "AgentActvityDurationSeconds",
    "Data": { "Past": 300} 
}
```

#### MetricDataThresholdSeconds
<a name="MetricDataThresholdSeconds"></a>

This filter is only required for `SERVICE_LEVEL_X`, and is defined [here](https://docs.aws.amazon.com/connect/latest/APIReference/API_MetricV2.html#connect-Type-MetricV2-Threshold). 

```
{
    "Type": "MetricDataThresholdSeconds",
    "Data": { "Comparison": "LT", "ThresholdValue": 300} // Comparison == "LT" only
}
```

### End Dimension filters
<a name="EndDimensionFilters"></a>

Exactly one of the below filters is required for every MetricCondition. If the MetricConditions are in the same group, then they are required to have the same End Dimension Filter. For more information about these filters, see [GetMetricDataV2 request filters](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html#connect-GetMetricDataV2-request-Filters). 

#### MetricDataFilterByAgent
<a name="MetricDataFilterByAgent"></a>

Provide the list of Agent IDs in MetricCondition. Up to 25 values can be provided.

```
{
    "Type": "MetricDataFilterByAgent",
    "Data": ["c04377e2-db01-4182-bc02-4285a66279e7", "1e5a6965-7b64-420d-88a8-a83d2a15081d"]
}
```

#### MetricDataFilterByAgentHierarchyLevelX
<a name="MetricDataFilterByAgentHierarchyLevelX"></a>

Agent Hierarchy filters can be any of the five types: 

1. MetricDataFilterByAgentHierarchyLevelOne

1. MetricDataFilterByAgentHierarchyLevelTwo 

1. MetricDataFilterByAgentHierarchyLevelThree

1. MetricDataFilterByAgentHierarchyLevelFour

1. MetricDataFilterByAgentHierarchyLevelFive

Provide the Agent Hierarchy ID in the filter. 

```
{
    "Type": "MetricDataFilterByAgentHierarchyLevelFive", 
    "Data": ["b99ba702-b84b-4279-abad-5ceda9ff2640"] // One array element only
}
```

**Note**  
Only one value is supported in the filter.

#### MetricDataFilterByQueue
<a name="MetricDataFilterByQueue"></a>

Provide the list of Queue IDs in MetricCondition. Up to 25 values can be provided.

```
{
    "Type": "MetricDataFilterByQueue",
    "Data": ["c04377e2-db01-4182-bc02-4285a66279e7", "1e5a6965-7b64-420d-88a8-a83d2a15081d"]
}
```

#### MetricDataFilterByRoutingProfile
<a name="MetricDataFilterByRoutingProfile"></a>

Provide the list of Routing Profile IDs in MetricCondition. Up to 25 values can be provided.

```
{
    "Type": "MetricDataFilterByRoutingProfile",
    "Data": ["b653beae-0a34-4f0c-83d3-067c9b8370bf" , "60a4c89a-b485-4bf2-8396-2a151b4e05a7"]
}
```

#### MetricDataFilterByFlow
<a name="MetricDataFilterByFlow"></a>

Provide the list of Flow IDs in MetricCondition. Up to 25 values can be provided.

```
{
    "Type": "MetricDataFilterByFlow",
    "Data": ["a04377e2-zb01-g182-nc02-a285a66279en", "ae5a6965-zb64-g20d-n8a8-a83d2a15081n"]
}
```

#### MetricDataFilterByFlowModule
<a name="MetricDataFilterByFlowModule"></a>

Provide the list of flow module IDs in MetricCondition. Up to 25 values can be provided.

```
{
    "Type": "MetricDataFilterByFlowModule",
    "Data": ["a04377e2-zb01-g182-nc02-a285a66279en", "ae5a6965-zb64-g20d-n8a8-a83d2a15081n"]
}
```

#### MetricDataFilterByFlowOutcomeType
<a name="MetricDataFilterByFlowOutcomeType"></a>

Flow Outcome Type filter values can be any of the following depending on the filter resource is flow/module.
+ DROPPED
+ DISCONNECTED\_PARTICIPANT
+ ENDED\_FLOW\_EXECUTION
+ TRANSFERRED\_TO\_QUEUE
+ TRANSFERRED\_TO\_AGENT
+ TRANSFERRED\_TO\_FLOW
+ TRANSFERRED\_TO\_PHONE\_NUMBER
+ RETURNED\_TO\_FLOW

```
{
    "Type": "MetricDataFilterByFlowOutcomeType", 
    "Data": ["DROPPED", "TRANSFERRED_TO_QUEUE"] // Multiple values can be provided
}
```

### Optional filters
<a name="optionalfilters"></a>

The following filters are optional in MetricCondition.

#### MetricDataFilterByChannel
<a name="MetricDataFilterByChannel"></a>

This is an optional filter that is supported in MetricCondition for all metrics. However, if used, it is require to be consistent for every MetricCondition. 

```
{
    "Type": "MetricDataFilterByChannel",
    "Data": ["VOICE", "CHAT", "TASK"], // any subset of this is valid
}
```

Exception: It cannot be used with `AGENT_ACTIVITY` and `AGENT_OCCUPANCY` metrics, but can be used for other metrics in the same RuleCondition but within a different MetricGroup.

## Metric Data Update - MetricCondition
<a name="OnMetricDataUpdate-MetricCondition"></a>

**Topics**
+ [AGENT\_ACTIVITY](#MetricCondition-Agent-Activity)
+ [OLDEST\_CONTACT\_AGE](#MetricCondition-Oldest-contact-age)
+ [AGENTS\_AVAILABLE](#MetricCondition-AGENTS_AVAILABLE)
+ [CONTACTS\_IN\_QUEUE](#MetricCondition-CONTACTS_IN_QUEUE)
+ [AVG\_QUEUE\_ANSWER\_TIME](#MetricCondition-AVG_QUEUE_ANSWER_TIME)
+ [AVG\_INTERACTION\_TIME](#MetricCondition-AVG_INTERACTION_TIME)
+ [AVG\_HOLD\_TIME](#MetricCondition-AVG_HOLD_TIME)
+ [AVG\_HANDLE\_TIME](#MetricCondition-AVG_HANDLE_TIME)
+ [AGENT\_OCCUPANCY](#MetricCondition-AGENT_OCCUPANCY)
+ [SERVICE\_LEVEL](#MetricCondition-SERVICE_LEVEL)
+ [FLOWS\_STARTED](#FLOWSSTARTED)
+ [AVG\_FLOW\_TIME](#AVG_FLOW_TIME)
+ [MAX\_FLOW\_TIME](#MAX_FLOW_TIME)
+ [MIN\_FLOW\_TIME](#MIN_FLOW_TIME)
+ [FLOWS\_OUTCOME](#FLOWS_OUTCOME)
+ [PERCENT\_FLOWS\_OUTCOME](#PERCENT_FLOWS_OUTCOME)

### AGENT\_ACTIVITY
<a name="MetricCondition-Agent-Activity"></a>

For more information about the AGENT\_ACTIVITY metric, see [AGENT\_ACTIVITY](https://docs.aws.amazon.com/connect/latest/adminguide/real-time-metrics-definitions.html#agent-activity-state-real-time) and [About agent status](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-agent-status.html). 

The `AGENT_ACTIVITY` metric supports an agent s`tatusId`, or string values of one of the following states: `ERROR`, `MISSED`, `REJECTED`, `ON_CONTACT`, `AFTER_CONTACT_WORK`, `INCOMING`, `AVAILABLE`.

The following example shows:

```
Rule: When any agent with Hierarchy Level 1 (filterValue = b99ba702-b84b-4279-abad-5ceda9ff2640) has 
                        had AGENT_ACTIVITY equal to statusId ee8c71b9-49c2-4d00-ab6d-244f2d9a5c58 for the last 600 seconds, then perform a [RuleAction](https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAction.html).
```

```
{
    Operator: "EQUALS", // Fixed value
    ComparisonValue: "$.MetricData.AGENT_ACTIVITY",
    Operands: ["ee8c71b9-49c2-4d00-ab6d-244f2d9a5c58"],
    FilterClause: {
      LogicOperator: "AND", // Always "AND"
      Filters: [
        {
          Type: "MetricDataFilterByAgentHierarchyLevelOne",
          Data: ["b99ba702-b84b-4279-abad-5ceda9ff2640"],
        },
        {
          Type: "AgentActivityDurationSeconds",
          Data: { Past: 600 },
        },
      ],
    },
    Negate: true, // or false
  },
```

Supported End Dimensions (MetricDataGrouping): `AGENT`

Required Filters: `AgentActivityDurationSeconds`

Supported End Dimension Filters: `MetricDataFilterByAgent`, `MetricDataFilterByAgentHierarchyLevelX`, `MetricDataFilterByQueue`, `MetricDataFilterByRoutingProfile`

### OLDEST\_CONTACT\_AGE
<a name="MetricCondition-Oldest-contact-age"></a>

For more information about the OLDEST\_CONTACT\_AGE metric, see [GetCurrentMetricData](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetCurrentMetricData.html) and [Oldest](https://docs.aws.amazon.com/connect/latest/adminguide/real-time-metrics-definitions.html#oldest-real-time). 

Rule: OLDEST\_CONTACT\_AGE metric value, filtered by listed queues and channels ≥ 900 (15 minutes), then perform a [RuleAction](https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAction.html). 

```
{
    Operator: "NumberGreaterOrEqualTo", // also supports "NumberLessOrEqualTo"
    ComparisonValue: "$.MetricData.OLDEST_CONTACT_AGE",
    Operands: [900],
    FilterClause: {
      LogicOperator: "AND", // Always "AND"
      Filters: [
        {
          Type: "MetricDataFilterByQueue",
          Data: ["c04377e2-db01-4182-bc02-4285a66279e7", "1e5a6965-7b64-420d-88a8-a83d2a15081d"],
        },
        {
          Type: "MetricDataFilterByChannel",
          Data: ["CHAT"],
        },
      ],
    },
    Negate: false, // Fixed value
}
```

Supported End Dimensions (MetricDataGrouping): `QUEUE`

Required filters: `MetricDataFilterByQueue`, `MetricDataFilterByRoutingProfile`

Supported optional filters: `MetricDataFilterByChannel`

### AGENTS\_AVAILABLE
<a name="MetricCondition-AGENTS_AVAILABLE"></a>

For more information about the AGENTS\_AVAILABLE metric, see [GetCurrentMetricData](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetCurrentMetricData.html) and [Available](https://docs.aws.amazon.com/connect/latest/adminguide/real-time-metrics-definitions.html#available-real-time). 

Rule: `AGENTS_AVAILABLE` metric value, filtered by listed queues and channels ≤ 5, then perform a [RuleAction](https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAction.html).

```
{
    Operator: "NumberLessOrEqualTo", // also supports "NumberGreaterOrEqualTo"
    ComparisonValue: "$.MetricData.AGENTS_AVAILABLE",
    Operands: [5],
    FilterClause: {
      LogicOperator: "AND", // Always "AND"
      Filters: [
        {
          Type: "MetricDataFilterByQueue",
          Data: ["c04377e2-db01-4182-bc02-4285a66279e7", "1e5a6965-7b64-420d-88a8-a83d2a15081d"],
        },
        {
          Type: "MetricDataFilterByChannel",
          Data: ["CHAT"],
        },
      ],
    },
    Negate: false, // fixed value
  },
```

Supported End Dimensions (MetricDataGrouping): `QUEUE`, `ROUTING_PROFILE`

Supported End Dimension filters: `MetricDataFilterByQueue`, `MetricDataFilterByRoutingProfile`

Supported optional filters: `MetricDataFilterByChannel`

### CONTACTS\_IN\_QUEUE
<a name="MetricCondition-CONTACTS_IN_QUEUE"></a>

For more information about the `CONTACTS_IN_QUEUE` metric, see [GetCurrentMetricData](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetCurrentMetricData.html) and [In queue](https://docs.aws.amazon.com/connect/latest/adminguide/real-time-metrics-definitions.html#in-queue-real-time). 

Rule: CONTACTS\_IN\_QUEUE metric value, filtered by listed queues and channels ≥ 100, then perform a [RuleAction](https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAction.html).

```
{
    Operator: "NumberGreaterOrEqualTo", // also supports "NumberLessOrEqualTo"
    ComparisonValue: "$.MetricData.CONTACTS_IN_QUEUE",
    Operands: [100],
    FilterClause: {
      LogicOperator: "AND", // Always "AND"
      Filters: [
        {
          Type: "MetricDataFilterByQueue",
          Data: ["c04377e2-db01-4182-bc02-4285a66279e7", "1e5a6965-7b64-420d-88a8-a83d2a15081d"],
        },
        {
          Type: "MetricDataFilterByChannel",
          Data: ["CHAT"],
        },
      ],
    },
    Negate: false, // fixed value
},
```

Supported End Dimensions (MetricDataGrouping): `QUEUE` 

Supported End Dimension filters: `MetricDataFilterByQueue`, `MetricDataFilterByRoutingProfile`

Supported optional filters: `MetricDataFilterByChannel`

### AVG\_QUEUE\_ANSWER\_TIME
<a name="MetricCondition-AVG_QUEUE_ANSWER_TIME"></a>

For more information about the AVG\_QUEUE\_ANSWER\_TIME metric, see [GetCurrentMetricData](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html) and [Avg queue answer time](https://docs.aws.amazon.com/connect/latest/adminguide/real-time-metrics-definitions.html#average-queue-answer-time-real-time). 

Rule: AVG\_QUEUE\_ANSWER\_TIME metric value, over the given duration of 28800 seconds (8 hours), filtered by listed queues and channels ≥ 900 (15 minutes), then perform a [RuleAction](https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAction.html).

```
{
    Operator: "NumberGreaterOrEqualTo", // also supports "NumberLessOrEqualTo"
    ComparisonValue: "$.MetricData.AVG_QUEUE_ANSWER_TIME",
    Operands: [900],
    FilterClause: {
      LogicOperator: "AND", // Always "AND"
      Filters: [
        {
          Type: "MetricDataFilterByQueue",
          Data: ["c04377e2-db01-4182-bc02-4285a66279e7", "1e5a6965-7b64-420d-88a8-a83d2a15081d"],
        },
        {
          Type: "MetricDataFilterByChannel",
          Data: ["CHAT"],
        },
        {
          Type: "MetricDataDurationSeconds",
          Data: { Past: 28800 },
        },
      ],
    },
    Negate: false, // fixed value
  }
```

Supported End Dimensions (MetricDataGrouping): `QUEUE` 

Required Filters: `MetricDataDurationSeconds`

Supported End Dimension filters: `MetricDataFilterByQueue`, `MetricDataFilterByRoutingProfile`

Supported optional filters: `MetricDataFilterByChannel`

### AVG\_INTERACTION\_TIME
<a name="MetricCondition-AVG_INTERACTION_TIME"></a>

For more information about the AVG\_INTERACTION\_TIME metric, see [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html). 

Rule: AVG\_INTERACTION\_TIME metric value, over the given duration of 28800 seconds (8 hours), filtered by listed queues and channels ≥ 1800 (30 minutes), then perform a [RuleAction](https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAction.html).

```
{
    Operator: "NumberGreaterOrEqualTo", // also supports "NumberLessOrEqualTo"
    ComparisonValue: "$.MetricData.AVG_INTERACTION_TIME",
    Operands: [1800],
    FilterClause: {
      LogicOperator: "AND", // Always "AND"
      Filters: [
        {
          Type: "MetricDataFilterByQueue",
          Data: ["c04377e2-db01-4182-bc02-4285a66279e7", "1e5a6965-7b64-420d-88a8-a83d2a15081d"],
        },
        {
          Type: "MetricDataFilterByChannel",
          Data: ["CHAT"],
        },
        {
          Type: "MetricDataDurationSeconds",
          Data: { Past: 28800 }, // 8 hours
        },
      ],
    },
    Negate: false, // fixed value
  },
```

Supported End Dimensions (MetricDataGrouping): `QUEUE` 

Required Filters: `MetricDataDurationSeconds`

Supported End Dimension filters: `MetricDataFilterByQueue`, `MetricDataFilterByRoutingProfile`

Supported optional filters: `MetricDataFilterByChannel`

### AVG\_HOLD\_TIME
<a name="MetricCondition-AVG_HOLD_TIME"></a>

For more information about the AVG\_HOLD\_TIME metric, see [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html). 

Rule: AVG\_HOLD\_TIME metric value, over the given duration of 28800 seconds (8 hours), filtered by listed queues and channels ≥ 1800 (30 minutes), then perform a [RuleAction](https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAction.html).

```
{
    Operator: "NumberGreaterOrEqualTo", // also supports "NumberLessOrEqualTo"
    ComparisonValue: "$.MetricData.AVG_HOLD_TIME",
    Operands: [1800],
    FilterClause: {
      LogicOperator: "AND", // Always "AND"
      Filters: [
        {
          Type: "MetricDataFilterByQueue",
          Data: ["c04377e2-db01-4182-bc02-4285a66279e7", "1e5a6965-7b64-420d-88a8-a83d2a15081d"],
        },
        {
          Type:"MetricDataFilterByChannel",
          Data: ["CHAT"],
        },
        {
          Type: "MetricDataDurationSeconds",
          Data: { Past: 28800 },
        },
      ],
    },
    Negate: false, // fixed value
  },
```

Supported End Dimensions (MetricDataGrouping): `QUEUE` 

Required Filters: `MetricDataDurationSeconds`

Supported End Dimension filters: `MetricDataFilterByQueue`, `MetricDataFilterByRoutingProfile`

Supported optional filters: `MetricDataFilterByChannel`

### AVG\_HANDLE\_TIME
<a name="MetricCondition-AVG_HANDLE_TIME"></a>

For more information about the AVG\_HANDLE\_TIME metric, see [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html). 

Rule: AVG\_HANDLE\_TIME metric value, over the given duration of 28800 seconds (8 hours), filtered by listed queues and channels ≥ 1800 (30 minutes), then perform a [RuleAction](https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAction.html).

```
{
    Operator: "NumberGreaterOrEqualTo", // also supports "NumberLessOrEqualTo"
    ComparisonValue: "$.MetricData.AVG_HANDLE_TIME",
    Operands: [1800],
    FilterClause: {
      LogicOperator: "AND", // Always "AND"
      Filters: [
        {
          Type: "MetricDataFilterByQueue",
          Data: ["c04377e2-db01-4182-bc02-4285a66279e7", "1e5a6965-7b64-420d-88a8-a83d2a15081d"],
        },
        {
          Type: "MetricDataFilterByChannel",
          Data: ["CHAT"],
        },
        {
          Type: "MetricDataDurationSeconds",
          Data: { Past: 28800 },
        },
      ],
    },
    Negate: false, // fixed value
  },
```

Supported End Dimensions (MetricDataGrouping): `QUEUE`, `AGENT` 

Required Filters: `MetricDataDurationSeconds`

Supported End Dimension filters: For QUEUE end dimension, `MetricDataFilterByQueue` and `MetricDataFilterByRoutingProfile` are supported. For AGENT end dimensions, `MetricDataFilterByQueue`, `MetricDataFilterByRoutingProfile`, `MetricDataFilterByAgent`, and `MetricDataFilterByAgentLevelX` are supported

Supported optional filters: `MetricDataFilterByChannel`

### AGENT\_OCCUPANCY
<a name="MetricCondition-AGENT_OCCUPANCY"></a>

For more information about the AGENT\_OCCUPANCY metric, see [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html). 

Rule: AGENT\_OCCUPANCY metric value, over the given duration of 28800 seconds (8 hours), filtered by listed queues and channels ≥ 80%, then perform a [RuleAction](https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAction.html).

```
{
    Operator: "NumberGreaterOrEqualTo", // also supports "NumberLessOrEqualTo"
    ComparisonValue: "$.MetricData.AGENT_OCCUPANCY",
    Operands: [80],
    FilterClause: {
      LogicOperator: "AND", // Always "AND"
      Filters: [
        {
          Type: "MetricDataFilterByAgent",
          Data: ["c04377e2-db01-4182-bc02-4285a66279e7", "1e5a6965-7b64-420d-88a8-a83d2a15081d"],
        },
        {
          Type: "MetricDataDurationSeconds",
          Data: { Past: 300 },
        },
      ],
    },
    Negate: false, // fixed value
  },
```

Supported End Dimensions (MetricDataGrouping): `AGENT` 

Required Filters: `MetricDataDurationSeconds`

Supported End Dimension filters: `MetricDataFilterByAgent`, `MetricDataFilterByAgentLevelX`, `MetricDataFilterByRoutingProfile`

### SERVICE\_LEVEL
<a name="MetricCondition-SERVICE_LEVEL"></a>

For more information about the SERVICE\_LEVEL metric, see [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html). 

Rule: SERVICE\_LEVEL metric value, over the given duration of 600 (10 minutes) metric value, over the given duration of 28800 seconds (8 hours), filtered by listed queues and channels ≤ 50%, then perform a [RuleAction](https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAction.html).

```
{
    Operator: "NumberLessOrEqualTo", // also supports "NumberGreaterOrEqualTo"
    ComparisonValue: "$.MetricData.SERVICE_LEVEL",
    Operands: [50],
    FilterClause: {
      LogicOperator: "AND", // Always "AND"
      Filters: [
        {
          Type: "MetricDataFilterByQueue",
          Data: ["c04377e2-db01-4182-bc02-4285a66279e7", "1e5a6965-7b64-420d-88a8-a83d2a15081d"],
        },
        {
          Type: "MetricDataFilterByChannel",
          Data: ["CHAT"],
        },
        {
          Type: "MetricDataDurationSeconds",
          Data: { Past: 28800 },
        },
        {
          Type: "MetricDataThresholdSeconds",
          Data: { Comparison: MetricThresholdComparison.LT, ThresholdValue: 600},
        },
      ],
    },
    Negate: false, // fixed value
  },
```

Supported End Dimensions (MetricDataGrouping): `QUEUE` 

Required filters: `MetricDataDurationSeconds`, `MetricDataThresholdSeconds`

Supported End Dimension filters: `MetricDataFilterByQueue`, `MetricDataFilterByRoutingProfile`

Supported optional filters: `MetricDataFilterByChannel`

### FLOWS\_STARTED
<a name="FLOWSSTARTED"></a>

For more information about the FLOWS\_STARTED metric, see [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html).

Rule : FLOWS\_STARTED metric value, over the given duration of 300 seconds (5 minutes), filtered by listed flows and channels 10, then perform a [RuleAction](https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAction.html). 

```
{
    Operator: "NumberGreaterOrEqualTo", // also supports "NumberLessOrEqualTo"
    ComparisonValue: "$.MetricData.FLOWS_STARTED",
    Operands: [10],
    FilterClause: {
      LogicOperator: "AND", // Always "AND"
      Filters: [
        {
          Type: "MetricDataFilterByFlow",
          Data: ["c04377e2-db01-4182-bc02-4285a66279e7", "1e5a6965-7b64-420d-88a8-a83d2a15081d"],
        },
        {
          Type: "MetricDataDurationSeconds",
          Data: { Past: 300 }
        },
        {
          Type: "MetricDataFilterByChannel",
          Data: ["CHAT"],
        },
      ],
    },
    Negate: false, // Fixed value
}
```

Supported End Dimensions (MetricDataGrouping): `FLOW`

Required Filters: `MetricDataDurationSeconds`

Supported End Dimension filters: `MetricDataFilterByFlow`, `MetricDataFilterByFlowModule`

Supported optional filters: `MetricDataFilterByChannel`

### AVG\_FLOW\_TIME
<a name="AVG_FLOW_TIME"></a>

For more information about the AVG\_FLOW\_TIME metric, see [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html).

Rule : `AVG_FLOW_TIME` metric value, over the given duration of 300 seconds (5 minutes), filtered by listed flows, flow outcomes and channels >= 600 (10 minutes), then perform a [RuleAction](https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAction.html).

```
{
    Operator: "NumberGreaterOrEqualTo", // also supports "NumberLessOrEqualTo"
    ComparisonValue: "$.MetricData.AVG_FLOW_TIME",
    Operands: [600],
    FilterClause: {
      LogicOperator: "AND", // Always "AND"
      Filters: [
        {
          Type: "MetricDataFilterByFlow",
          Data: ["5f873afb-f359-4c54-b626-ecad1bd3f774"],
        },
        {
          Type: "MetricDataFilterByFlowOutcomeType",
          Data: ["DROPPED", "TRANSFERRED_TO_QUEUE"],
        },
        {
          Type: "MetricDataDurationSeconds",
          Data: {
            "Past": 300
          },
        },
        {
          Type: "MetricDataFilterByChannel",
          Data: ["CHAT"],
        },
      ],
    },
    Negate: false, // Fixed value
}
```

Supported End Dimensions (MetricDataGrouping): `FLOW`

Required Filters: `MetricDataDurationSeconds`

Supported End Dimension filters: `MetricDataFilterByFlow`, `MetricDataFilterByFlowModule`, `MetricDataFilterByFlowOutcomeType`

Supported optional filters: `MetricDataFilterByChannel`

### MAX\_FLOW\_TIME
<a name="MAX_FLOW_TIME"></a>

For more information about the MAX\_FLOW\_TIME metric, see [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html).

Rule : `MAX_FLOW_TIME` metric value, over the given duration of 300 seconds (5 minutes), filtered by listed flows, flow outcomes and channels >= 600 (10 minutes), then perform a [RuleAction](https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAction.html).

```
{
    Operator: "NumberGreaterOrEqualTo", // also supports "NumberLessOrEqualTo"
    ComparisonValue: "$.MetricData.MAX_FLOW_TIME",
    Operands: [600],
    FilterClause: {
      LogicOperator: "AND", // Always "AND"
      Filters: [
        {
          Type: "MetricDataFilterByFlow",
          Data: ["5f873afb-f359-4c54-b626-ecad1bd3f774"],
        },
        {
          Type: "MetricDataFilterByFlowOutcomeType",
          Data: ["DROPPED", "TRANSFERRED_TO_QUEUE"],
        },
        {
          Type: "MetricDataDurationSeconds",
          Data: {
            "Past": 300
          },
        },
        {
          Type: "MetricDataFilterByChannel",
          Data: ["CHAT"],
        },
      ],
    },
    Negate: false, // Fixed value
}
```

Supported End Dimensions (MetricDataGrouping): `FLOW`

Required Filters: `MetricDataDurationSeconds`

Supported End Dimension filters: `MetricDataFilterByFlow`, `MetricDataFilterByFlowModule`, `MetricDataFilterByFlowOutcomeType`

Supported optional filters: `MetricDataFilterByChannel`

### MIN\_FLOW\_TIME
<a name="MIN_FLOW_TIME"></a>

For more information about the MIN\_FLOW\_TIME metric, see [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html).

Rule : `MIN_FLOW_TIME` metric value, over the given duration of 300 seconds (5 minutes), filtered by listed flows, flow outcomes and channels >= 600 (10 minutes), then perform a [RuleAction](https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAction.html).

```
{
    Operator: "NumberGreaterOrEqualTo", // also supports "NumberLessOrEqualTo"
    ComparisonValue: "$.MetricData.MIN_FLOW_TIME",
    Operands: [600],
    FilterClause: {
      LogicOperator: "AND", // Always "AND"
      Filters: [
        {
          Type: "MetricDataFilterByFlow",
          Data: ["5f873afb-f359-4c54-b626-ecad1bd3f774"],
        },
        {
          Type: "MetricDataFilterByFlowOutcomeType",
          Data: ["DROPPED", "TRANSFERRED_TO_QUEUE"],
        },
        {
          Type: "MetricDataDurationSeconds",
          Data: {
            "Past": 300
          },
        },
        {
          Type: "MetricDataFilterByChannel",
          Data: ["CHAT"],
        },
      ],
    },
    Negate: false, // Fixed value
}
```

Supported End Dimensions (MetricDataGrouping): `FLOW`

Required Filters: `MetricDataDurationSeconds`

Supported End Dimension filters: `MetricDataFilterByFlow`, `MetricDataFilterByFlowModule`, `MetricDataFilterByFlowOutcomeType`

Supported optional filters: `MetricDataFilterByChannel`

### FLOWS\_OUTCOME
<a name="FLOWS_OUTCOME"></a>

For more information about the FLOWS\_OUTCOME metric, see [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html).

Rule : `FLOWS_OUTCOME` metric value, over the given duration of 300 seconds (5 minutes), filtered by listed flows, flow outcomes and channels >= 10, then perform a [RuleAction](https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAction.html).

```
{
    Operator: "NumberGreaterOrEqualTo", // also supports "NumberLessOrEqualTo"
    ComparisonValue: "$.MetricData.FLOWS_OUTCOME",
    Operands: [10],
    FilterClause: {
      LogicOperator: "AND", // Always "AND"
      Filters: [
        {
          Type: "MetricDataFilterByFlow",
          Data: ["5f873afb-f359-4c54-b626-ecad1bd3f774"],
        },
        {
          Type: "MetricDataFilterByFlowOutcomeType",
          Data: ["DROPPED", "TRANSFERRED_TO_QUEUE"],
        },
        {
          Type: "MetricDataDurationSeconds",
          Data: {
            "Past": 300
          },
        },
        {
          Type: "MetricDataFilterByChannel",
          Data: ["CHAT"],
        },
      ],
    },
    Negate: false, // Fixed value
}
```

Supported End Dimensions (MetricDataGrouping): `FLOW`

Required Filters: `MetricDataDurationSeconds`

Supported End Dimension filters: `MetricDataFilterByFlow`, `MetricDataFilterByFlowModule`, `MetricDataFilterByFlowOutcomeType`

Supported optional filters: `MetricDataFilterByChannel`

### PERCENT\_FLOWS\_OUTCOME
<a name="PERCENT_FLOWS_OUTCOME"></a>

For more information about the PERCENT\_FLOWS\_OUTCOME metric, see [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html).

Rule : `PERCENT_FLOWS_OUTCOME` metric value, over the given duration of 300 seconds (5 minutes), filtered by listed flows, flow outcomes and channels >= 50%, then perform a [RuleAction](https://docs.aws.amazon.com/connect/latest/APIReference/API_RuleAction.html).

```
{
    Operator: "NumberGreaterOrEqualTo", // also supports "NumberLessOrEqualTo"
    ComparisonValue: "$.MetricData.PERCENT_FLOWS_OUTCOME",
    Operands: [50],
    FilterClause: {
      LogicOperator: "AND", // Always "AND"
      Filters: [
        {
          Type: "MetricDataFilterByFlow",
          Data: ["5f873afb-f359-4c54-b626-ecad1bd3f774"],
        },
        {
          Type: "MetricDataFilterByFlowOutcomeType",
          Data: ["DROPPED", "TRANSFERRED_TO_QUEUE"],
        },
        {
          Type: "MetricDataDurationSeconds",
          Data: {
            "Past": 300
          },
        },
        {
          Type: "MetricDataFilterByChannel",
          Data: ["CHAT"],
        },
      ],
    },
    Negate: false, // Fixed value
}
```

Supported End Dimensions (MetricDataGrouping): `FLOW`

Required Filters: `MetricDataDurationSeconds`

Supported End Dimension filters: `MetricDataFilterByFlow`, `MetricDataFilterByFlowModule`, `MetricDataFilterByFlowOutcomeType`

Supported optional filters: `MetricDataFilterByChannel`

## Full examples
<a name="MetricCondition-examples"></a>

### Example 1
<a name="MetricCondition-example1"></a>

A rule with `AGENTS_AVAILABLE`, `OLDEST_CONTACT_AGE`, `CONTACTS_IN_QUEUE` in MetricGroup 1 and `AVG_QUEUE_ANSWER_TIME`, `AVG_HOLD_TIME`, `AVG_INTERACTION_TIME`, `AVG_HANDLE_TIME`, and `SERVICE_LEVEL` in Metric Group 2, both of which have End Dimension = `QUEUE`.

```
{
    "Operator": "OR",
    "Operands": [{
        "Operator": "AND",
        "Operands": [{
            "Operator": "NumberGreaterOrEqualTo",
            "ComparisonValue": "$.MetricData.AGENTS_AVAILABLE",
            "Operands": [0],
            "FilterClause": {
                "LogicOperator": "AND",
                "Filters": [{
                    "Type": "MetricDataFilterByQueue",
                    "Data": ["e7a11ddd-041d-449a-ab1e-6a493cb83626", "26b9c7f4-ed5c-4cd1-b751-2cbfb4c54ea2"]
                }, {
                    "Type": "MetricDataFilterByChannel",
                    "Data": ["VOICE"]
                }]
            },
            "Negate": false
        }, {
            "Operator": "NumberGreaterOrEqualTo",
            "ComparisonValue": "$.MetricData.CONTACTS_IN_QUEUE",
            "Operands": [0],
            "FilterClause": {
                "LogicOperator": "AND",
                "Filters": [{
                    "Type": "MetricDataFilterByQueue",
                    "Data": ["e7a11ddd-041d-449a-ab1e-6a493cb83626", "26b9c7f4-ed5c-4cd1-b751-2cbfb4c54ea2"]
                }, {
                    "Type": "MetricDataFilterByChannel",
                    "Data": ["VOICE"]
                }]
            },
            "Negate": false
        }, {
            "Operator": "NumberGreaterOrEqualTo",
            "ComparisonValue": "$.MetricData.OLDEST_CONTACT_AGE",
            "Operands": [0],
            "FilterClause": {
                "LogicOperator": "AND",
                "Filters": [{
                    "Type": "MetricDataFilterByQueue",
                    "Data": ["e7a11ddd-041d-449a-ab1e-6a493cb83626", "26b9c7f4-ed5c-4cd1-b751-2cbfb4c54ea2"]
                }, {
                    "Type": "MetricDataFilterByChannel",
                    "Data": ["VOICE"]
                }]
            },
            "Negate": false
        }]
    }, {
        "Operator": "OR",
        "Operands": [{
            "Operator": "NumberGreaterOrEqualTo",
            "ComparisonValue": "$.MetricData.AVG_HANDLE_TIME",
            "Operands": [0],
            "FilterClause": {
                "LogicOperator": "AND",
                "Filters": [{
                    "Type": "MetricDataFilterByQueue",
                    "Data": ["e7a11ddd-041d-449a-ab1e-6a493cb83626", "26b9c7f4-ed5c-4cd1-b751-2cbfb4c54ea2"]
                }, {
                    "Type": "MetricDataDurationSeconds",
                    "Data": {
                        "Past": 300
                    }
                }, {
                    "Type": "MetricDataFilterByChannel",
                    "Data": ["VOICE"]
                }]
            },
            "Negate": false
        }, {
            "Operator": "NumberGreaterOrEqualTo",
            "ComparisonValue": "$.MetricData.AVG_QUEUE_ANSWER_TIME",
            "Operands": [0],
            "FilterClause": {
                "LogicOperator": "AND",
                "Filters": [{
                    "Type": "MetricDataFilterByQueue",
                    "Data": ["e7a11ddd-041d-449a-ab1e-6a493cb83626", "26b9c7f4-ed5c-4cd1-b751-2cbfb4c54ea2"]
                }, {
                    "Type": "MetricDataDurationSeconds",
                    "Data": {
                        "Past": 300
                    }
                }, {
                    "Type": "MetricDataFilterByChannel",
                    "Data": ["VOICE"]
                }]
            },
            "Negate": false
        }, {
            "Operator": "NumberGreaterOrEqualTo",
            "ComparisonValue": "$.MetricData.AVG_INTERACTION_TIME",
            "Operands": [0],
            "FilterClause": {
                "LogicOperator": "AND",
                "Filters": [{
                    "Type": "MetricDataFilterByQueue",
                    "Data": ["e7a11ddd-041d-449a-ab1e-6a493cb83626", "26b9c7f4-ed5c-4cd1-b751-2cbfb4c54ea2"]
                }, {
                    "Type": "MetricDataDurationSeconds",
                    "Data": {
                        "Past": 300
                    }
                }, {
                    "Type": "MetricDataFilterByChannel",
                    "Data": ["VOICE"]
                }]
            },
            "Negate": false
        }, {
            "Operator": "NumberGreaterOrEqualTo",
            "ComparisonValue": "$.MetricData.AVG_HOLD_TIME",
            "Operands": [0],
            "FilterClause": {
                "LogicOperator": "AND",
                "Filters": [{
                    "Type": "MetricDataFilterByQueue",
                    "Data": ["e7a11ddd-041d-449a-ab1e-6a493cb83626", "26b9c7f4-ed5c-4cd1-b751-2cbfb4c54ea2"]
                }, {
                    "Type": "MetricDataDurationSeconds",
                    "Data": {
                        "Past": 300
                    }
                }, {
                    "Type": "MetricDataFilterByChannel",
                    "Data": ["VOICE"]
                }]
            },
            "Negate": false
        }, {
            "Operator": "NumberGreaterOrEqualTo",
            "ComparisonValue": "$.MetricData.SERVICE_LEVEL",
            "Operands": [0],
            "FilterClause": {
                "LogicOperator": "AND",
                "Filters": [{
                    "Type": "MetricDataFilterByQueue",
                    "Data": ["e7a11ddd-041d-449a-ab1e-6a493cb83626", "26b9c7f4-ed5c-4cd1-b751-2cbfb4c54ea2"]
                }, {
                    "Type": "MetricDataDurationSeconds",
                    "Data": {
                        "Past": 300
                    }
                }, {
                    "Type": "MetricDataThresholdSeconds",
                    "Data": {
                        "Comparison": "LT",
                        "ThresholdValue": 60
                    }
                }, {
                    "Type": "MetricDataFilterByChannel",
                    "Data": ["VOICE"]
                }]
            },
            "Negate": false
        }]
    }],
    "FilterClause": {
        "LogicOperator": "AND",
        "Filters": [{
            "Type": "MetricDataGrouping",
            "Data": ["QUEUE"]
        }]
    }
}
```

### Example 2
<a name="MetricCondition-example2"></a>

A rule with `AGENT_OCCUPANCY` in MetricGroup 1 and ` AGENT_ACTIVITY` and MetricGroup 2, with End Dimension = `AGENT`.

```
{
    "Operator": "OR",
    "Operands": [{
        "Operator": "AND",
        "Operands": [{
            "Operator": "NumberGreaterOrEqualTo",
            "ComparisonValue": "$.MetricData.AGENT_OCCUPANCY",
            "Operands": [0],
            "FilterClause": {
                "LogicOperator": "AND",
                "Filters": [{
                    "Type": "MetricDataFilterByAgent",
                    "Data": ["e7a11ddd-041d-449a-ab1e-6a493cb83626", "26b9c7f4-ed5c-4cd1-b751-2cbfb4c54ea2"]
                }, {
                    "Type": "MetricDataDurationSeconds",
                    "Data": {
                        "Past": 100
                    }
                }]
            },
            "Negate": false
        }]
    }, {
        "Operator": "AND",
        "Operands": [{
            "Operator": "EQUALS",
            "ComparisonValue": "$.MetricData.AGENT_ACTIVITY",
            "Operands": ["ee8c71b9-49c2-4d00-ab6d-244f2d9a5c58"],
            "FilterClause": {
                "LogicOperator": "AND",
                "Filters": [{
                    "Type": "MetricDataFilterByAgentHierarchyLevelOne",
                    "Data": ["b99ba702-b84b-4279-abad-5ceda9ff2640"]
                }, {
                    "Type": "MetricDataDurationSeconds",
                    "Data": {
                        "Past":600
                    }
                }]
            },
            "Negate": false
        }]
    }],
    "FilterClause": {
        "LogicOperator": "AND",
        "Filters": [{
            "Type": "MetricDataGrouping",
            "Data": ["AGENT"]
        }]
    }
}
```

### Example 3
<a name="MetricCondition-example3"></a>

A rule with `FLOWS_STARTED`, `AVG_FLOW_TIME`, `MAX_FLOW_TIME` in MetricGroup 1 and `FLOWS_OUTCOME`, `PERCENT_FLOWS_OUTCOME` and `MIN_FLOW_TIME` in Metric Group 2, both of which have End Dimension = `FLOW`.

```
{
  "Operator": "OR",
  "Operands": [
    {
      "Operator": "AND",
      "Operands": [
        {
          "Operator": "NumberGreaterOrEqualTo",
          "ComparisonValue": "$.MetricData.FLOWS_STARTED",
          "Operands": [
            10
          ],
          "FilterClause": {
            "LogicOperator": "AND",
            "Filters": [
              {
                "Type": "MetricDataFilterByFlow",
                "Data": [
                  "z2a11ddd-041d-449a-ab1e-6a493cb83621",
                  "y1b9c7f4-ed5c-4cd1-b751-2cbfb4c54ea3"
                ]
              },
              {
                "Type": "MetricDataFilterByChannel",
                "Data": [
                  "VOICE"
                ]
              },
              {
                "Type": "MetricDataDurationSeconds",
                "Data": {
                  "Past": 300
                }
              }
            ]
          },
          "Negate": false
        },
        {
          "Operator": "NumberGreaterOrEqualTo",
          "ComparisonValue": "$.MetricData.AVG_FLOW_TIME",
          "Operands": [
            600
          ],
          "FilterClause": {
            "LogicOperator": "AND",
            "Filters": [
              {
                "Type": "MetricDataFilterByFlow",
                "Data": [
                  "z2a11ddd-041d-449a-ab1e-6a493cb83621",
                  "y1b9c7f4-ed5c-4cd1-b751-2cbfb4c54ea3"
                ]
              },
              {
                "Type": "MetricDataFilterByFlowOutcomeType",
                "Data": [
                  "DROPPED",
                  "TRANSFERRED_TO_QUEUE"
                ]
              },
              {
                "Type": "MetricDataFilterByChannel",
                "Data": [
                  "VOICE"
                ]
              },
              {
                "Type": "MetricDataDurationSeconds",
                "Data": {
                  "Past": 300
                }
              }
            ]
          },
          "Negate": false
        },
        {
          "Operator": "NumberGreaterOrEqualTo",
          "ComparisonValue": "$.MetricData.MAX_FLOW_TIME",
          "Operands": [
            600
          ],
          "FilterClause": {
            "LogicOperator": "AND",
            "Filters": [
              {
                "Type": "MetricDataFilterByFlow",
                "Data": [
                  "z2a11ddd-041d-449a-ab1e-6a493cb83621",
                  "y1b9c7f4-ed5c-4cd1-b751-2cbfb4c54ea3"
                ]
              },
              {
                "Type": "MetricDataFilterByFlowOutcomeType",
                "Data": [
                  "DROPPED",
                  "TRANSFERRED_TO_QUEUE"
                ]
              },
              {
                "Type": "MetricDataFilterByChannel",
                "Data": [
                  "VOICE"
                ]
              },
              {
                "Type": "MetricDataDurationSeconds",
                "Data": {
                  "Past": 300
                }
              }
            ]
          },
          "Negate": false
        }
      ]
    },
    {
      "Operator": "OR",
      "Operands": [
        {
          "Operator": "NumberGreaterOrEqualTo",
          "ComparisonValue": "$.MetricData.FLOWS_OUTCOME",
          "Operands": [
            10
          ],
          "FilterClause": {
            "LogicOperator": "AND",
            "Filters": [
              {
                "Type": "MetricDataFilterByFlow",
                "Data": [
                  "z2a11ddd-041d-449a-ab1e-6a493cb83621",
                  "y1b9c7f4-ed5c-4cd1-b751-2cbfb4c54ea3"
                ]
              },
              {
                "Type": "MetricDataFilterByFlowOutcomeType",
                "Data": [
                  "DROPPED",
                  "TRANSFERRED_TO_QUEUE"
                ]
              },
              {
                "Type": "MetricDataFilterByChannel",
                "Data": [
                  "VOICE"
                ]
              },
              {
                "Type": "MetricDataDurationSeconds",
                "Data": {
                  "Past": 300
                }
              }
            ]
          },
          "Negate": false
        },
        {
          "Operator": "NumberGreaterOrEqualTo",
          "ComparisonValue": "$.MetricData.PERCENT_FLOWS_OUTCOME",
          "Operands": [
            50
          ],
          "FilterClause": {
            "LogicOperator": "AND",
            "Filters": [
              {
                "Type": "MetricDataFilterByFlow",
                "Data": [
                  "z2a11ddd-041d-449a-ab1e-6a493cb83621",
                  "y1b9c7f4-ed5c-4cd1-b751-2cbfb4c54ea3"
                ]
              },
              {
                "Type": "MetricDataFilterByFlowOutcomeType",
                "Data": [
                  "DROPPED",
                  "TRANSFERRED_TO_QUEUE"
                ]
              },
              {
                "Type": "MetricDataFilterByChannel",
                "Data": [
                  "VOICE"
                ]
              },
              {
                "Type": "MetricDataDurationSeconds",
                "Data": {
                  "Past": 300
                }
              }
            ]
          },
          "Negate": false
        },
        {
          "Operator": "NumberGreaterOrEqualTo",
          "ComparisonValue": "$.MetricData.MIN_FLOW_TIME",
          "Operands": [
            600
          ],
          "FilterClause": {
            "LogicOperator": "AND",
            "Filters": [
              {
                "Type": "MetricDataFilterByFlow",
                "Data": [
                  "z2a11ddd-041d-449a-ab1e-6a493cb83621",
                  "y1b9c7f4-ed5c-4cd1-b751-2cbfb4c54ea3"
                ]
              },
              {
                "Type": "MetricDataFilterByFlowOutcomeType",
                "Data": [
                  "DROPPED",
                  "TRANSFERRED_TO_QUEUE"
                ]
              },
              {
                "Type": "MetricDataFilterByChannel",
                "Data": [
                  "VOICE"
                ]
              },
              {
                "Type": "MetricDataDurationSeconds",
                "Data": {
                  "Past": 300
                }
              }
            ]
          },
          "Negate": false
        }
      ]
    }
  ],
  "FilterClause": {
    "LogicOperator": "AND",
    "Filters": [
      {
        "Type": "MetricDataGrouping",
        "Data": [
          "FLOW"
        ]
      }
    ]
  }
}
```