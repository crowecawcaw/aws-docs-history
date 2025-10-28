# Viewing IAM role requests for Amazon ECS tasks

When you use a provider for your task credentials in an IAM role, the provider requests saved in an audit log. The audit log inherits the same log
rotation settings as the container agent log. The `ECS_LOG_ROLLOVER_TYPE`,
`ECS_LOG_MAX_FILE_SIZE_MB`, and `ECS_LOG_MAX_ROLL_COUNT`
container agent configuration variables can be set to affect the behavior of the audit
log. For more information, see [Amazon ECS container agent log configuration parameters](ecs-agent-versions.md#agent-logs "ecs-agent-versions.md#agent-logs").

For container agent version 1.36.0 and later, the audit log is located at
`/var/log/ecs/audit.log`. When the log is rotated, a timestamp in
``YYYY`-`MM`-`DD`-`HH``
format is added to the end of the log file name.

For container agent version 1.35.0 and earlier, the audit log is located at
`/var/log/ecs/audit.log.`YYYY`-`MM`-`DD`-`HH``.

The log entry format is as follows:

- Timestamp
- HTTP response code
- IP address and port number of request origin
- Relative URI of the credential provider
- The user agent that made the request
- The ARN of the task to which the requesting container belongs
- The `GetCredentials` API name and version number
- The name of the Amazon ECS cluster to which the container instance is
  registered
- The container instance ARN
  You can use the following command to view the log files.

```
`cat /var/log/ecs/audit.log.`2016-07-13-16``
```

Output:

```
2016-07-13T16:11:53Z 200 172.17.0.5:52444 "/v1/credentials" "python-requests/2.7.0 CPython/2.7.6 Linux/4.4.14-24.50.amzn1.x86_64" `TASK_ARN` GetCredentials 1 `CLUSTER_NAME` `CONTAINER_INSTANCE_ARN`
```
