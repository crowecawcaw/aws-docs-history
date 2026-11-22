

# Working with the Device Connect bridge

Device Connect for AWS Device Farm can tell you whether its bridge runs, which device is attached, and why a device detached. You can also read the log file of the bridge. For example, the Android Debug Bridge (adb) might no longer find your device. Run `devicefarm-connect bridge status` to see whether the bridge detached it, and why.

To check your computer, your credentials, and a session before you start, use the doctor command. For more information, see [Run the `doctor` command](device-connect-troubleshooting.md#device-connect-doctor).

After the session ends, Device Farm keeps the device log (logcat) and a log of the adb commands that you ran through Device Connect in the session results. For more information, see [Downloading session video or logs](how-to-access-session-results.md#how-to-access-session-files).

**Topics**
+ [Checking the bridge](#device-connect-bridge-status)
+ [Listing the attached device](#device-connect-device-list)
+ [Finding the log file](#device-connect-log-files)

## Checking the bridge
<a name="device-connect-bridge-status"></a>

To see whether the bridge runs and whether a device is attached, run `devicefarm-connect bridge status`. This command does not start the bridge and needs no AWS credentials. It exits with code 0 whether or not the bridge runs.

```bash
devicefarm-connect bridge status
```

The following table shows the output for each state of the bridge.


| Bridge state | Output | 
| --- | --- | 
| Not running | `devicefarm-connect bridge is not running` | 
| Running with no device | `devicefarm-connect bridge is running (PID 4242), no device attached` | 
| Running with one device | `devicefarm-connect bridge is running (PID 4242), 1 device attached; run 'device list' for details` | 
| Running with no device, after the bridge detached one | `devicefarm-connect bridge is running (PID 4242), no device attached; the last device detached 42 seconds ago: {{reason}}` | 

When the bridge detaches the device on its own, `devicefarm-connect bridge status` adds a note with the reason, as in the last row of the table. The note works as follows:
+ It shows only the newest detach that the bridge made on its own. For example, the session ended, or the bridge could not look up the session.
+ A `devicefarm-connect device remove` adds no note.
+ The note clears when you attach a device.

The reason tells you what to do next. For example, after the session ended, the reason reads `remote access session {{arn}} has ended (COMPLETED); start a new remote access session, then run 'devicefarm-connect device add --session-arn <new ARN>'`. For more information, see [A device detached, or adb lists no device](device-connect-troubleshooting.md#device-connect-troubleshooting-device-detached).

`devicefarm-connect bridge status` does not print the port or the device name. To see the device, see [Listing the attached device](#device-connect-device-list).

**Note**  
`devicefarm-connect bridge status` prints to standard output (stdout). For scripts, use `--json`. It prints one JSON object with the same information as the text lines: whether the bridge runs, its process ID and port, whether adb reverse is on, the attached device with the fields of `device list --json`, and the last detach that the bridge made on its own, with its reason and time. The object always says whether the bridge runs and lists the attached devices. The other members are present only when they apply.

## Listing the attached device
<a name="device-connect-device-list"></a>

To see the attached device, run `devicefarm-connect device list`. If the bridge does not run, this command starts it with default settings.

```bash
devicefarm-connect device list
```

This will show output such as the following:

```
+----------------+-------------+----------------+------------------------------+
| Device         | Serial      | Attached       | Session                      |
+----------------+-------------+----------------+------------------------------+
| Google Pixel 9 | R3CN30ABCDE | 12 minutes ago | started 25 minutes ago       |
|   (OS 16)      |             |                | expires in 2 hours 5 minutes |
+----------------+-------------+----------------+------------------------------+
```

The table has one row for the attached device, with the following columns:
+ `Device`: the device label, in the form `{{device name}} (OS {{version}})`.
+ `Serial`: the serial that adb shows.
+ `Attached`: how long ago you attached the device.
+ `Session`: when the remote access session started, and when it expires. After the expiry, the column reads `expired`.

To see the Amazon Resource Name (ARN) of the session, use `--json`. This option prints one JSON object on one line. The following example shows the object with line breaks added.

```bash
devicefarm-connect device list --json
```

This will show output such as the following:

```json
{
  "devices": [
    {
      "sessionArn": "arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000",
      "label": "Google Pixel 9 (OS 16)",
      "serial": "R3CN30ABCDE",
      "attachedAt": "2026-11-09T17:48:00Z",
      "sessionStartedAt": "2026-11-09T17:35:00Z",
      "sessionExpiresAt": "2026-11-09T20:05:00Z"
    }
  ]
}
```

The following table describes the fields of the JSON object.


| Field | Description | 
| --- | --- | 
| `devices` | One object for the attached device, with the fields `sessionArn` through `sessionExpiresAt` that follow. The array is empty when no device is attached. | 
| `sessionArn` | The ARN of the remote access session. | 
| `label` | The device label. | 
| `serial` | The serial that the device reports. | 
| `attachedAt` | The time that you attached the device. | 
| `sessionStartedAt` | The time that the session started. Device Connect computes it from `sessionExpiresAt` and the maximum session duration. | 
| `sessionExpiresAt` | The time that the session expires. | 
| `lastDetach` | A top-level field beside `devices`, not part of a device object. The newest detach that the bridge made on its own, with its `reason` and the time `at`. This field is absent when there is no such detach. | 

Times use the RFC 3339 format. A time that Device Connect cannot get is absent. To pass the serial to `adb -s` from a script, use `serial`.

The table and `--json` print to standard output (stdout). For scripts, we recommend `--json`.

When no device is attached, the command prints `no device attached; use 'device add' to connect one` to stderr instead of the table. If the bridge detached a device on its own, the note from `devicefarm-connect bridge status` follows. The `--json` view prints `{"devices":[]}`, with a `lastDetach` object when there is a note.

## Finding the log file
<a name="device-connect-log-files"></a>

The bridge writes a log file, `devicefarm-connect.log`, in its working directory for your user. The bridge only adds to the log. It never rotates or shortens the file. To see the working directory on your computer, run `devicefarm-connect doctor --verbose`. The first line names the directory, for example:

```
[PASS] local.runtime-dir: working directory /run/user/1000/devicefarm-connect is writable
```

The default location depends on your operating system.

------
#### [ macOS ]

The default log file is `$TMPDIR/devicefarm-connect-{{uid}}/devicefarm-connect.log`, where {{uid}} is your user ID.

To show the last lines of the log, run the following command:

```bash
tail -n 20 "$TMPDIR/devicefarm-connect-$(id -u)/devicefarm-connect.log"
```

------
#### [ Linux ]

The default log file is `$XDG_RUNTIME_DIR/devicefarm-connect/devicefarm-connect.log`, typically `/run/user/1000/devicefarm-connect/devicefarm-connect.log`. If `XDG_RUNTIME_DIR` is not set, the file is in `devicefarm-connect-{{uid}}` under `$TMPDIR` or `/tmp`, where {{uid}} is your user ID.

To show the last lines of the log, run the following command:

```bash
tail -n 20 "$XDG_RUNTIME_DIR/devicefarm-connect/devicefarm-connect.log"
```

------
#### [ Windows ]

The default log file is `%LocalAppData%\devicefarm-connect\devicefarm-connect.log`.

To show the last lines of the log, run the following command in PowerShell:

```powershell
Get-Content "$env:LocalAppData\devicefarm-connect\devicefarm-connect.log" -Tail 20
```

------

To write the log to another file, start the bridge with `--log`. This option moves only the log file. Only `devicefarm-connect bridge start` takes it. A bridge that `device add` or `device list` starts uses the default file.

```bash
devicefarm-connect bridge start --log {{/path/to/devicefarm-connect.log}}
```

To log more detail, start the bridge with `--debug`. If a bridge already runs, `bridge start` restarts it and detaches its device. On every command, `--debug` also prints the log records of that command on stderr.

```bash
devicefarm-connect bridge start --debug
```

The following table shows log messages that help you find a problem.


| Message | Meaning | 
| --- | --- | 
| `device attached` | You attached a device. | 
| `device removed` | You detached a device. | 
| `session refresh failed; detached device` | The bridge could not look up the session, so it detached the device. For example, the session ended, or the credentials expired. | 
| `a refused adb connection found the session gone; detaching` | The session ended, so the bridge detached the device. | 
| `refused a transport select; closing`, or `refused a local adb connection: the request names no attached device` | An adb command named a serial or transport ID that does not match the attached device, or no device is attached. For more information, see [Running adb commands](device-connect-interaction.md#device-connect-adb-commands). | 
| `a reverse connection was refused` | The bridge refused a reverse connection. No reverse rule names the port, or the port is the adb port of the bridge or a forward rule port. | 
| `a reverse connection failed` | The reverse connection did not reach a server on your computer. Make sure that the server listens on `127.0.0.1`. | 