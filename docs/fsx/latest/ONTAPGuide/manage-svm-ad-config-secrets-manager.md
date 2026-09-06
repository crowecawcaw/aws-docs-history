

# Managing SVM Microsoft Active Directory configurations
<a name="manage-svm-ad-config-secrets-manager"></a>

You can join an SVM to Microsoft Active Directory or modify the Microsoft Active Directory configuration of an SVM that's already joined to Microsoft Active Directory. FSx for ONTAP integrates with AWS Secrets Manager to securely manage your domain join service account credentials.<a name="update-svm-ad-config-console"></a>

**To update SVM Microsoft Active Directory configuration (console)**

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. Choose the SVM to update as follows:
   + In the left navigation pane, choose **File systems**, and then choose the ONTAP file system for which you want to update an SVM.
   + Choose the **Storage virtual machines** tab.

     –Or–
   + To display a list of all the SVMs available in your AWS account in the current AWS Region, expand **ONTAP** and choose **Storage virtual machines**.

1. Choose the storage virtual machine that you want to update.

1. Choose **Actions > Update Microsoft Active Directory configuration**. The **Update Microsoft Active Directory configuration** window appears.

1. For **Domain join service account credentials**, choose **Managed in Secrets Manager** (recommended) to use Secrets Manager for secure credential management.
**Note**  
Using Secrets Manager eliminates the need to store plaintext credentials and provides centralized credential management. For more information, see [Storing Active Directory credentials using AWS Secrets Manager](self-managed-AD-best-practices.md#bp-store-ad-creds-using-secret-manager).

1. For **Secret**, choose an existing secret from Secrets Manager that contains your updated domain join service account credentials, or choose **Create new secret** to create one.

1. Update other Microsoft Active Directory configuration fields as needed for your environment.

1. Choose **Update configuration** to save the changes.

**To update SVM Microsoft Active Directory configuration (CLI)**
+ To update the Microsoft Active Directory configuration of an FSx for ONTAP SVM, use the [update-storage-virtual-machine](https://docs.aws.amazon.com/cli/latest/reference/fsx/update-storage-virtual-machine.html) CLI command with the `--active-directory-configuration` parameter, as shown in the following example.

  ```
  aws fsx update-storage-virtual-machine \
  --storage-virtual-machine-id svm-abcdef01234567890 \
  --active-directory-configuration DomainJoinServiceAccountSecret={{secret-arn}}
  ```