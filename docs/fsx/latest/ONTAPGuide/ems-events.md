# Monitoring FSx for ONTAP EMS events

You can monitor FSx for ONTAP file system events using NetAPP ONTAP's
native Events Management System (EMS). You can view these events using the NetApp
ONTAP CLI.

###### Topics

- [Overview of EMS events](#ems-events-overview "#ems-events-overview")
- [Viewing EMS events](#view-ems-events "#view-ems-events")
- [EMS event forwarding to a Syslog server](#ems-log-forwarding "#ems-log-forwarding")

## Overview of EMS events

EMS events are automatically generated notifications that alert you when a predefined
condition occurs in your FSx for ONTAP file system. These notifications keep you informed so
that you can prevent or correct issues that can lead to larger problems, such as storage
virtual machine (SVM) authentication issues or full volumes.

By default, events are logged in the Event Management System log. Using EMS, you can
monitor events such as user password changes, a constituent within a FlexGroup approaching
full capacity, a Logical Unit Number (LUN) was manually brought online or offline, or a volume automatically
resizing.

For more information about ONTAP EMS events, see [ONTAP EMS Reference](https://docs.netapp.com/us-en/ontap-ems-9121/index.html "https://docs.netapp.com/us-en/ontap-ems-9121/index.html") in
the NetApp ONTAP Documentation Center. To display the event categories, use the document's
left navigation pane.

###### Note

Only some ONTAP EMS messages are available for FSx for ONTAP file systems.
To view a list of the available ONTAP EMS messages, use the NetApp ONTAP CLI
[event catalog show](https://docs.netapp.com/us-en/ontap-cli-9131/event-catalog-show.html "https://docs.netapp.com/us-en/ontap-cli-9131/event-catalog-show.html")
command.

EMS event descriptions contain event names, severity, possible causes, log messages, and
corrective actions that can help you decide how to respond. For example, a [wafl.vol.autoSize.fail](https://docs.netapp.com/us-en/ontap-ems-9121/wafl-vol-events.html#wafl-vol-autosize-fail "https://docs.netapp.com/us-en/ontap-ems-9121/wafl-vol-events.html#wafl-vol-autosize-fail") event occurs when automatic sizing of a volume fails.
According to the event description, the corrective action is to increase the maximum size of
the volume while setting the autosize.

## Viewing EMS events

Use the NetApp ONTAP CLI
[event log show](https://docs.netapp.com/us-en/ontap-cli-9131/event-log-show.html "https://docs.netapp.com/us-en/ontap-cli-9131/event-log-show.html")
command to display the contents of the events log. This command is available if you have the
`fsxadmin` role on your file system. The command syntax is as follows:

```
event log show [`event_options`]
```

The most recent events are listed first. By default, this command displays
`EMERGENCY`, `ALERT`, and `ERROR` severity-level events
with the following information:

- **Time** – The time of the event.
- **Node** – The node on which the event occurred.
- **Severity** – The severity level of the event. To display
  `NOTICE`, `INFORMATIONAL`, or `DEBUG` severity-level
  events, use the `-severity` option.
- **Event** – The event name and message.

To display detailed information about events, use one or more of the event options listed in the following table.

| Event option                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `-detail`                          | Displays additional event information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `-detailtime`                      | Displays detailed event information in reverse chronological order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `-instance`                        | Displays detailed information about all fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `-node `nodename`                  | local`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Displays a list of events for the node that you specify. Use this option<br>with `-seqnum` to display detailed information. |
| `-seqnum `sequence_number``        | Selects the events that match this number in the sequence. Use with `-node` to<br>display detailed information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `-time `MM/DD/YYYY HH:MM:SS``      | Selects the events that happened at this specific time. Use the format:<br>MM/DD/YYYY HH:MM:SS [+<br>• HH:MM]. You can specify a time range by using the `..`<br>operator between two time statements.<br>`<br>event log show -time "04/17/2023 05:55:00".."04/17/2023 06:10:00"<br>`<br>Comparative time values are relative to the current time when you run the command.<br>The following example shows how to display only events that occurred within the last minute:<br>`<br>event log show -time >1m<br>`<br>The month and date fields of this option are not zero-padded. These fields can<br>be single digits; for example, `4/1/2023 06:45:00`.                                                                                                                                                                                                                                                                   |
| `-severity `sev_level``            | Selects the events that match the `sev_level` value, which<br>must be one of the following:<br>• `EMERGENCY` – Disruption<br>• `ALERT` – Single point of failure<br>• `ERROR` – Degradation<br>• `NOTICE` – Information<br>• `INFORMATIONAL` – Information<br>• `DEBUG` – Debug information<br>To display all events, specify severity as follows:<br>`<br>event log show -severity <=DEBUG<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `-ems-severity `ems_sev_level``    | Selects the events that match the `ems_sev_level` value, which<br>must be one of the following:<br>• `NODE_FAULT` – Data corruption is detected<br>or the node is unable to provide client service.<br>• `SVC_FAULT` – A temporary loss of service—typically<br>a transient software fault—is detected.<br>• `NODE_ERROR` – A hardware error that's not immediately fatal<br>is detected.<br>• `SVC_ERROR` – A software error that's not immediately fatal<br>is detected.<br>• `WARNING` – A high-priority message that doesn't<br>indicate a fault.<br>• `NOTICE` – A normal-priority message that doesn't<br>indicate a fault.<br>• `INFO` – A low-priority message that doesn't<br>indicate a fault.<br>• `DEBUG` – A debugging message.<br>• `VAR` – A message with variable severity, selected<br>at runtime.<br>To display all events, specify severity as follows:<br>`<br>event log show -ems-severity <=DEBUG<br>` |
| `-source `text``                   | Selects the events that match the `text`<br>value. The source is typically a software module.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `-message-name `message_name``     | Selects the events that match the `message_name` value.<br>Message names are descriptive, so filtering output by message name displays messages<br>of a specific type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `-event `text``                    | Selects the events that match the `text` value.<br>The `event` field contains the full text of the event, including any<br>parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `-kernel-generation-num `integer`` | Selects the events that match the `integer` value. Only<br>events that come from the kernel have kernel generation numbers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `-kernel-sequence-num `integer``   | Selects the events that match the `integer` value. Only<br>events that come from the kernel have kernel sequence numbers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `-action `text``                   | Selects the events that match the `text` value.<br>The `action` field describes what corrective action, if any, you<br>must take to remedy the situation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `-description `text``              | Selects the events that match the `text` value.<br>The `description` field describes why the event happened<br>and what it means.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `-filter-name `filter_name``       | Selects the events that match the `filter_name` value.<br>Only events that are included by existing filters that match this value display.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `-fields `fieldname`,...`          | Indicates that the command output also includes the specified field or fields. You can use<br>`-fields ?` to choose the fields that you want to specify.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

###### To view EMS events

1. To SSH into the NetApp ONTAP CLI of your file system, follow the steps documented in
   the [Using the NetApp ONTAP CLI](managing-resources-ontap-apps.md#netapp-ontap-cli "managing-resources-ontap-apps.md#netapp-ontap-cli") section of the
   _Amazon FSx for NetApp ONTAP User Guide_.

```
`ssh fsxadmin@`file-system-management-endpoint-ip-address``
```

2. Use the `event log show` command to display the contents of the event log.

```
`::>` `event log show`
`Time Node Severity Event
------------------- ------------- ------------- ------------------------
6/30/2023 13:54:19 node1 NOTICE vifmgr.portup: A link up event was received on node node1, port e0a.
6/30/2023 13:54:19 node1 NOTICE vifmgr.portup: A link up event was received on node node1, port e0d.`
```

For information about the EMS events returned by the `event log show` command, refer to the
[ONTAP EMS Reference](https://docs.netapp.com/us-en/ontap-ems-9121/index.html "https://docs.netapp.com/us-en/ontap-ems-9121/index.html") in the
NetApp ONTAP Documentation Center.

## EMS event forwarding to a Syslog server

You can configure EMS events to forward notifications to a Syslog server.
EMS event forwarding is used for real-time monitoring of your file system to
determine and isolate root causes for a wide range of issues. If your environment
doesn't already contain a Syslog server for event notifications, you must first
create one. DNS must be configured on the file system to resolve the Syslog
server name.

###### Note

Your Syslog destination must be located in the primary subnet that is used
by your file system.

###### To configure EMS events to forward notifications to a Syslog server

1. To SSH into the NetApp ONTAP CLI of your file system, follow the steps documented in
   the [Using the NetApp ONTAP CLI](managing-resources-ontap-apps.md#netapp-ontap-cli "managing-resources-ontap-apps.md#netapp-ontap-cli") section of the
   _Amazon FSx for NetApp ONTAP User Guide_.

```
`ssh fsxadmin@`file-system-management-endpoint-ip-address``
```

2. Use the [event notification destination create](https://docs.netapp.com/us-en/ontap-cli-9131/event-notification-destination-create.html "https://docs.netapp.com/us-en/ontap-cli-9131/event-notification-destination-create.html")
   command to create an event notification destination of type `syslog`, specifying the following attributes:
   - `dest_name` – The name of the notification destination
     that is to be created (for example, `syslog-ems`). An event notification destination name must be 2 to 64
     characters long. Valid characters are the following ASCII characters: A-Z, a-z, 0-9, "\_", and "-". The name must
     start and end with: A-Z, a-z, or 0-9.
   - `syslog_name` – The Syslog server host name or IP address that
     Syslog messages are sent to.
   - `transport_protocol` – The protocol used to send the events:
     - `udp-unencrypted` – User Datagram Protocol with no security.
       This is the default protocol.
     - `tcp-unencrypted` – Transmission Control Protocol with no security.
     - `tcp-encrypted` – Transmission Control Protocol with Transport Layer Security (TLS).
       When this option is specified, FSx for ONTAP verifies the identity of the destination host by validating its certificate.

   - `port_number` – The Syslog server port that Syslog messages are sent to.
     The default value `syslog-port` parameter depends on the setting for the `syslog-transport` parameter.
     If `syslog-transport` is set to `tcp-encrypted`, the `syslog-port` default value is
     `6514`. If `syslog-transport` is set to `tcp-unencrypted`, `syslog-port` has
     the default value `601`. Otherwise, the default port is set to `514`.

```
`::>` `event notification destination create -name `dest_name` -syslog `syslog_name` -syslog-transport `transport_protocol` -syslog-port `port_number``
```

3. Use the [event notification create](https://docs.netapp.com/us-en/ontap-cli-9131/event-notification-create.html "https://docs.netapp.com/us-en/ontap-cli-9131/event-notification-create.html")
   command to create a new notification of a set of events defined by an event filter to the notification destination
   created in the previous step, specifying the following attributes:
   - `node_name` – The name of the event filter. Events that are included
     in the event filter are forwarded to the destinations specified in the `-destinations` parameter.
   - `dest_name` – The name of the existing notification destination
     that the event notifications are sent to.

```
`::>` `event notification create -filter-name `filter_name` -destinations `dest_name``
```

4. If you selected TCP as the `transport_protocol`, you can use the
   `event notification destination check` command to generate a test message and verify your setup works.
   Specify the following attributes with the command:
   - `node_name` – The name of the node (for example,
     `FsxId07353f551e6b557b4-01`).
   - `dest_name` – The name of the existing notification destination
     that the event notifications are sent to.

```
`::>` `set diag`
`::*>` `event notification destination check -node `node_name` -destination-name `dest_name``
```
