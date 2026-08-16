# Advanced configuration

This section describes advanced configuration options for Inspector VM Scanner.

## Configuring local outputs

Inspector VM Scanner provides the following options to configure how local outputs are written:

- `--send-results` must be set to `telemetry` or `disabled`. If you pass `disabled`, Inspector VM Scanner proceeds without sending the SBOM.

###### Tip

Use `--state-dir` with `--send-results disabled` to save the SBOM locally.

- `--log-dir` configures where logs are written. By default, logs are written to stdout.
- `--log-level` configures the granularity of logs. By default, this is INFO.
- `--log-retention` configures how many days to retain logs. If a log file older than `--log-retention` is found in `--log-dir`, it is deleted. By default, this is 7 days.
- `--debug` configures debug level logging and forces a dedicated log file for the current execution (rather than trying to maintain one log file for each day).
- `--state-dir` configures where SBOMs are written. By default, SBOMs are not saved.
- `--metric-dir` configures where metric logs are written. By default, metric logs are not saved.
- `--cpu-profile` enables the Go runtime CPU profiler and configures where the result is written.
- `--mem-profile` enables the Go runtime memory profiler and configures where the result is written.
- `--config-path` directs Inspector VM Scanner to derive arguments from a local configuration file. If the same argument is passed in both the CLI and configuration file, the CLI value is prioritized.

  - Inspector VM Scanner configuration files are specified in TOML, with all argument names identical to the CLI.
  - By default, Inspector VM Scanner looks for a configuration file at `/opt/aws/inspector/etc/config` on Linux and macOS, or `C:\\ProgramData\\Amazon\\Inspector\\Config\\config` on Windows. The file has no extension but uses TOML format.
  - When you specify `--config-path`, the specified path takes precedence over the default path.

The following example shows a configuration file:

```
# Configuration file for Inspector VM Scanner
log-level = "INFO"
send-results = "telemetry"
cpu-profile = "cpuprofile"
mem-profile = "memprofile"
log-dir = "log"
state-dir = "state"
debug = false
log-retention = 7
scan-timeout = 300

[sbom]
max-scan-depth = 5
target-directory = ["~"]
```

## Configuring resource usage

Inspector VM Scanner provides the following options to configure resource usage:

- `--scan-timeout` forces the scanner to timeout after a specified number of seconds. By default, the scanner does not timeout.
- `--nice-priority` sets the `nice` priority for the process (available for Unix systems). By default, this is 3.
- `--cpu-limit` sets a hard cap on CPU usage (available for Linux systems using `cgroups`). By default, this is 65%.
- `--process-priority` configures priority for the process (available for Windows systems). By default, this is the `BELOW NORMAL` priority.

###### Note

The default values for `--cpu-limit` and `--process-priority` are identical to Inspector SSM Plugin.

## Configuring scan targets

Inspector VM Scanner leverages Inspector SBOM Generator for inventory collection.
As a result, many of Inspector VM Scanner's scan coverage options are taken directly from SBOM Generator.

By default, Inspector VM Scanner does not scan your entire filesystem. It collects operating system packages, and on Windows it uses Windows Update (Knowledge Base) data to identify system software that needs updating. It also inspects common installation locations for popular programming language packages and their dependencies.

Software installed in a custom or non-standard location – such as a database or application server on a non-system drive – is scanned only if you add it. To cover such software, add it as a custom path in your Amazon EC2 scan settings. Under Enhanced EC2 Scanning, custom paths apply to Linux, Windows, and macOS instances, and are scanned in addition to the default locations. For more information, see [Custom paths for Amazon Inspector deep inspection](scanning-resources.md#deep-inspection-paths "scanning-resources.md#deep-inspection-paths").

You can also add directories per instance during VM Scanner invocation with the advanced options in this section. Directories that you add with `--target-directory` are scanned in addition to the defaults.

Inspector VM Scanner provides the following options to configure scan targets:

- `--max-scan-depth` configures the maximum number of directory levels that a scan traverses from each scan location.
- `--target-directory` adds one or more directories to scan in addition to the defaults. In a configuration file, specify it under `[sbom]` as an array, for example `target-directory = ["D:\\oracle"]`.
- `--override-scanners` configures exact filescanners, overriding Inspector VM Scanner defaults.
- `--additional-scanners` configures filescanners to use in addition to Inspector VM Scanner defaults.

You can use the following command to list all available scanners:

```
./inspector-vm-scanner sbom --list-scanners
```

## Managing periodic execution

When you install Inspector VM Scanner through a package manager, the installation creates a scheduled task that executes scans automatically.
You can view, modify, or disable this schedule.

### Linux (systemd)

**View service status and recent runs**

```
systemctl status inspector-vm-scanner
```

**View real-time logs**

```
journalctl -u inspector-vm-scanner -f
```

**View recent logs**

```
journalctl -u inspector-vm-scanner --since "1 hour ago"
```

**Check current timer interval**

```
systemctl cat inspector-vm-scanner.timer
```

#### Change the scan interval

###### Important

Do not edit the unit files in `/usr/lib/systemd/system/` directly.
Package updates overwrite those files. Use `systemctl edit` instead,
which creates a persistent override that survives updates.

The default interval is every 3 hours. To change it, run:

```
sudo systemctl edit inspector-vm-scanner.timer
```

In the editor that opens, add the following (this example sets the interval to 6 hours):

```
[Timer]
OnBootSec=
OnUnitActiveSec=
OnBootSec=0
OnUnitActiveSec=21600s
```

The empty assignments clear the defaults before your values take effect. After saving, restart the timer:

```
sudo systemctl daemon-reload
sudo systemctl restart inspector-vm-scanner.timer
```

To verify that the override took effect, run `systemctl cat inspector-vm-scanner.timer`.
To revert to defaults, run `sudo systemctl revert inspector-vm-scanner.timer`.

#### Enable or disable automatic execution

```
sudo systemctl enable inspector-vm-scanner.timer   # Enable automatic runs.
sudo systemctl disable inspector-vm-scanner.timer  # Disable automatic runs.
```

### Windows (Task Scheduler)

**View task status and last run**

```
Get-ScheduledTask -TaskName "Inspector VM Scanner" | Get-ScheduledTaskInfo
```

**View recent task logs**

```
Get-ScheduledTaskInfo -TaskName "Inspector VM Scanner"
```

**View detailed task history**

```
schtasks /query /tn "Inspector VM Scanner" /v /fo list
```

**View current task schedule**

```
Get-ScheduledTask -TaskName "Inspector VM Scanner" | Select-Object -ExpandProperty Triggers
```

**Update task schedule**

To change the scan frequency:

```
# Modify trigger to run daily at 2 AM
$trigger = New-ScheduledTaskTrigger -Daily -At 2:00AM
Set-ScheduledTask -TaskName "Inspector VM Scanner" -Trigger $trigger
```

**Enable or disable task**

```
Enable-ScheduledTask -TaskName "Inspector VM Scanner"   # Enable automatic runs
Disable-ScheduledTask -TaskName "Inspector VM Scanner"  # Disable automatic runs
```

### macOS (launchd)

**View launchd task**

```
sudo launchctl print system/com.amazon.inspector.vm-scanner
```

**Execute single task**

```
sudo launchctl start com.amazon.inspector.vm-scanner
```
