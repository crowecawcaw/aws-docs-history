# Create a game session queue

Queues are used to place new game sessions across multiple fleets and locations. Your game
starts new game sessions by submitting placement requests to a queue. A queue is configured
with instructions for how to process requests. Learn more about initiating game session
placement requests in [Create game sessions](gamelift-sdk-client-api.md#gamelift-sdk-client-api-create "gamelift-sdk-client-api.md#gamelift-sdk-client-api-create").

**To create a game session queue**

These instructions illustrate how to create a simple working queue with minimal
configuration settings and default settings. There are a number of options for customizing a
queue configuration. These options help you make the best possible placements based on the
needs of your game. To learn more about customizing queues for your game, see [Customize a game session queue](queues-design.md "queues-design.md"). You can update most queue
configuration settings at any time.

You can create a game session queue using either the Amazon GameLift Servers console or the AWS
CLI.

Console
In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"),
select an AWS Region to work in. Open the console’s left navigation bar and
choose **Queues**.

1. On the **Queues** page, choose **Create
   queue** to start the workflow.
2. Under **Queue settings** enter the following
   settings:
   1. Enter a queue name. This name must be unique to the AWS Region that you're creating the queue in.
   2. Keep the default **Timeout** setting, which
      is 600 seconds (or 10 minutes). This value controls how long
      Amazon GameLift Servers tries to place a new game session before stopping. Amazon GameLift Servers
      searches for available resources until the request times out.
      You can update a queue's timeout setting at any time.
   3. Skip the **Player latency policies** section.
      A queue uses latency policies only when it receives placement
      requests that include player latency data. You can add latency
      policies to a queue at any time. For more on creating latency
      policies, see [Create a player latency policy](queues-design-latency.md "queues-design-latency.md").

3. Skip the **Game session placement locations** section
   to use the default setting of **All locations**. This
   setting lets you create an allow list of locations where the queue can
   make placements (also called a filter
   configuration). For more about prioritizing by location and filter
   configurations, see
   [Prioritize placements by location](queues-design-priority.md#queues-design-priority-custom-location "queues-design-priority.md#queues-design-priority-custom-location").
4. Under **Destination order**, add one or more fleets
   to the queue. You can identify fleets by using fleet IDs or ARNs, or by
   using a fleet alias. When adding multiple fleets, keep in mind that they
   should all be running similar game builds and be compatible with any
   game client that uses this queue. In addition, all fleets in a queue
   must have the same certificate configuration.
   1. Select the **Region** where the fleet or
      alias was created. For a multi-location fleet, this is the
      "home" region.
   2. For destination **Type**, select either a
      fleet or an alias.
   3. Your region and type selections populate a dropdown list of
      existing fleets or aliases. Select one to designate as a queue
      destination.
   4. To specify another fleet or alias for the queue, choose
      **Add destination** and repeat the previous
      steps.
   5. After you've added a list of destinations, use the
      drag-and-drop feature to reorder the destinations. Amazon GameLift Servers uses
      this order when prioritizing placements by destination.

5. Skip the **Game session placement priority** section
   to keep the default priority order. This setting lets you customize how
   Amazon GameLift Servers chooses where to look for available hosting resources for new game
   session placements. For more information about prioritizing placements,
   see [Prioritize game session placement](queues-design-priority.md "queues-design-priority.md"). You can update a queue's
   placement priorities at any time.
6. Under **Location order**, keep the default values.
   This setting is used when prioritizing by fleet location. It provides
   location order to use. When using the default priority settings,
   location is used as a tiebreaker when the preferred destination is a
   fleet with multiple locations.
7. Skip the optional **Event notification settings**
   section. Event notifications are required for queues that process a high
   volume of placement requests. For queues that process low volumes, such
   as for development or testing purposes, you can track the status of
   placement requests by polling with[DescribeGameSessionPlacement](../../../https:/docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeGameSessionPlacement.md "../../../https:/docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeGameSessionPlacement.md"). For more details, see [Set up event notification for game session
   placement](queue-notification.md "queue-notification.md").
   You can update a queue's event notification settings at any time.
8. Choose **Create** to generate a new queue with
   minimal customization.

AWS CLI

###### Example Create a queue

The following example creates a game session queue with these
configurations:

- A five minute timeout.
- Two fleet destinations.
- Filter to only allow placements in these locations:
  `us-east-1`, `us-east-2`.
  `us-west-2`, and `ca-central-1`.
- Priority order based on cost and then locations in a specified
  order.

```
aws gamelift create-game-session-queue \
    --name "sample-test-queue" \
    --timeout-in-seconds 300 \
    --destinations DestinationArn="arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-772266ba-8c82-4a6e-b620-a74a62a93ff8" DestinationArn="arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-33f28fb6-aa8b-4867-85b4-ceb217bf5994" \
    --filter-configuration "AllowedLocations=us-east-1, ca-central-1, us-east-2, us-west-2" \
    --priority-configuration PriorityOrder="COST","LOCATION",LocationOrder="us-east-1","us-east-2","ca-central-1","us-west-2" \
    --notification-target "arn:aws:sns:us-east-1:111122223333:gamelift-test.fifo"
```

###### Note

You can get fleet and alias ARN values by calling either [describe-fleet-attributes](../../../cli/latest/reference/gamelift/describe-fleet-attributes.md "../../../cli/latest/reference/gamelift/describe-fleet-attributes.md") or [describe-alias](../../../cli/latest/reference/gamelift/describe-alias.md "../../../cli/latest/reference/gamelift/describe-alias.md")
with the fleet or alias ID.

If the `create-game-session-queue` request is successful, Amazon GameLift Servers
returns a [GameSessionQueue](../../../gamelift/latest/apireference/API_GameSessionQueue.md "../../../gamelift/latest/apireference/API_GameSessionQueue.md") object with the new queue configuration. You can
now submit requests to the queue using [StartGameSessionPlacement](../../../gamelift/latest/apireference/API_StartGameSessionPlacement.md "../../../gamelift/latest/apireference/API_StartGameSessionPlacement.md").

###### Example Create a queue with player latency policies

The following example creates a game session queue with these
configurations:

- A ten minute timeout
- Three fleet destinations
- A set of player latency policies

```
aws gamelift create-game-session-queue \
    --name "matchmaker-queue" \
    --timeout-in-seconds 600 \
    --destinations DestinationArn=arn:aws:gamelift:us-east-1::alias/alias-a1234567-b8c9-0d1e-2fa3-b45c6d7e8910 \
               DestinationArn=arn:aws:gamelift:us-west-2::alias/alias-b0234567-c8d9-0e1f-2ab3-c45d6e7f8901 \
               DestinationArn=arn:aws:gamelift:us-west-2::fleet/fleet-f1234567-b8c9-0d1e-2fa3-b45c6d7e8912 \
    --player-latency-policies "MaximumIndividualPlayerLatencyMilliseconds=50,PolicyDurationSeconds=120" \
               "MaximumIndividualPlayerLatencyMilliseconds=100,PolicyDurationSeconds=120" \
               "MaximumIndividualPlayerLatencyMilliseconds=150" \
```

If the `create-game-session-queue` request is successful, Amazon GameLift Servers
returns a [GameSessionQueue](../../../gamelift/latest/apireference/API_GameSessionQueue.md "../../../gamelift/latest/apireference/API_GameSessionQueue.md") object with the new queue configuration.
