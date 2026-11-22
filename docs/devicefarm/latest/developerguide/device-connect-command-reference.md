

# Device Connect command reference

Device Connect for AWS Device Farm is a command-line tool named `devicefarm-connect`. On Windows, the installed file is `devicefarm-connect.exe`. This topic describes each command, its options, and its output, with examples.

The `bridge` commands start, stop, and check the bridge. The `device` commands attach, list, and detach devices. The `doctor` command checks your computer, your AWS credentials, and a remote access session. When you run `devicefarm-connect`, `devicefarm-connect bridge`, or `devicefarm-connect device` with no command after it, it prints help and exits with code 0.

The following table lists each command. It also shows which commands start the bridge, and which commands need AWS credentials.


| Command | Purpose | Starts the bridge | Needs AWS credentials | 
| --- | --- | --- | --- | 
| `bridge start` | Starts the bridge with the options that you choose. | Yes. It restarts a running bridge. | No | 
| `bridge stop` | Stops the bridge. | No | No | 
| `bridge status` | Reports whether the bridge is running and whether a device is attached. | No | No | 
| `device add` | Attaches a device. | Yes, with default settings, when none runs | Yes | 
| `device list` | Shows the attached device. | Yes, with default settings, when none runs | No | 
| `device remove` | Detaches a device. | No. It needs a running bridge. | No | 
| `doctor` | Checks this computer, your AWS credentials, and optionally a remote access session. | No | It checks them. | 

For `device add`, the bridge makes the AWS call, not the command. The bridge uses the credentials of the shell that started it. For more information, see [Renew the credentials of the bridge](device-connect-troubleshooting.md#device-connect-troubleshooting-restart-credentials).

The following rules apply to every command:
+ Every command takes the global options, except where noted. For more information, see [Global options](#device-connect-command-global).
+ A command exits with code 0 when it succeeds and with code 1 when it fails. When it fails, it prints the problem to standard error (stderr), often with a cause and a fix. For more information, see [Reading error messages](device-connect-troubleshooting.md#device-connect-error-format).
+ Help, the version, the `bridge status` report, the `device list` views, and the `doctor` report go to standard output (stdout). Every other result line, log line, and error goes to stderr.
+ To read `device list` output in a script, use `--json`.
+ The examples assume that `devicefarm-connect` is on your `PATH`. For more information, see [Step 1: Install Device Connect](device-connect-getting-started.md#device-connect-install). On Windows, run the same commands in PowerShell or `cmd.exe`.

In the examples, replace each session ARN with your session ARN.

**Topics**
+ [Global options](#device-connect-command-global)
+ [`devicefarm-connect bridge start`](#device-connect-command-bridge-start)
+ [`devicefarm-connect bridge stop`](#device-connect-command-bridge-stop)
+ [`devicefarm-connect bridge status`](#device-connect-command-bridge-status)
+ [`devicefarm-connect device add`](#device-connect-command-device-add)
+ [`devicefarm-connect device remove`](#device-connect-command-device-remove)
+ [`devicefarm-connect device list`](#device-connect-command-device-list)
+ [`devicefarm-connect doctor`](#device-connect-command-doctor)

## Global options
<a name="device-connect-command-global"></a>

Every command takes `--debug` and `--help`. Only `devicefarm-connect` itself takes `--version`. The following table describes the global options.


| Option | Description | 
| --- | --- | 
| `--debug` | Prints the log records of the command on stderr, at the debug level. Without this option, a command prints no log records.<br />If the command starts a bridge, the bridge also writes its log at the debug level. For the location of the log, see [Finding the log file](device-connect-status-logs.md#device-connect-log-files). | 
| `-h`, `--help` | Prints help for the command. You can also run `devicefarm-connect help {{command}}`. | 
| `-v`, `--version` | Prints the version of `devicefarm-connect`. Only the bare command takes this option, so `devicefarm-connect bridge --version` fails. | 

The following example prints the version.

```bash
devicefarm-connect --version
```

The following example prints the help. The help lists the commands and the global options.

```bash
devicefarm-connect --help
```

## `devicefarm-connect bridge start`
<a name="device-connect-command-bridge-start"></a>

The `bridge start` command starts the bridge, or restarts it with new options.

The bridge takes the place of the local Android Debug Bridge (adb) server. By default, it listens on the loopback address, `127.0.0.1`, on port 5037, which is the default port of adb. Your adb tools can connect to the device through the bridge. You need `bridge start` only to choose options such as `--port` or `--allow-adb-reverse`. The `device add` and `device list` commands start the bridge with default settings when none runs.

We recommend that you keep the bridge on the loopback address. For more information, see [Infrastructure security for Device Connect](infrastructure-security.md#infrastructure-security-device-connect).

If a local adb server holds the port, `bridge start` stops it first, as `adb kill-server` does. For what this means for your local devices and for Android Studio, see [Local devices disappear, or Android Studio takes port 5037 back](device-connect-troubleshooting.md#device-connect-troubleshooting-adb-server-stopped).

If a bridge already runs, `bridge start` stops it and starts a new one with the options you gave. It prints a line such as the following:

```
* a bridge was running (PID 4242) and was stopped; its attached devices and forward rules were dropped, and its reverse rules no longer reach this machine
```

So, to restart the bridge, you run one `bridge start` command with the options that you want. You don't run `bridge stop` first. To attach the device again, run `device add`.

The command needs no AWS credentials. When `device add` later attaches a device, the bridge uses the credentials of the shell that ran `bridge start`.

The command has the following syntax.

```
devicefarm-connect bridge start
    [--port {{port}}]
    [--log {{path}}]
    [--allow-adb-reverse]
```

The following table describes the options.


| Option | Description | Default | 
| --- | --- | --- | 
| `--port {{port}}` | The local TCP port that the bridge listens on for adb clients. The value is an integer from 1 to 65535. On macOS and Linux, a port lower than 1024 needs administrator rights.<br />If you choose a port other than 5037, add `-P {{port}}` to every adb command. | 5037 | 
| `--log {{path}}` | The path of the log file of the bridge. This option moves only the log file. | `devicefarm-connect.log` in the per-user runtime directory. For the directory on each operating system, see [Finding the log file](device-connect-status-logs.md#device-connect-log-files). | 
| `--allow-adb-reverse` | Lets the device open connections to this computer with `adb reverse`. | Off | 

**Warning**  
The `--allow-adb-reverse` option turns on adb reverse. Each adb reverse rule names a localhost port of your computer. The device can then reach any service on a port that a rule names. Be careful about which services you open to which devices. Some services can give sensitive information to the device. Public devices in Device Farm are shared tenancy devices. Other customers use the same devices before you and after you.

The following example starts the bridge with default settings and no device.

```bash
devicefarm-connect bridge start
```

This will show output such as the following:

```
* bridge not running; starting it now
* bridge started (PID 4242); log file: /run/user/1000/devicefarm-connect/devicefarm-connect.log
devicefarm-connect listening on port 5037 with no device attached; use 'device add' to connect one
```

The following example starts the bridge with `adb reverse` turned on. Then it attaches the device of a remote access session.

```bash
devicefarm-connect bridge start --allow-adb-reverse
devicefarm-connect device add --session-arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}"
```

The last line of the `bridge start` output names the port and says that no device is attached. Lines that start with `*` are progress notes, not errors.

For more information, see [Step 3: Attach the device and run adb](device-connect-getting-started.md#device-connect-attach-device) and [Reaching your computer from the device with `adb reverse`](device-connect-interaction.md#device-connect-reverse).

## `devicefarm-connect bridge stop`
<a name="device-connect-command-bridge-stop"></a>

The `bridge stop` command stops the running bridge.

The bridge detaches the device, closes every adb connection, and removes every forward rule. Reverse rules stop working. If the bridge doesn't stop within 10 seconds, the command forces it to stop and prints `* the bridge (PID 4242) did not stop cleanly and was killed`. If an attach is in progress, the command can wait for it to end.

After the bridge stops, the next adb command starts a local adb server as usual. You can't stop the bridge with `adb kill-server`.

If no bridge runs, the command prints `devicefarm-connect not listening` and exits with code 0. The command needs no AWS credentials.

On Windows, if you started the bridge from an elevated shell, stop the bridge from an elevated shell. For more information, see [Problems on Windows](device-connect-troubleshooting.md#device-connect-troubleshooting-windows).

**Important**  
Device Farm bills the remote access session until you stop it. `device remove` and `bridge stop` don't stop the session. To stop it, see [Step 4: Clean up](device-connect-getting-started.md#device-connect-clean-up).

The command has the following syntax.

```
devicefarm-connect bridge stop
```

This command takes only the global options.

The following example stops the bridge. The command prints `devicefarm-connect stopped`.

```bash
devicefarm-connect bridge stop
```

For more information, see [Detaching the device and stopping the bridge](device-connect-interaction.md#device-connect-stop).

## `devicefarm-connect bridge status`
<a name="device-connect-command-bridge-status"></a>

The `bridge status` command reports whether the bridge is running and whether a device is attached.

The command does not start the bridge and needs no AWS credentials. It exits with code 0 whether or not a bridge runs. The text lines do not print the port or the device name. To see the attached device, use `device list`.

The command has the following syntax.

```
devicefarm-connect bridge status
    [--json]
```

With `--json`, the command prints one JSON object instead of the lines. For the members, see [Checking the bridge](device-connect-status-logs.md#device-connect-bridge-status). The command also takes the global options.

For every line that the command prints, including the note about a device that the bridge detached, see [Checking the bridge](device-connect-status-logs.md#device-connect-bridge-status).

## `devicefarm-connect device add`
<a name="device-connect-command-device-add"></a>

The `device add` command attaches the device of a remote access session to the bridge.

Pass the ARN of a remote access session, not the ARN of a device. The session must be in the US West (Oregon) Region, on an Android 9 or later device, with the status `RUNNING`. For instructions on creating one, see [Step 2: Create a remote access session](device-connect-getting-started.md#device-connect-create-session).

If no bridge runs, `device add` starts one with default settings, as adb starts its own server. Like `bridge start`, it stops a local adb server that holds port 5037. To choose other options, run `bridge start` first.

The bridge looks up the session with the AWS credentials of the shell that started it. If the session is already attached, the command makes no AWS call, prints its line again, and exits with code 0. The bridge holds one device at a time, so the command fails while another session is attached. For more information, see [Switching to another device](device-connect-interaction.md#device-connect-multiple-devices). If an attach fails, the bridge keeps running.

The command has the following syntax.

```
devicefarm-connect device add --session-arn {{session-arn}}
```

The following table describes the option.


| Option | Description | Default | 
| --- | --- | --- | 
| `--session-arn {{session-arn}}` | Required. The ARN of the remote access session whose device you attach. | None | 

The following example attaches a device when no bridge runs. The command starts the bridge first.

```bash
devicefarm-connect device add --session-arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}"
```

This will show output such as the following:

```
* bridge not running; starting it now
* bridge started (PID 4242); log file: /run/user/1000/devicefarm-connect/devicefarm-connect.log
devicefarm-connect listening on port 5037 with connected device: Google Pixel 9 (OS 16)
```

The last line names the port and the device that you attached. It does not print the adb serial of the device. To see the serial, use `device list`.

For more information, see [Step 3: Attach the device and run adb](device-connect-getting-started.md#device-connect-attach-device) and [Switching to another device](device-connect-interaction.md#device-connect-multiple-devices).

## `devicefarm-connect device remove`
<a name="device-connect-command-device-remove"></a>

The `device remove` command detaches the device from the bridge.

The bridge closes the adb connections of the device and removes its forward rules. If `adb reverse` is on, the bridge also asks Device Farm to clear the reverse rules of the session. The bridge keeps running.

You don't need an option. With `--session-arn`, the command detaches the device only if that session is attached. The command needs a running bridge. It needs no AWS credentials.

The command has the following syntax.

```
devicefarm-connect device remove [--session-arn {{session-arn}}]
```

The following table describes the option.


| Option | Description | Default | 
| --- | --- | --- | 
| `--session-arn {{session-arn}}` | The ARN of a remote access session. The command detaches the device only if this session is attached. | None | 

The following example detaches the attached device. The command prints one line that names the device.

```bash
devicefarm-connect device remove
```

If no device is attached, the command fails with the cause `no device is attached`. If the session that you name is not attached, the cause is `the attached device does not match the requested session`. If no bridge runs, the command prints `devicefarm-connect: error: the bridge is not listening`. In each case, the command exits with code 1.

For more information, see [Detaching the device and stopping the bridge](device-connect-interaction.md#device-connect-stop) and [Switching to another device](device-connect-interaction.md#device-connect-multiple-devices).

## `devicefarm-connect device list`
<a name="device-connect-command-device-list"></a>

The `device list` command shows the device that is attached to the bridge.

If no bridge runs, the command starts one with default settings, as adb starts its own server. Like `bridge start`, it stops a local adb server that holds port 5037. The command needs no AWS credentials.

By default, the command prints a table. The `--json` option prints one JSON object instead.

The command has the following syntax.

```
devicefarm-connect device list [--json]
```

The following table describes the option.


| Option | Description | Default | 
| --- | --- | --- | 
| `--json` | Prints one JSON object instead of the table. | Off | 

The following example shows the attached device as a table.

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

For the meaning of each value, the `--json` fields, and the output when no device is attached, see [Listing the attached device](device-connect-status-logs.md#device-connect-device-list).

## `devicefarm-connect doctor`
<a name="device-connect-command-doctor"></a>

The `doctor` command checks this computer, your AWS credentials, and optionally a remote access session, and then prints a report.

Run the command from the shell that will run `bridge start`, because the bridge inherits the environment of that shell. Without `--session-arn`, the doctor checks the session of the device that the running bridge holds. With no running bridge or no device, it checks only this computer and your AWS credentials. When it checks a session, it also checks the connection to the device and the adb versions.

The command reports problems but does not fix them. It starts no bridge, installs no forward or reverse rule, and starts no adb server. If a bridge runs, the command reports it but does not change it. The command has the following small side effects:
+ It creates the working directory of `devicefarm-connect` if it is missing. It also forgets a bridge that no longer runs.
+ When no bridge holds the listen port, it binds the port and frees it again. It also binds and frees one port on 127.0.0.1 to test `adb forward`.
+ It asks the program that holds the listen port whether it is a bridge, and for its adb version.
+ When it checks a session, it makes one `GetRemoteAccessSession` call. It also opens one short connection to the device for each network and dependency check. The session and reconnect checks leave one adb session open on the device side until Device Farm ends it.
+ It runs `adb version` on each adb that it finds on `PATH`, in `ANDROID_HOME` or `ANDROID_SDK_ROOT`, or in the default SDK location of Android Studio.

The command has the following syntax.

```
devicefarm-connect doctor
    [--session-arn {{session-arn}}]
    [--port {{port}}]
    [--verbose]
    [--json]
```

The following table describes the options.


| Option | Description | Default | 
| --- | --- | --- | 
| `--session-arn {{session-arn}}` | The ARN of a remote access session to check. With this option, the command also checks the session, the connection to the device, and the adb versions. | The session of the attached device, when the bridge holds one. Otherwise none. | 
| `--port {{port}}` | The local TCP port to check. Use the same value that you pass to `bridge start --port`. | 5037 | 
| `--verbose` | Prints one line for each check, with the check ID, instead of the table. | Off | 
| `--json` | Prints one JSON object instead of the table, with the same exit code. If you pass both `--json` and `--verbose`, the command prints JSON. | Off | 

The following example checks this computer and a remote access session. Every check passes.

```bash
devicefarm-connect doctor --session-arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}"
```

This will show output such as the following:

```
+---------------+--------+-----------------------------------------------------+
| Category      | Status | Details                                             |
+---------------+--------+-----------------------------------------------------+
| Local machine | PASS   | working directory, bridge, listen port, adb forward |
+---------------+--------+-----------------------------------------------------+
| AWS           | PASS   | AWS credentials, remote access session              |
+---------------+--------+-----------------------------------------------------+
| Network       | PASS   | adb session to the device, adb session reconnect,   |
|               |        |   adb reverse                                       |
+---------------+--------+-----------------------------------------------------+
| Dependencies  | PASS   | adb versions                                        |
+---------------+--------+-----------------------------------------------------+
doctor: 4 of 4 categories passed
```

For how to run the doctor and act on its report, see [Run the `doctor` command](device-connect-troubleshooting.md#device-connect-doctor).

### Doctor report formats and exit codes
<a name="device-connect-command-doctor-output"></a>

By default, the doctor prints a table with one row for each category. The status of a row is one of the following:
+ `FAIL`: A check in the category failed.
+ `WARN`: A check works, but with a caveat.
+ `SKIP`: No check in the category ran.
+ `PASS`: Every check in the category passed.

The `Details` column names each check that did not pass, and why. When a row is `WARN` or `FAIL`, a `What to do` list follows the table. Each item gives the fix and the command to run. The last line counts the categories that passed. The table fits the width of the terminal, or the `COLUMNS` value when stdout is not a terminal.

The `--verbose` view prints one line for each check, in the format `[{{STATUS}}] {{id}}: {{summary}}`. A line with a fix ends with `; fix: {{hint}}`. A count line follows the checks.

The `--json` view prints one JSON object on one line, with the same exit code. The object has the following fields:
+ `ok`: `true` when no check is `fail`, the same as exit code 0.
+ `sessionArn`: The session the doctor checked: the `--session-arn` value, the attached session, or an empty string.
+ `checks`: One object for each check, in run order, with `id`, `title`, `category`, `status`, `summary`, `hint`, `needs`, and `elapsedMs`. The `hint` field is absent when a check passes, and when a check fails because it timed out or you pressed Ctrl\+C. The `needs` field is always an array.
+ `summary`: The number of checks for each status: `pass`, `warn`, `fail`, and `skip`.

Any release can add fields. Only a new major version of `devicefarm-connect` renames, removes, or changes the type of a field.

For example, a script can read the `ok` field with jq.

```bash
devicefarm-connect doctor --session-arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}" --json | jq .ok
```

The doctor exits with code 0 unless a check is `FAIL`. A `WARN` or `SKIP` does not change the exit code. The report goes to stdout. When a check fails, the doctor also prints one error line to stderr and exits with code 1.

Each check has its own time limit. A run in which every check times out ends in less than two minutes. To stop a run, press Ctrl\+C. The doctor ends the current check and prints the results of the checks that ran.