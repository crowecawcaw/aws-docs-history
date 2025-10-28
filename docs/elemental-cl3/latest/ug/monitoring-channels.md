# Monitoring channels

###### Topics

- [Monitoring the health of
  channels](#monitoring-for-failure "#monitoring-for-failure")
- [Monitoring
  channel activity at the node](#monitoring-channel-activity-at-the-node "#monitoring-channel-activity-at-the-node")
- [Viewing channel
  history](#viewing-channel-history "#viewing-channel-history")

## Monitoring the health of

channels

You can monitor the status of channels as they run.

1. In the AWS Elemental Conductor Live main menu, choose **Channels** . Information
   is color-coded as follows:
   - Yellow background shading indicates that there are
     active alerts on the channel that you have not yet read
     and suppressed.
   - Red background shading indicates that the status of
     the channel is Error.

2. Display more information if you want:
   - Choose any red icon to go to the **Status –
     Messages** page. This page shows all
     messages for this channel. The error message is shaded
     red and have the same red icon.

   - Choose any orange icon to go to the **Status
     – Alerts** page. This page shows detailed
     information about any alerts for this channel.

## Monitoring

channel activity at the node

You can view information about the channel activity that is
happening at any worker node.

1. In the Conductor Live main menu, choose **Channels** .
2. Select any channel by its ID or name. The
   **Channels Details** page appears.

When a channel is running, information appears in three tabs:
**Status**, **Parameters**, and
**Logs**.

Elemental Live constantly forwards `_eme` and `_
 eme_ve` logs to Conductor Live.

Note that channel logs are displayed for 24 hours. Logs that are
from 24 hours to one-week old are held in zip files that you can
unzip if needed.

## Viewing channel

history

You can view a summarized history of the channel.

On the **Channel Details** page, choose
**History**.

Time is shown in the time zone currently configured on the
Conductor Live. The timeline captures when a channel gets created, started,
and stopped, and also includes node information.
