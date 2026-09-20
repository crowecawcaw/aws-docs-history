

# Extend on-premises Active Directory to an existing VPC
<a name="launch-wizard-ad-deploying-existing-vpc-extend"></a>

The following steps guide you through an Active Directory deployment with AWS Launch Wizard after you have launched it from the console for an existing VPC.

1. On the Launch Wizard console's landing page, use the **Choose application** button. This opens the Choose application wizard where you are prompted to select the type of application that you want to deploy.

1. Select **Active Directory**, select **Extend on-premises AD into an existing VPC**, then select **Create deployment.**

1. Review and acknowledge that the required IAM permissions are met before proceeding. For more information, see [Identity and Access Management for AWS Launch Wizard](launch-wizard-security.md#identity-access-management).

1. When prompted, enter the specifications for the new deployment. The following tabs provide information about the specification fields of the deployment model.

------
#### [ General settings ]
   + **Deployment name**. Enter a unique application name for your deployment.
   + **Amazon Simple Notification Service (Amazon SNS) topic ARN — optional**. Specify an Amazon SNS topic where Launch Wizard can send notifications and alerts. For more information, see the [Amazon Simple Notification Service Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/welcome.html).
   + **Deactivate rollback on failed deployment**. By default, if a deployment fails, your provisioned resources will be deleted. You can enable this setting during deployment to prevent this behavior.
   + **Tags - optional**. Enter a key and value to assign metadata to your deployment. For help with tagging, see [Tagging Your Amazon EC2 Resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html).

------
#### [ Network configuration ]


<table>
<thead>
  <tr><th>Parameter label (name)</th><th>Default value</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Parameter label (name)</td><td>Default value</td><td>Description</td></tr>
  <tr><td>VPC CIDR (VPCCIDR)</td><td>10.0.0.0/16</td><td>CIDR Block for the VPC.</td></tr>
  <tr><td>VPC ID (VPCID)</td><td><b><i>Requires input</i></b></td><td>ID of the VPC (for example, vpc-abcd0123).</td></tr>
  <tr><td>Subnet 1 ID (Subnet1ID)</td><td><b><i>Requires input</i></b></td><td>ID of subnet 1 in Availability Zone 1 (for example, subnet-abcd0123).</td></tr>
  <tr><td>Subnet 2 ID (Subnet2ID)</td><td><b><i>Requires input</i></b></td><td>ID of subnet 2 in Availability Zone 2 (for example, subnet-01234abcd).</td></tr>
  <tr><td>Exiting domain controllers Security Group ID (ExistingDomainControllersSG)</td><td>sg-1234567890abcdef0</td><td>Security Group ID for existing domain controllers Security Group. (Used only when JoinAndPromote equals Yes).</td></tr>
</tbody>
</table>


------
#### [ Amazon EC2 configuration ]


<table>
<thead>
  <tr><th>Parameter label (name)</th><th>Default value</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Domain controller 1 NetBIOS name (ADServer1NetBIOSName)</td><td>DC3</td><td>NetBIOS name of the first additional Active Directory domain controller (between 1-15 characters).</td></tr>
  <tr><td>Domain controller 1 private IP address (ADServer1PrivateIP)</td><td>10.0.0.11</td><td>Fixed private IP for the first additional Active Directory domain controller located in subnet 1.</td></tr>
  <tr><td>Domain controller 2 NetBIOS name (ADServer2NetBIOSName)</td><td>DC4</td><td>NetBIOS name of the second additional Active Directory domain controller (between 1-15 characters).</td></tr>
  <tr><td>Domain controller 2 private IP address (ADServer2PrivateIP)</td><td>10.0.32.11</td><td>Fixed private IP for the second additional Active Directory domain controller located in subnet 2.</td></tr>
  <tr><td>SYSVOL and NTDS Data Drive Size (DataDriveSizeGiB)</td><td>10</td><td>Size of SYSVOL and NTDS data drive in GiB.</td></tr>
  <tr><td>KMS key for EBS Encryption (EbsEncryptionKmsKeyId)</td><td>alias/aws/ebs</td><td>The identifier of the KMS key to use for Amazon EBS encryption. You can specify the KMS key using any of the following; key ID, key alias, key ARN, alias ARN.</td></tr>
  <tr><td>Key pair name (KeyPairName)</td><td><b><i>Requires input</i></b></td><td>Public/private key pairs allow you to securely connect to your instance after it launches.</td></tr>
  <tr><td>AMI ID (LatestAmiId)</td><td>/aws/service/ami-windows-latest/Windows_Server-2022-English-Full-Base</td><td>AWS Systems Manager parameter value for latest Windows Server AMI.</td></tr>
</tbody>
</table>


------
#### [ Microsoft Active Directory Domain Services configuration ]


<table>
<thead>
  <tr><th>Parameter label (name)</th><th>Default value</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Join and Promote to domain controllers (JoinAndPromote)</td><td>No</td><td>Do you want to join and promote these instances to be Active Directory domain controllers.</td></tr>
  <tr><td>DNS Server 1 IP address (ExistingDomainController1IP)</td><td>10.0.0.10</td><td>The IP address of the first DNS server that can resolve the domain. You must have connectivity from the VPC to the DNS server.</td></tr>
  <tr><td>DNS Server 2 IP address (ExistingDomainController2IP)</td><td>10.0.32.10</td><td>The IP address of the second DNS server that can resolve the domain. You must have connectivity from the VPC to the DNS server.</td></tr>
  <tr><td>Domain DNS name (DomainDNSName)</td><td>example.com</td><td>Fully qualified domain name (FQDN) of the domain you would like to join and promote to. For example, example.com.</td></tr>
  <tr><td>Domain NetBIOS name (DomainNetBIOSName)</td><td>example</td><td>NetBIOS name of the domain (between 1 to 15 characters) you would like to join and promote to for users of earlier versions of Windows. For example, EXAMPLE.</td></tr>
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