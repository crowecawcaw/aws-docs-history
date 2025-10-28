# UEFI Secure Boot for Amazon EC2 instances

UEFI Secure Boot builds on the long-standing secure boot process of Amazon EC2, and provides
additional defense-in-depth that helps customers secure software from threats that
persist across reboots. It ensures that the instance only boots software that is signed
with cryptographic keys. The keys are stored in the key database of the [UEFI non-volatile variable store](uefi-variables.md "uefi-variables.md"). UEFI Secure Boot
prevents unauthorized modification of the instance boot flow.

###### Contents

- [How UEFI Secure Boot works with Amazon EC2 instances](how-uefi-secure-boot-works.md "how-uefi-secure-boot-works.md")
- [Requirements for UEFI Secure Boot on Amazon EC2](launch-instance-with-uefi-sb.md "launch-instance-with-uefi-sb.md")
- [Verify whether an Amazon EC2 instance is enabled for
  UEFI Secure Boot](verify-uefi-secure-boot.md "verify-uefi-secure-boot.md")
- [Create a Linux AMI with custom UEFI Secure
  Boot keys](create-ami-with-uefi-secure-boot.md "create-ami-with-uefi-secure-boot.md")
- [Create the AWS binary blob for UEFI Secure Boot](aws-binary-blob-creation.md "aws-binary-blob-creation.md")
