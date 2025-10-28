# Validate the AMS service (SALZ)

To validate that the AWS Managed Services (AMS) service is working as expected, some exercise that you can do are described in this chapter.

## DNS friendly bastion names

MALZ
For Multi-account landing zone (MALZ), DNS records are created for the bastions in the FQDN of the AMS-managed
Active Directory. AMS replaces Linux and Windows bastions as required. For example, if
there is a new bastion AMI that must be deployed, the bastion DNS records dynamically update to point to new, valid bastions.

1. To access SSH (Linux) bastions, use DNS records like this:
   `sshbastion`(1-4)`.`Your_Domain`.com`

For example, where the domain is `Your_Domain`:

    * `sshbastion1.`Your_Domain`.com`
    * `sshbastion2.`Your_Domain`.com`
    * `sshbastion3.`Your_Domain`.com`
    * `sshbastion4.`Your_Domain`.com`

2. To access RDP (Windows) bastions, use DNS records like this:
   `rdp-`Username`.`Your_Domain`.com`.

For example, where the user name is `alex`, `test`,
`demo`, or `bob`, and the domain is
``Your_Domain`.com`:

    * `rdp-alex.`Your_Domain`.com`
    * `rdp-test.`Your_Domain`.com`
    * `rdp-demo.`Your_Domain`.com`
    * `rdp-bob.`Your_Domain`.com`

SALZ
Single-account landing zone (SALZ) replaces Linux and Windows bastions as required. For example, if
there is a new bastion AMI that must be deployed, the bastion DNS records dynamically update
to point to new, valid bastions.

1. To access SSH (Linux) bastions, use DNS records like this:
   `sshbastion`(1-4)`.A`AccountNumber`.amazonaws.com.`

For example, where `123456789012` is the account number:

    * `sshbastion1.A123456789012.amazonaws.com`
    * `sshbastion2.A123456789012.amazonaws.com`
    * `sshbastion3.A123456789012.amazonaws.com`
    * `sshbastion4.A123456789012.amazonaws.com`

2. To access RDP (Windows) bastions, use DNS records like this:
   `rdpbastion`(1-4)`.A`ACCOUNT_NUMBER`.amazonaws.com`.

For example, where `123456789012` is the account number:

    * `rdpbastion1.A123456789012.amazonaws.com`
    * `rdpbastion2.A123456789012.amazonaws.com`
    * `rdpbastion3.A123456789012.amazonaws.com`
    * `rdpbastion4.A123456789012.amazonaws.com`

## Finding bastion IP addresses

AMS customers can use SSH and RDP bastions, either the [DNS friendly bastion names](#dns-bastions "#dns-bastions") described previously,
or bastion IP addresses.

To find bastion IP addresses, SSH and RDP, for your account:

1. For multi-account landing zone only: Log in to the Shared Services account.
2. Open the EC2 Console and choose **Running Instances**.

The **Instances** page opens. 3. In the filter box at the top, enter either **ssh-bastion** or
**rdp-bastion**.

In the filter box at the top, enter either
**customer-ssh** or **customer-rdp**.

The SSH and/or RDP bastions for your account display.

Note that in addition to your SSH bastions, you may see AMS
perimeter network bastions in the list, which are unavailable for this. 4. Select an SSH or RDP bastion. If you're using a Windows computer and want to log in to a Linux
instance, you use an SSH bastion. If you want to log in to a Windows instance, you use
an RDP bastion. If you're on a Linux OS and want to log in to a Windows instance, you
use an SSH bastion through an RDP tunnel (this is so you can access the Windows
desktop). To access a Linux instance from a Linux OS, you use an SSH bastion.
