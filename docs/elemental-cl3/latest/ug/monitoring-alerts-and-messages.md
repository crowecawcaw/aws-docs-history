# Monitoring alerts and

messages

AWS Elemental Conductor Live generates alerts and messages to provide information about the status of the
nodes in the cluster and about the encoding channels. This section covers how to monitor
alerts and messages via the web interface.

For information about setting up automatic email or web callback
alert notifications, and about using the SNMP and REST interfaces for
alerts and messages, see [AWS Elemental Conductor Live Configuration Guide](../configguide.md "../configguide.md").

###### Topics

- [About alerts and
  messages](#about-alerts-and-messages "#about-alerts-and-messages")
- [Alerts
  and messages on the web interface](#alerts-and-messages-on-the-web-interface "#alerts-and-messages-on-the-web-interface")

## About alerts and

messages

In the following table, read down the first column to find the
type of information that you're interested in. Then read across to
find the interfaces that provide alerts about that information and
that provide messages about that information.

| Type of information  | Alerts                                                                                                                                                                                                                                                                                                     | Messages                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access Options       | Web Interface<br>Automatic email notification<br>Web callback notification<br>SNMP trap<br>SNMP poll<br>REST calls                                                                                                                                                                                         | Web Interface<br>SNMP poll<br>REST calls                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Information Conveyed | Alerts are feedback on a problem that must be<br>fixed.<br>The \*_Channel Error_<br>• alert<br>informs you that a channel has moved to an Error<br>state.<br>This can help when you are receiving automatic<br>email notifications, to let you know to check for<br>related messages on the web interface. | Three types of messages are:<br>**AuditMessage\*\***:**<br>Informational messages that you do not need to react<br>to. Often, these messages are feedback to actions you<br>performed.<br>**WarningMessage\***\*:**<br>Messages that advise you that there is a risk that a<br>future activity will fail unless you take action to<br>prevent it.<br>**ErrorMessage**: Messages that<br>indicate that a planned activity has failed or an<br>unexpected system error has occurred. |
| Active/Inactive      | Alerts remain active until the underlying problem is<br>resolved. When the cause of the alert is no longer<br>present, the system clears the alert so that it becomes<br>inactive.                                                                                                                         | Messages are neither active nor inactive. They are<br>defined as “recent” when they are fewer than 24 hours<br>old.                                                                                                                                                                                                                                                                                                                                                                |
| Visibility           | You can toggle the visibility of active alerts.<br>Suppressing an alert this way is similar to marking<br>an email as read.<br>The section below describes where you can see<br>suppressed and unsuppressed alerts on the web<br>interface.                                                                | Only messages of the type<br>**Error\*<br>• are visible in the<br>header. You can toggle the visibility of recent error<br>messages, which is similar to marking an email as<br>**read\*\*.<br>The section below describes where you can see<br>suppressed and unsuppressed messages on the web<br>interface.                                                                                                                                                                      |

## Alerts

and messages on the web interface

Conductor Live provides information about alerts and messages in two
places:

- On the header of every page.
- In more detail on the pages **Status –
  Alerts** and **Status –
  Messages**.

### Web interface

header: Alerts

The web interface header, located at the top of all pages of
the web interface, shows a count of alerts that are both active
and visible:

- Active: the condition that is causing the alert still
  exists.
- Visible: no user has marked the alert as _read_.

The count is in a red circle to the right of the information
(**i**) icon.

1. Select the red circle to display a pop-up list of the
   ten most recent active, visible alerts.
2. Optionally, choose the suppress (**x**)
   icon to dismiss this alert. The alert will remain active
   until the underlying cause is resolved. It won't appear in
   the popup list. But it is still listed in the
   **Status – Alerts** page, under the
   **Active** tab.

You can unsuppress the alert on the **Status –
Messages** page.

### Web interface

header: Messages

The web interface header, located at the top of all pages of
the web interface, shows a count of error messages that are both
recent and visible:

- Active: the messages was created in the last 24
  hours.
- Visible: no user has marked the alert as _read_.

The count is in a red circle to the right of the information
(**i**) icon.

1. Select the red circle to display a pop-up list of the
   ten most recent, visible alerts.
2. Optionally, choose the **Suppress**
   (**x**) icon to dismiss this alert. The
   alert will remain active until the underlying cause is
   resolved. It won't appear in the popup list. But it is
   still listed in the **Status – Alerts**
   page, under the **Active** tab.

You can unsuppress the alert on the **Status –
Messages** page.

### Status – Alerts

page

On the Conductor Live main menu, choose **Status**.
Then choose **Alerts** in the left panel.

The **Alerts** page contains three tabs, for
active, inactive, and all alerts.

Each tab shows the same information:

- The unique code for the alert
- The type and the message wording

- Whether the alert is visible. On the active tab, you can
  select this icon to change the alert between visible and
  invisible.

- The node and associate for this alert. The association
  identifies the target of the alert, for example, a
  channel.

You can choose the **Alert Filters** button
at the top right corner to filter alerts.

### Status - Messages

page

On the Conductor Live main menu, choose **Status**.
Then choose **Messages** in the left
panel.

The page shows the following information:

- The unique code for the message.
- The type. Messages are error messages, warning messages,
  and audit messages.
- Error messages have red shading and a red triangle icon.
  Only error messages are included in the message count on
  the web interface header.
- The message wording.

- Whether the message is visible. You can select this icon
  on an error message, to change the message between visible
  and invisible.

- The node and associate for this message. The association
  identifies the target of the message, for example, a
  channel.

You can choose the **Message Filters** button
at the top right corner to filter messages.
