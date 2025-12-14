# GAMEOPS03-BP05 Pre-scale infrastructure required to support

peak requirements

Scale infrastructure ahead of large-scale game events to make sure
that you can handle the sudden increase in player demand.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

In addition to new game launches, live games typically run in-game
events, promotions, new content, and season releases as examples
of ways to sustain and improve player engagement. Such activities
experience a high volume of player traffic for the duration of the
event or promotion. The business expects to hit or surpass their
intended targets for the event, and the game infrastructure must
sustain and support them through it.

Prepare your infrastructure ahead of time to be able to support
the anticipated player load that you will experience during large
scale events. To prepare, game operations teams should coordinate
with stakeholders in sales and marketing to estimate the projected
demand that will be generated in an upcoming event by looking at
past player concurrency, engagement metrics, and sales data. If
the event is for a new game launch, game operations teams should
work with these stakeholders to identify realistic projections for
what scale they anticipate. While it may be difficult to predict
how successful a game will become, it is important that everyone
understands what the expectations are for success so that the
infrastructure can be scaled and tested to support those goals.

Many games choose to launch in stages, starting with a soft launch
by opening the game to a small number of players and then
organically scaling the players at every stage, prior to a full
public launch. During the soft launch period, monitor, identify,
track, and resolve issues while refining your projections for the
public launch.

To properly estimate infrastructure requirements, collect data
through load and performance tests run against your game backends
running on production or a production-like staging environment
prior to the game launch. Multiple rounds of these tests should be
run to simulate different conditions of the game and validate that
the backend can withstand the load under most conditions.

To achieve this, developers can write gameplay bots that traverse
various workflows in the game and emulate different conditions.
These tests should inspect the different system layers of the game
backend so that each layer and component is tested and the details
are recorded. Use the data collected from these tests to provision
plan for the game launch.

Single points of failure (SPOF) should be identified and removed
where possible by making the application highly available and
fault tolerant. Use load tests to identify SPOFs by emulating
failures at different upstream and downstream layers and verifying
game and other component behavior.

Along with the necessary estimated infrastructure to be
provisioned for the game launch, in-game event, or promotion
preparations, set up the system to automatically scale on-demand.
Define, configure, and monitor scaling event thresholds to allow
the game backend to scale to sustain a high volume of player
traffic. For variable traffic, pre-provisioning is best because
there may not be enough time to scale-out. Manual scaling might be
required during initial game launches that drive higher than
anticipated demand faster than automated systems can scale
resources.

On AWS, organizations should request higher
[Service Quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") for the services that they use in the game backend.
Service Quotas are set up for accounts to safeguard customers from
inadvertently standing up or scaling more infrastructure than
intended. When a game running in an account hits the upper limit
of the configured service quota in that Region, the service
throttles the requests beyond the provisioned quota and burst
provisions. Throttles can cause unintended or unexpected errors
and impair the player experience. Monitor, track, and regularly
review service quota thresholds for the services used by the game
in-production to avoid throttling. When the usage crosses a
tolerable service quota threshold, an increase in the quota can be
requested by raising
an [Support
Case](../../../awssupport/latest/user/getting-started.md "../../../awssupport/latest/user/getting-started.md") from the Console Support Center, after logging in to
the affected account, or using the
[Support
API](../../../awssupport/latest/APIReference/Welcome.md "../../../awssupport/latest/APIReference/Welcome.md").

For critical events like game launches, content releases,
promotions, and major in-game events, use
[AWS Countdown](https://aws.amazon.com/premiumsupport/aws-countdown-sports/ "https://aws.amazon.com/premiumsupport/aws-countdown-sports/"). Countdown provides implementation guidance based
on playbooks built by Games experts to provide operational
readiness, mitigate potential risks, and plan for capacity
needs. AWS Countdown also has a
[premium
support](https://aws.amazon.com/premiumsupport/aws-countdown/ "https://aws.amazon.com/premiumsupport/aws-countdown/") option that offers enhanced support and options
like engineers to optimize your infrastructure.

If you are launching a game hosted on Amazon GameLift, review
the [pre-launch
checklists](../../../gamelift/latest/developerguide/gamelift_quickstart_customservers_launch.md "../../../gamelift/latest/developerguide/gamelift_quickstart_customservers_launch.md") to prepare.

### Implementation steps

- **Scale infrastructure
  ahead:** Prepare infrastructure in advance for
  large-scale game events to handle sudden increases in player
  demand.
- **Estimate demand:**
  Coordinate with sales and marketing to estimate projected
  demand using past player data and realistic projections.
- **Load testing and SPOF
  removal:** Conduct multiple rounds of load tests to
  validate backend capacity, identify single points of
  failure, and properly configure automated scaling.
