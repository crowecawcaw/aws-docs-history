# Viewing shadow copy storage

You can view the amount of storage currently consumed by shadow copies
on your file system using the `Get-FsxShadowStorage` command in a
remote PowerShell session on your file system. For instructions on launching a
remote PowerShell session on your file system, see [Using the Amazon FSx CLI for PowerShell](administering-file-systems.md#remote-pwrshell "administering-file-systems.md#remote-pwrshell").

```
`[fs-1234567890abcef12]: PS>`PS>Get-fsxshadowstorage
FSx Shadow Storage Configuration

AllocatedSpace UsedSpace    MaxSpace MaxShadowCopyNumber
-------------- ---------    -------- -------------------
             0         0 10737418240                  20

```

The output shows the shadow storage configuration, as follows:

- `AllocatedSpace` – The amount of storage on the file system in bytes
  currently allocated to shadow copies. Initially, this value is 0.
- `UsedSpace` – The amount of storage, in bytes, currently used
  by shadow copies. Initially, this value is 0.
- `MaxSpace` – The maximum amount of storage, in bytes, to which shadow storage
  can grow. This is the value that you set for [shadow copy storage](shadow-copy-storage.md "shadow-copy-storage.md")
  using the `Set-FsxShadowStorage` command.
- `MaxShadowCopyNumber` – The maximum number of shadow copies that the file system can have, from 1-500.
  When the `UsedSpace` amount reaches the maximum shadow copy storage amount configured (`MaxSpace`)
  or the number of shadow copies reaches the maximum shadow copy number configured (`MaxShadowCopyNumber`),
  the next shadow copy that you take replaces the oldest shadow copy. If you don't want to lose your oldest shadow copies,
  monitor your shadow copy storage to make sure that you have sufficient storage space for new shadow copies. If you need more space, you can [delete existing shadow copies](remove-fsxshadow-copies.md "remove-fsxshadow-copies.md") or
  increase the maximum amount of [shadow copy storage](shadow-copy-storage.md "shadow-copy-storage.md").

###### Note

When shadow copies are automatically or manually created, they use the amount of shadow copy storage that you configured as a storage
limit. Shadow copies grow in size over time and utilize the available storage space shown by the CloudWatch `FreeStorageCapacity` metric up
to the maximum shadow copy storage amount configured (`MaxSpace`).
