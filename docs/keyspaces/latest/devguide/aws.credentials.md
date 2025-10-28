# Store access keys for programmatic access

As a best practice, we recommend that you don't embed access keys directly into code.
The AWS SDKs and the AWS Command Line Tools enable you to put access keys in known
locations so that you do not have to keep them in code. Put access keys in one of the following locations:

- **Environment variables** – On a multitenant system, choose
  user environment variables, not system environment variables.
- **CLI credentials file** – The `credentials` and
  `config` file are updated when you run the command `aws
configure`. The `credentials` file is located at
  `~/.aws/credentials` on Linux, macOS, or Unix, or at `C:\Users\`USERNAME`\.aws\credentials` on Windows.
  This file can contain the credential details for the `default` profile
  and any named profiles.
- **CLI configuration file** – The `credentials`
  and `config` file are updated when you run the command `aws
 configure`. The `config` file is located at
  `~/.aws/config` on Linux, macOS, or Unix, or at `C:\Users\`USERNAME`\.aws\config` on
  Windows. This file contains the configuration settings for the default profile and
  any named profiles.
  Storing access keys as environment variables is a prerequisite for the [Step-by-step tutorial to connect to Amazon Keyspaces using the 4.x DataStax Java driver for Apache Cassandra
  and the SigV4 authentication plugin](using_java_driver.md#java_tutorial.SigV4 "using_java_driver.md#java_tutorial.SigV4"). Note that this includes the default AWS Region. The client searches for credentials using the default
  credentials provider chain, and access keys stored as environment variables take precedent
  over all other locations, for example configuration files. For more information, see
  [Configuration settings and precedence](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-precedence "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-precedence").

The following examples show how you can configure environment variables for the
default user.

Linux, macOS, or Unix

```
`$` `export AWS_ACCESS_KEY_ID=`AKIAIOSFODNN7EXAMPLE``
`$` `export AWS_SECRET_ACCESS_KEY=`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY``
`$` `export AWS_SESSION_TOKEN=`AQoDYXdzEJr...<remainder of security token>``
`$` `export AWS_DEFAULT_REGION=`us-east-1``
```

Setting the environment variable changes the value used until the end of
your shell session, or until you set the variable to a different value. You
can make the variables persistent across future sessions by setting them in
your shell's startup script.

Windows Command Prompt

```
`C:\>` `setx AWS_ACCESS_KEY_ID `AKIAIOSFODNN7EXAMPLE``
`C:\>` `setx AWS_SECRET_ACCESS_KEY `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY``
`C:\>` `setx AWS_SESSION_TOKEN `AQoDYXdzEJr...<remainder of security token>``
`C:\>` `setx AWS_DEFAULT_REGION `us-east-1``
```

Using `set` to set an environment variable changes the value
used until the end of the current command prompt session, or until you set
the variable to a different value. Using [`setx`](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/setx "https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/setx") to set an environment variable changes
the value used in both the current command prompt session and all command
prompt sessions that you create after running the command. It does **_not_** affect
other command shells that are already running at the time you run the
command.

PowerShell

```
`PS C:\>` `$Env:AWS_ACCESS_KEY_ID="`AKIAIOSFODNN7EXAMPLE`"`
`PS C:\>` `$Env:AWS_SECRET_ACCESS_KEY="`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY``"
`PS C:\>` `$Env:AWS_SESSION_TOKEN="`AQoDYXdzEJr...<remainder of security token>`"`
`PS C:\>` `$Env:AWS_DEFAULT_REGION="`us-east-1`"`
```

If you set an environment variable at the PowerShell prompt as shown in
the previous examples, it saves the value for only the duration of the
current session. To make the environment variable setting persistent across
all PowerShell and Command Prompt sessions, store it by using the
**System** application in **Control
Panel**. Alternatively, you can set the variable for all future
PowerShell sessions by adding it to your PowerShell profile. See the [PowerShell documentation](https://docs.microsoft.com/powershell/module/microsoft.powershell.core/about/about_environment_variables "https://docs.microsoft.com/powershell/module/microsoft.powershell.core/about/about_environment_variables") for more information about storing
environment variables or persisting them across sessions.
