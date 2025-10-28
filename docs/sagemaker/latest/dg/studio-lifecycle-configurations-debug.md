# Debug lifecycle configurations

The following topics show how to get information about and debug your lifecycle
configurations.

###### Topics

- [Verify lifecycle
  configuration process from CloudWatch Logs](#studio-lifecycle-configurations-debug-logs "#studio-lifecycle-configurations-debug-logs")
- [Lifecycle
  configuration timeout](studio-lifecycle-configurations-debug-timeout.md "studio-lifecycle-configurations-debug-timeout.md")

## Verify lifecycle

configuration process from CloudWatch Logs

Lifecycle configurations only log `STDOUT` and
`STDERR`.

`STDOUT` is the default output for bash scripts. You can write to
`STDERR` by appending `>&2` to the end of a bash
command. For example, `echo 'hello'>&2`.

Logs for your lifecycle configurations are published to your AWS account using
Amazon CloudWatch. These logs can be found in the `/aws/sagemaker/studio` log
stream in the CloudWatch console.

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Logs** from the left navigation pane. From the
   dropdown menu, select **Log groups**.
3. On the **Log groups** page, search for
   `aws/sagemaker/studio`.
4. Select the log group.
5. On the **Log group details** page, choose the
   **Log streams** tab.
6. To find the logs for a specific space and app, search the log streams
   using the following format:

```
`domain-id`/`space-name`/`app-type`/default/LifecycleConfigOnStart
```

For example, to find the lifecycle configuration logs for domain ID
`d-m85lcu8vbqmz`, space name `i-sonic-js`, and
application type `JupyterLab`, use the following search
string:

```
d-m85lcu8vbqmz/i-sonic-js/JupyterLab/default/LifecycleConfigOnStart
```

7. To view the script execution logs, select the log stream appended with
   `LifecycleConfigOnStart`.
