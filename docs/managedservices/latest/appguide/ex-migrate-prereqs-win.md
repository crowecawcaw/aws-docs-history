

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Windows Prerequisites
<a name="ex-migrate-prereqs-win"></a>

Observe the requirements listed in [Migrating Workloads: Prerequisites for Linux and Windows](ex-migrate-instance-prereqs.md) and ensure the following before submitting a WIGS RFC:
+ Powershell version 3 or higher is installed.
+  [AWS EC2 Config](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/UsingConfig_Install.html) is installed on the instance with the workload that you will migrate.
+ Install the AWS drivers that support the latest generation instance types: PV, ENA, and NVMe. You can use the information in these links:
  + [Upgrading PV Drivers on Your Windows Instances](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/Upgrading_PV_drivers.html)
  + [Enhanced Networking on Windows](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/enhanced-networking.html)
  + [AWS NVMe Drivers for Windows Instances](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/aws-nvme-drivers.html)
  + [Part 3: Upgrading AWS NVMe drivers](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/migrating-latest-types.html#upgrade-nvme)
  + [Part 5: Installing the Serial Port Driver for Bare Metal Instances](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/migrating-latest-types.html#install-serial-port-bare-metal)
  + [Part 6: Updating Power Management Settings](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/migrating-latest-types.html#power-management)
+ (Optional but recommended) Disable critical Services – Set critical application services, such as databases, to disabled, but ensure that any changes are documented so they can be reverted to their original startup mode during the application verification stage.
+ (Optional but recommended) Create a Failsafe AMI from the prepared instance:
  + Use the Deployment \| Advanced stack components \| AMI \| Create
  + During creation, add a tag Key=Name, Value=APPLICATION-ID\_IngestReady
  + Wait until AMI is created before proceeding
+ Third-party software components that will conflict with AMS components have been removed:
  + Anti-virus Clients
  + Backup Clients
  +  Virtualization software (such as VM Tools or Hyper-V Integration services)

**Note**  
[ The End-of-Support Migration Program for Windows server (EMP)](https://aws.amazon.com/emp-windows-server/) includes tooling to migrate your legacy applications from Windows Server 2003, 2008, and 2008 R2 to newer, supported versions on AWS, without any refactoring.