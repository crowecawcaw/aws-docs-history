

# Monitoring
<a name="auto-os-patch-monitoring"></a>

You can view Patch Manager output after each patch is run. By default, Patch Manager stores the first 48,000 characters of the command output. In some cases, you might want to view the complete log, such as for troubleshooting. In this case, the log output can be stored in Amazon S3. For details about how to store log output in Amazon S3, see [Configuring Amazon CloudWatch Logs Logs for Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-rc-setting-up-cwlogs.html) in the * AWS Systems Manager User Guide*.

Another option is to output the logs to Amazon CloudWatch Logs for unified logging. For more information, see [Sending SSM Agent logs to CloudWatch Logs](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-ssm-agent.html) in the * AWS Systems Manager User Guide*.

For information about how to set up detailed monitoring and notifications, see [Monitoring AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring.html) in the * AWS Systems Manager User Guide*.