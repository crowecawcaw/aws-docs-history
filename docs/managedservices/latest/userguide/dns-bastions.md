# DNS friendly bastion names

AWS Managed Services (AMS) uses DNS friendly bastion names.

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
