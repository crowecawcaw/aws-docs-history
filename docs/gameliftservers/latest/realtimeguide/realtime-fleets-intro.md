# Creating a managed EC2 fleet for Amazon GameLift Servers Realtime

This section guides you through how to create an Amazon GameLift Servers managed EC2 fleet for Realtime
servers. Managed fleets use Amazon Elastic Compute Cloud (Amazon EC2) compute instances that are optimized for
multiplayer game hosting. You can create a fleet that deploys Realtime servers globally,
in any AWS Region or Local Zone that Amazon GameLift Servers supports. For a list of supported locations,
see [Amazon GameLift Servers service
locations](../developerguide/gamelift-regions.md "../developerguide/gamelift-regions.md"). You can set up multi-location fleets for your Realtime
servers.

When you create a managed EC2 fleet, the fleet creation process starts immediately. This process
involves several phases as Amazon GameLift Servers prepares your Realtime servers based on your configuration script,
provisions EC2 instances and deploys the server code, and prepares to host game servers on each instance.
You can monitor a fleet's status in the console or using the AWS Command Line Interface (AWS CLI). A
fleet is ready to host game sessions when its status reaches `ACTIVE`. For more
guidance about creating a managed EC2 fleet, , see the following topics in the _Amazon GameLift Servers Hosting Guide_:

- [Amazon GameLift Servers managed EC2 fleets](../developerguide/fleets-intro-managed.md "../developerguide/fleets-intro-managed.md")
- [Customize your Amazon GameLift Servers managed EC2 fleets](../developerguide/fleets-design.md "../developerguide/fleets-design.md")
- [Debug Amazon GameLift Servers fleet issues](../developerguide/fleets-creating-debug.md "../developerguide/fleets-creating-debug.md")

###### Topics

- [Create a hosting fleet for Amazon GameLift Servers Realtime](realtime-fleets-creating.md "realtime-fleets-creating.md")
- [Debug managed EC2 fleets for Amazon GameLift Servers Realtime](fleets-creating-debug-realtime.md "fleets-creating-debug-realtime.md")
