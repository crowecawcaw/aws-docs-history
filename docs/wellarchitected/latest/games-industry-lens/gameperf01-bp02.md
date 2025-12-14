# GAMEPERF01-BP02 Consider operational overhead for scaling game

servers

Consider the management and operational overhead associated with
each hosting option.

Level of risk exposed if this best practice is not established: High

## Implementation guidance

**Operational overhead**

Self-hosted solutions on EC2 or containers
can provide more control but also will require more management.
Container orchestrators like ECS or EKS can reduce launch times
for containerized servers while also increasing networking
complexity and maintenance orchestration overhead.

As an example,
[EKS
managed node groups](../../../eks/latest/userguide/managed-node-groups.md "../../../eks/latest/userguide/managed-node-groups.md") can automate provisioning and lifecycle
management of your game servers but do not respect pod disruption
budgets when terminating a node, if your game requires longer than
the 15 minute termination period to safely complete games, you may
need to create lifecycle hooks or consider self-managed nodes with
custom controllers to block game interruption.

Managed services like Amazon Game Lift may handle most of the
operational overhead but reduce the amount of visibility and
control over special requirements for low level networking and
security configuration. Choosing a game server solution is a
trade-off between the level of customization, control and
responsibility you will have for tuning game server performance
and scaling behavior.

### Implementation steps

- Assess operational overhead for hosting options, balancing
  control and management effort between self-hosted solutions
  like EC2, ECS, or EKS and managed services like Amazon Game
  Lift.
- Use EKS managed node groups for automation but implement
  lifecycle hooks or custom controllers if your game servers
  require longer termination periods than the default.
- Weigh the trade-offs between customization, visibility, and
  operational responsibility when selecting a game server
  solution.
