

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Automatically configured logs
<a name="auto-config-logs-cw"></a>

We configure your instance to write the following logs.
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