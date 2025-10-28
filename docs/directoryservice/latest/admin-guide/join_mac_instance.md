# Joining an Amazon EC2 Mac instance to your AWS Managed Microsoft AD

Active Directory

This procedure manually joins an Amazon EC2 Mac instance to your AWS Managed Microsoft AD Active
Directory.

## Prerequisites

- Amazon EC2 Mac instances require [Amazon EC2 Dedicated Hosts](../../../AWSEC2/latest/UserGuide/dedicated-hosts-overview.md "../../../AWSEC2/latest/UserGuide/dedicated-hosts-overview.md"). You must allocate a dedicated host and launch an
  instance onto the host. For more information, see [Launch a Mac
  instance](../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md#mac-instance-launch "../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md#mac-instance-launch") in _Amazon EC2 User Guide_.
- We recommend creating a DHCP option set for your AWS Managed Microsoft AD Active Directory. This
  will allow any instances in your Amazon VPC to point to the specified domain and DNS servers
  to resolve their domain names. See [Creating or changing a DHCP options set for
  AWS Managed Microsoft AD](dhcp_options_set.md "dhcp_options_set.md") for more information.

###### Note

Dedicated Host pricing varies by the payment option that you select. For more
information, see [Pricing and Billing](../../../AWSEC2/latest/UserGuide/dedicated-hosts-billing.md "../../../AWSEC2/latest/UserGuide/dedicated-hosts-billing.md")
in _Amazon EC2 User Guide_.

## Manually joining a Mac instance

1. Use the following SSH command to connect to your Mac instance. For more information
   about connecting to your Mac instance, see [Connect
   to your Mac instance.](../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md#connect-to-mac-instance "../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md#connect-to-mac-instance")

```
ssh -i `/path/key-pair-name`.pem ec2-user@`my-instance-public-dns-name`
```

2. After you connect to your Mac instance, create a password for the
   `ec2-user` account using the following command:

```
sudo passwd `ec2-user`
```

3. When prompted at the command line, provide a password for the
   `ec2-user` account. You can update your operating system and
   software by following the procedure in [Update the
   operating system and software](../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md#mac-instance-updates "../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md#mac-instance-updates") in _Amazon EC2 User Guide_.
4. Use the following `dsconfigad` command to join your Mac
   instance to the AWS Managed Microsoft AD Active Directory domain. Make sure to replace the domain
   name, computer name, and organizational unit with your AWS Managed Microsoft AD Active Directory
   domain information. For more information, see [Configuring domain access in Directory Utility on Mac](https://support.apple.com/guide/directory-utility/configure-domain-access-diru11f4f748/mac "https://support.apple.com/guide/directory-utility/configure-domain-access-diru11f4f748/mac") on Apple
   website.

###### Warning

The computer name shouldn't contain a hyphen. Hyphens might prevent the bind to
the AWS Managed Microsoft AD Active Directory.

```
sudo dsconfigad -add `domainName` -computer `computerName` -username `Username` -ou `"Your-AWS-Delegated-Organizational-Unit"`
```

The following example is what the command should look like when joining an
administrative user on a Mac instance named `myec2mac01` to the
`example.com` domain:

```
sudo dsconfigad -add `example.com` -computer `myec2mac01` -username `admin` -ou `"OU=Computers,OU=Example,DC=Example,DC=com"`
```

5. Use the following command to add the **AWS Delegated
   Administrators** to the administrative user on your Mac instance:

```
sudo dsconfigad -group `"EXAMPLE\aws delegated administrators`
```

6. Use the following command to confirm the AWS Managed Microsoft AD Active Directory domain join
   was successful:

```
dsconfigad -show
```

You have successfully joined your Mac instance to your AWS Managed Microsoft AD Active Directory.
You can now log in to your Mac instance using your AWS Managed Microsoft AD Active Directory
credentials.

When you first log in to your Mac instance, you should be provided with an option to log
in as the "Other" user. At this point, you can use your Active Directory domain credentials
to log in to the Mac instance. If you're not provided with "Other" on the log in screen
after completing these steps, log in as ec2-user and then log out.

To log in using the graphical user interface with a domain user, follow the steps in
[Connect to your
instance's graphical user interface (GUI)](../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md#mac-instance-vnc "../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md#mac-instance-vnc") in
_Amazon EC2 User Guide_.
