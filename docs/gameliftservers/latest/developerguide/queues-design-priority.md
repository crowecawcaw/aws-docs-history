# Prioritize game session placement

Amazon GameLift Servers uses an algorithm to determine how to prioritize a queue's destinations and
determine where to place a new game session. The algorithm is based on an ordered set of
criteria. You can use the default priority order, or you can customize the order. You can
edit a queue's priority order at any time.

**Default priority order**

1. **Latency** – If the game session
   placement request includes location-specific latency data for players, Amazon GameLift Servers
   calculates the average player latency in each location and attempts to place a game
   session in a fleet location with the lowest average.
2. **Cost** – If a request doesn't include
   latency data, or if multiple fleets have equal latency, then Amazon GameLift Servers evaluates the
   hosting cost of each fleet. A fleet's hosting cost varies based on fleet type (Spot
   or On-Demand), instance type, and location.
3. **Destination** – If multiple fleets have
   equal latency and costs, then Amazon GameLift Servers prioritizes fleets based on the destination
   order as listed in the queue configuration.
4. **Location** – For queues with
   multi-location fleets, if all other criteria are equal, then Amazon GameLift Servers prioritizes the
   fleet's locations based on alphabetical order.

## Customize how a queue prioritizes game session placements

You can choose to customize how a queue prioritizes the placement criteria. The queue
applies the custom prioritization to all game session placement requests that it
receives.

###### Note

If you create a custom priority configuration and don't include all four criteria, Amazon GameLift Servers
automatically appends any missing criteria in the default order.

**To customize a queue’s priority configuration**

Use the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/") or the
AWS Command Line Interface (AWS CLI) to create a custom priority configuration.

Console
In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"), you can customize a queue's priorities when creating
a new queue or updating an existing queue. Select an AWS Region to work in.

Open the console’s left navigation bar and choose **Queues**.
On the Queues page, select an existing queue and choose
**Edit**.

1. Go to the section **Game session placement priority**. Drag and drop each
   priority criteria to create the order you want.
2. Go to the section **Location order**. Add any locations that you want to
   prioritize. This list is useful when the queue has fleets with
   multiple locations. At a minimum, you must specify one location. The
   locations you specify here are prioritized first, followed by all
   other locations in the queue's destinations.
3. Choose **Save changes**.

AWS CLIUse the [**update-game-session-queue**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-session-queue.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-game-session-queue.html") command with
the `--priority-configuration` option to customize a
queue's priority order. Amazon GameLift Servers updates a queue in your current default AWS Region, or you can add a
`--region` tag to specify a different AWS Region.

The following example request adds or updates the priority configuration for a
specified queue

```
aws gamelift update-game-session-queue \
    --name "example-queue-with-priority"
    --priority-configuration PriorityOrder="COST','LOCATION","DESTINATION",LocationOrder="us-east-1","us-east-2","ca-central-1","us-west-2" \
```

## Prioritize placements by player

latency

If you want to give your players the best possible player experience and ensure minimal latency, take the following steps when setting up your game session placement
system:

- Set your queue to prioritize latency when choosing where to place game sessions. Latency is at the
  top of the priority list by default. You can also customize your queue's priority configuration and choose where to put latency in priority order.
- Set up player latency policies for your queue. Latency policies let you set
  hard limits on the amount of latency to allow in a game session placement. If
  Amazon GameLift Servers can't place a game session without exceeding the limits, the placement
  request will time out and fail. You can set up a single latency policy, or you
  can create a series of policies that gradually relax the latency limit over
  time. With a series of policies, you can specify very low initial latency
  limits, and still accommodate players with higher latencies after a short delay.
  For details on creating latency policies, see [Create a player latency policy](queues-design-latency.md "queues-design-latency.md").
- When making game session placement requests (see [StartGameSessionPlacement](../apireference/API_StartGameSessionPlacement.md "../apireference/API_StartGameSessionPlacement.md")),
  include latency data for each player. Player latency data includes a value for every possible location where a game session might be placed. For example, for a queue that places
  game sessions in AWS Regions us-east-2 and ca-central-1, latency data might look like this:

```
"PlayerLatencies": [
    { "LatencyInMilliseconds": 100, "PlayerId": "player1", "RegionIdentifier": "us-east-2" },
    { "LatencyInMilliseconds": 100, "PlayerId": "player1", "RegionIdentifier": "ca-central-1" },
    { "LatencyInMilliseconds": 150, "PlayerId": "player2", "RegionIdentifier": "us-east-2" },
    { "LatencyInMilliseconds": 150, "PlayerId": "player2", "RegionIdentifier": "ca-central-1" }
  ]
```

To obtain accurate latency measurements, use Amazon GameLift Servers's UDP ping beacons. These
endpoints enable you to measure actual UDP network latency between player devices and
each of the potential hosting locations, resulting in more accurate placement decisions
than using ICMP pings. For more information on using UDP ping beacons to measure latency, refer
to [UDP ping beacons](reference-udp-ping-beacons.md "reference-udp-ping-beacons.md").

## Prioritize placements by location

You can configure a queue to make game session placements based on a prioritized list
of geographic locations. Location is one of the criteria that determines how a queue
chooses where to place a new game session. By default, location is prioritized fourth,
after latency, cost, and destination.

For game session placement, destination and location have somewhat different
meanings:

- _Destination_ refers to a specific fleet and
  includes all the fleet's hosting resources, wherever they're deployed. When
  prioritizing by destination, Amazon GameLift Servers might make a placement with any location in
  the fleet. Multi-location managed fleets and Anywhere fleets can have hosting
  resources that are deployed to one or more locations.
- _Location_ refers to a specific geographic
  position where a fleet's hosting resources are deployed. A fleet can have
  multiple locations, which might include AWS Regions, Local Zones, or custom
  locations (for an Anywhere fleet). A single-location managed fleet has one
  location and it is always an AWS Region. A multi-location managed fleet has a
  home Region and can have remote locations. An Anywhere fleet has one or more
  custom locations.

When prioritizing placements by location, Amazon GameLift Servers looks for any queue
destinations that include the priority location and searches them for an available
hosting resource. If there are multiple destinations with the priority location, Amazon GameLift Servers moves on to the next priority criteria (cost, latency, destination).

There are several ways that you can influence how a queue's locations are prioritized

- Configure how the queue handles all game session placement requests:
  - **Add a priority configuration to the
    queue.** A queue's priority configuration includes an
    ordered list of locations. You can specify one or more locations to
    prioritize. This list doesn't exclude any locations, it simply tells
    Amazon GameLift Servers where to look first for an available hosting resource. A common
    use for an ordered location list is when you want to funnel most traffic
    to one or more specific geographic locations and use additional
    locations as backup capacity. Add a priority configuration by calling
    [UpdateGameSessionQueue](../apireference/API_UpdateGameSessionQueue.md "../apireference/API_UpdateGameSessionQueue.md").
  - **Add a filter configuration to the
    queue.** A filter configuration is an allow list for the
    queue. It tells Amazon GameLift Servers to ignore any locations that aren't on the list
    when looking for an available hosting resource. There are two common
    uses for a filter configuration. First, for fleets with multiple
    locations, you might use a filter to exclude some of the fleet's
    locations. Second, you might want to temporarily disallow placements on
    a certain location; for example, a location might be experiencing
    transitory issues. Because you can update a queue's filter configuration
    at any time, you can easily add and remove locations as needed. Add a
    filter configuration by calling [UpdateGameSessionQueue](../apireference/API_UpdateGameSessionQueue.md "../apireference/API_UpdateGameSessionQueue.md").

- Use special instructions for individual placement requests:
  - **Include a priority override list in a game
    session placement request.** You can provide an alternate
    priority list of locations with any [StartGameSessionPlacement](../apireference/API_StartGameSessionPlacement.md "../apireference/API_StartGameSessionPlacement.md") request. This list effectively
    replaces the queue's configured prioritization for locations for that
    one request only. It doesn't impact any other requests. This override
    feature has a few requirements:
    - Use an override list only with a queue that has a priority
      configuration in place with `LOCATION` as the first
      priority.
    - Don't include player latency data in the same placement
      request. Including latency data sets up conflicts when
      prioritizing locations that Amazon GameLift Servers can't resolve.
    - Decide how you want Amazon GameLift Servers to proceed if it can't find an
      available resource on the priority override list. Choose between
      falling back to the queue's other locations, or limit placements
      to the override list. By default, Amazon GameLift Servers falls back to
      attempt placement on the queue's other locations.
    - Update the queue's filter configuration as needed, such as
      adding locations on the override list. The override list doesn't
      invalidate the filter list.
