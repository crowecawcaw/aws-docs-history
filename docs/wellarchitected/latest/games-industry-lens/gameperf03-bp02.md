# GAMEPERF03-BP02 Test performance and scalability of game

servers

To test the performance and scalability of your game servers,
implement a robust testing framework using the Amazon GameLift
features and the GameLift Testing Toolkit.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Key practices include:

Iterative testing

Use an Amazon GameLift Anywhere fleet to create a cloud-based
hosted environment where you can iteratively build and test game
components. This environment should mirror real-world hosting
conditions, enabling realistic performance and scalability
testing.

Game server integration testing

Test the integration of your game server with the Amazon GameLift
server SDK, including starting new game sessions and tracking game
session events using AWS CLI or GameLift Testing Toolkit. This
verifies that the game server functions correctly within the
GameLift environment.

Use the GameLift Testing Toolkit to automate testing and gather
detailed performance metrics. The toolkit allows you to visualize
GameLift infrastructure, launch virtual players for load testing,
and iterate on FlexMatch rule sets with the FlexMatch simulator.
It is particularly useful for scaling ECS Fargate tasks, which
simulate player sessions by creating numerous concurrent game
sessions to stress test the server infrastructure.

Scalability testing

Experiment with game session queue designs, multi-location fleets,
Spot and On-Demand fleets, and multiple instance types. Test game
session placement options, latency policies, and fleet
prioritization settings. Configure capacity scaling to meet player
demand and validate that the system can handle the expected load
under different conditions.

### Implementation steps

- Use Amazon GameLift Anywhere to set up a realistic test
  environment for iterative performance and scalability
  testing.
- Test game server integration with the GameLift server SDK,
  facilitating correct session management and event tracking
  within the GameLift environment.
- Perform scalability testing with the GameLift Testing
  Toolkit, simulating player load, testing session queues, and
  validating fleet scaling, latency policies, and
  prioritization settings.
