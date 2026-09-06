

# UpdateRoutingCriteria
<a name="flow-control-actions-updateroutingcriteria"></a>

Sets the routing criteria for the contact. 

## Parameter object
<a name="updateroutingcriteria-parameter"></a>

```
{
    "RoutingCriteria": { Required. RoutingCriteria is a JSON object.
            "Steps": [{  Required. List of routing steps. When Connect Customer not find an available agent meeting the requirements in a step for a given step duration, the routing criteria will move on to the next step sequentially until a join is completed with an agent. When all steps are exhausted, the contact will be offered to any agent in the queue.  May be set statically or dynamically
                "Expression": { Required. An object to specify the expression of a routing step. It is a tagged union to specify expression for a routing step.
                    "AttributeCondition": {An object to specify the predefined attribute condition.
                        "Name": The name of predefined attribute. It is a string and has length constraints between 1-64.
                        "Value": The value of predefined attribute. It is a string and has length constraints between 1-64.
                        "ProficiencyLevel": The proficiency level of the condition. It is a float value. Valid values are: 1.0, 2.0, 3.0, 4.0 and 5.0
                        "ComparisonOperator": The operator of the condition. It is a string. Valid values: NumberGreaterOrEqualTo
                    }
                   "AndExpression": [List of routing expressions (attribute conditions) which will be AND-ed together.]
                },
                "Expiry": { An object to specify the expiration of a routing step.
                    "DurationInSeconds": The number of seconds to wait before expiring the routing step. Can be set only statically
                }
            }]
        }
}
```

## Results and conditions
<a name="updateroutingcriteria-results"></a>

None. No conditions are supported.

## Errors
<a name="updateroutingcriteria-errors"></a>

NoMatchingError - if no other Error matches.

## Restrictions
<a name="updateroutingcriteria-restrictions"></a>

This action is supported on all channels and in only in Inbound flow, Customer Queue flow, Transfer to Agent flow, and Transfer to Queue flow types.

## Corresponding block in the UI
<a name="updateroutingcriteria-ui"></a>

[Set routing criteria](https://docs.aws.amazon.com/connect/latest/adminguide/set-routing-criteria.html) 