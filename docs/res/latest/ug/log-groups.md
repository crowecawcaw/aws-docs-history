# Amazon CloudWatch Logs

Research and Engineering Studio creates the following log groups in CloudWatch during installation. See the following
table for default retentions:

| CloudWatch Log groups                                                             | Retention    |
| --------------------------------------------------------------------------------- | ------------ |
| `/aws/lambda/`<installation-stack-name>`-cluster-endpoints`                       | Never expire |
| `/aws/lambda/`<installation-stack-name>`-cluster-manager-scheduled-ad-sync`       | Never expire |
| `/aws/lambda/`<installation-stack-name>`-cluster-settings`                        | Never expire |
| `/aws/lambda/`<installation-stack-name>`-oauth-credentials`                       | Never expire |
| `/aws/lambda/`<installation-stack-name>`-self-signed-certificate`                 | Never expire |
| `/aws/lambda/`<installation-stack-name>`-update-cluster-prefix-list`              | Never expire |
| `/aws/lambda/`<installation-stack-name>`-vdc-scheduled-event-transformer`         | Never expire |
| `/aws/lambda/`<installation-stack-name>`-vdc-update-cluster-manager-client-scope` | Never expire |
| `/`<installation-stack-name>`/cluster-manager`                                    | 3 months     |
| `/`<installation-stack-name>`/vdc/controller`                                     | 3 months     |
| `/`<installation-stack-name>`/vdc/dcv-broker`                                     | 3 months     |
| `/`<installation-stack-name>`/vdc/dcv-connection-gateway`                         | 3 months     |

If you would like to change the default retention for a log group, you can go to the
[CloudWatch console](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch") and follow the directions to
[Change log data retention in CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SettingLogRetention "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SettingLogRetention").
