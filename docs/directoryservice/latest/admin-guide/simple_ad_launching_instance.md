# Joining an Amazon EC2 Windows instance to your

Simple AD Active Directory

You can launch and join an Amazon EC2 Windows instance to a Simple AD. Alternatively, you
can manually join an existing EC2 Windows instance to a Simple AD

Seamlessly join an EC2 Windows
To seamlessly domain join an EC2 instance, you'll need to complete the following:

###### Prerequisites

- Have an Simple AD To learn more, see [Create your Simple AD](simple_ad_getting_started.md#how_to_create_simple_ad "simple_ad_getting_started.md#how_to_create_simple_ad").
- You'll need the following IAM permissions to seamlessly join an EC2
  Windows instance:
  - IAM Instance Profile with the following IAM permissions:
    - `AmazonSSMManagedInstanceCore`
    - `AmazonSSMDirectoryServiceAccess`

  - The user seamlessly domain joining the EC2 to the Simple AD needs the
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

When your Simple AD is created, a security group is created with inbound and
outbound rules. To learn more about these rules and ports, see [What gets created with your Simple AD](simple_ad_what_gets_created.md "simple_ad_what_gets_created.md"). To seamlessly domain join an
EC2 Windows instance, your VPC where you're launching your instance should allow
the same ports allowed in your Simple AD security group's inbound and outbound
rules.

- Depending on your network security and firewall settings, you could be
  required to allow additional outbound traffic. This traffic would be for HTTPS
  (port 443) to the following endpoints:

| Endpoint                             | Role                                                                                                                                                                                                                  |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ec2messages.`region`.amazonaws.com` | Creates and deletes session channels with Session Manager service. For more<br>information, see [AWS Systems Manager endpoints and<br>quotas](../../../general/latest/gr/ssm.md "../../../general/latest/gr/ssm.md"). |
| `ssm.`region`.amazonaws.com`         | Endpoint for AWS Systems Manager Session Manager. For more information, see [AWS Systems Manager<br>endpoints and quotas](../../../general/latest/gr/ssm.md "../../../general/latest/gr/ssm.md").                     |
| `ssmmessages.`region`.amazonaws.com` | Creates and deletes session channels with Session Manager service. For more<br>information, see [AWS Systems Manager endpoints and<br>quotas](../../../general/latest/gr/ssm.md "../../../general/latest/gr/ssm.md"). |
| `ds.`region`.amazonaws.com`          | Endpoint for Directory Service. For more information, see [Region availability for Directory Service](regions.md "regions.md").                                                                                       |

- We recommend to use a DNS server that will resolve your Simple AD domain
  name. To do so, you can create a DHCP option set. See [Creating a DHCP options set for
  Simple AD](simple_ad_dhcp_options_set.md "simple_ad_dhcp_options_set.md") for more
  information.
  - If you choose not to create a DHCP option set, then your DNS servers will be
    static and configured to by your Simple AD.

1. Sign in to the AWS Management Console and open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation bar, choose the same AWS Region as the existing directory.
3. On the **EC2 Dashboard**, in the **Launch instance** section, choose **Launch instance**.
4. On the **Launch an instance** page, under the **Name and Tags** section, enter the name you would like
   to use for your Windows EC2 instance.
5. (Optional) Choose **Add additional tags** to add one or more tag key-value pairs to organize, track, or control access for this EC2 instance.
6. In the **Application and OS Image (Amazon Machine Image)** section, choose **Windows** in the **Quick Start** pane.
   You can change the Windows Amazon Machine Image (AMI) from the **Amazon Machine Image (AMI)** dropdown list.
7. In the **Instance type** section, choose the instance type you would like to use from **Instance type** dropdown list.
8. In the **Key pair (login)** section, you can either choose to create a new key pair or choose from an existing key pair.
   1. To create a new key pair, choose **Create new key pair**.
   2. Enter a name for the key pair and select an option for the **Key pair type** and **Private key file format**.
   3. To save the private key in a format that can be used with OpenSSH, choose **.pem**.
      To save the private key in a format that can be used with PuTTY, choose **.ppk**.
   4. Choose **create key pair**.
   5. The private key file is automatically downloaded by your browser. Save the private key file in a safe place.

   ###### Important

   This is the only chance for you to save the private key file.

9. On the **Launch an instance** page, under **Network settings** section, choose **Edit**.
   Choose the **VPC** that your directory was created in from the **VPC - _required_** dropdown list.
10. Choose one of the public subnets in your VPC from the **Subnet** dropdown list.
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

![An error message when selecting your Domain join directory. There is an error with your existing SSM document.](/images/directoryservice/latest/admin-guide/images/SSM-Error-Message.png)
This error occurs if the EC2 launch wizard identifies an existing SSM document with unexpected properties. You can do one of the following:

    * If you previously edited the SSM document and the properties are expected, choose close and proceed to launch the EC2 instance with no changes.
    * Select the delete the existing SSM document here link to delete the SSM document. This will allow for the creation of an SSM document with the correct properties.
     The SSM document will automatically be created when you launch the EC2 instance.

15. For **IAM instance profile**, you can select an existing IAM
    instance profile or create a new one. Select an IAM instance profile that has the AWS managed policies
    **AmazonSSMManagedInstanceCore** and
    **AmazonSSMDirectoryServiceAccess** attached to it from the
    **IAM instance profile** dropdown list. To create a new one,
    choose **Create new IAM profile** link, and then do the
    following:
    1.  Choose **Create role**.
    2.  Under **Select trusted entity**, choose **AWS
        service**.
    3.  Under **Use case**, choose **EC2**.
    4.  Under **Add permissions**, in the list of policies, select the
        **AmazonSSMManagedInstanceCore** and
        **AmazonSSMDirectoryServiceAccess** policies. To filter the list,
        type `SSM` in the search box. Choose **Next**.

    ###### Note

    **AmazonSSMDirectoryServiceAccess** provides the permissions
    to join instances to an Active Directory managed by Directory Service.
    **AmazonSSMManagedInstanceCore** provides the minimum
    permissions necessary to use the AWS Systems Manager service. For more information about
    creating a role with these permissions, and for information about other
    permissions and policies you can assign to your IAM role, see [Create an IAM instance profile
    for Systems Manager](../../../systems-manager/latest/userguide/setup-instance-profile.md "../../../systems-manager/latest/userguide/setup-instance-profile.md") in the _AWS Systems Manager User Guide_. 5. On the **Name, review, and create** page, enter a
    **Role name**. You will need this role name to attach to the EC2
    instance. 6. (Optional) You can provide a description of the IAM instance profile in the
    **Description** field. 7. Choose **Create role**. 8. Return to **Launch an instance** page and choose the refresh
    icon next to the **IAM instance profile**. Your new IAM
    instance profile should be visible in the **IAM instance
    profile** dropdown list. Choose the new profile and leave the rest of the
    settings with their default values.

16. Choose **Launch instance**.

Manually join an EC2 Windows To manually join an existing Amazon EC2 Windows instance to a Simple AD Active Directory, the instance must be launched using the parameters as specified in Joining an Amazon EC2 Windows instance to your
Simple AD Active Directory.

You will need the IP addresses of the Simple AD DNS servers. This information can be found under **Directory Services** >
**Directories** > the **Directory ID** link for your directory > **Directory details** and **Networking & Security** sections.

![On the Directory Service console on the directory details page, the IP addresses of the Directory Service provided DNS servers are highlighted.](images/directory_details_highlighted.png)

###### To join a Windows instance to a Simple AD Active Directory

1. Connect to the instance using any Remote Desktop Protocol client.
2. Open the TCP/IPv4 properties dialog box on the instance.
   1. Open **Network Connections**.

   ###### Tip

   You can open **Network Connections** directly
   by running the following from a command prompt on the
   instance.

   ```
   %SystemRoot%\system32\control.exe ncpa.cpl
   ```

   2. Open the context menu (right-click) for any enabled network
      connection and then choose **Properties**.
   3. In the connection properties dialog box, open (double-click)
      **Internet Protocol Version 4**.

3. Select **Use the following DNS server
   addresses**, change the **Preferred DNS server**
   and **Alternate DNS server** addresses to the IP addresses of
   your Simple AD-provided DNS servers, and choose **OK**.

![The Internet Protocol Version 4 (TCP/IPv4) Properties dialog box with the preferred DNS server and alternative DNS server fields highlighted.](images/dns_server_addresses.png) 4. Open the **System Properties** dialog box for the
instance, select the **Computer Name** tab, and choose
**Change**.

###### Tip

You can open the **System Properties** dialog box
directly by running the following from a command prompt on the
instance.

```
%SystemRoot%\system32\control.exe sysdm.cpl
```

5. In the **Member of** field, select
   **Domain**, enter the fully qualified name of your Simple AD
   Active Directory, and choose **OK**.
6. When prompted for the name and password for the domain administrator, enter the
   username and password of an account that has domain join privileges. For more information
   about delegating these privileges, see [Delegating directory join privileges for
   Simple AD](simple_ad_directory_join_privileges.md "simple_ad_directory_join_privileges.md").

###### Note

You can enter either the fully qualified name of your domain or the NetBIOS name, followed by
a backslash (\), and then the username. The username would be **Administrator**. For
example, `corp.example.com\administrator` or `corp\administrator`. 7. After you receive the message welcoming you to the domain, restart the
instance to have the changes take effect.

Now that your instance has been joined to the Simple AD Active Directory domain, you can log into that
instance remotely and install utilities to manage the directory, such as adding
users and groups. The Active Directory Administration Tools can be used to create users and groups. For more information, see [Installing the Active Directory Administration
Tools for Simple AD](simple_ad_install_ad_tools.md "simple_ad_install_ad_tools.md").
