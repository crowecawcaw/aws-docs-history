# CloudWatch configuration change details

Additional detail on the CloudWatch configuration.

- CloudWatch configuration file location on the instance:
  - Windows: %ProgramData%\Amazon\AmazonCloudWatchAgent\amazon-cloudwatch-agent.json
  - Linux: /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.d/ams-accelerate-config.json

- CloudWatch configuration file location in Amazon S3:
  - Windows: https://ams-configuration-artifacts-`REGION_NAME`.s3.`REGION_NAME`.amazonaws.com/configurations/cloudwatch/latest/windows-cloudwatch-config.json
  - Linux: https://ams-configuration-artifacts-`REGION_NAME`.s3.`REGION_NAME`.amazonaws.com/configurations/cloudwatch/latest/linux-cloudwatch-config.json

- Metrics collected:
  - Windows:
    - AWS Systems Manager SSM Agent (CPU_Usage)
    - CloudWatch Agent (CPU_Usage)
    - Disk space utilization for all disks (% free space)
    - Memory (% committed bytes in use)

  - Linux:
    - AWS Systems Manager SSM Agent (CPU_Usage)
    - CloudWatch Agent (CPU_Usage)
    - CPU (cpu_usage_idle, cpu_usage_iowait, cpu_usage_user, cpu_usage_system)
    - Disk (used_percent, inodes_used, inodes_total)
    - Diskio (io_time, write_bytes, read_bytes, writes, reads)
    - Mem (mem_used_percent)
    - Swap (swap_used_percent)

- Logs collected:
  - Windows:
    - AmazonSSMAgentLog
    - AmazonCloudWatchAgentLog
    - AmazonSSMErrorLog
    - AmazonCloudFormationLog
    - ApplicationEventLog
    - EC2ConfigServiceEventLog
    - MicrosoftWindowsAppLockerEXEAndDLLEventLog
    - MicrosoftWindowsAppLockerMSIAndScriptEventLog
    - MicrosoftWindowsGroupPolicyOperationalEventLog
    - SecurityEventLog
    - SystemEventLog

  - Linux:
    - /var/log/amazon/ssm/amazon-ssm-agent.log
    - /var/log/amazon/ssm/errors.log
    - /var/log/audit/audit.log
    - /var/log/cloud-init-output.log
    - /var/log/cloud-init.log
    - /var/log/cron
    - /var/log/dpkg.log
    - /var/log/maillog
    - /var/log/messages
    - /var/log/secure
    - /var/log/spooler
    - /var/log/syslog
    - /var/log/yum.log
    - /var/log/zypper.log
