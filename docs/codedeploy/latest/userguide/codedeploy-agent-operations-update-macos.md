

# Update the CodeDeploy agent on macOS
<a name="codedeploy-agent-operations-update-macos"></a>

To configure automatic, scheduled updates of the CodeDeploy agent using AWS Systems Manager, follow the steps in [Install the CodeDeploy agent using AWS Systems Manager](codedeploy-agent-operations-install-ssm.md) and choose the `AWSCodeDeployAgentV2` package.

To force an update, run:

```
sudo /opt/codedeploy-agent/bin/codedeploy-agent update
```

Alternatively, download the latest `.pkg` file and install it over the existing agent. For installation instructions, see [Install the CodeDeploy agent for macOS](codedeploy-agent-operations-install-macos.md).