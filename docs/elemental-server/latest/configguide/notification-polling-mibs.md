This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Management Information Bases (MIBs) in AWS Elemental Server

AWS Elemental provides the following management information bases (MIBs) for use with
AWS Elemental Server:

ELEMENTAL-MIB
This is the base MIB for all AWS Elemental products.

| Variable           | Values                                                                      |
| ------------------ | --------------------------------------------------------------------------- |
| `serviceStatus`    | • 0 if the AWS Elemental Server isn't running.<br>• 1 if it is running.     |
| `firewallSettings` | • 0 if the node firewall is off.<br>• 1 if it is on.                        |
| `networkSettings`  | Always 1. Required for some network management<br>systems.                  |
| `mountPoints`      | Number of user-mounted filesystems in `/mnt`.                               |
| `version`          | The version of the AWS Elemental Server node.                               |
| `httpdStatus`      | • 0 if the `httpd` service isn't running.<br>• 1 if it is running.          |
| `databaseBackup`   | • 0 if writes (starting backups) is allowed.<br>• 1 if they aren't allowed. |

ELEMENTAL-SERVER-MIB
This MIB describes objects that are specific to AWS Elemental Server.

| Variable      | Values                                                                      |
| ------------- | --------------------------------------------------------------------------- |
| `jobId`       | The numerical ID of the job. This is the index to the<br>jobTable.          |
| `jobPending`  | • 0 if the job isn't a pending state.<br>• 1 if it is a pending state.      |
| `jobRunning`  | • 0 if the job isn't running.<br>• 1 if it is running.                      |
| `jobError`    | • 0 if the job isn't in an error state.<br>• 1 if it is in an error state.  |
| `jobComplete` | • 0 if the job isn't running complete.<br>• 1 if it is in a complete state. |
| `nodeId`      | The numerical ID of the node that the job is running on.                    |

Both the ELEMENTAL-MIB and ELEMENTAL-LIVE-MIB come installed on AWS Elemental Server. They
are located in `/opt/elemental_se/web/public/mib/`.

For more information, access the AWS Elemental Server web interface, go to the **Support** page and choose **SNMP Interface**.
