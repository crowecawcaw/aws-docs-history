

# Update a game server group
<a name="gsg-integrate-gameservergroup-update"></a>

You can update game server group properties that affect how Amazon GameLift Servers FleetIQ manages hosting for game servers, including resource type optimizations. To update these properties, call [UpdateGameServerGroup()](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateGameServerGroup.html). After the changes to the game server group take effect, Amazon GameLift Servers FleetIQ may overwrite certain properties in the Auto Scaling group. 

For all other Auto Scaling group properties, such as `MinSize`, `MaxSize`, and `LaunchTemplate`, you can modify these directly on the Auto Scaling group. 

In the example below, the instance type definitions are updated to switch over to c4.xlarge and c5.xlarge instance types.

```
AWS gamelift update-game-server-group \
    --game-server-group-name MyLiveGroup \
    --instance-definitions '[{"InstanceType": "c4.xlarge"}, {"InstanceType": "c5.xlarge"}]'
```