

# Reboot a Deadline Cloud worker after host configuration
<a name="examples-host-config-reboot"></a>

The [worker\_reboot](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/worker_reboot) sample on the GitHub website includes Linux and Windows scripts that reboot a Deadline Cloud worker after host configuration completes. Worker reboots are commonly required after driver installations or domain joins.

When the worker starts, host configuration scripts run during the `STARTED` state. The Linux script issues a standard `reboot` command and sleeps for 60 seconds while the host shuts down to prevent the worker agent from starting job processing. A `rebooted` marker file indicates that a reboot was issued. On the second start, the Deadline Cloud agent begins processing jobs.

The Windows script uses a marker file at `C:\deadline-rebooted` and issues `Restart-Computer -Force` if the marker file doesn't yet exist.