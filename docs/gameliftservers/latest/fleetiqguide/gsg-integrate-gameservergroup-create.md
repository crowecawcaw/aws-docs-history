# Create a game server group

To create a game server group, call [CreateGameServerGroup()](../../../gamelift/latest/apireference/API_CreateGameServerGroup.md "../../../gamelift/latest/apireference/API_CreateGameServerGroup.md").
This operation creates both a Amazon GameLift Servers FleetIQ game server group and a corresponding Auto
Scaling group. When you create the game server group, you provide game-specific settings
for Amazon GameLift Servers FleetIQ, including balancing strategy and instance type definitions. You also
provide initial property settings for the Auto Scaling group.

The following example triggers the creation of a `GameServerGroup` that
specifies c4.large and c5.large instance types and limits the group to Spot Instances
only, and an Auto Scaling group that uses the specified launch template for deploying
instances and manages group capcity within the minimum and maximum settings using a
target-tracking automatic scaling policy. After a short provisioning period, an
`AutoScalingGroup` resource is created, and the
`GameServerGroup` enters an ACTIVE state.

```
AWS gamelift create-game-server-group \
    --game-server-group-name MyLiveGroup \
    --role-arn arn:aws:iam::123456789012:role/GameLiftGSGRole \
    --min-size 1 \
    --max-size 10 \
    --game-server-protection-policy FULL_PROTECTION \
    --balancing-strategy SPOT_ONLY \
    --launch-template LaunchTemplateId=lt-012ab345cde6789ff \
    --instance-definitions '[{"InstanceType": "c4.large"}, {"InstanceType": "c5.large"}]' \
    --auto-scaling-policy '{"TargetTrackingConfiguration": {"TargetValue": 66}}'
```
