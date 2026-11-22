

# Supported platforms and features

Device Connect for AWS Device Farm runs on your computer and connects your local Android Debug Bridge (adb) to Android devices in remote access sessions. The following sections list the operating systems, versions, adb commands, and port forwarding that Device Connect supports.

Most adb commands work as they do with a local device.

**Topics**
+ [Supported operating systems](#device-connect-supported-platforms)
+ [Supported adb and Android versions](#device-connect-supported-versions)
+ [Supported adb commands](#device-connect-supported-commands)
+ [Supported port forwarding](#device-connect-supported-forwarding)
+ [Unsupported features](#device-connect-unsupported)

## Supported operating systems
<a name="device-connect-supported-platforms"></a>

At this time, `devicefarm-connect` runs on the operating systems and architectures in the following table.


| Operating system | Architectures | Notes | 
| --- | --- | --- | 
| macOS | arm64 (Apple silicon), amd64 (Intel) | macOS 13 or later. | 
| Linux | amd64, arm64 | `uname -m` prints `x86_64` for amd64 and `aarch64` for arm64. | 
| Windows | amd64 | Windows 10 build 17063 or later. Windows 10 version 1803 and later, and Windows 11, have such a build. To check your build, run `winver`. | 

`devicefarm-connect` doesn't include adb. You install adb separately. For more information, see [Prerequisites](device-connect-getting-started.md#device-connect-prerequisites).

## Supported adb and Android versions
<a name="device-connect-supported-versions"></a>

The following table lists the adb and device versions that Device Connect supports.


| Component | Supported versions | Notes | 
| --- | --- | --- | 
| adb on your computer | Android Debug Bridge version 1.0.41, from Android SDK Platform-Tools 29.0.0 or later | `adb version` prints the version. | 
| Device | Public devices with Android 9 or later | At this time, Device Connect works only with metered public devices. It doesn't work with private devices or unmetered public slots. It doesn't support iOS devices. | 

Your adb must be version 1.0.41. An adb with another version can't connect through the bridge, so every command fails. In Android Studio, update **Android SDK Platform-Tools** in the SDK Manager. To check every adb on your computer, run `devicefarm-connect doctor` with `--session-arn`. For more information, see [`adb server version doesn't match this client`](device-connect-troubleshooting.md#device-connect-troubleshooting-adb-version).

## Supported adb commands
<a name="device-connect-supported-commands"></a>

Most adb commands work as they do with a local device. For example, `adb shell`, `adb install`, and `adb logcat` work. The bridge handles a few requests on your computer, such as `adb devices` and `adb forward`, and sends every other request to the device. The commands named on this page are examples, not a complete list.

Android Studio works with the attached device, except for device mirroring. For more information, see [Using Android Studio](device-connect-interaction.md#device-connect-android-studio).

Two adb clients can use one bridge at the same time. They share the connection limit of the bridge. Several computers can also attach the same session, but only one of them at a time can use `adb reverse`. For the limits, see [Device Connect limits](limits.md#device-connect-limits).

### Refused commands
<a name="device-connect-supported-commands-refused"></a>

The following `adb reverse` commands fail with the message shown:
+ `adb reverse tcp:0 {{local}}`: `reverse tcp:0 is not supported on AWS Device Farm`.
+ `adb reverse` to a device port from 5555 to 5585: `reverse to a device port in 5555 to 5585 is not permitted on AWS Device Farm`.
+ `adb reverse` to the adb port of the bridge: `cannot reverse to tcp:{{port}}: the bridge listens on that port`.
+ `adb reverse` with an end that is not `tcp:{{port}}`, such as `adb reverse localabstract:{{name}} tcp:{{port}}`: `unsupported socket specification: {{spec}}; adb reverse accepts only tcp:<port> on AWS Device Farm`.

Device Farm also blocks commands that can disrupt the device, such as `adb reboot`.

## Supported port forwarding
<a name="device-connect-supported-forwarding"></a>

The following table lists what `adb forward` and `adb reverse` support.


| Property | `adb forward` | `adb reverse` | 
| --- | --- | --- | 
| On by default | Yes | No | 
| End on your computer | `tcp:{{port}}` | `tcp:{{port}}` | 
| End on the device | `tcp:{{port}}` | `tcp:{{port}}` | 
| Address on your computer | Listens on `127.0.0.1` only | Connects to `127.0.0.1` | 

With `tcp:0` as the end on your computer, `adb forward` picks a free port and prints it.

To turn on `adb reverse`, start the bridge with `--allow-adb-reverse`.

**Important**  
`--allow-adb-reverse` lets the device open connections to this machine, so use it only with a device you trust; a public device can run software you do not control.

For the limits on rules, connections, and device ports, see [Device Connect limits](limits.md#device-connect-limits). For instructions, see [Forwarding ports](device-connect-interaction.md#device-connect-port-forwarding) and [Reaching your computer from the device with `adb reverse`](device-connect-interaction.md#device-connect-reverse).

## Unsupported features
<a name="device-connect-unsupported"></a>

Device Connect doesn't support the following. For adb commands that fail, see [Refused commands](#device-connect-supported-commands-refused). For the limits, see [Device Connect limits](limits.md#device-connect-limits).

More than one attached device  
The bridge holds the device of one remote access session at a time. adb can't list or use two Device Farm devices together. To use another device, detach the attached device first. For instructions, see [Switching to another device](device-connect-interaction.md#device-connect-multiple-devices).

Local devices and Device Farm devices on one adb server  
The bridge takes the place of the local adb server. It shows only the attached Device Farm device, not your local devices. A tool that uses one adb server, such as Android Studio, can't use both kinds of device together.  
To keep your local devices, run the bridge on another port. The bridge then leaves port 5037 to your local adb server, and Android Studio uses your local devices only. For instructions, see [Using a different port](device-connect-interaction.md#device-connect-custom-port).

Rules to a socket on the device, and device mirroring in Android Studio  
At this time, an `adb forward` or `adb reverse` rule must use `tcp:{{port}}` on both ends. A tool that needs a rule to a socket on the device, such as a `localabstract:` socket, doesn't work. For example, device mirroring in Android Studio and Chrome DevTools for Chrome on the device don't work. For another way to view the screen, see [Viewing the device screen while you use Android Studio](device-connect-interaction.md#device-connect-android-studio-screen).