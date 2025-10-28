# Reset the Windows administrator password for an Amazon EC2 Windows instance

If you are no longer able to connect to your Amazon EC2 Windows instance because the Windows
administrator password is lost or expired, you can reset the password.

###### Note

There is an AWS Systems Manager Automation document that automatically applies the manual steps
necessary to reset the local administrator password. For more information, see [Reset passwords and SSH keys on EC2 instances](../../../systems-manager/latest/userguide/automation-ec2reset.md "../../../systems-manager/latest/userguide/automation-ec2reset.md")
in the _AWS Systems Manager User Guide_.

The manual methods to reset the administrator password use EC2Launch v2, EC2Config, or EC2Launch.

- For all supported Windows AMIs that include the EC2Launch v2 agent, use
  EC2Launch v2.
- For Windows AMIs before Windows Server 2016, use the EC2Config service.
- For Windows Server 2016 and later AMIs, use the EC2Launch service.
  These procedures also describe how to connect to an instance if you lost the key pair that
  was used to create the instance. Amazon EC2 uses a public key to encrypt a piece of data, such as
  a password, and a private key to decrypt the data. The public and private keys are known as
  a _key pair_. With Windows instances, you use a key pair to obtain the
  administrator password and then log in using RDP.

###### Note

If you have disabled the local administrator account on the instance and your instance
is configured for Systems Manager, you can also re-enable and reset your local administrator
password by using EC2Rescue and Run Command. For more information, see [Use EC2Rescue for Windows Server with
Systems Manager Run Command](ec2rw-ssm.md "ec2rw-ssm.md").

###### Contents

- [Reset Windows admin password for
  EC2 instance using EC2Launch v2](ResettingAdminPassword_EC2Launchv2.md "ResettingAdminPassword_EC2Launchv2.md")
- [Reset Windows admin password for
  EC2 instance using EC2Launch](ResettingAdminPassword_EC2Launch.md "ResettingAdminPassword_EC2Launch.md")
- [Reset Windows admin password for
  EC2 instance using EC2Config](ResettingAdminPassword_EC2Config.md "ResettingAdminPassword_EC2Config.md")
