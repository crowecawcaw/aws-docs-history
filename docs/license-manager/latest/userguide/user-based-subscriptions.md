

# Use License Manager user-based subscriptions for supported software products
<a name="user-based-subscriptions"></a>

With user-based subscriptions in AWS License Manager, you can purchase fully-compliant licensed software subscriptions. Licenses are provided by Amazon and have a per-user subscription fee. Amazon EC2 provides pre-configured Amazon Machine Images (AMIs) with the supported software, along with license-included Windows Server licenses. These licenses can be used without long-term licensing commitments.

To use user-based subscriptions, you associate users from [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) (AWS Managed Microsoft AD), or from your self-managed (on-premises) domain, with EC2 instances providing the software. To make your licensed software available, you must create user-based subscriptions and associate them with instances launched from pre-configured AMIs. [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) will configure and harden the license-included instances you launch. Users must connect with Remote Desktop software to access the instances providing the software.

Each associated user and [vCPU](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) for the license-included instances incur charges. Amazon EC2 Reserved Instances and Savings Plan pricing models can help optimize your Amazon EC2 costs. For more information, see [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html) in the *Amazon Elastic Compute Cloud User Guide*. User-based subscriptions are billed from the first half of the month to the end of the month.

**Topics**
+ [Considerations for using user-based subscriptions in License Manager](#usubs-considerations)
+ [Subscription charges in License Manager](#usubs-subscription-charges)
+ [Prerequisites to create user-based subscriptions in License Manager](#usubs-prerequisites)
+ [Supported software products for user-based subscriptions in License Manager](#usubs-software)
+ [Combine Microsoft Office with other software](#usubs-combine-products)
+ [Active Directory](#ad-support)
+ [Multiple Active Directory support for Microsoft Office](#usubs-multi-ad)
+ [Additional software](#usubs-software-additional)
+ [Get started with user-based subscriptions in License Manager](user-based-subscriptions-getting-started.md)
+ [Configure Active Directory GPO for more active remote user sessions](usubs-configure-gpo.md)
+ [Get Started with Cross-Account AWS License Manager using Shared AWS Managed Microsoft AD](license-cross-account.md)
+ [Launch an instance from a license included AMI](usubs-launch-instance.md)
+ [Connect to a user-based subscription instance with RDP](user-based-subscriptions-connect.md)
+ [Modify firewall settings for your Microsoft Office subscription](usubs-modify-firewall.md)
+ [Manage subscription users for License Manager user-based subscriptions](usubs-manage-users.md)
+ [Deregister an Active Directory from License Manager settings](usubs-deregister-ad.md)
+ [Troubleshoot user-based subscriptions in License Manager](user-based-subscriptions-troubleshoot.md)

## Considerations for using user-based subscriptions in License Manager
<a name="usubs-considerations"></a>

The following considerations apply when using user-based subscriptions with License Manager:
+ The AWS Marketplace subscription for license-included Microsoft Remote Desktop Services (`Win Remote Desktop Services SAL`) has a per user per month fee, with no proration.
+ Instances that provide user-based subscriptions support up to two active user sessions at a time by default. To enable more than two active user sessions, you can configure an Active Directory Group Policy Object (GPO), and set the Microsoft RDS licensing mode to `Per User`. For more information, see the prerequisites for [Configure Active Directory GPO for more active remote user sessions](usubs-configure-gpo.md).
+ When you create local users with administrator privileges on instances that provide user-based subscriptions, the instance health status might change to unhealthy. License Manager can terminate instances that are unhealthy for non-compliance. For more information, see [Troubleshooting instance compliance](user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-instance-compliance).
+ When you configure your Active Directory with Microsoft Office products, your VPC must have [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) provisioned in at least one subnet. If you want to remove all VPC endpoint resources created by License Manager, you must remove any Active Directory that's configured from the License Manager settings. For more information, see [Deregister an Active Directory from License Manager settings](usubs-deregister-ad.md).
+ The tag key of `AWSLicenseManager` with the value of `UserSubscriptions` assigned by License Manager to your instances must not be altered or deleted.
+ For the service to function as expected the two network interfaces created for License Manager must not be altered or deleted.
+ The objects that License Manager creates in the AWS Managed Microsoft AD directory's **AWS Reserved** organizational unit (OU) must not be altered or deleted.
+ The instances deployed for user-based subscriptions must be managed nodes with AWS Systems Manager and joined to the same domain. For information on keeping your instances managed by Systems Manager, see the [Troubleshoot user-based subscriptions in License Manager](user-based-subscriptions-troubleshoot.md#user-based-subscriptions-troubleshoot-systems-manager-connectivity) section of this guide.
+ To stop incurring Microsoft Office or Visual Studio subscription charges for a user, you must disassociate the user from all instances they are associated with. For more information, see [Disassociate users from an instance that provides License Manager user-based subscriptions](usubs-disassociate-users.md).

## Subscription charges in License Manager
<a name="usubs-subscription-charges"></a>

Subscription and billing in License Manager varies based on the subscription product that's used.

**Microsoft Office and Visual Studio subscriptions**  
For Microsoft Office and Visual Studio subscriptions, billing stops as soon as you have disassociated the user from all instances that provide the subscription product, and unsubscribed them from the product.

**Microsoft Remote Desktop Services (RDS) subscriptions**  
Microsoft RDS is billed on a per user, per month basis based on a combination of the user subscription and the client access license (CAL) token that's issued from the license server when the user connects to an instance that provides the subscription product.

### Microsoft RDS billing in License Manager
<a name="usubs-billing-rds"></a>

Microsoft RDS billing begins when the Active Directory user is subscribed through License Manager, and ends after the client access license (CAL) token expires, 60 days from the date it's issued, with no proration for partial months. Billing continues until the token expires, even if you unsubscribe the user.

If an unsubscribed user continues to log in after the license token expires, they are automatically re-subscribed, and billing continues until they are again unsubscribed and their token expires.

Similarly, if a user who has never subscribed, but logs into an instance that is associated with the license server, License Manager automatically subscribes them and begins RDS billing. Billing continues until they are unsubscribed and their token expires.

To stop billing for a user at the end of the current month, you must remove that user from the Active Directory that's configured for the license server before unsubscribing.

**Warning**  
If you remove an Active Directory user who still has an active Microsoft Office or Visual Studio subscription, that user will no longer be able to access instances that they are associated with.

The following example scenarios demonstrate how RDS billing works.

#### Scenario 1: Standard subscription and billing
<a name="rds-billing-scenario-01"></a>

The following scenario shows a standard set of actions that affect billing for an Active Directory (AD) user who is subscribed on 12/15/2024, but never accesses a subscription instance.

*Action:* If the user never unsubscribes, billing continues indefinitely.


| AD user subscribed | Billing starts | CAL issued | CAL expires | User unsubscribed | User removed from AD | Billing ends | 
| --- | --- | --- | --- | --- | --- | --- | 
| 12/15/2024 | 12/15/2024 | -- | N/A | -- | -- | -- | 

*Action:* The user is unsubscribed on 1/15/2025.


| AD user subscribed | Billing starts | CAL issued | CAL expires | User unsubscribed | User removed from AD | Billing ends | 
| --- | --- | --- | --- | --- | --- | --- | 
| 12/15/2024 | 12/15/2024 | -- | N/A | `1/15/2025` | `No` | `1/31/2025` | 

#### Scenario 2: How the license token affects user subscription and billing
<a name="rds-billing-scenario-02"></a>

The following scenario shows how the license token expiration affects the user subscription for an Active Directory (AD) user who is subscribed on 9/15/2024 and logs into a domain-joined subscription product instance the same day.

*Action:* Initial subscription and login for AD user.


| AD user subscribed | Billing starts | CAL issued | CAL expires | User unsubscribed | User removed from AD | Billing ends | 
| --- | --- | --- | --- | --- | --- | --- | 
| 9/15/2024 | 9/15/2024 | 9/15/2024 | 11/15/2024 | -- | -- | -- | 

*Action:* The same AD user is unsubscribed on 10/19/2024. However, since the user wasn't removed from the directory, billing continues until the end of the month during which the license token expires.


| AD user subscribed | Billing starts | CAL issued | CAL expires | User unsubscribed | User removed from AD | Billing ends | 
| --- | --- | --- | --- | --- | --- | --- | 
| 9/15/2024 | 9/15/2024 | 9/15/2024 | 11/15/2024 | `10/19/2024` | -- | `11/30/2024` | 

*Alternative action:* The AD administrator removes the user from the directory on 10/20/2024, and then unsubscribes the user on the following day. In this case, billing stops at the end of the month during which the user is removed from the directory.


| AD user subscribed | Billing starts | CAL issued | CAL expires | User unsubscribed | User removed from AD | Billing ends | 
| --- | --- | --- | --- | --- | --- | --- | 
| 9/15/2024 | 9/15/2024 | 9/15/2024 | 11/15/2024 | 10/21/2024 | `10/20/2024` | `10/31/2024` | 

#### Scenario 3: Unsubscribed user is resubscribed
<a name="rds-billing-scenario-03"></a>

The following scenario shows how an unsubscribed Active Directory (AD) user whose license token has expired is automatically resubscribed when they access a domain-joined subscription product instance.

*Action:* Initial subscription and login for AD user.


| AD user subscribed | Billing starts | CAL issued | CAL expires | User unsubscribed | User removed from AD | Billing ends | 
| --- | --- | --- | --- | --- | --- | --- | 
| 9/15/2024 | 9/15/2024 | 9/15/2024 | 11/15/2024 | -- | -- | -- | 

*Action:* The same AD user is unsubscribed on 10/19/2024. However, since the user wasn't removed from the directory, billing continues until the end of the month during which the license token expires.


| AD user subscribed | Billing starts | CAL issued | CAL expires | User unsubscribed | User removed from AD | Billing ends | 
| --- | --- | --- | --- | --- | --- | --- | 
| 9/15/2024 | 9/15/2024 | 9/15/2024 | 11/15/2024 | `10/19/2024` | -- | `11/30/2024` | 

*Action:* The same AD user accesses a domain-joined subscription product instance after their previous license token expires but before billing ends. Billing continues until the user is unsubscribed again and their new token expires.


| AD user subscribed | Billing starts | CAL issued | CAL expires | User unsubscribed | User removed from AD | Billing ends | 
| --- | --- | --- | --- | --- | --- | --- | 
| `11/20/2024 (re-subscribed)` | `billing continues` | `11/20/2024` | `1/20/2025` | -- | -- | -- | 

#### Scenario 4: Automatic subscription on instance access
<a name="rds-billing-scenario-04"></a>

The following scenario shows how an Active Directory (AD) user who was never subscribed to RDS SAL is automatically subscribed when they log into a domain-joined subscription product instance.

*Action:* An AD user who was never subscribed to RDS SAL logs into a domain-joined subscription product instance on 9/15/2024, and is auto-subscribed. Billing begins, and continues until the user is unsubscribed and their new token expires.


| AD user subscribed | Billing starts | CAL issued | CAL expires | User unsubscribed | User removed from AD | Billing ends | 
| --- | --- | --- | --- | --- | --- | --- | 
| 9/15/2024 (auto-subscribed) | 9/15/2024 | 9/15/2024 | 11/15/2024 | -- | -- | -- | 

For more information about how Microsoft RDS per user CALs work, see the **Per User CALs** section in the [License your Remote Desktop deployment](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-client-access-license) article on the *Microsoft Learn* website.

## Prerequisites to create user-based subscriptions in License Manager
<a name="usubs-prerequisites"></a>

The following prerequisites must be implemented in your environment before you can create user-based subscriptions.

**Contents**
+ [IAM roles and permissions](#usubs-prereq-iam)
  + [AWS KMS Key policy for License Server credentials](#usubs-prereq-iam-rdslic)
+ [Active Directory](#usubs-prereq-ad)
+ [Security groups](#usubs-prereq-sg)
+ [Network configuration](#usubs-prereq-network)
+ [Instances that provide user-based subscription products](#usubs-prereq-instance)
+ [Microsoft Remote Desktop Services](#usubs-prereq-rds)
  + [Administrative credentials secret](#usubs-prereq-rds-secret)

### IAM roles and permissions
<a name="usubs-prereq-iam"></a>

You must allow License Manager to create a service-linked role in order to onboard your AWS account for user-based subscriptions. In the License Manager console, a prompt appears in **User-based subscriptions** if the role hasn't been created yet. After you respond to the prompt and agree to allow License Manager to create the role, choose **Create** to continue. For more information, see [Using service-linked roles for License Manager](using-service-linked-roles.md).

To create user-based subscriptions, your user or role must have the following permissions:
+ **Amazon EC2** – Work with network interfaces and subnets.
  + `ec2:CreateNetworkInterface`
  + `ec2:DeleteNetworkInterface`
  + `ec2:DescribeNetworkInterfaces`
  + `ec2:CreateNetworkInterfacePermission`
  + `ec2:DescribeSubnets`
+ **Directory Service** – Administer Active Directories.
  + `ds:DescribeDirectories`
  + `ds:AuthorizeApplication`
  + `ds:UnauthorizeApplication`
  + `ds:GetAuthorizedApplicationDetails`
  + `ds:DescribeDomainControllers`
+ **Route 53** – Configure routing.
  + `route53:DeleteHealthCheck`
  + `route53:ChangeResourceRecordSets`
  + `route53:GetHostedZone`
  + `route53:ListHostedZonesByName`
  + `route53:ListHostedZones`
  + `route53:ListHostedZonesByVPC`
  + `route53:CreateHostedZone`
  + `route53:DeleteHostedZone`
  + `route53:ListResourceRecordSets`
  + `route53:GetHealthCheckCount`
  + `route53:AssociateVPCWithHostedZone`

To create user-based subscriptions for Microsoft Office products, your user or role must also have these additional permissions:
+ `ec2:CreateVpcEndpoint`
+ `ec2:DeleteVpcEndpoints`
+ `ec2:DescribeVpcEndpoints`
+ `ec2:ModifyVpcEndpoint`
+ `ec2:DescribeSecurityGroups`

#### AWS KMS Key policy for License Server credentials
<a name="usubs-prereq-iam-rdslic"></a>

To use your own KMS key to encrypt and decrypt the administrative credentials secret for Microsoft RDS License Server, you must attach a policy to the role that you use for accessing License Manager operations. The following example shows a policy that grants permission for Secrets Manager to access the KMS key to encrypt and decrypt the Microsoft RDS License Server credential secret.

------
#### [ JSON ]

****  

```
{
"Version":"2012-10-17",		 	 	 
"Id": "key-policy",
"Statement": [
    {
        "Sid": "Enable IAM User Permissions",
        "Effect": "Allow",
        "Principal": {
            "AWS": "arn:aws:iam::{{111122223333}}:role/{{RoleName}}"
        },
        "Action": [
            "kms:Decrypt"
        ],
        "Resource": "arn:aws:kms:us-west-2:{{111122223333}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}",
        "Condition": {
            "StringLike": {
                "kms:ViaService": "secretsmanager.*.amazonaws.com"
            }
        }
    },
    {
        "Sid": "Enable IAM User Permissions",
        "Effect": "Allow",
        "Principal": {
            "AWS": "arn:aws:iam::{{111122223333}}:role/aws-service-role/license-manager-user-subscriptions.amazonaws.com/AWSServiceRoleForAWSLicenseManagerUserSubscriptionsService"
        },
        "Action": "kms:Decrypt", 
        "Resource": "arn:aws:kms:us-west-2:{{111122223333}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}",
        "Condition": {
            "StringLike": {
                "kms:ViaService": "secretsmanager.*.amazonaws.com"
            }
        }
    }
]
}
```

------

### Active Directory
<a name="usubs-prereq-ad"></a>

To use License Manager user-based subscriptions, you must create an Active Directory (AD) that contains user information for the subscription product users. Depending on your configuration, you can use an AWS Managed Microsoft AD, or a self-managed AD.

If you use both AWS managed and self-managed Active directories, you must establish a two-way forest trust between the directories. For more information, see [Tutorial: Create a trust relationship between your AWS Managed Microsoft AD and your self-managed Active Directory domain](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust.html) in the *AWS Directory Service Administration Guide*.

**Note**  
Subnets that are configured for your directory must all be from the same VPC for your AWS account. Shared subnets are not supported.

AWS managed Active Directories have the following restrictions.
+ Directories that are shared with you are only supported if the directory is onboarded in the primary account first, then you can onboard it in a shared account.
+ Multi-factor authentication is not supported

**Prerequisite for tag-based filters**  
If you will use tag-based filters for your Active Directory, you must first onboard to the AWS Resource Explorer service, as follows:

1. Open the Resource Explorer console at [https://resource-explorer.console.aws.amazon.com/resource-explorer](https://resource-explorer.console.aws.amazon.com/resource-explorer).

1. Choose **Turn on Resource Explorer**.

1. In the **Set up Resource Explorer** page, choose a setup option, as follows.  
**Quick setup**  
Select this option for basic configuration.  
**Advanced setup**  
Select this option for custom configuration. Ensure that you create an index for at least the Region where your Active Directory resides.

1. Select a Region for the **Aggregator index Region**.

1. Choose **Turn on Resource Explorer** to save your settings.

1. In the navigation pane, select **Views**, then choose **Create view**.
**Note**  
To show the navigation pane if it's hidden, choose the menu icon (three horizontal bars).

1. 

   1. In the **Create view** page, enter **license-manager-user-subscriptions-view** in the **Name**.

   1. Verify that the **Resources filter** is set to **Include all resources**.

   1. In the **Additional resource attributes** section, verify that the **Tags** checkbox is selected.

1. Choose **Create view** to finish.

For more information about creating an AWS Managed Microsoft AD directory, see [AWS Managed Microsoft AD prerequisites](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_prereqs.html) and [Create your AWS Managed Microsoft AD directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_create_directory.html) in the *AWS Directory Service User Guide*.

To associate users with AWS Managed Microsoft AD, you must provision users in your AWS Managed Microsoft AD directory. For more information, see [Manage users and groups in AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups.html) in the *AWS Directory Service Administration Guide*.

### Security groups
<a name="usubs-prereq-sg"></a>

Security groups control the network traffic that's allowed into and out of the resources on your network. To ensure that resources in your user-based subscription environment can communicate, your security groups must meet the following criteria.

**Security group for VPC endpoints**  
Identify or create a security group that permits **inbound** TCP port `1688` connectivity. When you configure your VPC settings, you'll specify this security group. For more information, see [Work with security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#working-with-security-groups).

License Manager associates this security group to the VPC endpoints it creates on your behalf while configuring the VPC. For more information about VPC endpoints, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.

**Security group for Active Directory domain controllers**  
Ensure that the security group that you use for your AD domain controllers allows outbound traffic to each domain controller's network interface IP address. In addition, the domain controller security group should allow communication on all Active Directory related ports including TCP 9389. Port 9389 is required for Active Directory Web Services (ADWS), which is used by the Active Directory PowerShell module and other management tools to communicate with domain controllers.

**Security group requirements for "Register your Active Directory" step**  
During onboarding your Active Directory to License Manager, we create a network interface in your supplied subnets which gets tagged with the default security group of the VPC. Please make sure that this security group is allowed access to your Active Directory domain controllers. This can be replaced with a group of your choice after onboarding is complete but will still require network access to the domain controllers.

**Security group requirements for "Configure RDS license server" step**  
During license server configuration, License Manager creates two network interfaces in the subnets you provide. These network interfaces are automatically tagged with a newly created security group that includes all required port configurations. Ensure that your Active Directory domain controller security groups allow bidirectional traffic from the subnet CIDRs on all Active Directory related ports, including TCP port 9389. Port 9389 is required for Active Directory Web Services (ADWS), which is used by the Active Directory PowerShell module and other management tools to communicate with domain controllers.

**Security group for user-based subscription instances**  
Identify or create a security group that permits the following access to and from your instance. For more information, see [Work with security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#working-with-security-groups).
+ **Inbound** TCP port `3389` connectivity from your approved connection sources.
+ **Outbound** TCP port `1688` connectivity to reach the VPC endpoints, and to communicate with AWS Systems Manager.

### Network configuration
<a name="usubs-prereq-network"></a>

License Manager creates two network interfaces which use the default security group of the VPC where your AWS Managed Microsoft AD is provisioned. These interfaces are used for the service to interact with your directory. For more information, see [Step 2: Register your Active Directory in License Manager](user-based-subscriptions-getting-started.md#user-based-subscriptions-configure-ad) and [What gets created](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.html) in the *AWS Directory Service Administration Guide*.

After the provisioning process is complete, you can associate a different security group to the interfaces created by License Manager.

**DNS resolution**  
The Active Directory that you've registered for user-based subscriptions must be accessible from any VPCs and subnets that you've configured in License Manager settings. To ensure that Active Directory nodes are accessible, configure DNS resolution as follows:
+ Configure DNS forwarding between the VPCs and Active Directories that are configured in your License Manager settings for user-based subscriptions.You can use Amazon Route 53 or another DNS service for DNS forwarding. For more information, see the blog post [Integrating your Directory Service’s DNS resolution with Amazon Route 53 Resolvers](https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-your-directory-services-dns-resolution-with-amazon-route-53-resolvers/).
+  Enable **DNS hostnames** and **DNS resolution** for your VPC. For more information, see [View and update DNS attributes for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-updating).

**Network considerations for multiple Active Directories**  
If you register multiple Active Directories for Microsoft Office user-based subscriptions, consider the following network requirements:
+ Each registered Active Directory must be in a separate VPC.
+ Instances are automatically associated with a registered Active Directory based on their VPC. Ensure that instances that provide user-based subscriptions are launched in a VPC that has a registered Active Directory, or in a VPC that is peered with exactly one VPC that has a registered Active Directory.
+ If you use VPC peering, ensure that each instance VPC is peered with only one VPC that has a registered Active Directory. Peering with multiple Active Directory VPCs results in an ambiguous configuration that prevents instance activation.

### Instances that provide user-based subscription products
<a name="usubs-prereq-instance"></a>

For your user-based subscription instances to function as expected, you must meet the following prerequisites:
+ Set up a security group for your instances as described in [Security groups](#usubs-prereq-sg).
+ Ensure that the instances launched to provide user-based subscriptions with Microsoft Office have a route to the subnet where the VPC endpoints are provisioned.
+ Instances that provide user-based subscriptions must be managed by AWS Systems Manager in order to have a healthy status. Additionally, your instances must be able to activate their user-based subscription licensing to remain in compliance after license activation.
**Note**  
License Manager will attempt to recover unhealthy instances, but instances that are not able to be return to a healthy status will be terminated. For troubleshooting information on keeping your instances managed by Systems Manager, and instance compliance, see the [Troubleshoot user-based subscriptions in License Manager](user-based-subscriptions-troubleshoot.md) section of this guide.
+ You must have an instance profile role attached to instances providing the user-based subscription products that allows for the resource to be managed by AWS Systems Manager. For more information, see [Create an IAM instance profile for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-profile.html) in the *AWS Systems Manager User Guide*.
+ You must [Disassociate users from an instance](usubs-disassociate-users.md) prior to terminating the instance.

### Microsoft Remote Desktop Services
<a name="usubs-prereq-rds"></a>

The Microsoft Remote Desktop Services license server requires an administrative user that's defined in the associated Active Directory. That user must be able to perform the following tasks:
+ Create an OU under the Active Directory domain
+ Domain join instances (create Computer) inside of the OU that is created
+ Add a computer object to a Terminal servers group within the Active Directory domain
+ Have delegated control for user objects in the Active Directory domain to read and write Terminal Server license server, in order to generate license server reports.

To learn more about delegation, see [Delegation of Control in Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/delegation-control-wizard).

#### Administrative credentials secret
<a name="usubs-prereq-rds-secret"></a>

License Manager uses AWS Secrets Manager to manage the credentials needed for user administration tasks on the Microsoft Remote Desktop Services license server. Before you can set up the license server, you must create a secret in Secrets Manager that contains the credentials for the user who performs user administration tasks on the license server. When you configure the license server settings, you must provide the ID of the secret that you created.

**Note**  
This must be the same user that you've defined for RDS license server report generation.

To create a secret, follow detailed instructions on the [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) page in the *Secrets Manager User Guide*, with the following settings that are specific to License Manager.

**Important**  
To use the secret, License Manager depends on the exact key names, the username value, and the encryption key that are specified in the following list. The secret name must begin with the following prefix: `license-manager-user-`.

On the **Choose secret type** page:
+ **Secret type** – Choose **Other type of secret**.
+ **Key/value pairs** – Specify the following key pairs to store in the secret.  
Username  
  + Key: `username`
  + Value: `Administrator`  
Password  
  + Key: `password`
  + Value: {{The password}}
+ **Encryption key** – To specify a KMS key other than the `aws/secretsmanager` key, you must attach a policy to the role that you use for accessing License Manager operations. For more information, see [IAM roles and permissions](#usubs-prereq-iam).

On the **Configure secret** page:
+ **Secret name** – Specify a name for your secret that begins with the prefix that License Manager uses to identify license server credential secrets. For example:

  ```
  license-manager-user-{{admin-credentials}}
  ```

These instructions assume that you are using the AWS Management Console to create your secret. The Secrets Manager User Guide also includes detailed instructions for other methods. For more information about Secrets Manager, see [What Is Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/). For information specifically related to costs, see [Pricing for AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html#asm_pricing) in the *Secrets Manager User Guide*.

## Supported software products for user-based subscriptions in License Manager
<a name="usubs-software"></a>

AWS License Manager supports user-based subscriptions for Microsoft Visual Studio, and Microsoft Office. Supported software utilization is tracked by License Manager. A single subscription to Windows Server Remote Desktop Services Subscriber Access License (RDS SAL) is required for each user to access a license-included instance that provides a user-based subscription product. For more information, see [Get started with user-based subscriptions in License Manager](user-based-subscriptions-getting-started.md).

**Supported Windows operating system (OS) platforms**  
You can find Windows AMIs that include products covered by the RDS SAL license for the following Windows OS platforms:
+ Windows Server 2025
+ Windows Server 2022
+ Windows Server 2019

### Supported software for user-based subscriptions
<a name="usubs-software-supported"></a>

**Contents**
+ [Microsoft Visual Studio](#user-subs-visual-studio)
+ [Microsoft Office](#user-subs-ms-office)
  + [Microsoft Office EC2 Image Builder component](#user-subs-ms-office-builder-component)

#### Microsoft Visual Studio
<a name="user-subs-visual-studio"></a>

Microsoft Visual Studio is an integrated development environment (IDE) that enables developers to create, edit, debug, and publish applications. The provided Microsoft Visual Studio AMIs include the [AWS Toolkit for .NET Refactoring](https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.html) and the [AWS Toolkit for Visual Studio](https://aws.amazon.com/visualstudio/).

**Supported editions**
+ Visual Studio Professional 2022
+ Visual Studio Enterprise 2022

The following table details the software subscription names and their associated product value used for License Manager user-based subscription API operations.


| Software subscription name | Product value | 
| --- | --- | 
| Visual Studio Enterprise 2022 | `VISUAL_STUDIO_ENTERPRISE` | 
| Visual Studio Professional 2022 | `VISUAL_STUDIO_PROFESSIONAL` | 

#### Microsoft Office
<a name="user-subs-ms-office"></a>

Microsoft Office is a collection of software developed by Microsoft for various productivity use cases including working with documents, spreadsheets, and slide show presentations.

**Supported editions**
+ Office LTSC Professional Plus 2021
+ Office LTSC Professional Plus 2024
+ Office LTSC Professional Plus 2021 32-bit (x86)
+ Office LTSC Professional Plus 2024 32-bit (x86)
+ Office LTSC Standard 2021
+ Office LTSC Standard 2024
+ Office LTSC Standard 2021 32-bit (x86)
+ Office LTSC Standard 2024 32-bit (x86)

The following table details the software subscription names and their associated product value used for License Manager user-based subscription API operations.


| Software subscription name | Product value | 
| --- | --- | 
| Office LTSC Professional Plus 2021 | `OFFICE_PROFESSIONAL_PLUS` | 
| Office LTSC Professional Plus 2024 | `OFFICE_PROFESSIONAL_PLUS` | 
| Office LTSC Standard 2021 | `OFFICE_STANDARD` | 
| Office LTSC Standard 2024 | `OFFICE_STANDARD` | 

##### Microsoft Office EC2 Image Builder component
<a name="user-subs-ms-office-builder-component"></a>

In addition to the pre-configured AMIs, Microsoft Office is also available as EC2 Image Builder components. 

Image Builder components are available for both Microsoft Office LTSC Professional Plus and Microsoft Office LTSC Standard. You can configure the version year and architecture to match your requirements.

**Supported version year**
+ 2021
+ 2024

**Supported architecture**
+ 32-bit
+ 64-bit

## Combine Microsoft Office with other software
<a name="usubs-combine-products"></a>

You can use the Microsoft Office builder components with EC2 Image Builder to create customized AMIs that include Microsoft Office along with other software.

Office Image Builder components can be used with any of the following base AMIs:
+ Your own custom AMI
+ A Visual Studio user-based subscription AMI
+ A base Windows Server AMI

You can also include additional EC2 Image Builder components in your image recipe alongside the Office component. For example, you can add components that install your organization's tools, agents, or configurations to produce a fully customized AMI that includes Office and any other software your users need.

**Combine Microsoft Office and Microsoft Visual Studio into a single instance**  
You can bundle multiple licensed products into a single Amazon Machine Image (AMI) using EC2 Image Builder pipelines created through License Manager. For example, you can create an AMI that includes both Visual Studio Professional 2022 and Office LTSC Professional Plus 2024, then launch instances with all products pre-installed and pre-licensed. For step-by-step instructions, see [Launch an instance with both Microsoft Office and Microsoft Visual Studio products](usubs-launch-instance.md#launch-multi-product-instance) 

## Active Directory
<a name="ad-support"></a>

License Manager supports user-based subscriptions for Microsoft Visual Studio, Microsoft Office, and Remote Desktop Services Subscriber Access License (RDS SAL). Products may support either AWS Managed Microsoft AD or a self-managed active directory that is either deployed within your AWS environment or has network connectivity to a VPC in your AWS environment.

This table indicates which types of Active Directory are supported by each software product when used with user-based subscriptions:.


| Software product | AWS Managed Microsoft AD | Self-managed AD | 
| --- | --- | --- | 
| Microsoft Visual Studio  | Supported | Not supported | 
| Microsoft Office | Supported | Not supported | 
| RDS SAL Product | Supported | Supported | 

## Multiple Active Directory support for Microsoft Office
<a name="usubs-multi-ad"></a>

You can register multiple Active Directories for Microsoft Office user-based subscriptions within a single account and Region. This allows you to maintain separate Active Directories for different business units, environments, or workloads without requiring VPC peering or trust relationships between them.

When you register multiple Active Directories, the following constraints apply:
+ You can register up to 20 Active Directories per account per Region. In case you need adjustment, please reach out to AWS Support.
+ Each Active Directory must be associated with a unique VPC. You cannot register more than one Active Directory in the same VPC.
+ If multiple Active Directories share the same VPC endpoint VPC, the subnets and security group configuration must be identical across all registrations.
+ Accounts that use a shared Active Directory from another account cannot register additional Active Directories.

**How License Manager selects the Active Directory for an instance**  
When you launch an instance with a Microsoft Office user-based subscription product, License Manager automatically determines which registered Active Directory to use for activation. No additional launch parameters are required.

License Manager resolves the Active Directory using the following logic:

1. **Direct VPC match** – If the instance is launched in a VPC that has a registered Active Directory, that directory is used.

1. **Peered VPC match** – If the instance is launched in a VPC that does not have a registered Active Directory, but is peered with exactly one VPC that does, the peered directory is used.

If License Manager cannot determine a single Active Directory for an instance, activation will not succeed. To avoid this, ensure that each instance VPC can reach only one registered Active Directory, either directly or through VPC peering.

**Important**  
If an instance VPC is peered with multiple VPCs that each have a registered Active Directory, License Manager cannot determine which directory to use and the instance is unable to complete its initial configuration. Resources that are unable to complete the initial configuration are terminated. Review your VPC peering topology to ensure that each instance VPC has a path to only one registered Active Directory.

**Filtering instances by Active Directory**  
If you have multiple Active Directories registered, you can filter instances by Active Directory in the console or by using the ActiveDirectoryId filter with the ListInstances API.

## Additional software
<a name="usubs-software-additional"></a>

You can install additional software on your instances that aren't available as user-based subscriptions. Additional software installations aren't tracked by License Manager. These installations must be performed using the administrative account for your Active Directory. If you use an AWS Managed Microsoft AD, the administrative account (Admin) is created by default in your directory. For more information, see [Admin account](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_admin_account.html) in the *Directory Service Administration Guide*.

To install additional software with the Active Directory administrative account, you must:
+ Subscribe the administrative account to the product provided by the instance.
+ Associate the administrative account to the instance.
+ Connect to the instance using the administrative account to perform the installation.

For more information, see [Get started with user-based subscriptions in License Manager](user-based-subscriptions-getting-started.md).