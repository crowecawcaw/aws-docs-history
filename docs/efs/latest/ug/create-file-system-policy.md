

# Creating file system policies
<a name="create-file-system-policy"></a>

You can create a file system policy by using the Amazon EFS console or by using the AWS CLI. You can also create a file system policy programmatically by using AWS SDKs or the Amazon EFS API directly. EFS file system policies have a 20,000 character limit. For more information about using an EFS file system policy and examples, see [Using IAM to control access to file systems](iam-access-control-nfs-efs.md).

**Note**  
Amazon EFS file system policy changes can take several minutes to take effect.

## Using the console
<a name="create-file-system-policy-console"></a>

1. Open the Amazon Elastic File System console at [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/).

1. Choose **File Systems**.

1. On the **File systems** page, choose the file system that you want to edit or create a file system policy for. 

1. Choose **File system policy**, then choose **Edit**. 

1. In **Policy options**, you can choose any combination of the preconfigured file system policies:
   + **Prevent root access by default** – This option removes `ClientRootAccess` from the set of allowed EFS actions.
   + **Enforce read-only access by default** – This option removes `ClientWriteAccess` from the set of allowed EFS actions.
   + **Prevent anonymous access** – This option removes `ClientMount` from the set of allowed EFS actions.
   + **Enforce in-transit encryption for all clients** – This option denies access to unencrypted clients.

   When you choose a preconfigured policy, the policy JSON object is displayed in the **Policy editor** pane.

1. Use **Grant additional permissions** to grant file system permissions to additional IAM principals, including another AWS account. Choose **Add**, and enter the principal ARN of the entity that you are granting permissions to. Then choose the **Permissions** that you want to grant. The additional permissions are shown in the **Policy editor**.

1. You can use the **Policy editor** to customize a preconfigured policy or to create your own file system policy. When you use the editor, the preconfigured policy options become unavailable. To clear the current file system policy and start creating a new policy, choose **Clear**.

   When you clear the editor, the preconfigured policies become available once again.

1. After you complete editing the policy, choose **Save**.

## Using the AWS CLI
<a name="create-file-system-policy-cli"></a>

In the following example, the [put-file-system-policy](https://docs.aws.amazon.com/cli/latest/reference/efs/put-file-system-policy.html) CLI command creates a file system policy that allows the specified AWS account read-only access to the EFS file system. The equivalent API command is [PutFileSystemPolicy](https://docs.aws.amazon.com/efs/latest/APIReference/API_PutFileSystemPolicy.html).

```
aws efs put-file-system-policy --file-system-id fs-01234567 --policy '{
    "Id": "1",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "elasticfilesystem:ClientMount"
            ],
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:root"
            }
        }                                                                                                 
    ]
}'
```