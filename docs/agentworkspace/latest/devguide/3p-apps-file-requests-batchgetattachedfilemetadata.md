# Get metadata

about multiple attached files in Amazon Connect Agent Workspace

Get metadata about multiple attached files on an associated resource while
handling an active contact. The activeContactId is the id of the contact the agent
is actively viewing. Each attached file provided in the input list must be
associated with the associatedResourceArn in the RelatedAttachments request
object.

**Signature**

```
batchGetAttachedFileMetadata({ relatedAttachments, activeContactId }: { relatedAttachments: RelatedAttachments; activeContactId: string; }): Promise<BatchGetAttachedFileMetadataResponse>
```

**BatchGetAttachedFileMetadataResponse Properties**

| **Parameter** | **Type**             | **Description**                                                    |
| ------------- | -------------------- | ------------------------------------------------------------------ |
| files         | AttachmentMetadata[] | Array of file metadata objects that were successfully<br>retrieved |
| errors        | AttachmentError[]    | Array of errors of attached files that could not be<br>retrieved   |

**AttachmentMetadata Properties**

| **Parameter**         | **Type**   | **Description**                                                                                                                                                          |
| --------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| associatedResourceArn | string     | Amazon Connect ARN of the resource that the file is attached to.<br>Could be a Connect Email Contact ARN or a Connect Case ARN                                           |
| fileId                | string     | The unique identifier of the attached file resource                                                                                                                      |
| fileArn               | string     | The unique identifier of the attached file resource<br>(ARN).                                                                                                            |
| fileName              | string     | A case-sensitive name of the attached file being<br>uploaded.                                                                                                            |
| fileStatus            | FileStatus | The current status of the attached file. Supported values:<br>"APPROVED", "REJECTED", "PROCESSING", "FAILED"                                                             |
| fileSizeInBytes       | number     | The size of the attached file in bytes.                                                                                                                                  |
| creationTime          | string     | The time of Creation of the file resource as an ISO timestamp.<br>It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For<br>example, 2024-05-03T02:41:28.172Z. |

**AttachmentError Properties**

| **Parameter** | **Type** | **Description**                                     |
| ------------- | -------- | --------------------------------------------------- |
| errorCode     | string   | Status code describing the failure                  |
| errorMessage  | string   | Why the attached file couldn't be retrieved         |
| fileId        | string   | The unique identifier of the attached file resource |

**RelatedAttachments Properties**

| **Parameter**         | **Type** | **Description**                                                                                                                |
| --------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| associatedResourceArn | string   | Amazon Connect ARN of the resource that the file is attached to.<br>Could be a Connect Email Contact ARN or a Connect Case ARN |
| fileIds               | string[] | The unique identifiers of the attached file resources                                                                          |

**Usage**

```

const relatedAttachments: RelatedAttachments = {
  fileIds: [sampleFileId1, sampleFileId2],
  associatedResourceArn: sampleAssociatedResourceArn,
};

const response: BatchGetAttachedFileMetadataResponse = await fileClient.batchGetAttachedFileMetadata({
  relatedAttachments,
  activeContactId: sampleActiveContactId, // The contact the agent is actively handling
});

const { files, errors } = response;

// Add logic to handle response
```
