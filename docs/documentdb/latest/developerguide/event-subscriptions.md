# Amazon DocumentDB event categories and messages

Amazon DocumentDB generates a significant number of events in categories that you can subscribe to
using the console. Each category applies to a source type, which can be an instance,
cluster, snapshot, or parameter group.

###### Note

Amazon DocumentDB uses existing Amazon RDS event definitions and IDs.

## Amazon DocumentDB events originating from instances

| Category             | Description                                                                                                                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| availability         | The instance restarted.                                                                                                                                                                     |
| availability         | The instance shutdown.                                                                                                                                                                      |
| configuration change | Applying modification to an instance class.                                                                                                                                                 |
| configuration change | Finished applying modification to an instance class.                                                                                                                                        |
| configuration change | Reset primary credentials.                                                                                                                                                                  |
| creation             | Instance created.                                                                                                                                                                           |
| deletion             | Instance deleted                                                                                                                                                                            |
| failure              | The instance has failed due to an incompatible configuration or an underlying storage issue. Begin a point-in-time-restore for the instance.                                                |
| notification         | Instance stopped.                                                                                                                                                                           |
| notification         | Instance started.                                                                                                                                                                           |
| notification         | Instance is being started due to it exceeding the maximum allowed time being stopped.                                                                                                       |
| recovery             | Recovery of the instance has started. Recovery time will vary with the amount of data to be recovered.                                                                                      |
| recovery             | Recovery of the instance is complete.                                                                                                                                                       |
| security patching    | The operating system update is available for your instance. For information about applying updates, see [Maintaining Amazon DocumentDB](db-instance-maintain.md "db-instance-maintain.md"). | ## Amazon DocumentDB events originating from a cluster                                                                                                                                         |
| Category             | Description                                                                                                                                                                                 |
| ---                  | ---                                                                                                                                                                                         |
| creation             | Cluster created                                                                                                                                                                             |
| deletion             | Cluster deleted.                                                                                                                                                                            |
| failover             | Promoting previous primary again.                                                                                                                                                           |
| failover             | Completed failover to instance.                                                                                                                                                             |
| failover             | Started failover to DB instance: %s                                                                                                                                                         |
| failover             | Started same AZ failover to DB instance: %s                                                                                                                                                 |
| failover             | Started cross AZ failover to DB instance: %s                                                                                                                                                |
| maintenance          | Cluster has been patched.                                                                                                                                                                   |
| maintenance          | Database cluster is in a state that cannot be upgraded: %s                                                                                                                                  |
| notification         | The cluster stopped.                                                                                                                                                                        |
| notification         | The cluster started.                                                                                                                                                                        |
| notification         | The cluster stop failed.                                                                                                                                                                    |
| notification         | The cluster is being started due to it exceeding the maximum allowed time being stopped.                                                                                                    |
| notification         | Renamed cluster from %s to %s.                                                                                                                                                              | ## Amazon DocumentDB events originating from cluster snapshot The following table shows the event category and a list of events when an Amazon DocumentDB cluster snapshot is the source type. |
| Category             | Description                                                                                                                                                                                 |
| ---                  | ---                                                                                                                                                                                         |
| backup               | Creating manual cluster snapshot.                                                                                                                                                           |
| backup               | Manual cluster snapshot created.                                                                                                                                                            |
| backup               | Creating automated cluster snapshot.                                                                                                                                                        |
| backup               | Automated cluster snapshot created.                                                                                                                                                         | ## Amazon DocumentDB events originating from parameter group The following table shows the event category and a list of events when a parameter group is the source type.                      |
| Category             | Description                                                                                                                                                                                 |
| ---                  | ---                                                                                                                                                                                         |
| configuration change | Updated parameter %s to %s with apply method %s                                                                                                                                             |
