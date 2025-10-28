# Slurm log rotations

SageMaker HyperPod provides automatic log rotation for Slurm daemon logs to help manage disk space usage and
maintain system performance. Log rotation is crucial for preventing logs from consuming excessive disk space and
ensuring optimal system operation by automatically archiving and removing old log files while maintaining recent
logging information. Slurm log rotations are enabled by default when you create a cluster.

## How log rotation works

When enabled, the log rotation configuration:

- Monitors all Slurm log files with the extension `.log` located in the
  `/var/log/slurm/` folder on the controller, login and compute nodes.
- Rotates logs when they reach 50 MB in size.
- Maintains up to two rotated log files before deleting them.
- Sends SIGUSR2 signal to Slurm daemons (`slurmctld`, `slurmd`,
  and `slurmdbd`) after rotation.

## List of log files rotated

Slurm logs are located in the `/var/log/slurm/` directory. Log rotation is enabled for all
files that match `/var/log/slurm/*.log`. When rotation occurs, rotated files have numerical suffixes
(such as `slurmd.log.1`). The following list is not exhaustive but shows some of the critical log files that rotate automatically:

- `/var/log/slurm/slurmctld.log`
- `/var/log/slurm/slurmd.log`
- `/var/log/slurm/slurmdb.log`
- `/var/log/slurm/slurmrestd.log`

## Enable or disable log rotation

You can control the log rotation feature using the `enable_slurm_log_rotation` parameter in the
`config.py` script of your cluster's lifecycle scripts, as shown in the following example:

```
class Config:
    # Set false if you want to disable log rotation of Slurm daemon logs
    enable_slurm_log_rotation = True  # Default value
```

To disable log rotation, set the parameter to `False`, as shown in the following example:

```
enable_slurm_log_rotation = False
```

###### Note

Lifecycle scripts run on all Slurm nodes (controller, login, and compute nodes) during cluster creation.
They also run on new nodes when added to the cluster. Updating the log rotation configurations must be
done manually after cluster creation. The log rotation configuration is stored in `/etc/logrotate.d/sagemaker-hyperpod-slurm`.
We recommend keeping log rotation enabled to prevent log files from consuming excessive disk space. To disable
log rotation, delete the `sagemaker-hyperpod-slurm` file or comment out its contents by
adding `#` at the start of each line in the `sagemaker-hyperpod-slurm` file.

## Default log rotation settings

The following settings are configured automatically for each log file rotated:

| Setting        | Value    | Description                                |
| -------------- | -------- | ------------------------------------------ |
| `rotate`       | 2        | Number of rotated log files to keep        |
| `size`         | 50 MB    | Maximum size before rotation               |
| `copytruncate` | enabled  | Copies and truncates the original log file |
| `compress`     | disabled | Rotated logs are not compressed            |
| `missingok`    | enabled  | No error if log file is missing            |
| `notifempty`   | enabled  | Doesn't rotate empty files                 |
| `noolddir`     | enabled  | Rotated files stay in same directory       |
