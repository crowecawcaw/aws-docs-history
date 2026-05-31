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

By default, Inspector VM Scanner uses SBOM Generator's `localhost` scanner group, as well as `certificate` and `windows-kb` scanners.

Inspector VM Scanner provides the following options to configure scan targets:

- `--max-scan-depth` configures the maximum number of directories that scans traverse.
- `--target-directories` configures additional directories to scan outside of defaults.
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

**Update timer interval**

To change the scan frequency, edit the timer unit file:

```
# Edit the timer unit file
systemctl edit inspector-vm-scanner.timer

# Add override configuration:
[Timer]
OnCalendar=
OnCalendar=daily

# Reload and restart
systemctl daemon-reload
systemctl restart inspector-vm-scanner.timer
```

**Enable or disable automatic execution**

```
systemctl enable inspector-vm-scanner.timer   # Enable automatic runs
systemctl disable inspector-vm-scanner.timer  # Disable automatic runs
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
