# Prepare for launch with Amazon GameLift Servers hosting

Use the following checklists to validate each deployment phase of your game. Items marked **[Critical]** are critical for your
production launch.

Download and complete the Amazon GameLift Servers launch questionnaire, which is available in the [[Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/")](https://console.aws.amazon.com/gamelift/prepare-to-launch "https://console.aws.amazon.com/gamelift/prepare-to-launch").
We want every game developer using Amazon GameLift Servers to have a smooth launch day, and the requested
information helps us help you prepare for upcoming load testing, soft launch or public launch. Plan to submit the completed questionnaire at least three (3)
months before conducting your first load test.

###### Topics

- [Get your
  game ready](#gamelift_quickstart_customservers_prepgameserver_checklist "#gamelift_quickstart_customservers_prepgameserver_checklist")
- [Prepare for testing](#gamelift_quickstart_customservers_test_checklist "#gamelift_quickstart_customservers_test_checklist")
- [Prepare for launch](#gamelift_quickstart_customservers_launch_checklist "#gamelift_quickstart_customservers_launch_checklist")
- [Plan for
  post-launch updates](#gamelift_quickstart_customservers_launch_postchecklist "#gamelift_quickstart_customservers_launch_postchecklist")

## Get your

game ready

- **[Critical]** Verify that you've completed all the
  [development roadmap steps](getting-started-intro.md "getting-started-intro.md")  
  for your hosting solution, and that you have all the required components in place, including
  and integrated game server, a backend service for game clients, hosting fleets, and a game session placement
  method (such as a queue).
- **[Critical]**
  [Create AWS Identity and Access Management (IAM) roles](setting-up-aws-login.md "setting-up-aws-login.md") that
  allow your game server to access other AWS resources while running.
- **[Critical]** Design and implement failover to
  other hosting resources as needed.
- [Plan the rollout of fleets to your target
  locations](gamelift-regions.md "gamelift-regions.md"), considering your game's queue and fleet structure.
- [Automate your deployment](resources-cloudformation.md "resources-cloudformation.md") using
  infrastructure as code (IaC) with CloudFormation and the AWS Cloud Development Kit (AWS CDK).
- [Collect logs and analytics](monitoring-overview.md "monitoring-overview.md") using
  Amazon CloudWatch and Amazon Simple Storage Service (Amazon S3).

## Prepare for testing

- **[Critical]**
  [Request increases for Amazon GameLift Servers service quotas](limits-regions.md "limits-regions.md")
  and other AWS service quotas so that your live environment can scale up to
  production needs.
- **[Critical]** Verify that the open ports on live
  fleets match the range of ports that your servers could use.
- **[Critical]** Close RDP port 3389 and SSH port

22.

- Develop a plan for the DevOps management of your game. If you're using
  Amazon CloudWatch Logs or Amazon CloudWatch custom metrics, define alarms for severe or critical
  problems on the server fleet. Simulate failures and test the runbooks.
- Verify that the compute resources you're using can support the number of
  server processes that you want to run concurrently on each compute.
- [Tune your scaling policy](fleets-manage-capacity.md "fleets-manage-capacity.md") to be
  more conservative at first and provide more idle capacity than you think you
  need. You can optimize for cost later. Consider the use of target-based scaling
  policy with 20 percent idle capacity.
- For FlexMatch, use[latency rules](../flexmatchguide/match-intro.md "../flexmatchguide/match-intro.md") to match players who are geographically near each
  other. Test how this behaves under load with synthetic latency data from your
  load test client.
- Load test your player authentication and game session infrastructure to see if
  it scales effectively to meet demand.
- Verify that a server left running for several days can still accept
  connections.
- Raise your Support plan level to Business or Enterprise so that AWS can
  respond to you during problems or outages.

## Prepare for launch

- **[Critical]** [Set the fleet protection policy](fleets-creating.md "fleets-creating.md") to full protection on all live
  fleets so that scaling down doesn't stop active game sessions.
- **[Critical]**
  [Set fleet maximum sizes](fleets-capacity-limits.md "fleets-capacity-limits.md") high
  enough to accommodate peak anticipated demand, at minimum. We recommend that you
  double your maximum size for unanticipated demand.
- Encourage your entire development team to participate in the launch event and
  monitor your game launch in a launch room.
- Monitor player latency and player experience.

## Plan for

post-launch updates

- [Tune scaling policy](fleets-manage-capacity.md "fleets-manage-capacity.md") to minimize
  idle capacity based on player usage.
- [Modify FlexMatch
  rules](../flexmatchguide/match-intro.md "../flexmatchguide/match-intro.md") or [add hosting
  locations](gamelift-compute.md#gamelift-compute-location "gamelift-compute.md#gamelift-compute-location") based on player latency data and revised
  requirements.
- Optimize the runtime configuration to run as many games sessions as possible
  on each computing resource. Mazimizing performance efficiency in this way can
  directly affect your fleet costs, because you might be able to run more server
  processes with the same compute resources.
- [Use your analytics data](monitoring-overview.md "monitoring-overview.md") to drive
  continued development, improve player experience and game longevity, and
  optimize monetization.
