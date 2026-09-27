

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Post-launch actions questions
<a name="Post-Launch-Actions-FAQ"></a>

This section contains answers to questions about post-launch actions.

**Topics**
+ [What operating systems does the post-launch actions framework support?](#What-OS-Post-Launch-Actions)
+ [What version of AWS Systems Manager Agent is installed on my instance?](#What-Version-SSM)
+ [Why is the AWS Systems Manager Agent not executing my post launch actions?](#SSM-Agent-Not-Discovered)
+ [Can I run scripts by placing them on the source server instead of using the post-launch actions framework?](#mgn-post-launch)

## What operating systems does the post-launch actions framework support?
<a name="What-OS-Post-Launch-Actions"></a>

Verify that your operating systems [are supported by AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/prereqs-operating-systems.html). 

## What version of AWS Systems Manager Agent is installed on my instance?
<a name="What-Version-SSM"></a>

AWS Transform MGN uses the latest [AWS Systems Manager Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) version available in your instance's region.

## Why is the AWS Systems Manager Agent not executing my post launch actions?
<a name="SSM-Agent-Not-Discovered"></a>
+  By default, [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/index.html) doesn't have permission to perform actions on your instances. Grant access by using an AWS Identity and Access Management (IAM) instance profile. You can create an instance profile for AWS Systems Manager by attaching one or more IAM policies that define the necessary permissions to a new role or to a role you already created. You can use the managed policy `AmazonSSMManagedInstanceCore` which allows an instance to use AWS Systems Manager service core functionality or create a custom policy. For more information, see [ Create an IAM instance profile for AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-profile.html). 
+ The instances you connect to must also allow HTTPS (port 443) outbound traffic to the following endpoints:

  ```
  ec2messages.<REGION>.amazonaws.com
  ssm.<REGION>.amazonaws.com
  ssmmessages.<REGION>.amazonaws.com
  ```

   You can connect to the required endpoints by using interface endpoints. For more information, see [Creating VPC endpoints for AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-create-vpc.html#sysman-setting-up-vpc-create). 

   Alternatively, you can use public IP addresses for communication between your instances and the internet. 
+  Another reason might be that the managed instance has limited available CPU or memory resources. Although your instance might otherwise be functional, if the instance doesn't have enough available resources, you can't establish a session. For more information, see [Troubleshooting an unreachable instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-console.html). 

## Can I run scripts by placing them on the source server instead of using the post-launch actions framework?
<a name="mgn-post-launch"></a>

Yes, but the post-launch actions framework is the recommended approach. The framework runs predefined and custom actions as AWS Systems Manager (SSM) documents that you manage from the MGN console, with configurable parameters and reuse across source servers, and it supports your own custom scripts. For most use cases, the framework is the better choice.

If you prefer not to use the SSM-based framework, MGN can also run scripts that you place in a specific folder on the source server. MGN replicates the folder to the launched test or cutover instance and runs the scripts once, after the instance boots for the first time.

To use this option, create the following folder on the source server and place the scripts within that folder.

**Linux**: /boot/post\_launch (any files that are marked as executable)

**Windows**: C:\\Program Files (x86)\\AWS Replication Agent\\post\_launch\\ (any .exe, .cmd, or .bat files)

Once you put these scripts in the above folders on the source server, the folder is replicated to the test or cutover instance and executed once after the instance boots for the first time.

**Note**  
Post-launch scripts on Windows run under the Local System context. Post-launch scripts on Linux run under the 'root' user.

### Uninstalling VMTools from Windows
<a name="mgn-post-launch-uninstall-vmtools"></a>

The following script can be used to uninstall VMTools post migration from Windows. This is a powershell script. It needs to be wrapped by a .CMD file, as powershell scripts are not run automatically by the post\_launch.

```
        $regpath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\uninstall"

        Get-childItem $regpath | % {

        $keypath = $_.pschildname

        $key = Get-Itemproperty $regpath\$keypath

        if ($key.DisplayName -match "VMware Tools") {

        $VMwareToolsGUID = $keypath

        }

        MsiExec.exe /x $VMwareToolsGUID /qn /norestart

        }
```