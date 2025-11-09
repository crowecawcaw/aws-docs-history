# Management Information Bases (MIBs) in Elemental Live

AWS Elemental provides the following management information bases (MIBs) for use with
Elemental Live:

ELEMENTAL-MIB

ELEMENTAL-MIB is the base MIB for all AWS Elemental products. The following table
describes the variables included in this MIB.

| Variable           | Values                                                                      |
| ------------------ | --------------------------------------------------------------------------- |
| `serviceStatus`    | • 0 if the Elemental Live isn't running.<br>• 1 if it is running.           |
| `firewallSettings` | • 0 if the node firewall is off.<br>• 1 if it is on.                        |
| `networkSettings`  | Always 1. Required for some network management<br>systems.                  |
| `mountPoints`      | Number of user-mounted filesystems in `/mnt`.                               |
| `version`          | The version of the Elemental Live node.                                     |
| `httpdStatus`      | • 0 if the `httpd` service isn't running.<br>• 1 if it is running.          |
| `databaseBackup`   | • 0 if writes (starting backups) is allowed.<br>• 1 if they aren't allowed. |

ELEMENTAL-LIVE-MIB
ELEMENTAL-LIVE-MIB describes objects that are specific to Elemental Live. The following
table describes the variables included in this
MIB.

| Variable       | Values                                                                           |
| -------------- | -------------------------------------------------------------------------------- |
| `eventId`      | The numerical ID of the live event. This is the index to the<br>liveEventsTable. |
| `eventName`    | The name of the live event.                                                      |
| `eventRunning` | • 0 if the event isn't running.<br>• 1 if it is running.                         |
| `eventError`   | • 0 if the event isn't in an error state.<br>• 1 if it is in an error state.     |
| `eventStatus`  | Status information about the live event. Formatted in XML.                       |
| `nodeId`       | The numerical ID of the node that the event is running on.                       |

Both the ELEMENTAL-MIB and ELEMENTAL-LIVE-MIB come installed on Elemental Live. They
are located in `/opt/elemental_se/web/public/mib/`.

For more information, access the Elemental Live web interface, go to the **Support** page and choose **SNMP Interface**.
