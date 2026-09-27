

# Determine the version of the CodeDeploy agent
<a name="codedeploy-agent-operations-version"></a>

You can determine the version of the CodeDeploy agent running on your instance in two ways.

First, for version 2.0.x and later, use the `codedeploy-agent --version` command on all platforms.

Second, you can view the version in a `.version` file on the instance. On Amazon Linux, RHEL, and Ubuntu Server the file is located at `/opt/codedeploy-agent/.version`, and on Windows Server at `C:\ProgramData\Amazon\CodeDeploy\.version`. The contents of the file differ by version:
+ For version 2.0.x and later, the file contains the bare version number, in the format `agent_version: 2.0.0`. This value matches the version that the agent reports to the CodeDeploy service.
+ For version 1.8.x and earlier, the version string uses the format `OFFICIAL_1.0.1.854_rpm` (or `_deb`, `_msi`).

**Topics**
+ [Determine the version on Amazon Linux or RHEL](#codedeploy-agent-operations-version-linux)
+ [Determine the version on Ubuntu Server](#codedeploy-agent-operations-version-ubuntu)
+ [Determine the version on Windows Server](#codedeploy-agent-operations-version-windows)
+ [Determine the latest agent version available in an AWS Region](#codedeploy-agent-operations-version-latest)

## Determine the version on Amazon Linux or RHEL
<a name="codedeploy-agent-operations-version-linux"></a>

Sign in to the instance and run the following command:

```
sudo /opt/codedeploy-agent/bin/codedeploy-agent --version
```

For versions earlier than 2.0.0, you can also use:

```
sudo yum info codedeploy-agent
```

## Determine the version on Ubuntu Server
<a name="codedeploy-agent-operations-version-ubuntu"></a>

Sign in to the instance and run the following command:

```
sudo /opt/codedeploy-agent/bin/codedeploy-agent --version
```

For versions earlier than 2.0.0, you can also use:

```
sudo dpkg -s codedeploy-agent
```

## Determine the version on Windows Server
<a name="codedeploy-agent-operations-version-windows"></a>

Sign in to the instance and run the following command:

```
& 'C:\ProgramData\Amazon\CodeDeploy\bin\codedeploy-agent.exe' --version
```

## Determine the latest agent version available in an AWS Region
<a name="codedeploy-agent-operations-version-latest"></a>

To find out which version is the latest one available in the AWS Region you deploy to, query the CodeDeploy resource kit bucket for that Region. Each regional bucket holds a `latestv2/LATEST_VERSION` file that names the agent packages currently released in that Region. The file is publicly readable, so you don't need credentials to retrieve it.

```
curl https://{{bucket-name}}.s3.{{region-identifier}}.amazonaws.com/latestv2/LATEST_VERSION
```

Replace {{bucket-name}} and {{region-identifier}} with the resource kit bucket and Region identifier for the Region you deploy to. For the list, see [Resource kit bucket names by Region](resource-kit.md#resource-kit-bucket-names).

The command returns output similar to the following:

```
{
    "rpm_x86_64": "releases/codedeploy-agent-2.1.0-9745926189.x86_64.rpm",
    "rpm_aarch64": "releases/codedeploy-agent-2.1.0-9745926189.aarch64.rpm",
    "deb_x86_64": "releases/codedeploy-agent_2.1.0-9745926189_amd64.deb",
    "deb_aarch64": "releases/codedeploy-agent_2.1.0-9745926189_arm64.deb",
    "msi": "releases/codedeploy-agent-2.1.0-9745926189.msi"
}
```

Each key names a package type, and for RPM and DEB the instance architecture as well. Each value is the Amazon S3 object key of that package, and the agent version and build number are part of its file name, in the format `{{agent-version}}-{{build-number}}`. In the preceding output, the latest version available in the Region is 2.1.0.

To install or update to the version this file names, see [Install the CodeDeploy agent](codedeploy-agent-operations-install.md) and [Update the CodeDeploy agent](codedeploy-agent-operations-update.md). For the features included in each version, see [Version history of the CodeDeploy agent](codedeploy-agent.md#codedeploy-agent-version-history).