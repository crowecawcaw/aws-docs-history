# Use AWS Systems Manager to apply STIG settings to your instance

You can use the `AWSEC2-ConfigureSTIG` Systems Manager command document to apply STIG settings
to an existing EC2 instance. You must run the command document from the instance that it updates. The
command document applies appropriate settings based on the operating system and configuration of the
instance where it runs.

This page contains details about the `AWSEC2-ConfigureSTIG` command document, including
input parameters and how to run it in the Systems Manager console or with `send-command` in the
AWS CLI.

## AWSEC2-ConfigureSTIG input parameters

You can provide the following input parameters to specify how the command document should apply
STIG settings to your instance.

**Level** (string, required)

Specify the STIG severity category to apply. Valid values include the following:

- High
- Medium
- Low

If you don't specify a value the system defaults to `High`.

**InstallPackages** (string, optional – Linux only)

If the value is `No`, the script does not install any additional software
packages. If the value is `Yes`, the script installs additional software
packages that are required for maximum compliance. The default value is `No`.

**SetDoDConsentBanner** (string, optional – Linux only)

If the value is `No`, the DoD consent banner is not shown when you attach to
an instance that has a Linux STIG script installed. If the value is `Yes`, the DoD
consent banner is shown before you log in when you attach to an instance that has one of
the STIG Linux scripts installed. You must acknowledge the banner before you can log in.
The default value is `No`.

For an example of the consent banner, see the [Disclaimer
Department of Defense Privacy and Consent Notice](https://dso.dla.mil/ "https://dso.dla.mil/") that appears when you access
the DLA Document Services website.

## Run the AWSEC2-ConfigureSTIG command document

To run the `AWSEC2-ConfigureSTIG` document, follow the steps for
your preferred environment.

Console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Select **Run Command** from the navigation pane.
   This shows a list of commands that are currently running in your account,
   if applicable.
3. Choose **Run command**. This opens the **Run a
   command** dialog and displays a list of command documents that you have
   access to.
4. Select `AWSEC2-ConfigureSTIG` from the list
   of command documents. To streamline results, you can enter all or part of
   the document name. You can also filter by the owner, by platform types,
   or by tags.

When you select a command document, details populate below the list. 5. Select `Default version at runtime` from the
**Document version** list. 6. Configure the **Command parameters** to define how
`AWSEC2-ConfigureSTIG` will install the
script package and run it to update your instance. For parameter details, see [AWSEC2-ConfigureSTIG input parameters](#ec2-stig-ssm-cmd-doc-params "#ec2-stig-ssm-cmd-doc-params"). 7. For **Target selection**, specify tags or select
instances manually to identify the instances on which to run this operation.

###### Note

If you select instances manually, and an instance you expect to see is not
included in the list, see [Where Are My Instances?](../../../systems-manager/latest/userguide/troubleshooting-remote-commands.md#where-are-instances "../../../systems-manager/latest/userguide/troubleshooting-remote-commands.md#where-are-instances") for troubleshooting tips. 8. For additional parameters to define Systems Manager Run Command behavior such as
**Rate control**, enter values as described in
[Running commands from the console](../../../systems-manager/latest/userguide/running-commands-console.md "../../../systems-manager/latest/userguide/running-commands-console.md"). 9. Choose **Run**.

If successful, the command document installs the script and configures your instance.
If the command execution failed, view the Systems Manager command output for details about
why the execution failed.

AWS CLI

###### Example 1: Run with default values

Run the following command to install the STIG script and run it with default values.
For more information about input parameters, see [AWSEC2-ConfigureSTIG input parameters](#ec2-stig-ssm-cmd-doc-params "#ec2-stig-ssm-cmd-doc-params").

```
aws ssm send-command \
	--document-name "AWSEC2-ConfigureSTIG" \
	--instance-ids "`i-1234567890abcdef0`"'
```

###### Example 2: Configure Medium level STIG settings on your instance

Run the following command to install the STIG script and run it with the
`Level` input parameter set to `Medium`.
For more information about input parameters, see [AWSEC2-ConfigureSTIG input parameters](#ec2-stig-ssm-cmd-doc-params "#ec2-stig-ssm-cmd-doc-params").

```
aws ssm send-command \
	--document-name "AWSEC2-ConfigureSTIG" \
	--instance-ids "`i-1234567890abcdef0`"
	--parameters '{"Level":"Medium"}'
```

If successful, the command document installs the script and configures your instance.
If the command execution failed, view the command output for details about why the execution
failed.

PowerShell

###### Example 1: Run with default values

Run the following command to install the STIG script and run it with default values.
For more information about input parameters, see [AWSEC2-ConfigureSTIG input parameters](#ec2-stig-ssm-cmd-doc-params "#ec2-stig-ssm-cmd-doc-params").

```
Send-SSMCommand -DocumentName "AWSEC2-ConfigureSTIG" -InstanceId "`i-1234567890abcdef0`"}
```

###### Example 2: Configure Medium level STIG settings on your instance

Run the following command to install the STIG script and run it with the
`Level` input parameter set to `Medium`.
For more information about input parameters, see [AWSEC2-ConfigureSTIG input parameters](#ec2-stig-ssm-cmd-doc-params "#ec2-stig-ssm-cmd-doc-params").

```
Send-SSMCommand -DocumentName "AWSEC2-ConfigureSTIG" -InstanceId "`i-1234567890abcdef0`" -Parameter @{'Level'='Medium'}
```

If successful, the command document installs the script and configures your instance.
If the command execution failed, view the command output for details about why the execution
failed.
