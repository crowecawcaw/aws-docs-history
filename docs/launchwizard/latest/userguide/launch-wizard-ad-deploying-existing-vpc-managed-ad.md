# Deploy

AWS Directory Service for Microsoft Active Directory to an existing VPC

The following steps guide you through an Active Directory deployment with AWS Launch Wizard
after you have launched it from the console for an existing virtual private cloud
(VPC).

1. On the Launch Wizard Console's landing page, use the **Choose
   application** button. This opens the Choose application wizard
   where you are prompted to select the type of application that you want to
   deploy.
2. Select **Active Directory**, select **Deploy
   AWS Managed Microsoft AD into an existing VPC**, then select **Create
   deployment.**
3. Review and acknowledge the required IAM permissions are met before
   proceeding. For more information, see [Identity and Access Management for
   AWS Launch Wizard](launch-wizard-security.md#identity-access-management "launch-wizard-security.md#identity-access-management").
4. You are prompted to enter the specifications for the new deployment. The
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

Network Configuration

| Parameter label (name)                    | Default value        | Description                                                               |
| ----------------------------------------- | -------------------- | ------------------------------------------------------------------------- |
| VPC CIDR (VPCCIDR)                        | 10.0.0.0/16          | CIDR Block for the VPC.                                                   |
| VPC ID (VPCID)                            | **_Requires input_** | ID of the VPC (for example,<br>vpc-abcd0123).                             |
| Create a DHCP options set (DHCPOptionSet) | Yes                  | Creates and associates a new DHCP Options Set to<br>your VPC.             |
| Subnet 1 ID (PrivateSubnet1ID)            | **_Requires input_** | ID of subnet 1 in Availability Zone 1 (for<br>example, subnet-abcd0123).  |
| Subnet 2 ID (PrivateSubnet2ID)            | **_Requires input_** | ID of subnet 2 in Availability Zone 2 (for<br>example, subnet-01234abcd). |

AWS Managed Microsoft AD configuration

| Parameter label (name)                          | Default value        | Description                                                                                                                   |
| ----------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Domain DNS name (DomainDNSName)                 | example.com          | Fully qualified domain name (FQDN) of the forest<br>root domain. For example, example.com.                                    |
| Domain NetBIOS name (DomainNetBIOSName)         | example              | NetBIOS name of the domain (Between 1 to 15<br>characters) for users of earlier versions of<br>Windows. For example, EXAMPLE. |
| Admin account password<br>(DomainAdminPassword) | **_Requires input_** | Password for the Admin account. Must be at least<br>8 characters containing letters, numbers and<br>symbols.                  |
| AWS Managed Microsoft AD edition (ADEdition)    | Enterprise           | The AWS Managed Microsoft AD Edition you wish to<br>deploy.                                                                   |

Management instance

| Parameter label (name)                                               | Default value                                                         | Description                                                                                   |
| -------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Deploy management server (MgmtServer)                                | TRUE                                                                  | Deploys an EC2 instance to act as a management<br>server.                                     |
| Management Server SSM Parameter Value for latest<br>AMI ID (MgmtAmi) | /aws/service/ami-windows-latest/Windows_Server-2022-English-Full-Base | Management Server SSM Parameter Value to grab the<br>latest AMI ID.                           |
| Data drive size (MgmtDataDriveSizeGiB)                               | 2                                                                     | Size of the management server data drive in<br>GiB.                                           |
| Management server NetBIOS name<br>(MgmtServerNetBIOSName)            | MGMT1                                                                 | NetBIOS name of the Management Server server<br>(between 1-15 characters).                    |
| Key pair name (KeyPairName)                                          | **_Requires input_**                                                  | Public/private key pairs allow you to securely<br>connect to your instance after it launches. |

Microsoft Active Directory Certificate Services
configuration

| Parameter label (name)                                                                                   | Default value                                                         | Description                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Certificate authority (CA) deployment type<br>(PKI)                                                      | No                                                                    | Deploy two-tier (Offline Root with Subordinate<br>Enterprise CA) or one-tier (Enterprise Root CA) PKI<br>Infrastructure.                                                         |
| CA AMI ID (CaAmi)                                                                                        | /aws/service/ami-windows-latest/Windows_Server-2022-English-Full-Base | The Systems Manager Parameter Store value used to provision<br>the enterprise root CA.                                                                                           |
| CA data drive size (CaDataDriveSizeGiB)                                                                  | 2                                                                     | Size of the data drive in GiB for the CA<br>instance(s).                                                                                                                         |
| Offline root CA NetBIOS name (Only Used For<br>two-tier PKI) (OrCaServerNetBIOSName)                     | ORCA1                                                                 | NetBIOS name of the offline root CA server, used<br>only for two-tier PKI (between 1-15<br>characters).                                                                          |
| Enterprise root or subordinate CA NetBIOS name<br>(EntCaServerNetBIOSName)                               | ENTCA1                                                                | NetBIOS name of the enterprise root (one-tier) or<br>subordinate CA server (two-tier). The value must be<br>1-15 characters.                                                     |
| CA key length (CaKeyLength)                                                                              | 2048                                                                  | CA(s) cryptographic provider key length.                                                                                                                                         |
| CA hash algorithm (CaHashAlgorithm)                                                                      | SHA256                                                                | CA(s) hash algorithm for signing<br>certificates.                                                                                                                                |
| Offline root CA certificate validity period (only<br>used for two-tier PKI)<br>(OrCaValidityPeriodUnits) | 10                                                                    | Validity period in years for the offline root CA<br>certificate (used only for two-tier PKI).                                                                                    |
| Enterprise root or subordinate CA certificate<br>validity period (CaValidityPeriodUnits)                 | 5                                                                     | Validity period in years for the enterprise root<br>or subordinate CA certificate.                                                                                               |
| Use S3 for CA CRL location (UseS3ForCRL)                                                                 | No                                                                    | Store CA CRL(s) in an S3 bucket.                                                                                                                                                 |
| CA CRL S3 bucket name (S3CRLBucketName)                                                                  | examplebucket                                                         | S3 bucket name for CA CRL(s) storage. Bucket name<br>can include numbers, lowercase letters, uppercase<br>letters, and hyphens (-). It cannot start or end<br>with a hyphen (-). |

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
