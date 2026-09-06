

# SSH or RDP to a Deadline Cloud worker through Session Manager
<a name="examples-jb-ssh-to-worker"></a>

The [ssh\_to\_smf](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/ssh_to_smf) (Linux) and [ssh\_to\_smf\_windows](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/ssh_to_smf_windows) (Windows) job bundles on the GitHub website register a Deadline Cloud worker as an SSM hybrid managed node, enabling SSH, RDP, or PowerShell access through Session Manager for the duration of the job. Use these bundles to debug a job interactively or to forward ports for web UIs and Jupyter notebooks running on the worker.

The job follows this sequence:

1. The submit script creates a one-time SSM hybrid activation by calling `aws ssm create-activation`.

1. The Deadline Cloud job runs on a worker, registers the worker as a managed node, and prints the `mi-*` managed node ID to the job log.

1. You connect with `aws ssm start-session --target mi-{{XXXXXXXXX}}`.

1. After the configured session duration, the job deregisters the node and cleans up.

**To set up SSH access for one-time per account and Region**

1. Create an IAM role named `SSMServiceRole` with the SSM service principal trust and the `AmazonSSMManagedInstanceCore` managed policy attached.

1. Enable the advanced-instances tier:

   ```
   aws ssm update-service-setting \
     --setting-id "arn:aws:ssm:{{region}}:{{account-id}}:servicesetting/ssm/managed-instance/activation-tier" \
     --setting-value "advanced" \
     --region {{region}}
   ```

1. The Linux variant requires the [sudo\_for\_job\_user](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/sudo_for_job_user) host configuration script on the GitHub website, and the Windows variant requires the bundle's `setup/host_config.ps1` as the fleet host configuration script.

**Important**  
The Windows variant gives the RDP user local Administrator access and adds `job-user` to `Administrators`. Use this configuration for debugging only. Shut down all workers in the fleet after debugging completes.

Submit the job:

```
# Linux: 60-minute session
./submit.sh

# Linux: 120-minute session
./submit.sh 120

# Windows: 60-minute session
./submit.sh farm-{{XXX}} queue-{{XXX}}
```

Once the job is running, find the managed node ID in the job log and connect:

```
aws ssm start-session --target mi-{{XXXXXXXXX}} --region {{region}}
```