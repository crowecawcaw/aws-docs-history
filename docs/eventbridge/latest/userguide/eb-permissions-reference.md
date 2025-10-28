# Amazon EventBridge permissions reference

To specify an action in an EventBridge policy, use the `events:` prefix followed by
the API operation name, as shown in the following example.

```
"Action": "events:PutRule"
```

To specify multiple actions in a single statement, separate them with commas as
follows.

```
"Action": ["events:action1", "events:action2"]
```

To specify multiple actions, you can also use wildcards. For example, you can specify all
actions that begin with the word `"Put"` as follows.

```
"Action": "events:Put*"
```

To specify all EventBridge API actions, use the `*` wildcard as follows.

```
"Action": "events:*"
```

The following table lists the EventBridge API operations and corresponding actions that you can
specify in an IAM policy.

| EventBridge API operation                                                                                            | Required permissions           | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------- |
| [DeleteRule](../APIReference/API_DeleteRule.md "../APIReference/API_DeleteRule.md")                                  | `events:DeleteRule`            | Required to delete a rule.                                                                               |
| [DescribeEventBus](../APIReference/API_DescribeEventBus.md "../APIReference/API_DescribeEventBus.md")                | `events:DescribeEventBus`      | Required to list accounts that are allowed to write events to the current account's event bus.           |
| [DescribeRule](../APIReference/API_DescribeRule.md "../APIReference/API_DescribeRule.md")                            | `events:DescribeRule`          | Required to list the details about a rule.                                                               |
| [DisableRule](../APIReference/API_DisableRule.md "../APIReference/API_DisableRule.md")                               | `events:DisableRule`           | Required to disable a rule.                                                                              |
| [EnableRule](../APIReference/API_EnableRule.md "../APIReference/API_EnableRule.md")                                  | `events:EnableRule`            | Required to enable a rule.                                                                               |
| [ListRuleNamesByTarget](../APIReference/API_ListRuleNamesByTarget.md "../APIReference/API_ListRuleNamesByTarget.md") | `events:ListRuleNamesByTarget` | Required to list rules associated with a target.                                                         |
| [ListRules](../APIReference/API_ListRules.md "../APIReference/API_ListRules.md")                                     | `events:ListRules`             | Required to list all rules in your account.                                                              |
| [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")       | `events:ListTagsForResource`   | Required to list all tags associated with an EventBridge resource. Currently, only rules can be tagged.  |
| [ListTargetsByRule](../APIReference/API_ListTargetsByRule.md "../APIReference/API_ListTargetsByRule.md")             | `events:ListTargetsByRule`     | Required to list all targets associated with a rule.                                                     |
| [PutEvents](../APIReference/API_PutEvents.md "../APIReference/API_PutEvents.md")                                     | `events:PutEvents`             | Required to add custom events that can be matched to rules.                                              |
| [PutPermission](../APIReference/API_PutPermission.md "../APIReference/API_PutPermission.md")                         | `events:PutPermission`         | Required to give another account permission to write events to this account’s default event bus.         |
| [PutRule](../APIReference/API_PutRule.md "../APIReference/API_PutRule.md")                                           | `events:PutRule`               | Required to create or update a rule.                                                                     |
| [PutTargets](../APIReference/API_PutTargets.md "../APIReference/API_PutTargets.md")                                  | `events:PutTargets`            | Required to add targets to a rule.                                                                       |
| [RemovePermission](../APIReference/API_RemovePermission.md "../APIReference/API_RemovePermission.md")                | `events:RemovePermission`      | Required to revoke another account’s permissions for writing events to this account’s default event bus. |
| [RemoveTargets](../APIReference/API_RemoveTargets.md "../APIReference/API_RemoveTargets.md")                         | `events:RemoveTargets`         | Required to remove a target from a rule.                                                                 |
| [TestEventPattern](../APIReference/API_TestEventPattern.md "../APIReference/API_TestEventPattern.md")                | `events:TestEventPattern`      | Required to test an event pattern against a given event.                                                 |
