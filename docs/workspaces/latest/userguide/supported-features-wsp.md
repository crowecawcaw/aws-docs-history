

# Supported DCV features for WorkSpaces
<a name="supported-features-wsp"></a>

The following table compares the features that are supported by the DCV WorkSpaces clients.

**Note**  
Android and iPad clients aren't currently supported by DCV WorkSpaces.


| Feature | Windows client | MacOS client | Linux client | Web access | Notes | 
| --- | --- | --- | --- | --- | --- | 
| WorkSpaces Pool support | ✓ | ✓ | ✗ | ✓ | On client version 5.20.0 or greater. | 
| Client access restriction | ✓ | ✓ | ✓ | ✓ |  [ Control device access](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-directory-details.html#control-device-access)  | 
| USB redirection | ✓ | ✗ | ✗ | ✗ | On Windows client version 5.30.0 or greater. | 
| Audio input | ✓ | ✓ | ✓ | ✓ | Not supported on Amazon Linux DCV WorkSpaces but supported on Ubuntu, Rocky Linux, and Red Hat Enterprise Linux WorkSpaces. See [ Manage your Linux WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage_modern_linux_workspaces.html) for more information. | 
| Video input | ✓ | ✓ | ✓ | ✓ | Not supported on Amazon Linux 2 DCV WorkSpaces and Red Hat Enterprise Linux WorkSpaces but supported on Ubuntu and Rocky Linux WorkSpaces. See [ Manage your Linux WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage_modern_linux_workspaces.html) for more information. | 
| Storage redirection | ✗ | ✗ | ✗ | ✗ |  | 
| Local printer redirection | ✓ | ✓ | ✓ | ✗ | [ Print from a WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/userguide/printing.html) | 
| Clipboard redirection | ✓ | ✓ | ✓ | ✓ | Copy and paste on iPad and Android supports text and HTML content only. | 
| HIPAA/PCI compliance | ✓ | ✓ | ✓ | ✓ | [ Compliance and Security FAQ](https://aws.amazon.com/workspaces/faqs/#Compliance_and_Security) | 
| Active directory authentication | ✓ | ✓ | ✓ | ✓ | [ Manage directories for WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage-workspaces-directory.html) | 
| SAML 2.0 | ✓ | ✓ | ✓ | ✓ |  | 
| Certificate-based Authentication | ✓ | ✓ | ✓ | ✓ |  | 
| Multi-factor authentication (MFA) | ✓ | ✓ | ✓ | ✓ | [ Compliance and Security FAQ](https://aws.amazon.com/workspaces/faqs/#Compliance_and_Security) | 
| Smart card (CAC and PIV readers) | ✓ | ✓ | ✗ | ✗ | [ WorkSpaces client smart card support](https://docs.aws.amazon.com/workspaces/latest/userguide/smart_card_support.html) | 
| Certificate for access control | ✓ | ✓ | ✓ | ✗ | [ Configure the restriction](https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html#configure-restriction) | 
| Encryption at rest | ✓ | ✓ | ✓ | ✓ | [Encryption FAQ](https://aws.amazon.com/workspaces/faqs/#Encryption) | 
| Client customization available | ✓ | ✓ | ✓ | ✓ | [ Customize WorkSpaces branding](https://docs.aws.amazon.com/workspaces/latest/adminguide/customize-branding.html) | 
| WebAuthn support | ✓ | ✓ | ✓ | ✗ | [WebAuthn authentication for WorkSpaces client](webauthn_support.md) | 
| Monitor support |  [ Windows display support](https://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-windows-client.html#windows-display-support)  |  [ macOS display support](https://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-osx-client.html#osx-display-support)  |  [ Linux display support](https://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-linux-client.html#linux-display-support) |  [ Web access client views](https://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-web-access.html#web-access-views)  |  | 
| File transfer support  | ✓ | ✗ | ✓ | ✓ | [File transfer support in the WorkSpaces client applications](file-transfer.md)Only available for personal and Windows WorkSpaces. Unavailable for pooled and Linux WorkSpaces. | 
| Idle disconnect timeout | ✓ | ✓ | ✓ | ✓ | [Configure idle disconnect timeout for DCV ](https://docs.aws.amazon.com/workspaces/latest/adminguide/group_policy.html#idle-disconnect)Not supported on Linux WorkSpaces. | 
| AWS Global Accelerator (AGA) support | ✓ | ✓ | ✓ | ✓ | On Windows and Mac client version 5.23.0 or greater. On Linux client version 2024.7 or greater. | 