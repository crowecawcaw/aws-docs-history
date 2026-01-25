# Seamlessly joining an Amazon EC2 Linux instance

to your AWS Managed Microsoft AD Active Directory

This procedure seamlessly joins an Amazon EC2 Linux instance to your AWS Managed Microsoft AD Active
Directory. To complete this procedure, you will need to create an AWS Secrets Manager secret which
can incur additional costs. For more information, see [AWS Secrets Manager Pricing](https://aws.amazon.com/secrets-manager/pricing/ "https://aws.amazon.com/secrets-manager/pricing/").

If you need to perform seamless domain join across multiple AWS accounts, you can
optionally choose to enable [Directory sharing](ms_ad_directory_sharing.md "ms_ad_directory_sharing.md").

The following Linux instance distributions and versions are supported:

- Amazon Linux AMI 2018.03.0
- Amazon Linux 2 (64-bit x86)
- Red Hat Enterprise Linux 8 (HVM) (64-bit x86)
- Ubuntu Server 18.04 LTS & Ubuntu Server 16.04 LTS
- CentOS 7 x86-64
- SUSE Linux Enterprise Server 15 SP1

###### Note

Distributions prior to Ubuntu 14 and Red Hat Enterprise Linux 7 and 8 do not support the
seamless domain join feature.

For a demonstration on the process of seamlessly joining a Linux instance to your
AWS Managed Microsoft AD Active Directory, see the following YouTube video.

## Prerequisites

Before you can set up seamless domain join to an EC2 Linux instance, you need to
complete the procedures in these sections.

### Networking prerequisites for

seamless domain join

To seamlessly domain join an EC2 Linux instance, you will need to complete the
following:

- You will need the following IAM permissions to seamlessly join an EC2
  Linux instance:
  - Have an AWS Managed Microsoft AD. To learn more, see [Creating your AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory "ms_ad_getting_started.md#ms_ad_getting_started_create_directory").
  - You'll need the following IAM permissions to seamlessly join an EC2
    Windows instance:
    - IAM Instance Profile with the following IAM permissions:
      - `AmazonSSMManagedInstanceCore`
      - `AmazonSSMDirectoryServiceAccess`

    - The user seamlessly domain joining the EC2 to the AWS Managed Microsoft AD needs the
      following IAM permissions:
      - Directory Service Permissions:
        - `"ds:DescribeDirectories"`
        - `"ds:CreateComputer"`

      - Amazon VPC Permissions:
        - `"ec2:DescribeVpcs"`
        - `"ec2:DescribeSubnets"`
        - `"ec2:DescribeNetworkInterfaces"`
        - `"ec2:CreateNetworkInterface"`
        - `"ec2:AttachNetworkInterface"`

      - EC2 Permissions:
        - `"ec2:DescribeInstances"`
        - `"ec2:DescribeImages"`
        - `"ec2:DescribeInstanceTypes"`
        - `"ec2:RunInstances"`
        - `"ec2:CreateTags"`

      - AWS Systems Manager Permissions:
        - `"ssm:DescribeInstanceInformation"`
        - `"ssm:SendCommand"`
        - `"ssm:GetCommandInvocation"`
        - `"ssm:CreateBatchAssociation"`

- When your AWS Managed Microsoft AD is created, a security group is created with inbound and
  outbound rules. To learn more about these rules and ports, see [What gets created with your
  AWS Managed Microsoft AD](ms_ad_getting_started_what_gets_created.md "ms_ad_getting_started_what_gets_created.md"). To seamlessly domain join an
  EC2 Linux instance, your VPC where you're launching your instance should allow
  the same ports allowed in your AWS Managed Microsoft AD security group's inbound and outbound
  rules.
  - Depending on your network security and firewall settings, you could be
    required to allow additional outbound traffic. This traffic would be for HTTPS
    (port 443) to the following endpoints:

  | Endpoint                                | Role                                                                                                                                                                                                                  |
  | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `ec2messages.`region`.amazonaws.com`    | Creates and deletes session channels with Session Manager service. For more<br>information, see [AWS Systems Manager endpoints and<br>quotas](../../../general/latest/gr/ssm.md "../../../general/latest/gr/ssm.md"). |
  | `ssm.`region`.amazonaws.com`            | Endpoint for AWS Systems Manager Session Manager. For more information, see [AWS Systems Manager<br>endpoints and quotas](../../../general/latest/gr/ssm.md "../../../general/latest/gr/ssm.md").                     |
  | `ssmmessages.`region`.amazonaws.com`    | Creates and deletes session channels with Session Manager service. For more<br>information, see [AWS Systems Manager endpoints and<br>quotas](../../../general/latest/gr/ssm.md "../../../general/latest/gr/ssm.md"). |
  | `ds.`region`.amazonaws.com`             | Endpoint for Directory Service. For more information, see [Region availability for Directory Service](regions.md "regions.md").                                                                                       |
  | `secretsmanager.`region`.amazonaws.com` | Endpoint for AWS Secrets Manager. For more information, see [AWS Secrets Manager<br>endpoints and quotas](../../../general/latest/gr/asm.md "../../../general/latest/gr/asm.md").                                     |

- We recommend to use a DNS server that will resolve your AWS Managed Microsoft AD domain
  name. To do so, you can create a DHCP option set. See [Creating or changing a DHCP options set for
  AWS Managed Microsoft AD](dhcp_options_set.md "dhcp_options_set.md") for more
  information.
  - If you choose not to create a DHCP option set, then your DNS servers will be
    static and configured to by your AWS Managed Microsoft AD.

### Select your seamless domain join service

account

You can seamlessly join Linux computers to your AWS Managed Microsoft AD Active Directory domain. To do
that, you must use a user account with create computer account permissions to join the
machines to the domain. Although members of the _AWS delegated
administrators_ or other groups might have sufficient privileges to join
computers to the domain, we do not recommend using these. As a best practice, we
recommend that you use a service account that has the minimum privileges necessary to
join the computers to the domain.

To delegate an account with the minimum privileges necessary to join the computers
to the domain, you can run the following PowerShell commands. You must run these
commands from a domain-joined Windows computer with the [Installing Active Directory Administration
Tools for AWS Managed Microsoft AD](ms_ad_install_ad_tools.md "ms_ad_install_ad_tools.md") installed.
In addition, you must use an account that has permission to modify the permissions on
your Computers OU or container. The PowerShell command sets permissions allowing the
service account to create computer objects in your domain's default computers
container.

```
$AccountName = 'awsSeamlessDomain'
# DO NOT modify anything below this comment.
# Getting Active Directory information.
Import-Module 'ActiveDirectory'
$Domain = Get-ADDomain -ErrorAction Stop
$BaseDn = $Domain.DistinguishedName
$ComputersContainer = $Domain.ComputersContainer
$SchemaNamingContext = Get-ADRootDSE | Select-Object -ExpandProperty 'schemaNamingContext'
[System.GUID]$ServicePrincipalNameGuid = (Get-ADObject -SearchBase $SchemaNamingContext -Filter { lDAPDisplayName -eq 'Computer' } -Properties 'schemaIDGUID').schemaIDGUID
# Getting Service account Information.
$AccountProperties = Get-ADUser -Identity $AccountName
$AccountSid = New-Object -TypeName 'System.Security.Principal.SecurityIdentifier' $AccountProperties.SID.Value
# Getting ACL settings for the Computers container.
$ObjectAcl = Get-ACL -Path "AD:\$ComputersContainer"
# Setting ACL allowing the service account the ability to create child computer objects in the Computers container.
$AddAccessRule = New-Object -TypeName 'System.DirectoryServices.ActiveDirectoryAccessRule' $AccountSid, 'CreateChild', 'Allow', $ServicePrincipalNameGUID, 'All'
$ObjectAcl.AddAccessRule($AddAccessRule)
Set-ACL -AclObject $ObjectAcl -Path "AD:\$ComputersContainer"
```

If you prefer using a graphical user interface (GUI) you can use the manual process
that is described in [Delegate privileges to your service
account](ad_connector_getting_started.md#connect_delegate_privileges "ad_connector_getting_started.md#connect_delegate_privileges").

### Create the secrets to store the domain service account

You can use AWS Secrets Manager to store the domain service account. For more information, see [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md").

###### Note

There are fees associated with Secrets Manager. For more information see, [Pricing](../../../secretsmanager/latest/userguide/intro.md#asm_pricing "../../../secretsmanager/latest/userguide/intro.md#asm_pricing") in the _AWS Secrets Manager User Guide_.

###### To create secrets and store the domain service account information

1. Sign in to the AWS Management Console and open the AWS Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. Choose **Store a new secret**.
3. On the **Store a new secret** page, do the following:
   1. Under **Secret type**, choose **Other type of
      secrets**.
   2. Under **Key/value pairs**, do the following:
      1. In the first box, enter `awsSeamlessDomainUsername`.
         On the same row, in the next box, enter the username for your service
         account. For example, if you used the PowerShell command previously, the
         service account name would be `awsSeamlessDomain`.

      ###### Note

      You must enter `awsSeamlessDomainUsername` exactly
      as it is. Make sure there are not any leading or ending spaces. Otherwise
      the domain join will fail.

      ![In the AWS Secrets Manager console on the choose a secret type page. Other type of secret is selected under secret type and awsSeamlessDomainUsername is entered as the key value.](images/secrets_manager_1.png) 2. Choose **Add row**. 3. On the new row, in the first box, enter
      `awsSeamlessDomainPassword`. On the same row, in the
      next box, enter the password for your service account.

      ###### Note

      You must enter `awsSeamlessDomainPassword` exactly
      as it is. Make sure there are not any leading or ending spaces. Otherwise
      the domain join will fail. 4. Under **Encryption key,** leave the default value `aws/secretsmanager`.
      AWS Secrets Manager always encrypts the secret when you choose this option. You also may choose a key you created. 5. Choose **Next**.

4. Under **Secret name**, enter a secret name that includes your
   directory ID using the following format, replacing `d-xxxxxxxxx` with your directory ID:

```
`aws/directory-services/`d-xxxxxxxxx`/seamless-domain-join`
```

This will be used to retrieve secrets in the application.

###### Note

You must enter
`aws/directory-services/`d-xxxxxxxxx`/seamless-domain-join`
exactly as it is but replace `d-xxxxxxxxxx` with your
directory ID. Make sure that there are no leading or ending spaces. Otherwise the
domain join will fail.

![In the AWS Secrets Manager console on the configure secret page. The secret name is entered and highlighted.](images/secrets_manager_2.png) 5. Leave everything else set to defaults, and then choose
**Next**. 6. Under **Configure automatic rotation**, choose **Disable
automatic rotation**, and then choose **Next**.

You can turn on rotation for this secret after you store it. 7. Review the settings, and then choose **Store** to save your
changes. The Secrets Manager console returns you to the list of secrets in your account with
your new secret now included in the list. 8. Choose your newly created secret name from the list, and take note of the
**Secret ARN** value. You will need it in the next section.

### Turn on rotation for the domain service

account secret

We recommend that you regularly rotate secrets to improve your security posture.

###### To turn on rotation for the domain service account secret

- Follow the instructions in [Set up automatic rotation
  for AWS Secrets Manager secrets](../../../secretsmanager/latest/userguide/rotate-secrets_turn-on-for-other.md "../../../secretsmanager/latest/userguide/rotate-secrets_turn-on-for-other.md") in the _AWS Secrets Manager User Guide_.

For Step 5, use the rotation template [Microsoft
Active Directory credentials](../../../secretsmanager/latest/userguide/reference_available-rotation-templates.md#template-AD-password "../../../secretsmanager/latest/userguide/reference_available-rotation-templates.md#template-AD-password") in the _AWS Secrets Manager User Guide_.

For help, see [Troubleshoot AWS Secrets Manager rotation](../../../secretsmanager/latest/userguide/troubleshoot_rotation.md "../../../secretsmanager/latest/userguide/troubleshoot_rotation.md")
in the _AWS Secrets Manager User Guide_.

### Create the required IAM policy and role

Use the following prerequisite steps to create a custom policy that allows read-only
access to your Secrets Manager seamless domain join secret (which you created earlier), and to
create a new LinuxEC2DomainJoin IAM role.

#### Create the Secrets Manager IAM read

policy

You use the IAM console to create a policy that grants read-only access to your Secrets Manager secret.

###### To create the Secrets Manager IAM read policy

1. Sign in to the AWS Management Console as a user that has permission to create IAM policies.
   Then open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, **Access Management**, choose **Policies**.
3. Choose **Create policy**.
4. Choose the **JSON** tab and copy the text from the following
   JSON policy document. Then paste it into the **JSON** text
   box.

###### Note

Make sure you replace the Region and Resource ARN with the actual Region and ARN of the
secret that you created earlier.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue",
                "secretsmanager:DescribeSecret"
            ],
            "Resource": [
                "arn:aws:secretsmanager:`us-east-1:xxxxxxxxx`:secret:aws/directory-services/`d-xxxxxxxxx`/seamless-domain-join"
            ]
        }
    ]
}
```

5. When you are finished, choose **Next**. The policy validator reports any syntax errors. For more information, see [Validating IAM policies](../../../IAM/latest/UserGuide/access_policies_policy-validator.md "../../../IAM/latest/UserGuide/access_policies_policy-validator.md").
6. On the **Review policy** page, enter a policy name, such as
   `SM-Secret-Linux-DJ-`d-xxxxxxxxxx`-Read`.
   Review the **Summary** section to see the permissions that your
   policy grants. Then choose **Create policy** to save your changes.
   The new policy appears in the list of managed policies and is now ready to attach to
   an identity.

###### Note

We recommend you create one policy per secret. Doing so ensures that instances
only have access to the appropriate secret and minimizes the impact if an instance is
compromised.

#### Create the LinuxEC2DomainJoin role

You use the IAM console to create the role that you will use to domain join your
Linux EC2 instance.

###### To create the LinuxEC2DomainJoin role

1. Sign in to the AWS Management Console as a user that has permission to create IAM policies.
   Then open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, under **Access Management**, choose **Roles**.
3. In the content pane, choose **Create role**.
4. Under **Select type of trusted entity**, choose **AWS
   service**.
5. Under **Use case**, choose **EC2**, and
   then choose **Next**.

![In the IAM console on the select trusted entity page. AWS service and EC2 are selected.](images/iam-console-trusted-entity.png) 6. For **Filter policies**, do the following:

    1. Enter `AmazonSSMManagedInstanceCore`. Then select the
     check box for that item in the list.
    2. Enter `AmazonSSMDirectoryServiceAccess`. Then select the
     check box for that item in the list.
    3. Enter
     `SM-Secret-Linux-DJ-`d-xxxxxxxxxx`-Read`
     (or the name of the policy that you created in the previous procedure). Then select
     the check box for that item in the list.
    4. After adding the three policies listed above, select **Create role**.###### Note

AmazonSSMDirectoryServiceAccess provides the permissions to
join instances to an Active Directory managed by Directory Service.
AmazonSSMManagedInstanceCore provides the minimum permissions
necessary to use the AWS Systems Manager service. For more information about creating a role
with these permissions, and for information about other permissions and policies you
can assign to your IAM role, see [Create an IAM instance profile for Systems Manager](../../../systems-manager/latest/userguide/setup-instance-profile.md "../../../systems-manager/latest/userguide/setup-instance-profile.md") in the
_AWS Systems Manager User Guide_. 7. Enter a name for your new role, such as `LinuxEC2DomainJoin` or another name that you prefer in the **Role name** field. 8. (Optional) For **Role description**, enter a description. 9. (Optional) Choose **Add new tag** under **Step 3: Add tags** to add tags. Tag key-value pairs are used to organize, track, or control access for this role. 10. Choose **Create role**.

## Seamlessly join your Linux instance

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
