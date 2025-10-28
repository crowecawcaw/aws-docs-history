# Working with Microsoft Active Directory

in FSx for ONTAP

Amazon FSx works with Microsoft Active Directory to integrate with your existing environments. Active
Directory is the Microsoft directory service that's used to store information about objects on
the network, and to help administrators and users to find and use this information. These
objects typically include shared resources, such as file servers and network user and computer
accounts.

You can optionally join your FSx for ONTAP storage virtual machines (SVMs) to your Active Directory domain to
provide user authentication and file- and folder-level access control. Server message block
(SMB) clients can then use their existing user identities in Active Directory to authenticate themselves and
access SVM volumes. Your users can use their existing identities to control access to individual
files and folders. In addition, you can migrate your existing files and folders and their
security access control list (ACL) configurations to Amazon FSx without any modifications.

If the Microsoft Active Directory domain infrastructure is not available, you can configure a Server Message Block (SMB) server
in a workgroup on an SVM as an alternative to joining an SVM to a Microsoft Active Directory. For more information, see
[Setting up an SMB server in a workgroup](smb-server-workgroup-setup.md "smb-server-workgroup-setup.md").

When you join Amazon FSx for NetApp ONTAP to an Active Directory, you join the file system's SVMs to the Active Directory independently. This means
that you can have a file system with some SVMs that are joined to an Active Directory, and other SVMs that are
not.

After an SVM is joined to an Active Directory, you can update the following Active Directory configuration properties:

- DNS server IP addresses
- Self-managed Active Directory service account username and password

###### Topics

- [Prerequisites for joining an SVM to a
  self-managed Microsoft AD](self-manage-prereqs.md "self-manage-prereqs.md")
- [Best practices for working with Active Directory](self-managed-AD-best-practices.md "self-managed-AD-best-practices.md")
- [How joining SVMs to Microsoft Active Directory works](self-managed-AD-join.md "self-managed-AD-join.md")
- [Managing SVM Active Directory configurations](manage-svm-ad-config.md "manage-svm-ad-config.md")
