# Reduce game hosting costs with Spot fleets

When hosting multiplayer game servers using Amazon GameLift Servers managed hosting, Spot instances can
provide a cost-effective alternative to On-Demand instances. The Spot pricing model offers
the same hardware and performance as On-Demand but at potentially significant cost savings
(up to 70-90%). However, they come with a limitation: when AWS needs capacity back, it can
reclaim these instances with a two-minute interruption notification.

Amazon GameLift Servers mitigates the risk of interruptions for game server hosting. Amazon GameLift Servers predicts the
likelihood of interruptions on Spot instance types and avoids placing game sessions on any
instances at risk. If a rare interruption does occur, the notification allows you to
gracefully end a game session for players.

## How Amazon GameLift Servers works with Spot fleets

When you set up Spot fleets for game hosting, Amazon GameLift Servers continually evaluates your Spot
fleet instance types and locations for game hosting viability.

- The Spot viability algorithm analyzes recent availability patterns and
  historical interruption rates of Spot instance types by location.
- Based on this analysis, Amazon GameLift Servers identifies Spot instance types and locations
  where there's an unacceptable potential for game session interruption. It takes
  the following actions:
  - It marks the combination of instance type and location as temporarily
    non-viable.
  - It removes any non-viable Spot fleet location from consideration when
    placing new game sessions. As a result, game sessions are only placed in
    Spot fleet locations that have a high likelihood of uninterrupted game
    server hosting.
  - It drains the Spot fleet location of existing instances, even if AWS
    doesn't reclaim them, so you're not paying for instances that can't be
    used for game hosting. If game session protection is turned on,
    instances are shut down only after active game sessions are
    completed.

- Amazon GameLift Servers continually re-evaluates your Spot fleet instance types and
  locations for game hosting viability. When a previously non-viable instance type
  becomes viable again based on updated historical data, you can scale up the Spot
  fleet again, and Amazon GameLift Servers will resume placing game sessions with it.

## Design considerations

When designing your solution to use Spot fleets, consider the following issues:

- **Assess game session length** – The
  average length of your game sessions can impact how well Spot works for your
  game. With shorter game sessions, the faster turnaround keeps game sessions
  running on viable instance types based on the latest historical data. Longer
  game sessions continue to run on instance types without evaluating recent
  viability data, running a greater risk of interruption over time.
- **Evaluate instance type availability** –
  Not every fleet location offers every instance type as Spot. When choosing an
  instance type for your Spot fleet, use the Amazon GameLift Servers console fleet creation tool to
  help you find Spot instance types in the locations you need. With this tool, you
  can select your fleet locations and then view instance type availability across
  those locations.
- **Create multi-location Spot fleets** –
  You can create Spot fleets with multiple locations. A single multi-location Spot
  fleet deploys instances with the same instance type to multiple AWS Regions or
  Local Zones. The Spot viability algorithm evaluates viability based on both instance
  type and location. If a Spot fleet location is evaluated as nonviable, it
  doesn't impact other locations in the fleet, which can still be used to host
  game sessions.
- **Create queues with Spot fleet diversity**
  – If you're using Spot fleets for game hosting, you need to set up a game
  session placement queue. For each new game session request, the queue looks for
  available game hosting resources and selects the best possible option. With Spot
  fleets, you want a queue that can search across multiple fleets that vary in
  both locations and instance types, and you want to include at least one
  On-Demand fleet as backup capacity. A well-designed multi-fleet queue that
  offers diverse placement options is highly resilient against interruptions,
  slowdowns, and outages. For additional guidance on designing a queue for Spot,
  see [Build a queue for Spot Instances](spot-tasks.md "spot-tasks.md").
- **Handle interruptions gracefully** – Set
  up your game server to minimize player impact in the event of a Spot
  interruption. When AWS reclaims a Spot instance, Amazon GameLift Servers passes the termination
  notification to all affected server processes using the server SDK callback
  function `onProcessTerminate()`. Your game needs to implement this
  callback to end the game session gracefully. For more information, see [Respond to a server process shutdown
  notification](gamelift-sdk-server-api.md#gamelift-sdk-server-terminate "gamelift-sdk-server-api.md#gamelift-sdk-server-terminate").

###### Note

AWS makes every effort to provide the notification before it reclaims an
instance, but it's possible that AWS reclaims the Spot Instance before the
warning arrives. You should also prepare your game server to handle
unexpected interruptions.

- **Configure auto-scaling for your backup fleets to
  maintain service during a Spot interruption.** Target-tracking
  auto-scaling maintains a capacity buffer and scales automatically with demand.
  With auto-scaling, backup fleets (Spot or On-Demand) will begin increasing
  capacity whenever they start receiving more game session requests.

To quickly replace lost capacity when a Spot fleet becomes non-viable, a
custom scaling mechanism can use available queue and fleet metrics to initiate a
rapid scale-out of backup fleets. Detect when Spot fleets become non-viable with
metrics such as `FirstChoiceOutOfCapacity`,
`FirstChoiceNotViable`, and
`PercentAvailableGameSessions`. Estimate replacement capacity
needs by analyzing recent `PlacementsStarted` metric data. After
scaling backup fleets to handle immediate demand, normal auto-scaling can take
over.

- **Integration with FlexMatch** – If your
  solution uses a FlexMatch matchmaker, there are no special requirements for Spot
  fleets. You can configure a matchmaker to use a queue with Spot fleets. Amazon GameLift Servers
  automatically prioritizes match placements across Spot and On-Demand fleets,
  including when placing new game sessions and when backfilling empty player slots
  in existing game sessions.
