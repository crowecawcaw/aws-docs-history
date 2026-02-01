# Update a game server build

When you deploy your game server build for Amazon GameLift Servers managed EC2 hosting, you upload your
game server software and create an Amazon GameLift Servers build resource. After you've created an Amazon GameLift Servers
build, you can update the build's metadata, but you can't update the build files
themselves. To deploy updates to your game server builde, you must upload a new set of files and create a
new Amazon GameLift Servers build using the AWS CLI command[`upload-build`](../../../cli/latest/reference/gamelift/upload-build.md "../../../cli/latest/reference/gamelift/upload-build.md") command. Alternatively, you can use the [`create-build`](../../../cli/latest/reference/gamelift/create-build.md "../../../cli/latest/reference/gamelift/create-build.md") command to upload a new build from an Amazon S3
bucket that you control. Then deploy the new build by creating a new fleet for
it.

You can update a build's metadata, including the name and description. For these
tasks, use the Amazon GameLift Servers console or the [`update-build`](../../../cli/latest/reference/gamelift/update-build.md "../../../cli/latest/reference/gamelift/update-build.md") AWS CLI command.

## Automate your game build

updates

Follow these tips to help automate and streamline the process of updating game
server builds for Amazon GameLift Servers managed fleets:

- **Use game session queues and swap out fleets as
  needed.** When sending game session requests to Amazon GameLift Servers, specify
  a game session queue instead of a specific fleet. With queues, you can add
  fleets with a new build and remove old fleets as needed. For more
  information, see [Configure game session placement](queues-intro.md "queues-intro.md").
- **Use aliases to transfer players to a new game
  build.** When sending game session requests to Amazon GameLift Servers, specify a
  fleet alias instead of a fleet ID. For more information, see [Create an Amazon GameLift Servers alias](aliases-creating.md "aliases-creating.md").
- **Set up for iterative development.** During
  game development, explore options for setting up a hosted test environment
  that supports rapid iterative development. See [Set up for iterative development with Amazon GameLift Servers Anywhere](integration-dev-iteration.md "integration-dev-iteration.md").

Try out these resources from the [Amazon GameLift Servers Toolkit](https://github.com/aws/amazon-gamelift-toolkit "https://github.com/aws/amazon-gamelift-toolkit") on
Github:

**Fast build update tool (for development only)**

This tool helps you modify game server builds that are already
deployed on computes in a managed EC2 fleet, saving you time during fast
development iteration. The tool has several options; you can replace the
entire game build or change specific files, and you can manage how to
restart game server processes after the updates. You can also use it to
update all computes in a fleet or target individual computes.

Visit the Amazon GameLift Servers Toolkit repo in Github to get the [fast build update tool](https://github.com/aws/amazon-gamelift-toolkit/tree/main/fast-build-update-tool "https://github.com/aws/amazon-gamelift-toolkit/tree/main/fast-build-update-tool") in Github and learn more about how
to use it.

**Production deployment sample script**

This script illustrates how you can automate
the process of updating game server builds that are deployed on managed
EC2 fleets in production. To use this script, your Amazon GameLift Servers hosting
solution must use aliases to abstract fleet IDs. The sample script
handles the following basic steps: upload an updated build, create a new
build and deploy to a new fleet, redirect player traffic from an
existing fleet to the new fleet, and delete the old fleet. Customize the
sample script to meet your specific deployment requirements.

Visit the Amazon GameLift Servers Toolkit repo in Github to get the [production deployment sample script](https://github.com/aws/amazon-gamelift-toolkit/tree/main/production-deployment-sample-script "https://github.com/aws/amazon-gamelift-toolkit/tree/main/production-deployment-sample-script") in Github and learn
more about how to use it.
