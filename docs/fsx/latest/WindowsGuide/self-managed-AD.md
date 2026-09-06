

# Using a self-managed Microsoft Active Directory
<a name="self-managed-AD"></a>

If your organization manages identities and devices using a self-managed Active Directory on-premises or in the cloud, you can join an FSx for Windows File Server file system to your Active Directory domain at creation.

 When you join your file system to your self-managed Active Directory, your FSx for Windows File Server file system resides in the same Active Directory forest (the top logical container in an Active Directory configuration that contains domains, users, and computers) and in the same Active Directory domain as your users and existing resources (including existing file servers). 

**Note**  
You can isolate your resources—including your Amazon FSx ﬁle systems—into a separate Active Directory forest from the one where your users reside. To do this, join your ﬁle system to an AWS Managed Microsoft Active Directory and establish a one-way forest trust relationship between an AWS Managed Microsoft Active Directory that you create and your existing self-managed Active Directory. 
+  User name and password for a service account on your Active Directory domain, for Amazon FSx to use to join the file system to your Active Directory domain. You can provide these credentials as plaintext or store them in AWS Secrets Manager and provide the secret ARN (recommended).
+  (Optional) The Organizational Unit (OU) in your domain in which you want your file system to be joined.
+ (Optional) The domain group to which you want to delegate authority to perform administrative actions on your file system. For example, this domain group might manage Windows file shares, manage Access Control Lists (ACLs) on the file system's root folder, take ownership of files and folders, and so on. If you don’t specify this group, Amazon FSx delegates this authority to the Domain Admins group in your Active Directory domain by default.
**Note**  
The domain group name you provide must be unique in your Active Directory. FSx for Windows File Server will not create the domain group under the following circumstances:  
If a group already exists with the name you specify
If you do not specify a name, and a group named "Domain Admins" already exists in your Active Directory.

  For more information, see [Joining an Amazon FSx file system to a self-managed Microsoft Active Directory domain](creating-joined-ad-file-systems.md).

**Topics**
+ [Prerequisites](#self-manage-prereqs)
+ [Service account permissions](#service-account-prereqs)
+ [Best practices when using a self-managed Active Directory](#self-managed-AD-best-practices)
+ [Amazon FSx service account](#self-managed-AD-service-account)
+ [Delegating permissions to the Amazon FSx service account or group](assign-permissions-to-service-account.md)
+ [Validating your Active Directory configuration](validate-ad-config.md)
+ [Joining an Amazon FSx file system to a self-managed Microsoft Active Directory domain](creating-joined-ad-file-systems.md)
+ [Getting the correct file system IP addresses to use for manual DNS entries](file-system-ip-addresses-for-dns.md)
+ [Updating a self-managed Active Directory configuration](update-self-ad-config.md)
+ [Changing the Amazon FSx service account](changing-ad-service-account.md)
+ [Monitoring self-managed Active Directory updates](monitor-self-ad-update.md)

## Prerequisites
<a name="self-manage-prereqs"></a>

Before you join an FSx for Windows File Server file system to your self-managed Microsoft Active Directory domain, review the following prerequisites to help ensure that you can successfully join your Amazon FSx file system to your self-managed Active Directory.

### On-premises configurations
<a name="on-prem-prereqs"></a>

These are the prerequisites for your self-managed Microsoft Active Directory, either an on-premises or cloud-based, that you will join the Amazon FSx file system to.
+ The Active Directory domain controllers: 
  + Must have a domain functional level at Windows Server 2008 R2 or higher.
  + Must be writable.
  + At least one of the reachable domain controllers must be a Global Catalog of the forest.
+ The DNS server must be able to resolve names as follows:
  + In the domain that you are joining the file system
  + In the root domain of the forest
+ The DNS server and Active Directory domain controller IP addresses must meet the following requirements, which vary depending on when your Amazon FSx file system was created:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-managed-AD.html)

  If you need to access an FSx for Windows File Server file system that was created before December 17, 2020 using a non-private IP address range, you can create a new file system by restoring a backup of the file system. For more information, see [Restoring a backup to a new file system](how-to-restore-backups.md).
+ The domain name of your self-managed Active Directory must meet the following requirements:
  + The domain name isn't in Single Label Domain (SLD) format. Amazon FSx doesn't support SLD domains.
  + For Single-AZ 2 and all Multi-AZ file systems, the domain name cannot exceed 47 characters.
+ Any Active Directory sites that you have defined must meet the following prerequisites:
  + The subnets in the VPC that's associated with your file system must be defined in an Active Directory site.
  + There are no conflicts between the VPC subnets and any of the Active Directory site subnets.

  Amazon FSx requires connectivity to the domain controllers or Active Directory sites you have defined in your Active Directory environment. Amazon FSx will ignore any domain controllers with TCP and UDP blocked on port 389. For the remaining domain controllers in your Active Directory, ensure that they meet the Amazon FSx connectivity requirements. Additionally, verify that any changes to your service account are propagated to all these domain controllers.
**Important**  
Do not move, disable, or delete the computer objects that Amazon FSx creates in the OU. Do not change the default OU after your file system is created. Any of these actions will cause your file system to become misconfigured.

You can validate your Active Directory configuration, including testing connectivity of multiple domain controllers, using the [Amazon FSx Active Directory Validation tool](validate-ad-config.md). To limit the number of domain controllers that require connectivity, you can also build a trust relationship between your on-premise domain controllers and AWS Managed Microsoft AD. For more information, see [Using a resource forest isolation model](fsx-aws-managed-ad.md#using-a-rfim).

**Important**  
Amazon FSx only registers the DNS records for a file system if you are using Microsoft DNS as the default DNS service. If you are using a third-party DNS, you will need to manually set up DNS record entries for your file system after you create it.

### Network configurations
<a name="network-configs"></a>

This section describes the network configuration requirements for joining a file system to your self-managed Active Directory. We strongly recommend that you use the [Amazon FSx Active Directory validation tool](validate-ad-config.md#test-ad-network-config) to test your network settings before attempting to join your file system to your self-managed Active Directory.
+ Ensure that your firewall rules will allow ICMP traffic between your Active Directory domain controllers and Amazon FSx.
+ Connectivity must be configured between the Amazon VPC where you want to create the file system and your self-managed Active Directory. You can set up this connectivity using [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html), [AWS Virtual Private Network](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html), [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html), or [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html).
+ The default VPC security group for your default Amazon VPC must be added to your file system using the Amazon FSx console. Ensure that the security group and the VPC Network ACLs for the subnets where you create your file system allow traffic on the ports and in the direction shown in the following diagram.  
![FSx for Windows File Server port configuration requirements for VPC security groups and network ACLs for the subnets where the file system is created.](http://docs.aws.amazon.com/fsx/latest/WindowsGuide/images/Windows-port-requirements.png)

  The following table identifies the protocol, ports, and its role.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-managed-AD.html)

  These traffic rules need to also be mirrored on the firewalls that apply to each of the Active Directory domain controllers, DNS servers, FSx clients, and FSx administrators.

**Note**  
If you're using VPC network ACLs, you must also allow outbound traffic on dynamic ports (49152-65535) from your file system.

**Important**  
While Amazon VPC security groups require ports to be opened only in the direction that network traffic is initiated, most Windows firewalls and VPC network ACLs require ports to be open in both directions.

## Service account permissions
<a name="service-account-prereqs"></a>

You need to have a service account in your self-managed Microsoft Active Directory with delegated permissions to join computer objects to your self-managed Active Directory domain. A *service account *is a user account in your self-managed Active Directory that has been delegated certain tasks.

The following is the minimum set of permissions that must be delegated to the Amazon FSx service account in the OU that you're joining the file system to.
+ If using *Delegate Control* in the Active Directory User and Computers MMC:
  + Reset passwords
  + Read and write Account Restrictions
  + Validated write to DNS host name
  + Validated write to service principal name
+ If using *Advanced Features* in the Active Directory User and Computers MMC:
  + Modify permissions
  + Create computer objects
  + Delete computer objects

For more information, see the Microsoft Windows Server documentation topic [ Error: Access is denied when non-administrator users who have been delegated control try to join computers to a domain controller](https://support.microsoft.com/en-us/help/932455/error-message-when-non-administrator-users-who-have-been-delegated-con).

For more information about setting the required permissions, see [Delegating permissions to the Amazon FSx service account or group](assign-permissions-to-service-account.md).

## Best practices when using a self-managed Active Directory
<a name="self-managed-AD-best-practices"></a>

**Topics**
+ [Storing Active Directory credentials using AWS Secrets Manager](#bp-store-ad-creds-using-secret-manager-windows)

We recommend that you follow these best practices when joining an Amazon FSx for Windows File Server ﬁle systems to your self-managed Microsoft Active Directory. These best practices will help you in maintaining continuous, uninterrupted availability of your file system.

**Use a separate service account for Amazon FSx**  
Use a separate service account to delegate the [required privileges](#service-account-prereqs) for Amazon FSx to fully manage file systems that are joined to your self-managed Active Directory. We do not recommend using the **Domain Admins** for this purpose.

**Use an Active Directory group**  
Use an Active Directory group to manage Active Directory permissions and configurations associated with the Amazon FSx service account.

**Segregate the Organizational Unit (OU)**  
To make it easier to find and manage your Amazon FSx computer objects, we recommend that you segregate the Organizational Unit (OU) you use for your FSx for Windows File Server file systems from other domain controller concerns.

**Keep the Active Directory configuration up-to-date**  
It is imperative that you keep your file system's Active Directory configuration up-to-date with any changes. For example, if your self-managed Active Directory uses a time-based password reset policy, as soon as the password is reset, make sure to update the service account password on your file system. For more information, see [Updating a self-managed Active Directory configuration](update-self-ad-config.md).

**Changing the Amazon FSx service account**  
If you update your file system with a new service account, it must have the required permissions and privileges to join your Active Directory and have **Full control** permissions for the existing computer objects associated with the file system. For more information, see [Changing the Amazon FSx service account](changing-ad-service-account.md).

**Assign subnets to a single Microsoft Active Directory site**  
If your Active Directory environment has a large number of domain controllers, use **Active Directory Sites and Services** to assign the subnets used by your Amazon FSx file systems to a single Active Directory site with the highest availability and reliability. Make sure that the VPC security group, VPC network ACL, Windows firewall rules on your DCs, and any other network routing controls you have in your Active Directory infrastructure allow communication from Amazon FSx on the required ports. This allows Windows to revert to other domain controllers if it can't use the assigned Active Directory site. For more information, see [File system access control with Amazon VPC](limit-access-security-groups.md).

**Use security group rules to limit traffic**  
Use security group rules to implement the principle of least privilege in your virtual private cloud (VPC). You can limiting the type of inbound and outbound network traffic allowed for your file using VPC security group rules. For example, we recommend only allowing outbound traffic to your self-managed Active Directory domains controllers or to within the subnet or security group you are using. For more information, see [File system access control with Amazon VPC](limit-access-security-groups.md). 

**Do not move computer objects created by Amazon FSx**  
Do not move, disable, or delete the computer objects that Amazon FSx creates in the OU. Do not change the default OU after your file system is created. Any of these actions will cause your file system to become misconfigured.

**Validate your Active Directory configuration**  
Before attempting to join an FSx for Windows File Server file system to your Active Directory, we strongly recommend that you validate your Active Directory configuration using the [Amazon FSx Active Directory Validation tool](validate-ad-config.md).

### Storing Active Directory credentials using AWS Secrets Manager
<a name="bp-store-ad-creds-using-secret-manager-windows"></a>

You can use AWS Secrets Manager to securely store and manage your Microsoft Active Directory domain join service account credentials. This approach eliminates the need to store sensitive credentials in plaintext in application code or configuration files, strengthening your security posture.

You can also configure IAM policies to manage access to your secrets, and set up automatic rotation policies for your passwords.

#### Store Active Directory credentials in AWS Secrets Manager (Console)
<a name="bp-store-ad-creds-sm-windows-console"></a>

##### Step 1: Create a KMS key
<a name="create-kms-key-windows-console"></a>

Create a KMS key to encrypt and decrypt your Active Directory credentials in Secrets Manager.

**To create a key**
**Note**  
For **Encryption Key**, create a new key, don't use the AWS default KMS key. Be sure to create the AWS KMS key in the same Region that contains the file system that you want to join to your Active Directory.

1. Open the AWS KMS console at https://console.aws.amazon.com/kms.

1. Choose **Create key**.

1. For **Key Type**, choose **Symmetric**.

1. For **Key Usage**, choose **Encrypt and decrypt**.

1. For **Advanced options**, do the following:

   1. For **Key material origin**, choose **KMS**.

   1. For **Regionality**, choose **Single-Region key** and choose **Next**.

1. Choose **Next**.

1. For **Alias**, provide a name for the KMS key.

1. (Optional) For **Description**, provide a description of the KMS key.

1. (Optional) For **Tags**, provide a tag for the KMS key and choose **Next**.

1. (Optional) For **Key administrators**, provide the IAM users and roles authorized to manage this key.

1. For **Key deletion**, keep the box selected for **Allow key administrators** to delete this key and choose **Next**.

1. (Optional) For **Key users**, provide the IAM users and roles authorized to use this key in cryptographic operations. Choose **Next**.

1. For **Key policy**, choose **Edit** and include the following to the policy **Statement** to allow Amazon FSx to use the KMS key and choose **Next**. Make sure to replace the {{us-west-2}} to the AWS Region where the file system is deployed and {{123456789012}} to your AWS account ID.

   ```
   {
       "Sid": "Allow FSx to use the KMS key",
       "Version": "2012-10-17", 		 	 	 
       "Effect": "Allow",
       "Principal": {
           "Service": "fsx.amazonaws.com"
       },
       "Action": [
           "kms:Decrypt",
           "kms:DescribeKey"
       ],
       "Resource": "arn:aws:kms:{{us-west-2}}:{{123456789012}}:key/*",
       "Condition": {
           "StringEquals": {
               "kms:ViaService": "secretsmanager.{{us-west-2}}.amazonaws.com",
               "aws:SourceAccount": "{{123456789012}}"
           },
           "ArnLike": {
               "aws:SourceArn": "arn:aws:fsx:{{us-west-2}}:{{123456789012}}:file-system/*"
           }
       }
   }
   ```

1. Choose **Finish**.

**Note**  
You can set more granular access control by modifying the `Resource` and `aws:SourceArn` fields to target specific secrets and file systems.

##### Step 2: Create an AWS Secrets Manager secret
<a name="create-secret-windows-console"></a>

**To create a secret**

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. For **Secret type**, choose **Other type of secret**.

1. For **Key/value pairs**, do the following to add your two keys:

   1. For the first key, enter `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_USERNAME`.

   1. For the value of the first key, enter only the username (without the domain prefix) of the AD user.

   1. For the second key, enter `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_PASSWORD`.

   1. For the value of the second key, enter the password that you created for the AD user on your domain.

1. For **Encryption key**, enter the ARN of the KMS key that you created in a previous step and choose **Next**.

1. For **Secret name**, enter a descriptive name that helps you find your secret later.

1. (Optional) For **Description**, enter a description for the secret name.

1. For **Resource permission**, choose **Edit**.

   Add the following policy to the permission policy to allow Amazon FSx to use the secret, then choose **Next**. Make sure to replace the {{us-west-2}} to the AWS Region where the file system is deployed and {{123456789012}} to your AWS account ID.

   ```
   {
       "Version": "2012-10-17", 		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "fsx.amazonaws.com"
               },
               "Action": [
                   "secretsmanager:GetSecretValue",
                   "secretsmanager:DescribeSecret"
               ],
               "Resource": "arn:aws:secretsmanager:{{us-west-2}}:{{123456789012}}:secret:*",
               "Condition": {
                   "StringEquals": {
                       "aws:SourceAccount": "{{123456789012}}"
                   },
                   "ArnLike": {
                       "aws:SourceArn": "arn:aws:fsx:{{us-west-2}}:{{123456789012}}:file-system/*"
                   }
               }
           }
       ]
   }
   ```
**Note**  
You can set more granular access control by modifying the `Resource` and `aws:SourceArn` fields to target specific secrets and file systems.

1. (Optional) You can configure Secrets Manager to rotate your credentials automatically. Choose **Next**.

1. Choose **Finish**.

#### Store Active Directory credentials in AWS Secrets Manager (CLI)
<a name="bp-store-ad-creds-sm-windows-cli"></a>

##### Step 1: Create a KMS key
<a name="create-kms-key-windows-cli"></a>

Create a KMS key to encrypt and decrypt your Active Directory credentials in Secrets Manager.

To create a KMS key, use the AWS CLI command [create-key](https://docs.aws.amazon.com/cli/latest/reference/kms/create-key.html).

In this command, set the `--policy` parameter to specify the key policy that defines permissions for the KMS key. The policy must include the following:
+ The service principal for Amazon FSx, which is `fsx.amazonaws.com`.
+ Required KMS actions: `kms:Decrypt` and `kms:DescribeKey`.
+ Resource ARN pattern for your AWS Region and account.
+ Condition keys that restrict key usage:
  + `kms:ViaService` to ensure requests come through Secrets Manager.
  + `aws:SourceAccount` to limit to your account.
  + `aws:SourceArn` to restrict to specific Amazon FSx file systems.

The following example creates a symmetric encryption KMS key with a policy that allows Amazon FSx to use the key for decryption and key description operations. The command automatically retrieves your AWS account ID and Region, then configures the key policy with these values to ensure proper access controls between Amazon FSx, Secrets Manager, and the KMS key. Make sure your AWS CLI environment is in the same region as the file system that will join the Active Directory.

```
# Set region and get Account ID
REGION=${AWS_REGION:-$(aws configure get region)}
ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)

# Create Key
KMS_KEY_ARN=$(aws kms create-key --policy "{
  \"Version\": \"2012-10-17\", 		 	 	 
  \"Statement\": [
    {
      \"Sid\": \"Enable IAM User Permissions\",
      \"Effect\": \"Allow\",
      \"Principal\": {
        \"AWS\": \"arn:aws:iam::{{$ACCOUNT_ID}}:root\"
      },
      \"Action\": \"kms:*\",
      \"Resource\": \"*\"
    },
    {
      \"Sid\": \"Allow FSx to use the KMS key\",
      \"Effect\": \"Allow\",
      \"Principal\": {
        \"Service\": \"fsx.amazonaws.com\"
      },
      \"Action\": [
        \"kms:Decrypt\",
        \"kms:DescribeKey\"
      ],
      \"Resource\": \"*\",
      \"Condition\": {
        \"StringEquals\": {
          \"kms:ViaService\": \"secretsmanager.{{$REGION}}.amazonaws.com\",
          \"aws:SourceAccount\": \"{{$ACCOUNT_ID}}\"
        },
        \"ArnLike\": {
          \"aws:SourceArn\": \"arn:aws:fsx:{{$REGION}}:{{$ACCOUNT_ID}}:file-system/*\"
        }
      }
    }
  ]
}" --query 'KeyMetadata.Arn' --output text)

echo "KMS Key ARN: $KMS_KEY_ARN"
```

**Note**  
You can set more granular access control by modifying the `Resource` and `aws:SourceArn` fields to target specific secrets and file systems.

##### Step 2: Create an AWS Secrets Manager secret
<a name="create-secret-windows-cli"></a>

To create a secret for Amazon FSx to access your Active Directory, use the AWS CLI command [create-secret](https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/create-secret.html) and set the following parameters:
+ `--name`: The identifier for your secret.
+ `--description`: A description of the secret's purpose.
+ `--kms-key-id`: The ARN of the KMS key you created in [Step 1](#create-kms-key-windows-cli) for encrypting the secret at rest.
+ `--secret-string`: A JSON string containing your AD credentials in the following format:
  + `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_USERNAME`: Your AD service account username without the domain prefix, such as `svc-fsx`. **Don't** provide the domain prefix, such as `CORP\svc-fsx`.
  + `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_PASSWORD`: Your AD service account password.
+ `--region`: The AWS Region where your Amazon FSx file system will be created. This defaults to your configured region if `AWS_REGION` is not set.

After creating the secret, attach a resource policy using the [put-resource-policy](https://docs.aws.amazon.com/cli/latest/reference/logs/put-resource-policy.html) command, and set the following parameters:
+ `--secret-id`: The name or ARN of the secret to attach the policy to. The following example uses **FSxSecret** as the `--secret-id`.
+ `--region`: The same AWS Region as your secret.
+ `--resource-policy`: A JSON policy document that grants Amazon FSx permission to access the secret. The policy must include the following:
  + The service principal for Amazon FSx, which is **fsx.amazonaws.com**.
  + Required Secrets Manager actions: `secretsmanager:GetSecretValue` and `secretsmanager:DescribeSecret`.
  + Resource ARN pattern for your AWS Region and account.
  + The following condition keys that restrict access:
    + `aws:SourceAccount` to limit to your account.
    + `aws:SourceArn` to restrict to specific Amazon FSx file systems.

The following example creates a secret with the required format and attaches a resource policy that allows Amazon FSx to use the secret. This example automatically retrieves your AWS account ID and Region, then configures the resource policy with these values to ensure proper access controls between Amazon FSx and the secret.

Make sure to replace the `KMS_KEY_ARN` with the ARN from the key you created in [Step 1](#create-kms-key-windows-cli), `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_USERNAME`, and `CUSTOMER_MANAGED_ACTIVE_DIRECTORY_PASSWORD` with your Active Directory service account credentials. Additionally, verify that your AWS CLI environment is configured for the same region as the file system that will join the Active Directory.

```
# Set region and get account ID
REGION=${AWS_REGION:-$(aws configure get region)}
ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)

# Replace with your KMS key ARN from Step 1
KMS_KEY_ARN="{{arn:aws:kms:us-east-2:123456789012:key/1234542f-d114-555b-9ade-fec3c9200d8e}}"

# Replace with your Active Directory credentials
AD_USERNAME="{{Your_Username}}"  
AD_PASSWORD="{{Your_Password}}"

# Create the secret
SECRET_ARN=$(aws secretsmanager create-secret \
  --name "FSxSecret" \
  --description "Secret for FSx access" \
  --kms-key-id "$KMS_KEY_ARN" \
  --secret-string "{\"CUSTOMER_MANAGED_ACTIVE_DIRECTORY_USERNAME\":\"$AD_USERNAME\",\"CUSTOMER_MANAGED_ACTIVE_DIRECTORY_PASSWORD\":\"$AD_PASSWORD\"}" \
  --region "$REGION" \
  --query 'ARN' \
  --output text)

echo "Secret created with ARN: $SECRET_ARN"

# Attach the resource policy with proper formatting
aws secretsmanager put-resource-policy \
  --secret-id "FSxSecret" \
  --region "$REGION" \
  --resource-policy "{
    \"Version\": \"2012-10-17\", 		 	 	 
    \"Statement\": [
      {
        \"Effect\": \"Allow\",
        \"Principal\": {
          \"Service\": \"fsx.amazonaws.com\"
        },
        \"Action\": [
          \"secretsmanager:GetSecretValue\",
          \"secretsmanager:DescribeSecret\"
        ],
        \"Resource\": \"$SECRET_ARN\",
        \"Condition\": {
          \"StringEquals\": {
            \"aws:SourceAccount\": \"$ACCOUNT_ID\"
          },
          \"ArnLike\": {
            \"aws:SourceArn\": \"{{arn:aws:fsx:$REGION:$ACCOUNT_ID:file-system/*}}\"
          }
        }
      }
    ]
  }"

echo "Resource policy attached successfully"
```

**Note**  
You can set more granular access control by modifying the `Resource` and `aws:SourceArn` fields to target specific secrets and file systems.

## Amazon FSx service account
<a name="self-managed-AD-service-account"></a>

Amazon FSx file systems that are joined to a self-managed Active Directory require a valid service account throughout their lifetime. Amazon FSx uses the service account to fully manage your file systems and perform administrative tasks that require unjoining and rejoining computer objects to your Active Directory domain. These tasks include replacing a failed file server and patching Microsoft Windows Server software. For Amazon FSx to perform these tasks, the Amazon FSx service account must have, at a minimum, the set of permissions that are described in [Service account permissions](#service-account-prereqs) delegated to it.

Although members of the **Domain Admins** group have sufficient privileges to perform these tasks, we strongly recommend that you use a separate service account to delegate the required privileges to Amazon FSx. 

For more information about how to delegate privileges using either the **Delegate Control** or **Advanced Features** features in the **Active Directory User and Computers** MMC snap-in, see [Delegating permissions to the Amazon FSx service account or group](assign-permissions-to-service-account.md).

If you update your file system with a new service account, the new service account must have the required permissions and privileges to join your Active Directory and have **Full control** permissions for the existing computer objects associated with the file system. For more information, see [Changing the Amazon FSx service account](changing-ad-service-account.md).

We recommend storing your Active Directory service account credentials in AWS Secrets Manager for enhanced security. This eliminates the need to store sensitive credentials in plaintext and aligns with security best practices. For more information, see [Using a self-managed Microsoft Active Directory](#self-managed-AD).