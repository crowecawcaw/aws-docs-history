# Integration with Amazon CloudWatch Logs

For more information about CloudWatch Logs, see [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md"). To configure CloudWatch Logs integration, see the [Monitoring](Monitoring-v3.md "Monitoring-v3.md") section.
To learn how to append custom logs to the CloudWatch configuration using `append-config`, see
[Multiple CloudWatch agent configuration files](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-common-scenarios.md#CloudWatch-Agent-multiple-config-files "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-common-scenarios.md#CloudWatch-Agent-multiple-config-files")
in the _Amazon CloudWatch User Guide_.

## Amazon CloudWatch Logs cluster logs

A log group is created for each cluster with a name,
`/aws/parallelcluster/`cluster-name-<timestamp>``(for example,
 `/aws/parallelcluster/testCluster-202202050215`). Each log (or set of logs if the path contains a `*`) on each node has a
 log stream named
``{hostname}`.`{instance_id}`.`{logIdentifier}``. (For
 example `ip-172-31-10-46.i-02587cf29cc3048f3.nodewatcher`.) Log data is sent to CloudWatch by the [CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md"), which runs as `root` on all cluster
instances.

An Amazon CloudWatch dashboard is created when the cluster is created. This dashboard
gives you the ability to review the logs stored in CloudWatch Logs. For more information, see [Amazon CloudWatch dashboard](cloudwatch-dashboard-v3.md "cloudwatch-dashboard-v3.md").

This list contains the `logIdentifier` and path for the log streams available for platforms, schedulers, and nodes.

| Log streams available for platforms, schedulers, and nodes | Platforms         | Schedulers               | Nodes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Log streams |
| ---------------------------------------------------------- | ----------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| amazon<br>redhat<br>ubuntu                                 | awsbatch<br>slurm | HeadNode                 | dcv-authenticator: `/var/log/parallelcluster/pcluster_dcv_authenticator.log`<br>dcv-ext-authenticator: `/var/log/parallelcluster/pcluster_dcv_connect.log`<br>dcv-agent: `/var/log/dcv/agent.*.log`<br>dcv-xsession: `/var/log/dcv/dcv-xsession.*.log`<br>dcv-server: `/var/log/dcv/server.log`<br>dcv-session-launcher: `/var/log/dcv/sessionlauncher.log`<br>Xdcv: `/var/log/dcv/Xdcv.*.log`<br>cfn-init: `/var/log/cfn-init.log`<br>chef-client: `/var/log/chef-client.log`                                                                                                                                                            |
| amazon<br>redhat<br>ubuntu                                 | awsbatch<br>slurm | ComputeFleet<br>HeadNode | cloud-init: `/var/log/cloud-init.log`<br>supervisord: `/var/log/supervisord.log`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| amazon<br>redhat<br>ubuntu                                 | slurm             | ComputeFleet             | cloud-init-output: `/var/log/cloud-init-output.log`<br>computemgtd: `/var/log/parallelcluster/computemgtd`<br>slurmd: `/var/log/slurmd.log`<br>slurm_prolog_epilog: `/var/log/parallelcluster/slurm_prolog_epilog.log`                                                                                                                                                                                                                                                                                                                                                                                                                    |
| amazon<br>redhat<br>ubuntu                                 | slurm             | HeadNode                 | sssd: `/var/log/sssd/sssd.log`<br>sssd_domain_default: `/var/log/sssd/sssd_default.log`<br>pam_ssh_key_generator: `/var/log/parallelcluster/pam_ssh_key_generator.log`<br>clusterstatusmgtd: `/var/log/parallelcluster/clusterstatusmgtd`<br>clustermgtd: `/var/log/parallelcluster/clustermgtd`<br>compute_console_output: `/var/log/parallelcluster/compute_console_output`<br>slurm_resume: `/var/log/parallelcluster/slurm_resume.log`<br>slurm_suspend: `/var/log/parallelcluster/slurm_suspend.log`<br>slurmctld: `/var/log/slurmctld.log`<br>slurm_fleet_status_manager: `/var/log/parallelcluster/slurm_fleet_status_manager.log` |
| amazon<br>redhat                                           | awsbatch<br>slurm | ComputeFleet<br>HeadNode | system-messages: `/var/log/messages`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ubuntu                                                     | awsbatch<br>slurm | ComputeFleet<br>HeadNode | syslog: `/var/log/syslog`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

Jobs in clusters that use AWS Batch store the output of jobs that reached a state of `RUNNING`, `SUCCEEDED`, or
`FAILED` in CloudWatch Logs. The log group is `/aws/batch/job`, and the log stream name format is
``jobDefinitionName`/default/`ecs_task_id``. By default, these logs are set not to
expire, but you can modify the retention period. For more information, see [Change log data
retention in CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/SettingLogRetention.md "../../../AmazonCloudWatch/latest/logs/SettingLogRetention.md") in the _Amazon CloudWatch Logs User Guide_.

## Amazon CloudWatch Logs build image logs

A log group is created for each custom build image with a name,
`/aws/imagebuilder/ParallelClusterImage-`<image-id>``. A unique log stream with name,
 `{pcluster-version}`/1 contains the output of the build image process.

You can access the logs by using the [pcluster](pcluster-v3.md "pcluster-v3.md") image commands. For more information, see [AWS ParallelCluster AMI customization](custom-ami-v3.md "custom-ami-v3.md").
