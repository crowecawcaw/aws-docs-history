AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# SSH environment host requirements

To instruct AWS Cloud9 to connect an environment to an existing cloud compute instance or your own
 server, you create an *AWS Cloud9 SSH development environment*. However, before you create an
 SSH environment, consider the benefits of creating EC2 environments instead. 

When you create an EC2 environment, AWS Cloud9 creates a new environment, requests Amazon EC2 to launch a new
 instance, and then connects the newly launched instance to the new environment. Creating an EC2 environment
 has the following benefits:


* **Automatic instance launching.** When you create an
 EC2 environment, AWS Cloud9 requests Amazon EC2 to create a new instance at the same time. In an
 SSH environment, you must provide an existing cloud compute instance (for example, an Amazon EC2
 instance) or your own server yourself.
* **Automatic instance shutdown.** By default, AWS Cloud9
 automatically shuts down the EC2 environment 30 minutes after all web browser instances that
 are connected to the IDE for the EC2 environment are closed. You can change this behavior at
 any time. This helps reduce the possibility of having additional charges applied to your
 AWS account for using Amazon EC2.
* **Automatic instance cleanup.** When you delete an
 EC2 environment, the connected Amazon EC2 instance is automatically deleted. This also helps reduce
 the possibility of additional charges applied to your AWS account for using Amazon EC2. In
 an SSH environment that's connected to a cloud compute instance, you must remember to delete
 the instance yourself.
* **AWS managed temporary credentials.** For an EC2 environment, you can easily turn
 on or off all AWS actions for all AWS resources in the caller's AWS account (with
 some restrictions). You can don't need to configure instance profiles for your
 environment's Amazon EC2 instance or store permanent AWS access credentials of an AWS
 entity (for example, an IAM user).


For more information, see [AWS managed temporary credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials "security-iam.md#auth-and-access-control-temporary-managed-credentials").
* **AWS Toolkit and Git panel.** These tools for interacting
 with AWS services and using visual source control are available only in AWS Cloud9
 environments that are created with an Amazon EC2 instance.
If you want to create an EC2 environment instead, see [Creating an EC2 Environment](create-environment-main.md "create-environment-main.md"). Otherwise, continue reading for information
 about creating SSH environments.


## When and how to create an
 SSH Environment


You must create an SSH environment instead of an EC2 environment whenever you have any of the
 following requirements:




| **Requirement** | **Directions** |
| --- | --- |
| You don't want to incur additional charges to your AWS account for using AWS Cloud compute instances. So, you decide to connect AWS Cloud9 to an existing cloud compute instance outside of AWS or your own server instead. | 1. Make sure your instance or server meets the [requirements](#ssh-settings-requirements "#ssh-settings-requirements") that are described later in this topic. 2. [Create an SSH environment](create-environment.md "create-environment.md") for AWS Cloud9 to connect your instance or server to. |
| You want to use an existing AWS cloud compute instance (for example, an Amazon EC2 instance) in your AWS account instead of having AWS Cloud9 to launch a new instance at the same time the environment is created. | 1. Make sure the instance meets the [requirements](#ssh-settings-requirements "#ssh-settings-requirements") that are described later in this topic. 2. [Create an SSH environment](create-environment.md "create-environment.md") for AWS Cloud9 to connect the instance to. |
| You want to use an Amazon EC2 instance type that AWS Cloud9 currently doesn't support for an EC2 environment (for example, R4). | 1. [Launch an Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html") based on your desired instance type. Or, identify an existing instance in your AWS account that runs the desired instance type. 2. Make sure the instance meets the [requirements](#ssh-settings-requirements "#ssh-settings-requirements") that are described later in this topic. 3. [Create an SSH environment](create-environment.md "create-environment.md") for AWS Cloud9 to connect the instance to. |
| You want to use an Amazon EC2 instance that's based on an Amazon Machine Image (AMI) other than Amazon Linux or Ubuntu Server. | 1. [Launch an Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html") based on your desired AMI. Or, identify an existing instance in your AWS account that's based on your desired AMI. 2. Make sure the instance meets the [requirements](#ssh-settings-requirements "#ssh-settings-requirements") that are described later in this topic. 3. [Create an SSH environment](create-environment.md "create-environment.md") for AWS Cloud9 to connect the instance to. |
| You want to connect multiple environments to a single existing cloud compute instance or your own server. | 1. Make sure the instance or server meets the [requirements](#ssh-settings-requirements "#ssh-settings-requirements") that are described later in this topic. 2. [Create an SSH environment](create-environment.md "create-environment.md") for each environment you want AWS Cloud9 to connect the instance or server to. | ###### Note Launching an Amazon EC2 instance might result in possible charges to your AWS account for Amazon EC2. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/"). ## SSH host requirements The existing cloud compute instance or your own server must meet the following requirements for AWS Cloud9 to connect it to an SSH environment. <br>• It must run Linux. (AWS Cloud9 doesn't support Windows.) <br>• It must *not* use an Arm-based architecture. (Support for systems built around Arm processors is under review.) <br>• It must be reachable over the public internet by using SSH. If it's reachable only through a virtual private cloud (VPC) or virtual private network (VPN), that VPC or VPN must have access to the public internet. <br>• If the host is an existing AWS Cloud compute instance that's part of an Amazon Virtual Private Cloud (Amazon VPC), there are additional requirements. For more information, see [Amazon VPC Settings](vpc-settings.md "vpc-settings.md"). <br>• It must have Python3 installed and set as the default Python version and pip3 when installing AWS Cloud9. To check the version, from the terminal of an existing instance or your server, run the command **`python --version`**. To install Python on the instance or server, see one of the following resources: + [Step 1: Install Required Tools](sample-python.md#sample-python-install "sample-python.md#sample-python-install") in the *Python Sample*. + [Download Python](https://www.python.org/downloads/ "https://www.python.org/downloads/") from the Python website. ###### Note To connect to an existing AWS Cloud compute instance to verify and meet requirements, see one or more of the following resources: + For Amazon EC2, see [Connect to Your Linux Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html") in the *Amazon EC2 User Guide*. + For Amazon Lightsail, see [Connect to your Linux/Unix-based Lightsail instance](https://docs.aws.amazon.com/en_us/lightsail/latest/userguide/lightsail-how-to-connect-to-your-instance-virtual-private-server.html "https://docs.aws.amazon.com/en_us/lightsail/latest/userguide/lightsail-how-to-connect-to-your-instance-virtual-private-server.html") in the *Amazon Lightsail Documentation*. + For AWS Elastic Beanstalk, see [Listing and Connecting to Server Instances](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.ec2connect.html "https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.ec2connect.html") in the *AWS Elastic Beanstalk Developer Guide*. + For AWS OpsWorks, see [Using SSH to Log In to a Linux Instance](https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-ssh.html "https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-ssh.html") in the *AWS OpsWorks User Guide*. + For other AWS services, see the service's [documentation](https://aws.amazon.com/documentation/ "https://aws.amazon.com/documentation/").To connect to your own server to verify and meet requirements, search the internet using a phrase such as "connect to a server by using the SSH command" (from macOS or Linux) or "connect to a server by using PuTTY" (from Windows). <br>• Run the following command to install all required packages. For Amazon Linux: ``` sudo yum install -y make glibc-devel gcc gcc-c++ ``` For Ubuntu Server: ``` sudo apt install build-essential ``` <br>• It must have Node.js installed. We recommend installing the latest Node.js version supported by the host's operating system. ###### Warning AWS Cloud9 installation problems might occur when creating an SSH environment if you use a Node.js version that's not supported by AWS Cloud9. To check your version, from the terminal of the existing instance or your server, run the command **`node --version`**. To install Node.js on the instance or server, see one of the following resources: + [Step 1: Install required tools](sample-nodejs.md#sample-nodejs-install "sample-nodejs.md#sample-nodejs-install") in the *Node.js Sample*. + [Installing Node.js via package manager](https://nodejs.org/en/download/package-manager/ "https://nodejs.org/en/download/package-manager/") on the Node.js website. + [Node Version Manager](https://github.com/nvm-sh/nvm/blob/master/README.md "https://github.com/nvm-sh/nvm/blob/master/README.md") on GitHub. <br>• The path to the directory on the existing instance or server that you want AWS Cloud9 to start from after login must have its access permissions set to `rwxr-xr-x`. This means that read-write-run permissions for the owner that corresponds to the login name that you specify in the [create environment wizard](create-environment-ssh.md "create-environment-ssh.md") for **User** on the **Configure settings** page, read-run permissions for the group that this owner belongs to, and read-run permissions for others. For example, if the directory's path is `~` (where `~` represents the home directory for the login name that you specify for **User** on the **Configure settings** page), you can set these permissions on the directory by running the **`chmod`** command on the instance or server using the following command and instructions that follow. ``` sudo chmod u=rwx,g=rx,o=rx ~ ``` <br>• [Download and run the AWS Cloud9 Installer](installer.md#installer-download-run "installer.md#installer-download-run") on the existing instance or server. <br>• Optionally, you can restrict inbound traffic over SSH to only the IP addresses that AWS Cloud9 uses. To do this, set inbound SSH traffic to the IP ranges as described in [Inbound SSH IP address ranges for AWS Cloud9](ip-ranges.md "ip-ranges.md"). After you're sure your instance or server meets the preceding requirements, [create an SSH environment](create-environment-ssh.md "create-environment-ssh.md") for AWS Cloud9 to connect it to.
