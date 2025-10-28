# Step 2: Prepare Each EC2 Instance for SAP Installation

1. Log into the newly created RDP host in the public subnet. We will call this **jumpbox** for easy reference. Do this by either using [AWS Systems Manager Session Manager](../../../systems-manager/latest/userguide/session-manager.md "../../../systems-manager/latest/userguide/session-manager.md") (for command line tasks), or by doing the following:
   1. Go to the AWS Management Console, select the EC2 instance **jumpbox**, and choose **Connect**. Download the RDP file from the pop-up that appears.
   2. Click **Get Password** and provide your private key to decrypt the password. This is the password for the local administrator on **jumpbox**.
   3. Open the RDP file in your preferred RDP program, and connect to **jumpbox**. Log in with user Administrator and the password that you just retrieved in [step 1b](#net-win-substep-getpw "#net-win-substep-getpw").
   4. After you are logged in, go back to the AWS Management Console and repeat [step 1a](#net-win-substep-connect "#net-win-substep-connect") and [step 1b](#net-win-substep-getpw "#net-win-substep-getpw"), but specify the EC2 instance where you will install NetWeaver. We’ll call this **nw-ascs** for reference. Copy the downloaded RDP file to **jumpbox**.
   5. While logged into **jumpbox**, open the RDP file for **nw-ascs** in your preferred RDP program.

2. Log in as a user with administrator privileges but not an existing `<SID>adm` user (as per SAP’s requirements).
3. Install the AWS CLI tools or use the [AWS Tools for PowerShell](https://aws.amazon.com/powershell/ "https://aws.amazon.com/powershell/") provided with the Windows AMI.
4. Install the Java Runtime Environment (JRE) version that is compatible with your SAP installation software.
5. Install the AWS Data Provider, following the instructions for Windows in the [Installation and Operations Guide](https://s3.amazonaws.com/aws-data-provider/aws-data-provider-ig.pdf "https://s3.amazonaws.com/aws-data-provider/aws-data-provider-ig.pdf").
6. [Install and configure AWS Systems Management Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md") (SSM Agent).
