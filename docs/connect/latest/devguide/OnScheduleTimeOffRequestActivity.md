

# OnScheduleTimeOffRequestActivity
<a name="OnScheduleTimeOffRequestActivity"></a>

The OnScheduleTimeOffRequestActivity event source runs a rule when there is activity on an agent's time off request.

Scheduling rules have the following requirements:
+ The rule function must contain a forecast group, staffing group, or time off activity condition. An impacted agent condition on its own isn't enough.
+ The rule function can contain only one of the forecast group, staffing group, or impacted agent conditions. You can combine a time off activity condition with any of them.
+ All conditions use the CONTAINS\_ANY operator and Negate must be false.
+ Each condition can be used only once in a rule function. To match more than one resource, list them in the Operands of that condition.
+ The rule function is a single AND operator whose operands are conditions. The OR operator and nested AND or OR groups aren't supported.
+ Supported actions are CREATE\_TASK, SEND\_NOTIFICATION, SEND\_IN\_APP\_NOTIFICATION, and GENERATE\_EVENTBRIDGE\_EVENT. A rule can have 1 to 4 actions, and each action type can be used only once.

## Forecast group condition
<a name="OnScheduleTimeOffRequestActivity-fg-condition"></a>

The rule runs when the event belongs to one of the specified forecast groups.

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of 1 to 100 forecast group IDs.
+ ComparisonValue – "$.Scheduling.ForecastGroup.Id"
+ Negate - false

```
{
    "Operator": "CONTAINS_ANY",
    "Operands": ["forecastGroupId"],
    "ComparisonValue": "$.Scheduling.ForecastGroup.Id",
    "Negate": false
}
```

## Staffing group condition
<a name="OnScheduleTimeOffRequestActivity-sg-condition"></a>

The rule runs when the event affects at least one of the specified staffing groups.

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of 1 to 100 staffing group IDs.
+ ComparisonValue – "$.Scheduling.StaffingGroups[\*].Id"
+ Negate - false

```
{
    "Operator": "CONTAINS_ANY",
    "Operands": ["staffingGroupId1", "staffingGroupId2"],
    "ComparisonValue": "$.Scheduling.StaffingGroups[*].Id",
    "Negate": false
}
```

## Time off activity condition
<a name="OnScheduleTimeOffRequestActivity-toa-condition"></a>

The rule runs when the time off request uses one of the specified time off activities.

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of 1 to 100 time off activity IDs.
+ ComparisonValue – "$.Scheduling.TimeOffActivity.Id"
+ Negate - false

```
{
    "Operator": "CONTAINS_ANY",
    "Operands": ["timeOffActivityId"],
    "ComparisonValue": "$.Scheduling.TimeOffActivity.Id",
    "Negate": false
}
```

## Impacted agent condition
<a name="OnScheduleTimeOffRequestActivity-agent-condition"></a>

The rule runs when the time off request belongs to one of the specified agents.

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of 1 to 100 agent (user) IDs.
+ ComparisonValue – "$.Scheduling.ImpactedAgent.Id"
+ Negate - false

```
{
    "Operator": "CONTAINS_ANY",
    "Operands": ["agentId1", "agentId2"],
    "ComparisonValue": "$.Scheduling.ImpactedAgent.Id",
    "Negate": false
}
```

## Example rule function
<a name="OnScheduleTimeOffRequestActivity-example"></a>

```
{
    "Version": "2022-11-25",
    "RuleFunction": {
        "Operator": "AND",
        "Operands": [
        {
            "Operator": "CONTAINS_ANY",
            "Operands": ["staffingGroupId1", "staffingGroupId2"],
            "ComparisonValue": "$.Scheduling.StaffingGroups[*].Id",
            "Negate": false
        },
        {
            "Operator": "CONTAINS_ANY",
            "Operands": ["timeOffActivityId"],
            "ComparisonValue": "$.Scheduling.TimeOffActivity.Id",
            "Negate": false
        }
        ]
    }
}
```