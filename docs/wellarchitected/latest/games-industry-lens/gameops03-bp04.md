# GAMEOPS03-BP04 Adopt a deployment strategy that minimizes

impact to players

Incorporate a deployment strategy for your game software and
infrastructure that minimizes the amount of downtime that keeps
players out of your game. While certain types of updates might
require installing new updates to the game client, design the game
to minimize or avoid the need for downtime during deployments.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

One of the most important steps to consider when developing a game
deployment strategy is to determine how your game infrastructure
will be managed. Manage your game infrastructure using an
infrastructure as code (IaC) tool such
as [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") or
[Terraform by](https://www.terraform.io/ "https://www.terraform.io/")
[Hashicorp](https://www.terraform.io/ "https://www.terraform.io/") to
reduce human errors during environment preparation. Infrastructure
templates can be deployed and tested in automated pipelines, which
creates consistency in the configuration of different game
environments.

There are several deployment strategies that can be used for a
game:

**Rolling substitution**

The primary objective of a rolling substitution for deployment is
to perform the release without shutting down the game and without
impacting players. It is important that the upgrade or changes
that are to be performed are backward compatible and will work
adjacent to the previous versions of the system.

In this deployment, the server instances are incrementally
replaced (substituted or rolled out) by instances running the
updated version. This rolling substitution can be performed in a
few different ways. For example, to implement rolling updates to a
fleet of dedicated game servers, a typical approach involves
creating a new Auto Scaling group of EC2 instances that contain
the new game server build version deployed onto them, and then
gradually routing players into game sessions hosted on this new
fleet of servers. If there is an associated game client update
that is required as a prerequisite to use the new game server
build, then you must include a validation check to verify that
only players that have this new game client update installed are
routed into these game sessions.

Server fleets (for example, EC2 Auto Scaling groups) containing
the old game server build version are only removed from service
after they are drained of active player sessions in a graceful
manner, typically by setting up individualized-server metrics that
allow game operations teams to automate this process.
Alternatively, to reduce the amount of infrastructure and time to
conduct a rolling deployment, an alternative approach can be
performed where existing production instances are removed from
service, updated with the new game server build, and then placed
back into the production fleet. This approach reduces the amount
of infrastructure that is required, but it also increases risk
since the number of available live game servers for players is
reduced as servers are being replaced.

This model can also be used for performing rolling deployments to
backend services such as databases, caches, and application
servers that don't host gameplay. As long as these services are
deployed in a highly-available manner with multiple clustered
instances, then the complexity of deployments to these services
should be less than deployments to dedicated game servers.

**Blue/green deployment**

The primary objective of a blue/green deployment in a game is to
minimize downtime while also allowing safe rollback to the
previous deployment if issues are identified. It is suitable for
deployments where two versions of the game backend are compatible
and can serve players simultaneously.

In the blue/green deployment strategy, two identical environments
(blue and green) are set up. The existing game version is labeled
as blue, while the new game version that is the deployment target
is labeled as green. When the green environment is ready for
migration, you can configure your routing layer to flip the traffic
over to the green environment while keeping the old environment
(blue) available in case failback is needed. In this scenario, the
routing updates might require updating the matchmaking service to
configure it to begin sending game sessions to the new fleet, or
in the case of game backend services, this could be updating DNS
records in Amazon Route 53 for your service
or [shifting
application load balancer weights](https://aws.amazon.com/blogs/aws/new-application-load-balancer-simplifies-deployment-with-weighted-target-groups/ "https://aws.amazon.com/blogs/aws/new-application-load-balancer-simplifies-deployment-with-weighted-target-groups/") to send traffic to your
new target group.

One of the drawbacks of the blue/green deployment strategy is the
inherent cost of the standby environment due to the additional
infrastructure required while performing the deployment. An option
to mitigate this additional infrastructure cost is to consider
adopting a variant of blue/green deployment where new game
software is deployed onto the same servers that are already
deployed into production. In this scenario, a new green server
process can be started with the new software alongside the
existing blue server process, with the cutover happening between
server processes rather than between separate physical
infrastructure. This approach can also speed up game deployments
across a large amount of infrastructure by removing the need to
wait for new servers to be launched in the cloud. For best
practices on this deployment approach,
see [Blue/Green
Deployments on AWS.](../../../whitepapers/latest/blue-green-deployments/welcome.md "../../../whitepapers/latest/blue-green-deployments/welcome.md")

**Canary deployment**

Canary deployment is useful for game developers, as the strategy
can be applied to release an early alpha or beta build of a game,
or a game feature like a new game mode, map, or challenge to a
restricted or small set of players in-production. Such a
deployment is called a _canary_. The release
may have additional tracking and reporting, so when real players
play that game or feature, their game play telemetry is collected
and analyzed for anomalies and issues.

For new features, the players are not consistently notified about
this, and the game telemetry is the primary source used to
determine if players are experiencing issues and the release
should be rolled-back. At the same time, if no significant issues
are identified, the feature can then be further rolled out to more
players for additional data. If the players are notified, then
they can be asked to provide regular feedback about their
experience. Such test activity would ideally be coordinated by a
live operations team.

As a strategy, canary deployment can also be used for standard
releases to gradually make a new feature available to the players.
A potential advantage over the standard blue/green environment is
that a full-scale second environment is not required. The capacity
of the new scaled-down environment determines how many players are
to be onboarded to the new feature. Before adding more players,
the capacity must be scaled appropriately. Even if this customized
blue/green technique is expected to cost comparatively lesser than
standard blue/green, it is still estimated to incur cost that may
be higher than the rolling substitution technique of canary
deployments.

Run only a single canary on a production environment, and focus it
for its data and feedback. If multiple canaries are deployed, it
complicates troubleshooting and isolating of issues in production
and impairs the quality of the datasets and feedback being
collected.

A variation in the canary is when one or more experiments
(generally UI tests) are run through targeted deployments, where
one set of the game backend servers serve one version of a feature
and another same-sized set serve another version of the same
feature. No additional or special infrastructure is created for
this, and only the chosen pockets of backend servers receive these
updates. The outcome of the experiments is to observe how players
react to each of the versions of the same feature, determine if
there is a consensus of overall like or dislike, and observe if
there are issues identified with its usability or functionality.
Such strategic experiments are also called A/B tests, and the
overall process is called *A/B testing*. On
completion of these experiments, necessary test data is collected
before reverting to the current version of the game backend system
on the servers used for the tests.

**Legacy traditional deployments**

In the traditional style of deployment, during a scheduled
maintenance window the game is shut down and connected players are
dropped or drained before server instances within the game backend
are updated with the latest code builds. This deployment impacts
players each time it is performed, and the players must be
notified ahead of the schedule. As a result, this model causes the
most player impact and should be avoided whenever possible.

After the game update is deployed, the game can be smoke tested
prior to opening the game to the players, who would be waiting for
the game to reopen. This can cause a spike of traffic when players
try to login and play within a short period of time. Therefore, if
the game is not designed to handle such spikes of traffic, you can
choose to gradually allow players back into the game in batches.

Alternatively, you can opt to over-provision the infrastructure to
sustain the opening spike of traffic, and after the game traffic
settles, resources can be scaled down. If necessary, conduct this
type of deployment during off-peak hours when the number of
players is at its lowest. Frequently scheduled maintenance, as
well as extended maintenance, inherently carries a risk of player
attrition and potential loss of revenue. Players also expect
changes after a new release and can lose trust in the game once
returning after a period of downtime.

### Implementation steps

- **Minimize downtime:**
  Implement deployment strategies that reduce downtime and
  keep players in the game.
- **Infrastructure as code
  (IaC):** Use tools like AWS CloudFormation or
  Terraform to manage game infrastructure and reduce human
  errors.
- **Deployment strategies:**
  Use one or a combination of rolling substitution,
  blue/green, and canary deployments to provide smooth updates
  and reduce player impact.
