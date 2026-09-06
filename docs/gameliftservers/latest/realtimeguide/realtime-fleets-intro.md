

# Creating a managed EC2 fleet for Amazon GameLift Servers Realtime
<a name="realtime-fleets-intro"></a>

This section guides you through how to create an Amazon GameLift Servers managed EC2 fleet for Realtime servers. Managed fleets use Amazon Elastic Compute Cloud (Amazon EC2) compute instances that are optimized for multiplayer game hosting. You can create a fleet that deploys Realtime servers globally, in any AWS Region or Local Zone that Amazon GameLift Servers supports. For a list of supported locations, see [Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-regions.html). You can set up multi-location fleets for your Realtime servers.

When you create a managed EC2 fleet, the fleet creation process starts immediately. This process involves several phases as Amazon GameLift Servers prepares your Realtime servers based on your configuration script, provisions EC2 instances and deploys the server code, and prepares to host game servers on each instance. You can monitor a fleet's status in the console or using the AWS Command Line Interface (AWS CLI). A fleet is ready to host game sessions when its status reaches `ACTIVE`. For more guidance about creating a managed EC2 fleet, see the following topics in the *Amazon GameLift Servers Hosting Guide*: 
+ [Amazon GameLift Servers managed EC2 fleets](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-intro-managed.html)
+ [Customize your Amazon GameLift Servers managed EC2 fleets](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-design.html)
+ [Debug Amazon GameLift Servers fleet issues](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/fleets-creating-debug.html)

**Topics**
+ [Create a hosting fleet for Amazon GameLift Servers Realtime](realtime-fleets-creating.md)
+ [Debug managed EC2 fleets for Amazon GameLift Servers Realtime](fleets-creating-debug-realtime.md)