

# Managing DNS aliases on existing file systems
<a name="manage-aliases-existing-fs"></a>

You can add and remove aliases on existing FSx for Windows File Server file systems using the AWS Management Console and AWS CLI, as described in the following procedures.

## To manage file system DNS aliases (console)
<a name="w2aac20c25c39b5b1"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. Navigate to **File systems**, and choose the Windows file system that you want to manage DNS aliases for.

1. On the **Network & security** tab, choose **Manage** for **DNS aliases** to display the **Manage DNS aliases** window.
   + To associate DNS aliases – In the **Associate new aliases** box, enter the DNS aliases that you want to associate. Choose **Associate**. 
   + To disassociate DNS aliases – In the **Current aliases** list, choose the aliases to disassociate from. Choose **Disassociate**.

   You can monitor the status of the aliases you have managed in the **Current aliases** list. Refresh the list to update the status. It takes up to 2.5 minutes for an alias to be associated or disassociated with a file system.

1. When the alias is **Available**, you can access your file system using the DNS alias by configuring service principal names (SPNs) and updating or creating a DNS CNAME record for the alias. For more information, see [Accessing data using DNS aliases](dns-aliases.md).

## To associate DNS aliases with existing file systems (CLI)
<a name="w2aac20c25c39b5b3"></a>

1. Use the `associate-file-system-aliases` CLI command or the [AssociateFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_AssociateFileSystemAliases.html) API operation to associate DNS aliases with an existing file system. 

   The following CLI request associates two aliases with the specified file system.

   ```
   aws fsx associate-file-system-aliases \
     --file-system-id fs-0123456789abcdef0 \
     --aliases financials.corp.example.com transfers.corp.example.com
   ```

   The response shows the status of the aliases that Amazon FSx is associating with the file system.

   ```
   {
       "Aliases": [
           {
               "Name": "financials.corp.example.com",
               "Lifecycle": CREATING
           },
           {
               "Name": "transfers.corp.example.com",
               "Lifecycle": CREATING
           }
       ]
   }
   ```

1. Use the `describe-file-system-aliases` CLI command ([DescribeFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileSystemAliases.html) is the equivalent API operation) to monitor the status of the aliases that you are associating.

1. When the `Lifecycle` has a value of AVAILABLE (a process that can take up to 2.5 minutes), you can access your file system using the DNS alias by configuring service principal names (SPNs) and updating or creating a DNS CNAME record for the alias. For more information, see [Accessing data using DNS aliases](dns-aliases.md).

## To disassociate DNS aliases from file systems (CLI)
<a name="w2aac20c25c39b5b5"></a>
+ Use the `disassociate-file-system-aliases` CLI command or the [DisassociateFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DisassociateFileSystemAliases.html) API operation to disassociate DNS aliases from an existing file system. 

  The following command disassociates one alias from a file system.

  ```
  aws fsx disassociate-file-system-aliases \
    --file-system-id fs-0123456789abcdef0 \
    --aliases financials.corp.example.com
  ```

  The response shows the status of the aliases that Amazon FSx is disassociating from the file system.

  ```
  {
      "Aliases": [
          {
              "Name": "financials.corp.example.com",
              "Lifecycle": DELETING
          }
      ]
  }
  ```

  Use the `describe-file-system-aliases` CLI command ([DescribeFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileSystemAliases.html) is the equivalent API operation) to monitor the status of the aliases. It takes up to 2.5 minutes for the alias to be deleted.