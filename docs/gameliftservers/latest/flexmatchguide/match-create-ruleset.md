# Tutorial: Create a matchmaking rule set

Before you create a matchmaking rule set for your Amazon GameLift Servers FlexMatch matchmaker, we recommend
checking the [rule set syntax](match-rules-reference.md "match-rules-reference.md"). After you create
a rule set using the Amazon GameLift Servers console or the AWS Command Line Interface (AWS CLI), you can't change it.

Note that there is a [service quota](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/ "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/") for the maximum
number of rule sets that you can have in an AWS Region, so it's a good idea to delete
unused rule sets.

###### Topics

Console

###### Create a rule set

1. Open the Amazon GameLift Servers console at [https://console.aws.amazon.com/gamelift/](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/").
2. Switch to the AWS Region where you want to create your rule set.
   Define rule sets in the same Region as the matchmaking configuration
   that uses them.
3. In the navigation pane, choose **FlexMatch**,
   **Matchmaking rule sets**.
4. On the **Matchmaking rule sets** page, choose
   **Create rule set**.
5. On the **Create matchmaking rule set** page, do the
   following:
   1. Under **Rule set settings**, for
      **Name**, enter a unique descriptive name
      that you can use to identify it in a list or in events and
      metrics tables.
   2. For **Rule set**, enter your rule set in
      JSON. For information about designing a rule set, see [Design a FlexMatch rule set](match-design-ruleset.md "match-design-ruleset.md"). You can also use one
      of the example rule sets from [FlexMatch rule set examples](match-examples.md "match-examples.md").
   3. Choose **Validate** to verify that the syntax
      of your rule set is correct. You can't edit rule sets after
      they're created, so it's a good idea to validate them
      first.
   4. (Optional) Under **Tags**, add tags to help
      you manage and track your AWS resources.

6. Choose **Create**. If creation is successful, you can
   use the rule set with a matchmaker.

AWS CLI
**Create a rule set**

Open a command line window and use the command [create-matchmaking-rule-set](../../../cli/latest/reference/gamelift/create-matchmaking-rule-set.md "../../../cli/latest/reference/gamelift/create-matchmaking-rule-set.md").

This example command creates a simple matchmaking rule set that sets up a
single team. Be sure to create the rule set in the same AWS Region as the
matchmaking configurations that uses it.

```
aws gamelift create-matchmaking-rule-set \
    --name "SampleRuleSet123" \
    --rule-set-body '{"name": "aliens_vs_cowboys", "ruleLanguageVersion": "1.0", "teams": [{"name": "cowboys", "maxPlayers": 8, "minPlayers":  4}]}'
```

If the creation request is successful, Amazon GameLift Servers returns a [MatchmakingRuleSet](../apireference/API_MatchmakingRuleSet.md "../apireference/API_MatchmakingRuleSet.md") object that includes the settings that you
specified. A matchmaker can now use the new rule set.

Console

###### Delete a rule set

1. Open the Amazon GameLift Servers console at [https://console.aws.amazon.com/gamelift/](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/").
2. Switch to the Region that you created the rule set in.
3. In the navigation pane, choose **FlexMatch**,
   **Matchmaking rule sets**.
4. On the **Matchmaking rule sets** page, select the
   rule set that you want to delete, and then choose
   **Delete**.
5. In the **Delete rule set** dialog box, choose
   **Delete** to confirm deletion.

###### Note

If a matchmaking configuration is using the rule set, Amazon GameLift Servers
displays an error message (**Can't delete rule
set**). If this occurs, change the matchmaking
configuration to use a different rule set, then try again. To find
out which matchmaking configurations are using a rule set, choose
the name of a rule set to view its details page.

AWS CLI
**Delete a rule set**

Open a command line window and use the command [delete-matchmaking-rule-set](../../../cli/latest/reference/gamelift/delete-matchmaking-rule-set.md "../../../cli/latest/reference/gamelift/delete-matchmaking-rule-set.md") to delete a matchmaking rule
set.

If a matchmaking configuration is using the rule set, Amazon GameLift Servers returns an error
message. If this occurs, change the matchmaking configuration to use a different
rule set, then try again. To get a list of which matchmaking configurations are
using a rule set, use the command [describe-matchmaking-configurations](../../../cli/latest/reference/gamelift/describe-matchmaking-configurations.md "../../../cli/latest/reference/gamelift/describe-matchmaking-configurations.md") and specify the rule set
name.

This example command checks for the matchmaking rule set's usage and then
deletes the rule set.

```
aws gamelift describe-matchmaking-rule-sets \
    --rule-set-name "SampleRuleSet123" \
    --limit 10

aws gamelift delete-matchmaking-rule-set \
    --name  "SampleRuleSet123"
```
