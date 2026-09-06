

# Add or remove tags on existing recovery points
<a name="tagging-recovery-points"></a>

In addition to copying tags from source resources at backup creation time, you can add, modify, or remove tags on existing recovery points.

**Important**  
You can only manage tags via the AWS Backup console and API for recovery points of resources that are [fully managed by AWS Backup](whatisbackup.md#full-management). For non-fully managed resources (such as Amazon EC2, Amazon EBS, Amazon RDS, and Aurora), the **Manage tags** option is not available in the console. To manage tags on these recovery points, use the underlying service's tagging capabilities instead.

## Required permissions
<a name="tagging-recovery-points-permissions"></a>

The IAM role or user performing the tagging operation must have the following permissions:
+ `backup:TagResource` – Required to add or modify tags on a recovery point.
+ `backup:UntagResource` – Required to remove tags from a recovery point.
+ `backup:ListTags` – Required to view existing tags on a recovery point.

## Add or remove tags using the console
<a name="tagging-recovery-points-console"></a>

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup/](https://console.aws.amazon.com/backup/home).

1. In the navigation pane, choose **Backup vaults**.

1. Choose the backup vault that contains the recovery point you want to tag.

1. Under **Recovery points**, choose the **Recovery point ID** of the backup you want to tag.

1. In the **Tags** section, choose **Manage tags**.

1. To add a tag, choose **Add tag**, then enter a **Key** and an optional **Value**.

   To remove a tag, choose **Remove** next to the tag you want to delete.

1. Choose **Save**.

## Add or remove tags using the AWS CLI
<a name="tagging-recovery-points-cli"></a>

**Add tags to a recovery point:**

```
aws backup tag-resource \
    --resource-arn {{arn:aws:backup:us-east-1:123456789012:recovery-point:abcdef12-3456-7890-abcd-ef1234567890}} \
    --tags Key1=Value1,Key2=Value2
```

**Remove tags from a recovery point:**

```
aws backup untag-resource \
    --resource-arn {{arn:aws:backup:us-east-1:123456789012:recovery-point:abcdef12-3456-7890-abcd-ef1234567890}} \
    --tag-key-list Key1 Key2
```

**List tags on a recovery point:**

```
aws backup list-tags \
    --resource-arn {{arn:aws:backup:us-east-1:123456789012:recovery-point:abcdef12-3456-7890-abcd-ef1234567890}}
```

For more information, see [TagResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_TagResource.html), [UntagResource](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_UntagResource.html), and [ListTags](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListTags.html) in the *AWS Backup API Reference*.