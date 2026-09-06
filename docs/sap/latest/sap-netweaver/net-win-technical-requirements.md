

# Technical Requirements
<a name="net-win-technical-requirements"></a>

1. Ensure that any [service limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) are high enough and the current usage low enough to be able to launch the resources that you need. If necessary, request a service limit increase for the AWS resource that you’re planning to use. In particular:

   1. Ensure that your [EC2 service limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) are sufficient to launch the instances that you need for your SAP NetWeaver system.

   1. Ensure that your [VPC service limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_vpc) are sufficient to launch a new VPC (if necessary) or individual network resources within your VPC, such as Elastic IP addresses.

1. Gather the following information about your existing AWS resources. You will need this information to create your Amazon EC2 and Amazon EBS resources using the AWS Command Line Interface (AWS CLI) commands:  
**AWS Resource Information Required**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-technical-requirements.html)

   1. Ensure that you have a key pair that you can use to launch your Amazon EC2 instances. To import or create a new key pair, see [Amazon EC2 Key Pairs and Windows Instances](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-key-pairs.html).

   1. Ensure that you know the network details, such as VPC-ID and Subnet-ID, of the VPC where you plan to launch your Amazon EC2 instances to host your SAP NetWeaver application.

   1. Ensure that you have the required ports open on the security group attached to your Amazon EC2 instance hosting your database, to allow communication between your database and your SAP NetWeaver application. If needed, create new security groups that allow network traffic over both the database ports and the SAP NetWeaver application ports. For a list of SAP ports, see [TCP/IP Ports of All SAP Products](https://help.sap.com/viewer/ports).

1. If you plan to use the AWS Command Line Interface (AWS CLI) to launch your instances, ensure that you have installed and configured the AWS CLI with the appropriate credentials. See [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) for more details.

1. If you plan to use the AWS Management Console to launch your instances, ensure that your IAM user has permission to launch and configure Amazon EC2, Amazon EBS, etc. See the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) for more details.

1. Ensure that you have the required SAP software available either via an S3 bucket or on a file share accessible from Windows, such as Amazon FSx. For the fastest installation experience, we recommend copying the required software to an EBS volume attached to the relevant EC2 instance before running the install. This is best set up as a separate volume (mapped to a new drive in Windows) that, after completion of the installation, can then be detached and either deleted or re-attached to other EC2 instances for further installations. We recommend using the AWS CLI for this. Be sure to assign the appropriate IAM role permissions to the EC2 instance to allow S3 access.

1. If the installation type is distributed or high availability (HA), it will need to be a domain-based installation and a domain controller is required. If desired, you can use AWS Directory Service for this purpose. AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD, enables your directory-aware workloads and AWS resources to use managed Active Directory in AWS. For details, see [AWS Directory Service](https://aws.amazon.com/directoryservice/) and [Create Your AWS Managed Microsoft AD directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_create_directory.html).

   When doing a domain-based installation, `sapinst.exe` should be run by a user with domain administration privileges (but not the `<SID>adm` user) or a domain administrator must complete the appropriate preparatory steps. For more details, consult the SAP NetWeaver installation guide for your version of SAP NetWeaver.

1. To create an Amazon FSx file system, you need the following prerequisites:

   1. An AWS account with the permissions necessary to create an Amazon FSx file system and an Amazon EC2 instance. For more information, see [Setting Up](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/setting-up.html).

   1. An Amazon EC2 instance running Microsoft Windows Server in the VPC based on the Amazon VPC service that you want to associate with your Amazon FSx file system. For information on creating an EC2 Windows instance, see [Getting Started with Amazon EC2 Windows Instances](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html).

   1. Amazon FSx works with Microsoft Active Directory to perform user authentication. You join your Amazon FSx file system to an AWS Directory Service for Microsoft Active Directory. For more information, see [Create Your File System](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/getting-started.html#getting-started-step1).

   1. This guide assumes that you haven’t changed the rules on the default security group for your VPC. If you have changed them, you need to ensure that you add the necessary rules to allow network traffic from your Amazon EC2 instance to your Amazon FSx file system. For more details, see [Security](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/security.html).

   1. Install and configure the AWS Command Line Interface (AWS CLI).

For additional details on these prerequisites, see [Prerequisites for Getting Started](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/walkthrough01-prereqs.html).