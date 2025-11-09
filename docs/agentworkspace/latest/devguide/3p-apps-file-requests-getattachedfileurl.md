# Get a pre-signed S3 URL

to download an approved attached file in Amazon Connect Agent Workspace

Returns a pre-signed URL to download an approved attached file while handling an
active contact. The activeContactId is the id of the contact the agent is actively
viewing. This API also returns metadata about the attached file and it will only
return a downloadUrl if the status of the attached file is APPROVED.

**Signature**

```
getAttachedFileUrl({ attachment, activeContactId }: { attachment: Attachment; activeContactId: string; }): Promise<DownloadableAttachment>
```

**DownloadableAttachment Properties**

| **Parameter**         | **Type**   | **Description**                                                                                                                                                          |
| --------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| associatedResourceArn | string     | Amazon Connect ARN of the resource that the file is attached to.<br>Could be a Connect Email Contact ARN or a Connect Case ARN                                           |
| fileId                | string     | The unique identifier of the attached file resource.                                                                                                                     |
| downloadUrl           | string     | A pre-signed URL that should be used to download the attached<br>file.                                                                                                   |
| fileArn               | string     | The unique identifier of the attached file resource<br>(ARN).                                                                                                            |
| fileName              | string     | A case-sensitive name of the attached file being<br>uploaded.                                                                                                            |
| fileStatus            | FileStatus | The current status of the attached file. Supported values:<br>"APPROVED", "REJECTED", "PROCESSING", "FAILED"                                                             |
| fileSizeInBytes       | number     | The size of the attached file in bytes.                                                                                                                                  |
| creationTime          | string     | The time of Creation of the file resource as an ISO timestamp.<br>It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For<br>example, 2024-05-03T02:41:28.172Z. |

**Attachment Properties**

| **Parameter**         | **Type** | **Description**                                                                                                                |
| --------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| associatedResourceArn | string   | Amazon Connect ARN of the resource that the file is attached to.<br>Could be a Connect Email Contact ARN or a Connect Case ARN |
| fileId                | string   | The unique identifier of the attached file resource.                                                                           |

**Usage**

```

const downloadableAttachment = await fileClient.getAttachedFileUrl({
  attachment: {
    associatedResourceArn: sampleAssociatedResourceArn,
    fileId: sampleFileId,
  },
  activeContactId: sampleActiveContactId, // The contact the agent is actively handling
});

const { downloadUrl } = downloadableAttachment;
const response: Response = await fetch(downloadUrl, { method: "GET" });
```
