# Queue configuration examples

This topic provides example queue configurations for common game hosting scenarios. Each
example includes the complete AWS Command Line Interface (AWS CLI) command and an explanation of when to use that
configuration. For instructions on creating a queue, see [Create a game session queue](queues-creating.md "queues-creating.md"). For more information about customizing queue
behavior, see [Customize a game session queue](queues-design.md "queues-design.md").

## Latency-optimized queue for competitive games

**Use case:** You host a competitive multiplayer
game (such as a first-person shooter or fighting game) where low latency is critical to
fair gameplay. Players are distributed globally and you want to place game sessions as
close to players as possible.

**Strategy:** Prioritize latency first (the default) and
add player latency policies that enforce strict limits. Use graduated latency policies
to give the queue time to find ideal placements before relaxing limits. Set the
strictest tier to your game's target latency (this example uses 50 ms). Include player
latency data in every placement request.

```
aws gamelift create-game-session-queue \
    --name "competitive-fps-global" \
    --timeout-in-seconds 300 \
    --destinations \
        DestinationArn="arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-1a2b3c4d-na-east" \
        DestinationArn="arn:aws:gamelift:us-west-2:111122223333:fleet/fleet-2b3c4d5e-na-west" \
        DestinationArn="arn:aws:gamelift:eu-west-1:111122223333:fleet/fleet-3c4d5e6f-eu" \
        DestinationArn="arn:aws:gamelift:ap-northeast-1:111122223333:fleet/fleet-4d5e6f7g-apac" \
    --player-latency-policies \
        "MaximumIndividualPlayerLatencyMilliseconds=50,PolicyDurationSeconds=90" \
        "MaximumIndividualPlayerLatencyMilliseconds=80,PolicyDurationSeconds=60" \
        "MaximumIndividualPlayerLatencyMilliseconds=120,PolicyDurationSeconds=60" \
        "MaximumIndividualPlayerLatencyMilliseconds=150" \
    --priority-configuration PriorityOrder="LATENCY","COST"
```

**Key configuration choices:**

- **LATENCY as first priority** – Amazon GameLift Servers
  calculates the average latency for all players in the request and places the
  game session in the location with the lowest average. This is the default
  behavior when `PlayerLatencies` are provided.
- **Graduated latency policies** – The queue
  waits up to 90 seconds for capacity in any location where all players have
  under 50 ms latency. If no location satisfies the policy for all players,
  Amazon GameLift Servers skips to the next tier immediately rather than waiting. The policies
  then relax to 80 ms, 120 ms, and finally 150 ms. This reduces the likelihood
  of high-latency placements while still finding a placement.
- **Fleets in multiple Regions** – Global
  coverage ensures that players in any Region can find a low-latency
  placement. Multi-location fleets extend this coverage to locations beyond
  the Regions that have Amazon GameLift Servers API endpoints. See [Amazon GameLift Servers service locations](gamelift-regions.md "gamelift-regions.md") for the full list of supported
  locations.

###### Important

Latency-based placement works only when your placement requests include player
latency data. Your game client must measure latency to each potential hosting
location using Amazon GameLift Servers [UDP ping beacons](reference-udp-ping-beacons.md "reference-udp-ping-beacons.md") and include the results in
the [StartGameSessionPlacement](../apireference/API_StartGameSessionPlacement.md "../apireference/API_StartGameSessionPlacement.md") request. Without latency data, Amazon GameLift Servers skips
the latency priority and moves to the next criterion.

## Hybrid cost and latency queue

**Use case:**
You want to minimize hosting costs and ensure that all players stay within an acceptable latency range.
Define your acceptable latency range using a target latency (for example, 50 ms). Any latency at or
below the target is acceptable.

**Strategy:** Prioritize cost over latency but add a
latency policy that enforces your target threshold. Amazon GameLift Servers picks the cheapest location
that satisfies the latency policy. For example, Amazon GameLift Servers chooses a 49 ms location over a
25 ms location if it costs less. The latency policy expands eligible low-cost locations.
This reduces your overall hosting cost and maintains acceptable gameplay quality.

```
aws gamelift create-game-session-queue \
    --name "competitive-cost-aware" \
    --timeout-in-seconds 300 \
    --destinations \
        DestinationArn="arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-1a2b3c4d-spot-east" \
        DestinationArn="arn:aws:gamelift:us-west-2:111122223333:fleet/fleet-2b3c4d5e-spot-west" \
        DestinationArn="arn:aws:gamelift:eu-west-1:111122223333:fleet/fleet-3c4d5e6f-spot-eu" \
        DestinationArn="arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-4d5e6f7g-ondemand-east" \
    --player-latency-policies \
        "MaximumIndividualPlayerLatencyMilliseconds=50,PolicyDurationSeconds=120" \
        "MaximumIndividualPlayerLatencyMilliseconds=100" \
    --priority-configuration PriorityOrder="COST","LATENCY"
```

**Key configuration choices:**

- **Latency policies set the target latency**
  – The first tier accepts placements only where all players have under
  the target latency (50 ms). If no location satisfies the policy for all
  players, Amazon GameLift Servers skips to the next tier immediately. After 120 seconds, the
  policy relaxes to allow up to 100 ms to ensure players find a placement when
  capacity is constrained.
- **COST before LATENCY in priority order**
  – In this example, the lowest latency does not matter as long as it
  stays below the target threshold. `COST` first ensures that a cheaper location at
  49 ms is chosen over a more expensive location at 25 ms. However, a cheaper
  location at 51 ms is not chosen over a more expensive location at 49 ms
  until relaxing to the second tier.

###### Important

This approach requires player latency data in every placement request. Without
latency data, the latency policy has nothing to evaluate and all locations are
eligible, which causes the queue to behave as purely cost-optimized.

## Cost-optimized queue with Spot Instances

**Use case:** You want to minimize hosting costs for a
casual or non-latency-sensitive game. Your players are located primarily in one area,
or your players can tolerate moderate latency (under 150 ms).

**Strategy:** Prioritize cost first to prefer the cheapest
available hosting, which is typically a Spot fleet. Include On-Demand fleets as fallback
for when Spot capacity is unavailable. Use multiple Spot fleets with different instance
types to increase the chance that at least one Spot fleet stays viable and provides
reduced costs.

###### Important

This queue does not consider player latency when placing game sessions. Do not use this
configuration if players need to be placed in a location based on their latency.

```
aws gamelift create-game-session-queue \
    --name "cost-optimized-na" \
    --timeout-in-seconds 300 \
    --destinations \
        DestinationArn="arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-1a2b3c4d-spot-c5large" \
        DestinationArn="arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-2b3c4d5e-spot-c5xlarge" \
        DestinationArn="arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-3c4d5e6f-ondemand-c5large" \
    --priority-configuration PriorityOrder="COST",LocationOrder="us-east-1","us-west-2","ca-central-1"
```

**Key configuration choices:**

- **COST as first priority** – Amazon GameLift Servers
  picks the cheapest available fleet first. Spot fleets are typically 50–70%
  cheaper than On-Demand. This priority order is the default behavior when
  `PlayerLatencies` are not provided.
- **Multiple Spot fleets with different instance
  types** – If a Spot instance type has high risk for interruption,
  Amazon GameLift Servers marks that fleet as non-viable and attempts the other Spot fleet. Having
  variety in instance types (c5.large and c5.xlarge) reduces the risk of all Spot
  fleets being unavailable at the same time.
- **On-Demand fleet for backup** –
  Provides guaranteed capacity when Spot is unavailable. Because cost is
  prioritized first, Amazon GameLift Servers uses On-Demand only when Spot fleets are non-viable or
  at capacity.
- **Non-viable Spot fleets as a last resort**
  – If there is no available capacity on a viable Spot fleet or an
  On-Demand fleet, Amazon GameLift Servers places requests on non-viable Spot capacity.

## Resilient multi-Region failover queue

**Use case:** You need high availability for your game.
If one AWS Region experiences an issue or capacity constraints, you want game session
placement to automatically fail over to another Region without player-visible
disruption.

**Strategy:** Use multi-location fleets with different
home Regions so that a regional issue does not affect all your fleets. For example,
two fleets that each have us-east-1, us-west-2, and ca-central-1 locations. Use a filter
configuration to control which locations are active. Disable locations during an
issue. This example can be combined with any of the other examples to provide resilience.

```
aws gamelift create-game-session-queue \
    --name "resilient-na-queue" \
    --timeout-in-seconds 300 \
    --destinations \
        DestinationArn="arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-1a2b3c4d-primary-spot" \
        DestinationArn="arn:aws:gamelift:us-west-2:111122223333:fleet/fleet-2b3c4d5e-secondary-spot" \
        DestinationArn="arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-3c4d5e6f-primary-ondemand" \
        DestinationArn="arn:aws:gamelift:us-west-2:111122223333:fleet/fleet-4d5e6f7g-secondary-ondemand" \
    --filter-configuration "AllowedLocations=us-east-1,us-west-2,ca-central-1"
```

**Key configuration choices:**

- **Can be combined with other examples' priorities** –
  This example does not specify a priority order and can be applied on top of
  any other example. Adjust the filter configuration to include locations
  relevant to your setup.
- **Fleets with at least two different home
  Regions** – If us-east-1 experiences a regional issue, the
  fleet with home Region us-west-2 remains operational. A fleet's home Region is
  where its control plane resides. If that Region is unavailable, the fleet cannot
  accept new game sessions.
- **Filter configuration as an operational lever**
  – You can update the filter configuration at any time to remove a
  location that is experiencing issues. For example, if ca-central-1 is impacted, call
  `update-game-session-queue` to remove it from the allowed
  locations list. This immediately stops new placements in that location without
  changing any other queue configuration.

###### Tip

Use at least two multi-location fleets with different home Regions. This ensures
that a single regional issue does not prevent all new game session placements. Use
auto-scaling policies so fleets in the secondary Region can absorb traffic when
the primary Region is unavailable.

## Queue for FlexMatch matchmaking

**Use case:** You use Amazon GameLift Servers FlexMatch to match players
into game sessions. FlexMatch sends placement requests to a queue after forming a match.
The queue must handle latency data from the matchmaker and place sessions quickly to
avoid long player wait times.

**Strategy:** Use the default latency-first priority so
that matched players get low-latency sessions. Set a moderate timeout that aligns with
your matchmaking ticket timeout. Add latency policies to avoid placing matched players
in sessions with poor latency. Your queue's latency policies must align with the
latency constraints in your matchmaking rule set to avoid excess wait time.

```
aws gamelift create-game-session-queue \
    --name "matchmaker-queue" \
    --timeout-in-seconds 300 \
    --destinations \
        DestinationArn="arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-1a2b3c4d-spot-east" \
        DestinationArn="arn:aws:gamelift:us-west-2:111122223333:fleet/fleet-2b3c4d5e-spot-west" \
        DestinationArn="arn:aws:gamelift:eu-west-1:111122223333:fleet/fleet-3c4d5e6f-spot-eu" \
        DestinationArn="arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-4d5e6f7g-ondemand-east" \
    --player-latency-policies \
        "MaximumIndividualPlayerLatencyMilliseconds=75,PolicyDurationSeconds=60" \
        "MaximumIndividualPlayerLatencyMilliseconds=100,PolicyDurationSeconds=60" \
        "MaximumIndividualPlayerLatencyMilliseconds=150"
```

**Key configuration choices:**

- **Queue timeout shorter than matchmaking
  timeout** – Set the queue timeout to less than your
  FlexMatch matchmaking configuration timeout. If the queue times out, FlexMatch
  can retry the placement or return the ticket to the matchmaking pool. This example
  uses a 10-minute matchmaking timeout and a 5-minute queue timeout.
- **Latency policies aligned with game
  requirements** – FlexMatch includes player latency data in
  placement requests automatically. FlexMatch rules support matching players based
  on latency requirements. The latency policies on the queue must align with
  the FlexMatch rules to ensure the latency requirements are met.

###### Note

When using FlexMatch, you do not call `StartGameSessionPlacement`
directly. Instead, configure your matchmaking configuration to reference this queue.
FlexMatch automatically sends placement requests to the queue after forming a match.
Update your matchmaking configuration using the Amazon GameLift Servers console or by calling [UpdateMatchmakingConfiguration](../apireference/API_UpdateMatchmakingConfiguration.md "../apireference/API_UpdateMatchmakingConfiguration.md") with the queue ARN.

## Per-request location override

**Use case:** Your game uses a custom matchmaker that has
already determined the best Region for a group of players, based on
their latency, their selected geographic area, or an in-game event such as
a tournament.

**Strategy:** Set `LOCATION` as the first
queue priority—this is a prerequisite for location overrides to work. You
cannot use overrides on a queue that prioritizes latency or cost first. Then use the
`PriorityConfigurationOverride` parameter in individual
`StartGameSessionPlacement` requests to specify the preferred locations
for that request.

First, create the queue with location as the top priority:

```
aws gamelift create-game-session-queue \
    --name "global-queue-with-overrides" \
    --timeout-in-seconds 300 \
    --destinations \
        DestinationArn="arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-1a2b3c4d-na" \
        DestinationArn="arn:aws:gamelift:eu-west-1:111122223333:fleet/fleet-2b3c4d5e-eu" \
        DestinationArn="arn:aws:gamelift:ap-northeast-1:111122223333:fleet/fleet-3c4d5e6f-apac" \
    --priority-configuration PriorityOrder="LOCATION",LocationOrder="us-east-1","eu-west-1","ap-northeast-1"
```

Then, when placing a game session for a player who registered for the Europe
tournament, override the location priority to restrict placement to that Region:

```
aws gamelift start-game-session-placement \
    --game-session-queue-name "global-queue-with-overrides" \
    --placement-id "tournament-match-001" \
    --maximum-player-session-count 10 \
    --priority-configuration-override LocationOrder="eu-west-1",PlacementFallbackStrategy="NONE"
```

**Key configuration choices:**

- **LOCATION as first queue priority** –
  Required for per-request location overrides to work. The override replaces the
  queue's location order for that single request only. Providing location
  overrides on `StartGameSessionPlacement` without `LOCATION` as the first
  priority causes an `InvalidRequestException`.
- **PlacementFallbackStrategy** – Controls
  what happens if no capacity is available in the override locations.
  `NONE` means the placement attempts only the override
  locations until it times out—appropriate for tournaments where Region matters.
  `DEFAULT_AFTER_SINGLE_PASS` means Amazon GameLift Servers tries the override
  locations first, then falls back to the queue's other locations—use
  this when your matchmaker has a location preference but you want the queue
  to find capacity elsewhere if needed.
  If not specified, the default is `DEFAULT_AFTER_SINGLE_PASS`.
- **No player latency data with overrides**
  – A placement request that uses a location override does not accept
  `PlayerLatencies`. Including them causes an
  `InvalidRequestException`.
- **Filter configuration still applies**
  – If the queue has a `FilterConfiguration`, it continues to
  filter locations even when a location override is provided. Locations excluded
  by the filter are not eligible for placement regardless of whether they appear
  in the override.

## Queue with Anywhere fleets

**Use case:** You host game servers on your own
hardware (on-premises servers, other cloud providers, or edge devices) using Amazon GameLift Servers
Anywhere fleets. You want to use a queue to place game sessions across your custom
compute resources, optionally combined with Amazon GameLift Servers managed fleets for overflow
capacity.

**Strategy:** Register your hardware as compute in an
Anywhere fleet with custom locations that represent your physical sites. When you create
the Anywhere fleet, assign the fleet a representative cost. For on-premises servers,
consider a cost of 0.0 to represent already-purchased hardware. Use `COST`
priority to direct traffic to your cheaper on-premises servers, or use
`LATENCY` priority to place sessions based on proximity to your custom
locations.

First, create custom locations and an Anywhere fleet with a cost of 0.0:

```
aws gamelift create-location \
    --location-name "custom-location-dallas"

aws gamelift create-location \
    --location-name "custom-location-chicago"

aws gamelift create-fleet \
    --name "on-prem-anywhere-fleet" \
    --compute-type ANYWHERE \
    --locations "Location=custom-location-dallas" "Location=custom-location-chicago" \
    --anywhere-configuration "Cost=0.0"
```

Then, create a queue that directs traffic to your Anywhere fleet with a managed fleet
as overflow:

```
aws gamelift create-game-session-queue \
    --name "hybrid-anywhere-queue" \
    --timeout-in-seconds 300 \
    --destinations \
        DestinationArn="arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-1a2b3c4d-anywhere" \
        DestinationArn="arn:aws:gamelift:us-east-1:111122223333:fleet/fleet-2b3c4d5e-managed-ondemand" \
    --priority-configuration PriorityOrder="COST",LocationOrder="custom-location-dallas","custom-location-chicago","us-east-1" \
    --filter-configuration "AllowedLocations=custom-location-dallas,custom-location-chicago,us-east-1"
```

**Key configuration choices:**

- **Custom locations in LocationOrder** –
  Anywhere fleets use custom location names that you define when you create the
  fleet (for example, `custom-location-dallas`). These custom
  locations work in priority and filter configurations the same way as AWS
  Regions.
- **Managed fleet as overflow** – If your
  on-premises hardware reaches capacity, the queue falls back to the managed
  On-Demand fleet in us-east-1. This provides burst capacity without
  provisioning additional hardware.
- **Player latency to custom locations**
  – If you use latency-based placement, players must report latency to
  the custom location names (for example, `custom-location-dallas`).
- **Filter includes both custom and AWS
  locations** – If you use the filter, it must list every
  location where you want placements to occur. The Anywhere fleet's home Region
  does not implicitly include its custom locations in the filter, so you must
  list each custom location explicitly.
