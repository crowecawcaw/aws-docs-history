# Grant passwordless sudo to job-user on Deadline Cloud Linux workers

The
[sudo\_for\_job\_user](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/sudo_for_job_user "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/sudo_for_job_user")
host configuration script on the GitHub website grants the Deadline Cloud `job-user` account
passwordless sudo access on Linux service-managed fleet workers. Some
workloads require root privileges, for example to install packages, mount
file systems, or register the worker as an SSM managed node. By default,
`job-user` doesn't have sudo access.

The script adds a sudoers rule that allows `job-user` to
run any command as root without a password prompt. If
`job-user` doesn't yet exist (for example, the worker agent
hasn't created it), the script logs a warning and exits successfully so
that it doesn't block fleet provisioning.

###### Important

Granting passwordless sudo to `job-user` means that any
job running on the worker can execute arbitrary commands as root. Only
enable this script on fleets where you trust the jobs being submitted,
and consider scoping the sudoers rule to specific commands when your
use case allows it.

This script is required by the Linux variant of the
[SSH or RDP to a Deadline Cloud worker through Session Manager](examples-jb-ssh-to-worker.md "examples-jb-ssh-to-worker.md") sample.
