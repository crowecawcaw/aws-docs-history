# Setting up self-managed Active Directory

To set up a self-managed AD, take the following steps.

###### Topics

- [Step 1: Create an Organizational Unit in your AD](#USER_SQLServer_SelfManagedActiveDirectory.SettingUp.CreateOU "#USER_SQLServer_SelfManagedActiveDirectory.SettingUp.CreateOU")
- [Step 2: Create an AD domain service account in your AD](#USER_SQLServer_SelfManagedActiveDirectory.SettingUp.CreateADuser "#USER_SQLServer_SelfManagedActiveDirectory.SettingUp.CreateADuser")
- [Step 3: Delegate control to the AD domain service account](#USER_SQLServer_SelfManagedActiveDirectory.SettingUp.DelegateControl "#USER_SQLServer_SelfManagedActiveDirectory.SettingUp.DelegateControl")
- [Step 4: Create an AWS KMS key](#USER_SQLServer_SelfManagedActiveDirectory.SettingUp.CreateKMSkey "#USER_SQLServer_SelfManagedActiveDirectory.SettingUp.CreateKMSkey")
- [Step 5: Create an AWS secret](#USER_SQLServer_SelfManagedActiveDirectory.SettingUp.CreateSecret "#USER_SQLServer_SelfManagedActiveDirectory.SettingUp.CreateSecret")

## Step 1: Create an Organizational Unit in your AD

###### Important

We recommend creating a dedicated OU and service credential scoped to that OU for any AWS account that
owns an RDS for SQL Server DB instance joined your self-managed AD domain. By dedicating an OU and service credential, you can avoid
conflicting permissions and follow the principal of least privilege.

###### To create an OU in your AD

1. Connect to your AD domain as a domain administrator.
2. Open **Active Directory Users and Computers** and
   select the domain where you want to create your OU.
3. Right-click the domain and choose **New**, then **Organizational Unit**.
4. Enter a name for the OU.
5. Keep the box selected for **Protect container from accidental deletion**.
6. Click **OK**. Your new OU will appear under your domain.

## Step 2: Create an AD domain service account in your AD

The domain service account credentials will be used for the secret in AWS Secrets Manager.

###### To create an AD domain service account in your AD

1. Open **Active Directory Users and Computers** and
   select the domain and OU where you want to create your user.
2. Right-click the **Users** object and choose **New**, then **User**.
3. Enter a first name, last name, and logon name for the user. Click **Next**.
4. Enter a password for the user. Don't select **"User must change password at next login"**.
   Don't select **"Account is disabled"**. Click **Next**.
5. Click **OK**. Your new user will appear under your domain.

## Step 3: Delegate control to the AD domain service account

###### To delegate control to the AD domain service account in your domain

1. Open **Active Directory Users and Computers** MMC snap-in and
   select the domain where you want to create your user.
2. Right-click the OU that you created earlier and choose **Delegate Control**.
3. On the **Delegation of Control Wizard**, click **Next**.
4. On the **Users or Groups** section, click **Add**.
5. On the **Select Users, Computers, or Groups** section, enter the AD domain service account you created and click **Check Names**.
   If your AD domain service account check is successful, click **OK**.
6. On the **Users or Groups** section, confirm your AD domain service account was added and click **Next**.
7. On the **Tasks to Delegate** section, choose **Create a custom task to delegate** and click **Next**.
8. On the **Active Directory Object Type** section:
   1. Choose **Only the following objects in the folder**.
   2. Select **Computer Objects**.
   3. Select **Create selected objects in this folder**.
   4. Select **Delete selected objects in this folder** and click **Next**.

9. On the **Permissions** section:
   1. Keep **General** selected.
   2. Select **Validated write to DNS host name**.
   3. Select **Validated write to service principal name** and click **Next**.
   4. To enable Kerberos authentication, keep
      **Property-specific** selected and select
      **Write servicePrincipalName** from the
      list.

10. For **Completing the Delegation of Control Wizard**,
    review and confirm your settings and click
    **Finish**.
11. For Kerberos authentication, open the DNS Manager and open **Server**
    properties.
    1. In the Windows dialog box, type `dnsmgmt.msc`.
    2. Add the AD domain service account under the
       **Security** tab.
    3. Select the **Read** permission and apply your
       changes.

## Step 4: Create an AWS KMS key

The KMS key is used to encrypt your AWS secret.

###### To create an AWS KMS key

###### Note

For **Encryption Key**, don't use the AWS default KMS key.
Be sure to create the AWS KMS key in the same AWS account that contains the RDS for SQL Server DB instance that you want
to join to your self-managed AD.

1. In the AWS KMS console, choose **Create key**.
2. For **Key Type**, choose **Symmetric**.
3. For **Key Usage**, choose **Encrypt and decrypt**.
4. For **Advanced options**:
   1. For **Key material origin**, choose **KMS**.
   2. For **Regionality**, choose **Single-Region key** and click **Next**.

5. For **Alias**, provide a name for the KMS key.
6. (Optional) For **Description**, provide a description of the KMS key.
7. (Optional) For **Tags**, provide a tag the KMS key and click **Next**.
8. For **Key administrators**, provide the name of an IAM user and select it.
9. For **Key deletion**, keep the box selected for **Allow key administrators to delete this key** and click **Next**.
10. For **Key users**, provide the same IAM user from the previous step and select it. Click **Next**.
11. Review the configuration.
12. For **Key policy**, include the following to the policy **Statement**:

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

13. Click **Finish**.

## Step 5: Create an AWS secret

###### To create a secret

###### Note

Be sure to create the secret in the same AWS account that contains the RDS for SQL Server DB instance that you want
to join to your self-managed AD.

1. In AWS Secrets Manager, choose **Store a new secret**.
2. For **Secret type**, choose **Other type of secret**.
3. For **Key/value pairs**, add your two keys:
   1. For the first key, enter `SELF_MANAGED_ACTIVE_DIRECTORY_USERNAME`.
   2. For the value of the first key, enter only the username (without the domain prefix) of the AD user.
      Do not include the domain name as this causes instance creation to fail.
   3. For the second key, enter `SELF_MANAGED_ACTIVE_DIRECTORY_PASSWORD`.
   4. For the value of the second key, enter the password that you created for the AD user on your domain.

4. For **Encryption key**, enter the KMS key that you created in a previous step and click **Next**.
5. For **Secret name**, enter a descriptive name that helps you find your secret later.
6. (Optional) For **Description**, enter a description for the secret name.
7. For **Resource permission**, click **Edit**.
8. Add the following policy to the permission policy:

###### Note

We recommend that you use the `aws:sourceAccount` and `aws:sourceArn` conditions in the policy
to avoid the _confused deputy_ problem. Use your AWS account for `aws:sourceAccount` and
the RDS for SQL Server DB instance ARN for `aws:sourceArn`. For more information, see [Preventing cross-service confused deputy problems](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").

JSON

```
`{
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
 "aws:sourceAccount": "`123456789012`"
 },
 "ArnLike":
 {
 "aws:sourceArn": "arn:aws:rds:`us-west-2`:`123456789012`:`db:*`"
 }
 }
 }
 ]
}`

```

9. Click **Save** then click **Next**.
10. For **Configure rotation settings**, keep the default values and choose **Next**.
11. Review the settings for the secret and click **Store**.
12. Choose the secret you created and copy the value for the **Secret ARN**. This will be used in the next step to set up self-managed Active Directory.
