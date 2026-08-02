# Determine the version of the CodeDeploy agent

You can determine the version of the CodeDeploy agent running on your instance in two
ways.

First, for version 2.0.x and later, use the `codedeploy-agent --version`
command on all platforms.

Second, you can view the version in a `.version` file on the instance. On
Amazon Linux, RHEL, and Ubuntu Server the file is located at
`/opt/codedeploy-agent/.version`, and on Windows Server at
`C:\ProgramData\Amazon\CodeDeploy\.version`. The contents of the file differ by
version:

- For version 2.0.x and later, the file contains the bare version number, in the format
  `agent_version: 2.0.0`. This value matches the version that the agent
  reports to the CodeDeploy service.
- For version 1.8.x and earlier, the version string uses the format
  `OFFICIAL_1.0.1.854_rpm` (or `_deb`, `_msi`).

###### Topics

- [Determine the version on Amazon Linux or RHEL](#codedeploy-agent-operations-version-linux "#codedeploy-agent-operations-version-linux")
- [Determine the version on Ubuntu Server](#codedeploy-agent-operations-version-ubuntu "#codedeploy-agent-operations-version-ubuntu")
- [Determine the version on Windows Server](#codedeploy-agent-operations-version-windows "#codedeploy-agent-operations-version-windows")

## Determine the version on Amazon Linux or RHEL

Sign in to the instance and run the following command:

```
sudo /opt/codedeploy-agent/bin/codedeploy-agent --version
```

For versions earlier than 2.0.0, you can also use:

```
sudo yum info codedeploy-agent
```

## Determine the version on Ubuntu Server

Sign in to the instance and run the following command:

```
sudo /opt/codedeploy-agent/bin/codedeploy-agent --version
```

For versions earlier than 2.0.0, you can also use:

```
sudo dpkg -s codedeploy-agent
```

## Determine the version on Windows Server

Sign in to the instance and run the following command:

```
& 'C:\ProgramData\Amazon\CodeDeploy\bin\codedeploy-agent.exe' --version
```
