# GAMEPERF03-BP01 Use Amazon GameLift Anywhere and a GameLift

testing toolkit

To enhance performance efficiency through an iterative development
process, utilize Amazon GameLift Anywhere along with the Amazon
GameLift Testing Toolkit to establish a comprehensive testing
environment.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

This approach allows rapid iteration, efficient data
collection, and detailed performance analysis. Key steps include:

**Create a test environment**

Use Amazon GameLift Anywhere to set up a local or cloud-based test
environment. This setup removes the need to upload each game
server build iteration to a managed fleet, reducing the activation
time.

**Integrate Amazon GameLift Testing
Toolkit**

Incorporate the Amazon GameLift Testing Toolkit into your
development workflow. The toolkit provides scripts, tools, and
libraries to visualize Amazon GameLift infrastructure, launch
virtual players, and iterate upon FlexMatch rule sets with the
FlexMatch simulator. It simplifies the integration and management
of Amazon GameLift resources, allowing you to automate common
tasks and gather necessary data for performance analysis.

**Rapid build and test cycles**

Quickly update the test fleet with new builds, start it, and
commence testing. This facilitates a fast build-test-repeat cycle,
enabling developers to validate various aspects of the game's
player experience, including multiplayer interactions.

**Comprehensive testing**

Test your game server integration with the Amazon GameLift server
SDK, backend service interactions, matchmaking configurations, and
other GameLift hosting features. Utilize the GameLift Testing
Toolkit to automate testing and gather detailed performance
metrics, making sure that game components work seamlessly
together.

**Analyze performance data**

Use the data collected by the GameLift Testing Toolkit to analyze
performance bottlenecks and optimize your game server. The toolkit
helps track key metrics, identify issues, and make data-driven
decisions to improve performance efficiency.

By incorporating Amazon GameLift Anywhere and the GameLift Testing
Toolkit into your iterative development process, you can
significantly enhance performance efficiency through rapid
testing, comprehensive integration checks, and detailed
performance analysis.

### Implementation steps

- Use Amazon GameLift Anywhere to create a test environment,
  reducing activation time for game server builds and enabling
  rapid iteration.
- Integrate the Amazon GameLift Testing Toolkit to automate
  testing tasks, simulate players, and validate FlexMatch
  configurations during development.
- Collect and analyze performance data with the GameLift
  Testing Toolkit to identify bottlenecks, optimize game
  servers, and enhance performance efficiency.
