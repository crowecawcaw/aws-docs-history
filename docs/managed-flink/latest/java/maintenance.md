Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Manage maintenance tasks for Managed Service for Apache Flink

Managed Service for Apache Flink patches your applications periodically with operating-system and
container-image security updates to maintain compliance and meet AWS security
goals. A maintenance window for a Managed Service for Apache Flink application is a time window of 8 hours during which
Managed Service for Apache Flink performs application maintenance activities on an application. The maintenance might
begin on different days for different AWS Regions as scheduled by the service team.
Consult the table in the following section for maintenance time windows.

As part of the maintenance procedure, your Managed Service for Apache Flink application will be restarted. This
causes a downtime of 10 to 30 seconds during the application's maintenance window. The
actual downtime duration depends on the application state, size, and snapshot/checkpoint
recency. For information on how to minimize the impact of this downtime, see [Fault tolerance: checkpoints and savepoints](best-practices.md#how-dev-bp-checkpoint "best-practices.md#how-dev-bp-checkpoint"). You can find out if Managed Service for Apache Flink has performed a maintenance
action on your application using the `ListApplicationOperations` API. For more
information, see [Identify when maintenance has ocurred on your application](maintenance.md#maintenance-identify-ids "maintenance.md#maintenance-identify-ids").

| Maintenance time windows in AWS Regions | AWS Region      | Maintenance time window                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS GovCloud (US-West)                  | 06:00–14:00 UTC |
| AWS GovCloud (US-East)                  | 03:00–11:00 UTC |
| US East (N. Virginia)                   | 03:00–11:00 UTC |
| US East (Ohio)                          | 03:00–11:00 UTC |
| US West (N. California)                 | 06:00–14:00 UTC |
| US West (Oregon)                        | 06:00–14:00 UTC |
| Asia Pacific (Hong Kong)                | 13:00–21:00 UTC |
| Asia Pacific (Mumbai)                   | 16:30–00:30 UTC |
| Asia Pacific (Hyderabad)                | 16:30–00:30 UTC |
| Asia Pacific (Seoul)                    | 13:00–21:00 UTC |
| Asia Pacific (Singapore)                | 14:00–22:00 UTC |
| Asia Pacific (Sydney)                   | 12:00–20:00 UTC |
| Asia Pacific (Jakarta)                  | 15:00–23:00 UTC |
| Asia Pacific (Tokyo)                    | 13:00–21:00 UTC |
| Canada (Central)                        | 03:00–11:00 UTC |
| China (Beijing)                         | 13:00–21:00 UTC |
| China (Ningxia)                         | 13:00–21:00 UTC |
| Europe (Frankfurt)                      | 06:00–14:00 UTC |
| Europe (Zurich)                         | 20:00–04:00 UTC |
| Europe (Ireland)                        | 22:00–06:00 UTC |
| Europe (London)                         | 22:00–06:00 UTC |
| Europe (Stockholm)                      | 23:00–07:00 UTC |
| Europe (Milan)                          | 21:00–05:00 UTC |
| Europe (Spain)                          | 21:00–05:00 UTC |
| Africa (Cape Town)                      | 20:00–04:00 UTC |
| Europe (Ireland)                        | 22:00–06:00 UTC |
| Europe (London)                         | 23:00–07:00 UTC |
| Europe (Paris)                          | 23:00–07:00 UTC |
| Europe (Stockholm)                      | 23:00–07:00 UTC |
| Middle East (Bahrain)                   | 13:00–21:00 UTC |
| Middle East (UAE)                       | 18:00–02:00 UTC |
| South America (São Paulo)               | 19:00–03:00 UTC |
| Israel (Tel Aviv)                       | 20:00–04:00 UTC | ## Choose a maintenance window Managed Service for Apache Flink notifies you about upcoming planned maintenance events through email and AWS Health notifications. In Managed Service for Apache Flink, you can change the time of the day during which maintenance begins by using the `UpdateApplicationMaintenanceConfiguration` API and updating your maintenance window configuration. For more information, see [UpdateApplicationMaintenanceConfiguration](../apiv2/API_UpdateApplicationMaintenanceConfiguration.md "../apiv2/API_UpdateApplicationMaintenanceConfiguration.md"). Managed Service for Apache Flink uses the updated maintenance configuration the next time it schedules maintenance for the application. If you invoke this operation after the service has already scheduled maintenance, the service applies the configuration update the next time it schedules maintenance for the application. ###### Note To provide the highest possible security posture, Managed Service for Apache Flink does not support any exception to opt out of maintenance, pause maintenance, or perform maintenance on specific days. ## Identify when maintenance has occurred on your application You can find if Managed Service for Apache Flink has performed a maintenance action on your application by using the `ListApplicationOperations` API. The following is an example request for `ListApplicationOperations` that can help you filter the list for maintenance on the application: `{ "ApplicationName": "MyApplication", "operation": "ApplicationMaintenance" }` |
