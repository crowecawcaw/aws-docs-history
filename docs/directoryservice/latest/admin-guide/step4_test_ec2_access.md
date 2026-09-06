

# Step 4: Test seamlessly joining an EC2 instance for Windows Server to a domain
<a name="step4_test_ec2_access"></a>

You can use either of the following two methods to test seamlessly joining an EC2 instance to a domain. 

## Method 1: Test domain join using the Amazon EC2 console
<a name="collapsible-section-1"></a>

Use these steps in the directory consumer account. 

1. Sign in to the AWS Management Console and open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation bar, choose the same AWS Region as the existing directory.

1. On the **EC2 Dashboard**, in the **Launch instance** section, choose **Launch instance**.

1. On the **Launch an instance** page, under the **Name and Tags** section, enter the name you would like to use for your Windows EC2 instance.

1.  (Optional) Choose **Add additional tags** to add one or more tag key-value pairs to organize, track, or control access for this EC2 instance. 

1. In the **Application and OS Image (Amazon Machine Image)** section, choose **Windows** in the **Quick Start** pane. You can change the Windows Amazon Machine Image (AMI) from the **Amazon Machine Image (AMI)** dropdown list. 

1. In the **Instance type** section, choose the instance type you would like to use from **Instance type** dropdown list.

1. In the **Key pair (login)** section, you can either choose to create a new key pair or choose from an existing key pair.

   1. To create a new key pair, choose **Create new key pair**.

   1. Enter a name for the key pair and select an option for the **Key pair type** and **Private key file format**.

   1.  To save the private key in a format that can be used with OpenSSH, choose **.pem**. To save the private key in a format that can be used with PuTTY, choose **.ppk**.

   1. Choose **create key pair**.

   1. The private key file is automatically downloaded by your browser. Save the private key file in a safe place.
**Important**  
This is the only chance for you to save the private key file.

1. On the **Launch an instance** page, under **Network settings** section, choose **Edit**. Choose the **VPC** that your directory was created in from the **VPC -* required*** dropdown list.

1. Choose one of the public subnets in your VPC from the **Subnet** dropdown list. The subnet you choose must have all external traffic routed to an internet gateway. If this is not the case, you won't be able to connect to the instance remotely.

   For more information on how to connect to a internet gateway, see [Connect to the internet using an internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) in the *Amazon VPC User Guide*.

1. Under **Auto-assign public IP**, choose **Enable**.

   For more information about public and private IP addressing, see [Amazon EC2 instance IP addressing](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/using-instance-addressing.html) in the *Amazon EC2 User Guide*.

1. For **Firewall (security groups)** settings, you can use the default settings or make changes to meet your needs. 

1. For **Configure storage** settings, you can use the default settings or make changes to meet your needs.

1. Select **Advanced details** section, choose your domain from the **Domain join directory** dropdown list.
**Note**  
After choosing the Domain join directory, you may see:   

![An error message when selecting your Domain join directory. There is an error with your existing SSM document.](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/images/SSM-Error-Message.png)

This error occurs if the EC2 launch wizard identifies an existing SSM document with unexpected properties. You can do one of the following:  
If you previously edited the SSM document and the properties are expected, choose close and proceed to launch the EC2 instance with no changes.
Select the delete the existing SSM document here link to delete the SSM document. This will allow for the creation of an SSM document with the correct properties. The SSM document will automatically be created when you launch the EC2 instance.

1. For **IAM instance profile**, you can select an existing IAM instance profile or create a new one. Select an IAM instance profile that has the AWS managed policies **AmazonSSMManagedInstanceCore** and **AmazonSSMDirectoryServiceAccess** attached to it from the **IAM instance profile** dropdown list. To create a new one, choose **Create new IAM profile** link, and then do the following: 

   1. Choose **Create role**.

   1. Under **Select trusted entity**, choose **AWS service**.

   1. Under **Use case**, choose **EC2**.

   1.  Under **Add permissions**, in the list of policies, select the **AmazonSSMManagedInstanceCore** and **AmazonSSMDirectoryServiceAccess** policies. To filter the list, type **SSM** in the search box. Choose **Next**. 
**Note**  
**AmazonSSMDirectoryServiceAccess** provides the permissions to join instances to an Active Directory managed by Directory Service. **AmazonSSMManagedInstanceCore** provides the minimum permissions necessary to use the AWS Systems Manager service. For more information about creating a role with these permissions, and for information about other permissions and policies you can assign to your IAM role, see [Create an IAM instance profile for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-profile.html) in the *AWS Systems Manager User Guide*.

   1. On the **Name, review, and create** page, enter a **Role name**. You will need this role name to attach to the EC2 instance.

   1. (Optional) You can provide a description of the IAM instance profile in the **Description** field.

   1. Choose **Create role**.

   1.  Return to **Launch an instance** page and choose the refresh icon next to the **IAM instance profile**. Your new IAM instance profile should be visible in the **IAM instance profile** dropdown list. Choose the new profile and leave the rest of the settings with their default values. 

1. Choose **Launch instance**.

## Method 2: Test domain join using AWS Systems Manager
<a name="collapsible-section-2"></a>

Use these steps in the directory consumer account. To complete this procedure, you will need some information about the directory owner account such as the Directory ID, directory name, and the DNS IP addresses.

**Prerequisites**
+ Setup AWS Systems Manager.
  + For more information about Systems Manager, see [General setup for AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setting_up_prerequisites.html).
+ Instances you wish to join the AWS Managed Microsoft Active Directory domain must have an attached IAM role containing the **AmazonSSMManagedInstanceCore** and **AmazonSSMDirectoryServiceAccess** managed policies. 
  + For more information about these managed policies and other policies you can attach to an IAM instance profile for Systems Manager, see [Create an IAM instance profile for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-profile.html) in the *AWS Systems Manager User Guide*. For information about managed policies, see [AWS Managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

For more information on using Systems Manager to join EC2 instances to a AWS Managed Microsoft Active Directory domain, see [ How do I use AWS Systems Manager to join a running EC2 Windows instance to my AWS Directory Service domain?](https://repost.aws/knowledge-center/ec2-systems-manager-dx-domain#).

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, under **Node Management**, choose **Run Command**.

1. Choose **Run command**.

1. On the **Run a command** page, search for `AWS-JoinDirectoryServiceDomain`. When it is displayed in the search results, select the `AWS-JoinDirectoryServiceDomain` option.

1. Scroll down to the **Command parameters** section. You must provide the following parameters:
**Note**  
You can locate the **Directory ID**, **directory name**, and **DNS IP addresses** by going back to the Directory Service console, selecting **Directories shared with me**, and selecting your directory. Your **Directory ID** can be found under the **Shared directory details** section. You can locate the values for **Directory name** and **DNS IP addresses** under the **Owner directory details** section.
   + For **Directory ID**, enter the name of the AWS Managed Microsoft Active Directory.
   + For **Directory Name**, enter the name of the AWS Managed Microsoft Active Directory (for the directory owner account).
   + For **DNS IP Addresses**, enter the IP addresses of the DNS servers in the AWS Managed Microsoft Active Directory (for the directory owner account).

1. For **Targets**, choose **Choose instances manually**, and then select the instances that you want to join the domain.

1. Leave the remainder of the form set to their default values, scroll down the page, and then choose **Run**.

1. The command status will change from **Pending** to **Success** once the instances have successfully joined the domain. You can view the command output by selecting the **Instance ID** of the instance that joined the domain and **View output**.

After completing either of these steps, you should now be able to join your EC2 instance to the domain. Once you do that, you can then log into your instance using a Remote Desktop Protocol (RDP) client with the credentials from your AWS Managed Microsoft AD user account.