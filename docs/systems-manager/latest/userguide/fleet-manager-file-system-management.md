AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Working with OS file systems

using Fleet Manager

You can use Fleet Manager, a tool in AWS Systems Manager, to work with the file system on your
managed nodes. Using Fleet Manager, you can view information about the directory and file
data stored on the volumes attached to your managed nodes. For example, you can view
the name, size, extension, owner, and permissions for your directories and files. Up
to 10,000 lines of file data can be previewed as text from the Fleet Manager console. You
can also use this feature to `tail` files. When using `tail`
to view file data, the last 10 lines of the file are displayed initially. As new
lines of data are written to the file, the view is updated in real time. As a
result, you can review log data from the console, which can improve the efficiency
of your troubleshooting and systems administration. Additionally, you can create
directories and copy, cut, paste, rename, or delete files and directories.

We recommend creating regular backups, or taking snapshots of the Amazon Elastic Block Store
(Amazon EBS) volumes attached to your managed nodes. When copying, or cutting and pasting
files, existing files and directories in the destination path with the same name as
the new files or directories are replaced. Serious problems can occur if you replace
or modify system files and directories. AWS doesn't guarantee that these problems
can be solved. Modify system files at your own risk. You're responsible for all file
and directory changes, and ensuring you have backups. Deleting or replacing files
and directories can't be undone.

###### Note

Fleet Manager uses Session Manager, a tool in AWS Systems Manager, to view text previews and
`tail` files. For Amazon Elastic Compute Cloud (Amazon EC2) instances, the instance
profile attached to your managed instances must provide permissions for Session Manager
to use this feature. For more information about adding Session Manager permissions to
an instance profile, see [Add
Session Manager permissions to an existing IAM role](getting-started-add-permissions-to-existing-profile.md "getting-started-add-permissions-to-existing-profile.md").

###### Topics

- [Viewing the OS file system
  using Fleet Manager](fleet-manager-viewing-file-system.md "fleet-manager-viewing-file-system.md")
- [Previewing OS files using
  Fleet Manager](fleet-manager-preview-os-files.md "fleet-manager-preview-os-files.md")
- [Tailing OS files using
  Fleet Manager](fleet-manager-tailing-os-files.md "fleet-manager-tailing-os-files.md")
- [Copying, cutting, and
  pasting OS files or directories using Fleet Manager](fleet-manager-move-files-or-directories.md "fleet-manager-move-files-or-directories.md")
- [Renaming OS files
  and directories using Fleet Manager](fleet-manager-renaming-files-and-directories.md "fleet-manager-renaming-files-and-directories.md")
- [Deleting OS files
  and directories using Fleet Manager](fleet-manager-deleting-files-and-directories.md "fleet-manager-deleting-files-and-directories.md")
- [Creating OS directories
  using Fleet Manager](fleet-manager-creating-directories.md "fleet-manager-creating-directories.md")
- [Cutting, copying, and
  pasting OS directories using Fleet Manager](fleet-manager-managing-directories.md "fleet-manager-managing-directories.md")
