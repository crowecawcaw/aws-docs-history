

# Verify the CodeDeploy agent is running
<a name="codedeploy-agent-operations-verify"></a>

This section describes commands to run if you suspect the CodeDeploy agent has stopped running on an instance.

**Topics**
+ [Verify the CodeDeploy agent for Amazon Linux or RHEL is running](#codedeploy-agent-operations-verify-linux)
+ [Verify the CodeDeploy agent for Ubuntu Server is running](#codedeploy-agent-operations-verify-ubuntu)
+ [Verify the CodeDeploy agent for Windows Server is running](#codedeploy-agent-operations-verify-windows)
+ [Verify the CodeDeploy agent for macOS is running](#codedeploy-agent-operations-verify-macos)

## Verify the CodeDeploy agent for Amazon Linux or RHEL is running
<a name="codedeploy-agent-operations-verify-linux"></a>

To see if the CodeDeploy agent is installed and running, sign in to the instance, and run the following command:

```
systemctl status codedeploy-agent
```

If the command returns an error, the CodeDeploy agent is not installed. Install it as described in [Install the CodeDeploy agent for Amazon Linux or RHEL](codedeploy-agent-operations-install-linux.md).

If the CodeDeploy agent is installed and running, you should see a message like `The AWS CodeDeploy agent is running.` (exit code 0).

If you see a message like `The AWS CodeDeploy agent is not running.` (exit code 3), start the service and run the following two commands, one at a time:

```
systemctl start codedeploy-agent
```

```
systemctl status codedeploy-agent
```

For version 2.0.x and later, the `codedeploy-agent status` command returns LSB-compatible exit codes: `0` (running), `3` (not running), `4` (unknown). When using `systemctl status`, the unit state is displayed (for example, `Active: active (running)`).

## Verify the CodeDeploy agent for Ubuntu Server is running
<a name="codedeploy-agent-operations-verify-ubuntu"></a>

To see if the CodeDeploy agent is installed and running, sign in to the instance, and run the following command:

```
systemctl status codedeploy-agent
```

If the command returns an error, the CodeDeploy agent is not installed. Install it as described in [Install the CodeDeploy agent for Ubuntu Server](codedeploy-agent-operations-install-ubuntu.md).

If the CodeDeploy agent is installed and running, you should see a message like `The AWS CodeDeploy agent is running.` (exit code 0).

If you see a message like `The AWS CodeDeploy agent is not running.` (exit code 3), start the service and run the following two commands, one at a time:

```
systemctl start codedeploy-agent
```

```
systemctl status codedeploy-agent
```

## Verify the CodeDeploy agent for Windows Server is running
<a name="codedeploy-agent-operations-verify-windows"></a>

To see if the CodeDeploy agent is installed and running, sign in to the instance, and run the following command:

```
powershell.exe -Command Get-Service -Name codedeployagent
```

You should see output similar to the following:

```
Status   Name               DisplayName
------   ----               -----------
Running codedeployagent    CodeDeploy Host Agent Service
```

If the command returns an error, the CodeDeploy agent is not installed. Install it as described in [Install the CodeDeploy agent for Windows Server](codedeploy-agent-operations-install-windows.md).

If `Status` shows anything other than `Running`, start the service with the following command:

```
powershell.exe -Command Start-Service -Name codedeployagent
```

You can restart the service with the following command:

```
powershell.exe -Command Restart-Service -Name codedeployagent
```

You can stop the service with the following command:

```
powershell.exe -Command Stop-Service -Name codedeployagent
```

## Verify the CodeDeploy agent for macOS is running
<a name="codedeploy-agent-operations-verify-macos"></a>

To see if the CodeDeploy agent is installed and running, sign in to the instance, and run the following command:

```
sudo /opt/codedeploy-agent/bin/codedeploy-agent status
```

If the command returns an error because the file is not found, the CodeDeploy agent is not installed. Install it as described in [Install the CodeDeploy agent for macOS](codedeploy-agent-operations-install-macos.md).

If the CodeDeploy agent is installed and running, you should see a message like `The AWS CodeDeploy agent is running.` (exit code 0).

If you see a message like `The AWS CodeDeploy agent is not running.` (exit code 3), start the agent with the following command:

```
sudo launchctl kickstart system/com.amazon.aws.codedeploy-agent
```

If that command reports that the service could not be found, the launchd daemon is not loaded. Load and start it with the following command:

```
sudo launchctl bootstrap system /Library/LaunchDaemons/com.amazon.aws.codedeploy-agent.plist
```

To see the state of the launchd daemon, run:

```
sudo launchctl print system/com.amazon.aws.codedeploy-agent
```