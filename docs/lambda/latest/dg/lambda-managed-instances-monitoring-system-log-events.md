

# Capacity provider system log event reference
<a name="lambda-managed-instances-monitoring-system-log-events"></a>

Lambda publishes system log events for capacity provider instance lifecycle operations. The following table shows the events that Lambda publishes and whether each event is logged based on your configured system log level.

For more information about configuring the system log level, see [Log-level filtering for capacity provider system logs](lambda-managed-instances-monitoring-log-levels.md). For details on the log entry format, see [Capacity provider system log format](lambda-managed-instances-monitoring-log-format.md).

## System log event level mapping
<a name="lambda-managed-instances-system-log-event-mapping"></a>


| Event | Description | `DEBUG` | `INFO` | `WARN` | 
| --- | --- | --- | --- | --- | 
| Launching | Emitted when Lambda initiates an instance launch for the capacity provider. | Logged | Logged | Not logged | 
| Launched | Emitted when an instance successfully transitions to an active state and is ready to serve invocations. | Logged | Logged | Not logged | 
| LaunchFailed | Emitted when an instance launch attempt fails. | Logged | Logged | Logged | 
| Terminating | Emitted when Lambda marks an instance for termination. | Logged | Logged | Not logged | 
| Terminated | Emitted when an instance is successfully terminated. | Logged | Logged | Not logged | 
| TerminateFailed | Emitted when Lambda fails to terminate an instance. | Logged | Logged | Logged | 
| HealthCheckFailed | Emitted when an instance fails its health check and is marked as unhealthy. | Logged | Logged | Logged | 

**Note**  
This list expands as Lambda adds new capacity provider capabilities.