

# Run host configuration scripts with administrator privileges
<a name="smf-admin"></a>

Host configuration scripts allow you to perform administrative tasks, such as software installation, on your service-managed fleet workers. These scripts run with elevated privileges (`sudo` on Linux, Administrator on Windows), giving you the flexibility to configure your workers for your system.

Deadline Cloud runs the script after the worker enters the `STARTING` state and before it runs any tasks.

The script runs after Deadline Cloud sets up usage-based licensing (UBL). Deadline Cloud sets the UBL license environment variables when the worker instance launches, before the worker agent starts, and the worker agent then runs your host configuration script. The automatic UBL setup doesn't overwrite environment variables that your script sets: license variables that your script sets system-wide take precedence for the jobs that the worker runs. For more information about licensing options, see [Using software licenses with Deadline Cloud](license.md).

**Important**  
The script runs with elevated permissions. It is your responsibility to ensure that the script does not introduce any security issues.  
When you use a host configuration script you are responsible for monitoring the health of your fleet.

Common uses for host configuration scripts include:
+ Installing software that requires administrator access
+ Installing Docker containers
+ Installing third-party cloud storage solutions such as LucidLink. For a walkthrough, see [Set up LucidLink with service managed fleet scripts for Deadline Cloud](https://aws.amazon.com/blogs/media/set-up-lucidlink-with-service-managed-fleet-scripts-for-aws-deadline-cloud/) on the AWS for M&E Blog.

You can create and update a host configuration script using the console or using the AWS CLI.

------
#### [ Console ]

1. On the **Fleet details** page, choose the **Configurations** tab.

1. In the **Script** field, enter the script to run with elevated permissions. You can choose **Import** to load a script from your workstation.

1. Set a timeout period in seconds for running the script. The default is 300 seconds (5 minutes).

1. Choose **Save changes** to save the script.

------
#### [ Create with CLI ]

Use the following AWS CLI command to create a fleet with a host configuration script. Replace the {{placeholder}} text with your information.

```
aws deadline create-fleet \
--farm-id {{farm-12345}} \
--display-name "{{fleet-name}}" \
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
--role-arn arn:aws:iam::{{111122223333}}:role/{{role-name}} \
--host-configuration '{ "scriptBody": "{{script body}}", "scriptTimeoutSeconds": {{timeout value}}}'
```

------
#### [ Update with CLI ]

Use the following AWS CLI command to update a fleet's host configuration script. Replace the {{placeholder}} text with your information.

```
aws deadline update-fleet \
--farm-id {{farm-12345}} \
--fleet-id {{fleet-455678}} \
--host-configuration '{ "scriptBody": "{{script body}}", "scriptTimeoutSeconds": {{timeout value}}}'
```

------

The following scripts demonstrate:
+ The environment variables available to the script
+ That AWS credentials are working in the shell
+ That the script is running in an elevated shell

------
#### [ Linux ]

Use the following script to show that a script is running with `root` privileges:

```
# Print environment variables
set 
# Check AWS Credentials
aws sts get-caller-identity
```

------
#### [ Windows ]

Use the following PowerShell script to show that a script is running with Administrator privileges:

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

------

## Troubleshoot host configuration scripts
<a name="smf-admin-troubleshooting"></a>

When you run the host configuration script: 
+ On success: The worker runs the job
+ On failure (non-zero exit code or crash): 
  + The worker shuts down

  The fleet automatically launches a new worker using the latest host configuration script

To monitor the script:

1. Open the fleet page in the Deadline Cloud console.

1. Choose **View workers** to open the Deadline Cloud monitor.

1. View the worker status in the monitor page.

**Tip**  
When testing host configuration scripts, set the fleet's maximum worker count to 1 to avoid starting multiple workers while iterating on the script.

Important notes:
+ Workers that shut down due to an error are not available in the list of workers in the monitor. Use CloudWatch Logs to view the worker logs in the following log group:

  ```
  /aws/deadline/farm-{{XXXXX}}/fleet-{{YYYYY}}
  ```

  Within that log group, look for a stream named `worker-{{ZZZZZ}}`.
+ CloudWatch Logs retains worker logs according to your configured retention period.

### Monitor host configuration script execution
<a name="smf-admin-monitoring"></a>

With host configuration scripts, you can take full control of a Deadline Cloud worker. You can install any software package, reconfigure operating system parameters, or mount shared file systems. With this advanced feature and Deadline Cloud's capability to scale to thousands of workers, you can monitor when configuration scripts are executed successfully or failed.

We recommend the following solutions for monitoring host configuration script execution.

#### CloudWatch Logs monitoring
<a name="smf-admin-cloudwatch-logs"></a>

All fleet host configuration logs are streamed to the fleet's CloudWatch log group, and specifically to a worker's CloudWatch log stream. For example, `/aws/deadline/farm-123456789012/fleet-777788889999` is the log group for farm `123456789012`, fleet `777788889999`.

Each worker provisions a dedicated log stream, for example `worker-123456789012`. Host configuration logs include log banners such as *Running Host Configuration Script* and *Finished running Host Configuration Script, exit code: 0*. The exit code of the script is included in the finished banner and can be queried using CloudWatch tools.

#### CloudWatch Logs Insights
<a name="smf-admin-log-insights"></a>

CloudWatch Logs Insights offers advanced capabilities to analyze log information. For example, the following Log Insights query parses for the host configuration exit code, sorted by time:

```
fields @timestamp, @message, @logStream, @log
| filter @message like /Finished running Host Configuration Script/
| parse @message /exit code: (?<exit_code>\d+)/
| display @timestamp, exit_code
| sort @timestamp desc
```

For more information about CloudWatch Logs Insights, see [Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html) in the *Amazon CloudWatch Logs User Guide*.

##### Worker agent structured logging
<a name="smf-admin-structured-logging"></a>

The Deadline Cloud worker agent publishes structured JSON logs to CloudWatch. The worker agent offers many structured logs for analyzing worker health. For more information, see [Deadline Cloud worker agent logging](https://github.com/aws-deadline/deadline-cloud-worker-agent/blob/mainline/docs/logging.md) on the GitHub website.

The attributes of the structured logs are unpacked to fields in Log Insights. You can use this CloudWatch capability to count and analyze host configuration startup failures. For example, a count and bin query can be used to determine how often failures occur:

```
fields @timestamp, @message, @logStream, @log
| sort @timestamp desc
| filter message like /Worker Agent host configuration failed with exit code/
| stats count(*) by exit_code, bin(1h)
```

#### CloudWatch metric filters for metrics and alarming
<a name="smf-admin-metric-filters"></a>

You can set up CloudWatch metric filters to generate CloudWatch metrics from logs. Metric filters let you create alarms and dashboards for monitoring host configuration script execution.

**To create a metric filter**

1. Open the CloudWatch console.

1. In the navigation pane, choose **Logs**, then **Log groups**.

1. Select your fleet's log group.

1. Choose **Create metric filter**.

1. Define your filter pattern using one of the following:
   + **For success metrics:**

     ```
     {$.message = "*Worker Agent host configuration succeeded.*"}
     ```
   + **For failure metrics:**

     ```
     {$.exit_code != 0 && $.message = "*Worker Agent host configuration failed with exit code*"}
     ```

1. Choose **Next** to create a metric with the following values:
   + **Metric namespace:** Your metric namespace (for example, **MyDeadlineFarm**)
   + **Metric name:** Your requested metric name (for example, **host\_config\_failure**)
   + **Metric value:** **1** (each instance is a count of 1)
   + **Default value:** Leave empty
   + **Unit:** **Count**

After creating metric filters, you can configure standard CloudWatch alarms to take action on elevated host configuration failure rates, or add the metrics to a CloudWatch dashboard for day-to-day operations and monitoring.

For more details, see [Filter and pattern syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html) in the *Amazon CloudWatch Logs User Guide*.