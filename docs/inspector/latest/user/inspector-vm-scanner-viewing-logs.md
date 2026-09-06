

# Viewing logs
<a name="inspector-vm-scanner-viewing-logs"></a>

 Inspector VM Scanner logs always start with `inspector-vm-scanner` and end with `.log`. 

 On Unix systems, Inspector VM Scanner writes logs to `/var/log/amazon/inspector`. On Windows, Inspector VM Scanner writes logs to `C:\ProgramData\Amazon\Inspector\Logs`. 

 Both of these paths are identical to what Inspector SSM Plugin used. This means that you might see old Inspector SSM Plugin logs alongside Inspector VM Scanner logs. 

 Inspector VM Scanner can also output optional metric logs, which track CPU and memory usage throughout program execution. These logs are written to the log directories mentioned previously, under a subdirectory named `metrics` (`Metrics` on Windows). See [Advanced configuration](inspector-vm-scanner-advanced-config.md) for more details. 

## Viewing logs with systemd
<a name="inspector-vm-scanner-viewing-logs-systemd"></a>

 On Linux systems using systemd, you can use **journalctl** to view Inspector VM Scanner logs. 

 **View real-time logs** 

```
journalctl -u inspector-vm-scanner -f
```

 **View recent logs** 

```
journalctl -u inspector-vm-scanner --since "1 hour ago"
```

 **View logs from today** 

```
journalctl -u inspector-vm-scanner --since today
```

 **View service status and recent runs** 

```
systemctl status inspector-vm-scanner
```