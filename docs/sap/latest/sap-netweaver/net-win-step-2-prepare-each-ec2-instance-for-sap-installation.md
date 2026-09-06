

# Step 2: Prepare Each EC2 Instance for SAP Installation
<a name="net-win-step-2-prepare-each-ec2-instance-for-sap-installation"></a>

1. Log into the newly created RDP host in the public subnet. We will call this **jumpbox** for easy reference. Do this by either using [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) (for command line tasks), or by doing the following:

   1.  Go to the AWS Management Console, select the EC2 instance **jumpbox**, and choose **Connect**. Download the RDP file from the pop-up that appears.

   1.  Click **Get Password** and provide your private key to decrypt the password. This is the password for the local administrator on **jumpbox**.

   1. Open the RDP file in your preferred RDP program, and connect to **jumpbox**. Log in with user Administrator and the password that you just retrieved in [step 1b](#net-win-substep-getpw).

   1. After you are logged in, go back to the AWS Management Console and repeat [step 1a](#net-win-substep-connect) and [step 1b](#net-win-substep-getpw), but specify the EC2 instance where you will install NetWeaver. We’ll call this **nw-ascs** for reference. Copy the downloaded RDP file to **jumpbox**.

   1. While logged into **jumpbox**, open the RDP file for **nw-ascs** in your preferred RDP program.

1. Log in as a user with administrator privileges but not an existing `<SID>adm` user (as per SAP’s requirements).

1. Install the AWS CLI tools or use the [AWS Tools for PowerShell](https://aws.amazon.com/powershell/) provided with the Windows AMI.

1. Install the Java Runtime Environment (JRE) version that is compatible with your SAP installation software.

1. Install the AWS Data Provider, following the instructions for Windows in the [Installation and Operations Guide](https://s3.amazonaws.com/aws-data-provider/aws-data-provider-ig.pdf).

1.  [Install and configure AWS Systems Management Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) (SSM Agent).