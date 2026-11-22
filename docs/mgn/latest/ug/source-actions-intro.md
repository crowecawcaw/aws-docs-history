

# Source actions overview and prerequisites

Source actions in AWS Transform MGN are account-level resources that allow you to execute and manage custom scripts on your source environment during your migration. You provide the scripts and specify the target operating systems, and source actions execute them on your on-premises machines. Source actions enable you to execute your scripts securely and with monitoring throughout the migration lifecycle using the AWS Transform MGN Connector.

Each source action specifies:
+ Your custom script (provided as text or stored in SSM Parameter Store)
+ Target operating systems (Linux, Windows, or both)

Source actions enable you to:
+ Target scripts to specific operating systems (Linux or Windows, or both)
+ Monitor script execution status and collect results in a centralized way

## Prerequisites
<a name="source-actions-prerequisites"></a>

Before you can create and execute source actions, ensure that you have the following:
+ AWS Transform MGN connector deployed and registered
  + Network connectivity from the connector to your on-premises machines via SSH (Linux) or WinRM (Windows)
  + The connector role (`AWSApplicationMigrationConnectorManagementRole`) should allow the `mgn:SendClientLogsForMgn` and `mgn:SendClientMetricsForMgn` actions. If you created the connector before source actions were available, update its role. Without these actions, source actions still run, but the result includes a warning that AWS Transform MGN couldn't send logs or metrics. For more information, see [MGN connector permissions](mgn-connector-permissions.md)
  + We recommend that you provide the address that the connector uses to reach each machine (**FQDN for Action Framework**) in the [`mgn:server:fqdn-for-action-framework`](import-parameters.md) field of the inventory file when you import the source servers. If no address is set, MGN uses the source server's primary private IP address. For more information, see [Source actions after launching test or cutover instances](source-actions-execute.md#source-actions-after-launch)
+ Credentials registered for each machine. Source actions use the credentials secret that you registered for the source server. For more information, see [Register server credentials](connector-register-server-credentials.md)
  + On Windows, if the user isn't an administrator, the user must also have access to WinRM. For more information, see [Register server credentials](connector-register-server-credentials.md)
+ On-premises machines added to your AWS Transform MGN account and connected to the connector
  + The fully qualified domain name (FQDN) that the connector uses to reach each machine must include a dot and a top-level domain, for example `srv01.example.com`. The `RunSourceServerAction` SSM document rejects single-label names, such as `srv01`, before the action runs
+ Custom scripts, whether provided as text or stored in SSM Parameter Store. When you provide the script content in the AWS Transform MGN console of the account that owns the source servers, AWS Transform MGN creates the SSM parameter for you in that account. This doesn't apply when you create the source action for a member account from the delegated admin account through [global view](global-view.md); the SSM parameter must already exist in the member account. When using the API, scripts must be stored in SSM Parameter Store. AWS Transform MGN supports only SSM parameters whose names start with `ManagedByAWSApplicationMigrationService`.

## Security best practices for source action scripts
<a name="source-actions-security"></a>

For higher security when managing scripts in SSM Parameter Store, consider these best practices:
+ Restrict `ssm:PutParameter` permissions on parameters with the `ManagedByAWSApplicationMigrationService` prefix to authorized users only
+ Don't include secrets in your scripts. Source actions don't support `SecureString` parameters
+ Keep scripts repeatable to ensure consistent results across multiple executions
+ Keep scripts within the SSM Parameter Store parameter size limits. Parameter Store rejects values that exceed the limit
+ Use AWS CloudTrail to audit the SSM `SendCommand` operations that AWS Transform MGN runs on your behalf to execute your scripts

For more information on SSM Parameter Store security and best practices, see [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) in the *AWS Systems Manager User Guide*.

## Supported operating systems and script limitations
<a name="source-actions-supported"></a>

Source actions are supported on Linux and Windows machines. When creating a source action, you specify the target operating system. Each platform has different script requirements and behaviors.

### Linux script requirements and behaviors
<a name="source-actions-linux-scripts"></a>

On Linux, scripts are executed as root using sudo under the configured user account. The user must have passwordless sudo access.

**Script interpreter:** The script runs under the interpreter specified by the shebang (\#\!) line. For example, `#!/usr/bin/env python3` runs the script as Python. If there is no shebang line, the script runs under bash. The shebang can specify one interpreter argument, e.g., `#!/bin/bash -e`.
+ `#!/bin/sh` runs /bin/sh (dash on Debian and Ubuntu; if your script uses bash-specific syntax, use `#!/bin/bash`)
+ The interpreter must be installed on the machine. The job fails with exit code 127 if the interpreter is not found
+ The interpreter is looked up in sudo's secure path, not in your user's PATH

**Line endings:** Save scripts with Unix (LF) line endings. Windows (CRLF) line endings cause errors such as `bash: /bin/bash\r: No such file or directory` with exit code 127, or `$'\r': command not found` if there is no shebang line.

**Standard input:** The script's standard input is empty. Commands that read input (such as `read`) or expect interactive prompts (such as package manager confirmations) get end-of-input. Use non-interactive options where available, for example, `apt-get -y`.

**Script output:** SSM keeps the first 24,000 characters of the script's standard output and the first 8,000 characters of its standard error. Standard error also includes AWS Transform MGN's own progress messages and result summary, which count toward the 8,000 characters.

**Script limitations:**
+ Maximum script size: 4096 characters for a standard SSM parameter, 8192 for an advanced parameter (SSM counts characters as UTF-16 code units, so emoji and characters outside the Basic Multilingual Plane count as two). For more information, see [Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html) in the *AWS Systems Manager User Guide*
+ Maximum execution timeout: 5,400 seconds (1.5 hours). The default is 3,600 seconds (1 hour)

**Sudo requirements:** The user account must have passwordless sudo access without requiring a terminal. If this is not configured, the job fails with exit code 1 and stderr shows `sudo: a password is required` or `sudo: sorry, you must have a tty to run sudo`. To verify, run: `ssh <user>@<server> 'sudo -n bash -c true' && echo ok`

### Windows script requirements and behaviors
<a name="source-actions-windows-scripts"></a>

On Windows, scripts run as Windows PowerShell scripts. There is no equivalent of the Linux shebang line, so the script type cannot be chosen per script. To run batch files, VBScript, or other interpreters, call them from within your PowerShell script.

**Exit codes:** The job's exit code is the exit code of the last external program (.exe) your script ran, not PowerShell's own commands. PowerShell non-terminating errors (such as `Write-Error` or `Get-Item` on a missing path with default settings) do not change the exit code. A script with only non-terminating errors is reported as succeeded even though errors occurred. To fail the job on any error, add this line at the top of your script: `$ErrorActionPreference = 'Stop'`. Alternatively, end your script or each failure path with an explicit exit code, e.g., `exit 1`.

**PowerShell language mode:** The script runs in Windows PowerShell FullLanguage mode. Constrained Language Mode is not supported; scripts fail with exit code 1 if the server is configured with Constrained Language Mode. To check your server, run `$ExecutionContext.SessionState.LanguageMode`; it must print `FullLanguage`.

**Script output:** SSM keeps the first 24,000 characters of the script's standard output and the first 8,000 characters of its standard error. Standard error also includes AWS Transform MGN's own progress messages and result summary, which count toward the 8,000 characters. Progress output is suppressed (`$ProgressPreference = 'SilentlyContinue'`); if your script needs progress output, set `$ProgressPreference` explicitly.

**Script paths:** `$PSCommandPath` and `$PSScriptRoot` are empty because the script does not run from a visible file path.

**Script limitations:**
+ Maximum script size: 4096 characters for a standard SSM parameter, 8192 for an advanced parameter (SSM counts characters as UTF-16 code units, so emoji and characters outside the Basic Multilingual Plane count as two). For more information, see [Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html) in the *AWS Systems Manager User Guide*
+ Maximum execution timeout: 5,400 seconds (1.5 hours). The default is 3,600 seconds (1 hour)

**Running other script types:** To run batch files or other interpreters, call them from PowerShell. For example:
+ Batch commands: `cmd /c "echo Hello from cmd && ver"`
+ Other interpreters: `& 'C:\Program Files\Python312\python.exe' C:\scripts\setup.py` or `pwsh -NoProfile -File C:\scripts\setup.ps1`

### Common limitations for both platforms
<a name="source-actions-common-limitations"></a>
+ Scripts must be stored in SSM Parameter Store

## Account ownership and multi-account migrations
<a name="source-actions-accounts"></a>

AWS Transform MGN uses an AWS multi-account architecture with two types of accounts:
+ **Member account:** The AWS account where migrated servers are launched as Amazon EC2 instances. Member accounts are individual business units or applications within an organization. Each member account manages its own on-premises servers and source actions within that account. A delegated admin account can view and manage the member account's source servers through [global view](global-view.md).
+ **Delegated admin account:** The AWS account of the organization that controls and has full administrator permissions to manage migrations across all member accounts. The delegated admin account can execute source actions on behalf of member accounts through an AWS Transform MGN Connector. The connector can be deployed in the delegated admin account or in a member account.

Source actions follow a specific account ownership model in AWS Transform MGN:

### Multi-account migration scenarios
<a name="source-actions-multi-account"></a>

You have two main approaches for multi-account migrations:

**Scenario 1: Centralized connector in the delegated admin account (recommended for scale)**

In typical multi-account migrations with a centralized connector:
+ The AWS Transform MGN Connector is deployed in the delegated admin account
+ On-premises machines and source actions reside in member accounts
+ The delegated admin account executes actions against machines in any connected member account
+ Member accounts can create and manage their own actions, but cannot execute them
+ Suitable for organizations with a central migration team managing multiple business units

**Scenario 2: Dedicated connector per member account (independent control)**

Each member account can create and deploy its own AWS Transform MGN Connector:
+ Member account creates source actions and owns the connector managing them
+ Member account has full control over all source action operations and execution
+ Each member account with on-premises machines requires its own connector deployment
+ Suitable for organizations where individual business units manage their own migrations
+ Provides account-level isolation and independent monitoring of source action executions

### Member account capabilities
<a name="source-actions-member-account"></a>

In the member account:
+ **Create** source actions that contain your custom scripts
+ **Update** or **delete** source actions
+ **View monitoring results** (limited) — see the status and results of source action executions. The link to the SSM execution log is available only in the account where the AWS Transform MGN connector is deployed
+ Source actions are owned by the member account but cannot be executed from this account

A member account can also deploy its own AWS Transform MGN Connector and execute its source actions. For more information, see [Multi-account migration scenarios](#source-actions-multi-account) (Scenario 2).

### Delegated admin account capabilities
<a name="source-actions-management-account"></a>

In the delegated admin account (connector owner):
+ **Execute** source actions on source servers in member accounts
+ **Monitor executions** (full) — track job status, invocation status, and view execution details across all connected source servers
+ Create and manage source action execution jobs
+ Runs source actions through an AWS Transform MGN Connector, which can be deployed in the delegated admin account or in a member account

The delegated admin account has these limitations:
+ When you create a source action for a member account, the **Script content** option is not available. The SSM parameter must exist in the member account, because the delegated admin account doesn't have permission to create SSM parameters in the member account through the AWS Transform MGN console. If you only have the script content, create the SSM parameter in the member account, and then return to the delegated admin account and choose it
+ You can't run a source action on machines from multiple accounts in a single execution. To run a source action on all of the machines in one account, filter the source server list by account, server name, or another attribute