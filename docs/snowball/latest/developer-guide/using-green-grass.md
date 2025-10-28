Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Using AWS IoT Greengrass to run pre-installed software on Amazon EC2-compatible instances on Snowball Edge

AWS IoT Greengrass is an open source Internet of Things (IoT) edge runtime and cloud service that helps
you build, deploy, and manage IoT applications on your devices. You can use AWS IoT Greengrass to build
software that enables your devices to act locally on the data that they generate, run
predictions based on machine learning models, and filter and aggregate device data. For
detailed information about AWS IoT Greengrass, see [What is AWS IoT Greengrass?](../../../greengrass/v2/developerguide/what-is-iot-greengrass.md "../../../greengrass/v2/developerguide/what-is-iot-greengrass.md") in
the _AWS IoT Greengrass Version 2 Developer Guide_.

By using AWS IoT Greengrass on your Snowball Edge device, you enable the device to collect and analyze
data closer to where it is generated, react autonomously to local events, and communicate
securely with other devices on the local network.

## Setting up an Amazon EC2-compatible instance for AWS IoT Greengrass on a Snowball Edge

###### Note

To install AWS IoT Greengrass Version 2 on a Snowball Edge device, make sure that your device is connected to the
internet. After installation, the internet is not required for a Snowball Edge device
to work with AWS IoT Greengrass.

###### To set up an EC2-compatible instance for AWS IoT Greengrass V2

1. Launch the AWS IoT Greengrass validated AMI with a public IP Address and an SSH key:
   1. Using the AWS CLI: [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md").
   2. Using AWS OpsHub: [Launching an Amazon EC2-compatible instance](manage-ec2.md#launch-instance "manage-ec2.md#launch-instance").###### Note

Take note of the public IP address and SSH key name that are associated with
the instance. 2. Connect to the EC2-compatible instance using SSH. To do so, run the following command on the computer
that is connected to your device. Replace `ssh-key`
with the key you used to launch the EC2-compatible instance. Replace
`public-ip-address` with the public IP address of
the EC2-compatible instance.

```
ssh -i `ssh-key` ec2-user@ `public-ip-address`
```

###### Important

If your computer uses an earlier version of Microsoft Windows, you might
not have the SSH command, or you might have SSH but can’t connect to your
EC2-compatible instance. To connect to your EC2-compatible instance, you can install and configure
PuTTY, which is a no-cost, open source SSH client. You must convert the SSH
key from `.pem` format to PuTTY format and connect to your EC2
instance. For instructions on how to convert from `.pem` to PuTTY
format, see [Convert your private key using PuTTYgen](../../../AWSEC2/latest/UserGuide/putty.md#putty-private-key "../../../AWSEC2/latest/UserGuide/putty.md#putty-private-key") in the Amazon EC2 User Guide.

### Installing AWS IoT Greengrass on an EC2-compatible instance on a Snowball Edge

Next, you set up your EC2-compatible instance as an AWS IoT Greengrass Core device that you can use for
local development.

###### To install AWS IoT Greengrass

1. Use the following command to install the prerequisite software for AWS IoT Greengrass. This command installs
   the AWS Command Line Interface (AWS CLI) v2, Python 3, and Java 8.

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && sudo ./aws/install && sudo yum -y install python3 java-1.8.0-openjdk
```

2. Grant the root user permission to run the AWS IoT Greengrass software and modify the root permission from
   `root ALL=(ALL) ALL` to `root ALL=(ALL:ALL) ALL`
   in the sudoers config file.

```
sudo sed -in 's/root\tALL=(ALL)/root\tALL=(ALL:ALL)/' /etc/sudoers
```

3. Use the following command to download the AWS IoT Greengrass Core software.

```
curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip > greengrass-nucleus-latest.zip && unzip greengrass-nucleus-latest.zip -d GreengrassCore && rm greengrass-nucleus-latest.zip
```

4. Use the following commands to provide credentials to allow you to install AWS IoT Greengrass Core software. Replace the example values with your credentials:

```

export AWS_ACCESS_KEY_ID=`AKIAIOSFODNN7EXAMPLE`
export AWS_SECRET_ACCESS_KEY=`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`

```

###### Note

These are credentials from the IAM user in the AWS Region, not the Snowball Edge device. 5. Use the following command to install the AWS IoT Greengrass Core software. The command creates AWS resources that the core software requires to operate and sets up the core software as a system service that runs when the AMI boots up.

Replace the following parameters in the command:

    * `region`: The AWS Region in which to find or create resources.
    * `MyGreengrassCore`: The name of the AWS IoT thing for your AWS IoT Greengrass core device.
    * `MyGreengrassCoreGroup`: The name of the AWS IoT thing group for your AWS IoT Greengrass core device.

```

sudo -E java -Droot="/greengrass/v2" -Dlog.store=FILE \
    -jar ./GreengrassInstaller/lib/Greengrass.jar \
    --aws-region `region` \
    --thing-name `MyGreengrassCore` \
    --thing-group-name `MyGreengrassCoreGroup` \
    --thing-policy-name GreengrassV2IoTThingPolicy \
    --tes-role-name GreengrassV2TokenExchangeRole \
    --tes-role-alias-name GreengrassCoreTokenExchangeRoleAlias \
    --component-default-user ggc_user:ggc_group \
    --provision true \
    --setup-system-service true \
    --deploy-dev-tools true

```

###### Note

This command is for an Amazon EC2-compatible instance running an Amazon Linux 2 AMI. For a Windows AMI, see [Install the AWS IoT Greengrass Core software](../../../greengrass/v2/developerguide/install-greengrass-core-v2.md "../../../greengrass/v2/developerguide/install-greengrass-core-v2.md").

When you are finished, you will have an AWS IoT Greengrass core running on your Snowball Edge
device for your local use.
