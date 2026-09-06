

# Files and Directories Associated with Compute-Intensive Applications
<a name="storage-solutions-files-directories-associated-with-compute-intensive-applications"></a>

During WorkSpaces Applications streaming sessions, saving large files and directories associated with compute-intensive applications to persistent storage can take longer than saving files and directories required for basic productivity applications. For example, it might take longer for applications to save a large amount of data or frequently modify the same files than it would to save files created by applications that perform a single write action. It might also take longer to save many small files.

If your users save files and directories associated with compute-intensive applications and WorkSpaces Applications persistent storage options aren't performing as expected, we recommend that you use a Server Message Block (SMB) solution such as Amazon FSx for Windows File Server or an AWS Storage Gateway file gateway. Following are examples of files and directories associated with compute-intensive applications that are more suitable for use with these SMB solutions:
+ Workspace folders for integrated development environments (IDEs)
+ Local database files
+ Scratch space folders created by graphics simulation applications

For more information, see:
+  [*Amazon FSx for Windows File Server Windows User Guide*](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)
+ [Using Amazon FSx with Amazon WorkSpaces Applications ](https://aws.amazon.com/blogs/desktop-and-application-streaming/using-amazon-fsx-with-amazon-appstream-2-0/)
+ [File gateways](https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html#file-gateway-concepts) in the *AWS Storage Gateway User Guide*