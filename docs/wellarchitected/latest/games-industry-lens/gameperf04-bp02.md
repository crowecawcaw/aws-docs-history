# GAMEPERF04-BP02 Performance test your game server with

simulated and real gameplay scenarios

Conduct performance testing and evaluate various
gameplay scenarios to determine whether the game server process
handles the utilization of fixed resources appropriately, such as
EC2 instance memory, CPU, and network bandwidth.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Creating simulated gameplay tests with bots that can mirror common
gameplay paths and behaviors of your players can determine how
your game server processes handle this under different usage
scenarios. For example, you can implement a solution, such as
[Distributed
Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/ "https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/") that you can customize to run game
client simulations or game client builds to generate gameplay
scenarios. Run internal play tests and use QA teams to stress test
the various features of your game so that you can develop
confidence that your game is designed to perform optimally.
[AWS Device Farm](https://aws.amazon.com/device-farm/ "https://aws.amazon.com/device-farm/") can be used to perform mobile and web testing for your
iOS, Android, and browser games on multiple device types.

### Implementation steps

- Conduct performance testing with bots simulating common
  player behaviors to evaluate game server resource
  utilization under different scenarios.
- Use solutions like Distributed Load Testing on AWS to
  customize and simulate gameplay scenarios for stress
  testing.
- Perform internal playtests and use tools like AWS Device Farm for mobile and browser game testing on various devices.
