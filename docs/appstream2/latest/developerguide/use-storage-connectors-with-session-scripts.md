# Use Storage Connectors

with Session Scripts

When AppStream 2.0 storage connectors are enabled, they begin mounting when the session
start scripts run. If your script relies on the storage connectors being mounted,
you can wait for the connectors to be available. AppStream 2.0 maintains the mount status
of the storage connectors in the Windows registry on Windows instances, at the
following key:

HKEY_LOCAL_MACHINE\SOFTWARE\Amazon\AppStream\Storage\<provided user
name>\<Storage connector>

The registry key values are as follows:

- Provided user name — The user ID provided through the access mode.
  The access modes and value for each mode are as follows:
  - User Pool — The email address for the user
  - Streaming URL — The UserID
  - SAML — The NameID. If the user name includes a slash (for
    example, a domain user’s SAMAccountName), the slash is replaced by a
    "-" character.

- Storage connector — The connector for the persistent storage option
  that is enabled for the user. The storage connector values are as
  follows:

      + HomeFolder
      + GoogleDrive
      + OneDrive

  Each storage connector registry key contains a **MountStatus**
  DWORD value. The following table lists the possible values for
  **MountStatus**.

###### Note

To view these registry keys, you must have Microsoft .NET Framework version
4.7.2 or later installed on your image.

| Value | Description                                                |
| ----- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0     | Storage connector not be enabled for this user             |
| 1     | Storage connector mounting is in progress                  |
| 2     | Storage connector mounted successfully                     |
| 3     | Storage connector mounting failed                          |
| 4     | Storage connector mounting is enabled, but not mounted yet | On Linux instances, you can check the home folder mount status by looking at the value of appstream_home_folder_mount_status in the file ~/.config/appstream-home-folder/appstream-home-folder-mount-status. |
| Value | Description                                                |
| ---   | ---                                                        |
| True  | Home folder is mounted successfully                        |
| False | Home folder is not mounted yet                             |
