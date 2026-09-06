

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Amazon Elastic Compute Cloud (Amazon EC2) - system level logs
<a name="access-to-logs-ec2"></a>

Instance logs are collected by a CloudWatch Logs agent running on the instance and can be accessed through a CloudWatch Log group of the same name as the instance. For example, if the instance ID is i-0123456789abcdef0 and the log file name is /var/log/messages, the Log Group would be i-0123456789abcdef0 and the Log Stream /var/log/messages.

See also [AMS aggregated service logs](service-logs.md).

To access your logs, ensure that you have one of the required IAM roles and are in your AMS account. Then navigate to the directory shown.

**Note**  
The following logs are collected by default.

**Amazon Linux / Red Hat Linux / Centos Linux / Ubuntu / SUSE Linux**

**Log file / Log stream**

```
/var/log/amazon/ssm/amazon-ssm-agent.log
/var/log/amazon/ssm/errors.log
/var/log/audit/audit.log
/var/log/cloud-init-output.log
/var/log/cfn-init.log
/var/log/cfn-init-cmd.log
/var/log/cloud-init.log (Amazon Linux 1 / Amazon Linux 2 only)
/var/log/cron
/var/log/dnf.log
/var/log/maillog
/var/log/messages
/var/log/secure
/var/log/spooler
/var/log/yum.log
/var/log/aws/ams/bootstrap.log
/var/log/aws/ams/build.log
/var/log/syslog
/var/log/dpkg.log
/var/log/auth.log
/var/log/zypper.log
```

**Note**  
For information on accessing logs for Amazon Linux 2023, see [Why is the /var/log directory missing logs in my EC2 Amazon Linux 2023 instance?](https://repost.aws/knowledge-center/ec2-linux-al2023-find-log-files)

**Windows**

**Log file / Log stream**

```
SecurityEventLog
SystemEventLog
AmazonSSMAgentLog
MicrosoftWindowsAppLockerMSIAndScriptEventLog
MicrosoftWindowsAppLockerEXEAndDLLEventLog
AmazonCloudWatchAgentLog
EC2ConfigServiceEventLog (Windows Server 2012 R2 Only)
ApplicationEventLog
AmazonCloudFormationLog
MicrosoftWindowsGroupPolicyOperationalEventLog
AmazonSSMErrorLog
```