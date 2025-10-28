# Seamlessly joining an Amazon EC2 Linux

instance to a shared AWS Managed Microsoft AD

In this procedure, you will seamlessly join an Amazon EC2 Linux instance to a shared
AWS Managed Microsoft AD. To do this, you will create an AWS Secrets Manager IAM read policy in the EC2
instance role in the account where you wish to launch the EC2 Linux instance. This will be
referred to as `Account 2` in this procedure. This instance will be using the
AWS Managed Microsoft AD that is being shared from the other account which is referred to as
`Account 1`.

## Prerequisites

Before you can seamlessly join an Amazon EC2 Linux instance to a shared AWS Managed Microsoft AD,
you will need to complete the following:

- Steps 1 through 3 in the tutorial, [Tutorial: Sharing your AWS Managed Microsoft AD
  directory for seamless EC2 domain-join](ms_ad_tutorial_directory_sharing.md "ms_ad_tutorial_directory_sharing.md"). This tutorial walks you through
  setting up your network and sharing your AWS Managed Microsoft AD.
- The procedure outlined in [Seamlessly joining an Amazon EC2 Linux instance
  to your AWS Managed Microsoft AD Active Directory](seamlessly_join_linux_instance.md "seamlessly_join_linux_instance.md").

## Step 1. Create

LinuxEC2DomainJoin role in Account 2

In this step, you will use the IAM console to create the IAM role that
you will use to domain join your EC2 Linux instance while signed in to `Account
 2`.

###### Create the LinuxEC2DomainJoin role

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, under **Access Management**, choose
   **Roles**.
3. On the **Roles** page, choose **Create
   role**.
4. Under **Select type of trusted entity**, choose **AWS
   service**.
5. Under **Use case**, choose **EC2**, and then
   choose **Next**
6. For **Filter policies**, do the following:
   1. Enter `AmazonSSMManagedInstanceCore`. Then select the checkbox for
      that item in the list.
   2. Enter `AmazonSSMDirectoryServiceAccess`. Then select the checkbox
      for that item in the list.
   3. After adding these policies, select **Create role**.

   ###### Note

   `AmazonSSMDirectoryServiceAccess` provides the permissions to
   join instances to an Active Directory managed by AWS Directory Service.
   `AmazonSSMManagedInstanceCore` provides the minimum permissions
   necessary to use AWS Systems Manager. For more information about creating a role with
   these permissions, and for information about other permissions and policies you
   can assign to your IAM role, see [Configure instance permissions required for Systems Manager](../../../systems-manager/latest/userguide/setup-instance-permissions.md "../../../systems-manager/latest/userguide/setup-instance-permissions.md") in the
   _AWS Systems Manager User Guide_.

7. Enter a name for your new role, such as `LinuxEC2DomainJoin` or another
   name that you prefer in the **Role name** field.
8. _(Optional)_ For **Role description**, enter a
   description.
9. _(Optional)_ Choose **Add new tag** under
   **Step 3: Add tags** to add tags. Tag key-value pairs are used to
   organize, track, or control access for this role.
10. Choose **Create role**.

## Step 2. Create cross account

resource access to share AWS Secrets Manager secrets

The next section are additional requirements that need to be met to seamlessly join
EC2 Linux instances with a shared AWS Managed Microsoft AD. These requirements include creating
resource policies and attaching them to the appropriate services and resources.

To allow users in an account to access AWS Secrets Manager secrets in another account, you must
allow access in both a resource policy and identity policy. This type of access is called
[cross
account resource access](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md").

This type of access is different than granting access to identities in the same
account as the Secrets Manager secret. You must also allow the identity to use [AWS Key Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")
(KMS) key that the secret is encrypted with. This permission is necessary as you can't use
the AWS managed key (`aws/secretsmanager`) for cross-account access. Instead,
you will encrypt your secret with a KMS key that you create, and then attach a key
policy to it. To change the encryption key for a secret, see [Modify an AWS Secrets Manager
secret](../../../secretsmanager/latest/userguide/manage_update-secret.md "../../../secretsmanager/latest/userguide/manage_update-secret.md").

###### Note

There are fees associated with AWS Secrets Manager, depending on which secret you use. For the
current complete pricing list, see [AWS Secrets Manager Pricing](https://aws.amazon.com/secrets-manager/pricing/ "https://aws.amazon.com/secrets-manager/pricing/"). You can use the
AWS managed key `aws/secretsmanager` that Secrets Manager creates to encrypt your
secrets for free. If you create your own KMS keys to encrypt your secrets, AWS charges
you at the current AWS KMS rate. For more information, see [AWS Key Management Service Pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

The following steps allow you to create the resource policies to enable users to
seamlessly join a EC2 Linux instance to a shared AWS Managed Microsoft AD.

###### Attach a resource

policy to the secret in Account 1

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. From the list of secrets, choose your **Secret** you created
   during the [Prerequisites](#seamlessly_join_linux_to_shared_MAD_prereqs "#seamlessly_join_linux_to_shared_MAD_prereqs").
3. On the **Secret's details page** under the
   **Overview** tab, scroll down to **Resource
   permissions**.
4. Select **Edit permissions**.
   1. In the policy field, enter the following policy. The following policy allows
      **LinuxEC2DomainJoin** in `Account 2` to access the
      secret in `Account 1`. Replace the ARN value with the ARN value for
      your `Account 2`, `LinuxEC2DomainJoin` role you created in
      [Step 1](#seamlessly_join_linux_to_shared_MAD_step_1 "#seamlessly_join_linux_to_shared_MAD_step_1"). To use
      this policy, see [Attach a permissions policy to an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/auth-and-access_resource-policies.md "../../../secretsmanager/latest/userguide/auth-and-access_resource-policies.md").

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Principal": {
    "AWS": "`arn:aws:iam::123456789012:role/LinuxEC2DomainJoin`"
    },
    "Action": "secretsmanager:GetSecretValue",
    "Resource": "*"
    }
    ]
   }`

   ```

###### Add a statement to the key policy for the KMS key in

Account 1

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. In the left navigation pane, select **Customer managed
   keys**.
3. On the **Customer managed keys** page, select the key you
   created.
4. On the **Key Details** page, navigate to **Key
   policy**, and select **Edit**.
5. The following key policy statement allows `ApplicationRole` in
   `Account 2` to use the KMS key in `Account 1` to decrypt the
   secret in `Account 1`. To use this statement, add it to the key policy for
   your KMS key. For more information, see [Changing a key
   policy](../../../kms/latest/developerguide/key-policy-modifying.md "../../../kms/latest/developerguide/key-policy-modifying.md").

```
{
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "`arn:aws:iam::Account2:role/ApplicationRole`"
  },
  "Action": [
    "kms:Decrypt",
    "kms:DescribeKey"
  ],
  "Resource": "*"
}

```

###### Create an identity policy to the identity in Account 2

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, under **Access management**, select
   **Policies**.
3. Select **Create Policy**. Choose **JSON** in the
   **Policy editor**.
4. The following policy allows `ApplicationRole` in `Account 2`
   to access the secret in `Account 1` and decrypt the secret value by using
   the encryption key which is also in `Account 1`. You can find the ARN for
   your secret in the Secrets Manager console on the **Secret Details** page under
   **Secret ARN**. Alternatively, you can call [describe-secret](../../../cli/latest/reference/secretsmanager/describe-secret.md "../../../cli/latest/reference/secretsmanager/describe-secret.md") to identify the secret's ARN. Replace the Resource ARN with
   the Resource ARN for the secret ARN and `Account 1`. To use this policy,
   see [Attach
   a permissions policy to an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/auth-and-access_resource-policies.md "../../../secretsmanager/latest/userguide/auth-and-access_resource-policies.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "secretsmanager:GetSecretValue",
 "Resource": "arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:`secretName-AbCdEf`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:Describekey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`Your_Encryption_Key`"
 }
 ]
}`

```

5. Select **Next** and then select **Save
   changes**.
6. Find and select the Role you created in `Account 2` in [Attach a resource policy to the secret in Account 1](#step1ResourcePolicy "#step1ResourcePolicy").
7. Under **Add permissions**, select **Attach
   policies**.
8. In the search bar, find the policy you created in [Add a statement to the key policy for the KMS key in Account 1](#step2KeyPolicy "#step2KeyPolicy") and select the box to add the policy to the role. Then
   select **Add permissions**.

## Step 3. Seamlessly

join your Linux instance

You can now use the following procedure to seamlessly join your EC2 Linux instance to
your shared AWS Managed Microsoft AD.

###### To seamlessly join your Linux instance

1. Sign in to the AWS Management Console and open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the Region selector in the navigation bar, choose the same AWS Region as the existing directory.
3. On the **EC2 Dashboard**, in the **Launch instance** section, choose **Launch instance**.
4. On the **Launch an instance** page, under the **Name and Tags** section, enter the name you would like
   to use for your Linux EC2 instance.
5. _(Optional)_ Choose **Add additional tags** to add one or more tag key-value pairs to organize, track, or control access for this EC2 instance.
6. In the **Application and OS Image (Amazon Machine Image)** section, choose a Linux AMI you wish to launch.

###### Note

The AMI used must have AWS Systems Manager (SSM Agent) version
2.3.1644.0 or higher. To check the installed SSM Agent version in your AMI by
launching an instance from that AMI, see [Getting the currently installed SSM Agent version](../../../systems-manager/latest/userguide/ssm-agent-get-version.md "../../../systems-manager/latest/userguide/ssm-agent-get-version.md").
If you need to upgrade the SSM Agent, see [Installing and configuring SSM Agent on EC2 instances for Linux](../../../systems-manager/latest/userguide/sysman-install-ssm-agent.md "../../../systems-manager/latest/userguide/sysman-install-ssm-agent.md").

SSM uses the `aws:domainJoin` plugin when joining a Linux instance to a Active Directory domain. The plugin changes the hostname for the Linux instances to the format EC2AMAZ-`XXXXXXX`.
For more information about `aws:domainJoin`, see [AWS Systems Manager command document plugin reference](../../../systems-manager/latest/userguide/documents-command-ssm-plugin-reference.md#aws-domainJoin "../../../systems-manager/latest/userguide/documents-command-ssm-plugin-reference.md#aws-domainJoin")
in the _AWS Systems Manager User Guide_. 7. In the **Instance type** section, choose the instance type you would like to use from **Instance type** dropdown list. 8. In the **Key pair (login)** section, you can either choose to create a new key pair or choose from an existing key pair. To create a new key pair, choose **Create new key pair**.
Enter a name for the key pair and select an option for the **Key pair type** and **Private key file format**. To save the private key in a format that can be used with OpenSSH, choose **.pem**.
To save the private key in a format that can be used with PuTTY, choose **.ppk**.
Choose **create key pair**. The private key file is automatically downloaded by your browser. Save the private key file in a safe place.

###### Important

This is the only chance for you to save the private key file. 9. On the **Launch an instance** page, under **Network settings** section, choose **Edit**.
Choose the **VPC** that your directory was created in from the **VPC - _required_** dropdown list. 10. Choose one of the public subnets in your VPC from the **Subnet** dropdown list.
The subnet you choose must have all external traffic routed to an internet gateway.
If this is not the case, you won't be able to connect to the instance remotely.

For more information on how to connect to a internet gateway,
see [Connect to the internet using an internet gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") in the
_Amazon VPC User Guide_. 11. Under **Auto-assign public IP**, choose **Enable**.

For more information about public and private IP addressing, see
[Amazon
EC2 instance IP addressing](../../../AWSEC2/latest/WindowsGuide/using-instance-addressing.md "../../../AWSEC2/latest/WindowsGuide/using-instance-addressing.md") in the
_Amazon EC2 User Guide_. 12. For **Firewall (security groups)** settings, you can use the default settings or make changes to meet your needs. 13. For **Configure storage** settings, you can use the default settings or make changes to meet your needs. 14. Select **Advanced details** section, choose your domain from the **Domain join directory** dropdown list.

###### Note

After choosing the Domain join directory, you may see:

![An error message when selecting your Domain join directory. There is an error with your existing SSM document.](images/SSM-Error-Message.png)
This error occurs if the EC2 launch wizard identifies an existing SSM document with unexpected properties. You can do one of the following:

    * If you previously edited the SSM document and the properties are expected, choose close and proceed to launch the EC2 instance with no changes.
    * Select the delete the existing SSM document here link to delete the SSM document. This will allow for the creation of an SSM document with the correct properties.
     The SSM document will automatically be created when you launch the EC2 instance.

15. For **IAM instance profile**, choose the IAM role that you previously created in the prerequisites section **Step 2: Create the LinuxEC2DomainJoin role**.
16. Choose **Launch instance**.

###### Note

If you are performing a seamless domain join with SUSE Linux, a reboot is required before authentications will work. To reboot SUSE from the Linux terminal, type **sudo reboot**.
