# Design a FlexMatch matchmaker

This topic provides guidance on how to design a matchmaker that fits your game.

###### Topics

- [Configure a basic matchmaker](#match-configuration-elements "#match-configuration-elements")
- [Choose a location for the
  matchmaker](match-configuration-regions.md "match-configuration-regions.md")
- [Add optional elements](match-configuration-options.md "match-configuration-options.md")

## Configure a basic matchmaker

At a minimum, a matchmaker needs the following elements:

- The **rule set** determines the size and scope of
  teams for a match and defines a set of rules to use when evaluating players for
  a match. Each matchmaker is configured to use one rule set. See [Build a FlexMatch rule set](match-rulesets.md "match-rulesets.md") and [FlexMatch rule set examples](match-examples.md "match-examples.md").
- The **notification target** receives all
  matchmaking event notifications. You need to set up an Amazon Simple
  Notification Service (SNS) topic and then add the topic ID to the matchmaker.
  See more information on setting up notifications at [Set up FlexMatch event notifications](match-notification.md "match-notification.md").
- The **request timeout** determines how long
  matchmaking requests can remain in the request pool and be evaluated for
  potential matches. Once a request has timed out, it has failed to make a match
  and is removed from the pool.
- When using FlexMatch with Amazon GameLift Servers managed hosting, the **game
  session queue** finds the best available resources to host a game
  session for the match, and starts a new game session. Each queue is configured
  with a list of locations and resource types (including Spot or On-Demand
  Instances) that determine where game sessions can be placed. For more
  information on queues, see [Using
  multi-location queues](../../../gamelift/latest/developerguide/queues-intro.md "../../../gamelift/latest/developerguide/queues-intro.md").
