# SQL Server Deployment for High Availability

1. Deploy the SAP NetWeaver ASCS instance. For instructions, see the [SAP NetWeaver on AWS Deployment and Operations Guide for Windows](sap-netweaver-windows-guide.md "sap-netweaver-windows-guide.md") .
2. Create two EC2 instances for Microsoft SQL server, one in each Availability Zone. See the [Windows EC2 instances deployment](windows-ec2-instance-deployment.md "windows-ec2-instance-deployment.md") section for steps.
3. Assign two secondary IP addresses to each instance from the same subnet CIDR in which they are installed:
   1. Use one address for Windows Server Failover Cluster (WSFC).
   2. Use the second address for the Availability Group listener.

   You can assign IP addresses through the AWS Management Console, AWS Command Line Interface (AWS CLI), or AWS Tools for Windows PowerShell. For detailed working instructions, see [Multiple IP Addresses](../../../AWSEC2/latest/UserGuide/MultipleIP.md#ManageMultipleIP "../../../AWSEC2/latest/UserGuide/MultipleIP.md#ManageMultipleIP").

   For example, in the screenshot that follows, 10.100.4.53 is the primary private IP address of the EC2 instance. It has been allocated two secondary private addresses: 10.100.4.54 and 10.100.4.55.

   ![Locate the private IP addresses for your EC2 instances.](images/multiple-ip-addresses.png)

4. Domain join EC2 instances created in Step 1. If you are using AWS Managed Microsoft AD, see [AWS Directory Service documentation](../../../en_us/directoryservice/latest/admin-guide/join_windows_instance.md "../../../en_us/directoryservice/latest/admin-guide/join_windows_instance.md") for detailed steps.
5. Log in to the EC2 instance as admin, open PowerShell, and execute the following command to install the Windows Failover Clustering feature.

```
Install-WindowsFeature -Name Failover-Clustering -restart -IncludeAllSubFeature
```

###### Note

This command may force your EC2 instance to restart. Make sure you execute the command on both EC2 instances. 6. Log in as domain admin into one of the EC2 instance and execute the following command to create the Windows Server Failover Cluster. Make sure to replace the placeholders before executing the command.

```
New-Cluster -Name <ClusterName> -Node <Node1>,<Node2> -NoStorage
```

For example:

```
New-Cluster -Name SAPSQLCluster -Node primarysql,secondarysql -NoStorage
```

7. Install SQL Server on both EC2 instances. For instructions, see the [SAP installation guide](https://help.sap.com/viewer/nwguidefinder "https://help.sap.com/viewer/nwguidefinder").

Install the database instance on the primary node. Follow SAP installation guide to install Database instance on primary node. Make sure you perform domain installations and choose **Domain of Current User** or **Different Domain** as appropriate during parameter selection.

![The domain model parameter.](images/domain-installation.png) 8. Create operating system users on secondary instance.

    1. Start **sapinst**, and in the **Available Options** pane, navigate to **Generic Options >**
    **MS SQL Server >**
    **Preparations >**
    **Operating System Users and Groups**.


    ###### Note

    The navigation path can vary depending on the version of SWPM you are using.
    2. Create users and groups for this instance, as appropriate.


    ###### Note

    You do not need to create users on the primary instance because the database instance was installed on the primary node operating system.



    ![The Operating System Users and Groups option.](images/os-users-groups.png)

9. Install SAP Host agent on secondary instance with SWPM.
10. Create a SQL Server Always On availability group. See the [Microsoft documentation](https://techcommunity.microsoft.com/t5/ITOps-Talk-Blog/Step-By-Step-Creating-a-SQL-Server-Always-On-Availability-Group/ba-p/648772 "https://techcommunity.microsoft.com/t5/ITOps-Talk-Blog/Step-By-Step-Creating-a-SQL-Server-Always-On-Availability-Group/ba-p/648772") for SQL Always On availability group installation instructions.
11. Adjust the SAP profile files for parameters per the following example. Make sure to replace the `<availabilitygroup listener>` placeholder with appropriate the value for your setup. For details, refer to [SAP Note 1772688 - SQL Server Always On and SAP applications](https://launchpad.support.sap.com/#/notes/1772688 "https://launchpad.support.sap.com/#/notes/1772688").

```
dbs/mss/server = <availabilitygroup listener>;MultiSubnetFailover=yes
```

SAPDBHOST = `<availabilitygroup listener>` 12. Perform failover and failback of SQL Server to validate it is working correctly. 13. Continue with installation of primary application server (PAS) and additional application server (AAS) following the instructions in [SAP installation guides](https://help.sap.com/viewer/nwguidefinder "https://help.sap.com/viewer/nwguidefinder").
