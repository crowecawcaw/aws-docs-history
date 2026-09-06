

# Managing CodeDeploy agent operations
<a name="codedeploy-agent-operations"></a>

The instructions in this section show you how to install, uninstall, reinstall, or update the CodeDeploy agent and how to verify the CodeDeploy agent is running.

**Version 2.0.x rollout status**  
Version 2.0.x of the CodeDeploy agent is being rolled out across AWS Regions and might not be available in all Regions yet. Version 2.0.0 is an opt-in upgrade. In order to upgrade to version 2.0.x from any older revisions, see [Install the CodeDeploy agent](codedeploy-agent-operations-install.md).

**Tip**  
Some instructions on this page differ depending on the agent version. If you are unsure which version is installed, run `/opt/codedeploy-agent/bin/codedeploy-agent --version` (Linux) or `& 'C:\ProgramData\Amazon\CodeDeploy\bin\codedeploy-agent.exe' --version` (Windows). If that command is not recognized, you are running version 1.8.x or earlier. For more information, see [Determine the version of the CodeDeploy agent](codedeploy-agent-operations-version.md).

**Topics**
+ [Verify the CodeDeploy agent is running](codedeploy-agent-operations-verify.md)
+ [Determine the version of the CodeDeploy agent](codedeploy-agent-operations-version.md)
+ [Install the CodeDeploy agent](codedeploy-agent-operations-install.md)
+ [Update the CodeDeploy agent](codedeploy-agent-operations-update.md)
+ [Uninstall the CodeDeploy agent](codedeploy-agent-operations-uninstall.md)
+ [Send CodeDeploy agent logs to CloudWatch](codedeploy-agent-operations-cloudwatch-agent.md)