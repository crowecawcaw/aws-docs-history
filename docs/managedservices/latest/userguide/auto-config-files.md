# CloudWatch configuration files, update details

We read your custom CloudWatch configurations (JSON only) from the following CloudWatch directories (see
[recommended directories](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.md")),
and merge them with the standard AMS CloudWatch configuration:

- CloudWatch Files
  - On the instance:
    - Windows
      - %ProgramData%\Amazon\AmazonCloudWatchAgent\Configs\
      - %ProgramFiles%\WindowsPowerShell\Modules\AWSManagedServices.Logging.Utilities\Files\Config.json

    - Linux
      - /opt/aws/ams/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json

  - On Amazon S3:
    - Windows:
      - https://ams-configuration-artifacts-`REGION_NAME`.s3.`REGION_NAME`.amazonaws.com/configurations/cloudwatch/latest/windows-cloudwatch-config.json

    - Linux:
      - https://ams-configuration-artifacts-`REGION_NAME`.s3.`REGION_NAME`.amazonaws.com/configurations/cloudwatch/latest/linux-cloudwatch-config.json
