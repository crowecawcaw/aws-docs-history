# Disconnecting idle clients

You can configure Amazon DCV to disconnect idle clients. More specifically, you can do this for clients that didn't send any keyboard or pointer
input to the Amazon DCV server for a specific period of time. By default, the Amazon DCV server disconnects Amazon DCV clients after being idle for 60 minutes (one
hour).

There are certain actions that will reset the idle disconnect timeout period. If any of the following actions occur, the idle timeout
period will reset to its set time frame:

- Moving the mouse
- Pressing the mouse buttons or moving the mouse wheel
- Pressing any key on the keyboard
- Touching the touchscreen (if enabled)
- Using the stylus (if enabled)
- Using the gamepad (if enabled)
- Streaming with the webcam (if enabled)
- Any file storage operation such as uploading files, creating directories, downloading files, or listing items

###### Note

Connecting and using any audio devices does not reset the idle timeout period.

You can also configure the Amazon DCV server to send a notification to idle clients. The notification is to inform them that their session is about to
disconnect. Timeout notifications are supported only with Amazon DCV servers and clients version 2017.4 and later.

You can use the following procedures to specify a custom idle timeout period.

Windows Amazon DCV server
To change the Amazon DCV server's idle timeout period, you must configure the `idle-timeout` parameter using the Windows Registry
Editor.

###### To change the idle timeout period on Windows

1. Open the Windows Registry Editor.
2. Navigate to the **HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\connectivity\*\* key and select the
   **idle-timeout\*\* parameter.

If the parameter can't be found, use the following steps to create it:

    1. In the navigation pane, open the context (right-click) menu for the **connectivity** key. Then, choose
     **New**, **DWORD (32-bit) value**.
    2. For **Name**, enter `idle-timeout` and press **Enter**.

3. Open the **idle-timeout** parameter. For **Value data**, enter a value for the idle timeout period (in
   minutes, decimal). To avoid disconnecting idle clients, enter `0`.
4. Choose **OK** and close the Windows Registry Editor.

###### (Optional) To configure the Amazon DCV server to send timeout notifications to idle clients

1. Navigate to the **HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\connectivity\*\* key and select the
   **idle-timeout-warning\*\* parameter.

If the parameter can't be found, use the following steps to create it:

    1. In the navigation pane, open the context (right-click) menu for the **connectivity** key. Then, choose
     **New**, **DWORD (32-bit) value**.
    2. For **Name**, enter `idle-timeout-warning` and press **Enter**.

2. Open the **idle-timeout-warning** parameter. For **Value data**, enter the number of seconds (decimal) in
   advance of the disconnection that the associated warning notification is sent. For example, if you want the notification to be sent two minutes
   before the idle timeout is reached, enter `120`.
3. Choose **OK** and close the Windows Registry Editor.

Linux Amazon DCV server
To change the Amazon DCV server's idle timeout period, you must configure the `idle-timeout` parameter in the `dcv.conf`
file.

###### To change the idle timeout period on Linux

1. Open `/etc/dcv/dcv.conf` with your preferred text editor.
2. Locate the `idle-timeout` parameter in the `[connectivity]` section. Then, replace the existing timeout period with
   the new timeout period (in minutes, decimal).

If there's no `idle-timeout` parameter in the `[connectivity]` section, add it manually using the following
format:

```
[connectivity]
  idle-timeout=`timeout_in_minutes`
```

To avoid disconnecting idle clients, enter `0`. 3. Save and close the file.

###### (Optional) To configure the Amazon DCV server to send timeout notifications to idle clients

1. Open `/etc/dcv/dcv.conf` with your preferred text editor.
2. Add the `idle-timeout-warning` parameter to the `[connectivity]` section and specify the number of seconds (decimal)
   in advance of the disconnection that the associated warning notification is sent.

```
idle-timeout-warning=`seconds_before_idle_timeout`
```

For example, if you want the notification to be sent two minutes before the idle timeout is reached, specify `120`. 3. Save and close the file.

macOS Amazon DCV server
To change the Amazon DCV server's idle timeout period, you must configure the `idle-timeout` parameter in the `dcv.conf`
file.

###### To change the idle timeout period on macOS

1. Open `/etc/dcv/dcv.conf` with your preferred text editor.
2. Locate the `idle-timeout` parameter in the `[connectivity]` section. Then, replace the existing timeout period with
   the new timeout period (in minutes, decimal).

If there's no `idle-timeout` parameter in the `[connectivity]` section, add it manually using the following
format:

```
[connectivity]
  idle-timeout=`timeout_in_minutes`
```

To avoid disconnecting idle clients, enter `0`. 3. Save and close the file.

###### (Optional) To configure the Amazon DCV server to send timeout notifications to idle clients

1. Open `/etc/dcv/dcv.conf` with your preferred text editor.
2. Add the `idle-timeout-warning` parameter to the `[connectivity]` section and specify the number of seconds (decimal)
   in advance of the disconnection that the associated warning notification is sent.

```
idle-timeout-warning=`seconds_before_idle_timeout`
```

For example, if you want the notification to be sent two minutes before the idle timeout is reached, specify `120`. 3. Save and close the file.
