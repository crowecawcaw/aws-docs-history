# MSFTSEC03-BP03 Use Trusted Platform Module (TPM) technology for

hardware-based security on your instances

The AWS Nitro Trusted Platform Module (NitroTPM) is a virtual TPM
2.0 device that's fully integrated with the AWS Nitro System,
providing hardware-based security features for EC2 instances running
Windows Server 2016 and later, as well as supported Linux
distributions. It enables secure boot functionality, disk
encryption, and enhanced protection of sensitive data and keys
directly through the operating system.

When enabled on instance launch, NitroTPM allows Windows to use
BitLocker disk encryption, measured boot capabilities, and Windows
Hello for Business authentication. The TPM functionality is
implemented through the Nitro security chip, which processes
cryptographic operations and sensitive key material in an isolated,
hardware-protected environment separate from the instance's CPU and
hypervisor. This hardware-based root of trust helps meet
requirements for regulated workloads and supports Windows security
features that require TPM 2.0, including Windows Defender System
Guard, Credential Guard, and Device Guard.

NitroTPM integrates with Windows' built-in security tools and
third-party applications that rely on TPM capabilities, making it
particularly valuable for enterprises requiring enhanced security
posture for their Windows workloads on AWS. Additionally, NitroTPM
supports attestation capabilities, allowing applications to verify
the integrity and authenticity of the platform, which is essential
for zero-trust architectures and confidential computing scenarios.

**Desired outcome:** Implement
hardware-based security capabilities through TPM technology that
provides a secure foundation for cryptographic operations, secure
boot processes, and enhanced protection of sensitive keys and
credentials in Microsoft workloads on AWS.

**Common anti-patterns:**

- Deploying Windows workloads without enabling TPM capabilities,
  missing opportunities to use hardware-based security features
  that provide stronger protection than software-only solutions.
- Using software-based encryption and key storage without the
  additional security layer provided by hardware security modules,
  potentially exposing keys to compromise through software
  vulnerabilities.
- Failing to integrate TPM capabilities with Windows security
  features, limiting the effectiveness of built-in security
  technologies that depend on hardware-based trust anchors.

**Benefits of establishing this best
practice:**

- Enhanced security through hardware-based cryptographic
  operations that provide stronger protection for encryption keys
  and sensitive data compared to software-only solutions.
- Improved compliance capabilities through hardware-based
  attestation and secure boot features that help meet regulatory
  requirements for high-security environments.
- Strengthened Windows security features through TPM integration
  that enables advanced capabilities like Credential Guard, Device
  Guard, and Windows Hello for Business authentication.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing TPM technology for Microsoft workloads requires
enabling NitroTPM during EC2 instance launch and configuring
Windows security features to use the hardware-based capabilities.
Focus on integrating TPM with existing security controls and
Windows features to maximize security benefits.

### Implementation steps

1. Enable NitroTPM when launching new EC2 instances running
   Windows Server 2016 or later, verifying that the instance
   type supports TPM functionality and is built on the AWS
   Nitro System.
2. Deploy EC2 Instances with NitroTPM Using AWS CloudFormation.
3. Integrate AWS KMS with NitroTPM for Enhanced Key Management
   for runtime attestation and system integrity protection
   against firmware and kernel-level attacks.
4. Configure AWS Systems Manager for TPM-enabled Microsoft
   workloads to secure credential storage and certificate-based
   authentication capabilities.
5. Implement Credential Guard to protect domain credentials and
   other sensitive authentication information using TPM-based
   virtualization security.
6. Set up secure boot functionality that uses TPM to verify the
   integrity of the boot process and block unauthorized code
   execution during startup.
7. Configure monitoring and logging using AWS CloudTrail,
   Amazon CloudWatch, and Windows event logs to track TPM
   usage, key operations, and security events related to
   hardware-based security features.
8. Establish procedures for TPM endorsement key management and
   disaster recovery, understanding that NitroTPM keys are
   instance-specific and require proper backup strategies for
   encrypted data.
9. Implement AWS IAM Roles Anywhere for certificate-based
   authentication.

## Resources

**Related documents:**

- [Amazon EC2 now supports NitroTPM and UEFI Secure Boot](https://aws.amazon.com/blogs/aws/amazon-ec2-now-supports-nitrotpm-and-uefi-secure-boot/ "https://aws.amazon.com/blogs/aws/amazon-ec2-now-supports-nitrotpm-and-uefi-secure-boot/")
- [Credential
  Guard for Windows instances](../../../AWSEC2/latest/UserGuide/credential-guard.md "../../../AWSEC2/latest/UserGuide/credential-guard.md")
- [Windows
  TPM 2.0 Overview](https://docs.microsoft.com/en-us/windows/security/information-protection/tpm/trusted-platform-module-overview "https://docs.microsoft.com/en-us/windows/security/information-protection/tpm/trusted-platform-module-overview")

**Related tools:**

- [IAM
  Roles Anywhere Credential Helper - GitHub Repository](https://github.com/aws/rolesanywhere-credential-helper "https://github.com/aws/rolesanywhere-credential-helper")
- [IAM
  Roles Anywhere Credential Helper - Configuration
  Examples](https://github.com/aws/rolesanywhere-credential-helper/tree/main/examples "https://github.com/aws/rolesanywhere-credential-helper/tree/main/examples")
- [BitLocker
  Drive Encryption](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview "https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview")
- [Windows
  Defender System Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows "https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows")
