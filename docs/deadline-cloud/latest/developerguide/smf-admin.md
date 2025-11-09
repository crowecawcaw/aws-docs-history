# Run scripts as an administrator to configure workers

Custom fleet host configuration scripts allow you to perform administrative tasks, such as
software installation, on your service-managed fleet workers. These scripts run with elevated
privileges, giving you the flexibility to configure your workers for your system.

Deadline Cloud runs the script after the worker enters the `STARTING` state and before
it runs any tasks.

###### Important

The script runs with elevated permissions, `sudo` on Linux systems and
'Administrator' on Windows systems. It is your responsibility to ensure that the script
does not introduce any security issues.

When you use an admin script you are responsible for monitoring the health of your
fleet.

Common uses for the script include:

- Installing software that requires administrator access
- Installing Docker containers
  You can create and update a host configuration script using the console or using the
  AWS CLI.

Console

1. On the **Fleet details** page, choose the
   **Configurations** tab.
2. In the **Script** field, enter the script to run with elevated
   permissions. You can choose **Import** to load a script from your
   workstation.
3. Set a timeout period in seconds for running the script. The default is 300
   seconds (5 minutes).
4. Choose **Save changes** to save the script.

Create with CLI
Use the following AWS CLI command to create a fleet with a host configuration script.
Replace the `placeholder` text with your information.

```
aws deadline-internal create-fleet \
--farm-id `farm-12345` \
--display-name "`fleet-name`" \
--max-worker-count 1 \
--configuration '{
  "serviceManagedEc2": {
    "instanceCapabilities": {
      "vCpuCount": {"min": 2},
      "memoryMiB": {"min": 4096},
      "osFamily": "linux",
      "cpuArchitectureType": "x86_64"
    },
    "instanceMarketOptions": {"type":"spot"}
  }
}' \
--role-arn arn:aws:iam::`111122223333`:role/`role-name` \
--host-configuration '{ "scriptBody": "`script body`", "scriptTimeoutSeconds": `timeout value`}'
```

Update with CLI
Use the following AWS CLI command to update a fleet's host configuration script.
Replace the `placeholder` text with your information.

```
aws deadline update-fleet \
--farm-id `farm-12345` \
--fleet-id `fleet-455678` \
--host-configuration '{ "scriptBody": "`script body`", "scriptTimeoutSeconds": `timeout value`}'
```

The following scripts demonstrate:

- The environment variables available to the script
- That AWS credentials are working in the shell
- That the script is running in an elevated shell

Linux
Use the following script to show that a script is running with `root`
privileges:

```
# Print environment variables
set
# Check AWS Credentials
aws sts get-caller-identity
```

Windows
Use the following PowerShell script to show that a script is running
with Administrator privileges:

```
Get-ChildItem env: | ForEach-Object { "$($_.Name)=$($_.Value)" }
aws sts get-caller-identity
function Test-AdminPrivileges {
    $currentUser = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
    $isAdmin = $currentUser.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

    return $isAdmin
}

if (Test-AdminPrivileges) {
    Write-Host "The current PowerShell session is elevated (running as Administrator)."
} else {
    Write-Host "The current PowerShell session is not elevated (not running as Administrator)."
}
exit 0
```

## Troubleshooting host configuration scripts

When you run the host configuration script:

- On success: The worker runs the job
- On failure (non-zero exit code or crash):

      + The worker shuts down

  The fleet automatically launches a new worker using the latest host configuration
  script

To monitor the script:

1. Open the fleet page in the Deadline Cloud console.
2. Choose **View workers** to open the Deadline Cloud monitor.
3. View the worker status in the monitor page.

Important notes:

- Workers that shut down due to an error are not available in the list of workers in
  the monitor. Use CloudWatch Logs to view the worker logs in the following log group:

```
/aws/deadline/farm-`XXXXX`/fleet-`YYYYY`
```

Within that log group is a stream of

```
worker-`ZZZZZ`
```

- CloudWatch Logs retains worker logs according to your configured retention period.

### Monitoring host configuration script execution

With Admin scripts to configure workers, you can take full control of a Deadline Cloud worker. You can install any software package, reconfigure operating system parameters, or mount shared file systems. With this advanced feature and Deadline Cloud's capability to scale to thousands of workers, you can now monitor when configuration scripts are executed successfully or failed. Failure causes may include script errors, flaky behavior, or other unknown situations.

We recommend the following solutions for monitoring host configuration script execution.

#### CloudWatch Logs monitoring

All fleet host configuration logs are streamed to the fleet's CloudWatch log group, and specifically to a worker's CloudWatch log stream. For example, `/aws/deadline/farm-123456789012/fleet-777788889999` is the log group for farm `123456789012`, fleet `777788889999`.

Each worker provisions a dedicated log stream, for example `worker-123456789012`. Host configuration logs include log banners such as _Running Host Configuration Script_ and _Finished running Host Configuration Script, exit code: 0_. The exit code of the script is included in the finished banner and can be queried using CloudWatch tools.

#### CloudWatch Logs Insights

CloudWatch Logs Insights offers advanced capabilities to analyze log information. For example, the following Log Insights query parses for the host configuration exit code, sorted by time:

```
fields @timestamp, @message, @logStream, @log
| filter @message like /Finished running Host Configuration Script/
| parse @message /exit code: (?<exit_code>\d+)/
| display @timestamp, exit_code
| sort @timestamp desc
```

For more information about CloudWatch Logs Insights, see [Analyzing log data with CloudWatch Logs Insights](../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax.md "../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax.md") in the _Amazon CloudWatch Logs User Guide_.

##### Worker agent structured logging

Deadline Cloud's worker agent publishes structured JSON logs to CloudWatch. The worker agent offers a wide array of structured logs for analyzing worker health. For more information, see [Deadline Cloud worker agent logging](https://github.com/aws-deadline/deadline-cloud-worker-agent/blob/mainline/docs/logging.md "https://github.com/aws-deadline/deadline-cloud-worker-agent/blob/mainline/docs/logging.md") on GitHub.

The attributes of the structured logs are unpacked to fields in Log Insights. You can use this CloudWatch capability to count and analyze host configuration startup failures. For example, a count and bin query can be used to determine how often failures occur:

```
fields @timestamp, @message, @logStream, @log
| sort @timestamp desc
| filter message like /Worker Agent host configuration failed with exit code/
| stats count(*) by exit_code, bin(1h)
```

#### CloudWatch metric filters for metrics and alarming

You can set up CloudWatch metric filters to generate CloudWatch metrics from logs. This lets you create alarms and dashboards for monitoring host configuration script execution.

###### To create a metric filter

1. Open the CloudWatch console.
2. In the navigation pane, choose **Logs**, then **Log groups**.
3. Select your fleet's log group.
4. Choose **Create metric filter**.
5. Define your filter pattern using one of the following:
   - **For success metrics:**

   ```
   {$.message = "*Worker Agent host configuration succeeded.*"}
   ```

   - **For failure metrics:**

   ```
   {$.exit_code != 0 && $.message = "*Worker Agent host configuration failed with exit code*"}
   ```

6. Choose **Next** to create a metric with the following values:
   - **Metric namespace:** Your metric namespace (for example, `MyDeadlineFarm`)
   - **Metric name:** Your requested metric name (for example, `host_config_failure`)
   - **Metric value:** `1` (each instance is a count of 1)
   - **Default value:** Leave empty
   - **Unit:** `Count`

After creating metric filters, you can configure standard CloudWatch alarms to take action on elevated host configuration failure rates, or add the metrics to a CloudWatch dashboard for day-to-day operations and monitoring.

For more details, see [Filter and pattern syntax](../../../AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.md "../../../AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.md") in the _Amazon CloudWatch Logs User Guide_.
