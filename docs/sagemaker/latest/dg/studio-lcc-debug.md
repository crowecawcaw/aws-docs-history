# Debug Lifecycle Configurations in Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

The following topics show how to get information about and debug your lifecycle
configurations.

###### Topics

- [Verify lifecycle configuration process from
  CloudWatch Logs](#studio-lcc-debug-logs "#studio-lcc-debug-logs")
- [JupyterServer app failure](#studio-lcc-debug-jupyterserver "#studio-lcc-debug-jupyterserver")
- [KernelGateway app failure](#studio-lcc-debug-kernel "#studio-lcc-debug-kernel")
- [Lifecycle configuration timeout](#studio-lcc-debug-timeout "#studio-lcc-debug-timeout")

## Verify lifecycle configuration process from

CloudWatch Logs

Lifecycle configurations only log `STDOUT` and `STDERR`.

`STDOUT` is the default output for bash scripts. You can write to
`STDERR` by appending `>&2` to the end of a bash command.
For example, `echo 'hello'>&2`.

Logs for your lifecycle configurations are published to your AWS account using
Amazon CloudWatch. These logs can be found in the `/aws/sagemaker/studio` log stream
in the CloudWatch console.

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Logs** from the left side. From the dropdown menu, select **Log
   groups**.
3. On the **Log groups** page, search for `aws/sagemaker/studio`.
4. Select the log group.
5. On the **Log group details** page, choose the **Log
   streams** tab.
6. To find the logs for a specific app, search the log streams using the following format:

```
`domain-id`/`space-name`/`app-type`/default/LifecycleConfigOnStart
```

For example, to find the lifecycle configuration logs for domain
`d-m85lcu8vbqmz`, space name `i-sonic-js`, and
application type `JupyterLab`, use the following search string:

```
d-m85lcu8vbqmz/i-sonic-js/JupyterLab/default/LifecycleConfigOnStart
```

## JupyterServer app failure

If your JupyterServer app crashes because of an issue with the attached lifecycle
configuration, Studio Classic displays the following error message on the Studio Classic startup
screen.

```
Failed to create SageMaker Studio due to start-up script failure
```

Select the `View script logs` link to view the CloudWatch logs for your
JupyterServer app.

In the case where the faulty lifecycle configuration is specified in the
`DefaultResourceSpec` of your domain, user profile, or shared space,
Studio Classic continues to use the lifecycle configuration even after restarting
Studio Classic.

To resolve this error, follow the steps in [Set Default Lifecycle Configurations for Amazon SageMaker Studio Classic](studio-lcc-defaults.md "studio-lcc-defaults.md") to remove the lifecycle configuration script
from the `DefaultResourceSpec` or select another script as the default. Then
launch a new JupyterServer app.

## KernelGateway app failure

If your KernelGateway app crashes because of an issue with the attached lifecycle
configuration, Studio Classic displays the error message in your Studio Classic Notebook.

Choose `View script logs` to view the CloudWatch logs for your KernelGateway
app.

In this case, your lifecycle configuration is specified in the Studio Classic Launcher
when launching a new Studio Classic Notebook.

To resolve this error, use the Studio Classic launcher to select a different lifecycle
configuration or select `No script`.

###### Note

A default KernelGateway lifecycle configuration specified in `DefaultResourceSpec`
applies to all KernelGateway images in the domain, user profile, or shared space
unless the user selects a different script from the list presented in the Studio Classic
launcher. The default script also runs if `No Script` is selected by the
user. For more information on selecting a script, see [Step 3: Launch an application with the
lifecycle configuration](studio-lcc-create-console.md#studio-lcc-create-console-step3 "studio-lcc-create-console.md#studio-lcc-create-console-step3").

## Lifecycle configuration timeout

There is a lifecycle configuration timeout limitation of 5 minutes. If a lifecycle
configuration script takes longer than 5 minutes to run, Studio Classic throws an
error.

To resolve this error, ensure that your lifecycle configuration script completes in
less than 5 minutes.

To help decrease the run time of scripts, try the following:

- Cut down on necessary steps. For example, limit which conda environments to install large packages in.
- Run tasks in parallel processes.
- Use the `nohup` command in your script to ensure that hangup
  signals are ignored and do not stop the execution of the script.
