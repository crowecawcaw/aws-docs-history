# Debug and troubleshoot your multicast

groups and FUOTA tasks using network analyzer

The wireless resources that you can monitor include LoRaWAN devices, LoRaWAN gateways,
and multicast groups. You can also use network analyzer to debug and troubleshoot any
issues with your FUOTA task. You can also monitor and track messages related to setup,
data transmission, and status query when the FUOTA task is in progress.

To monitor your FUOTA task, if the task contains multicast groups, you must add both
the multicast group and the devices in the group to your network analyzer configuration.
You must also activate frame info and multicast frame info to track the unicast and
multicast uplink and downlink messages that are exchanged with the multicast group and
the devices while the FUOTA task is in progress.

To monitor multicast groups, you can add them to your network analyzer configuration
and use multicast frame info to troubleshoot multicast downlink messages that are sent
to these groups. For troubleshooting devices that are attempting to join a group, where
unicast communication is used, you must also include these devices in the network
analyzer configuration. To monitor only the unicast communication with the devices in
the group, activate the frame info for your wireless devices. This approach ensures
comprehensive monitoring and diagnostics for both multicast groups and devices that are
joining the group.

The following sections describe how to debug and troubleshoot your multicast groups
and FUOTA tasks using network analyzer.

###### Topics

- [Debug FUOTA tasks that only
  contains devices](#lorawan-network-analyzer-fuota-devices "#lorawan-network-analyzer-fuota-devices")
- [Debug FUOTA tasks with
  multicast groups](#lorawan-network-analyzer-fuota-multicast "#lorawan-network-analyzer-fuota-multicast")
- [Debug devices that are
  attempting to join a multicast group](#lorawan-network-analyzer-fuota-multicast "#lorawan-network-analyzer-fuota-multicast")
- [Debug a multicast
  group session](#lorawan-network-analyzer-fuota-multicastsession "#lorawan-network-analyzer-fuota-multicastsession")

## Debug FUOTA tasks that only

contains devices

You can use network analyzer to debug a FUOTA task that only has LoRaWAN devices
added to the task. For information about adding devices to a FUOTA task, see [Add devices and multicast groups and
schedule FUOTA session](lorawan-fuota-add-devices.md "lorawan-fuota-add-devices.md").
To debug the FUOTA task, perform the following steps:

1. Create a network analyzer configuration by activating frame info for the
   wireless devices so that you can monitor the FUOTA uplink and downlink
   messages that are exchanged with the devices while the task is in
   progress.
2. Add the devices in your FUOTA task to the network analyzer configuration
   by using their wireless device identifiers.
3. Activate trace messaging to start receiving trace messages for the devices
   in your network analyzer configuration.

In the `applicationCommandType` column of the trace message
information, you'll start receiving unicast downlink messages related to data
transmission and fragmentation setup.

###### Note

If you don't see the `applicationCommandType` column in the trace
message table, you can adjust the settings to show this column in the
table.

You can also see the `applicationCommandType` and other detailed
messages in the JSON log message under **WirelessMetadata >
ApplicationInfo**.

## Debug FUOTA tasks with

multicast groups

You can use network analyzer to debug a FUOTA task that has multicast groups and
LoRaWAN devices added to the group. For information about adding devices to a FUOTA
task, see [Add devices and multicast groups and
schedule FUOTA session](lorawan-fuota-add-devices.md "lorawan-fuota-add-devices.md"). To debug the FUOTA task, perform
the following steps:

1. Create a network analyzer configuration by activating the frame info and
   multicast frame info settings for the wireless devices and multicast
   groups.
2. Add the multicast group in your FUOTA task to the network analyzer
   configuration by using their multicast group identifier. By enabling
   multicast frame info, you can debug the firmware data message and FUOTA
   status query messages that are sent to the group while the FUOTA task is in
   progress.
3. Add the devices in your multicast group to the network analyzer
   configuration by using their wireless device identifiers. By activating
   frame info, you can monitor uplink and downlink messages that are exchanged
   directly with the devices while the FUOTA task is in progress.
4. Activate trace messaging to start receiving trace messages for the devices
   and multicast groups in your network analyzer configuration.

You can then view the trace messages and debug them using the
`applicationCommandType` column of the trace message table and using
the details in the JSON log message as described in [Debug FUOTA tasks that only
contains devices](#lorawan-network-analyzer-fuota-devices "#lorawan-network-analyzer-fuota-devices").

## Debug devices that are

attempting to join a multicast group

You can use network analyzer to debug devices that are attempting to join a
multicast group. For information about adding devices to a multicast group, see
[Create multicast groups and add
devices to the group](lorawan-create-multicast-groups.md "lorawan-create-multicast-groups.md"). To debug the multicast group,
perform the following steps:

1. Create a network analyzer configuration by activating frame info for the
   wireless devices.
2. Add the devices you want to monitor to the network analyzer configuration
   by using their wireless device identifiers.
3. Activate trace messaging to start receiving trace messages for the devices
   in your network analyzer configuration.
4. Start associating the devices to the multicast group after trace messaging
   has been activated for the devices in the group.

## Debug a multicast

group session

You can use network analyzer to debug a multicast group session. For more
information, see [Schedule a downlink message
for your multicast group](lorawan-multicast-schedule-downlink.md "lorawan-multicast-schedule-downlink.md"). To debug a multicast
group session, perform the following steps:

1. Create a network analyzer configuration by activating multicast frame info
   for the multicast group.
2. Add the multicast group that you want to monitor to the network analyzer
   configuration by using their multicast group identifier.
3. Before the multicast session starts, activate trace messaging to start
   receiving trace messages for the multicast group session.
4. Start the multicast group session and monitor the status by viewing the
   messages that are displayed in the trace message table and the JSON log
   message.

In the trace message table, the `MulticastAddr` will be displayed in
the `DevAddr` column. In the JSON log message, you can view detailed
information such as the `MulticastGroupId` under
**WirelessMetadata > ApplicationInfo**.
