

# OnScheduleUpdate
<a name="OnScheduleUpdate"></a>

The OnScheduleUpdate event source runs a rule when a published schedule is updated.

Scheduling rules have the following requirements:
+ The rule function must contain a forecast group, staffing group, impacted agents, or shift activity condition.
+ The rule function can contain only one of the forecast group, staffing group, or impacted agents conditions. You can combine a shift activity condition with any of them.
+ All conditions use the CONTAINS\_ANY operator and Negate must be false.
+ Each condition can be used only once in a rule function. To match more than one resource, list them in the Operands of that condition.
+ The rule function is a single AND operator whose operands are conditions. The OR operator and nested AND or OR groups aren't supported.
+ Supported actions are CREATE\_TASK, SEND\_NOTIFICATION, SEND\_IN\_APP\_NOTIFICATION, and GENERATE\_EVENTBRIDGE\_EVENT. A rule can have 1 to 4 actions, and each action type can be used only once.

## Forecast group condition
<a name="OnScheduleUpdate-fg-condition"></a>

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
<a name="OnScheduleUpdate-sg-condition"></a>

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

## Impacted agents condition
<a name="OnScheduleUpdate-agents-condition"></a>

The rule runs when the event affects at least one of the specified agents.

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of 1 to 100 agent (user) IDs.
+ ComparisonValue – "$.Scheduling.ImpactedAgents[\*].Id"
+ Negate - false

```
{
    "Operator": "CONTAINS_ANY",
    "Operands": ["agentId1", "agentId2"],
    "ComparisonValue": "$.Scheduling.ImpactedAgents[*].Id",
    "Negate": false
}
```

## Shift activity condition
<a name="OnScheduleUpdate-sa-condition"></a>

The rule runs when the schedule update involves at least one of the specified shift activities.

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of 1 to 100 shift activity IDs.
+ ComparisonValue – "$.Scheduling.ShiftActivities[\*].Id"
+ Negate - false

```
{
    "Operator": "CONTAINS_ANY",
    "Operands": ["shiftActivityId"],
    "ComparisonValue": "$.Scheduling.ShiftActivities[*].Id",
    "Negate": false
}
```

## Example rule function
<a name="OnScheduleUpdate-example"></a>

```
{
    "Version": "2022-11-25",
    "RuleFunction": {
        "Operator": "AND",
        "Operands": [
        {
            "Operator": "CONTAINS_ANY",
            "Operands": ["agentId1", "agentId2"],
            "ComparisonValue": "$.Scheduling.ImpactedAgents[*].Id",
            "Negate": false
        },
        {
            "Operator": "CONTAINS_ANY",
            "Operands": ["shiftActivityId"],
            "ComparisonValue": "$.Scheduling.ShiftActivities[*].Id",
            "Negate": false
        }
        ]
    }
}
```