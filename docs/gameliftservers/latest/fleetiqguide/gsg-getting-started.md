# Amazon GameLift Servers FleetIQ integration steps

This integration plan outlines the key steps to getting your multiplayer games up and
running on Amazon EC2 instances with Amazon GameLift Servers FleetIQ. If you're looking for the Amazon GameLift Servers managed hosting
service, which automates more game hosting processes for you, see the [Amazon GameLift Servers Developer Guide](../developerguide/gamelift-intro.md "../developerguide/gamelift-intro.md").

To get started using Amazon GameLift Servers FleetIQ, you need to have a working game server that runs in either
an on-premises or Amazon EC2 environment. Your game server can be a single process that manages
one or multiple game sessions, spawns child processes, or runs inside of a container.

1. **Get an [AWS
   account](https://aws.amazon.com/account/ "https://aws.amazon.com/account/") and set up users with Amazon GameLift Servers FleetIQ access.**

Create a new AWS account or choose an existing account to use with Amazon GameLift Servers FleetIQ. Set
up users with permissions to manage the Amazon EC2, Amazon EC2 Auto Scaling, and other AWS resources used
with your game. For detailed instructions, see [Set up your AWS account for Amazon GameLift Servers FleetIQ](gsg-iam-permissions.md "gsg-iam-permissions.md"). 2. **Create IAM roles.**

Create roles that allow Amazon GameLift Servers FleetIQ, Amazon EC2, and Amazon EC2 Auto Scaling resources to communicate with
each other. See [Create IAM roles for cross-service
interaction](gsg-iam-permissions-roles.md "gsg-iam-permissions-roles.md") for more details. 3. **Get the AWS SDK and AWS CLI with Amazon GameLift Servers FleetIQ
functionality.**

    * [Download the latest version of the
     AWS SDK](https://aws.amazon.com/tools/#SDKs "https://aws.amazon.com/tools/#SDKs").
    * [View the Amazon GameLift Servers API reference
     documentation](../../../gamelift/latest/apireference.md "../../../gamelift/latest/apireference.md").

4. **Prepare your game server for use with Amazon GameLift Servers FleetIQ.**

Add the AWS SDK to your game server project and add code to keep Amazon GameLift Servers FleetIQ
updated with the current status and usage of your game servers. See [Integrate Amazon GameLift Servers FleetIQ into a game server](gsg-integrate-gameserver.md "gsg-integrate-gameserver.md") for additional guidance and examples.
Amazon GameLift Servers FleetIQ uses this information to provide your matchmaking system with a list of
viable, unoccupied game servers, and also avoid terminating instances that are
currently hosting players during balancing. 5. **Create an Amazon EC2 Amazon Machine Image (AMI) with your game
server.**

Create an AMI with your game server software and with any other runtime assets or
configuration settings. For help, see [Amazon
Machine Images (AMI)](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md") in the _Amazon EC2 User
Guide_. 6. **Create an Amazon EC2 launch template.**

Build an Amazon EC2 launch template that uses your custom AMI and defines network and
security settings for your hosting resources. The launch template must reference the
instance profile that you created (see Step 2) with permissions that allow your game
server to communicate with Amazon GameLift Servers FleetIQ. You don’t need to include instance types in
your launch template, as this is done later. For help, see [Creating a Launch
Template](../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md "../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md") in the _Amazon EC2 User Guide_.

###### Note

Before using a launch template with Amazon GameLift Servers FleetIQ, we highly recommend that you
first set up an Amazon EC2 Auto Scaling group to verify that the template configuration and AMI are
deploying properly. 7. **Set up Amazon GameLift Servers FleetIQ hosting resources.**

In each Region where you want to deploy game servers, create a game server group
by calling [CreateGameServerGroup()](../../../gamelift/latest/apireference/API_CreateGameServerGroup.md "../../../gamelift/latest/apireference/API_CreateGameServerGroup.md"). Pass in the launch template (containing your
custom AMI and network and security settings), IAM role, and a list of instance
types that your game can run on. This action sets up an Amazon EC2 Auto Scaling group in your AWS
account that Amazon GameLift Servers FleetIQ can modify. For additional guidance and examples, see [Manage Amazon GameLift Servers FleetIQ game server groups](gsg-integrate-gameservergroup.md "gsg-integrate-gameservergroup.md"). 8. **Integrate Amazon GameLift Servers FleetIQ into your game client.**

Add the AWS SDK to your game client, matchmaker, or other backend component that
allocates game server capacity. Depending on your game type, your matchmaker might
call [ListGameServers()](../../../gamelift/latest/apireference/API_ListGameServers.md "../../../gamelift/latest/apireference/API_ListGameServers.md") or
[ClaimGameServer()](../../../gamelift/latest/apireference/API_ClaimGameServer.md "../../../gamelift/latest/apireference/API_ClaimGameServer.md") to
obtain server capacity and reserve an available game server. For additional guidance
and examples, see [Integrate Amazon GameLift Servers FleetIQ into a game client](gsg-integrate-gameclient.md "gsg-integrate-gameclient.md"). 9. **Scale up your Auto Scaling group.**

As instances are provisioned in your Amazon EC2 Auto Scaling group, they launch your game servers.
Each game server then registers with Amazon GameLift Servers FleetIQ as available capacity, to be listed or
claimed later by your matchmaker. 10. **Test your game.**

Invoke your matchmaker and call `ClaimGameServer` to request server
capacity. Pass the resulting IP and port back to game clients so they can connect to
the game server.
