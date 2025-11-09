# Build a queue for Spot Instances

You can achieve of potentially significant savings in hosting costs by using Spot fleets.
For more details about Spot fleets and how to use them, see [On-Demand Instances versus Spot
Instances](gamelift-compute.md#gamelift-compute-spot "gamelift-compute.md#gamelift-compute-spot").

If your game hosting solution includes Spot fleets, you must use a game session placement
queue. Amazon GameLift Servers uses queues to search across multiple game hosting resources and select the
best one available to host a new game session. With Spot fleets, queues are particularly
important for minimizing hosting costs and avoiding possible Spot interruptions. This topic
helps you set up a resilient queue that can continue to host games for players even in the
event of interruptions, slowdowns and outages. You can customize how the queue prioritizes
available hosting resources based on several factors including hosting cost.

Are you using FlexMatch for matchmaking? You can use a queue with Spot fleets to make game
session placements for your matches.

## Implementation tasks for Spot fleets

When creating or updating your game hosting solution to use Spot fleets, complete the
following tasks. For more detailed guidance on how to build a queue that optimizes Spot
availability and resiliency, see [Reduce game hosting costs with Spot fleets](fleets-spot.md "fleets-spot.md") .

1. **Choose and create a set of fleet destinations for your game
   session queue.**

Start by deciding where you want your queue to place game sessions. A queue can
search across multiple fleets to find the best possible placement. Each fleet
has one instance type but can have multiple geographic locations. Queues with
fleets that offer variety in both location and instance type are more likely to
make successful placements. See these best practices for designing an effective
and resilient Spot-optimized queue. 2. **Create your Spot-optimized game session queue.**

Create a queue and configure it for your Spot fleets. See [Create a game session queue](queues-creating.md "queues-creating.md") for help creating
and configuring the new queue. You can use the Amazon GameLift Servers console or the AWS CLI to create or edit a queue.

    * Add the fleet destinations from Step 1.
    * Prioritize the destination order as appropriate. By default, Amazon GameLift Servers
     prioritizes by cost before destination, so destination order is used only
     when the lowest costs between destinations are equal.
    * If you want to prioritize game hosting cost before player latency, provide
     a custom placement priority. See [Prioritize game session placement](queues-design-priority.md "queues-design-priority.md").

3. **Update other components in your solution to use the new
   queue.**

When your solution uses a Spot-optimized queue to start new game sessions, the
queue automatically avoids placing game sessions with fleets that have a high
likelihood of interruption. It instead searches all viable fleets for resources that
match your defined priorities, including player latency, hosting cost, and
destination order.

    * If you're not using FlexMatch – Update your backend service to specify
     the new Spot-optimized queue in game session requests. The backend service
     makes API requests to Amazon GameLift Servers on behalf of your game client (using
     `StartGameSessionPlacement()`), and each request must specify
     a queue name. For help implementing game session placements in your game
     client, see [Create game sessions](gamelift-sdk-client-api.md#gamelift-sdk-client-api-create "gamelift-sdk-client-api.md#gamelift-sdk-client-api-create").
    * If you are using FlexMatch – Update your matchmaking configuration to
     send game session requests to the new Spot-optimized queue. When the
     matchmaking system forms a player match, it sends a game session placement
     request to the designated queue to start a new game session for the match.
     Only matchmaking configurations with FlexMatch mode set to "Managed" can
     designate a placement queue. You can update a matchmaking configuration
     using the AWS CLI or the Amazon GameLift Servers console (see [Edit a matchmaking configuration](../flexmatchguide/match-create-configuration-edit.md "../flexmatchguide/match-create-configuration-edit.md")).

4. **Review the performance of your Spot fleets and
   queues.**

View Amazon GameLift Servers metrics in the Amazon GameLift Servers console or with Amazon CloudWatch to review performance.
For more information about Amazon GameLift Servers metrics, see [Monitor Amazon GameLift Servers with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md"). Key metrics include:

    * Interruption rate – Use the `InstanceInterruptions` and
     `GameSessionInterruptions` metrics to track the number
     and frequency of Spot-related interruptions for instances and game
     sessions. Game sessions on reclaimed instances have a status of
     `TERMINATED` and a status reason of
     `INTERRUPTED`.
    * Queue effectiveness – Track placement success rates, average wait
     time, and queue depth to confirm that Spot fleets don't impact your queue
     performance.
    * Fleet usage – Monitor data on instances, game sessions and player
     sessions. Usage for your On-Demand fleets can be an indicator that queues
     are avoiding placements into your Spot fleets to avoid disruption.

## Best practices for queues with Spot fleets

Use the following best practices when creating fleets and queues for Spot instances.

- **Expand your queue's geographic coverage.** Even
  if your players are clustered in a single AWS Region, add adjacent locations
  to your Spot fleet. This approach improves the queue's ability to maintain
  capacity during regional slowdowns, outages, and Spot interruptions.
  Multi-location fleets work with both Spot and On-Demand instances.
- **Diversify your queue's instance type
  coverage.** Amazon GameLift Servers evaluates Spot viability based on instance type,
  so having Spot fleets with a variety of instance types reduces the chance that
  multiple Spot fleets are nonviable at the same time. Include at least two Spot
  fleets with different instances types each location.

###### Note

Pricing is based on the instances you use, not the number of fleets.
Running five fleets with 10 instances each is the same as running one fleet
with 50 instances of similar cost. Pricing varies by instance type, size,
and location.

Tips for grouping Spot instance types:

    + Use instance types in the same family, such as
     `m6g.medium`, `m6g.large`, and
     `m6g.xlarge`. Larger instance types cost more, but can
     also host more game sessions at a time.
    + Select widely available instances types. Typically, older generation
     families (such as C5, M5, and R5) and common sizes (such as .large,
     .xlarge, and .2xlarge) have better availability.
    + Check the 30-90 day pricing history in the Amazon GameLift Servers console. Look for
     instance types with consistent availability patterns.
    + Use the Amazon GameLift Servers console, fleet creation tool, to explore location
     coverage for instance types.

- **Add On-Demand fleets for backup capacity.**
  Game hosting can switch to On-Demand fleets whenever Spot fleets are
  unavailable. Put at least one On-Demand fleet in each location to maintain low
  player latency. Add auto-scaling to your backup On-Demand fleets, so you can
  keep them scaled down until they're needed.
- **Assign aliases to all fleet destinations.**
  Create aliases for each of your queue's destinations. Aliases make it easier and
  more efficient whenever you need to replace fleets.
- **Apply a queue prioritization strategy.** You
  can customize how a queue prioritizes where to place game sessions (see [Prioritize game session placement](queues-design-priority.md "queues-design-priority.md")
  for more details). For Spot-optimized queues, prioritizing by cost ensures that
  low-cost Spot fleets are used whenever possible.

You can also prioritize certain fleets by specifying a destination order. For
example, some users designate a set of primary fleets for regular use and also a
set of secondary fleets as backup. In this scenario, set the queue's destination
order to list the primary fleets first. Then configure the queue's priority
order with destination followed by cost.
