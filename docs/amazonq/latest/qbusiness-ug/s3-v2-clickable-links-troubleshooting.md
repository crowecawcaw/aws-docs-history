# Troubleshooting

clickable links

This section helps you resolve errors that you might encounter when using
clickable links for source references in your conversations with your Amazon Q Business AI assistant.

## Full sync required

###### Note

The following suggested troubleshooting steps apply only to existing
accounts using the Amazon S3 connector.

**Issue**: When you try to access referenced URLs
from an Amazon S3 or uploaded files data source, you receive the
following error message.

**Error message**:

```
This document cannot be downloaded because the raw document download feature requires a full connector sync performed after 07/02/2025. Your admin has not yet completed this full sync. Please contact your admin to request a complete sync of the data source.
```

**Solution**: This error occurs when the data
source hasn't completed a full sync after the clickable links feature was
enabled. To resolve this issue:

- For S3 data sources: Perform a full sync of the S3 data source.
- For uploaded files data sources: Delete the files from the upload
  files data source and upload them again.

## Permission changes

**Issue**: When browsing conversation history,
you click on a reference URL from an Amazon S3 data source but can't
view or download the file.

**Error message**:

```
You no longer have permission to access this document. The access permissions for this document have been changed since you last accessed it. Please contact your admin if you believe you should have access to this content.
```

**Solution**: This error occurs when the
permissions for the document in the ACLs on the Amazon S3 bucket changed
after your conversation, removing your access to the file. The ACLs were updated
in the Amazon Q Business index during a subsequent data source sync. If
you believe you should have access to the document, contact your administrator
to:

- Review and update the ACLs
- Perform a data source sync

## Document not found

**Issue**: When browsing conversation history,
you click on a reference URL from an Amazon S3 or upload files data
source but can't view or download the file.

**Error message**:

```
The document you're trying to access no longer exists in the data source. It may have been deleted or moved since it was last referenced. Please check with the admin if you need access to this document.
```

**Solution**: This error occurs when the document
was deleted from the Amazon S3 bucket, moved to a different location, or
deleted from the upload files data source after your conversation. The document
was also removed from the Amazon Q Business index and staging bucket
during a subsequent data source sync. If you believe the document shouldn't have
been deleted, contact your administrator to restore the document and perform a
data source sync.

## Insufficient

permissions

###### Note

The following suggested troubleshooting steps apply only to existing
accounts using the Amazon S3 connector.

**Issue**: When you click on a reference URL from
an Amazon S3 or upload files data source, you can't view or download the
file.

**Error message**:

```
Unable to download this document because your Web Experience lacks the required permissions. Your admin needs to update the IAM role for the Web Experience to include permissions for the GetDocumentContent API. Please contact your admin to request this IAM role update.
```

**Solution**: This error occurs when the web
experience doesn't have the required permissions to invoke the
GetDocumentContent API. Your administrator can resolve this error by updating
the IAM role for the web experience with the permissions described in the
_Considerations for using S3 clickable URLs_
section.

If you already use a Amazon Q Business web experience, add the following
permissions to the [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") for the Amazon Q Business web
experience:

```

{
    "Sid": "QBusinessGetDocumentContentPermission",
    "Effect": "Allow",
    "Action": ["qbusiness:GetDocumentContent"],
    "Resource": [
        "arn:aws:qbusiness:{{region}}:{{source_account}}:application/{{application_id}}",
        "arn:aws:qbusiness:{{region}}:{{source_account}}:application/{{application_id}}/index/*"
    ]
}

```
