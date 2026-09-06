

# Deleting an association to an S3 bucket
<a name="delete-linked-dra"></a>

The following procedures walk you through the process of deleting a data repository association from an existing Amazon FSx file system to an existing S3 bucket, using the AWS Management Console and AWS Command Line Interface (AWS CLI). Deleting the data repository association unlinks the file system from the S3 bucket.

## To delete a link from a file system to an S3 bucket (console)
<a name="delete-dra-console-dra"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. From the dashboard, choose **File systems** and then select the file system that you want to delete a data repository association from. 

1. Choose the **Data repository** tab.

1. In the **Data repository associations** pane, choose the data repository association that you want to delete.

1. For **Actions**, choose **Delete association**.

1. In the **Delete** dialog, you can choose **Delete data in file system** to physically delete the data in the file system that corresponds to the data repository association.

   Choose this option if you plan to create a new data repository association using the same file system path but pointing to a different S3 bucket prefix, or if you no longer need the data in your file system.

1. Choose **Delete** to remove the data repository association from the file system.

## To delete a link from a file system to an S3 bucket (AWS CLI)
<a name="delete-dra-cli-dra"></a>

The following example deletes a data repository association that links an Amazon FSx file system to an S3 bucket. The `--association-id` parameter specifies the ID of the data repository association to be deleted.
+ To delete a data repository association, use the Amazon FSx CLI command `delete-data-repository-association`, as shown following.

  ```
  $ aws fsx delete-data-repository-association \
        --association-id dra-872abab4b4503bfc \
        --delete-data-in-file-system false
  ```

After successfully deleting the data repository association, Amazon FSx returns its description as JSON.

**Recreating DRAs with the same file system path**  
We do not recommend deleting and recreating data repository associations that use the same file system path. If you delete a DRA and later create a new DRA using the same file system path, some files may retain HSM state from the previously deleted DRA.  
If you need to export files from a recreated DRA that were managed by a previously deleted DRA, you need to mark those files as dirty using the command below and then run an export data repository task:  

```
sudo lfs hsm_set --dirty {{file_path}}
```