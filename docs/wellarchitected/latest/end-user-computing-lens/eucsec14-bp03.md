# EUCSEC14-BP03 Limit egress channels available to users to only the required set of channels to perform their role

End user systems can provide multiple channels for users to
export and access data. Evaluate these channels to determine
their suitability in the specific use case being delivered.
Block channels not required for specific use cases.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- **Encrypt streaming and control data
  traffic using strong ciphers**: To protect data
  confidentiality, WorkSpaces using PCoIP are encrypted
  using an AES 128-bit cipher by default. For encryption up
  to AES 256-bit see
  [Data
  protection in Amazon WorkSpaces](../../../workspaces/latest/adminguide/data-protection.md "../../../workspaces/latest/adminguide/data-protection.md"). Evaluate your
  security requirements and use stronger ciphers where
  necessary. For Windows, you can implement this using the
  Group Policy template, and for Linux WorkSpaces, the
  appropriate configuration file needs to be edited to
  increase the default level of encryption. For example, for
  PCoIP Amazon Linux 2 WorkSpaces, edit the
  /etc/pcoip-agent/pcoip-agent.conf file.
- WorkSpaces using the Amazon DCV protocol have streaming
  and control data in-transit encrypted using DTLS 1.3
  encryption for UDP traffic and TLS 1.3 encryption for TCP
  traffic with AES-256 ciphers. For details of the
  implementation, see
  [Data
  protection in Amazon WorkSpaces](../../../workspaces/latest/adminguide/data-protection.md "../../../workspaces/latest/adminguide/data-protection.md").
- **Restrict data access to required
  functionality within Amazon WorkSpaces**: To
  protect data on the endpoint used to connect to an Amazon WorkSpaces session and the WorkSpace itself, enable data
  exportation features only when needed and allowed to
  users. For example, Amazon WorkSpaces can block copying
  in-session clipboard contents to the endpoint, copying of
  files between client and WorkSpace, and block printers
  attached to the endpoint from being mapped into the
  session. The blocking of these capabilities can remove
  these potential data exportation vectors from the Amazon WorkSpaces service.
- The implementation of these controls is through Group
  Policy on Windows WorkSpaces, editing the
  /etc/pcoip-agent/pcoip-agent.conf file on Amazon Linux 2
  WorkSpaces using PCoIP, or editing the /etc/wsp/wsp.conf
  file on Ubuntu Amazon WorkSpaces using Amazon DCV. For
  details on how to configure clipboard and other settings
  on Windows WorkSpaces, see
  [Manage
  your Windows WorkSpaces in WorkSpaces Personal](../../../workspaces/latest/adminguide/group_policy.md "../../../workspaces/latest/adminguide/group_policy.md").
- **Restrict data access to required
  functionality within Amazon WorkSpaces Applications**: To
  protect data on the endpoint used to connect to an Amazon
  WorkSpaces Applications session and the WorkSpaces Applications instance
  itself, implement controls to close potential inbound or
  outbound channels that are not required by the users
  connecting to the service. The service has controls to
  configure the clipboard, file transfer, printing to a
  local device, and file system redirection. You can
  configure each of these options on an WorkSpaces Applications stack
  and disable them when not required. For details on
  configuring data access restrictions with Amazon AppStream
  2.0, see
  [Create
  an Amazon WorkSpaces Applications Fleet and Stack](../../../appstream2/latest/developerguide/set-up-stacks-fleets.md#set-up-stacks-fleets-install "../../../appstream2/latest/developerguide/set-up-stacks-fleets.md#set-up-stacks-fleets-install").
