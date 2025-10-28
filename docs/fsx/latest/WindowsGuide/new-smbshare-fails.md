# New-FSxSmbShare command fails with a one-way trust

Amazon FSx does not support executing the `New-FSxSmbShare` PowerShell command in cases where you
have a one-way trust and the domain in which the user resides is not configured to trust the domain associated with Amazon FSx file system.

You can resolve this situation using one of following solutions:

- The user executing the `New-FSxSmbShare` command needs to be in the same domain as the FSx file system.
- You can use the fsmgmt.msc GUI to create shares on your file system. For more information, see [Managing file shares with the Shared Folders GUI](managing-file-shares.md#shared-folders-tool "managing-file-shares.md#shared-folders-tool").
