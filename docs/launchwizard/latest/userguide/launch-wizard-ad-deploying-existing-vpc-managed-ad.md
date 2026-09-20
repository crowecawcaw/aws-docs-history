

# Deploy AWS Directory Service for Microsoft Active Directory to an existing VPC
<a name="launch-wizard-ad-deploying-existing-vpc-managed-ad"></a>

The following steps guide you through an Active Directory deployment with AWS Launch Wizard after you have launched it from the console for an existing virtual private cloud (VPC).

1. On the Launch Wizard Console's landing page, use the **Choose application** button. This opens the Choose application wizard where you are prompted to select the type of application that you want to deploy.

1. Select **Active Directory**, select **Deploy AWS Managed Microsoft AD into an existing VPC**, then select **Create deployment.**

1. Review and acknowledge the required IAM permissions are met before proceeding. For more information, see [Identity and Access Management for AWS Launch Wizard](launch-wizard-security.md#identity-access-management).

1. You are prompted to enter the specifications for the new deployment. The following tabs provide information about the specification fields of the deployment model.

------
#### [ General settings ]
   + **Deployment name**. Enter a unique application name for your deployment.
   + **Amazon Simple Notification Service (Amazon SNS) topic ARN — optional**. Specify an Amazon SNS topic where Launch Wizard can send notifications and alerts. For more information, see the [Amazon Simple Notification Service Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/welcome.html).
   + **Deactivate rollback on failed deployment**. By default, if a deployment fails, your provisioned resources will be deleted. You can enable this setting during deployment to prevent this behavior.
   + **Tags - optional**. Enter a key and value to assign metadata to your deployment. For help with tagging, see [Tagging Your Amazon EC2 Resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html).

------
#### [ Network Configuration ]


<table>
<thead>
  <tr><th>Parameter label (name)</th><th>Default value</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>VPC CIDR (VPCCIDR)</td><td>10.0.0.0/16</td><td>CIDR Block for the VPC.</td></tr>
  <tr><td>VPC ID (VPCID)</td><td><b><i>Requires input</i></b></td><td>ID of the VPC (for example, vpc-abcd0123).</td></tr>
  <tr><td>Create a DHCP options set (DHCPOptionSet)</td><td>Yes</td><td>Creates and associates a new DHCP Options Set to your VPC.</td></tr>
  <tr><td>Subnet 1 ID (PrivateSubnet1ID)</td><td><b><i>Requires input</i></b></td><td>ID of subnet 1 in Availability Zone 1 (for example, subnet-abcd0123).</td></tr>
  <tr><td>Subnet 2 ID (PrivateSubnet2ID)</td><td><b><i>Requires input</i></b></td><td>ID of subnet 2 in Availability Zone 2 (for example, subnet-01234abcd).</td></tr>
</tbody>
</table>


------
#### [ AWS Managed Microsoft AD configuration ]


<table>
<thead>
  <tr><th>Parameter label (name)</th><th>Default value</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Domain DNS name (DomainDNSName)</td><td>example.com</td><td>Fully qualified domain name (FQDN) of the forest root domain. For example, example.com.</td></tr>
  <tr><td>Domain NetBIOS name (DomainNetBIOSName)</td><td>example</td><td>NetBIOS name of the domain (Between 1 to 15 characters) for users of earlier versions of Windows. For example, EXAMPLE.</td></tr>
  <tr><td>Admin account password (DomainAdminPassword)</td><td><b><i>Requires input</i></b></td><td>Password for the Admin account. Must be at least 8 characters containing letters, numbers and symbols.</td></tr>
  <tr><td>AWS Managed Microsoft AD edition (ADEdition)</td><td>Enterprise</td><td>The AWS Managed Microsoft AD Edition you wish to deploy.</td></tr>
</tbody>
</table>


------
#### [ Management instance ]


<table>
<thead>
  <tr><th>Parameter label (name)</th><th>Default value</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Deploy management server (MgmtServer)</td><td>TRUE</td><td>Deploys an EC2 instance to act as a management server.</td></tr>
  <tr><td>Management Server SSM Parameter Value for latest AMI ID (MgmtAmi)</td><td>/aws/service/ami-windows-latest/Windows_Server-2022-English-Full-Base</td><td>Management Server SSM Parameter Value to grab the latest AMI ID.</td></tr>
  <tr><td>Data drive size (MgmtDataDriveSizeGiB)</td><td>2</td><td>Size of the management server data drive in GiB.</td></tr>
  <tr><td>Management server NetBIOS name (MgmtServerNetBIOSName)</td><td>MGMT1</td><td>NetBIOS name of the Management Server server (between 1-15 characters).</td></tr>
  <tr><td>Key pair name (KeyPairName)</td><td><b><i>Requires input</i></b></td><td>Public/private key pairs allow you to securely connect to your instance after it launches.</td></tr>
</tbody>
</table>


------
#### [ Microsoft Active Directory Certificate Services configuration ]


<table>
<thead>
  <tr><th>Parameter label (name)</th><th>Default value</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Certificate authority (CA) deployment type (PKI)</td><td>No</td><td>Deploy two-tier (Offline Root with Subordinate Enterprise CA) or one-tier (Enterprise Root CA) PKI Infrastructure.</td></tr>
  <tr><td>CA AMI ID (CaAmi)</td><td>/aws/service/ami-windows-latest/Windows_Server-2022-English-Full-Base</td><td>The Systems Manager Parameter Store value used to provision the enterprise root CA.</td></tr>
  <tr><td>CA data drive size (CaDataDriveSizeGiB)</td><td>2</td><td>Size of the data drive in GiB for the CA instance(s).</td></tr>
  <tr><td>Offline root CA NetBIOS name (Only Used For two-tier PKI) (OrCaServerNetBIOSName)</td><td>ORCA1</td><td>NetBIOS name of the offline root CA server, used only for two-tier PKI (between 1-15 characters).</td></tr>
  <tr><td>Enterprise root or subordinate CA NetBIOS name (EntCaServerNetBIOSName)</td><td>ENTCA1</td><td>NetBIOS name of the enterprise root (one-tier) or subordinate CA server (two-tier). The value must be 1-15 characters.</td></tr>
  <tr><td>CA key length (CaKeyLength)</td><td>2048</td><td>CA(s) cryptographic provider key length.</td></tr>
  <tr><td>CA hash algorithm (CaHashAlgorithm)</td><td>SHA256</td><td>CA(s) hash algorithm for signing certificates.</td></tr>
  <tr><td>Offline root CA certificate validity period (only used for two-tier PKI) (OrCaValidityPeriodUnits)</td><td>10</td><td>Validity period in years for the offline root CA certificate (used only for two-tier PKI).</td></tr>
  <tr><td>Enterprise root or subordinate CA certificate validity period (CaValidityPeriodUnits)</td><td>5</td><td>Validity period in years for the enterprise root or subordinate CA certificate.</td></tr>
  <tr><td>Use S3 for CA CRL location (UseS3ForCRL)</td><td>No</td><td>Store CA CRL(s) in an S3 bucket.</td></tr>
  <tr><td>CA CRL S3 bucket name (S3CRLBucketName)</td><td>examplebucket</td><td>S3 bucket name for CA CRL(s) storage. Bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).</td></tr>
</tbody>
</table>


------

1. When you are satisfied with your application settings, choose **Next**. If you don't want to complete the configuration, choose **Cancel**. When you choose **Cancel**, all of the selections on the specification page are lost and you are returned to the landing page. To return to the previous screen, choose **Previous**.

1. On the **Configure infrastructure settings** page, you are prompted to define the infrastructure settings for the new deployment. The following tab provides information about the input fields.

------
#### [ Storage and compute ]

   You can choose to select your instances, or to use AWS recommended resources. If you choose to use AWS recommended resources, you have the option of defining your performance needs. If you don't select either option, default values are assigned. Launch Wizard will display the estimated charges incurred to deploy the application based on suggested infrastructure and also based on static values.
   + **Based on infrastructure suggestion**. Launch Wizard displays the suggested resources for the deployment. You can specify your performance requirements of the resources to update the recommendation.
     + **Number of instance cores**. Choose the number of CPU cores for your infrastructure. The default value assigned is 4.
     + **Network performance**. Choose your preferred network performance in Gbps.
     + **Memory (GB)**. Choose the amount of RAM that you want to attach to your EC2 instances. The default value assigned is 4 GB.
     + **Recommended resources**. Launch Wizard displays the system-recommended resources based on your infrastructure selections. If you want to change the recommended resources, select different infrastructure settings.
     +  **Estimated on-demand cost to deploy additional resources**. Launch Wizard displays the estimated charges incurred to deploy the resources.
   + **Based on static values**. You can specify specific instance types for the resources used in your deployment. If you don't select either option, default values are assigned.
     + **Instance type**. You can choose your instance type from the dropdown list, or you can use AWS recommended resources.
     +  **Estimated on-demand cost to deploy additional resources**. Launch Wizard displays the estimated charges incurred to deploy the resources.

------

1. When you are satisfied with your infrastructure settings, select **Next**. If you don't want to complete the configuration, select **Cancel**. When you select **Cancel**, all of the selections on the specification page are lost and you are returned to the landing page. To go to the previous screen, select **Previous**.

1. On the **Review and deploy** page, review your configuration details. If you want to make changes, select **Previous**. To stop, select **Cancel**. When you select **Cancel**, all of the selections on the specification page are lost and you are returned to the landing page. When you choose **Deploy**, you agree to the terms of the **Acknowledgment**. Launch Wizard validates the inputs and notifies you if you need to address any issues. 

1. When validation is complete, Launch Wizard deploys your AWS resources and configures your application. Launch Wizard provides you with status updates about the progress of the deployment on the **Deployments** page. From the **Deployments** page, you can view the list of current and previous deployments. 

1. When your deployment is ready, a notification informs you that your application is successfully deployed. If you have set up an Amazon SNS notification, you are also alerted through Amazon SNS. You can manage and access all of the resources related to your application by selecting the deployment, and then selecting **Manage** from the **Actions** dropdown list. 

1. When the application is deployed, you can access your EC2 instances through the Amazon EC2 console.