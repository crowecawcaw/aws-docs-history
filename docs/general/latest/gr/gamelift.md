# Amazon GameLift Servers endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

###### Note

The following service endpoints table lists the AWS Regions that are available as
Amazon GameLift Servers fleet home Regions. For more on Region availability for Amazon GameLift Servers features, including
multi-location fleets, remote locations, and Local Zones, see [Amazon GameLift Servers service
locations](../../../gamelift/latest/developerguide/gamelift-regions.md "../../../gamelift/latest/developerguide/gamelift-regions.md").

## Service endpoints

| Region Name               | Region         | Endpoint                                                                 | Protocol       |
| ------------------------- | -------------- | ------------------------------------------------------------------------ | -------------- |
| US East (Ohio)            | us-east-2      | gamelift.us-east-2.amazonaws.com<br>gamelift.us-east-2.api.aws           | HTTPS<br>HTTPS |
| US East (N. Virginia)     | us-east-1      | gamelift.us-east-1.amazonaws.com<br>gamelift.us-east-1.api.aws           | HTTPS<br>HTTPS |
| US West (N. California)   | us-west-1      | gamelift.us-west-1.amazonaws.com<br>gamelift.us-west-1.api.aws           | HTTPS<br>HTTPS |
| US West (Oregon)          | us-west-2      | gamelift.us-west-2.amazonaws.com<br>gamelift.us-west-2.api.aws           | HTTPS<br>HTTPS |
| Asia Pacific (Mumbai)     | ap-south-1     | gamelift.ap-south-1.amazonaws.com<br>gamelift.ap-south-1.api.aws         | HTTPS<br>HTTPS |
| Asia Pacific (Seoul)      | ap-northeast-2 | gamelift.ap-northeast-2.amazonaws.com<br>gamelift.ap-northeast-2.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Singapore)  | ap-southeast-1 | gamelift.ap-southeast-1.amazonaws.com<br>gamelift.ap-southeast-1.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Sydney)     | ap-southeast-2 | gamelift.ap-southeast-2.amazonaws.com<br>gamelift.ap-southeast-2.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Tokyo)      | ap-northeast-1 | gamelift.ap-northeast-1.amazonaws.com<br>gamelift.ap-northeast-1.api.aws | HTTPS<br>HTTPS |
| Canada (Central)          | ca-central-1   | gamelift.ca-central-1.amazonaws.com<br>gamelift.ca-central-1.api.aws     | HTTPS<br>HTTPS |
| Europe (Frankfurt)        | eu-central-1   | gamelift.eu-central-1.amazonaws.com<br>gamelift.eu-central-1.api.aws     | HTTPS<br>HTTPS |
| Europe (Ireland)          | eu-west-1      | gamelift.eu-west-1.amazonaws.com<br>gamelift.eu-west-1.api.aws           | HTTPS<br>HTTPS |
| Europe (London)           | eu-west-2      | gamelift.eu-west-2.amazonaws.com<br>gamelift.eu-west-2.api.aws           | HTTPS<br>HTTPS |
| South America (São Paulo) | sa-east-1      | gamelift.sa-east-1.amazonaws.com<br>gamelift.sa-east-1.api.aws           | HTTPS<br>HTTPS |

## UDP ping beacon endpoints

Amazon GameLift Servers UDP ping beacons allow you to measure network latency between your players and
AWS locations. You can use these UDP ping beacon endpoints to collect latency data and make
informed decisions about which hosting locations provide the best gaming experience for your
players. The following table lists the UDP ping beacon endpoints available for each AWS location and Local Zone that Amazon GameLift Servers supports.

| UDP ping beacons by location | Location name    | Location code                             | Endpoint | Protocol | IPv6 Support |
| ---------------------------- | ---------------- | ----------------------------------------- | -------- | -------- | ------------ |
| **North America**            |                  |                                           |          |          |
| US East (N. Virginia)        | us-east-1        | gamelift-ping.us-east-1.api.aws:7770      | UDP      | Yes      |
| US East (Ohio)               | us-east-2        | gamelift-ping.us-east-2.api.aws:7770      | UDP      | Yes      |
| US West (N. California)      | us-west-1        | gamelift-ping.us-west-1.api.aws:7770      | UDP      | Yes      |
| US West (Oregon)             | us-west-2        | gamelift-ping.us-west-2.api.aws:7770      | UDP      | Yes      |
| Canada (Central)             | ca-central-1     | gamelift-ping.ca-central-1.api.aws:7770   | UDP      | Yes      |
| **US Local Zones**           |                  |                                           |          |          |
| US West (Los Angeles)        | us-west-2-lax-1  | gamelift-ping-lax.us-west-2.api.aws:7770  | UDP      | Yes      |
| US East (Chicago)            | us-east-1-chi-1  | gamelift-ping-chi.us-east-1.api.aws:7770  | UDP      | No       |
| US East (Houston)            | us-east-1-iah-1  | gamelift-ping-iah.us-east-1.api.aws:7770  | UDP      | No       |
| US East (Dallas)             | us-east-1-dfw-1  | gamelift-ping-dfw.us-east-1.api.aws:7770  | UDP      | No       |
| US West (Denver)             | us-west-2-den-1  | gamelift-ping-den.us-west-2.api.aws:7770  | UDP      | No       |
| US East (Atlanta)            | us-east-1-atl-1  | gamelift-ping-atl.us-east-1.api.aws:7770  | UDP      | No       |
| US West (Phoenix)            | us-west-2-phx-1  | gamelift-ping-phx.us-west-2.api.aws:7770  | UDP      | No       |
| US East (Kansas City)        | us-east-1-mci-1  | gamelift-ping-mci.us-east-1.api.aws:7770  | UDP      | No       |
| **South America**            |                  |                                           |          |          |
| South America (São Paulo)    | sa-east-1        | gamelift-ping.sa-east-1.api.aws:7770      | UDP      | Yes      |
| **Europe**                   |                  |                                           |          |          |
| Europe (Ireland)             | eu-west-1        | gamelift-ping.eu-west-1.api.aws:7770      | UDP      | Yes      |
| Europe (London)              | eu-west-2        | gamelift-ping.eu-west-2.api.aws:7770      | UDP      | Yes      |
| Europe (Paris)               | eu-west-3        | gamelift-ping.eu-west-3.api.aws:7770      | UDP      | Yes      |
| Europe (Frankfurt)           | eu-central-1     | gamelift-ping.eu-central-1.api.aws:7770   | UDP      | Yes      |
| Europe (Milan)               | eu-south-1       | gamelift-ping.eu-south-1.api.aws:7770     | UDP      | Yes      |
| Europe (Stockholm)           | eu-north-1       | gamelift-ping.eu-north-1.api.aws:7770     | UDP      | Yes      |
| **Asia Pacific**             |                  |                                           |          |          |
| Asia Pacific (Malaysia)      | ap-southeast-5   | gamelift-ping.ap-southeast-5.api.aws:7770 | UDP      | Yes      |
| Asia Pacific (Mumbai)        | ap-south-1       | gamelift-ping.ap-south-1.api.aws:7770     | UDP      | Yes      |
| Asia Pacific (Hong Kong)     | ap-east-1        | gamelift-ping.ap-east-1.api.aws:7770      | UDP      | Yes      |
| Asia Pacific (Thailand)      | ap-southeast-7   | gamelift-ping.ap-southeast-7.api.aws:7770 | UDP      | Yes      |
| Asia Pacific (Osaka)         | ap-northeast-3   | gamelift-ping.ap-northeast-3.api.aws:7770 | UDP      | Yes      |
| Asia Pacific (Seoul)         | ap-northeast-2   | gamelift-ping.ap-northeast-2.api.aws:7770 | UDP      | Yes      |
| Asia Pacific (Singapore)     | ap-southeast-1   | gamelift-ping.ap-southeast-1.api.aws:7770 | UDP      | Yes      |
| Asia Pacific (Sydney)        | ap-southeast-2   | gamelift-ping.ap-southeast-2.api.aws:7770 | UDP      | Yes      |
| Asia Pacific (Tokyo)         | ap-northeast-1   | gamelift-ping.ap-northeast-1.api.aws:7770 | UDP      | Yes      |
| **Middle East**              |                  |                                           |          |          |
| Middle East (Bahrain)        | me-south-1       | gamelift-ping.me-south-1.api.aws:7770     | UDP      | Yes      |
| **Africa**                   |                  |                                           |          |          |
| Africa (Cape Town)           | af-south-1       | gamelift-ping.af-south-1.api.aws:7770     | UDP      | Yes      |
| Africa (Lagos)               | af-south-1-los-1 | gamelift-ping-los.af-south-1.api.aws:7770 | UDP      | No       |

## Service quotas

| Name                                                                  | Default                              | Adjustable                                                                                                                                                                           | Description                                                                                                                                                   |
| --------------------------------------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Aliases per region                                                    | Each supported Region: 100           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-AED4A06A "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-AED4A06A") | The maximum number of aliases allowed per region.                                                                                                             |
| Anywhere fleets per region                                            | Each supported Region: 10            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-593688D9 "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-593688D9") | The maximum number of Anywhere fleets allowed (in any status) per region.                                                                                     |
| Build capacity                                                        | Each supported Region: 100 Gigabytes | No                                                                                                                                                                                   | The maximum capacity (in gigabytes) available for all uploaded game builds combined per region. To free storage space, delete unused builds as needed.        |
| Builds per region                                                     | Each supported Region: 1,000         | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-90D24F1B "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-90D24F1B") | The maximum number of game server builds allowed (in any status) per region.                                                                                  |
| Compute per Anywhere fleet                                            | Each supported Region: 100           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-0536A98D "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-0536A98D") | The maximum number of registered compute resources allowed per Anywhere fleet.                                                                                |
| Custom locations per region                                           | Each supported Region: 20            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-C6F4238C "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-C6F4238C") | The maximum number of custom locations allowed per region.                                                                                                    |
| Game server groups per region                                         | Each supported Region: 20            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-8D885299 "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-8D885299") | The maximum number of game server groups allowed per region.                                                                                                  |
| Game servers per game server group                                    | Each supported Region: 1,000         | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-51AF299A "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-51AF299A") | The maximum number of game servers allowed per game server group.                                                                                             |
| Game session log file size                                            | Each supported Region: 200 Megabytes | No                                                                                                                                                                                   | The maximum file size (in megabytes) allowed for game session logs that are uploaded to Amazon GameLift Servers at the conclusion of a game session.          |
| Game session queues per region                                        | Each supported Region: 20            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-22451070 "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-22451070") | The maximum number of game session queues allowed per region.                                                                                                 |
| Key-value pairs per string to double map matchmaking player attribute | Each supported Region: 10            | No                                                                                                                                                                                   | The maximum number of key-value pairs in a string to double map (SDM) matchmaking player attribute.                                                           |
| Locations in a fleet per region                                       | Each supported Region: 4             | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-55650DB7 "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-55650DB7") | The maximum number of locations allowed (in any status) in a fleet per region.                                                                                |
| Managed EC2 fleet EBS volume                                          | Each supported Region: 50 Gigabytes  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-BFEEB817 "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-BFEEB817") | The provisioned EBS volume capacity (in gigabytes) for managed EC2 fleet instances.                                                                           |
| Managed EC2 fleets per region                                         | Each supported Region: 10            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-FDDD1260 "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-FDDD1260") | The maximum number of managed EC2 fleets allowed (in any status) per region.                                                                                  |
| Matchmaking configurations per region                                 | Each supported Region: 100           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-73F6E300 "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-73F6E300") | The maximum number of matchmaking configurations allowed per region.                                                                                          |
| Matchmaking rule sets per region                                      | Each supported Region: 1,000         | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-8AE49BBD "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-8AE49BBD") | The maximum number of matchmaking rule sets allowed per region.                                                                                               |
| Maximum NewGameSessionsPerCreator per fleet configuration             | Each supported Region: 10            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-3A43EF3C "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-3A43EF3C") | The maximum new game sessions per creator allowed in a fleets resource policy configuration.                                                                  |
| Maximum PolicyPeriodInMinutes per fleet configuration                 | Each supported Region: 60            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-9F9DE0B2 "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-9F9DE0B2") | The maximum period (in minutes) allowed in a fleets resource policy configuration.                                                                            |
| Player attributes per matchmaking player                              | Each supported Region: 10            | No                                                                                                                                                                                   | The maximum number of player attributes for each player in a matchmaking ticket.                                                                              |
| Player session timeout                                                | Each supported Region: 60 Seconds    | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-24BE0A39 "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-24BE0A39") | The maximum time (in seconds) for a reserved player session to timeout pending a valid player connection.                                                     |
| Player sessions per game session                                      | Each supported Region: 200           | No                                                                                                                                                                                   | The maximum number of player sessions that can join a game session.                                                                                           |
| Players per matchmaking ticket                                        | Each supported Region: 10            | No                                                                                                                                                                                   | The maximum number of players that can be included in a matchmaking ticket.                                                                                   |
| Queue destinations per game session queue                             | Each supported Region: 10            | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-BB62CF1D "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-BB62CF1D") | The maximum number of queue destinations allowed per game session queue.                                                                                      |
| Script capacity                                                       | Each supported Region: 100 Gigabytes | No                                                                                                                                                                                   | The maximum capacity (in gigabytes) available for all uploaded scripts combined per region. To free storage space, delete unused builds as needed.            |
| Scripts per region                                                    | Each supported Region: 1,000         | [Yes](https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-293B0017 "https://console.aws.amazon.com/servicequotas/home/services/gamelift/quotas/L-293B0017") | The maximum number of game server scripts allowed per region.                                                                                                 |
| Server processes per instance (Server SDK v3 and up)                  | Each supported Region: 50            | No                                                                                                                                                                                   | The maximum number of concurrent server processes that can run on a single instance when using the Server SDK for Amazon GameLift Servers version 3 or later. |
| Strings per string list matchmaking player attribute                  | Each supported Region: 100           | No                                                                                                                                                                                   | The maximum number of strings in a string list (SL) matchmaking player attribute.                                                                             |
