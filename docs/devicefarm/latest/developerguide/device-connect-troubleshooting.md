

# Troubleshooting Device Connect

To find and fix most problems with Device Connect for AWS Device Farm, run the `devicefarm-connect doctor` command first. If the doctor finds no problem, search this page for the message that you see. In the examples, replace each session ARN with your session ARN.

**Topics**
+ [Run the `doctor` command](#device-connect-doctor)
+ [Reading error messages](#device-connect-error-format)
+ [Problems when the bridge starts](#device-connect-troubleshooting-start)
+ [Credential and attach problems](#device-connect-troubleshooting-attach)
+ [Problems with adb commands](#device-connect-troubleshooting-adb)
+ [Problems with `adb forward` and `adb reverse`](#device-connect-troubleshooting-forwarding)
+ [Problems on Windows](#device-connect-troubleshooting-windows)
+ [Network problems](#device-connect-troubleshooting-network)

## Run the `doctor` command
<a name="device-connect-doctor"></a>

The `devicefarm-connect doctor` command checks your computer, your AWS credentials, and your remote access session. It reports one row for each category. It doesn't start a bridge or change a running one. For each problem that it finds, it gives you the command to run.

**To run the `doctor` command**

1. Open the shell that you use to run `devicefarm-connect bridge start`. The bridge uses the AWS credentials and environment of that shell.

1. Run the doctor with the Amazon Resource Name (ARN) of your remote access session:

   ```bash
   devicefarm-connect doctor --session-arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}"
   ```

1. If a row is `WARN` or `FAIL`, run the command that each item in the `What to do` list gives.

1. Run the doctor again until no row is `FAIL`.

For example, the following command runs the doctor while a local Android Debug Bridge (adb) server holds port 5037.

```bash
devicefarm-connect doctor
```

This will show output such as the following:

```
+---------------+--------+-----------------------------------------------------+
| Category      | Status | Details                                             |
+---------------+--------+-----------------------------------------------------+
| Local machine | WARN   | listen port: an adb server (version 41) is          |
|               |        |   listening on 127.0.0.1:5037                       |
|               |        | also passed: working directory, bridge, adb forward |
+---------------+--------+-----------------------------------------------------+
| AWS           | PASS   | AWS credentials                                     |
|               |        | remote access session not checked: pass             |
|               |        |   --session-arn to check the session, the device    |
|               |        |   connection, and adb versions                      |
+---------------+--------+-----------------------------------------------------+
| Network       | SKIP   | not checked: needs remote access session            |
+---------------+--------+-----------------------------------------------------+
| Dependencies  | SKIP   | not checked: needs remote access session            |
+---------------+--------+-----------------------------------------------------+

What to do
1. Local machine, listen port: an adb server is listening on 127.0.0.1:5037, so
   the bridge cannot bind it until that server stops. Run
   'devicefarm-connect bridge start --port 5037': it stops that server first
   (via 'adb kill-server'). If a program that restarts adb automatically, such
   as Android Studio, takes the port back, quit that program, run
   'devicefarm-connect bridge start --port 5037' again, then open it: it then
   uses the bridge as its adb server on port 5037.
doctor: 1 of 4 categories passed, 1 warning, 2 not checked
```

A running bridge with adb reverse turned off makes the `Local machine` row `WARN`. You can ignore this warning if you don't use `adb reverse`. The doctor's bridge check also gives `WARN` and the reason when the bridge detached a device itself, or when the `--session-arn` session is not attached.

If you started the bridge on a port other than 5037, add the same `--port` option to the doctor, for example `--port 5038`.

For the list of checks, the output formats, and the exit codes, see [`devicefarm-connect doctor`](device-connect-command-reference.md#device-connect-command-doctor).

## Reading error messages
<a name="device-connect-error-format"></a>

When a `devicefarm-connect` command fails, it prints an error to stderr and exits with code 1. The error has the following shape:

```
devicefarm-connect: error: {{problem}}
  cause: {{cause}}
  fix:   {{fix}}
```

The `error:` line says what failed. Each `cause:` line says why, and each `fix:` line says what to do. An error can have several cause and fix lines. Some errors have only the error line.

For example, a mistake on the command line ends with a fix line that points to the help.

```bash
devicefarm-connect bridge bogus
```

This will show output such as the following:

```
devicefarm-connect: error: unknown command "bogus" for "devicefarm-connect bridge"
  fix:   run 'devicefarm-connect bridge --help' for usage
```

Lines that start with `*` are progress notes, not errors. Lines with `time=` and `level=` appear only with `--debug`. Messages that start with `error:` or `adb:` come from adb. For more detail, read the log file of the bridge. For its location, see [Finding the log file](device-connect-status-logs.md#device-connect-log-files).

## Problems when the bridge starts
<a name="device-connect-troubleshooting-start"></a>

The bridge starts when you run `devicefarm-connect bridge start`. It also starts when `devicefarm-connect device add` or `devicefarm-connect device list` finds no running bridge. The following table lists messages that you can see at that time. The sections after the table cover the local adb server and the port.


| Message or symptom | Cause | What to do | 
| --- | --- | --- | 
| The shell can't find `devicefarm-connect`. | The install folder is not on your `PATH`. | Add the install folder to your `PATH`, then open a new terminal. The install script uses `~/.local/bin` on macOS and Linux, and `%USERPROFILE%\.local\bin` on Windows. For more information, see [Step 1: Install Device Connect](device-connect-getting-started.md#device-connect-install). | 
| `the bridge exited while starting` | The bridge failed while it started. For example, a malformed AWS config profile or `AWS_` environment variable gives `cannot load the AWS configuration`. The doctor reports this problem in its `AWS` row. | Fix what the message names. Then run `devicefarm-connect bridge start`. The message also names the log file. | 
| `the bridge did not report ready within 5s and logged no error, so it was stopped` | The bridge didn't finish starting. | Read the log file that the message names. Then run `devicefarm-connect bridge start`. | 
| `another program held 127.0.0.1:5037 while the bridge started and has released it` | Another program held the port for a short time while the bridge started. | Run `devicefarm-connect bridge start` again. | 
| `unknown flag: --port` | The `--port`, `--log`, and `--allow-adb-reverse` options belong to `bridge start`. The doctor also takes `--port`. | Run `devicefarm-connect bridge start` with the option. The restart detaches the device, so attach it and add your rules again. | 
| `unknown flag: --session-arn` from `bridge start` | `bridge start` takes no session. `--session-arn` belongs to `device add`, `device remove`, and the doctor. | Run `devicefarm-connect bridge start` with the bridge options that you want. Then run `devicefarm-connect device add --session-arn {{arn}}`. | 
| `cannot use the working directory`, with `working directory "{{dir}}" is owned by UID {{n}}, not {{m}}`. The `fix:` line says to run the doctor. | Another user owns the working directory. This happens on macOS and Linux when `XDG_RUNTIME_DIR` is not set, so the directory is in a temporary directory that all users share. | Set `XDG_RUNTIME_DIR` to a private directory with a short path, in every shell that runs `devicefarm-connect`. | 
| `cannot use the working directory`, with `cannot find a location for the working directory: %LocalAppData% is not defined` | On Windows, the working directory is in `%LocalAppData%`. The `LocalAppData` environment variable is not set. | Set `LocalAppData` to a directory with a short path that only your user can write, in every shell that runs `devicefarm-connect`. | 
| `the bridge is not listening` from `device add` or `device list`, while `bridge status` says that the bridge is not running | A registered bridge no longer answers. For example, it hangs. | Run `devicefarm-connect bridge start`. It stops that bridge and starts a new one. Then attach the device again. | 
| The doctor says `the bridge runs another version of devicefarm-connect than this command` | You updated `devicefarm-connect` while the bridge ran. The bridge keeps the earlier version until it restarts, so a command can fail. | Run the commands that the doctor gives: `devicefarm-connect bridge start`, then `devicefarm-connect device add`. Then add your forward and reverse rules again. For more information, see [Update Device Connect](device-connect-getting-started.md#device-connect-update). | 

### Local devices disappear, or Android Studio takes port 5037 back
<a name="device-connect-troubleshooting-adb-server-stopped"></a>

For example, you run the following command while a local adb server holds port 5037.

```bash
devicefarm-connect bridge start
```

This will show output such as the following:

```
* bridge not running; starting it now
* stopped the adb server on 127.0.0.1:5037 (via 'adb kill-server')
* bridge started (PID 4242); log file: /run/user/1000/devicefarm-connect/devicefarm-connect.log
devicefarm-connect listening on port 5037 with no device attached; use 'device add' to connect one
```

This is expected. The bridge takes the place of your local adb server on port 5037, so it stops that server first, as `adb kill-server` does. The local devices that the server served then disappear from adb. Through the bridge, adb shows only Device Farm devices. `device add` and `device list` start the bridge the same way, so they also stop the server.

**To use your local devices again**

1. Stop the bridge:

   ```bash
   devicefarm-connect bridge stop
   ```

1. Run any adb command, such as `adb devices`. adb starts its own server again, and that server serves your local devices.

To keep your local adb server and the bridge at the same time, start the bridge on another port. For more information, see [Using a different port](device-connect-interaction.md#device-connect-custom-port).

A program that restarts adb automatically, such as Android Studio, can keep port 5037 or take it back. Then `devicefarm-connect` prints a message such as the following. A similar message starts with `an adb server took 127.0.0.1:5037 before the bridge could bind it`.

```
devicefarm-connect: error: could not start the bridge
  cause: an adb server on 127.0.0.1:5037 was asked to stop (via 'adb kill-server') and did not (it answered OKAY but port 5037 is still held after 1s; a program that restarts adb automatically, such as Android Studio, can take it back at once). Quit the program that started adb, such as Android Studio, run 'devicefarm-connect bridge start --port 5037', then open that program again: it then uses the bridge as its adb server on port 5037.
```

**To use the bridge with a program that restarts adb**

1. Quit the program, such as Android Studio.

1. Start the bridge:

   ```bash
   devicefarm-connect bridge start
   ```

1. Open the program again. It now uses the bridge as its adb server on port 5037.

For more information about Android Studio, see [Using Android Studio](device-connect-interaction.md#device-connect-android-studio).

### The bridge can't use the port
<a name="device-connect-troubleshooting-port-in-use"></a>

`devicefarm-connect` prints one of the following messages when the bridge can't listen on the port.


| Message | Cause | What to do | 
| --- | --- | --- | 
| `another program is listening on 127.0.0.1:5037, so the bridge cannot bind it` | A program that is not adb holds the port. | Stop that program, then run `devicefarm-connect bridge start`. If the program must keep the port, use another port. | 
| `another devicefarm-connect bridge (PID {{n}}) is listening on 127.0.0.1:5037` | A bridge started from another working directory or by another user holds the port. | Run `devicefarm-connect bridge stop` in the shell that started it, then run `devicefarm-connect bridge start`. Or use another port. | 
| `the bridge cannot bind 127.0.0.1:80: listen tcp 127.0.0.1:80: bind: permission denied` | On macOS and Linux, a port lower than 1024 needs administrator rights. On Windows, the message has a Windows error text instead of `permission denied`, and Hyper-V, WSL, or Docker reserved the port. | Use another port. On Windows, choose a port outside the reserved ranges. | 
| `--port must be from 1 to 65535, got {{n}}` | The `--port` value is not a valid port. | Pass a port from 1 to 65535. | 

On Windows, to list the reserved port ranges, run the following command:

```powershell
netsh int ipv4 show excludedportrange protocol=tcp
```

**To start the bridge on another port**

1. Check the port that you want to use. The `Local machine` row passes when the port is free.

   ```bash
   devicefarm-connect doctor --port 5038
   ```

1. Start the bridge on that port:

   ```bash
   devicefarm-connect bridge start --port 5038
   ```

1. Add `-P` with that port to every adb command, for example:

   ```bash
   adb -P 5038 devices
   ```

For more information, see [Using a different port](device-connect-interaction.md#device-connect-custom-port).

## Credential and attach problems
<a name="device-connect-troubleshooting-attach"></a>

When an attach fails, `devicefarm-connect device add` prints `could not attach the device`. The `cause:` line names what failed, and the `fix:` line names the command to run.

The bridge keeps running. A fix that restarts the bridge names two commands: `devicefarm-connect bridge start`, which stops the running bridge first and starts one that reads the AWS settings of your shell, then `devicefarm-connect device add`, which attaches the device again. The sections after the table cover credentials and the session status.


| Message | Cause | What to do | 
| --- | --- | --- | 
| `invalid session ARN`, for example with `arn: invalid prefix` or `is not a remote access session ARN` | The value is not a remote access session ARN. For example, it is a device ARN or a project ARN. A session ARN contains `:session:`. | Pass the session ARN that `aws devicefarm create-remote-access-session` printed. | 
| `Device Farm remote access is only supported in us-west-2` | The session is in another Region. The `AWS_REGION` variable and the Region in your profile don't change this. | Create the session in the US West (Oregon) Region. Pass `--region us-west-2` to each AWS CLI command. | 
| `this client only supports Android devices`, or `this client only supports Android 9 and above` | The session's device is an iOS device or runs Android 8 or earlier. | Stop the session, because Device Farm bills it until you stop it. Then create a session on a device that runs Android 9 or later. | 
| `GetRemoteAccessSession "{{arn}}": session not found`, or `remote access session "{{arn}}" not found` | The ARN is wrong, or the session belongs to another AWS account. | Check that you copied the whole ARN. In the shell that started the bridge, run `aws sts get-caller-identity` to see the account. If the account is wrong, see [Renew the credentials of the bridge](#device-connect-troubleshooting-restart-credentials). | 
| `GetRemoteAccessSession "{{arn}}":` and then a timeout or throttling error | Device Farm throttled the lookup, or the network was slow. | Wait a moment, then run `devicefarm-connect device add` again. If the error remains, run the doctor command on the `fix:` line. | 
| `the remote adb server lists no device`, or `the remote adb server answered FAIL instead of OKAY` | The remote adb server lists no device, so the bridge can't read the serial of the device. The problem is on the Device Farm side. | Wait a moment, then run `devicefarm-connect device add` again. If the error remains, run the doctor command on the `fix:` line. If the doctor finds no cause, contact AWS Support. | 
| `remote access session "{{arn}}" has ended (status STOPPING)` | The session is ending, for example because nothing was connected to it for a few minutes. | Start a new session and attach it. | 
| `Device Farm at {{host}} rejected the connection request` from `device add`, or `the bridge could not reach the device: Device Farm rejected the connection request` from adb | The session ended, the endpoint URL expired, or the ARN names another account. | Run `devicefarm-connect device add` again. If the error remains, run the doctor command on the `fix:` line. If the doctor finds no cause, contact AWS Support. | 
| `Device Farm refused the connection to the device: {{reason}} (close code 1008)`, where the reason starts with `Device Connect is not supported` | At this time, Device Connect works only with metered public devices. The reason says what the session doesn't meet: `with private devices`, `with this billing method`, or `on this device`. | Stop the session. Create a remote access session on a public device with the `METERED` billing method, then run `devicefarm-connect device add` with the new ARN. If the error remains on such a device, contact AWS Support. For more information, see [Device Connect limits](limits.md#device-connect-limits). | 
| `the connection to Device Farm ended before the device answered`, `the device did not answer within {{time}}`, or `the attach ran out of time before the device answered` | The device didn't answer in time, or the connection dropped while the bridge waited for it. | Run `devicefarm-connect device add` again. If the error remains, run the doctor command on the `fix:` line. If the doctor finds no cause, contact AWS Support. | 
| `* the service names this session {{arn}}` | This is a note, not an error. The ARN you typed carries another account ID. The bridge attached the session under the ARN the service returned. | Use the printed ARN with `devicefarm-connect device remove`. | 
| `a different device is already attached ({{device}})` | The device of another session is attached. The bridge holds one device at a time. | Run `devicefarm-connect device remove`. Then run `devicefarm-connect device add` again. For more information, see [Switching to another device](device-connect-interaction.md#device-connect-multiple-devices). | 

### Renew the credentials of the bridge
<a name="device-connect-troubleshooting-restart-credentials"></a>

The bridge reads AWS credentials from the shell that started it. If you change the credentials or `AWS_PROFILE` in a shell later, the bridge doesn't see the change. The following messages mean that the bridge needs new or fixed credentials.


| Message | Cause | What to fix first | 
| --- | --- | --- | 
| `GetRemoteAccessSession "{{arn}}": access denied` | The credentials don't allow `devicefarm:GetRemoteAccessSession` on the session. The bridge makes this call when it attaches the device, and every few minutes after. | Allow `devicefarm:GetRemoteAccessSession` on the session in your IAM policy. | 
| `request rejected (ExpiredTokenException)`. The code in parentheses can differ. | The credentials are expired or wrong, the request signature is bad, or the clock of your computer is wrong. | Run `aws sts get-caller-identity` with the same profile. Fix the credentials, or set the clock to the correct time. | 
| The doctor says `this shell has no usable AWS credentials`, or a command prints an AWS error such as `failed to refresh cached credentials, no EC2 IMDS role found` | The bridge started from a shell with no credentials. For example, you ran `device add` in a shell where `AWS_PROFILE` was not set. | Set `AWS_PROFILE` to a profile with Device Farm access, or export keys. For more information, see [Authentication and access credentials for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html). | 
| `the AWS credentials the bridge started with have expired` from adb | The credentials of the bridge expired, so it detached the device. | Refresh the credentials. Then, from that shell, restart the bridge with `devicefarm-connect bridge start` and the options that you started it with. Then run `devicefarm-connect device add --session-arn {{arn}}`. | 
| `the bridge can no longer read remote access session` from adb | The credentials of the bridge lost their permission. | Fix the credentials or their permission. Then, from that shell, restart the bridge with `devicefarm-connect bridge start` and run `devicefarm-connect device add --session-arn {{arn}}`. | 

After you fix the credentials, give them to the bridge. If the bridge uses an IAM Identity Center (SSO) profile, you don't need to restart it.

**To renew the credentials of an SSO profile**

1. Refresh the token. The bridge reads the new token.

   ```bash
   aws sso login --profile {{profile-name}}
   ```

1. If the bridge detached a device, attach it again:

   ```bash
   devicefarm-connect device add --session-arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}"
   ```

For other credentials, restart the bridge from a shell with working credentials.

**To restart the bridge with new credentials**

1. Open a shell and fix the credentials. For example, set `AWS_PROFILE` or export new keys. In PowerShell, set a variable in the form `$env:AWS_PROFILE = '{{profile-name}}'`.

1. Run the doctor, and check that the AWS row is not `FAIL`:

   ```bash
   devicefarm-connect doctor --session-arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}"
   ```

1. From the same shell, restart the bridge. `bridge start` stops a running bridge first. If you started the bridge with other options, such as `--port`, add them.

   ```bash
   devicefarm-connect bridge start
   ```

1. Attach the device.

   ```bash
   devicefarm-connect device add --session-arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}"
   ```

1. Add your forward and reverse rules again.

### The session is not RUNNING, or has ended
<a name="device-connect-troubleshooting-not-running"></a>

When you attach the device, the cause line reads like one of the following:

```
remote access session "arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000" is not running yet (status PREPARING)
remote access session "arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000" has ended (status COMPLETED)
```

When the session ends while the device is attached, adb prints a message such as the following. The message can also say `is stopping` or `no longer exists`.

```
error: remote access session arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000 has ended (COMPLETED); start a new remote access session, then run 'devicefarm-connect device add --session-arn <new ARN>'
```

Later adb commands print the same reason, until you attach a device again.

You can attach a session only while its status is `RUNNING`. A session ends when you stop it, when it reaches its maximum length, or when it fails before `RUNNING`. For the session length, see [Service limits](limits.md#service-limits). The bridge then detaches the device and keeps running. Until it detaches the device, `adb devices` can still list it.

The following table shows what to do for each session status.


| Status | Meaning | What to do | 
| --- | --- | --- | 
| `PENDING`, `PROCESSING`, `SCHEDULING`, `PREPARING` | The session is still starting. | Keep checking the status. | 
| `PENDING_CONCURRENCY` | Your account is at its remote access concurrency limit. | Wait, or stop another session. | 
| `PENDING_DEVICE` | The device is busy or not ready yet. | Wait. After more than 2 minutes, stop the session. Then create a new session, on another device if you can. | 
| `RUNNING` | The session is ready. | Attach the device with `devicefarm-connect device add`. | 
| `STOPPING` | The session is ending. This is not the end state. | Wait for `COMPLETED`. To keep working, create a new session. | 
| `COMPLETED` | The session ended. | Create a new session. | 

**To attach a session after it starts**

1. Check the session status every 20 seconds until it is `RUNNING`:

   ```bash
   aws devicefarm get-remote-access-session --arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}" --query remoteAccessSession.status --output text --region us-west-2
   ```

   This will show output such as the following:

   ```
   RUNNING
   ```

1. Attach the device:

   ```bash
   devicefarm-connect device add --session-arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}"
   ```

If the session ended, create a new session, and attach the device with the new session ARN. For instructions, see [Step 2: Create a remote access session](device-connect-getting-started.md#device-connect-create-session).

## Problems with adb commands
<a name="device-connect-troubleshooting-adb"></a>

adb prints the following messages when you run adb commands through the bridge. The sections after the table cover the adb version and a device that detached.


| Message or symptom | Cause | What to do | 
| --- | --- | --- | 
| `the device connection was refused: {{reason}}`, for example `the device connection was refused: failed to connect to the adb server` | Device Farm refused a new adb connection to the device. The text after the colon is the reason from Device Farm. `failed to connect to the adb server` means that Device Farm couldn't reach the adb server next to the device. | Run the command again. If the error remains, run `devicefarm-connect doctor` with `--session-arn`. If the doctor finds no cause, contact AWS Support. | 
| `Device Farm refused the connection to the device: {{reason}}`, often followed by `(close code {{n}})`, or `Device Farm closed the connection to the device` | Device Farm closed a new adb connection before the device answered. `device add` prints the same text as its cause. | Run the command again. If the error remains, run `devicefarm-connect doctor` with `--session-arn`. If the doctor finds no cause, contact AWS Support. If the reason starts with `Device Connect is not supported`, create a session on a metered public device. | 
| `is not permitted on AWS Device Farm`, for example after `adb root` | Device Farm refuses some adb commands. A refusal ends only that adb connection. The device stays attached and usable. | Remove the command from your workflow. For more information, see [Supported adb commands](device-connect-support.md#device-connect-supported-commands). To stop the bridge, run `devicefarm-connect bridge stop`, not `adb kill-server`. | 
| `error: too many adb connections (limit 24)` | The bridge has the maximum number of open adb connections to the device. The limit counts local, forwarded, and reverse connections together. | Close the shells, logcat streams, and forwarded connections that you don't need. | 
| `device '{{serial}}' not found`, or `adb: no device with transport id '{{id}}'` | The serial or transport ID does not match the attached device. | Run `adb devices -l` to see the serial and the transport ID of the device. If you set `ANDROID_SERIAL`, change it or unset it. | 
| `could not detach the device`, or `the bridge is not listening`, from `device remove` | The cause line names the problem: `the attached device does not match the requested session` or `no device is attached`. `not listening` means that no bridge runs. | To detach the attached device, run `devicefarm-connect device remove` without `--session-arn`. With no device or no bridge, there is nothing to remove. | 

### `adb server version doesn't match this client`
<a name="device-connect-troubleshooting-adb-version"></a>

adb prints messages such as the following:

```
adb server version (41) doesn't match this client (40); killing...
ADB server didn't ACK
could not install *smartsocket* listener: Address already in use
error: cannot connect to daemon
```

Your adb must be version 1.0.41. An adb with another version can't connect through the bridge, so every command fails. The doctor's `Dependencies` row then says that your adb `differs from the remote adb server`.

**To use adb version 1.0.41**

1. Check your adb version:

   ```bash
   adb version
   ```

1. If the first line is not `Android Debug Bridge version 1.0.41`, install Android SDK Platform-Tools whose adb is 1.0.41, such as Platform-Tools 37. In Android Studio, update **Android SDK Platform-Tools** in the SDK Manager.

1. Put the directory of that adb first on your `PATH`.

1. Run the doctor. It checks every adb that it finds on your computer.

   ```bash
   devicefarm-connect doctor --session-arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}"
   ```

### A device detached, or adb lists no device
<a name="device-connect-troubleshooting-device-detached"></a>

A device that you attached is gone, or its adb commands fail. For example, adb prints `adb: no devices/emulators found`, followed by the reason when the bridge detached the device itself, or an adb shell stops after your network drops. `adb wait-for-device` waits until you attach a device.

The bridge looks up the session every few minutes. When a lookup fails after retries, the bridge detaches the device and closes its forward rules and connections. A lookup fails when the session ended, when the credentials expired or lost their permission, or when a network outage lasted through the lookup.

A short network drop doesn't stop an open adb connection, but a drop of about 20 seconds closes it. `adb devices` can still list a device for a few minutes after its commands start to fail.

**To attach the device again**

1. Check the bridge. If it detached a device on its own, the output gives the reason.

   ```bash
   devicefarm-connect bridge status
   ```

   This will show output such as the following:

   ```
   devicefarm-connect bridge is running (PID 4242), no device attached; the last device detached 42 seconds ago: the bridge could not look up remote access session arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000: {{error}}; run 'devicefarm-connect device add --session-arn arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000' to attach it again
   ```

1. Fix the cause. For a network problem, see [Network problems](#device-connect-troubleshooting-network). For a credential problem, see [Renew the credentials of the bridge](#device-connect-troubleshooting-restart-credentials). For a session that ended, see [The session is not RUNNING, or has ended](#device-connect-troubleshooting-not-running).

1. Attach the device again:

   ```bash
   devicefarm-connect device add --session-arn "{{arn:aws:devicefarm:us-west-2:111122223333:session:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/c3d4e5f6-7890-12cd-ef01-EXAMPLE33333/00000}}"
   ```

1. Add the forward rules of the device again.

## Problems with `adb forward` and `adb reverse`
<a name="device-connect-troubleshooting-forwarding"></a>

The following table lists messages for port forwarding rules. For the rules that Device Connect supports, see [Supported port forwarding](device-connect-support.md#device-connect-supported-forwarding). The section after the table covers adb reverse when it is turned off.


| Message or symptom | Cause | What to do | 
| --- | --- | --- | 
| `error: the device's reverse rules are not ready yet; run the command again` | The bridge was still preparing `adb reverse` for the device. This can take a few seconds after you attach the device. | Run the `adb reverse` command again. | 
| `error: adb reverse on this device is held by another bridge, or by this bridge's previous connection for a short while; stop the other bridge or retry later` | Another computer attached the same device with adb reverse on. Only one computer at a time can use `adb reverse` on a device. | On the other computer, run `devicefarm-connect device remove` or `devicefarm-connect bridge stop`. If you can't, wait a few minutes. Then run the command again. | 
| `error: reverse tcp:0 is not supported on AWS Device Farm`, or `error: reverse to a device port in 5555 to 5585 is not permitted on AWS Device Farm` | Device Farm refuses `tcp:0` as the device port. It also refuses device ports 5555 to 5585, the device's own adb range. | Choose a device port outside 5555 to 5585, for example `adb reverse tcp:18082 tcp:18083`. | 
| `error: cannot reverse to tcp:{{port}}: the bridge listens on that port` | The reverse rule names the adb port of the bridge as the port on your computer. The bridge refuses the rule. | Name the port of the server on your computer that the device must reach. | 
| Reverse traffic never reaches your computer. The log shows `a reverse connection was refused` or `a reverse connection failed`. | No server on your computer listens on the port of the rule, or the bridge refused the port. | Read the reason in the log. Run `adb reverse --list`, and fix the rule. Make sure that your local server listens on `127.0.0.1`. | 
| `cannot bind listener: Address already in use`. For `adb forward` on Windows, a Windows socket error follows `cannot bind listener:`. | For `adb forward`, another program uses the local port. For `adb reverse`, something on the device uses the device port. | For `adb forward`, choose another local port, or use `tcp:0`. For `adb reverse`, choose another device port. | 
| `cannot bind listener: unknown socket specification:{{spec}}` | The end of an `adb forward` rule on your computer is not a `tcp:` port. | Use `tcp:{{port}}` as the end on your computer. | 
| `unknown socket specification:{{spec}}` from `adb forward`, for example `adb: error: unknown socket specification:localabstract:chrome_devtools_remote` | The device end of the rule is not a `tcp:` port. At this time, Device Connect forwards only to TCP ports on the device, so the bridge refuses the rule. | Use `tcp:{{port}}` on both ends. A tool that needs a rule to a device socket doesn't work with Device Connect. For more information, see [Unsupported features](device-connect-support.md#device-connect-unsupported). | 
| `unsupported socket specification: {{spec}}; adb reverse accepts only tcp:<port> on AWS Device Farm` | An `adb reverse` rule has an end that is not a `tcp:` port, such as a `localabstract:` socket. Some tools, such as device mirroring in Android Studio, add such a rule themselves. | Use `tcp:` on both ends. A tool that needs a rule to a device socket doesn't work with Device Connect. For more information, see [Unsupported features](device-connect-support.md#device-connect-unsupported). | 
| `error: too many forward rules (limit 8)`, or `error: too many reverse rules (limit 8)` | The device has the maximum number of rules. | Run `adb forward --list` or `adb reverse --list`. Remove a rule that you don't need with `adb forward --remove tcp:{{port}}` or `adb reverse --remove tcp:{{port}}`. | 
| A forwarded connection opens, then closes with no data | Nothing listens on the device port, or the device port is from 5555 to 5585. | Make sure that the app on the device listens on the port in the rule. If the port is from 5555 to 5585, remove the rule and add it again with a device port outside that range. | 

### `adb reverse is off for this bridge`
<a name="device-connect-troubleshooting-reverse-off"></a>

adb prints a message such as the following:

```
error: adb reverse is off for this bridge. '--allow-adb-reverse' turns it on and lets the device open connections to this machine, so use it only with a device you trust. Run 'devicefarm-connect doctor --port 5037' for the commands that restart the bridge with reverse on and attach the device again.
```

adb reverse is off by default. With it off, no connection from the device reaches your computer.

**Important**  
`--allow-adb-reverse` lets the device open connections to this machine, so use it only with a device you trust; a public device can run software you do not control.

To turn on adb reverse, see [Reaching your computer from the device with `adb reverse`](device-connect-interaction.md#device-connect-reverse).

## Problems on Windows
<a name="device-connect-troubleshooting-windows"></a>

The following problems happen on Windows only. For the working directory and port messages on Windows, see [Problems when the bridge starts](#device-connect-troubleshooting-start) and [The bridge can't use the port](#device-connect-troubleshooting-port-in-use).


| Message or symptom | Cause | What to do | 
| --- | --- | --- | 
| A window opens, says that the program is a command line tool, and closes after a few seconds. | You started `devicefarm-connect.exe` from File Explorer, the Start menu, or a shortcut. | Open PowerShell or `cmd.exe`, and run `devicefarm-connect` from there. | 
| Windows shows a SmartScreen notice. | Windows can show the notice for a new release, until Windows has seen the file often. The Windows file has an Authenticode signature from `Amazon Web Services, Inc.` | Verify the download first. For instructions, see [Verify your download](device-connect-getting-started.md#device-connect-verify-download). Then choose **More info**. If Windows names a publisher, the publisher must be `Amazon Web Services, Inc.` If Windows names another publisher, don't run the file. Otherwise, choose **Run anyway**. | 
| `devicefarm-connect bridge stop` fails with the fix `stop it from an elevated shell`. | You started the bridge from an elevated shell. | Open PowerShell as an administrator, and run `devicefarm-connect bridge stop`. To prevent this problem, start the bridge from a shell that is not elevated. | 

## Network problems
<a name="device-connect-troubleshooting-network"></a>

Device Connect needs the following outbound connections from your computer. It needs no inbound ports.
+ HTTPS on port 443 to `devicefarm.us-west-2.amazonaws.com`, for the Device Farm API. This connection uses `HTTPS_PROXY`. Your credentials might also need to reach AWS STS, IAM Identity Center, or instance metadata endpoints.
+ A TLS WebSocket (`wss://`) to the session's device endpoint, `devicefarm-interactive-global.us-west-2.api.aws` on TCP port 443, for adb traffic. This connection doesn't use `HTTPS_PROXY`. It needs a direct outbound connection.

On your computer, the bridge and each forward rule listen on `127.0.0.1`. Reverse connections connect to `127.0.0.1`. Sandboxes, containers, and local firewalls must allow this. The following table lists network messages.


| Message or symptom | Cause | What to do | 
| --- | --- | --- | 
| `x509: certificate signed by unknown authority` | A proxy or security device on your network inspects TLS traffic, and your operating system doesn't trust its certificate. Device Connect uses the trust store of your operating system and TLS 1.2 or later. It has no option to skip certificate checks. | Allow direct TLS connections from your computer to Device Farm, or add the certificate of that proxy or security device to your trust store. Then run `devicefarm-connect device add` again. | 
| Device Farm API calls work through a proxy, but adb commands to the device fail | The adb connections to the device don't use `HTTPS_PROXY`. They need a direct outbound TLS connection. | Run the doctor. When `HTTPS_PROXY` is set and a `Network` check fails, the fix of that check says that the connection to the device doesn't use the proxy. Ask your network administrator to allow direct outbound WebSocket connections (`wss`) to the session's device endpoint on TCP port 443. | 
| `the bridge could not reach the device` from adb, or `cannot connect to Device Farm at {{host}}` when you attach the device. The doctor's `What to do` item for the `Network` row says `could not open a WebSocket connection (wss) to {{host}} on TCP port 443`. | Your computer can't open the WebSocket connection to the device endpoint. For example, a firewall or a proxy on your network blocks it. For an adb command, the connection failed two times in a row. | Check that your computer can reach the host that the message names on TCP port 443. If a firewall or a proxy blocks the connection, ask your network administrator to allow direct outbound WebSocket connections (`wss`) to that host and port. Then run `devicefarm-connect device add` or the adb command again. The doctor command on the `fix:` line tests the connection. | 
| The doctor says `the call to Device Farm for session '{{arn}}' failed` | Your computer can't reach the Device Farm API, or Device Farm returned an error. | Check that your computer can reach `devicefarm.us-west-2.amazonaws.com` on port 443. Set or clear `HTTPS_PROXY` to match your network. A running bridge keeps the `HTTPS_PROXY` of the shell that started it. To give it the new value, run `devicefarm-connect bridge start` again from a shell that has it. | 
| The doctor says `'adb forward' could not open or reach a port on 127.0.0.1` | A sandbox, a container, or a local firewall stops `devicefarm-connect` from listening on `127.0.0.1`. | Allow `devicefarm-connect` to listen on `127.0.0.1` in those rules. Then run `devicefarm-connect doctor` again. | 
| The doctor says `there is an error communicating with the remote adb server` | The adb server next to the device didn't answer the doctor's version request. | Wait, then run the doctor again. If the problem continues, contact AWS Support. | 
| `only wss endpoints are supported for connections to devices` | The session returned a device endpoint that is not `wss://`. The problem is on the Device Farm side. | Run the doctor command on the `fix:` line. If the doctor finds no cause, contact AWS Support. | 