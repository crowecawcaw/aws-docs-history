This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Management Information Bases (MIBs) in AWS Elemental Statmux

AWS Elemental provides the following management information bases (MIBs) for use with
AWS Elemental Statmux:

ELEMENTAL-MIB
This is the base MIB for all AWS Elemental products.

| Variable           | Values                                                                      |
| ------------------ | --------------------------------------------------------------------------- |
| `serviceStatus`    | • 0 if the AWS Elemental Statmux isn't running.<br>• 1 if it is running.    |
| `firewallSettings` | • 0 if the node firewall is off.<br>• 1 if it is on.                        |
| `networkSettings`  | Always 1. Required for some network management<br>systems.                  |
| `mountPoints`      | Number of user-mounted filesystems in `/mnt`.                               |
| `version`          | The version of the AWS Elemental Statmux node.                              |
| `httpdStatus`      | • 0 if the `httpd` service isn't running.<br>• 1 if it is running.          |
| `databaseBackup`   | • 0 if writes (starting backups) is allowed.<br>• 1 if they aren't allowed. |

ELEMENTAL-MIB comes installed on AWS Elemental Statmux. It's located in
`/opt/elemental_se/web/public/mib/`.

For more information, access the AWS Elemental Statmux web interface, go to the **Support** page and choose **SNMP Interface**.
