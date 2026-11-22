

# Using local adb tools with Device Connect

During a remote access session, you can control the device from your own computer with the Android Debug Bridge (adb). Device Connect for AWS Device Farm connects the adb on your computer to the device in the session. Your adb tools, such as Android Studio, shell scripts, and continuous integration (CI) jobs, work with the device. For more information, see [Android Debug Bridge (adb)](https://developer.android.com/tools/adb) and [Android Studio](https://developer.android.com/studio) on the Android Developers website.

With Device Connect, you install apps, run shell commands, copy files, and forward ports, as you do with a device that is connected locally through USB. For example, you can install a new app build with `adb install`. Then you can run the app's Espresso tests with `adb shell am instrument`.

Device Connect works with public devices that run Android 9 or later. For now, Device Connect supports only public devices that use the metered, pay-as-you-go billing method. For more information, see [Supported platforms and features](device-connect-support.md).

Device Connect doesn't support some features of a local adb server. For the list, see [Unsupported features](device-connect-support.md#device-connect-unsupported).

**Topics**
+ [What is Device Connect?](#device-connect-what-is)
+ [Installing Device Connect and attaching a device](device-connect-getting-started.md)
+ [Interacting with devices using adb](device-connect-interaction.md)
+ [Working with the Device Connect bridge](device-connect-status-logs.md)
+ [Supported platforms and features](device-connect-support.md)
+ [Device Connect command reference](device-connect-command-reference.md)
+ [Troubleshooting Device Connect](device-connect-troubleshooting.md)

## What is Device Connect?
<a name="device-connect-what-is"></a>

The adb tool uses a client-server model with three parts:
+ The **adb client** sends your requests. The client is the `adb` command, or a tool such as Android Studio.
+ The **adb server** runs in the background on your computer. Clients connect to it on port 5037. The server keeps track of the devices and sends each request to the correct device.
+ The **adb daemon** (`adbd`) runs on the device. It runs the commands that it gets from the server.

Device Connect takes the place of the adb server on your computer. You run it with the `devicefarm-connect` command. It starts the **bridge**, a process that runs in the background. The bridge listens on `127.0.0.1:5037`, the default address of the adb server. Because of this, adb and tools such as Android Studio can connect to the device through the bridge.

In Device Farm, an adb server runs next to each device. The bridge relays your adb connections to that remote adb server. Your adb must have the same version as the remote adb server, 1.0.41.

When you run an adb command, the following occurs:

1. The adb client connects to the bridge on port 5037.

1. The bridge handles a few requests on your computer, such as `adb devices` and `adb forward`.

1. For other requests, such as `adb shell` or `adb install`, the bridge opens an encrypted WebSocket connection to the device in the session. Each adb connection gets its own WebSocket connection.

1. The adb daemon on the device runs the command. The bridge sends the result back to the adb client.

The bridge also does the following:
+ It keeps running after you close the terminal. It doesn't start when you sign in, and it doesn't restart itself.
+ It uses the AWS credentials of the shell that starts it. With these credentials, it reads the remote access session and gets the session's endpoint.
+ It renews the session's endpoint every few minutes. It replaces its connections before they expire, and adb doesn't notice.
+ It keeps the session active while a device is attached. It holds one idle connection open, so the session doesn't end between your commands.
+ It holds the device of one remote access session at a time. The device appears in `adb devices` with its own serial. To use another device, first detach the attached device.

When you detach a device or stop the bridge, the change happens only on your computer. The remote access session keeps running until you stop it in Device Farm. For more information, see [Step 4: Clean up](device-connect-getting-started.md#device-connect-clean-up).