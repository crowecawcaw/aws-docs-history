# Networking protocols and access for WorkSpaces Personal

As a WorkSpace administrator, you must understand how to manage WorkSpaces networking and
access, beginning with protocols.

## Protocols for WorkSpaces Personal

Amazon WorkSpaces supports two protocols: PCoIP and DCV. The protocol that you choose
depends on several factors, such as the type of devices your users will be accessing their
WorkSpaces from, which operating system is on your WorkSpaces, what network conditions your
users will be facing, and whether your users require bidirectional video support.

### Requirements

DCV WorkSpaces are only supported with the following minimum
requirements.

Host agent requirements:

- Windows host agent version 2.0.0.312 or above
- Ubuntu host agent version 2.1.0.501 or above
- Amazon Linux 2 host agent version 2.0.0.596 or above
- Rocky Linux host agent version 2.1.0.1628 or above
- Red Hat Enterprise Linux host agent version 2.1.0.1628 or above

Client requirements:

- Windows native client version 5.1.0.329 or higher
- macOS native client version 5.5.0 or higher
- Ubuntu 22.04 client version 2024.x or higher
- Amazon WorkSpaces Thin Client (For more information, see the [Amazon WorkSpaces Thin Client Documentation](../../../workspaces-thin-client.md "../../../workspaces-thin-client.md"))
- Web Access

For more information about how to check your WorkSpace client version and host agent version, see the
[FAQ](https://aws.amazon.com/workspaces/faqs/#:~:text=Q%3A%20How%20do%20I%20find%20my%20WSP%20host%20agent%20version%3F "https://aws.amazon.com/workspaces/faqs/#:~:text=Q%3A%20How%20do%20I%20find%20my%20WSP%20host%20agent%20version%3F").

### When to use DCV

- If you need higher loss/latency tolerance to support your end user network conditions. For example,
  you have users who are accessing their WorkSpaces across global distances or using unreliable networks.
- If you need your users to authenticate with smart cards or to use smart cards
  in-session.
- If you need webcam support capabilities in-session.
- If you need to use Web Access with the Windows Server 2022-powered WorkSpaces bundle.
- If you need to use Ubuntu WorkSpaces.
- If you need to use Windows 11 BYOL WorkSpaces.
- If you need to use Windows or Ubuntu GPU-based bundles (Graphics.g4dn and GraphicsPro.g4dn).
- If you need your users to authenticate in-session with WebAuthn authenticators such as YubiKey or Windows Hello.

### When to use PCoIP

- If you want to use the iPad or Android Linux clients.
- If you use Teradici zero client devices.
- If you need to use GPU-based bundles (Graphics.g4dn, GraphicsPro.g4dn, Graphics, or GraphicsPro).
- If you need to use a Linux bundle for non-smart card use cases.
- If you need to use WorkSpaces in the China (Ningxia) Region.

###### Note

- A directory can have a mix of PCoIP and DCV WorkSpaces in it.
- A user can have both a PCoIP and a DCV WorkSpace as long as the two WorkSpaces are located
  in separate directories. The same user cannot have a PCoIP and a DCV WorkSpace in the same directory.
  For more information about creating multiple WorkSpaces for a user, see
  [Create multiple WorkSpaces for a user in WorkSpaces Personal](create-multiple-workspaces-for-user.md "create-multiple-workspaces-for-user.md").
- You can migrate a WorkSpace between the two protocols by using the WorkSpaces migration feature,
  which requires a rebuild of the WorkSpace. For more information, see
  [Migrate a WorkSpace in WorkSpaces Personal](migrate-workspaces.md "migrate-workspaces.md").
- If your WorkSpace was created with PCoIP bundles you can modify the streaming protocol to migrate between the
  two protocols without requiring a rebuild, while retaining the root volume. For more information, see
  [Modify protocols](modify-workspaces.md#modify_protocols "modify-workspaces.md#modify_protocols").
- For the best experience with video conferencing we recommend using Power, PowerPro,
  GeneralPurpose.4xlarge, or GeneralPurpose.8xlarge bundles only.

The following topics offer additional detail about how to manage networking and access for WorkSpaces Personal:
