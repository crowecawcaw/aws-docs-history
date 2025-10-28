# Add a build install

script

Create an install script for the operating system (OS) of your game build:

- Windows: Create a batch file named `install.bat`.
- Linux: Create a shell script file named
  `install.sh`.
  When creating an install script, keep in mind the following:

- The script can't take any user input.
- Amazon GameLift Servers installs the build and recreates the file directories in your build
  package on a hosting server in the following locations:
  - Windows fleets: `C:\game`
  - Linux fleets: `/local/game`

- During the installation process for Linux fleets, the run-as user has limited access to the
  instance file structure. This user has full rights to the directory where your
  build files are installed. If your install script performs actions that require
  administrator permissions, then specify admin access using **sudo**.
  The run-as user for Windows fleets has administrator permissions by default.
  Permission failures related to the install script generate an event message that indicates
  a problem with the script.
- On Linux, Amazon GameLift Servers supports common shell interpreter languages such as bash. Add
  a shebang (such as `#!/bin/bash`) to the top of your install script.
  To verify support for your preferred shell commands, remotely access an active
  Linux instance and open a shell prompt. For more information, see [Remotely connect to Amazon GameLift Servers fleet instances](fleets-remote-access.md "fleets-remote-access.md").
- The install script can't rely on a VPC peering connection. A VPC peering
  connection isn't available until after Amazon GameLift Servers installs the build on fleet
  instances.

###### Example Windows install bash file

This example `install.bat` file installs Visual C++ runtime
components required for the game server and writes the results to a log file. The
script includes the component file in the build package at the root.

```
vcredist_x64.exe /install /quiet /norestart /log c:\game\vcredist_2013_x64.log
```

###### Example Linux install shell script

This example `install.sh` file uses bash in the install script
and writes results to a log file.

```
#!/bin/bash
echo 'Hello World' > install.log
```

This example `install.sh` file shows how you can use the
Amazon CloudWatch agent to collect system-level and custom metrics, and handle log rotation.
Because Amazon GameLift Servers runs in a service VPC, you must grant Amazon GameLift Servers permissions to assume an
AWS Identity and Access Management (IAM) role on your behalf. To allow Amazon GameLift Servers to assume a role, create a
role that includes the AWS managed policy `CloudWatchAgentAdminPolicy`,
and use that role when you create a fleet.

```
sudo yum install -y amazon-cloudwatch-agent
sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
sudo yum install -y collectd
cat <<'EOF' > /tmp/config.json
{
    "agent": {
        "metrics_collection_interval": 60,
        "run_as_user": "root",
        "credentials": {
            "role_arn": "arn:aws:iam::`account#`:role/`rolename`"
        }
    },
    "logs": {
        "logs_collected": {
            "files": {
                "collect_list": [
                    {
                        "file_path": "/tmp/log",
                        "log_group_name": "gllog",
                        "log_stream_name": "{instance_id}"
                    }
                ]
            }
        }
    },
    "metrics": {
       "namespace": "GL_Metric",
        "append_dimensions": {
            "ImageId": "${aws:ImageId}",
            "InstanceId": "${aws:InstanceId}",
            "InstanceType": "${aws:InstanceType}"
        },
        "metrics_collected": {
            // Configure metrics you want to collect.
            // For more information, see Manually create or edit the CloudWatch agent configuration file.
        }
    }
}
EOF
sudo mv /tmp/config.json /opt/aws/amazon-cloudwatch-agent/bin/config.json
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json
sudo systemctl enable amazon-cloudwatch-agent.service
```
