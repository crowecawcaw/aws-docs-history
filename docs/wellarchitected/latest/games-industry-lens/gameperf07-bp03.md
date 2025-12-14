# GAMEPERF07-BP03 Regularly monitor matchmaking

performance

One of the most noticeable ways to optimize the performance of a
game for players is to reduce the time that they must wait before
they can enter a game session. Long wait times can cause players
to lose interest and lead to attrition, so it is important to
consider this when designing your matchmaking solution.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When you are designing your matchmaking configuration for your
game, create rules that determine the conditions that are applied
to form a match. You should consider the impact that these rules
will have on the performance of the system, particularly the wait
times for players. Before deploying changes to your matchmaking
implementation, such as the addition of new matchmaking conditions
or filters, test this beforehand or consider releasing this change
gradually to a small sample population of players as a canary or
A/B test to gather performance metrics before introducing this
change to the entire player population.

Configure your matchmaking service to generate detailed logs to
understand the conditions or rules that were applied to each
matchmaking request. This assists in the review and to adjust
matchmaking implementation as necessary.

For example,
[Amazon GameLift
FlexMatch](../../../gamelift/latest/flexmatchguide/match-intro.md "../../../gamelift/latest/flexmatchguide/match-intro.md") provides a fully managed matchmaking service
which can be used as a standalone service with your own game
server hosting or used with game servers hosted on Amazon
GameLift. FlexMatch can generate event notifications to Amazon EventBridge, see
[Set
up FlexMatch event notifications](../../../gameliftservers/latest/flexmatchguide/match-notification.md "../../../gameliftservers/latest/flexmatchguide/match-notification.md"). Use Amazon Simple Notification Service (Amazon SNS) to receive matchmaking data in
JSON format, allowing you to automatically process and store this
information for analysis to improve matchmaking performance.

Set up metrics to track how long your matchmaking service takes to
find a suitable game session for players. Review matchmaking
duration metrics regularly and correlate these times with player
behavior and community sentiment. Use this data to develop
suitable thresholds for matchmaking timeouts that can be included
in your matchmaking rule configuration.

For example, Amazon GameLift FlexMatch provides support for
defining matchmaking request timeouts as well as creating
matchmaking rules that can
[allow
requirements to relax over time](../../../gamelift/latest/flexmatchguide/match-design-ruleset.md#match-rulesets-components-expansion "../../../gamelift/latest/flexmatchguide/match-design-ruleset.md#match-rulesets-components-expansion"). This feature allows you to
create matchmaking that can adapt to make it straightforward to
create matches and place players into game sessions when matches
are difficult to find.
