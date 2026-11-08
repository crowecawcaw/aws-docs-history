

# Setting up self-managed Active Directory
<a name="oracle-smad-setting-up"></a>

Before you join an Amazon RDS for Oracle DB instance to your self-managed Active Directory (AD) domain, complete the following steps to prepare your AD domain and your AWS account. You complete these steps once, and you can use the Organizational Unit (OU), domain service account, AWS KMS key, and secret that they create for each DB instance in the same AWS account and AWS Region that you join to the domain. After you finish, join each DB instance to the domain and connect to it as described in [Configuring a Kerberos client and connecting to your DB instance](oracle-smad-connecting.md).
+ [Step 1: Create an Organizational Unit in your AD](#oracle-smad-setting-up.step1)
+ [Step 2: Create an AD domain service account in your AD](#oracle-smad-setting-up.step2)
+ [Step 3: Delegate control to the AD domain service account](#oracle-smad-setting-up.step3)
+ [Step 4: Create an AWS KMS key](#oracle-smad-setting-up.step4)
+ [Step 5: Create a Secrets Manager secret](#oracle-smad-setting-up.step5)

## Step 1: Create an Organizational Unit in your AD
<a name="oracle-smad-setting-up.step1"></a>

**Important**  
We recommend that you create a dedicated OU and a service account scoped to that OU for each AWS account that owns an RDS for Oracle DB instance joined to your domain. A dedicated OU and service account avoid conflicting permissions and follow the principle of least privilege.

**To create an OU in your AD**

1. Connect to your AD domain as a domain administrator.

1. Open **Active Directory Users and Computers** and select the domain where you want to create your OU.

1. Open the context menu for the domain, choose **New**, and then choose **Organizational Unit**.

1. Enter a name for the OU, such as `AWS-RDS-OU`. It can't contain shell metacharacters $, `, \|, ; or control characters.

1. Keep **Protect container from accidental deletion** checkbox selected.

1. Choose **OK**. Your new OU appears under your domain.

## Step 2: Create an AD domain service account in your AD
<a name="oracle-smad-setting-up.step2"></a>

You store the credentials of this account in Secrets Manager in Step 5.

**To create an AD domain service account in your AD**

1. Open **Active Directory Users and Computers** and select the domain and OU where you want to create the user.

1. Open the context menu for **Users**, choose **New**, and then choose **User**.

1. Enter a first name, last name, and user logon name for the user, such as `rds-join-svc`. Choose **Next**.

1. Enter a password for the user. Don't select **User must change password at next logon**. Don't select **Account is disabled**. Choose **Next**.

1. Choose **OK**. Your new user appears under your domain.

## Step 3: Delegate control to the AD domain service account
<a name="oracle-smad-setting-up.step3"></a>

You grant most permissions with the Delegation of Control Wizard and grant the remaining attribute permissions with PowerShell.

### Part A: Delegate permissions with the Delegation of Control Wizard
<a name="oracle-smad-setting-up.step3.partA"></a>

**To delegate control to the AD domain service account in your domain**

1. Open the **Active Directory Users and Computers** Microsoft Management Console (MMC) snap-in and select your domain.

1. Open the context menu for the OU that you created in Step 1, and choose **Delegate Control**.

1. On the **Delegation of Control Wizard**, choose **Next**.

1. In the **Users or Groups** section, choose **Add**.

1. In the **Select Users, Computers, or Groups** section, enter the domain service account that you created in Step 2, and choose **Check Names**. If the check succeeds, choose **OK**.

1. In the **Users or Groups** section, confirm that the domain service account appears, and choose **Next**.

1. In the **Tasks to Delegate** section, choose **Create a custom task to delegate**, and choose **Next**.

1. In the **Active Directory Object Type** section:

   1. Choose **Only the following objects in the folder**.

   1. Select **User objects**.

   1. Select **Create selected objects in this folder**.

   1. Select **Delete selected objects in this folder**, and choose **Next**.

1. In the **Permissions** section:

   1. Keep **General** selected.

   1. Select **Property-specific**.

   1. Select **Creation/deletion of specific child objects**.

   1. Select **Read All Properties**.

   1. Select **Reset Password**.

   1. Select **Read msDS-SupportedEncryptionTypes**.

   1. Select **Write msDS-SupportedEncryptionTypes**.

1. On **Completing the Delegation of Control Wizard**, review your settings and choose **Finish**.

### Part B: Delegate servicePrincipalName permissions with PowerShell
<a name="oracle-smad-setting-up.step3.partB"></a>

The Delegation of Control Wizard doesn't expose the `servicePrincipalName` property for user objects. Run the following PowerShell script on a domain controller to grant the domain service account read and write access to `servicePrincipalName` on user objects in the OU.

Replace *service-account* with the name of the domain service account that you created in Step 2, such as `rds-join-svc`, and replace the OU distinguished name with the OU that you created in Step 1.

```
$ou   = "OU=AWS-RDS-OU,DC=corp,DC=example,DC=com"
$user = Get-ADUser "service-account"
$acl  = Get-Acl "AD:$ou"

$schemaPath = (Get-ADRootDSE).schemaNamingContext
$spnSchema = Get-ADObject -SearchBase $schemaPath -Filter {lDAPDisplayName -eq "servicePrincipalName"} -Properties schemaIDGUID
$spnGuid = New-Object Guid (,$spnSchema.schemaIDGUID)
$userGuid = New-Object Guid "bf967aba-0de6-11d0-a285-00aa003049e2"

$ace = New-Object System.DirectoryServices.ActiveDirectoryAccessRule(
   $user.SID,
   "ReadProperty,WriteProperty",
   "Allow",
   $spnGuid,
   "Descendents",
   $userGuid
)

$acl.AddAccessRule($ace)
Set-Acl "AD:$ou" $acl
```

To verify that the permissions applied, run the following PowerShell commands.

```
$acl = Get-Acl "AD:$ou"
$acl.Access | Where-Object { $_.IdentityReference -like "*service-account*" } | Format-List
```

## Step 4: Create an AWS KMS key
<a name="oracle-smad-setting-up.step4"></a>

The AWS KMS key encrypts your Secrets Manager secret.

**Note**  
For Encryption Key, don't use the AWS default AWS KMS key. Be sure to create the AWS KMS key in the same AWS account that contains the RDS for Oracle DB instance that you want to join to your self-managed AD.

**To create an AWS KMS key**

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms/](https://console.aws.amazon.com/kms/), and choose **Create key**.

1. For **Key type**, choose **Symmetric**.

1. For **Key usage**, choose **Encrypt and decrypt**.

1. For **Advanced options**:

   1. For **Key material origin**, choose **KMS**.

   1. For **Regionality**, choose **Single-Region key**, and choose **Next**.

1. For **Alias**, enter a name for the AWS KMS key.

1. (Optional) For **Description**, enter a description of the AWS KMS key.

1. (Optional) For **Tags**, add tags for the AWS KMS key, and choose **Next**.

1. For **Key administrators**, select an IAM user and select it.

1. For **Key deletion**, keep **Allow key administrators to delete this key** selected, and choose **Next**.

1. For **Key users**, select the same IAM user from the previous step and select it. Choose **Next**.

1. Review the configuration.

1. For **Key policy**, add the following to the policy **Statement**.

   ```
   {
       "Sid": "Allow use of the KMS key on behalf of RDS",
       "Effect": "Allow",
       "Principal": {
           "Service": [
               "rds.amazonaws.com"
           ]
       },
       "Action": "kms:Decrypt",
       "Resource": "*"
   }
   ```

1. Choose **Finish**.

## Step 5: Create a Secrets Manager secret
<a name="oracle-smad-setting-up.step5"></a>

**Note**  
Create the secret in the same AWS account and AWS Region as the RDS for Oracle DB instance that you want to join to your domain.

**To create a secret with the console**

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/), and choose **Store a new secret**.

1. For **Secret type**, choose **Other type of secret**.

1. For **Key/value pairs**, add two keys:

   1. For the first key, enter `SELF_MANAGED_ACTIVE_DIRECTORY_USERNAME`.

   1. For the value of the first key, enter the user logon name of the domain service account, without the domain prefix. For example, enter `rds-join-svc`. Do not include the domain name as this causes instance creation to fail.

   1. For the second key, enter `SELF_MANAGED_ACTIVE_DIRECTORY_PASSWORD`.

   1. For the value of the second key, enter the password of the domain service account.

1. For **Encryption key**, choose the AWS KMS key that you created in Step 4, and choose **Next**.

1. For **Secret name**, enter a descriptive name for the secret.

1. (Optional) For **Description**, enter a description of the secret.

1. For **Resource permissions**, choose **Edit**.

1. Add the following policy. Replace `123456789012` with your AWS account ID and `us-west-2` with your AWS Region.
**Note**  
We recommend that you use the `aws:sourceAccount` and `aws:sourceArn` conditions to avoid the confused deputy problem. Use your AWS account for `aws:sourceAccount` and the ARN of your DB instances for `aws:sourceArn`. For more information, see [Preventing cross-service confused deputy problems](cross-service-confused-deputy-prevention.html).

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "rds.amazonaws.com"
               },
               "Action": "secretsmanager:GetSecretValue",
               "Resource": "*",
               "Condition": {
                   "StringEquals": {
                       "aws:sourceAccount": "123456789012"
                   },
                   "ArnLike": {
                       "aws:sourceArn": "arn:aws:rds:us-west-2:123456789012:db:*"
                   }
               }
           }
       ]
   }
   ```

1. Choose **Save**, and then choose **Next**.

1. For **Configure rotation**, keep the default values, and choose **Next**.

1. Review the settings for the secret, and choose **Store**.

1. Choose the secret that you created, and copy the **Secret ARN**. Use this value when you join your DB instance to the domain in [Step 1: Create or modify an Amazon RDS for Oracle DB instance](oracle-smad-connecting.md#oracle-smad.connecting.step1).