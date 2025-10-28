# Connect to your Linux instance using SSH

There are multiple ways to connect to your Linux instance using SSH. Some ways depend on the
operating system of the local computer that you connect from. Other methods are
browser-based, such as EC2 Instance Connect or AWS Systems Manager Session Manager, and can be used from any
computer. You can use SSH to connect to your Linux instance and run commands, or use SSH to
transfer files between your local computer and your instance.

Before you connect to your Linux instance using SSH, complete the following
prerequisites:

- Check that your instance has passed its status checks.
  It can take a few minutes for an instance to be ready to accept connection requests.
  For more information, see [View status checks](viewing_status.md "viewing_status.md").
- Ensure that the security group associated with your instance allows incoming SSH traffic
  from your IP address. For more information, see [Rules to connect to instances from your computer](security-group-rules-reference.md#sg-rules-local-access "security-group-rules-reference.md#sg-rules-local-access").
- [Get the required instance details](connection-prereqs-general.md#connection-prereqs-get-info-about-instance "connection-prereqs-general.md#connection-prereqs-get-info-about-instance").
- [Locate the private key and set permissions](connection-prereqs-general.md#connection-prereqs-private-key "connection-prereqs-general.md#connection-prereqs-private-key").
- [(Optional) Get the instance fingerprint](connection-prereqs-general.md#connection-prereqs-fingerprint "connection-prereqs-general.md#connection-prereqs-fingerprint").
  Then, choose from one of the following options to connect to your Linux instance
  using SSH.

- [Connect using an SSH client](connect-linux-inst-ssh.md "connect-linux-inst-ssh.md")
- [Connect using PuTTY](connect-linux-inst-from-windows.md "connect-linux-inst-from-windows.md")
- [Transfer files using SCP](linux-file-transfer-scp.md "linux-file-transfer-scp.md")
  If you can't connect to your instance and need help troubleshooting, see
  [Troubleshoot issues connecting to your Amazon EC2 Linux instance](TroubleshootingInstancesConnecting.md "TroubleshootingInstancesConnecting.md").
