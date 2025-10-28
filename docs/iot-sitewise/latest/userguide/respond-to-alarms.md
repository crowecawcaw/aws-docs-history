# Respond to alarms in AWS IoT SiteWise

When an AWS IoT Events alarm changes state, you can do the
following to respond to the alarm:

- Acknowledge an alarm to indicate that you are handling the issue.
- Snooze an alarm to disable it temporarily.
- Disable an alarm to disable it permanently until you enable it again.
- Enable a disabled alarm to detect alarm state.
- Reset an alarm to clear its state and latest value.
  You can use the AWS IoT SiteWise console or the AWS IoT Events API to respond to an alarm.

###### Note

You can respond to AWS IoT Events alarms, but not external alarms.

###### Topics

- [Respond to an alarm (console)](#respond-to-alarm-console "#respond-to-alarm-console")
- [Respond to an alarm (API)](#respond-to-alarm-cli "#respond-to-alarm-cli")

## Respond to an alarm (console)

You can use the AWS IoT SiteWise console to acknowledge, snooze, disable, or enable an
alarm.

###### Topics

- [Acknowledge an alarm (console)](#acknowledge-alarm-console "#acknowledge-alarm-console")
- [Snooze an alarm (console)](#snooze-alarm-console "#snooze-alarm-console")
- [Disable an alarm (console)](#disable-alarm-console "#disable-alarm-console")
- [Enable an alarm (console)](#enable-alarm-console "#enable-alarm-console")
- [Reset an alarm (console)](#reset-alarm-console "#reset-alarm-console")

### Acknowledge an alarm (console)

You can acknowledge an alarm to indicate that you're handling the issue.

###### Note

You must enable the acknowledge flow on the alarm so that you can acknowledge the
alarm. This option is enabled by default if you define the alarm from the AWS IoT SiteWise
console.

###### To acknowledge an alarm (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Assets**.
3. Choose the asset to for which you want to acknowledge an alarm.

###### Tip

You can choose the arrow icon to expand an asset hierarchy to find your
asset. 4. Choose the **Alarms** tab. 5. Select the alarm to acknowledge, and then choose **Actions** to
open the response action menu. 6. Choose **Acknowledge**. The alarm's state changes to
**Acknowledged**.

### Snooze an alarm (console)

You can snooze an alarm to disable it temporarily. Specify the duration for which to
snooze the alarm.

###### To snooze an alarm (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Assets**.
3. Choose the asset to for which you want to snooze an alarm.

###### Tip

You can choose the arrow icon to expand an asset hierarchy to find your
asset. 4. Choose the **Alarms** tab. 5. Select the alarm to snooze, and then choose **Actions** to open
the response action menu. 6. Choose **Snooze**. A model opens where you specify the duration
to snooze. 7. Choose the **Snooze length** or enter a **Custom snooze
length**. 8. Choose **Save**. The alarm's state changes to
**Snoozed**.

### Disable an alarm (console)

You can disable an alarm so that it doesn't detect anymore. After you disable the
alarm, you must enable it again if you want the alarm to detect.

###### To disable an alarm (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Assets**.
3. Choose the asset to for which you want to disable an alarm.

###### Tip

You can choose the arrow icon to expand an asset hierarchy to find your
asset. 4. Choose the **Alarms** tab. 5. Select the alarm to disable, and then choose **Actions** to open
the response action menu. 6. Choose **Disable**. The alarm's state changes to
**Disabled**.

### Enable an alarm (console)

You can enable an alarm to detect again after you disable or snooze it.

###### To enable an alarm (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Assets**.
3. Choose the asset to for which you want to enable an alarm.

###### Tip

You can choose the arrow icon to expand an asset hierarchy to find your
asset. 4. Choose the **Alarms** tab. 5. Select the alarm to enable, and then choose **Actions** to open
the response action menu. 6. Choose **Enable**. The alarm's state changes to
**Normal**.

### Reset an alarm (console)

You can reset an alarm to clear its state and latest value.

###### To reset an alarm (console)

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Assets**.
3. Choose the asset to for which you want to reset an alarm.

###### Tip

You can choose the arrow icon to expand an asset hierarchy to find your
asset. 4. Choose the **Alarms** tab. 5. Select the alarm to enable, and then choose **Actions** to open
the response action menu. 6. Choose **Reset**. The alarm's state changes to
**Normal**.

## Respond to an alarm (API)

You can use the AWS IoT Events API to acknowledge, snooze, disable, enable, or reset an alarm.
For more information, see the following operations in the
_AWS IoT Events API Reference_:

- [BatchAcknowledgeAlarm](../../../iotevents/latest/apireference/API_iotevents-data_BatchAcknowledgeAlarm.md "../../../iotevents/latest/apireference/API_iotevents-data_BatchAcknowledgeAlarm.md")
- [BatchSnoozeAlarm](../../../iotevents/latest/apireference/API_iotevents-data_BatchSnoozeAlarm.md "../../../iotevents/latest/apireference/API_iotevents-data_BatchSnoozeAlarm.md")
- [BatchDisableAlarm](../../../iotevents/latest/apireference/API_iotevents-data_BatchDisableAlarm.md "../../../iotevents/latest/apireference/API_iotevents-data_BatchDisableAlarm.md")
- [BatchEnableAlarm](../../../iotevents/latest/apireference/API_iotevents-data_BatchEnableAlarm.md "../../../iotevents/latest/apireference/API_iotevents-data_BatchEnableAlarm.md")
- [BatchResetAlarm](../../../iotevents/latest/apireference/API_iotevents-data_BatchResetAlarm.md "../../../iotevents/latest/apireference/API_iotevents-data_BatchResetAlarm.md")

For more information, see [Responding to alarms](../../../iotevents/latest/developerguide/respond-to-alarms.md "../../../iotevents/latest/developerguide/respond-to-alarms.md")
in the _AWS IoT Events Developer Guide_.
