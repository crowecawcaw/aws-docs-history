

# Remotely access fleet resources
<a name="remote-access-intro"></a>

You can connect to any instance in your active Amazon GameLift Servers managed EC2 or managed container fleets. For container fleets, you can also connect to individual containers running on an instance to troubleshoot game sessions, inspect logs, and debug runtime issues. Common reasons to remotely access an instance include:
+ Troubleshoot issues with your game server integration.
+ Fine-tune your runtime configuration and other fleet-specific settings.
+ Monitor real-time game server activity, such as log tracking.
+ Run benchmarking tools using actual player traffic.
+ Investigate specific issues with a game session or server process.

When connecting to an instance, keep the following in mind:
+ You can connect to any instance in an active fleet. Generally, you can't connect to non-active fleets, such as fleets that are in the process of activating or are in an error state. (These fleets might have limited availability for a short period of time.) For help with fleet activation issues, see [Debug Amazon GameLift Servers fleet issues](fleets-creating-debug.md).
+ Connecting to an active instance doesn't affect the instance's hosting activity. The instance continues to start and stop server processes based on the runtime configuration. It activates and runs game sessions. The instance might shut down in response to a scale down event or other event.
+ Any changes you make to files or settings on the instance might impact the instance's active game sessions and connected players.