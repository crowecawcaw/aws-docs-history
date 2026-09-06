

# Creating file system policies
<a name="s3-files-file-system-policies-creating"></a>

You can use file system policies to grant or deny permissions for NFS clients to perform operations such as mounting, writing, and root access on your file systems. A file system either has an empty (default) file system policy or exactly one explicit policy. You can update your file system policy at any time after file system creation using the AWS Management Console, AWS CLI, or AWS SDK.

You can update a file system policy by using the Amazon S3 console, the AWS CLI, programmatically with AWS SDKs, or the S3 Files API directly. These policy changes can take several minutes to take effect. S3 file system policies have a 20,000 character limit. For more information about using an S3 file system policy, supported actions, supported condition keys, and examples, see [How S3 Files works with IAM](s3-files-security-iam.md).

## Using the S3 console
<a name="s3-files-file-system-policies-creating-console"></a>

This section explains how to use the Amazon S3 console to create a file system policy for S3 Files.

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation bar, verify you are in the AWS Region where your file system exists.

1. In the left navigation pane, choose **File systems**.

1. Choose your desired file system.

1. Select the **Permissions** tab and select **Edit**.

1. You can use the Policy editor to add your own file system policy.

1. After you complete editing the policy, choose **Save**.

## Using the AWS CLI
<a name="s3-files-file-system-policies-creating-cli"></a>

The following `put-file-system-policy` example command shows how you can use the AWS CLI to create a file system policy for S3 Files. The following file system policy grants only `ClientMount` (read-only) permissions to the `ReadOnly` IAM role. Replace the example AWS account ID {{111122223333}} with your AWS account ID.

```
aws s3files put-file-system-policy --file-system-id {{file-system-id}} --policy '{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:role/ReadOnly"
            },
            "Action": [
                "s3files:ClientMount"
            ]
        }
    ]
}'
```