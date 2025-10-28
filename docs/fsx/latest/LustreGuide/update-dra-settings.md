# Updating data repository association settings

You can update an existing data repository association's settings using the
AWS Management Console, the AWS CLI, and the Amazon FSx API, as shown in the following procedures.

###### Note

You cannot update the `File system path` or `Data repository
 path` of a DRA after it's created. If you want to change the `File
 system path` or `Data repository path`, you must delete the DRA and
create it again.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. From the dashboard, choose **File systems**, and then select
   the file system that you want to manage.
3. Choose the **Data repository** tab.
4. In the **Data repository associations** pane, choose the data
   repository association you want to change.
5. Choose **Update**. An edit dialog displays for the
   data repository association.
6. For **Import settings - optional**, you can update your
   **Import Policy**. For more information on import policies, see
   [Automatically import updates from your S3
   bucket](autoimport-data-repo-dra.md "autoimport-data-repo-dra.md").
7. For **Export settings - optional**, you can update your export
   policy. For more information on export policies, see [Automatically export updates to your S3
   bucket](autoexport-data-repo-dra.md "autoexport-data-repo-dra.md").
8. Choose **Update**.

- To update a data repository association, use the Amazon FSx CLI command
  `update-data-repository-association`, as shown following.

```
`$` aws fsx update-data-repository-association \
      --association-id 'dra-872abab4b4503bfc2' \
      --s3 "AutoImportPolicy={Events=[NEW,CHANGED,DELETED]},AutoExportPolicy={Events=[NEW,CHANGED,DELETED]}"
```

After successfully updating the data repository association's import and export policies, Amazon FSx returns the
description of the updated data repository association as JSON.
