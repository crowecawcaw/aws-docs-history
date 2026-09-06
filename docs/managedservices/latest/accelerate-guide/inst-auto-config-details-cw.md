

# CloudWatch configuration change details
<a name="inst-auto-config-details-cw"></a>

Additional detail on the CloudWatch configuration.
+ CloudWatch configuration file location on the instance:
  + Windows: %ProgramData%\\Amazon\\AmazonCloudWatchAgent\\amazon-cloudwatch-agent.json
  + Linux: /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.d/ams-accelerate-config.json
+ CloudWatch configuration file location in Amazon S3:
  + Windows: https://ams-configuration-artifacts-{{REGION\_NAME}}.s3.{{REGION\_NAME}}.amazonaws.com/configurations/cloudwatch/latest/windows-cloudwatch-config.json
  + Linux: https://ams-configuration-artifacts-{{REGION\_NAME}}.s3.{{REGION\_NAME}}.amazonaws.com/configurations/cloudwatch/latest/linux-cloudwatch-config.json
+ Metrics collected:
  + Windows:
    + AWS Systems Manager SSM Agent (CPU\_Usage)
    + CloudWatch Agent (CPU\_Usage)
    + Disk space utilization for all disks (% free space)
    + Memory (% committed bytes in use)
  + Linux:
    + AWS Systems Manager SSM Agent (CPU\_Usage)
    + CloudWatch Agent (CPU\_Usage)
    + CPU (cpu\_usage\_idle, cpu\_usage\_iowait, cpu\_usage\_user, cpu\_usage\_system)
    + Disk (used\_percent, inodes\_used, inodes\_total)
    + Diskio (io\_time, write\_bytes, read\_bytes, writes, reads)
    + Mem (mem\_used\_percent)
    + Swap (swap\_used\_percent)
+ Logs collected:
  + Windows:
    + AmazonSSMAgentLog
    + AmazonCloudWatchAgentLog
    + AmazonSSMErrorLog
    + AmazonCloudFormationLog
    + ApplicationEventLog
    + EC2ConfigServiceEventLog
    + MicrosoftWindowsAppLockerEXEAndDLLEventLog
    + MicrosoftWindowsAppLockerMSIAndScriptEventLog
    + MicrosoftWindowsGroupPolicyOperationalEventLog
    + SecurityEventLog
    + SystemEventLog
  + Linux:
    + /var/log/amazon/ssm/amazon-ssm-agent.log
    + /var/log/amazon/ssm/errors.log
    + /var/log/audit/audit.log
    + /var/log/cloud-init-output.log
    + /var/log/cloud-init.log
    + /var/log/cron
    + /var/log/dpkg.log
    + /var/log/maillog
    + /var/log/messages
    + /var/log/secure
    + /var/log/spooler
    + /var/log/syslog
    + /var/log/yum.log
    + /var/log/zypper.log