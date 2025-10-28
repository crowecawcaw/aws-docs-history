# Set up for iterative development with Amazon GameLift Servers Anywhere

Amazon GameLift Servers provides tools and solutions to help you set up a hosted test environment for
use during game development. With these tools, you can create an environment that mirrors
the real-world player experience of managed hosting with Amazon GameLift Servers and supports a rapid,
iterative development process.

With a separate test environment, you remove the overhead of an Amazon GameLift Servers managed fleet
during testing. You no longer have to upload each new game server build iteration, create a
new fleet for it, and then wait 15+ minutes to it to activate. Instead, you can create a new
build, quickly update the test fleet with the new build, start it, and commence
testing.

Using an Amazon GameLift Servers Anywhere fleet, you can set up a test environment using a local device, such as your development
workstation. You can also set up a test environment using a cloud-based hosting
resource.

Set up an Anywhere test environment to develop and test a range of scenarios, including
these:

- Test your game server integration with the Amazon GameLift Servers server SDK. You can test even
  without a working game client by using AWS CLI calls to start new game sessions and
  track game session events.
- Test interactions between your game client, backend service, and the Amazon GameLift Servers
  service as you develop components for your game. Fine-tune the player experience for
  joining a game.
- Experiment with your FlexMatch matchmaker design. Try out rule set variations and
  other matchmaking feature implementations. Set up and test matchmaking
  backfill.
- Try out other Amazon GameLift Servers hosting features, such as runtime configuration settings
  (with the Amazon GameLift Servers Agent) for game server life cycle management.
- Quickly build, test, and repeat to validate all aspects of your game's player
  experience, including multiplayer interactions, in a live, hosted environment.
  Later, as you prepare your game for launch, you'll want to add Amazon GameLift Servers managed fleets to
  fine-tune your hosting configurations and test additional scenarios, including the
  following:

- Experiment with and test game session queue designs, including use of
  multi-location fleets, Spot and On-Demand fleets, and multiple instance
  types.
- Try out game session placement options with managed fleets, including the use of
  optional latency policies and fleet prioritization settings.
- Configure capacity scaling to meet player demand, using automatic or manual
  scaling options.
- Set up AWS CloudFormation with Amazon GameLift Servers managed fleets to manage your hosting resources
  long term.

###### Fast Build Update Tool (for development only)

With managed EC2 fleets, to deploy a game server build update,
you need to upload each new build to Amazon GameLift Servers and create a new fleet for it.

The Fast Build Update Tool lets you can bypass these steps during development,
saving you time and allowing for faster development iteration. With this tool, you
can quickly update your game build files across all computes in an existing fleet.
The tool has several options; you can replace an entire game build or change
6 specific files, and you can manage how to restart game server processes after
the updates. You can also use it to update individual computes in a fleet.

To get the Fast Build Update Tool and learn more about how to use it, visit the Amazon GameLift Servers Toolkit repo for
[The Fast Build Update Tool](https://github.com/aws/amazon-gamelift-toolkit/tree/main/fast-build-update-tool "https://github.com/aws/amazon-gamelift-toolkit/tree/main/fast-build-update-tool") in Github.

###### Topics

- [Build a cloud-based test
  environment](integration-dev-iteration-cloud.md "integration-dev-iteration-cloud.md")
- [Set up local testing with Amazon GameLift Servers Anywhere](integration-testing.md "integration-testing.md")
- [Work with the Amazon GameLift Servers Agent](integration-dev-iteration-agent.md "integration-dev-iteration-agent.md")
