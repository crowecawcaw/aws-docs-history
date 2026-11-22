

# Interacting with devices using adb

With Device Connect for AWS Device Farm, you use the Android Debug Bridge (adb) with an attached device as you use a local device. During the remote access session, you can run as many adb commands as you want, from any adb client on your computer. For example, you can install your app from Android Studio, then run a shell script that copies test files to the device. A session can last up to 150 minutes. For more information, see [Service limits](limits.md#service-limits).

While a device is attached, the bridge keeps the session active between commands. The session can still end if your computer loses its network connection for about 5 minutes, or sleeps for a long time.

Before you start, attach a device. For instructions, see [Step 3: Attach the device and run adb](device-connect-getting-started.md#device-connect-attach-device). In the examples, replace each session ARN with your session ARN.

**Topics**
+ [Running adb commands](#device-connect-adb-commands)
+ [Using Android Studio](#device-connect-android-studio)
+ [Forwarding ports](#device-connect-port-forwarding)
+ [Reaching your computer from the device with `adb reverse`](#device-connect-reverse)
+ [Switching to another device](#device-connect-multiple-devices)
+ [Using a different port](#device-connect-custom-port)
+ [Detaching the device and stopping the bridge](#device-connect-stop)

## Running adb commands
<a name="device-connect-adb-commands"></a>

You run adb as usual, with no extra options. The bridge handles a few requests on your computer, such as `adb devices` and `adb version`. It sends the other requests, such as `adb shell`, `adb install`, `adb push`, and `adb pull`, to the device.

**Note**  
On some devices, the first adb command after you attach the device can take several seconds while the device warms up.

To run one shell command, pass it to `adb shell`. For example, the following command prints the Android version of the device:

```bash
adb shell getprop ro.build.version.release
```

To open an interactive shell, run `adb shell` with no command.

To install an app, run `adb install` with the path to the APK file. adb prints `Success` when the install is complete. To remove the app, run `adb uninstall` with its package name.

```bash
adb install -r {{app-debug.apk}}
adb uninstall {{com.example.myapp}}
```

To copy files, use `adb push` and `adb pull`. For example, the following commands copy a file to the device, copy it back, and then delete it from the device:

```bash
adb push {{notes.txt}} /data/local/tmp/{{notes.txt}}
adb pull /data/local/tmp/{{notes.txt}} {{received.txt}}
adb shell rm /data/local/tmp/{{notes.txt}}
```

To read the device log, run `adb logcat`. To stop the log stream, press Ctrl\+C.

```bash
adb logcat
```

Because the bridge holds one device, adb commands need no device option. You can also use the device options of a local adb server:
+ `-s {{serial}}` chooses the device with that serial.
+ The `ANDROID_SERIAL` environment variable works the same as `-s`, for example `ANDROID_SERIAL=R3CN30ABCDE adb shell getprop ro.build.version.release`. In PowerShell, run `$env:ANDROID_SERIAL = 'R3CN30ABCDE'` before the adb command. The value stays set in that window until you run `Remove-Item Env:ANDROID_SERIAL`. If the variable holds another serial, adb prints `device '{{serial}}' not found`. Unset the variable when you don't need it.
+ `-t {{id}}` chooses the device with that `transport_id` in `adb devices -l`.

Each open shell, log stream, and forwarded connection counts toward the limit of 24 open adb connections for the device. For more information, see [Device Connect limits](limits.md#device-connect-limits).

Device Farm refuses some adb commands, such as `adb root`, `adb remount`, and `adb tcpip`. adb then prints the reason and exits with a nonzero code. A refusal ends only that command, and the device stays attached. For more information, see [Supported adb commands](device-connect-support.md#device-connect-supported-commands).

## Using Android Studio
<a name="device-connect-android-studio"></a>

Android Studio uses the adb server on port 5037. The bridge listens on the same port, so Android Studio can connect to the attached device through the bridge.

**Important**  
The adb that Android Studio uses must be version 1.0.41. An adb with another version can't connect through the bridge, so every command fails.

To update that adb, update **Android SDK Platform-Tools** in the SDK Manager of Android Studio. To check the version of the adb on your `PATH` and of the adb that Android Studio uses, run `devicefarm-connect doctor` with `--session-arn`. For more information, see [Run the `doctor` command](device-connect-troubleshooting.md#device-connect-doctor).

**To use Android Studio with an attached device**

1. Quit Android Studio.

1. Start the bridge. If the adb server that Android Studio started still holds port 5037, the bridge stops that server first.

   ```bash
   devicefarm-connect bridge start
   ```

1. Attach the device.

   ```bash
   devicefarm-connect device add --session-arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}"
   ```

1. Open Android Studio. Android Studio uses the bridge as its adb server on port 5037.

If Android Studio takes port 5037 back, quit Android Studio. Then run `devicefarm-connect bridge start` again, and open Android Studio. For more information, see [Local devices disappear, or Android Studio takes port 5037 back](device-connect-troubleshooting.md#device-connect-troubleshooting-adb-server-stopped).

### Viewing the device screen while you use Android Studio
<a name="device-connect-android-studio-screen"></a>

Device mirroring in Android Studio doesn't work with Device Connect. The **Running Devices** window can't show the screen of the attached device.

We recommend that you use the pop-out window of the remote access session instead. It shows the device screen and the menu of actions in a separate browser window.

**To pop out the device screen**

1. Open the remote access session in the Device Farm console.

1. In the menu on the left-hand side of the device, choose **Pop out**.

1. Place the pop-out window next to Android Studio. In some browsers, such as Google Chrome and Microsoft Edge, the window stays on top of other windows.

1. To move the device screen back, choose **Return to page**, or close the pop-out window.

Keep the session page open. If you close it, the pop-out window closes. Some actions work only on the session page. For the details, see [Popping out the device screen](how-to-use-session.md#how-to-use-session-pop-out).

## Forwarding ports
<a name="device-connect-port-forwarding"></a>

With `adb forward`, a program on your computer can reach a port on the device. For example, a test that runs on your computer can call a server that your app runs on the device.

A forward rule connects a `tcp:{{port}}` on your computer to a `tcp:{{port}}` on the device. At this time, both ends must be TCP ports. For more information, see [Supported port forwarding](device-connect-support.md#device-connect-supported-forwarding).

**To forward a local port to the device**

1. Add the rule. The following command forwards local port 18080 to port 18082 on the device.

   ```bash
   adb forward tcp:{{18080}} tcp:{{18082}}
   ```

1. List the rules. adb shows the rule with the serial of the device.

   ```bash
   adb forward --list
   ```

1. Connect your program to `127.0.0.1:18080`. For example, run `curl 127.0.0.1:18080`. The bridge carries the connection to port 18082 on the device.

1. When you finish, remove the rule.

   ```bash
   adb forward --remove tcp:{{18080}}
   ```

`adb forward --remove-all` removes every rule.

Forward rules end when you detach the device or stop the bridge. For more information, see [Detaching the device and stopping the bridge](#device-connect-stop).

## Reaching your computer from the device with `adb reverse`
<a name="device-connect-reverse"></a>

With `adb reverse`, the device can open connections to a port on your computer. For example, an app on the device can call a development server that runs on your computer. adb reverse is off by default. To turn it on, start the bridge with `--allow-adb-reverse`.

**Important**  
`--allow-adb-reverse` lets the device open connections to this machine, so use it only with a device you trust; a public device can run software you do not control.

When adb reverse is off, adb prints an error that starts with `adb reverse is off for this bridge`. `bridge start` restarts a running bridge with the options you give. The restart detaches the device and removes every forward rule.

**To turn on `adb reverse` and add a rule**

1. Start the bridge with adb reverse on.

   ```bash
   devicefarm-connect bridge start --allow-adb-reverse
   ```

1. Attach the device.

   ```bash
   devicefarm-connect device add --session-arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}"
   ```

1. If you use forward rules, add them again.

1. Add a reverse rule. The following command lets the device reach port 18083 on your computer through port 18082 on the device.

   ```bash
   adb reverse tcp:{{18082}} tcp:{{18083}}
   ```

1. List the reverse rules of the device. adb lists the rule that you added.

   ```bash
   adb reverse --list
   ```

**Note**  
When you add a reverse rule, use `tcp:` on both ends, and keep the device port outside 5555 to 5585. Device Farm refuses a reverse rule to a socket on the device, such as a `localabstract:` socket. For more information, see [Refused commands](device-connect-support.md#device-connect-supported-commands-refused).

After you attach a device with adb reverse on, the first reverse command can wait a few seconds.

Add your reverse rules again each time you attach the device.

When you no longer need adb reverse, run `devicefarm-connect bridge start` without `--allow-adb-reverse`. The restart turns it off.

## Switching to another device
<a name="device-connect-multiple-devices"></a>

The bridge holds the device of one remote access session at a time. To use another device, detach the attached device. Then attach the new device.

**To switch to another device**

1. Create a remote access session for the other device. For instructions, see [Step 2: Create a remote access session](device-connect-getting-started.md#device-connect-create-session).

1. Detach the attached device.

   ```bash
   devicefarm-connect device remove
   ```

1. Attach the device of the other session.

   ```bash
   devicefarm-connect device add --session-arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/d4e5f6a7-8901-23de-f012-EXAMPLE44444/00000}}"
   ```

1. If you no longer need the first session, stop it with its own ARN. Device Farm bills a session until you stop it. This command doesn't change the attached device.

   ```bash
   aws devicefarm stop-remote-access-session --arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}" --region us-west-2
   ```

If a device is attached and you run `device add` with another session, the command fails and prints the following:

```
devicefarm-connect: error: could not attach the device
  cause: a different device is already attached (Google Pixel 9 (OS 16))
  fix:   Remove that device with 'devicefarm-connect device remove', then run 'devicefarm-connect device add --session-arn {{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/d4e5f6a7-8901-23de-f012-EXAMPLE44444/00000}}' again.
```

## Using a different port
<a name="device-connect-custom-port"></a>

By default, the bridge listens on port 5037, the default port of adb. Use a different port when another program must keep port 5037. For example, you can keep the local adb server on port 5037 for your USB devices.

**To use a different port**

1. Start the bridge on the new port. This restarts any running bridge and detaches its device.

   ```bash
   devicefarm-connect bridge start --port {{5038}}
   ```

1. Attach the device.

   ```bash
   devicefarm-connect device add --session-arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}"
   ```

1. Run adb with `-P` and the same port.

   ```bash
   adb -P {{5038}} devices
   ```

   adb lists the attached device.

Pass `-P` with the port on every adb command. To check the port, run `devicefarm-connect doctor --port 5038`.

## Detaching the device and stopping the bridge
<a name="device-connect-stop"></a>

When you finish, detach the device with `devicefarm-connect device remove`, and stop the bridge with `devicefarm-connect bridge stop`. For the steps, including how to stop the session, see [Step 4: Clean up](device-connect-getting-started.md#device-connect-clean-up).

**Important**  
Device Farm bills the remote access session until you stop it. `device remove` and `bridge stop` don't stop the session.

The following list shows what each command removes:
+ `devicefarm-connect device remove` closes the forward rules and open adb connections of the device. With adb reverse on, it also removes the reverse rules. The bridge keeps listening.
+ `devicefarm-connect bridge stop` detaches the device, and closes every connection and forward rule. Reverse rules stop working.