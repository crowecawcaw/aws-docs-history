# Performing planned maintenance

When performing maintenance on SAP HANA systems in a cluster environment, it’s important to understand how the cluster interacts with SAP HANA system replication. Planned maintenance activities should be conducted carefully to prevent unnecessary failovers or cluster interventions.

There are different options to perform planned maintenance on nodes, resources, and the cluster.

###### Topics

- [Maintenance mode](#_maintenance_mode "#_maintenance_mode")
- [Placing a node in standby mode](#_placing_a_node_in_standby_mode "#_placing_a_node_in_standby_mode")
- [Moving a resource](#_moving_a_resource "#_moving_a_resource")

## Maintenance mode

Use maintenance mode if you want to make any changes to the configuration or take control of the resources and nodes in the cluster. In most cases, this is the safest option for administrative tasks.

###### Example

On
Use one of the following commands to turn on maintenance mode.

```
# crm maintenance on
```

```
# crm configure property maintenance-mode="true"
```

Off
Use one of the following commands to turn off maintenance mode.

```
# crm maintenance off
```

```
# crm configure property maintenance-mode="false"
```

## Placing a node in standby mode

To perform maintenance on the cluster without a full system outage, the recommended method for moving active resources is to place the node you want to remove from the cluster in standby mode.

```
# crm node standby <hostname>
```

The cluster will cleanly relocate resources, and you can perform activities, including reboots on the node in standby mode. When maintenance activities are complete, you can re-introduce the node with the following command.

```
# crm node online <hostname>
```

## Moving a resource

Moving individual resources is not recommended because of the migration or move constraints that are created to lock the resource in its new location. These can be cleared as described in the info messages, but this introduces an additional setup.

```
 # crm resource move msl_SAPHanaController_HDB_HDB00 hanahost02
INFO: Move constraint created for msl_SAPHanaController_HDB_HDB00 to hanahost02
INFO: Use `crm resource clear msl_SAPHanaController_HDB_HDB00` to remove this constraint
```

Note: The exact resource name will vary depending on your SAP HANA system ID and instance number. Adjust the commands accordingly.

Use the following command once the resources have relocated to their target location.

```
# crm resource clear msl_SAPHanaController_HDB_HDB00
```
