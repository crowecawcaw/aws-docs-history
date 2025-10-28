# Disabling the As Run log

To disable the As Run log for a channel that has it enabled, specify the channel
name and disable the _As Run_ log type for that channel.

Console

###### To disable the As Run log when updating a channel

###### Note

If the channel is currently running, you must first stop that
channel before you can update it. After you stop the channel,
you can choose **Actions** >
**Edit** to begin updating the
channel.

1. Sign in to the AWS Management Console and open the MediaTailor console at [https://console.aws.amazon.com/mediatailor/](https://console.aws.amazon.com/mediatailor/ "https://console.aws.amazon.com/mediatailor/").
2. In the navigation pane, choose **Channel
   assembly** > **Channels**.
3. Choose the channel that you want to update to enable the As
   Run log for.
4. Choose **Actions** >
   **Edit**.
5. In the **Set channel details**,
   **Configure outputs**, and **Access
   control** panes, update your channel configuration
   as desired.
6. In the **Access control** pane, choose
   **Next**.
7. In the **Logging** pane, under **Log
   types**, clear **Enable as run**
   to disable the As Run log.

###### To disable the As Run log from the **Logging**

tab

###### Note

If the channel is currently running, you must use the
**Logging** tab instead of choosing
**Actions** > **Edit** to
disable the As Run log.

1. Sign in to the AWS Management Console and open the MediaTailor console at [https://console.aws.amazon.com/mediatailor/](https://console.aws.amazon.com/mediatailor/ "https://console.aws.amazon.com/mediatailor/").
2. In the navigation pane, choose **Channel
   assembly** > **Channels**.
3. Choose the channel that you want to disable the As Run log
   for.
4. In the navigation bar under the channel's name, choose
   **Logging**.
5. Under **Logging** > **Log
   types**, clear **As run** to
   disable the As Run log.

AWS Command Line Interface (AWS CLI)
**To disable the As Run log**

Run the [configure-logs-for-channel](../../../cli/latest/reference/mediatailor/configure-logs-for-channel.md "../../../cli/latest/reference/mediatailor/configure-logs-for-channel.md") command and specify the
appropriate values for the required parameters.

This example is formatted for Linux, macOS, or Unix, and it uses the
backslash (\) line-continuation character to improve readability.

```
$ aws mediatailor configure-logs-for-channel \
--channel-name `MyChannel` \
--log-types
```

This example is formatted for Microsoft Windows, and it uses the caret
(^) line-continuation character to improve readability.

```
C:\> aws mediatailor configure-logs-for-channel ^
--channel-name `MyChannel` ^
--log-types
```

Where:

- `MyChannel` is the name
  of the channel that you own and want to disable the As Run log
  for.

If the command runs successfully, you receive output similar to the
following.

```
{
    "ChannelName": "`MyChannel`",
    "LogTypes": []
}
```
