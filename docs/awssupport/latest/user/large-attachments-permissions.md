

# Required permissions for large attachments
<a name="large-attachments-permissions"></a>

To attach files larger than 5 MB or more than 3 files to a support case, your AWS Identity and Access Management (IAM) identity must have the correct permissions.

The following table shows the required IAM actions for each attachment operation.


| Operation | Required IAM actions | Grants access to | 
| --- | --- | --- | 
| Upload attachments | `support:UploadAttachment`<br />`support:AddAttachmentsToSet` | `GetAttachmentUploadLinks`<br />`CompleteAttachmentUpload`<br />`DescribeAttachmentUploadStatus` | 
| Download attachments | `support:DownloadAttachment`<br />`support:DescribeAttachment` | `GetAttachmentDownloadLink` | 

**Important**  
All listed permissions are required for each operation. For example, to upload attachments, you must have both `support:UploadAttachment` and `support:AddAttachmentsToSet`.

The following example policy grants full upload and download permissions for large attachments:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "support:UploadAttachment",
        "support:AddAttachmentsToSet",
        "support:DownloadAttachment",
        "support:DescribeAttachment"
      ],
      "Resource": "*"
    }
  ]
}
```

**Note**  
If you have the `AWSSupportAccess` managed policy attached to your IAM identity, no additional permissions are required. The managed policy includes all actions needed for large attachments.  
If you don't have the required permissions, then the Support Center Console supports attaching up to 3 files at 5 MB each. An **Update your permissions** notice appears with details about the missing permissions.