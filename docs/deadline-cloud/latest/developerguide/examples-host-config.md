# Host configuration script examples for Deadline Cloud

Host configuration scripts run with elevated privileges on
service-managed fleet workers, which lets you install software, configure
runtimes, and perform other administrative tasks. The
[host\_configuration\_scripts](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts")
directory in the deadline-cloud-samples repository on the GitHub website
includes sample scripts for common configuration tasks.

To attach a script to a fleet, use the Deadline Cloud console or the
`update-fleet` CLI command. For details, see
[Run host configuration scripts with administrator privileges](smf-admin.md "smf-admin.md").

Fleet host configuration logs stream to the fleet's CloudWatch log
group (for example,
`/aws/deadline/farm-`FARM_ID`/fleet-`FLEET_ID``).
Each worker has a dedicated log stream that includes the
`Running Host Configuration Script` and
`Finished running Host Configuration Script, exit code:`
banners.

###### Topics

- [Run Docker containers with NVIDIA GPUs on Deadline Cloud workers](examples-host-config-docker-nvidia.md "examples-host-config-docker-nvidia.md")
- [Install Autodesk 3ds Max on Deadline Cloud Windows workers](examples-host-config-3dsmax.md "examples-host-config-3dsmax.md")
- [Install Adobe After Effects with Red Giant on Deadline Cloud Windows workers](examples-host-config-aftereffects.md "examples-host-config-aftereffects.md")
- [Install Cinema 4D with Red Giant on Deadline Cloud Windows workers](examples-host-config-cinema4d.md "examples-host-config-cinema4d.md")
- [Install custom fonts on Deadline Cloud Linux workers](examples-host-config-fonts.md "examples-host-config-fonts.md")
- [Grant passwordless sudo to job-user on Deadline Cloud Linux workers](examples-host-config-sudo.md "examples-host-config-sudo.md")
- [Enable swap on Deadline Cloud Linux workers](examples-host-config-swap.md "examples-host-config-swap.md")
- [Configure the Windows page file on Deadline Cloud workers](examples-host-config-page-file.md "examples-host-config-page-file.md")
- [Reboot a Deadline Cloud worker after host configuration](examples-host-config-reboot.md "examples-host-config-reboot.md")
