# Troubleshoot issues connecting to your Amazon EC2 Windows instance

The following information and common errors can help you troubleshoot issues when connecting to your
Windows instance.

###### Connection issues

- [Remote Desktop can't connect to the remote computer](#rdp-issues "#rdp-issues")
- [Error using the macOS RDP
  client](#troubleshoot-instance-connect-mac-rdp "#troubleshoot-instance-connect-mac-rdp")
- [RDP displays a black screen instead of the
  desktop](#rdp-black-screen "#rdp-black-screen")
- [Unable to remotely log on to an instance with a user that is not
  an administrator](#remote-failure "#remote-failure")
- [Troubleshooting Remote Desktop issues using AWS Systems Manager](#Troubleshooting-Remote-Desktop-Connection-issues-using-AWS-Systems-Manager "#Troubleshooting-Remote-Desktop-Connection-issues-using-AWS-Systems-Manager")
- [Enable Remote Desktop on an
  EC2 instance with remote registry](#troubleshooting-windows-rdp-remote-registry "#troubleshooting-windows-rdp-remote-registry")
- [I've lost my private key. How can I connect to
  my Windows instance?](#replacing-lost-key-pair-windows "#replacing-lost-key-pair-windows")

## Remote Desktop can't connect to the remote computer

Try the following to resolve issues related to connecting to your instance:

- Verify that you're using the correct public DNS hostname. (In the Amazon EC2
  console, select the instance and check **Public DNS
  (IPv4)** in the details pane.) If your instance is in a VPC and
  you do not see a public DNS name, you must enable DNS hostnames. For more
  information, see [DNS attributes for your
  VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md") in the _Amazon VPC User Guide_.
- Verify that your instance has a public IPv4 address. If not, you can
  associate an Elastic IP address with your instance. For more information,
  see [Elastic IP addresses](elastic-ip-addresses-eip.md "elastic-ip-addresses-eip.md").
- To connect to your instance using an IPv6 address, check that your local computer has an
  IPv6 address and is configured to use IPv6. For more information, see [Configure
  IPv6 on your instances](../../../vpc/latest/userguide/vpc-migrate-ipv6.md#vpc-migrate-ipv6-dhcpv6 "../../../vpc/latest/userguide/vpc-migrate-ipv6.md#vpc-migrate-ipv6-dhcpv6") in the
  _Amazon VPC User Guide_.
- Verify that your security group has a rule that allows RDP access
  on port 3389.
- If you copied the password but get the error `Your credentials did
not work`, try typing them manually when prompted. It's possible
  that you missed a character or got an extra white space character when you
  copied the password.
- Verify that the instance has passed status checks. For more information,
  see [Status checks for Amazon EC2
  instances](monitoring-system-instance-status-check.md "monitoring-system-instance-status-check.md") and [Troubleshoot Amazon EC2 Linux instances with failed status checks](TroubleshootingInstances.md "TroubleshootingInstances.md").
- Verify that the route table for the subnet has a route that sends all
  traffic destined outside the VPC to the internet gateway for the VPC. For
  more information, see [Creating a
  custom route table](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Routing "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#Add_IGW_Routing") (Internet Gateways) in the
  _Amazon VPC User Guide_.
- Verify that Windows Firewall, or other firewall software, is not blocking RDP traffic to
  the instance. We recommend that you disable Windows Firewall and control access
  to your instance using security group rules. Try one of the following options:
  - Use [AWSSupport-TroubleshootRDP](#AWSSupport-TroubleshootRDP "#AWSSupport-TroubleshootRDP") to [disable the Windows Firewall profiles using SSM Agent](#disable-firewall "#disable-firewall"). This option requires that the instance
    is configured for AWS Systems Manager.
  - Use [AWSSupport-ExecuteEC2Rescue](#AWSSupport-ExecuteEC2Rescue "#AWSSupport-ExecuteEC2Rescue").
  - Stop the instance, detach the root volume, and attach the volume to a
    temporary instance as a data volume. Connect to the temporary instance and
    bring the volume online. Load the registry hive from the data volume. Under
    `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicyStandardProfile`,
    set `EnableFirewall` to 0. Unload the registry hive and then
    bring the volume offline. Detach the volume from the temporary instance
    and attach it to the original instance as the root volume. Start the
    original instance.

- Verify that Network Level Authentication is disabled on instances that are not part of
  an Active Directory domain (use [AWSSupport-TroubleshootRDP](#AWSSupport-TroubleshootRDP "#AWSSupport-TroubleshootRDP") to [disable NLA](#disable-nla "#disable-nla")).
- Verify that the Remote Desktop Service (TermService) Startup Type is Automatic and the
  service is started (use [AWSSupport-TroubleshootRDP](#AWSSupport-TroubleshootRDP "#AWSSupport-TroubleshootRDP") to [enable and start the RDP service](#rdp-auto "#rdp-auto")).
- Verify that you are connecting to the correct Remote Desktop Protocol port, which by
  default is 3389 (use [AWSSupport-TroubleshootRDP](#AWSSupport-TroubleshootRDP "#AWSSupport-TroubleshootRDP") to [read the current RDP port](#check-rdp "#check-rdp") and [change it back to 3389](#restore-3389 "#restore-3389")).
- Verify that Remote Desktop connections are allowed on your instance (use [AWSSupport-TroubleshootRDP](#AWSSupport-TroubleshootRDP "#AWSSupport-TroubleshootRDP") to [enable Remote Desktop connections](#allow-rdp "#allow-rdp")).
- Verify that the password has not expired. If the password has expired,
  you can reset it. For more information, see [Reset the Windows administrator password for an Amazon EC2 Windows instance](ResettingAdminPassword.md "ResettingAdminPassword.md").
- If you attempt to connect using a user that you created on the instance and receive the
  error `The user cannot connect to the server due to insufficient access
privileges`, verify that you granted the user the right to log on
  locally. For more information, see [Grant a Member the Right to Logon Locally](<https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/ee957044(v%3dws.10)> "https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/ee957044(v%3dws.10)").
- If you attempt more than the maximum allowed concurrent RDP sessions,
  your session is terminated with the message `Your Remote Desktop
Services session has ended. Another user connected to the remote
computer, so your connection was lost.` By default, you are
  allowed two concurrent RDP sessions to your instance.

## Error using the macOS RDP

client

If you are connecting to a Windows Server instance using the Remote Desktop Connection
client from the Microsoft website, you may get the following error:

```
Remote Desktop Connection cannot verify the identity of the computer that you want to connect to.
```

Download the Microsoft Remote Desktop app from the Mac App Store and use the app
to connect to your instance.

## RDP displays a black screen instead of the

desktop

Try the following to resolve this issue:

- Check the console output for additional information. To get the console
  output for your instance using the Amazon EC2 console, select the instance, and
  then choose **Actions**, **Monitor and
  troubleshoot**, **Get system log**.
- Verify that you are running the latest version of your RDP client.
- Try the default settings for the RDP client.
- If you are using Remote Desktop Connection, try starting it with the
  `/admin` option as follows.

```
`mstsc /v:`instance` /admin`
```

- If the server is running a full-screen application, it might have stopped
  responding. Use Ctrl+Shift+Esc to start Windows Task Manager, and then close
  the application.
- If the server is over-utilized, it might have stopped responding. To
  monitor the instance using the Amazon EC2 console, select the instance and then
  select the **Monitoring** tab. If you need to change the
  instance type to a larger size, see [Amazon EC2 instance type changes](ec2-instance-resize.md "ec2-instance-resize.md").

## Unable to remotely log on to an instance with a user that is not

an administrator

If you are not able to remotely log on to a Windows instance with a user that is not an
administrator account, ensure that you have granted the user the right to log on
locally. See [Grant a user or group the right to log on locally to the domain controllers in the
domain](<https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee957044(v=ws.10)#grant-a-user-or-group-the-right-to-log-on-locally-to-the-domain-controllers-in-the-domain> "https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee957044(v=ws.10)#grant-a-user-or-group-the-right-to-log-on-locally-to-the-domain-controllers-in-the-domain").

## Troubleshooting Remote Desktop issues using AWS Systems Manager

You can use AWS Systems Manager to troubleshoot issues connecting to your Windows instance
using RDP.

### AWSSupport-TroubleshootRDP

The AWSSupport-TroubleshootRDP automation document allows the user to check or
modify common settings on the target instance that can impact Remote Desktop
Protocol (RDP) connections, such as the **RDP
Port**, **Network Layer Authentication
(NLA)**, and **Windows Firewall**
profiles. By default, the document reads and outputs the values of these
settings.

The AWSSupport-TroubleshootRDP automation document can be used with EC2 instances,
on-premises instances, and virtual machines (VMs) that are enabled for use with
AWS Systems Manager (managed instances). In addition, it can also be used with EC2 instances
for Windows Server that are _not_ enabled for use
with Systems Manager. For information about enabling instances for use with AWS Systems Manager, see
[Managed nodes](../../../systems-manager/latest/userguide/fleet-manager-managed-nodes.md "../../../systems-manager/latest/userguide/fleet-manager-managed-nodes.md")
in the*AWS Systems Manager User Guide*.

###### To troubleshoot using the AWSSupport-TroubleshootRDP document

1. Log in to the [Systems Manager
   Console](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Verify that you are in the same Region as the impaired instance.
3. Choose **Documents** from the left navigation pane.
4. On the **Owned by Amazon** tab, enter
   `AWSSupport-TroubleshootRDP` in the search field. When the
   `AWSSupport-TroubleshootRDP` document appears, select
   it.
5. Choose **Execute automation**.
6. For **Execution Mode**, choose **Simple
   execution**.
7. For **Input parameters**,
   **InstanceId**, enable **Show interactive instance
   picker**.
8. Choose your Amazon EC2 instance.
9. Review the [examples](#AWSSupport-TroubleshootRDP-Examples "#AWSSupport-TroubleshootRDP-Examples"), then choose **Execute**.
10. To monitor the execution progress, for **Execution
    status**, wait for the status to change from
    **Pending** to **Success**. Expand
    **Outputs** to view the results. To view the output of
    individual steps, in **Executed Steps**, choose an item
    from **Step ID.**

#### AWSSupport-TroubleshootRDP examples

The following examples show you how to accomplish common troubleshooting tasks using
AWSSupport-TroubleshootRDP. You can use either the example AWS CLI [start-automation-execution](../../../cli/latest/reference/ssm/start-automation-execution.md "../../../cli/latest/reference/ssm/start-automation-execution.md") command or the
provided link to the AWS Management Console.

###### Example: Check the current RDP status

AWS CLI:

```
aws ssm start-automation-execution --document-name "AWSSupport-TroubleshootRDP" --parameters "InstanceId=`i-1234567890abcdef0`, Action=Custom" --region `region_code`
```

AWS Systems Manager console:

```
https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootRDP?region=`region`#documentVersion=$LATEST
```

###### Example: Disable the Windows Firewall

AWS CLI:

```
aws ssm start-automation-execution --document-name "AWSSupport-TroubleshootRDP" --parameters "InstanceId=`i-1234567890abcdef0`, Action=Custom, Firewall=Disable" --region `region_code`
```

AWS Systems Manager console:

```
https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootRDP?region=`region_code`#documentVersion=$LATEST&Firewall=Disable
```

###### Example: Disable Network Level Authentication

AWS CLI:

```
aws ssm start-automation-execution --document-name "AWSSupport-TroubleshootRDP" --parameters "InstanceId=`i-1234567890abcdef0`, Action=Custom, NLASettingAction=Disable" --region `region_code`
```

AWS Systems Manager console:

```
https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootRDP?region=`region_code`#documentVersion
```

###### Example: Set RDP Service Startup Type to Automatic and start the RDP service

AWS CLI:

```
aws ssm start-automation-execution --document-name "AWSSupport-TroubleshootRDP" --parameters "InstanceId=`i-1234567890abcdef0`, Action=Custom, RDPServiceStartupType=Auto, RDPServiceAction=Start" --region `region_code`
```

AWS Systems Manager console:

```
https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootRDP?region=`region_code`#documentVersion=$LATEST&RDPServiceStartupType=Auto&RDPServiceAction=Start
```

###### Example: Restore the default RDP Port (3389)

AWS CLI:

```
aws ssm start-automation-execution --document-name "AWSSupport-TroubleshootRDP" --parameters "InstanceId=`i-1234567890abcdef0`, Action=Custom, RDPPortAction=Modify" --region `region_code`
```

AWS Systems Manager console:

```
https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootRDP?region=`region_code`#documentVersion=$LATEST&RDPPortAction=Modify
```

###### Example: Allow remote connections

AWS CLI:

```
aws ssm start-automation-execution --document-name "AWSSupport-TroubleshootRDP" --parameters "InstanceId=`i-1234567890abcdef0`, Action=Custom, RemoteConnections=Enable" --region `region_code`
```

AWS Systems Manager console:

```
https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootRDP?region=`region_code`#documentVersion=$LATEST&RemoteConnections=Enable
```

### AWSSupport-ExecuteEC2Rescue

The AWSSupport-ExecuteEC2Rescue automation document uses EC2Rescue for Windows Server
to automatically troubleshoot and restore EC2 instance connectivity and RDP
issues. For more information, see [Run the EC2Rescue tool on
unreachable instances](../../../systems-manager/latest/userguide/automation-ec2rescue.md "../../../systems-manager/latest/userguide/automation-ec2rescue.md").

The AWSSupport-ExecuteEC2Rescue automation document requires a stop and
restart of the instance. Systems Manager Automation stops the instance and creates an
Amazon Machine Image (AMI). Data stored in instance store volumes is lost.
The public IP address changes if you are not using an Elastic IP address.
For more information, see [Run the EC2Rescue tool on
unreachable instances](../../../systems-manager/latest/userguide/automation-ec2rescue.md "../../../systems-manager/latest/userguide/automation-ec2rescue.md") in the
_AWS Systems Manager User Guide_.

###### To troubleshoot using the AWSSupport-ExecuteEC2Rescue document

1. Open the [Systems Manager
   console](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Verify that you are in the same Region as the impaired Amazon EC2
   instance.
3. In the navigation panel, choose **Documents**.
4. Search for and select the `AWSSupport-ExecuteEC2Rescue` document,
   and then choose **Execute automation**.
5. In **Execution Mode**, choose **Simple execution**.
6. In the **Input parameters** section, for
   **UnreachableInstanceId**, enter the
   Amazon EC2 instance ID of the unreachable instance.
7. (Optional) For **LogDestination**, enter the Amazon Simple Storage Service
   (Amazon S3) bucket name if you want to collect operating system logs for
   troubleshooting your Amazon EC2 instance. Logs are automatically uploaded to the
   specified bucket.
8. Choose **Execute**.
9. To monitor the execution progress, in **Execution
   status**, wait for the status to change from **Pending** to **Success**. Expand **Outputs**
   to view the results. To view the output of individual steps, in
   **Executed Steps**, choose the
   **Step ID**.

## Enable Remote Desktop on an

EC2 instance with remote registry

If your unreachable instance is not managed by AWS Systems Manager Session Manager, then
you can use remote registry to enable Remote Desktop.

1. From the EC2 console, stop the unreachable instance.
2. Detach the root volume of the unreachable instance and attach it to a reachable instance in
   the same Availability Zone as a storage volume. If you don't have a reachable
   instance in the same Availability Zone, launch one. Note the device name of the root
   volume on the unreachable instance.
3. On the reachable instance, open Disk Management. You can do so by running the following
   command in the Command Prompt window.

```
`diskmgmt.msc`
```

4. Right click the newly attached volume that came from the unreachable instance, and then choose
   **Online**.
5. Open the Windows Registry Editor. You can do so by running the following command in the
   Command Prompt window.

```
`regedit`
```

6. In Registry Editor, choose **HKEY_LOCAL_MACHINE**, then select
   **File**, **Load Hive**.
7. Select the drive of the attached volume, navigate to `\Windows\System32\config\`,
   select `SYSTEM`, and then choose **Open**.
8. For **Key Name**, enter a unique name for the hive and choose
   **OK**.
9. Back up the registry hive before making any changes to the registry.
   1. In the Registry Editor console tree, select the hive that you loaded: **HKEY_LOCAL_MACHINE**\`your-key-name`.
   2. Choose **File**, **Export**.
   3. In the Export Registry File dialog box, choose the location to which you want to save the backup copy, and then type a name for the backup file in the **File name** field.
   4. Choose **Save**.

10. In Registry Editor, navigate to `HKEY_LOCAL_MACHINE\`your key
    name`\ControlSet001\Control\Terminal Server`, and then,
    in the details pane, double-click **fDenyTSConnections**.
11. In the **Edit DWORD** value box, enter `0` in the **Value data** field.
12. Choose **OK**.

###### Note

If the value in the **Value data** field is `1`, then the instance
will deny remote desktop connections. A value of `0` allows remote
desktop connections. 13. In Registry Editor, choose
**HKEY_LOCAL_MACHINE**\`your-key-name`,
then select **File**, **Unload Hive**. 14. Close Registry Editor and Disk Management. 15. From the EC2 console, detach the volume from the reachable instance and then reattach it to
the unreachable instance. When attaching the volume to the unreachable instance,
enter the device name that you saved earlier in the **device**
field. 16. Restart the unreachable instance.

## I've lost my private key. How can I connect to

my Windows instance?

When you connect to a newly-launched Windows instance, you decrypt the password for the
Administrator account using the private key for the key pair that you specified when you
launched the instance.

If you lose the Administrator password and you no longer have the private key, you must
reset the password or create a new instance. For more information, see [Reset the Windows administrator password for an Amazon EC2 Windows instance](ResettingAdminPassword.md "ResettingAdminPassword.md"). For steps
to reset the password using an Systems Manager document, see [Reset passwords and
SSH keys on EC2 instances](../../../systems-manager/latest/userguide/automation-ec2reset.md "../../../systems-manager/latest/userguide/automation-ec2reset.md") in the
_AWS Systems Manager User Guide_.
