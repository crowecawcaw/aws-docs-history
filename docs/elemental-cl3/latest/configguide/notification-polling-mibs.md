# MIBs in Conductor Live

AWS Elemental provides the following MIBs for use with
Conductor Live:

ELEMENTAL-MIB

This is the base MIB for all AWS Elemental products.

| Variable             | Values                                                                                                                                                                       |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `serviceStatus`      | <br>• 0 if the Conductor Live isn't running. <br>• 1 if it is running.                                                                                                       |
| `firewallSettings`   | <br>• 0 if the node firewall is off. <br>• 1 if it is on.                                                                                                                    |
| `networkSettings`    | Always 1. Required for some network management systems.                                                                                                                      |
| `mountPoints`        | Number of user-mounted file systems in `/mnt`.                                                                                                                               |
| `version`            | The version of the Conductor Live node.                                                                                                                                      |
| `httpdStatus`        | <br>• 0 if the `httpd` service isn't running. <br>• 1 if it is running.                                                                                                      |
| `databaseBackup`     | <br>• 0 if writes (starting backups) is allowed. <br>• 1 if they aren't allowed.                                                                                             | ELEMENTAL-CONDUCTOR-MIB This MIB describes objects that are specific to Conductor Live.                                                  |
| Variable             | Values                                                                                                                                                                       |
| ---                  | ---                                                                                                                                                                          |
| `channelId`          | The system-assigned numerical ID of the channel.                                                                                                                             |
| `channelName`        | The user-defined name of the channel.                                                                                                                                        |
| `channelRunning`     | <br>• 0 if the channel isn't running. <br>• 1 if it is running.                                                                                                              |
| `channelError`       | <br>• 0 if the channel isn't in an error state. <br>• 1 if it is in an error state.                                                                                          |
| `channelLiveEventId` | The system-assigned ID of the event associated with the channel.                                                                                                             |
| `channelStartTime`   | Start time of the channel which is provided if the channel is currently running only.                                                                                        |
| `channelDuration`    | The duration of time that the channel has been running which is provided if the channel is currently running only.                                                           |
| `channelAlerts`      | The text bodies of any active alerts related to the channel, including the time the alert was last set. Each alert is separated by semicolons.                               |
| `channelMessages`    | The text bodies of any messages generated in the last 24 hours related to the channel, including the time the message was last set. Each message is separated by semicolons. |
| `nodeId`             | The numerical ID of the node on which the channel is running.                                                                                                                |
| `nodeHostname`       | Hostname of the node that the channel is running on.                                                                                                                         | Both the ELEMENTAL-MIB and ELEMENTAL-LIVE-MIB come installed on Conductor Live. They are located in `/opt/elemental_se/web/public/mib/`. |
