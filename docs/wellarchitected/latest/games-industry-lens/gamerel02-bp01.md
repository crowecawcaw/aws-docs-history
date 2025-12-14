# GAMEREL02-BP01 Implement a scaling strategy that incorporates

the state of active player game sessions

Implement a solution for automatically scaling your game
infrastructure in a manner that incorporates the stateful nature
of your actively connected player sessions and gracefully handles
scaling activities without disrupting gameplay.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

One of advantages of developing a game in the cloud is the
elasticity that can be achieved by automatically scaling server
infrastructure as needed to meet demand. While stateless or
asynchronous games and backend services can be dynamically scaled
using [Amazon EC2 Auto Scaling policies](../../../autoscaling/ec2/userguide/as-scale-based-on-demand.md "../../../autoscaling/ec2/userguide/as-scale-based-on-demand.md"),
[EKS
autoscaling](../../../eks/latest/userguide/autoscaling.md "../../../eks/latest/userguide/autoscaling.md"), or similar techniques typically adopted for
scalable web applications, game developers typically require a
more customized approach for scaling stateful or synchronous games
to help block disruptions to active player sessions.

### Implementation steps

- For stateful games, generate custom metrics that can be used
  to monitor the state of your player sessions and available
  game server capacity, which can be reported to Amazon CloudWatch as custom metrics. Exercise features with
  application monitoring, such as CloudWatch Synthetics,
  checking the game for impairment of functions that simple up
  and down health monitoring may not detect.
- Using custom metrics, implement game server scaling
  software, for example, as a serverless application using AWS Lambda function or AWS Fargate, to manage the fleet of
  dedicated game server instances by using the AWS SDK to make
  API calls to update the minimum, maximum, and desired
  capacity settings for the
  EC2 [Auto
  Scaling groups](../../../autoscaling/ec2/userguide/AutoScalingGroup.md "../../../autoscaling/ec2/userguide/AutoScalingGroup.md") hosting your game server build.
- Use Amazon GameLift to host your game servers and use
  the [out-of-the-box
  game server auto scaling capabilities](../../../gamelift/latest/developerguide/fleets-manage-capacity.md "../../../gamelift/latest/developerguide/fleets-manage-capacity.md") to manage this
  scaling process for you.

The automatic scaling capabilities of Amazon GameLift are aware
of active player sessions and can be configured to block the
termination or scale-in of game server instances that are
actively hosting players. For more information,
see [Monitor
Amazon GameLift Servers with Amazon CloudWatch](../../../gamelift/latest/developerguide/monitoring-cloudwatch.md "../../../gamelift/latest/developerguide/monitoring-cloudwatch.md").
