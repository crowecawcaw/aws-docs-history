

# Manage Amazon GameLift Servers FleetIQ game server groups
<a name="gsg-integrate-gameservergroup"></a>

This topic describes the tasks required to set up a Amazon GameLift Servers FleetIQ game server group. Creating a game server group triggers the creation of an EC2 Auto Scaling group with all the necessary configuration settings, along with configuration to manage Amazon GameLift Servers FleetIQ optimizations for game hosting.

Before you can create a game server group, you must at minimum have the following resources prepared: 
+ An Amazon EC2 launch template that specifies how to launch Amazon EC2 instances with your game server build. For more information, see [ Launching an Instance from a Launch Template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon EC2 User Guide*.
+ An IAM role that extends limited access to your AWS account to allow Amazon GameLift Servers FleetIQ to create and interact with the Auto Scaling group. For more information, see [Create IAM roles for cross-service interaction](gsg-iam-permissions-roles.md).