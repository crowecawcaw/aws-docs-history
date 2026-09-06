

# Pause and resume your sync
<a name="manage-sync-pause-resume-sync-configurable-ADsync"></a>

Pausing your sync pauses all future sync cycles and prevents any changes that you make to users and groups in Active Directory from being reflected in IAM Identity Center. After you resume the sync, the sync cycle picks up these changes from the next scheduled sync.

**To pause your sync**

1. Open the [IAM Identity Center console.](https://console.aws.amazon.com/singlesignon)

1. Choose **Settings**.

1. On the **Settings** page, choose the **Identity source** tab, choose **Actions**, and then choose **Manage Sync**.

1. Under **Manage Sync**, choose **Pause sync**.

**To resume your sync**

1. Open the [IAM Identity Center console.](https://console.aws.amazon.com/singlesignon)

1. Choose **Settings**.

1. On the **Settings** page, choose the **Identity source** tab, choose **Actions**, and then choose **Manage Sync**.

1. Under **Manage Sync**, choose **Resume sync**.
**Note**  
If you see **Pause sync** instead of **Resume sync**, the sync from Active Directory to IAM Identity Center has already resumed.