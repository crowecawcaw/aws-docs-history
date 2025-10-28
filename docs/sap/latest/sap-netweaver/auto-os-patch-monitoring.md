# Monitoring

You can view Patch Manager output after each patch is run. By default, Patch Manager stores the first 48,000 characters of the command output. In some cases, you might want to view the complete log, such as for troubleshooting. In this case, the log output can be stored in Amazon S3. For details about how to store log output in Amazon S3, see [Configuring Amazon CloudWatch Logs Logs for Run Command](../../../systems-manager/latest/userguide/sysman-rc-setting-up-cwlogs.md "../../../systems-manager/latest/userguide/sysman-rc-setting-up-cwlogs.md") in the _AWS Systems Manager User Guide_.

Another option is to output the logs to Amazon CloudWatch Logs for unified logging. For more information, see [Sending SSM Agent logs to CloudWatch Logs](../../../systems-manager/latest/userguide/monitoring-ssm-agent.md "../../../systems-manager/latest/userguide/monitoring-ssm-agent.md") in the _AWS Systems Manager User Guide_.

For information about how to set up detailed monitoring and notifications, see [Monitoring AWS Systems Manager](../../../systems-manager/latest/userguide/monitoring.md "../../../systems-manager/latest/userguide/monitoring.md") in the _AWS Systems Manager User Guide_.
