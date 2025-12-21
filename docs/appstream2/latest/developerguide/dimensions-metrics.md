# Dimensions for Amazon WorkSpaces Applications Metrics

The `AWS/AppStream` namespace includes the following dimensions and dimension groups.

| Dimension    | Description                                     |
| ------------ | ----------------------------------------------- |
| `Fleet`      | Filters the metric data by name of the Fleet.   |
| `FleetName`  | Filters the metric data by name of the Fleet.   |
| `SessionId`  | Filters the metric data by session identifier.  |
| `InstanceId` | Filters the metric data by instance identifier. |
| `UserId`     | Filters the metric data by user identifier.     |

| Dimension                                    | Where Available in Amazon CloudWatch Metrics |
| -------------------------------------------- | -------------------------------------------- |
| `[Fleet]`                                    | Fleet Metrics                                |
| `[FleetName, InstanceId]`                    | Fleet Instance Metrics                       |
| `[FleetName, InstanceId, SessionId]`         | Fleet Session Metrics                        |
| `[UserId]`                                   | UserId                                       |
| `[FleetName, InstanceId, SessionId, UserId]` | FleetName, InstanceId, SessionId, UserId     |
