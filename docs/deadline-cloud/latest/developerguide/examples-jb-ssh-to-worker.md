

# SSH or RDP to a Deadline Cloud worker through Session Manager
<a name="examples-jb-ssh-to-worker"></a>

The [ssh\_to\_smf](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/ssh_to_smf) (Linux) and [ssh\_to\_smf\_windows](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/ssh_to_smf_windows) (Windows) job bundles on the GitHub website give SSH, RDP, or PowerShell access to Deadline Cloud workers. Each bundle registers the worker as an SSM hybrid managed node through Session Manager during the job. Use these bundles to debug a job on the worker. You can also forward ports for web UIs and Jupyter notebooks.

The job follows this sequence:

1. The submit script starts a one-time SSM hybrid activation by calling `aws ssm create-activation`.

1. The Deadline Cloud job runs on a worker and registers it as a managed node. The job prints the `mi-*` node ID to the job log.

1. You connect with `aws ssm start-session --target mi-{{XXXXXXXXX}}`.

1. After the session time expires, the job removes the node and cleans up.

**To set up SSH access (one time per account and Region)**

1. Create an IAM role named `SSMServiceRole`. Add the SSM service principal as the trust and attach the `AmazonSSMManagedInstanceCore` managed policy.

1. For the Linux variant, use the [sudo\_for\_job\_user](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/sudo_for_job_user) script on the GitHub website. For the Windows variant, use the bundle's `setup/host_config.ps1` script.

**Note**  
The advanced-instances tier no longer exists. You don't need a tier setting to use Session Manager on hybrid managed nodes.

**Important**  
The Windows variant gives the RDP user local Administrator access. It also adds `job-user` to `Administrators`. Use this setup for debugging only. Shut down all workers in the fleet after you finish debugging.

Submit the job:

```
# Linux: 60-minute session
./submit.sh

# Linux: 120-minute session
./submit.sh 120

# Windows: 60-minute session
./submit.sh farm-{{XXXX}} queue-{{YYYY}}
```

After the job starts, find the managed node ID in the job log and connect:

```
aws ssm start-session --target mi-{{XXXXXXXXX}} --region {{region}}
```