

# Limit what members can see
<a name="omni-limit-what-members-can-see"></a>

By default, every member of the space can read all of its telemetry. To give a member a narrower view, add a **data scope** to their grant. A data scope is a set of conditions that a row of telemetry must match for that member to see it. Rows that do not match are filtered out at read time, before results reach the member. The stored data is not changed. To control what telemetry is captured or stored in the first place, see [Protect sensitive data](omni-data-protection.md).

A data scope is enforced on the query path, so it applies wherever the member reads telemetry: query results, dashboards, trace and session views, and the answers the Omni agent gives them. The same scope applies in the Omni web UI, the IDE extension, and the API.

You configure a data scope on the grant, under `Advanced: limit the data this principal can see`, when you add or edit a member (step 5 of the procedure in [Manage space members and permissions](omni-manage-space-members-and-permissions.md)).

**Fine-grained access control with a data scope**

A data scope has two parts: the signal types the conditions apply to, and one or more condition groups.

*Signal types.* Under `Applies to`, choose `Logs`, `Traces`, or both. The condition groups filter only the signal types you select. A signal type you do not select is not filtered, and the member sees all of its rows.

*Condition groups.* Each group is a set of conditions on the fields of a row. You can add conditions of four kinds:
+ **By agent** matches rows whose resource attribute `service.name` is one of the agents you select and whose `aws.service.type` is `gen_ai_agent`. Use this to give a team access to only the agents it owns.
+ **By service** matches rows whose resource attribute `service.name` is one of the services you select. This matches every instrumented service, agents included.
+ **By account** matches rows whose resource attribute `cloud.account.id` is one of the AWS accounts you select. Use this when several accounts send telemetry to one space and each team owns an account.
+ **By field value** matches rows where a field you choose is any one of the values you enter. You can use any field that appears in your telemetry, such as a deployment environment, a tenant identifier, or a custom attribute your application sets. The field picker lists fields discovered from your telemetry, and you can also type a field name.

A condition matches when the field is equal to one of the values you list. Within one group, every condition must match (AND). Across groups, a row is visible when it matches any group (OR). A grant with no condition groups applies no data scope, and the member sees everything.

When a member holds more than one grant, their view is the union of what each grant allows. A grant without a data scope gives the member the full view, whatever scopes their other grants carry. To keep a member's view narrow, put a data scope on every grant you give them, including grants they inherit through a group.

You can set a data scope on any permission level, including Space Admin. It limits what the member can read. It does not limit the space-management actions the level allows.

**Common patterns**


| Goal | Data scope | 
| --- | --- | 
| A team sees only the agents it owns | One group. By agent, listing the team's agents. | 
| Each team sees only telemetry from its own AWS account | One grant per team. One group, By account, listing that team's account ID. | 
| An on-call engineer sees production traces for one service | Applies to Traces. One group with By service for the service and By field value for the environment attribute set to the production value. | 
| A reviewer sees two unrelated slices | Two groups, one for each slice. The member sees rows that match either group. | 

**What a data scope does and does not filter**

A data scope decides which rows a member can see. It does not hide fields inside a row. A member who can see a span or a log record sees every field on it, including prompt and response content. To keep specific content out of every member's view, redact it before it reaches the space. See [Protect sensitive data](omni-data-protection.md).

Aggregates follow the scope. A count, an error rate, or a latency percentile is computed over the rows the member can see. Two members with different scopes can get different numbers from the same query.

**Note**  
The By agent, By service, and By account pickers suggest values found in your recent telemetry. You can also type a value that has not been seen yet, for example an agent you are about to deploy. A condition on a value that never appears in the data matches no rows.

**Data scope in the grant JSON**

The `JSON` view of the add-grants form shows the grant definition, and you can edit it directly. You can also reuse it with the API, the AWS CDK, or the AWS CLI. It carries the grant name, permission level, action scopes, and tags. The principal comes from the `Name` picker and is not part of the JSON. A data scope is an action scope on a `DataSet` resource. This example limits a Viewer to traces from two agents, or to any trace whose deployment environment is `prod`. Logs stay unrestricted: the scope names only `TRACES` in `signalTypes`, so the `READ` permission level keeps its default full access to logs.

```
{
  "name": "checkout-team-viewer",
  "permission": "READ",
  "scopedActions": [
    {
      "actions": [
        "cloudwatch:GetRecords",
        "cloudwatch:ListMetrics",
        "cloudwatch:GetMetricData"
      ],
      "resources": [
        {
          "resourceType": "DataSet",
          "signalTypes": ["TRACES"],
          "rowScopeGroups": [
            [
              {
                "operator": "IN",
                "field": "resource['attributes']['service.name']",
                "values": ["checkout-agent", "returns-agent"]
              },
              {
                "operator": "IN",
                "field": "resource['attributes']['aws.service.type']",
                "values": ["gen_ai_agent"]
              }
            ],
            [
              {
                "operator": "IN",
                "field": "resource['attributes']['deployment.environment']",
                "values": ["prod"]
              }
            ]
          ]
        }
      ]
    }
  ]
}
```

`rowScopeGroups` is a list of groups. Conditions inside a group combine with AND, and groups combine with OR. `IN` is the only operator. A nested attribute is written in bracket notation, so a dotted attribute name such as `service.name` is read as one name.

The example above uses a single group. This one uses two groups, each with two conditions, so it shows both axes at once. It limits a Viewer to traces from the `checkout-agent` **in `prod`**, or to any trace from the `returns-service` **in account `111122223333`**. Logs stay unrestricted, since `signalTypes` names only `TRACES`.

```
{
  "name": "returns-reviewer",
  "permission": "READ",
  "scopedActions": [
    {
      "actions": [
        "cloudwatch:GetRecords",
        "cloudwatch:ListMetrics",
        "cloudwatch:GetMetricData"
      ],
      "resources": [
        {
          "resourceType": "DataSet",
          "signalTypes": ["TRACES"],
          "rowScopeGroups": [
            [
              {
                "operator": "IN",
                "field": "resource['attributes']['service.name']",
                "values": ["checkout-agent"]
              },
              {
                "operator": "IN",
                "field": "resource['attributes']['deployment.environment']",
                "values": ["prod"]
              }
            ],
            [
              {
                "operator": "IN",
                "field": "resource['attributes']['service.name']",
                "values": ["returns-service"]
              },
              {
                "operator": "IN",
                "field": "resource['attributes']['cloud.account.id']",
                "values": ["111122223333"]
              }
            ]
          ]
        }
      ]
    }
  ]
}
```

A trace is visible when it matches group 1 (`service.name` is `checkout-agent` **and** `deployment.environment` is `prod`) or group 2 (`service.name` is `returns-service` **and** `cloud.account.id` is `111122223333`). Every condition inside a group must match (AND); a row that matches any group is visible (OR).