# Managing an AWS IoT rule

You can use the following actions to manage your AWS IoT rules.

###### In this topic:

- [Tagging a rule](#iot-create-rule-tagging "#iot-create-rule-tagging")
- [Viewing a rule](#iot-view-rules "#iot-view-rules")
- [Deleting a rule](#iot-delete-rule "#iot-delete-rule")

## Tagging a rule

To add another layer of specificity to your new or existing rules, you can apply
tagging. Tagging leverages key-value pairs in your rules to provide you with greater
control over how and where your rules are applied to your AWS IoT resources and
services. For example, you can limit the scope of your rule to only apply in your
beta environment for pre release testing (`Key=environment, Value=beta`)
or capturing all messages sent to the `iot/test` topic from a specific
endpoint only and storing them in an Amazon S3 bucket.

For an example that shows how to grant tagging permissions for a rule,
consider a user that runs the following command to create a rule and tag it
to apply only to their beta environment.

In the example, replace:

- `MyTopicRuleName` with the name of the
  rule.
- `myrule.json` with the name of the policy
  document.

```
aws iot create-topic-rule
    --rule-name `MyTopicRuleName`
    --topic-rule-payload file://`myrule.json`
    --tags "environment=beta"
```

For this example, you must use the following IAM policy:

```
`{
 "Version":"2012-10-17",
 "Statement":
 {
 "Action": [ "iot:CreateTopicRule", "iot:TagResource" ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:iot:us-east-1:123456789012:rule/`MyTopicRuleName`"
 ]
 }
}`

```

The above example shows a newly created rule called `MyTopicRuleName`
that applies only to your beta environment. The `iot:TagResource` in the
policy statement with `MyTopicRuleName` specifically called out allows
tagging when creating or updating `MyTopicRuleName`. The parameter
`--tags "environment=beta"` used when creating the rule limits the
scope of `MyTopicRuleName` to only your beta environment. If you remove
the parameter `--tags "environment=beta"`, then
`MyTopicRuleName` will apply to all environments.

For more information on creating IAM roles and policies specific to an AWS IoT
rule, see [Granting an AWS IoT rule the access it requires](iot-create-role.md "iot-create-role.md")

For general information about tagging your resources, see [Tagging your AWS IoT resources](tagging-iot.md "tagging-iot.md").

## Viewing a rule

Use the [list-topic-rules](../../../cli/latest/reference/iot/list-topic-rules.md "../../../cli/latest/reference/iot/list-topic-rules.md") command to list your rules:

```
`aws iot list-topic-rules`
```

Use the [get-topic-rule](../../../cli/latest/reference/iot/get-topic-rule.md "../../../cli/latest/reference/iot/get-topic-rule.md")
command to get information about a rule:

```
`aws iot get-topic-rule --rule-name `myrule``
```

## Deleting a rule

When you are finished with a rule, you can delete it.

###### To delete a rule (AWS CLI)

Use the [delete-topic-rule](../../../cli/latest/reference/iot/delete-topic-rule.md "../../../cli/latest/reference/iot/delete-topic-rule.md") command to delete a rule:

```
`aws iot delete-topic-rule --rule-name `myrule``
```
