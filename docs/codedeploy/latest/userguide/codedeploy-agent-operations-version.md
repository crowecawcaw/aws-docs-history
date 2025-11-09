# Determine the version of the CodeDeploy

agent

You can determine the version of the CodeDeploy agent running on your instance in two
ways.

First, starting with version 1.0.1.854 of the CodeDeploy agent, you can view the version number
in a `.version` file on the instance. The following table shows the location and
sample version string for each of the supported operating systems.

| Operating system                                 | File location                               | Sample agent_version string |
| ------------------------------------------------ | ------------------------------------------- | --------------------------- |
| Amazon Linux and Red Hat Enterprise Linux (RHEL) | `/opt/codedeploy-agent/.version`            | OFFICIAL_1.0.1.854_rpm      |
| Ubuntu Server                                    | `/opt/codedeploy-agent/.version`            | OFFICIAL_1.0.1.854_deb      |
| Windows Server                                   | `C:\ProgramData\Amazon\CodeDeploy\.version` | OFFICIAL_1.0.1.854_msi      |

Second, you can run a command on an instance to determine the version of the CodeDeploy
agent.

###### Topics

- [Determine the version on Amazon Linux or
  RHEL](#codedeploy-agent-operations-version-linux "#codedeploy-agent-operations-version-linux")
- [Determine the version on
  Ubuntu Server](#codedeploy-agent-operations-version-ubuntu "#codedeploy-agent-operations-version-ubuntu")
- [Determine the version on
  Windows Server](#codedeploy-agent-operations-version-windows "#codedeploy-agent-operations-version-windows")

## Determine the version on Amazon Linux or

RHEL

Sign in to the instance and run the following command:

```
sudo yum info codedeploy-agent
```

## Determine the version on

Ubuntu Server

Sign in to the instance and run the following command:

```
sudo dpkg -s codedeploy-agent
```

## Determine the version on

Windows Server

Sign in to the instance and run the following command:

```
sc qdescription codedeployagent
```
