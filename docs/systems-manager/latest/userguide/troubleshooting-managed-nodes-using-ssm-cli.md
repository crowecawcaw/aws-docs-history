• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Troubleshooting

managed node availability using `ssm-cli`

The `ssm-cli` is a standalone command line tool included in the SSM Agent
installation. When you install SSM Agent 3.1.501.0 or later on a machine, you can run
`ssm-cli` commands on that machine. The output of those commands
helps you determine whether the machine meets the minimum requirements for an Amazon EC2
instance or non-EC2 machine to be managed by AWS Systems Manager, and therefore added to lists
of managed nodes in Systems Manager. (SSM Agent version 3.1.501.0 was released in November,
2021.)

###### Minimum requirements

For an Amazon EC2 instance or non-EC2 machine to be managed by AWS Systems Manager, and
available in lists of managed nodes, it must meet three primary
requirements:

- SSM Agent must be installed and running on a machine with a [supported operating
  system](operating-systems-and-machine-types.md#prereqs-operating-systems "operating-systems-and-machine-types.md#prereqs-operating-systems").

Some AWS managed Amazon Machine Images (AMIs) for EC2 are configured to
launch instances with [SSM Agent](ssm-agent.md "ssm-agent.md")
preinstalled. (You can also configure a custom AMI to preinstall
SSM Agent.) For more information, see [Find AMIs with the SSM Agent
preinstalled](ami-preinstalled-agent.md "ami-preinstalled-agent.md").

- An AWS Identity and Access Management (IAM) instance profile (for EC2 instances) or IAM service
  role (for non-EC2 machines) that supplies the required permissions to
  communicate with the Systems Manager service must be attached to the machine.
- SSM Agent must be able to connect to a Systems Manager endpoint to register itself
  with the service. Thereafter, the managed node must be available to the
  service, which is confirmed by the service sending a signal every five
  minutes to check the managed node's health.

###### Preconfigured commands in `ssm-cli`

Preconfigured commands are included that gather the required information to
help you diagnose why a machine that you have confirmed is running isn't
included in your lists of managed nodes in Systems Manager. These commands are run when
you specify the `get-diagnostics` option.

On the machine, run the following command to use `ssm-cli` to help you
troubleshoot managed node availability.

Linux & macOS

```
ssm-cli get-diagnostics --output table
```

Windows
On Windows Server machines, you must navigate to the `C:\Program
 Files\Amazon\SSM` directory before running the
command.

```
ssm-cli.exe get-diagnostics --output table
```

PowerShell
On Windows Server machines, you must navigate to the `C:\Program
 Files\Amazon\SSM` directory before running the
command.

```
.\ssm-cli.exe get-diagnostics --output table
```

The command returns output as a table similar to the following.

###### Note

Connectivity checks to the `ssmmessages`, `s3`,
`kms`, `logs`, and `monitoring` endpoints
are for additional optional features such as Session Manager that can log to Amazon Simple Storage Service
(Amazon S3) or Amazon CloudWatch Logs, and use AWS Key Management Service (AWS KMS) encryption.

Linux & macOS

```
[root@instance]# ssm-cli get-diagnostics --output table
┌───────────────────────────────────────┬─────────┬───────────────────────────────────────────────────────────────────────┐
│ Check                                 │ Status  │ Note                                                                  │
├───────────────────────────────────────┼─────────┼───────────────────────────────────────────────────────────────────────┤
│ EC2 IMDS                              │ Success │ IMDS is accessible and has instance id i-0123456789abcdefa in Region  │
│                                       │         │ us-east-2                                                             │
├───────────────────────────────────────┼─────────┼───────────────────────────────────────────────────────────────────────┤
│ Hybrid instance registration          │ Skipped │ Instance does not have hybrid registration                            │
├───────────────────────────────────────┼─────────┼───────────────────────────────────────────────────────────────────────┤
│ Connectivity to ssm endpoint          │ Success │ ssm.us-east-2.amazonaws.com is reachable                              │
├───────────────────────────────────────┼─────────┼───────────────────────────────────────────────────────────────────────┤
│ Connectivity to ec2messages endpoint  │ Success │ ec2messages.us-east-2.amazonaws.com is reachable                      │
├───────────────────────────────────────┼─────────┼───────────────────────────────────────────────────────────────────────┤
│ Connectivity to ssmmessages endpoint  │ Success │ ssmmessages.us-east-2.amazonaws.com is reachable                      │
├───────────────────────────────────────┼─────────┼───────────────────────────────────────────────────────────────────────┤
│ Connectivity to s3 endpoint           │ Success │ s3.us-east-2.amazonaws.com is reachable                               │
├───────────────────────────────────────┼─────────┼───────────────────────────────────────────────────────────────────────┤
│ Connectivity to kms endpoint          │ Success │ kms.us-east-2.amazonaws.com is reachable                              │
├───────────────────────────────────────┼─────────┼───────────────────────────────────────────────────────────────────────┤
│ Connectivity to logs endpoint         │ Success │ logs.us-east-2.amazonaws.com is reachable                             │
├───────────────────────────────────────┼─────────┼───────────────────────────────────────────────────────────────────────┤
│ Connectivity to monitoring endpoint   │ Success │ monitoring.us-east-2.amazonaws.com is reachable                       │
├───────────────────────────────────────┼─────────┼───────────────────────────────────────────────────────────────────────┤
│ AWS Credentials                       │ Success │ Credentials are for                                                   │
│                                       │         │ arn:aws:sts::123456789012:assumed-role/Fullaccess/i-0123456789abcdefa │
│                                       │         │ and will expire at 2021-08-17 18:47:49 +0000 UTC                      │
├───────────────────────────────────────┼─────────┼───────────────────────────────────────────────────────────────────────┤
│ Agent service                         │ Success │ Agent service is running and is running as expected user              │
├───────────────────────────────────────┼─────────┼───────────────────────────────────────────────────────────────────────┤
│ Proxy configuration                   │ Skipped │ No proxy configuration detected                                       │
├───────────────────────────────────────┼─────────┼───────────────────────────────────────────────────────────────────────┤
│ SSM Agent version                     │ Success │ SSM Agent version is 3.0.1209.0, latest available agent version is    │
│                                       │         │ 3.1.192.0                                                             │
└───────────────────────────────────────┴─────────┴───────────────────────────────────────────────────────────────────────┘

```

Windows Server and PowerShell

```
PS C:\Program Files\Amazon\SSM> .\ssm-cli.exe get-diagnostics --output table
┌───────────────────────────────────────┬─────────┬─────────────────────────────────────────────────────────────────────┐
│ Check                                 │ Status  │ Note                                                                │
├───────────────────────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
│ EC2 IMDS                              │ Success │ IMDS is accessible and has instance id i-0123456789EXAMPLE in       │
│                                       │         │ Region us-east-2                                                    │
├───────────────────────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
│ Hybrid instance registration          │ Skipped │ Instance does not have hybrid registration                          │
├───────────────────────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
│ Connectivity to ssm endpoint          │ Success │ ssm.us-east-2.amazonaws.com is reachable                            │
├───────────────────────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
│ Connectivity to ec2messages endpoint  │ Success │ ec2messages.us-east-2.amazonaws.com is reachable                    │
├───────────────────────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
│ Connectivity to ssmmessages endpoint  │ Success │ ssmmessages.us-east-2.amazonaws.com is reachable                    │
├───────────────────────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
│ Connectivity to s3 endpoint           │ Success │ s3.us-east-2.amazonaws.com is reachable                             │
├───────────────────────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
│ Connectivity to kms endpoint          │ Success │ kms.us-east-2.amazonaws.com is reachable                            │
├───────────────────────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
│ Connectivity to logs endpoint         │ Success │ logs.us-east-2.amazonaws.com is reachable                           │
├───────────────────────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
│ Connectivity to monitoring endpoint   │ Success │ monitoring.us-east-2.amazonaws.com is reachable                     │
├───────────────────────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
│ AWS Credentials                       │ Success │ Credentials are for                                                 │
│                                       │         │  arn:aws:sts::123456789012:assumed-role/SSM-Role/i-123abc45EXAMPLE  │
│                                       │         │  and will expire at 2021-09-02 13:24:42 +0000 UTC                   │
├───────────────────────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
│ Agent service                         │ Success │ Agent service is running and is running as expected user            │
├───────────────────────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
│ Proxy configuration                   │ Skipped │ No proxy configuration detected                                     │
├───────────────────────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
│ Windows sysprep image state           │ Success │ Windows image state value is at desired value IMAGE_STATE_COMPLETE  │
├───────────────────────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
│ SSM Agent version                     │ Success │ SSM Agent version is 3.2.815.0, latest agent version in us-east-2   │
│                                       │         │ is 3.2.985.0                                                        │
└───────────────────────────────────────┴─────────┴─────────────────────────────────────────────────────────────────────┘
```

The following table provides additional details for each of the checks performed
by `ssm-cli`.

| `ssm-cli` diagnostic checks            | Check                                                                                                                                                                                                                                                                                                                                                                                                                                         | Details |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| Amazon EC2 instance metadata service   | Indicates whether the managed node is able to reach the metadata<br>service. A failed test indicates a connectivity issue to<br>`http://169.254.169.254` which can be caused<br>by local route, proxy, or operating system (OS) firewall and proxy<br>configurations.                                                                                                                                                                         |
| Hybrid instance registration           | Indicates whether SSM Agent is registered using a hybrid<br>activation.                                                                                                                                                                                                                                                                                                                                                                       |
| Connectivity to `ssm` endpoint         | Indicates whether the node is able to reach the service endpoints<br>for Systems Manager on TCP port 443. A failed test indicates connectivity<br>issues to<br>`https://ssm.`region`.amazonaws.com`<br>depending on the AWS Region where the node is located.<br>Connectivity issues can be caused by the VPC configuration including<br>security groups, network access control lists, route tables, or OS<br>firewalls and proxies.         |
| Connectivity to `ec2messages` endpoint | Indicates whether the node is able to reach the service endpoints<br>for Systems Manager on TCP port 443. A failed test indicates connectivity<br>issues to<br>`https://ec2messages.`region`.amazonaws.com`<br>depending on the AWS Region where the node is located.<br>Connectivity issues can be caused by the VPC configuration including<br>security groups, network access control lists, route tables, or OS<br>firewalls and proxies. |
| Connectivity to `ssmmessages` endpoint | Indicates whether the node is able to reach the service endpoints<br>for Systems Manager on TCP port 443. A failed test indicates connectivity<br>issues to<br>`https://ssmmessages.`region`.amazonaws.com`<br>depending on the AWS Region where the node is located.<br>Connectivity issues can be caused by the VPC configuration including<br>security groups, network access control lists, route tables, or OS<br>firewalls and proxies. |
| Connectivity to `s3` endpoint          | Indicates whether the node is able to reach the service endpoint<br>for Amazon Simple Storage Service on TCP port 443. A failed test indicates connectivity<br>issues to<br>`https://s3.`region`.amazonaws.com`<br>depending on the AWS Region where the node is located.<br>Connectivity to this endpoint is not required for a node to appear<br>in your managed nodes list.                                                                |
| Connectivity to `kms` endpoint         | Indicates whether the node is able to reach the service<br>endpoint for AWS Key Management Service on TCP port 443. A failed test indicates<br>connectivity issues to<br>`https://kms.`region`.amazonaws.com`<br>depending on the AWS Region where the node is located.<br>Connectivity to this endpoint is not required for a node to<br>appear in your managed nodes list.                                                                  |
| Connectivity to `logs` endpoint        | Indicates whether the node is able to reach the service endpoint<br>for Amazon CloudWatch Logs on TCP port 443. A failed test indicates connectivity<br>issues to<br>`https://logs.`region`.amazonaws.com`<br>depending on the AWS Region where the node is located.<br>Connectivity to this endpoint is not required for a node to appear<br>in your managed nodes list.                                                                     |
| Connectivity to `monitoring` endpoint  | Indicates whether the node is able to reach the service endpoint<br>for Amazon CloudWatch on TCP port 443. A failed test indicates connectivity<br>issues to<br>`https://monitoring.`region`.amazonaws.com`<br>depending on the AWS Region where the node is located.<br>Connectivity to this endpoint is not required for a node to appear<br>in your managed nodes list.                                                                    |
| AWS Credentials                        | Indicates whether SSM Agent has the required credentials based on<br>the IAM instance profile (for EC2 instances) or IAM service role<br>(for non-EC2 machines) attached to the machine. A failed test<br>indicates that no IAM instance profile or IAM service role is<br>attached to the machine, or it does not contain the required<br>permissions for Systems Manager.                                                                   |
| Agent service                          | Indicates whether SSM Agent service is running, and whether the<br>service is running as root for Linux or macOS, or SYSTEM for<br>Windows Server. A failed test indicates SSM Agent service is not running or<br>is not running as root or SYSTEM.                                                                                                                                                                                           |
| Proxy configuration                    | Indicates whether SSM Agent is configured to use a proxy.                                                                                                                                                                                                                                                                                                                                                                                     |
| Sysprep image state (Windows only)     | Indicates the state of `Sysprep` on the node.<br>SSM Agent will not start on the node if the<br>`Sysprep` state is a value other than<br>`IMAGE_STATE_COMPLETE`.                                                                                                                                                                                                                                                                              |
| SSM Agent version                      | Indicates whether the latest available version of SSM Agent is<br>installed.                                                                                                                                                                                                                                                                                                                                                                  |
