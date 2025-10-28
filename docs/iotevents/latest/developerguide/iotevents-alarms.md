End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Monitoring with alarms in AWS IoT Events

AWS IoT Events alarms help you monitor your data for changes. The data can be metrics that you
measure for your equipment and processes. You can create alarms that send notifications when
a threshold is breached. Alarms help you detect issues, streamline maintenance, and optimize
performance of your equipment and processes.

Alarms are instances of alarm models. The alarm model specifies what to detect, when to
send notifications, who gets notified, and more. You can also specify one or more [supported actions](iotevents-supported-actions.md "iotevents-supported-actions.md") that
occur when the alarm state changes. AWS IoT Events routes [input attributes](iotevents-detector-input.md "iotevents-detector-input.md") derived
from your data to the appropriate alarms. If the data that you're monitoring is outside the
specified range, the alarm is invoked. You can also acknowledge the alarms or set them to
the snooze mode.

## Working with AWS IoT SiteWise

You can use AWS IoT Events alarms to monitor asset properties in AWS IoT SiteWise. AWS IoT SiteWise sends asset
property values to AWS IoT Events alarms. AWS IoT Events sends the alarm state to AWS IoT SiteWise.

AWS IoT SiteWise also supports external alarms. You might choose external alarms if you use
alarms outside of AWS IoT SiteWise and have a solution that returns alarm state data. The external
alarm contains a measurement property that ingests the alarm state data.

AWS IoT SiteWise doesn't evaluate the state of external alarms. Additionally, you can't
acknowledge or snooze an external alarm when the alarm state changes.

You can use the SiteWise Monitor feature to view the state of external alarms in SiteWise Monitor
portals.

For more information, see [Monitoring data with alarms](../../../iot-sitewise/latest/userguide/industrial-alarms.md "../../../iot-sitewise/latest/userguide/industrial-alarms.md") in the _AWS IoT SiteWise User Guide_
and [Monitoring with alarms](../../../iot-sitewise/latest/appguide/monitor-alarms.md "../../../iot-sitewise/latest/appguide/monitor-alarms.md") in the _SiteWise Monitor Application
Guide_.

## Acknowledge flow

When you create an alarm model, you choose whether to enable acknowledge flow. If you
enable acknowledge flow, your team gets notified when the alarm state changes. Your team
can acknowledge the alarm and leave a note. For example, you can include the information
of the alarm and the actions that you're going to take to address the issue. If the data
that you're monitoring is outside the specified range, the alarm is invoked.

Alarms have the following states:

`DISABLED`

When the alarm is in the `DISABLED` state, it isn't ready to
evaluate data. To enable the alarm, you must change the alarm to the
`NORMAL` state.

`NORMAL`

When the alarm is in the `NORMAL` state, it's ready to evaluate
data.

`ACTIVE`

If the alarm is in the `ACTIVE` state, the alarm is invoked.
The data that you're monitoring is outside the specified range.

`ACKNOWLEDGED`

When the alarm is in the `ACKNOWLEDGED` state, the alarm was
invoked and you acknowledged the alarm.

`LATCHED`

The alarm was invoked, but you didn't acknowledge the alarm after a period
of time. The alarm automatically changes to the `NORMAL`
state.

`SNOOZE_DISABLED`

When the alarm is in the `SNOOZE_DISABLED` state, the alarm is
disabled for a specified period of time. After the snooze time, the alarm
automatically changes to the `NORMAL` state.
