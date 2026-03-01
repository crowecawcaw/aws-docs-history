# Enable and Administer Custom Shared Folders (Server Message Block (SMB) Network Drives) for Your WorkSpaces Applications Users

You can enable one or more options for your organization. When you enable and map the
Server Message Block (SMB) network drives, multiple users can access the same data from
Windows WorkSpaces Applications sessions. Any changes that users make to SMB network drives during those
sessions are automatically backed up and synchronized.

###### Note

- Server Message Block (SMB) network drives mapping are supported only on
  domain-joined fleets
- To use this feature, you must use an WorkSpaces Applications image that uses the WorkSpaces Applications agent
  released after September 18, 2024. For more information, see
  [Manage WorkSpaces Applications Agent Versions](base-images-agent.md "base-images-agent.md") and
  [WorkSpaces Applications Base Image and Managed Image Update Release Notes](base-image-version-history.md "base-image-version-history.md").
  Before you map Server Message Block (SMB) network drives, ensure that for inbound rules,
  the security group that your users use to connect to fleets exposes TCP port 445 (SMB protocol)
  to the domain controller and the security group.

###### Contents

- [Map Server Message Block (SMB) Network Drives](map-smb-network-drives.md "map-smb-network-drives.md")
