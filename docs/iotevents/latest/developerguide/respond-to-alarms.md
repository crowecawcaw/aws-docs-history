End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Responding to alarms in AWS IoT Events

Responding to alarms effectively is an important aspect of managing IoT systems with
AWS IoT Events. Explore various ways to configure and handle alarms, including: setting up
notification channels, defining escalation procedures, and implementing automated
response actions. Learn to create nuanced alarm conditions, prioritize alerts, and
integrate with other AWS services to build a responsive alarm management system for
your IoT applications.

If you enabled [acknowledge flow](iotevents-alarms.md#acknowledge-flow "iotevents-alarms.md#acknowledge-flow"), you receive notifications when the alarm state changes.
To respond to the alarm, you can acknowledge, disable, enable, reset, or snooze the
alarm.

Console
The following shows you how to respond to an alarm in the AWS IoT Events
console.

1.  Sign in to the [AWS IoT Events
    console](https://console.aws.amazon.com/iotevents/ "https://console.aws.amazon.com/iotevents/").
2.  In the navigation pane, choose **Alarm
    models**.
3.  Choose the target alarm model.
4.  In the **List of alarms** section, choose the
    target alarm.
5.  You can choose one of the following options from
    **Actions**:

        * **Acknowledge** - The alarm changes to
         the `ACKNOWLEDGED` state.
        * **Disable** - The alarm changes to the
         `DISABLED` state.
        * **Enable** - The alarm changes to the
         `NORMAL` state.
        * **Reset** - The alarm changes to the
         `NORMAL` state.
        * **Snooze**, and then do the
         following:




        	1. Choose the **Snooze length** or
        	 enter a **Custom snooze
        	 length**.
        	2. Choose **Save**.
        The alarm changes to the `SNOOZE_DISABLED`
         state

    For more information about the alarm states, see [Acknowledge flow](iotevents-alarms.md#acknowledge-flow "iotevents-alarms.md#acknowledge-flow").

API
To respond to one or more alarms, you can use the following AWS IoT Events API
operations:

- [BatchAcknowledgeAlarm](../apireference/API_iotevents-data_BatchAcknowledgeAlarm.md "../apireference/API_iotevents-data_BatchAcknowledgeAlarm.md")
- [BatchDisableAlarm](../apireference/API_iotevents-data_BatchDisableAlarm.md "../apireference/API_iotevents-data_BatchDisableAlarm.md")
- [BatchEnableAlarm](../apireference/API_iotevents-data_BatchEnableAlarm.md "../apireference/API_iotevents-data_BatchEnableAlarm.md")
- [BatchResetAlarm](../apireference/API_iotevents-data_BatchResetAlarm.md "../apireference/API_iotevents-data_BatchResetAlarm.md")
- [BatchSnoozeAlarm](../apireference/API_iotevents-data_BatchSnoozeAlarm.md "../apireference/API_iotevents-data_BatchSnoozeAlarm.md")
