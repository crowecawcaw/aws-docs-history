

# Deleting file system policies
<a name="s3-files-file-system-policies-deleting"></a>

You can delete a file system policy using the Amazon S3 console and the AWS CLI.

## Using the S3 console
<a name="s3-files-file-system-policies-deleting-console"></a>

This section explains how to use the Amazon S3 console to delete a file system policy for S3 Files.

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation bar, verify you are in the AWS Region where your file system exists.

1. In the left navigation pane, choose **File systems**.

1. Choose your file system.

1. Select the **Permissions** tab and select **Delete**.

1. In the confirmation window, type **confirm** and choose **Delete**.

## Using the AWS CLI
<a name="s3-files-file-system-policies-deleting-cli"></a>

The following `delete-file-system-policy` example command shows how you can use the AWS CLI to delete a file system policy for S3 Files.

```
aws s3files delete-file-system-policy --file-system-id {{file-system-id}}
```