

# Updating data repository association settings
<a name="update-dra-settings"></a>

You can update an existing data repository association's settings using the AWS Management Console, the AWS CLI, and the Amazon FSx API, as shown in the following procedures.

**Note**  
You cannot update the `File system path` or `Data repository path` of a DRA after it's created. If you want to change the `File system path` or `Data repository path`, you must delete the DRA and create it again.

## To update settings for an existing data repository association (console)
<a name="update-dra-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. From the dashboard, choose **File systems**, and then select the file system that you want to manage.

1. Choose the **Data repository** tab.

1. In the **Data repository associations** pane, choose the data repository association you want to change.

1. Choose **Update**. An edit dialog displays for the data repository association.

1. For **Import settings - optional**, you can update your **Import Policy**. For more information on import policies, see [Automatically import updates from your S3 bucket](autoimport-data-repo-dra.md).

1. For **Export settings - optional**, you can update your export policy. For more information on export policies, see [Automatically export updates to your S3 bucket](autoexport-data-repo-dra.md).

1. Choose **Update**.

## To update settings for an existing data repository association (CLI)
<a name="update-dra-cli"></a>
+ To update a data repository association, use the Amazon FSx CLI command `update-data-repository-association`, as shown following.

  ```
  $ aws fsx update-data-repository-association \
        --association-id 'dra-872abab4b4503bfc2' \
        --s3 "AutoImportPolicy={Events=[NEW,CHANGED,DELETED]},AutoExportPolicy={Events=[NEW,CHANGED,DELETED]}"
  ```

After successfully updating the data repository association's import and export policies, Amazon FSx returns the description of the updated data repository association as JSON.