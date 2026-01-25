# Performing planned maintenance

When performing maintenance on SAP HANA systems in a cluster environment, it’s important to understand how the cluster interacts with SAP HANA system replication. Planned maintenance activities should be conducted carefully to prevent unnecessary failovers or cluster interventions.

There are different options to perform planned maintenance on nodes, resources, and the cluster.

###### Topics

- [Maintenance mode](#_maintenance_mode "#_maintenance_mode")
- [Placing a node in standby mode](#_placing_a_node_in_standby_mode "#_placing_a_node_in_standby_mode")
- [Moving a resource](#_moving_a_resource "#_moving_a_resource")

## Maintenance mode

Use maintenance mode if you want to make any changes to the configuration or take control of the resources and nodes in the cluster. In most cases, this is the safest option for administrative tasks.

On
Use the following commands to turn on maintenance mode.

```
# pcs property maintenance-mode=true
```

Off
Use the following command to turn off maintenance mode.

```
# pcs property maintenance-mode=false
```

## Placing a node in standby mode

To perform maintenance on the cluster without a full system outage, the recommended method for moving active resources is to place the node you want to remove from the cluster in standby mode.

```
# pcs node standby <hostname>
```

The cluster will cleanly relocate resources, and you can perform activities, including reboots on the node in standby mode. When maintenance activities are complete, you can re-introduce the node with the following command.

```
# pcs node unstandby <hostname>
```

## Moving a resource

When moving individual resources, be sure you understand resource dependencies and constraints. The following commands demonstrate how to force a HANA takeover. Always review the cluster status and verify any temporary location constraints afterwards.

For example:

```
# pcs resource move rsc_SAPHana_HDB_HDB00-clone hanahost02
Location constraint to move resource 'rsc_SAPHana_HDB_HDB00-clone' has been created
Waiting for the cluster to apply configuration changes...
Location constraint created to move resource 'rsc_SAPHana_HDB_HDB00-clone' has been removed
Waiting for the cluster to apply configuration changes...
resource 'rsc_SAPHana_HDB_HDB00-clone' is promoted on node 'hanahost02'; unpromoted on node 'hanahost01'
```

Note: The exact resource name will vary depending on your SAP HANA system ID and instance number. Adjust the commands accordingly.
