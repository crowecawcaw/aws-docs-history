# Tutorial: Create a matchmaker for

standalone FlexMatch

Before creating a matchmaking configuration, [create a rule set](match-create-ruleset.md "match-create-ruleset.md") to use with the matchmaker.

Console

1. Open the Amazon GameLift Servers console at [https://console.aws.amazon.com/gamelift/home](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/").
2. Switch to the AWS Region where you want to create your
   matchmaker. For a list of Regions that support FlexMatch matchmaking
   configurations, see [Choose a location for the
   matchmaker](match-configuration-regions.md "match-configuration-regions.md").
3. In the navigation pane, choose **FlexMatch**,
   **Matchmaking configurations**.
4. On the **Matchmaking configurations** page,
   choose **Create matchmaking configuration**.
5. On the **Define configuration details** page,
   under **Matchmaking configuration details**, do the
   following:
   1. For **Name**, enter a matchmaker name
      that can help you identify it in a list and in metrics. The
      matchmaker name must be unique within the Region.
      Matchmaking requests identify which matchmaker to use by its
      name and Region.
   2. (Optional) For **Description**, add a
      description to help identify the matchmaker.
   3. For **Rule set**, choose a rule set from
      the list to use with the matchmaker. The list contains all
      rule sets that you've created in the current Region.
   4. For **FlexMatch mode**, choose
      **Standalone**. This indicates that you
      have a custom mechanism for starting new game sessions on a
      hosting solution outside of Amazon GameLift Servers.

6. Choose **Next**.
7. On the **Configure settings** page, under
   **Matchmaking settings**, do the
   following:
   1. For **Request timeout**, set the maximum
      amount of time, in seconds, for the matchmaker to complete a
      match for each request. Matchmaking requests that exceed
      this time are rejected.
   2. (Optional) Under **Match acceptance
      options**, for **Acceptance
      required**, if you want to require each player
      in a proposed match to actively accept participation in the
      match, select **Required**. If you select
      this option, then for **Acceptance
      timeout**, set how long, in seconds, you want
      the matchmaker to wait for player acceptances before
      canceling the match.

8. (Optional) Under **Event notification settings**,
   do the following:
   1. (Optional) For **SNS topic**, choose an
      Amazon SNS topic for receiving matchmaking event notifications.
      If you haven't yet set up an SNS topic, you can choose this
      later by editing the matchmaking configuration. For more
      information, see [Set up FlexMatch event notifications](match-notification.md "match-notification.md").
   2. (Optional) For **Custom event data**,
      enter any custom data that you want to associate with this
      matchmaker in event messaging. FlexMatch includes this data in
      every event associated with the matchmaker.

9. (Optional) Under **Tags**, add tags to help you
   manage and track your AWS resources.
10. Choose **Next**.
11. On the **Review and create** page, review your
    choices, and then choose **Create**. Upon
    successful creation, the matchmaker is ready to accept matchmaking
    requests.

AWS CLI
To create a matchmaking configuration with the AWS CLI, open a command line
window and use the [create-matchmaking-configuration](../../../cli/latest/reference/gamelift/create-matchmaking-configuration.md "../../../cli/latest/reference/gamelift/create-matchmaking-configuration.md") command to define a new
matchmaker.

This example command creates a new matchmaking configuration for a
standalone matchmaker that requires player acceptance.

```
aws gamelift create-matchmaking-configuration \
    --name "SampleMatchamker123" \
    --description "The sample test matchmaker with acceptance" \
    --flex-match-mode STANDALONE \
    --rule-set-name "MyRuleSetOne" \
    --request-timeout-seconds 120 \
    --acceptance-required \
    --acceptance-timeout-seconds 30 \
    --notification-target "arn:aws:sns:us-west-2:111122223333:My_Matchmaking_SNS_Topic"
```

If the matchmaking configuration creation request is successful, Amazon GameLift Servers
returns a [MatchmakingConfiguration](../apireference/API_MatchmakingConfiguration.md "../apireference/API_MatchmakingConfiguration.md") object with the settings that you
requested for the matchmaker. The new matchmaker is ready to accept
matchmaking requests.
