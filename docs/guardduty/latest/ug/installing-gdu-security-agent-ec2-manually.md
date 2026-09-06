

# Installing the security agent manually
<a name="installing-gdu-security-agent-ec2-manually"></a>

GuardDuty provides the following two methods to install the GuardDuty security agent on your Amazon EC2 instances. Before proceeding, make sure to follow the steps under [Prerequisite – Creating Amazon VPC endpoint manually](creating-vpc-endpoint-ec2-agent-manually.md).

Choose a preferred access method to install the security agent in your Amazon EC2 resources.
+ [Method 1 - Using AWS Systems Manager](#install-gdu-by-using-sys-runtime-monitoring) – This method requires your Amazon EC2 instance to be AWS Systems Manager managed.
+ [Method 2 - Using Linux Package Managers](#install-gdu-by-rpm-scripts-runtime-monitoring) – You can use this method whether or not your Amazon EC2 instances are AWS Systems Manager managed. Based on your [OS distributions](https://docs.aws.amazon.com/guardduty/latest/ug/prereq-runtime-monitoring-ec2-support.html#validating-architecture-req-ec2), you can choose an appropriate method to install either RPM scripts or Debian scripts. If you use *Fedora* platform, then you must use this method to install the agent.

## Method 1 - Using AWS Systems Manager
<a name="install-gdu-by-using-sys-runtime-monitoring"></a>

To use this method, make sure that your Amazon EC2 instances are AWS Systems Manager managed and then install the agent.

### AWS Systems Manager managed Amazon EC2 instance
<a name="manage-ssm-ec2-instance-runtime-monitoring"></a>

Use the following steps to make your Amazon EC2 instances AWS Systems Manager managed.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) helps you manage your AWS applications and resources end-to-end and enable secure operations at scale. 

  To manage your Amazon EC2 instances with AWS Systems Manager, see [Setting up Systems Manager for Amazon EC2 instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-ec2.html) in the *AWS Systems Manager User Guide*.
+ The following table shows the new GuardDuty managed AWS Systems Manager documents:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/installing-gdu-security-agent-ec2-manually.html)

  For more information about AWS Systems Manager, see [Amazon EC2 Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents.html) in the *AWS Systems Manager User Guide*.
**For Debian Servers**  
The Amazon Machine Images (AMIs) for Debian Server provided by AWS require you to install the AWS Systems Manager agent (SSM agent). You will need to perform an additional step to install the SSM agent to make your Amazon EC2 Debian Server instances SSM managed. For information about steps that you need to take, see [Manually installing SSM agent on Debian Server instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-deb.html) in the *AWS Systems Manager User Guide*.

**To install the GuardDuty agent for Amazon EC2 instance by using AWS Systems Manager**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Documents**

1. In **Owned by Amazon**, choose `AmazonGuardDuty-ConfigureRuntimeMonitoringSsmPlugin`.

1. Choose **Run Command**.

1. Enter the following Run Command parameters
   + Action: Choose **Install**.
   + Installation Type: Choose **Install or Uninstall.**
   + Name: `AmazonGuardDuty-RuntimeMonitoringSsmPlugin`
   + Version: If this remains empty, you'll get latest version of the GuardDuty security agent. For more information about the release versions, [GuardDuty security agent versions for Amazon EC2 instances](runtime-monitoring-agent-release-history.md#ec2-gdu-agent-release-history).

1. Select the targeted Amazon EC2 instance. You can select one or more Amazon EC2 instances. For more information, see [AWS Systems Manager Running commands from the console](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-commands-console.html) in the *AWS Systems Manager User Guide* 

1. Validate if the GuardDuty agent installation is healthy. For more information, see [Validating GuardDuty security agent installation status](#validate-ec2-gdu-agent-installation-healthy).

## Method 2 - Using Linux Package Managers
<a name="install-gdu-by-rpm-scripts-runtime-monitoring"></a>

With this method, you can install the GuardDuty security agent by running RPM scripts or Debian scripts. Based on the operating systems, you can choose a preferred method:
+ Use RPM scripts to install the security agent on OS distributions AL2, AL2023, RedHat, CentOS, or Fedora.
+ Use Debian scripts to install the security agent on OS distributions Ubuntu or Debian. For information about supported Ubuntu and Debian OS distributions, see [Validate architectural requirements](prereq-runtime-monitoring-ec2-support.md#validating-architecture-req-ec2).

------
#### [ RPM installation ]
**Important**  
We recommend verifying the GuardDuty security agent RPM signature before installing it on your machine. 

1. Verify the GuardDuty security agent RPM signature

   1. 

**Prepare the template**

      Prepare the commands with appropriate public key, signature of x86\_64 RPM, signature of arm64 RPM, and the corresponding access link to the RPM scripts hosted in Amazon S3 buckets. Replace the value of the AWS Region, AWS account ID, and the GuardDuty agent version to access the RPM scripts.
      + **Public key**: 

        ```
        s3://{{694911143906}}-{{eu-west-1}}-guardduty-agent-rpm-artifacts/{{1.16.0}}/publickey.pem
        ```
      + **GuardDuty security agent RPM signature**:  
Signature of x86\_64 RPM  

        ```
        s3://{{694911143906}}-{{eu-west-1}}-guardduty-agent-rpm-artifacts/{{1.16.0}}/x86_64/amazon-guardduty-agent-{{1.16.0}}.x86_64.sig
        ```  
Signature of arm64 RPM  

        ```
        s3://{{694911143906}}-{{eu-west-1}}-guardduty-agent-rpm-artifacts/{{1.16.0}}/arm64/amazon-guardduty-agent-{{1.16.0}}.arm64.sig
        ```
      + **Access links to the RPM scripts in Amazon S3 bucket**:  
Access link for x86\_64 RPM  

        ```
        s3://{{694911143906}}-{{eu-west-1}}-guardduty-agent-rpm-artifacts/{{1.16.0}}/x86_64/amazon-guardduty-agent-{{1.16.0}}.x86_64.rpm
        ```  
Access link for arm64 RPM  

        ```
        s3://{{694911143906}}-{{eu-west-1}}-guardduty-agent-rpm-artifacts/{{1.16.0}}/arm64/amazon-guardduty-agent-{{1.16.0}}.arm64.rpm
        ```    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/installing-gdu-security-agent-ec2-manually.html)

   1. 

**Download the template**

      In the following command to download appropriate public key, signature of x86\_64 RPM, signature of arm64 RPM, and the corresponding access link to the RPM scripts hosted in Amazon S3 buckets, make sure to replace the account ID with the appropriate AWS account ID and the Region with your current Region. 

      ```
      aws s3 cp s3://{{694911143906}}-{{eu-west-1}}-guardduty-agent-rpm-artifacts/{{1.16.0}}/x86_64/amazon-guardduty-agent-{{1.16.0}}.x86_64.rpm ./amazon-guardduty-agent-{{1.16.0}}.x86_64.rpm
      aws s3 cp s3://{{694911143906}}-{{eu-west-1}}-guardduty-agent-rpm-artifacts/{{1.16.0}}/x86_64/amazon-guardduty-agent-{{1.16.0}}.x86_64.sig ./amazon-guardduty-agent-{{1.16.0}}.x86_64.sig
      aws s3 cp s3://{{694911143906}}-{{eu-west-1}}-guardduty-agent-rpm-artifacts/{{1.16.0}}/publickey.pem ./publickey.pem
      ```

   1. 

**Import the public key**

      Use the following command to import the public key to the database:

      ```
      gpg --import publickey.pem
      ```

      gpg shows import successfully

      ```
      gpg: key 093FF49D: public key "AwsGuardDuty" imported
      gpg: Total number processed: 1
      gpg:               imported: 1  (RSA: 1)
      ```

   1. 

**Verify the signature**

      Use the following command to verify the signature

      ```
      gpg --verify amazon-guardduty-agent-{{1.16.0}}.x86_64.sig amazon-guardduty-agent-{{1.16.0}}.x86_64.rpm
      ```

      If verification passes, you will see a message similar to the result below. You can now proceed to install the GuardDuty security agent using RPM.

      Example output:

      ```
      gpg: Signature made Fri 17 Nov 2023 07:58:11 PM UTC using ? key ID 093FF49D
      gpg: Good signature from "AwsGuardDuty"
      gpg: WARNING: This key is not certified with a trusted signature!
      gpg:          There is no indication that the signature belongs to the owner.
      Primary key fingerprint: 7478 91EF 5378 1334 4456  7603 06C9 06A7 093F F49D
      ```

      If verification fails, it means the signature on RPM has been potentially tampered. You must remove the public key from the database and retry the verification process.

      Example: 

      ```
      gpg: Signature made Fri 17 Nov 2023 07:58:11 PM UTC using ? key ID 093FF49D
      gpg: BAD signature from "AwsGuardDuty"
      ```

      Use the following command to remove the public key from the database:

      ```
      gpg --delete-keys AwsGuardDuty
      ```

      Now, try the verification process again.

1. [Connect with SSH from Linux or macOS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html).

1. Install the GuardDuty security agent by using the following command:

   ```
   sudo rpm -ivh amazon-guardduty-agent-{{1.16.0}}.x86_64.rpm
   ```

1. Validate if the GuardDuty agent installation is healthy. For more information about the steps, see [Validating GuardDuty security agent installation status](#validate-ec2-gdu-agent-installation-healthy).

------
#### [ Debian installation ]
**Important**  
We recommend verifying the GuardDuty security agent Debian signature before installing it on your machine. 

1. Verify the GuardDuty security agent Debian signature

   1. 

**Prepare templates for the appropriate public key, signature of amd64 Debian package, signature of arm64 Debian package, and the corresponding access link to the Debian scripts hosted in Amazon S3 buckets**

      In the following templates, replace the value of the AWS Region, AWS account ID, and the GuardDuty agent version to access the Debian package scripts. 
      + **Public key**: 

        ```
        s3://{{694911143906}}-{{eu-west-1}}-guardduty-agent-deb-artifacts/{{1.16.0}}/publickey.pem
        ```
      + **GuardDuty security agent Debian signature**:  
Signature of amd64  

        ```
        s3://{{694911143906}}-{{eu-west-1}}-guardduty-agent-deb-artifacts/{{1.16.0}}/amd64/amazon-guardduty-agent-{{1.16.0}}.amd64.sig
        ```  
Signature of arm64  

        ```
        s3://{{694911143906}}-{{eu-west-1}}-guardduty-agent-deb-artifacts/{{1.16.0}}/arm64/amazon-guardduty-agent-{{1.16.0}}.arm64.sig
        ```
      + **Access links to the Debian scripts in Amazon S3 bucket**:  
Access link for amd64  

        ```
        s3://{{694911143906}}-{{eu-west-1}}-guardduty-agent-deb-artifacts/{{1.16.0}}/amd64/amazon-guardduty-agent-{{1.16.0}}.amd64.deb
        ```  
Access link for arm64  

        ```
        s3://{{694911143906}}-{{eu-west-1}}-guardduty-agent-deb-artifacts/{{1.16.0}}/arm64/amazon-guardduty-agent-{{1.16.0}}.arm64.deb
        ```    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/installing-gdu-security-agent-ec2-manually.html)

   1. 

**Download the appropriate public key, signature of amd64, signature of arm64, and the corresponding access link to the Debian scripts hosted in Amazon S3 buckets**

      In the following commands, replace the account ID with the appropriate AWS account ID, and the Region with your current Region. 

      ```
      aws s3 cp s3://{{694911143906}}-{{eu-west-1}}-guardduty-agent-deb-artifacts/{{1.16.0}}/amd64/amazon-guardduty-agent-{{1.16.0}}.amd64.deb ./amazon-guardduty-agent-{{1.16.0}}.amd64.deb
      aws s3 cp s3://{{694911143906}}-{{eu-west-1}}-guardduty-agent-deb-artifacts/{{1.16.0}}/amd64/amazon-guardduty-agent-{{1.16.0}}.amd64.sig ./amazon-guardduty-agent-{{1.16.0}}.amd64.sig
      aws s3 cp s3://{{694911143906}}-{{eu-west-1}}-guardduty-agent-deb-artifacts/{{1.16.0}}/publickey.pem ./publickey.pem
      ```

   1. Import the public key to the database

      ```
      gpg --import publickey.pem
      ```

      gpg shows import successfully

      ```
      gpg: key 093FF49D: public key "AwsGuardDuty" imported
      gpg: Total number processed: 1
      gpg:               imported: 1  (RSA: 1)
      ```

   1. Verify the signature

      ```
      gpg --verify amazon-guardduty-agent-{{1.16.0}}.amd64.sig amazon-guardduty-agent-{{1.16.0}}.amd64.deb
      ```

      After a successful verification, you will see a message similar to the following result:

      Example output:

      ```
      gpg: Signature made Fri 17 Nov 2023 07:58:11 PM UTC using ? key ID 093FF49D
      gpg: Good signature from "AwsGuardDuty"
      gpg: WARNING: This key is not certified with a trusted signature!
      gpg:          There is no indication that the signature belongs to the owner.
      Primary key fingerprint: 7478 91EF 5378 1334 4456  7603 06C9 06A7 093F F49D
      ```

      You can now proceed to install the GuardDuty security agent using Debian.

      However, if verification fails, it means the signature in Debian package has been potentially tampered. 

      Example: 

      ```
      gpg: Signature made Fri 17 Nov 2023 07:58:11 PM UTC using ? key ID 093FF49D
      gpg: BAD signature from "AwsGuardDuty"
      ```

      Use the following command to remove the public key from the database:

      ```
      gpg --delete-keys AwsGuardDuty
      ```

      Now, retry the verification process.

1. [Connect with SSH from Linux or macOS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html).

1. Install the GuardDuty security agent by using the following command:

   ```
   sudo dpkg -i amazon-guardduty-agent-{{1.16.0}}.amd64.deb
   ```

1. Validate if the GuardDuty agent installation is healthy. For more information about the steps, see [Validating GuardDuty security agent installation status](#validate-ec2-gdu-agent-installation-healthy).

------

## Out of memory error
<a name="out-of-memory-error-ec2-instal-agent-manual"></a>

If you experience an `out-of-memory` error while installing or updating the GuardDuty security agent for Amazon EC2 manually, see [Troubleshooting out of memory error](troubleshooting-guardduty-runtime-monitoring.md#troubleshoot-ec2-cpu-out-of-memory-error).

## Validating GuardDuty security agent installation status
<a name="validate-ec2-gdu-agent-installation-healthy"></a>

After you have performed the steps to install the GuardDuty security agent, use the following steps to validate the status of the agent:

**To validate if the GuardDuty security agent is healthy**

1. [Connect with SSH from Linux or macOS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html).

1. Run the following command to check the status of the GuardDuty security agent:

   ```
   sudo systemctl status amazon-guardduty-agent
   ```

If you want to view the security agent installation logs, they are available under `/var/log/amzn-guardduty-agent/`.

To view the logs, do `sudo journalctl -u amazon-guardduty-agent`.