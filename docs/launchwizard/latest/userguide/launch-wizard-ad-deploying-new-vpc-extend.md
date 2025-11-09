# Extend an existing Active

Directory to a new VPC

The following steps guide you through an Active Directory deployment with AWS Launch Wizard
after you have launched it from the console for a new VPC.

1. On the Launch Wizard Console's landing page, use the **Choose
   application** button. This opens the Choose application wizard
   where you are prompted to select the type of application that you want to
   deploy.
2. Select **Active Directory**, select **Extend
   on-premises AD into a new VPC**, then select **Create
   deployment.**
3. Review and acknowledge the required IAM permissions are met before
   proceeding. For more information, see [Identity and Access Management for
   AWS Launch Wizard](launch-wizard-security.md#identity-access-management "launch-wizard-security.md#identity-access-management").
4. On the **Configure application settings** page,
   you are prompted to enter the specifications for the new deployment. The
   following tabs provide information about the specification fields of the
   deployment model.

General settings

    * **Deployment name**.
     Enter a unique application name for your
     deployment.
    * **Amazon Simple Notification Service (Amazon SNS) topic ARN —
     optional**. Specify an Amazon SNS topic where
     Launch Wizard can send notifications and alerts. For more
     information, see the [Amazon Simple Notification Service
     Developer Guide](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md").
    * **Deactivate rollback on failed
     deployment**. By default, if a deployment
     fails, your provisioned resources will be deleted. You
     can enable this setting during deployment to prevent
     this behavior.
    * **Tags - optional**.
     Enter a key and value to assign metadata to your
     deployment. For help with tagging, see [Tagging Your Amazon EC2 Resources](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md").

Network configuration

| Parameter label (name)                                   | Default value        | Description                                                                                                                        |
| -------------------------------------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Availability zones (AvailabilityZones)                   | **_Requires input_** | List of Availability Zones (AZs) to use for the<br>subnets in the VPC.                                                             |
| Number of Availability Zones<br>(NumberOfAZs)            | 2                    | Number of Availability Zones to use in the VPC.<br>This must match your selections in the list of<br>Availability Zones parameter. |
| VPC CIDR (VPCCIDR)                                       | 10.0.0.0/16          | CIDR Block for the VPC.                                                                                                            |
| Private subnet 1 CIDR<br>(PrivateSubnet1CIDR)            | 10.0.0.0/19          | CIDR block for private subnet 1 located in<br>Availability Zone 1.                                                                 |
| Private subnet 2 CIDR<br>(PrivateSubnet2CIDR)            | 10.0.32.0/19         | CIDR block for private subnet 2 located in<br>Availability Zone 2.                                                                 |
| (Optional) Private subnet 3 CIDR<br>(PrivateSubnet3CIDR) | **_Blank string_**   | CIDR block for private subnet 3 located in<br>Availability Zone 3.                                                                 |
| Public subnet 1 CIDR (PublicSubnet1CIDR)                 | 10.0.128.0/20        | CIDR Block for the public subnet 1 located in<br>Availability Zone 1.                                                              |
| Public subnet 2 CIDR (PublicSubnet2CIDR)                 | 10.0.144.0/20        | CIDR Block for the public subnet 2 located in<br>Availability Zone 2.                                                              |
| (Optional) Public subnet 3 CIDR<br>(PublicSubnet3CIDR)   | **_Blank string_**   | CIDR Block for the public subnet 3 located in<br>Availability Zone 3.                                                              |

Amazon EC2 configuration

| Parameter label (name)                                         | Default value        | Description                                                                                               |
| -------------------------------------------------------------- | -------------------- | --------------------------------------------------------------------------------------------------------- |
| Domain controller 1 NetBIOS name<br>(ADServer1NetBIOSName)     | DC3                  | NetBIOS name of the first additional Active<br>Directory domain controller (between 1-15<br>characters).  |
| Domain controller 1 private IP address<br>(ADServer1PrivateIP) | 10.0.0.11            | Fixed private IP for the first additional Active<br>Directory domain controller located in subnet<br>1.   |
| Domain controller 2 NetBIOS name<br>(ADServer2NetBIOSName)     | DC4                  | NetBIOS name of the second additional Active<br>Directory domain controller (between 1-15<br>characters). |
| Domain controller 2 private IP address<br>(ADServer2PrivateIP) | 10.0.32.11           | Fixed private IP for the second additional Active<br>Directory domain controller located in subnet<br>2.  |
| SYSVOL and NTDS and data drive size<br>(DataDriveSizeGiB)      | 10                   | Size of SYSVOL and NTDS data drive in<br>GiB.                                                             |
| Key pair name (KeyPairName)                                    | **_Requires input_** | Public/private key pairs allow you to securely<br>connect to your instance after it launches.             |

Microsoft Active Directory Domain Services configuration

| Parameter label (name)                                   | Default value | Description                                                                                                                                                            |
| -------------------------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DNS Server 1 IP address<br>(ExistingDomainController1IP) | 10.0.0.10     | The IP address of the first DNS server that<br>can resolve the domain. You must have connectivity<br>from the VPC to the DNS server.                                   |
| DNS Server 2 IP address<br>(ExistingDomainController2IP) | 10.0.32.10    | The IP address of the second DNS server that<br>can resolve the domain. You must have connectivity<br>from the VPC to the DNS server.                                  |
| Domain DNS name (DomainDNSName)                          | example.com   | Fully qualified domain name (FQDN) of the domain<br>you would like to join and promote to. For example,<br>example.com.                                                |
| Domain NetBIOS name (DomainNetBIOSName)                  | example       | NetBIOS name of the domain (between 1 to 15<br>characters) you would like to join and promote to<br>for users of earlier versions of Windows. For<br>example, EXAMPLE. |

Microsoft Remote Desktop Gateway configuration

| Parameter label (name)                                            | Default value        | Description                                                                                                        |
| ----------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Local administrator user name (AdminUser)                         | StackAdmin           | User name for the new local administrator account<br>This is separate from the default "Administrator"<br>account. |
| Local administrator password<br>(AdminPassword)                   | **_Requires input_** | Password for the new local administrator account<br>containing letters, numbers and symbols.                       |
| Number of RDGW hosts (NumberOfRDGWHosts)                          | 1                    | Enter the number of Remote Desktop Gateway hosts<br>to create.                                                     |
| Allowed Remote Desktop Gateway external access<br>CIDR (RDGWCIDR) | **_Requires input_** | Allowed CIDR block for external access to the<br>Remote Desktop Gateways.                                          |

5. When you are satisfied with your application settings, choose
   **Next**. If you don't want to complete the
   configuration, choose **Cancel**. When you choose
   **Cancel**, all of the selections on the specification
   page are lost and you are returned to the landing page. To return to the
   previous screen, choose **Previous**.
6. On the **Configure infrastructure settings**
   page, you are prompted to define the infrastructure settings for the new
   deployment. The following tab provides information about the input
   fields.

Storage and compute
You can choose to select your instances, or to use AWS
recommended resources. If you choose to use AWS recommended
resources, you have the option of defining your performance
needs. If you don't select either option, default values
are assigned. Launch Wizard will display the estimated charges incurred
to deploy the application based on suggested infrastructure and
also based on static values.

    * **Based on infrastructure
     suggestion**. Launch Wizard displays the suggested
     resources for the deployment. You can specify your
     performance requirements of the resources to update the
     recommendation.




    	+ **Number of instance
    	 cores**. Choose the number of CPU cores
    	 for your infrastructure. The default value
    	 assigned is 4.
    	+ **Network
    	 performance**. Choose your preferred
    	 network performance in Gbps.
    	+ **Memory (GB)**.
    	 Choose the amount of RAM that you want to attach
    	 to your EC2 instances. The default value assigned
    	 is 4 GB.
    	+ **Recommended
    	 resources**. Launch Wizard displays the
    	 system-recommended resources based on your
    	 infrastructure selections. If you want to change
    	 the recommended resources, select different
    	 infrastructure settings.
    	+ **Estimated on-demand cost to
    	 deploy additional resources**. Launch Wizard
    	 displays the estimated charges incurred to deploy
    	 the resources.


    * **Based on static
     values**. You can specify specific instance
     types for the resources used in your deployment. If you
     don't select either option, default values are
     assigned.




    	+ **Instance
    	 type**. You can choose your instance type
    	 from the dropdown list, or you can use AWS
    	 recommended resources.
    	+ **Estimated on-demand cost to
    	 deploy additional resources**. Launch Wizard
    	 displays the estimated charges incurred to deploy
    	 the resources.

7. When you are satisfied with your infrastructure settings, select
   **Next**. If you don't want to complete the
   configuration, select **Cancel**. When you select
   **Cancel**, all of the selections on the specification
   page are lost and you are returned to the landing page. To go to the
   previous screen, select **Previous**.
8. On the **Review and deploy** page, review your
   configuration details. If you want to make changes, select
   **Previous**. To stop, select
   **Cancel**. When you select
   **Cancel**, all of the selections on the specification page
   are lost and you are returned to the landing page. When you choose
   **Deploy**, you agree to the terms of the **Acknowledgment**. Launch Wizard validates the inputs and
   notifies you if you need to address any issues.
9. When validation is complete, Launch Wizard deploys your AWS resources and
   configures your application. Launch Wizard provides you with status updates about the
   progress of the deployment on the **Deployments** page.
   From the **Deployments** page, you can view the list of
   current and previous deployments.
10. When your deployment is ready, a notification informs you that your
    application is successfully deployed. If you have set up an Amazon SNS
    notification, you are also alerted through Amazon SNS. You can manage and access
    all of the resources related to your application by selecting the
    deployment, and then selecting **Manage** from the
    **Actions** dropdown list.
11. When the application is deployed, you can access your EC2 instances
    through the Amazon EC2 console.
