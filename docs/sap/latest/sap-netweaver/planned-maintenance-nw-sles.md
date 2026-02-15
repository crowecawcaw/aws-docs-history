# Performing planned maintenance

The cluster connector is designed to integrate the cluster with SAP start framework (`sapstartsrv`), including the rolling kernel switch (RKS) awareness. Stopping and starting the SAP system using `sapcontrol` should not result in any cluster remediation activities as these actions are not interpreted as failures. Validate this scenario when testing your cluster.

There are different options to perform planned maintenance on nodes, resources, and the cluster.

###### Topics

- [Maintenance mode](#maintenance-mode-nw-sles "#maintenance-mode-nw-sles")
- [Placing a node in standby mode](#node-standby-nw-sles "#node-standby-nw-sles")
- [Moving a resource](#moving-resource-nw-sles "#moving-resource-nw-sles")

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

To perform maintenance on the cluster without system outage, the recommended method for moving active resources is to place the node you want to remove from the cluster in standby mode.

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
<slxhost01>:~ crm resource move grp_<SLX>_ASCS<00> <slxhost02>
INFO: Move constraint created for grp_<SLX>_ASCS<00> to <slxhost02>
INFO: Use `crm resource clear grp_<SLX>_ASCS<00>` to remove this constraint
```

Use the following command once the resources have relocated to their target location.

```
# crm resource clear grp_SLX_ASCS00
```
