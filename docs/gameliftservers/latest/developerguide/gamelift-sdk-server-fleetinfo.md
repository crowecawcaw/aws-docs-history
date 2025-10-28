# Get fleet data for an Amazon GameLift Servers instance

There are some situations where your custom game build or Amazon GameLift Servers Realtime script may require
information about the Amazon GameLift Servers fleet. For example, your game build or script might include code
to:

- Monitor activity based on fleet data.
- Roll up metrics to track activity by fleet data. (Many games use this data for
  LiveOps activities.)
- Provide relevant data to custom game services, such as for matchmaking, additional
  capacity scaling, or testing.
  Fleet information is available as a JSON file on each instance in the following
  locations:

- Windows: `C:\GameMetadata\gamelift-metadata.json`
- Linux: `/local/gamemetadata/gamelift-metadata.json`
  The `gamelift-metadata.json` file includes the [attributes of a Amazon GameLift Servers fleet
  resource](../../../gamelift/latest/apireference/API_FleetAttributes.md "../../../gamelift/latest/apireference/API_FleetAttributes.md").

Example JSON file:

```
{
    "buildArn":"arn:aws:gamelift:us-west-2:123456789012:build/build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
    "buildId":"build-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
    "fleetArn":"arn:aws:gamelift:us-west-2:123456789012:fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "fleetDescription":"Test fleet for Really Fun Game v0.8",
    "fleetId":"fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "name":"ReallyFunGameTestFleet08",
    "fleetType":"ON_DEMAND",
    "instanceRoleArn":"arn:aws:iam::123456789012:role/S3AccessForGameLift",
    "instanceType":"c5.large",
    "serverLaunchPath":"/local/game/reallyfungame.exe"
}
```
