

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# CloudWatch configuration files, update details
<a name="auto-config-files"></a>

 We read your custom CloudWatch configurations (JSON only) from the following CloudWatch directories (see [recommended directories](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html)), and merge them with the standard AMS CloudWatch configuration: 
+ CloudWatch Files
  + On the instance:
    + Windows
      + %ProgramData%\\Amazon\\AmazonCloudWatchAgent\\Configs\\
      + %ProgramFiles%\\WindowsPowerShell\\Modules\\AWSManagedServices.Logging.Utilities\\Files\\Config.json
    + Linux
      + /opt/aws/ams/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
  + On Amazon S3:
    + Windows:
      + https://ams-configuration-artifacts-{{REGION\_NAME}}.s3.{{REGION\_NAME}}.amazonaws.com/configurations/cloudwatch/latest/windows-cloudwatch-config.json
    + Linux:
      + https://ams-configuration-artifacts-{{REGION\_NAME}}.s3.{{REGION\_NAME}}.amazonaws.com/configurations/cloudwatch/latest/linux-cloudwatch-config.json