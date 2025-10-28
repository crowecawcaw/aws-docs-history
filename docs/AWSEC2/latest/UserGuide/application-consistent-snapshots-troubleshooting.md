# Troubleshoot

Windows VSS based EBS snapshots

Before you try any other troubleshooting steps, we recommend that you verify the
following details.

- Ensure that you've met all [Prerequisites to create Windows VSS
  based EBS snapshots](application-consistent-snapshots-prereqs.md "application-consistent-snapshots-prereqs.md").
- Verify that you're using the latest [Windows OS version support](vss-comps-history.md#windows-version-support "vss-comps-history.md#windows-version-support") of the
  `AwsVssComponents` package for your operating system. The issue
  that you've observed might have been addressed in newer versions.

###### Topics

- [Check log files](#general-log-files "#general-log-files")
- [Collect additional diagnostic logs](#vss-ts-collect-diagnostic-logs "#vss-ts-collect-diagnostic-logs")
- [Use VSS on instances with proxy configured](#general-using-vss-with-proxy "#general-using-vss-with-proxy")
- [Error: Thaw pipe connection timed out, error on thaw,
  timeout waiting for VSS Freeze, or other timeout errors](#error-thaw "#error-thaw")
- [Error: Cannot invoke method. Method invocation is supported only on core
  types in this language mode](#error-invoke "#error-invoke")

## Check log files

If you experience problems or receive error messages when you create VSS based
EBS snapshots, you can view the command output in the Systems Manager console.

For Systems Manager documents that create VSS snapshots, you can set the `CollectDiagnosticLogs`
parameter to "`True`" at runtime. When the `CollectDiagnosticLogs`
parameter is set to "`True`", VSS collects additional logs to aid in debugging.
For more information, see [Collect additional diagnostic logs](#vss-ts-collect-diagnostic-logs "#vss-ts-collect-diagnostic-logs").

If you collect diagnostic logs, the Systems Manager document stores them on your instance at the
following location: `C:\ProgramData\Amazon\AwsVss\Logs\`timestamp`.zip`. The
default for the `CollectDiagnosticLogs` parameter is "`False`".

###### Note

For additional debugging help, you can send the `.zip` file to Support.

The following additional logs are available, whether you collect diagnostic logs
or not:

- `%ProgramData%\Amazon\SSM\InstanceData\`InstanceID`\document\orchestration\`SSMCommandID`\awsrunPowerShellScript\runPowerShellScript\stdout`
- `%ProgramData%\Amazon\SSM\InstanceData\`InstanceID`\document\orchestration\`SSMCommandID`\awsrunPowerShellScript\runPowerShellScript\stderr`

You can also open the Event Viewer Windows application and choose
**Windows Logs**, **Application** to view
additional logs. To see events specifically from the EC2 Windows VSS Provider and
the Volume Shadow Copy Service, filter by **Source** on the terms
`Ec2VssSoftwareProvider` and
`VSS`.

If you're using Systems Manager with VPC endpoints, and the Systems Manager [send-command](../../../cli/latest/reference/ssm/send-command.md "../../../cli/latest/reference/ssm/send-command.md")
API action (**Run Command** in the console) failed, verify that you configured
the following endpoint correctly:
**com.amazonaws.`region`.ec2**.

Without the Amazon EC2 endpoint defined, the call to enumerate attached EBS volumes fails,
which causes the Systems Manager command to fail. For more information about setting up VPC endpoints
with Systems Manager, see [Create a Virtual Private Cloud
Endpoint](../../../systems-manager/latest/userguide/setup-create-vpc.md "../../../systems-manager/latest/userguide/setup-create-vpc.md") in the _AWS Systems Manager User Guide_.

## Collect additional diagnostic logs

To collect additional diagnostic logs when you use the Systems Manager send command to run the
VSS snapshot document, set the `CollectDiagnosticLogs` input parameter to
"`True`" at runtime. We recommend that you set this parameter to "`True`"
when you troubleshoot.

To see a command line example, select one of the following tabs.

AWS CLI
The following example runs the `AWSEC2-CreateVssSnapshot` Systems Manager document
in the AWS CLI:

```
aws ssm send-command \
    --document-name "`AWSEC2-CreateVssSnapshot`" \
    --instance-ids "`i-1234567890abcdef0`" \
    --parameters '{"description":["`Example - create diagnostic logs at runtime.`"],"tags":["Key=`tag_name`,Value=`tag_value`"],"CollectDiagnosticLogs":["True"]}'
```

PowerShell
The following example runs the `AWSEC2-CreateVssSnapshot` Systems Manager document
in PowerShell:

```
Send-SSMCommand `
    -DocumentName "`AWSEC2-CreateVssSnapshot`" `
    -InstanceId "`i-1234567890abcdef0`" `
    -Parameter @{'description'='`Example - create diagnostic logs at runtime.`';'tags'='Key=`tag_name`,Value=`tag_value`';'CollectDiagnosticLogs'='True'}
```

## Use VSS on instances with proxy configured

If you experience problems when creating VSS based EBS snapshots on
instances that use a proxy to reach EC2 endpoints, verify the following settings
on your instance:

- Verify that the proxy is configured so that the EC2 service endpoints in the
  instance’s Region and IMDS are reachable by AWS Tools for Windows PowerShell running as
  SYSTEM.
- To support using the system configured WinHTTP proxy, make sure that
  you've installed the latest `AwsVssComponents` version on your
  instance. For more information about configuring WinHTTP proxy, see [Netsh Commands for Windows Hypertext Transfer Protocol
  (WINHTTP)](<https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc731131(v=ws.10)> "https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc731131(v=ws.10)") on the Microsoft website.

## Error: Thaw pipe connection timed out, error on thaw,

timeout waiting for VSS Freeze, or other timeout errors

The EC2 Windows VSS Provider might time out due to activity or services on the
instance preventing VSS based snapshots from proceeding in a timely manner.
The Windows VSS Framework provides a non-configurable 10-second window during
which communication to the file system is paused. During this time,
`AWSEC2-CreateVssSnapshot` snapshots your volumes.

The following issues can cause the EC2 Windows VSS Provider to run into time limits
during a snapshot:

- Excessive I/O to a volume
- Slow responsiveness of the EC2 API on the instance
- Fragmented volumes
- Incompatibility with some antivirus software
- Issues with a VSS Application writer
- When Module Logging is enabled for a large number of PowerShell modules,
  that can cause PowerShell scripts to run slowly

Most timeout issues that occur when you run the `AWSEC2-CreateVssSnapshot`
command document are related to the workload on the instance being too high at the time
of the backup. The following actions can help you take a successful snapshot:

- Retry the `AWSEC2-CreateVssSnapshot` command to see if the
  snapshot attempt is successful. If retrying succeeds in some cases, reducing
  the instance load might make snapshots more successful.
- Wait a while for the workload on the instance to decrease, and retry the
  `AWSEC2-CreateVssSnapshot` command. Alternatively, you can
  attempt snapshots when the instance is known to be under low stress.
- Attempt VSS snapshots when the antivirus software on the system is turned
  off. If this resolves the issue, refer to the antivirus software instructions
  and configure it to allow VSS snapshots.
- If there is a high volume of Amazon EC2 API calls in your account within the same
  Region where you're running a snapshot, API throttling might delay snapshot
  operations. To reduce throttling impact, use the latest `AwsVssComponents`
  package. This package utilizes the EC2 `CreateSnapshots` API action to
  reduce the number of mutating actions like per-volume snapshot creation and tagging.
- If you have multiple `AWSEC2-CreateVssSnapshot` command scripts
  running at the same time, you can take the following steps to reduce concurrency
  issues.
  - Consider scheduling snapshots during periods of lower API activity.
  - If you use **Run Command** in the Systems Manager console (or
    **SendCommand** in the API) to run the command script, you
    can use Systems Manager rate controls to reduce concurrency.

  You can also use Systems Manager rate controls to reduce concurrency for services
  like AWS Backup that use Systems Manager to run the command script.

- Run the command `vssadmin list writers` in a shell and see if
  it reports any errors in the **Last error** field for any
  writers on the system. If any writers report a **time out**
  error, consider retrying snapshots when the instance is under less
  load.
- When you use smaller instance types like `t2 | t3 | t3a`.nano
  or `t2 | t3 | t3a`.micro, timeouts due to memory and CPU
  constraints can occur. The following actions might help reduce timeout issues.
  - Try closing memory or CPU intensive applications before taking snapshots.
  - Try taking snapshots during periods of lower instance activity.

## Error: Cannot invoke method. Method invocation is supported only on core

types in this language mode

You will encounter this error when the PowerShell language
mode is not set to `FullLanguage`. The `AWSEC2-CreateVssSnapshot`
SSM document requires PowerShell to be configured to `FullLanguage` mode.

To verify the language mode, run the following command on the instance in a
PowerShell console:

```
$ExecutionContext.SessionState.LanguageMode
```

For more information about language modes, see [about_Language_Modes](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_language_modes "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_language_modes") in the Microsoft documentation.
