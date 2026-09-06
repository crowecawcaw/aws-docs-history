

# Setting up self-managed Active Directory
<a name="db2-self-managed-active-directory.SettingUp"></a>

To set up a self-managed AD, take the following steps.

**Topics**
+ [Step 1: Create an Organizational Unit in your AD](#db2-self-managed-active-directory.SettingUp.CreateOU)
+ [Step 2: Create an AD domain service account in your AD](#db2-self-managed-active-directory.SettingUp.CreateADuser)
+ [Step 3: Delegate control to the AD domain service account](#db2-self-managed-active-directory.SettingUp.DelegateControl)
+ [Step 4: Create an AWS KMS key](#db2-self-managed-active-directory.SettingUp.CreateKMSkey)
+ [Step 5: Create an AWS secret](#db2-self-managed-active-directory.SettingUp.CreateSecret)
+ [Step 6: Create or modify a Db2 DB instance](#db2-self-managed-active-directory.SettingUp.CreateModify)

## Step 1: Create an Organizational Unit in your AD
<a name="db2-self-managed-active-directory.SettingUp.CreateOU"></a>

**Important**  
We recommend creating a dedicated OU and service credential scoped to that OU for any AWS account that owns an RDS for Db2 DB instance joined to your self-managed AD domain. By dedicating an OU and service credential, you can avoid conflicting permissions and follow the principle of least privilege.

**To create an OU in your AD**

1. Connect to your AD domain as a domain administrator.

1. Open **Active Directory Users and Computers** and select the domain where you want to create your OU.

1. Open the context menu for the domain, choose **New**, and then choose **Organizational Unit**.

1. Enter a name for the OU.

1. Keep the box selected for **Protect container from accidental deletion**.

1. Choose **OK**. Your new OU appears under your domain.

## Step 2: Create an AD domain service account in your AD
<a name="db2-self-managed-active-directory.SettingUp.CreateADuser"></a>

Use the domain service account credentials as the secret in AWS Secrets Manager.

**To create an AD domain service account in your AD**

1. Open **Active Directory Users and Computers** and select the domain and OU where you want to create your user.

1. Open the context menu for **Users**, choose **New**, and then choose **User**.

1. Enter a first name, last name, and logon name for the user. Choose **Next**.

1. Enter a password for the user. Don't select **User must change password at next login**. Don't select **Account is disabled**. Choose **Next**.

1. Choose **OK**. Your new user appears under your domain.

## Step 3: Delegate control to the AD domain service account
<a name="db2-self-managed-active-directory.SettingUp.DelegateControl"></a>

### Part A: Delegate permissions using the Delegation of Control Wizard
<a name="db2-self-managed-active-directory.SettingUp.DelegateControl.Wizard"></a>

**To delegate control to the AD domain service account in your domain**

1. Open the **Active Directory Users and Computers** Microsoft Management Console (MMC) snap-in and select the domain where you want to create your user.

1. Open the context menu for the OU that you created earlier, and choose **Delegate Control**.

1. On the **Delegation of Control Wizard**, choose **Next**.

1. On the **Users or Groups** section, choose **Add**.

1. On the **Select Users, Computers, or Groups** section, enter the AD domain service account you created and choose **Check Names**. If your AD domain service account check is successful, choose **OK**.

1. On the **Users or Groups** section, confirm your AD domain service account was added and choose **Next**.

1. On the **Tasks to Delegate** section, choose **Create a custom task to delegate** and choose **Next**.

1. On the **Active Directory Object Type** section:

   1. Choose **Only the following objects in the folder**.

   1. Select **User Objects**.

   1. Select **Create selected objects in this folder**.

   1. Select **Delete selected objects in this folder** and choose **Next**.

1. On the **Permissions** section:

   1. Keep **General** selected.

   1. Select **Property-specific**.

   1. Select **Creation/deletion of specific child objects**.

   1. Select **Reset Password**.

   1. Select **Read msDS-SupportedEncryptionTypes**.

   1. Select **Write msDS-SupportedEncryptionTypes**.

1. For **Completing the Delegation of Control Wizard**, review and confirm your settings and choose **Finish**.

### Part B: Delegate servicePrincipalName permissions using PowerShell
<a name="db2-self-managed-active-directory.SettingUp.DelegateControl.PowerShell"></a>

The Delegation of Control Wizard does not expose the `servicePrincipalName` property for user objects. Run the following PowerShell script on the domain controller to grant the AD domain service account read and write access to `servicePrincipalName` on user objects in the OU.

Replace {{service-account}} with the name of the AD domain service account you created in Step 2, and update the OU distinguished name to match the OU you created in Step 1.

```
$ou = "OU={{my-AD-test-OU}},DC={{my-AD-test}},DC={{my-AD}},DC={{my-domain}}"
$user = Get-ADUser "{{service-account}}"
$acl = Get-Acl "AD:\$ou"

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
Set-Acl "AD:\$ou" $acl
```

To verify that the permissions applied correctly, run the following PowerShell script:

```
$acl = Get-Acl "AD:\$ou"
$acl.Access | Where-Object { $_.IdentityReference -like "*{{service-account}}*" } | Format-List
```

## Step 4: Create an AWS KMS key
<a name="db2-self-managed-active-directory.SettingUp.CreateKMSkey"></a>

The KMS key encrypts your AWS secret.

**Note**  
For **Encryption Key**, don't use the AWS default KMS key. Be sure to create the AWS KMS key in the same AWS account that contains the RDS for Db2 DB instance that you want to join to your self-managed AD.

**To create an AWS KMS key**

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms/](https://console.aws.amazon.com/kms/). Choose **Create key**.

1. For **Key Type**, choose **Symmetric**.

1. For **Key Usage**, choose **Encrypt and decrypt**.

1. For **Advanced options**:

   1. For **Key material origin**, choose **KMS**.

   1. For **Regionality**, choose **Single-Region key** and choose **Next**.

1. For **Alias**, provide a name for the KMS key.

1. (Optional) For **Description**, provide a description of the KMS key.

1. (Optional) For **Tags**, provide a tag for the KMS key and choose **Next**.

1. For **Key administrators**, provide the name of an IAM user and select it.

1. For **Key deletion**, keep the box selected for **Allow key administrators to delete this key** and choose **Next**.

1. For **Key users**, provide the same IAM user from the previous step and select it. Choose **Next**.

1. Review the configuration.

1. For **Key policy**, include the following to the policy **Statement**:

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

## Step 5: Create an AWS secret
<a name="db2-self-managed-active-directory.SettingUp.CreateSecret"></a>

**Note**  
Be sure to create the secret in the same AWS account that contains the RDS for Db2 DB instance that you want to join to your self-managed AD.

**To create a secret**

1. Open the AWS Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/). Choose **Store a new secret**.

1. For **Secret type**, choose **Other type of secret**.

1. For **Key/value pairs**, add your two keys:

   1. For the first key, enter `SELF_MANAGED_ACTIVE_DIRECTORY_USERNAME`.

   1. For the value of the first key, enter only the username (without the domain prefix) of the AD user. Do not include the domain name as this causes instance creation to fail.

   1. For the second key, enter `SELF_MANAGED_ACTIVE_DIRECTORY_PASSWORD`.

   1. For the value of the second key, enter the password that you created for the AD user on your domain.

1. For **Encryption key**, enter the KMS key that you created in a previous step and choose **Next**.

1. For **Secret name**, enter a descriptive name that helps you find your secret later.

1. (Optional) For **Description**, enter a description for the secret name.

1. For **Resource permission**, choose **Edit**.

1. Add the following policy to the permission policy:
**Note**  
We recommend that you use the `aws:sourceAccount` and `aws:sourceArn` conditions in the policy to avoid the *confused deputy* problem. Use your AWS account for `aws:sourceAccount` and the RDS for Db2 DB instance ARN for `aws:sourceArn`. For more information, see [Preventing cross-service confused deputy problems](cross-service-confused-deputy-prevention.md).

   ```
   {
       "Version":"2012-10-17",
       "Statement":
       [
           {
               "Effect": "Allow",
               "Principal":
               {
                   "Service": "rds.amazonaws.com"
               },
               "Action": "secretsmanager:GetSecretValue",
               "Resource": "*",
               "Condition":
               {
                   "StringEquals":
                   {
                       "aws:sourceAccount": "123456789012"
                   },
                   "ArnLike":
                   {
                       "aws:sourceArn": "arn:aws:rds:us-west-2:123456789012:db:*"
                   }
               }
           }
       ]
   }
   ```

1. Choose **Save** then choose **Next**.

1. For **Configure rotation settings**, keep the default values and choose **Next**.

1. Review the settings for the secret and choose **Store**.

1. Choose the secret you created and copy the value for the **Secret ARN**. Use this value in the next step to set up self-managed Active Directory.

## Step 6: Create or modify a Db2 DB instance
<a name="db2-self-managed-active-directory.SettingUp.CreateModify"></a>

You can use the AWS CLI to associate an RDS for Db2 DB instance with a self-managed AD domain. You can do this in one of the following ways:
+ Create a new Db2 DB instance using the [create-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) CLI command. For instructions, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md).
+ Modify an existing Db2 DB instance using the [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) CLI command. For instructions, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md).

When you use the AWS CLI, the following parameters are required for the DB instance to be able to use the self-managed AD domain that you created:
+ For the `--domain-fqdn` parameter, use the fully qualified domain name (FQDN) of your self-managed AD.
+ For the `--domain-ou` parameter, use the OU that you created in your self-managed AD.
+ For the `--domain-auth-secret-arn` parameter, use the value of the Secret ARN that you created in a previous step.
+ For the `--domain-dns-ips` parameter, use the primary and secondary IPv4 addresses of the DNS servers for your self-managed AD. If you don't have a secondary DNS server IP address, enter the primary IP address twice.

The following CLI command creates a new RDS for Db2 DB instance and joins it to a self-managed AD domain.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-instance-identifier {{my-DB-instance}} \
    --db-instance-class db.m6i.large \
    --allocated-storage 50 \
    --engine db2-se \
    --engine-version 11.5 \
    --master-username {{my-master-username}} \
    --master-user-password {{my-master-password}} \
    --domain-fqdn {{my_AD_domain.my_AD.my_domain}} \
    --domain-ou {{OU=my-AD-test-OU,DC=my-AD-test,DC=my-AD,DC=my-domain}} \
    --domain-auth-secret-arn "arn:aws:secretsmanager:{{region}}:{{account-number}}:secret:{{my-AD-test-secret-123456}}" \
    --domain-dns-ips "{{10.11.12.13}}" "{{10.11.12.14}}"
```

For Windows:

```
aws rds create-db-instance ^
    --db-instance-identifier {{my-DB-instance}} ^
    --db-instance-class db.m6i.large ^
    --allocated-storage 50 ^
    --engine db2-se ^
    --engine-version 11.5 ^
    --master-username {{my-master-username}} ^
    --master-user-password {{my-master-password}} ^
    --domain-fqdn {{my_AD_domain.my_AD.my_domain}} ^
    --domain-ou {{OU=my-AD-test-OU,DC=my-AD-test,DC=my-AD,DC=my-domain}} ^
    --domain-auth-secret-arn "arn:aws:secretsmanager:{{region}}:{{account-number}}:secret:{{my-AD-test-secret-123456}}" ^
    --domain-dns-ips "{{10.11.12.13}}" "{{10.11.12.14}}"
```