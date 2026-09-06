

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Find AMIs with the SSM Agent preinstalled
<a name="ami-preinstalled-agent"></a>

AWS Systems Manager Agent (SSM Agent) is preinstalled on some Amazon Machine Images (AMIs) provided by AWS and trusted third-parties.

For example, when you launch an Amazon Elastic Compute Cloud (Amazon EC2) instance created from an AMI with one of the following operating systems, you'll likely find that the SSM Agent is already installed:
+ AlmaLinux
+ Amazon Linux 2
+ Amazon Linux 2 ECS-Optimized Base AMIs
+ Amazon Linux 2023 (AL2023)
+ Amazon EKS-Optimized Amazon Linux AMIs
+ macOS 13.x (Ventura), 14.x (Sonoma), and 15.x (Sequoia)
+ SUSE Linux Enterprise Server (SLES) 15.3 and later
+ Ubuntu Server 18.04, 20.04, 22.04 LTS, 24.04 LTS, 24.0, and 25.04 
+ Windows Server 2012 R2 AMIs published in November 2016 or later
+ Windows Server 2016, 2019, 2022 (excluding Nano versions), and 2025

**Note**  
The version of SSM Agent preinstalled on an AMI might not be the latest available version. As a best practice, we recommend always using the latest available version of SSM Agent on your managed nodes. For more information about automating SSM Agent updates, see [Automating updates to SSM Agent](ssm-agent-automatic-updates.md).  
SSM Agent might be preinstalled on AWS managed AMIs that aren’t on this list. This typically indicates that the operating system (OS) is not fully supported by all Systems Manager tools.  
SSM Agent might also be preinstalled on AMIs found in AWS Marketplace or in the Community AMIs repository, but AWS doesn’t support these AMIs.

## Verify the status of SSM Agent
<a name="verify-ssm-agent-status"></a>

Depending on when it was initialized, an instance created from an AMI on the preceding list might not have SSM Agent preinstalled. It's also possible that an instance has the agent preinstalled, but the agent isn't running. Therefore, we recommend that you check the status of SSM Agent before you try to use Systems Manager on an instance for the first time.

Use the following procedure to verify that SSM Agent is installed and running on an instance. If you find that the agent is not installed, you can manually install it on [Linux, ](manually-install-ssm-agent-linux.md) [macOS](manually-install-ssm-agent-macos.md), and [Windows Server](manually-install-ssm-agent-windows.md) instances. 

**To verify installation of SSM Agent on an instance**

1. After launching a new instance, wait a few minutes for it to initialize.

1. Connect to the instance using your preferred method. For example, you can use SSH to connect to Linux instances or use Remote Desktop to connect to Windows Server instances.

1. Check the status of SSM Agent by running the command for your instance's operating system type.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/systems-manager/latest/userguide/ami-preinstalled-agent.html)
**Tip**  
To view the commands for checking SSM Agent status on all operating system types supported by Systems Manager, see [Checking SSM Agent status and starting the agent](ssm-agent-status-and-restart.md).

1. Evaluate the command output to learn the status of the SSM Agent.

**Status: *Installed and running***  
In most cases, the command output indicates that the agent is installed and running.

   The following example shows that SSM Agent is installed and running on an Amazon Linux 2 instance.

   ```
   amazon-ssm-agent.service - amazon-ssm-agent
   Loaded: loaded (/usr/lib/systemd/system/amazon-ssm-agent.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2021-10-20 19:09:29 UTC; 4min 6s ago
   --truncated--
   ```

   The following example shows that SSM Agent is installed and running on a Windows Server instance.

   ```
   Status   Name               DisplayName
   ------   ----               -----------
   Running  AmazonSSMAgent     Amazon SSM Agent
   ```

**Status: *Installed but not running***  
In some cases, the command output indicates that the agent is installed but not running.

   The following example shows that SSM Agent is installed but not running on an Amazon Linux 2 instance.

   ```
   amazon-ssm-agent.service - amazon-ssm-agent
   Loaded: loaded (/usr/lib/systemd/system/amazon-ssm-agent.service; enabled; vendor preset: enabled)
   Active: inactive (dead) since Wed 2021-10-20 22:16:41 UTC; 18s ago
   --truncated--
   ```

   The following example shows that SSM Agent is installed but not running on a Windows Server instance.

   ```
   Status   Name               DisplayName
   ------   ----               -----------
   Stopped  AmazonSSMAgent     Amazon SSM Agent
   ```

   If the agent is installed but not running, you can activate it manually using the commands for your instance's operating system type.

       
[See the AWS documentation website for more details](http://docs.aws.amazon.com/systems-manager/latest/userguide/ami-preinstalled-agent.html)

**Status: *Not installed***  
In some cases, the command output indicates that the agent is not installed.

   The following example shows that SSM Agent is not installed on an Amazon Linux 2 instance.

   ```
   Unit amazon-ssm-agent.service could not be found.
   ```

   The following example shows that SSM Agent is not installed on a Windows Server instance.

   ```
   Get-Service : Cannot find any service with service name 'AmazonSSMAgent'.
   --truncated--
   ```

   If the agent isn't installed, you can install it manually using the procedure for your operating system type:
   + [Manually installing and uninstalling SSM Agent on EC2 instances for Linux](manually-install-ssm-agent-linux.md)
   + [Manually installing and uninstalling SSM Agent on EC2 instances for macOS](manually-install-ssm-agent-macos.md)
   + [Manually installing and uninstalling SSM Agent on EC2 instances for Windows Server](manually-install-ssm-agent-windows.md)