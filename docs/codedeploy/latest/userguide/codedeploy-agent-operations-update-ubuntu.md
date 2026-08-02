# Update the CodeDeploy agent on Ubuntu Server

To configure automatic, scheduled updates of the CodeDeploy agent using AWS Systems Manager, follow the
steps in [Install the
CodeDeploy agent with AWS Systems Manager](codedeploy-agent-operations-install-ssm.md "codedeploy-agent-operations-install-ssm.md").

For version 2.0.x and later, to force an update, run:

```
sudo /opt/codedeploy-agent/bin/codedeploy-agent update
```

Alternatively, re-download and run the regional `latestv2/install` script. For
installation instructions, see [Install the CodeDeploy agent for Ubuntu Server](codedeploy-agent-operations-install-ubuntu.md "codedeploy-agent-operations-install-ubuntu.md").

For version 1.8.x and earlier, to force an update, run:

```
sudo /opt/codedeploy-agent/bin/install auto
```

###### Important

There is currently no automatic update path from version 1.8.x to 2.0.0. To upgrade
to 2.0.0, run the regional `latestv2/install` script manually. For
instructions, see [Install the CodeDeploy agent for Ubuntu Server](codedeploy-agent-operations-install-ubuntu.md "codedeploy-agent-operations-install-ubuntu.md").
