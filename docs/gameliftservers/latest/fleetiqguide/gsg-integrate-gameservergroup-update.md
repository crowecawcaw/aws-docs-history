# Update a game server

group

You can update game server group properties that affect how Amazon GameLift Servers FleetIQ manages hosting
for game servers, including resource type optimizations. To update these properties,
call [UpdateGameServerGroup()](../../../gamelift/latest/apireference/API_UpdateGameServerGroup.md "../../../gamelift/latest/apireference/API_UpdateGameServerGroup.md"). After the changes to the game server group take
effect, Amazon GameLift Servers FleetIQ may overwrite certain properties in the Auto Scaling group.

For all other Auto Scaling group properties, such as `MinSize`,
`MaxSize`, and `LaunchTemplate`, you can modify these directly
on the Auto Scaling group.

In the example below, the instance type definitions are updated to switch over to
c4.xlarge and c5.xlarge instances types.

```
AWS gamelift update-game-server-group \
    --game-server-group-name MyLiveGroup \
    --instance-definitions '[{"InstanceType": "c4.xlarge"}, {"InstanceType": "c5.xlarge"}]'
```
