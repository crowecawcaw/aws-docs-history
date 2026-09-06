

# Update the CodeDeploy agent on Amazon Linux or RHEL
<a name="codedeploy-agent-operations-update-linux"></a>

To configure automatic, scheduled updates of the CodeDeploy agent using AWS Systems Manager, follow the steps in [Install the CodeDeploy agent with AWS Systems Manager](https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-ssm.html).

For version 2.0.x and later, to force an update, run:

```
sudo /opt/codedeploy-agent/bin/codedeploy-agent update
```

Alternatively, re-download and run the regional `latestv2/install` script. For installation instructions, see [Install the CodeDeploy agent for Amazon Linux or RHEL](codedeploy-agent-operations-install-linux.md).

For version 1.8.x and earlier, to force an update, run:

```
sudo /opt/codedeploy-agent/bin/install auto
```

**Important**  
No automatic update path currently exists from version 1.8.x to 2.0.0. To upgrade to 2.0.0, install it with the `AWSCodeDeployAgentV2` Systems Manager Distributor package or run the regional `latestv2/install` script manually. For instructions, see [Install the CodeDeploy agent](codedeploy-agent-operations-install.md).