# Creating a link to an S3 bucket

The following procedures walk you through the process of creating a data repository
association for an FSx for Lustre file system to an existing S3 bucket, using the
AWS Management Console and AWS Command Line Interface (AWS CLI). For information on adding permissions to an S3 bucket
in order to link it to your file system,
see [Adding permissions to use data repositories in
Amazon S3](setting-up.md#fsx-adding-permissions-s3 "setting-up.md#fsx-adding-permissions-s3").

###### Note

Data repositories cannot be linked to file systems that have file system backups
enabled. Disable backups before linking to a data repository.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Follow the procedure for creating a new file system described in
   [Step 1: Create your FSx for Lustre file system](getting-started.md#getting-started-step1 "getting-started.md#getting-started-step1") in the Getting Started section.
3. Open the **Data Repository Import/Export - _optional_** section.
   The feature is disabled by default.
4. Choose **Import data from and export data to S3**.
5. In the **Data repository association information** dialog,
   provide information for the following fields.
   - **File system path**: Enter the name of a high-level
     directory (such as `/ns1`) or subdirectory (such as
     `/ns1/subdir`) within the Amazon FSx file system that will be associated
     with the S3 data repository. The leading forward slash in the path is required.
     Two data repository associations cannot have overlapping file system paths. For
     example, if a data repository is associated with file system path
     `/ns1`, then you cannot link another data repository with file
     system path `/ns1/ns2`. The **File system path**
     setting must be unique across all the data repository associations for the file
     system.
   - **Data repository path**: Enter the path of an existing S3
     bucket or prefix to associate with your file system (for example,
     `s3://amzn-s3-demo-bucket/my-prefix`). Two data repository associations cannot
     have overlapping data repository paths. The **Data repository path**
     setting must be unique across all the data repository associations for the file system.
   - **Import metadata from repository**: Select this property
     to optionally run an import data repository task to import metadata immediately
     after the link is created.

6. For **Import settings - optional**, set an **Import
   Policy** that determines how your file and directory listings are kept up
   to date as you add, change, or delete objects in your S3 bucket. For example, choose
   **New** to import metadata to your file system for new objects
   created in the S3 bucket. For more information on import policies, see [Automatically import updates from your S3
   bucket](autoimport-data-repo-dra.md "autoimport-data-repo-dra.md").
7. For **Export policy**, set an export policy that determines how
   your files are exported to your linked S3 bucket as you add, change, or delete
   objects in your file system. For example, choose **Changed** to
   export objects whose content or metadata has been changed on your file system. For
   more information about export policies, see [Automatically export updates to your S3
   bucket](autoexport-data-repo-dra.md "autoexport-data-repo-dra.md").
8. Continue with the next section of the file system creation wizard.
9. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
10. From the dashboard, choose **File systems** and then select the
    file system that you want to create a data repository association for.
11. Choose the **Data repository** tab.
12. In the **Data repository associations** pane, choose
    **Create data repository association**.
13. In the **Data repository association information** dialog,
    provide information for the following fields.
    - **File system path**: Enter the name of a high-level
      directory (such as `/ns1`) or subdirectory (such as
      `/ns1/subdir`) within the Amazon FSx file system that will be associated
      with the S3 data repository. The leading forward slash in the path is required.
      Two data repository associations cannot have overlapping file system paths. For
      example, if a data repository is associated with file system path
      `/ns1`, then you cannot link another data repository with file
      system path `/ns1/ns2`. The **File system path**
      setting must be unique across all the data repository associations for the file
      system.
    - **Data repository path**: Enter the path of an existing S3
      bucket or prefix to associate with your file system (for example,
      `s3://amzn-s3-demo-bucket/my-prefix`). Two data repository associations cannot
      have overlapping data repository paths. The **Data repository path**
      setting must be unique across all the data repository associations for the file system.
    - **Import metadata from repository**: Select this property
      to optionally run an import data repository task to import metadata immediately
      after the link is created.

14. For **Import settings - optional**, set an **Import
    Policy** that determines how your file and directory listings are kept up
    to date as you add, change, or delete objects in your S3 bucket. For example, choose
    **New** to import metadata to your file system for new objects
    created in the S3 bucket. For more information about import policies, see [Automatically import updates from your S3
    bucket](autoimport-data-repo-dra.md "autoimport-data-repo-dra.md").
15. For **Export policy**, set an export policy that determines how
    your files are exported to your linked S3 bucket as you add, change, or delete
    objects in your file system. For example, choose **Changed** to
    export objects whose content or metadata has been changed on your file system. For
    more information about export policies, see [Automatically export updates to your S3
    bucket](autoexport-data-repo-dra.md "autoexport-data-repo-dra.md").
16. Choose **Create**.
    The following example creates a data repository association that links an Amazon FSx file system to an S3
    bucket, with an import policy that imports any new or changed files to the file system
    and an export policy that exports new, changed, or deleted files to the linked S3
    bucket.

- To create a data repository association, use the Amazon FSx CLI command
  `create-data-repository-association`, as shown following.

```
`$` aws fsx create-data-repository-association \
      --file-system-id fs-0123456789abcdef0 \
      --file-system-path /ns1/path1/ \
      --data-repository-path s3://amzn-s3-demo-bucket/myprefix/ \
      --s3 "AutoImportPolicy={Events=[NEW,CHANGED,DELETED]},AutoExportPolicy={Events=[NEW,CHANGED,DELETED]}"
```

Amazon FSx returns the JSON description of the DRA immediately. The DRA is created
asynchronously.

You can use this command to create a data repository association even before
the file system has finished creating. The request will be queued and the data
repository association will be created after the file system is available.
