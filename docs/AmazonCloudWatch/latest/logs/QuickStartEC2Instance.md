# Quick Start: Install and configure the CloudWatch Logs agent on a

running EC2 Linux instance

###### Important

The older logs agent is deprecated. CloudWatch includes a unified agent that can collect both logs and metrics from EC2 instances
and on-premises servers. For more information,
see [Getting started with CloudWatch Logs](CWL_GettingStarted.md "CWL_GettingStarted.md").

For information about migrating from the older CloudWatch Logs agent to the unified agent, see
[Create the CloudWatch agent configuration file with the wizard](../monitoring/create-cloudwatch-agent-configuration-file-wizard.md "../monitoring/create-cloudwatch-agent-configuration-file-wizard.md").

The older logs agent supports only versions 2.6 to 3.5 of Python. Additionally, the older CloudWatch Logs agent doesn't support Instance Metadata Service Version 2 (IMDSv2). If
your server uses IMDSv2, you must use the newer unified agent instead of the older CloudWatch Logs agent.

The rest of this section explains the use of the older CloudWatch Logs agent for customers
who are still using it.

###### Tip

CloudWatch includes a new unified agent that can collect both logs and metrics from EC2 instances and on-premises servers. If you are
not already using the older CloudWatch Logs agent, we recommend that you use the newer unified CloudWatch
agent. For more information,
see [Getting started with CloudWatch Logs](CWL_GettingStarted.md "CWL_GettingStarted.md").

Additionally, the older agent doesn't support Instance Metadata Service Version 2 (IMDSv2). If
your server uses IMDSv2, you must use the newer unified agent instead of the older CloudWatch Logs agent.

The rest of this section explains the use of the older CloudWatch Logs agent.

## Configure the older CloudWatch Logs agent on a running EC2

Linux instance

You can use the CloudWatch Logs agent installer on an existing EC2 instance to install and
configure the CloudWatch Logs agent. After installation is complete, logs automatically flow from the instance
to the log stream you create while installing the agent. The agent confirms that it
has started and it stays running until you disable it.

In addition to using the agent, you can also publish log data using the AWS CLI, CloudWatch Logs SDK, or
the CloudWatch Logs API. The AWS CLI is best suited for publishing data at the command line or
through scripts. The CloudWatch Logs SDK is best suited for publishing log data directly from
applications or building your own log publishing application.

### Step 1: Configure your IAM role or user for CloudWatch Logs

The CloudWatch Logs agent supports IAM roles and users. If your instance already has an
IAM role associated with it, make sure that you include the IAM policy below. If
you don't already have an IAM role assigned to your instance, you can use your
IAM credentials for the next steps or you can assign an IAM role to that
instance. For more information, see [Attaching an
IAM Role to an Instance](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#attach-iam-role "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#attach-iam-role").

###### To configure your IAM role or

user for CloudWatch Logs

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Choose the role by selecting the role name (do not select the check box next to the name).
4. Choose **Attach
   Policies**, **Create Policy**.

A new browser tab or window opens. 5. Choose the **JSON** tab and type the following JSON policy document.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:DescribeLogStreams"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

6. When you are finished, choose **Review policy**. The Policy Validator reports any syntax errors.
7. On the **Review Policy** page, type a **Name** and a **Description**
   (optional) for the policy that you are creating. Review the policy **Summary** to see the
   permissions that are granted by your policy. Then choose **Create policy** to save your work.
8. Close the browser tab or window, and return to the **Add permissions** page for your role. Choose
   **Refresh**, and then choose the new policy to attach it to your role.
9. Choose **Attach Policy**.

### Step 2: Install and configure CloudWatch Logs on an existing Amazon EC2

instance

The process for installing the CloudWatch Logs agent differs depending on whether your Amazon EC2
instance is running Amazon Linux, Ubuntu, CentOS, or Red Hat. Use the steps appropriate for
the version of Linux on your instance.

###### To install and configure CloudWatch Logs on an existing Amazon Linux instance

Starting with Amazon Linux AMI 2014.09, the CloudWatch Logs agent is available as an RPM
installation with the awslogs package. Earlier versions of Amazon Linux can access the
awslogs package by updating their instance with the `sudo yum update
 -y` command. By installing the awslogs package as an RPM instead of
the using the CloudWatch Logs installer, your instance receives regular package updates
and patches from AWS without having to manually reinstall the CloudWatch Logs
agent.

###### Warning

Do not update the CloudWatch Logs agent using the RPM installation method if you
previously used the Python script to install the agent. Doing so may cause
configuration issues that prevent the CloudWatch Logs agent from sending your logs to
CloudWatch.

1. Connect to your Amazon Linux instance. For more information, see [Connect to Your
   Instance](../../../AWSEC2/latest/UserGuide/ec2-connect-to-instance-linux.md "../../../AWSEC2/latest/UserGuide/ec2-connect-to-instance-linux.md") in the _Amazon EC2 User Guide_.

For more information about connection issues, see [Troubleshooting Connecting to Your Instance](../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md "../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md") in the
_Amazon EC2 User Guide_. 2. Update your Amazon Linux instance to pick up the latest changes in the package
repositories.

```
sudo yum update -y
```

3. Install the `awslogs` package. This is the recommended method
   for installing awslogs on Amazon Linux instances.

```
sudo yum install -y awslogs
```

4. Edit the `/etc/awslogs/awslogs.conf` file to configure
   the logs to track. For more information about editing this file, see [CloudWatch Logs agent reference](AgentReference.md "AgentReference.md").
5. By default, the `/etc/awslogs/awscli.conf` points to
   the us-east-1 Region. To push your logs to a different Region, edit the
   `awscli.conf` file and specify that
   Region.
6. Start the `awslogs` service.

```
`sudo service awslogs start`
```

If you are running Amazon Linux 2, start the `awslogs` service with the following command.

```
`sudo systemctl start awslogsd`
```

7. (Optional) Check the `/var/log/awslogs.log` file for
   errors logged when starting the service.
8. (Optional) Run the following command to start the
   `awslogs` service at each system boot.

```
`sudo chkconfig awslogs on`
```

If you are running Amazon Linux 2, use the following command to start the service at each system boot.

```
`sudo systemctl enable awslogsd.service`
```

9. You should see the newly created log group and log stream in the CloudWatch
   console after the agent has been running for a few moments.

For more information, see [View log data sent to CloudWatch Logs](Working-with-log-groups-and-streams.md#ViewingLogData "Working-with-log-groups-and-streams.md#ViewingLogData").

###### To install and configure CloudWatch Logs on an existing Ubuntu Server, CentOS, or Red

Hat instance

If you're using an AMI running Ubuntu Server, CentOS, or Red Hat, use the
following procedure to manually install the CloudWatch Logs agent on your instance.

1. Connect to your EC2 instance. For more information, see [Connect to Your
   Instance](../../../AWSEC2/latest/UserGuide/ec2-connect-to-instance-linux.md "../../../AWSEC2/latest/UserGuide/ec2-connect-to-instance-linux.md") in the _Amazon EC2 User Guide_.

For more information about connection issues, see [Troubleshooting Connecting to Your Instance](../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md "../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.md") in the
_Amazon EC2 User Guide_. 2. Run the CloudWatch Logs agent installer using one of two options. You can run it
directly from the internet, or download the files and run it
standalone.

###### Note

If you are running CentOS 6.x, Red Hat 6.x, or Ubuntu 12.04, use the steps for downloading and running the installer
standalone. Installing the CloudWatch Logs agent directly from the internet is not supported on these systems.

###### Note

On Ubuntu, run `apt-get update` before running the commands
below.

To run it directly from the internet, use the following commands and
follow the prompts:

```
curl https://s3.amazonaws.com/aws-cloudwatch/downloads/latest/awslogs-agent-setup.py -O
```

```
sudo python ./awslogs-agent-setup.py --region us-east-1
```

If the preceding command does not work, try the following:

```
sudo python3 ./awslogs-agent-setup.py --region us-east-1
```

To download and run it standalone, use the following commands and follow the prompts:

```
curl https://s3.amazonaws.com/aws-cloudwatch/downloads/latest/awslogs-agent-setup.py -O
```

```
curl https://s3.amazonaws.com/aws-cloudwatch/downloads/latest/AgentDependencies.tar.gz -O
```

```
tar xvf AgentDependencies.tar.gz -C /tmp/
```

```
sudo python ./awslogs-agent-setup.py --region us-east-1 --dependency-path /tmp/AgentDependencies
```

You can install the CloudWatch Logs agent by specifying the us-east-1, us-west-1, us-west-2, ap-south-1, ap-northeast-2,
ap-southeast-1, ap-southeast-2, ap-northeast-1, eu-central-1, eu-west-1, or sa-east-1
Regions.

###### Note

For more information about the current version and the version history of `awslogs-agent-setup`, see
[CHANGELOG.txt](https://s3.amazonaws.com/aws-cloudwatch/downloads/latest/CHANGELOG.txt "https://s3.amazonaws.com/aws-cloudwatch/downloads/latest/CHANGELOG.txt").

The CloudWatch Logs agent installer requires certain information during setup.
Before you start, you need to know which log file to monitor and its
time stamp format. You should also have the following information
ready.

| Item                        | Description                                                                                                                                                                                                    |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS access key ID           | Press Enter if using an IAM role. Otherwise, enter your AWS access key ID.                                                                                                                                     |
| AWS secret access key       | Press Enter if using an IAM role. Otherwise, enter your AWS secret access key.                                                                                                                                 |
| Default Region name         | Press Enter. The default is us-east-2. You can set this to us-east-1, us-west-1, us-west-2, ap-south-1, ap-northeast-2, ap-southeast-1, ap-southeast-2, ap-northeast-1, eu-central-1, eu-west-1, or sa-east-1. |
| Default output format       | Leave blank and press Enter.                                                                                                                                                                                   |
| Path of log file to upload  | The location of the file that contains the log data to send. The installer suggests a path for you.                                                                                                            |
| Destination Log Group name  | The name for your log group. The installer suggests a log group name for you.                                                                                                                                  |
| Destination Log Stream name | By default, this is the name of the host. The installer suggests a host name for you.                                                                                                                          |
| Timestamp format            | Specify the format of the time stamp within the specified log file. Choose custom to specify your own format.                                                                                                  |
| Initial position            | How data is uploaded. Set this to start_of_file to upload everything in the data file. Set to end_of_file to upload only newly appended data.                                                                  | After you have completed these steps, the installer asks about configuring another log file. You can run the process as many times as you like for each log file. If you have no more log files to monitor, choose **N** when prompted by the installer to set up another log. For more information about the settings in the agent configuration file, see [CloudWatch Logs agent reference](AgentReference.md "AgentReference.md"). ###### Note Configuring multiple log sources to send data to a single log stream is not supported. 3. You should see the newly created log group and log stream in the CloudWatch console after the agent has been running for a few moments. For more information, see [View log data sent to CloudWatch Logs](Working-with-log-groups-and-streams.md#ViewingLogData "Working-with-log-groups-and-streams.md#ViewingLogData"). |
