# Logging differences: Managed EC2 vs Container fleets

Logging behavior differs significantly between managed EC2 fleets and container fleets. Understanding these differences is crucial when migrating from EC2 to containers or choosing the right fleet type for your logging requirements.

## Key differences overview

| Feature                  | Managed EC2 Fleets                                          | Container Fleets                                                 |
| ------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------- |
| Log storage              | Automatically uploaded to Amazon S3 after game session ends | Must configure Amazon CloudWatch Logs or custom logging solution |
| GetGameSessionLogUrl API | Available<br>• returns Amazon S3 URL for log download       | Not available<br>• logs not automatically stored in Amazon S3    |
| Log retention            | 14 days in Amazon S3 (automatic)                            | Depends on your logging configuration                            |
| Real-time monitoring     | Limited<br>• logs available only after game session ends    | Available with Amazon CloudWatch Logs integration                |
| Setup complexity         | Automatic<br>• no additional configuration required         | Requires explicit logging configuration                          |

## Managed EC2 fleet logging

For managed EC2 fleets, Amazon GameLift Servers provides automatic log management:

- **Automatic upload:** Server logs are automatically uploaded to Amazon S3 when a game session ends
- **GetGameSessionLogUrl API:** Use this API to retrieve a pre-signed URL for downloading logs from Amazon S3
- **14-day retention:** Logs are retained in Amazon S3 for 14 days before automatic deletion
- **Size limits:** Log files have size limits per game session (see [Amazon GameLift Servers endpoints and quotas](../../../general/latest/gr/gamelift.md "../../../general/latest/gr/gamelift.md"))

For more information, see [Logging server messages (custom
servers)](logging-server-messages-custom.md "logging-server-messages-custom.md") and the [GetGameSessionLogUrl API reference](../apireference/API_GetGameSessionLogUrl.md "../apireference/API_GetGameSessionLogUrl.md").

## Container fleet logging

Container fleets require you to configure logging explicitly:

- **No automatic Amazon S3 upload:** Logs are not automatically uploaded to Amazon S3
- **GetGameSessionLogUrl not available:** This API does not work with container fleets
- **Amazon CloudWatch Logs integration:** Configure your container to send logs to Amazon CloudWatch Logs for centralized logging
- **Custom logging solutions:** Implement your own logging infrastructure using log drivers or sidecar containers
- **Real-time access:** With proper configuration, logs can be accessed in real-time during game sessions

For detailed container logging options, see [How container fleets work](containers-howitworks.md "containers-howitworks.md").

## Migration considerations

When migrating from managed EC2 to container fleets, consider these logging changes:

- **Update log retrieval code:** Replace GetGameSessionLogUrl API calls with Amazon CloudWatch Logs queries or your custom logging solution
- **Configure log retention:** Set up appropriate retention policies in Amazon CloudWatch Logs or your logging system
- **Implement real-time monitoring:** Take advantage of real-time log access for better observability
- **Review log volume and costs:** Amazon CloudWatch Logs pricing differs from the included Amazon S3 storage in managed EC2 fleets

## Recommended container logging setup

For container fleets, we recommend:

1. **Amazon CloudWatch Logs integration:** Configure your container definition to use the `awslogs` log driver
2. **Structured logging:** Use structured log formats (JSON) for better searchability and analysis
3. **Log levels:** Implement appropriate log levels to control verbosity and costs
4. **Retention policies:** Set retention periods based on your compliance and debugging needs
