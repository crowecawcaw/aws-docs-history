# Confirm that an

attached file has been uploaded in Amazon Connect Agent Workspace

Allows you to confirm that the attachment has been uploaded using the pre-signed
URL provided in the startAttachedFileUpload API. The request accepts an Attachment
object, which has the following properties:

- `associatedResourceArn: string`: Amazon Connect ARN of the
  resource that the file is attached to. Could be a Connect Email Contact ARN
  or a Connect Case ARN
- `fileId: string`: ID in Connect's File record

**Signature**

```
completeAttachedFileUpload(attachment: Attachment): Promise<void>
```

**Usage**

```

/* Logic with startAttachedFileUplaod and uploading attachment to pre-signed URL */

/* ... */

await fileClient.completeAttachedFileUpload({
  associatedResourceArn: sampleAssociatedResourceArn, // Get this from the response from `startAttachedFileUpload`
  fileId: sampleFileId // Get this from the response from `startAttachedFileUpload`
});
```
