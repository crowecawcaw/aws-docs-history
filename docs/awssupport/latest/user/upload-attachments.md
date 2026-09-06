

# Uploading attachments
<a name="upload-attachments"></a>

You can attach files when creating a support case or when replying to an existing case. You can attach up to 10 files, with each file up to 150 MB.

------
#### [ Support Center Console ]

**To upload attachments using the console**

1. On the **Create case** page or in the reply section of a case, choose **Choose file**.

1. Select up to 10 files from your file picker. Each file can be up to 150 MB. Each file begins uploading immediately and the **Status** column displays a real-time progress bar during the upload.

1. When a file finishes uploading, the status changes to **Upload completed** and the **Action** column displays **Remove**.

1. After all files reach **Upload completed** status, complete the remaining case fields and then choose **Submit**.

After you submit the case, uploaded attachments appear as clickable links in the case correspondence on the **Case details** page.

------
#### [ AWS Support API ]

You can programmatically attach files to a support case or case communication using the AWS Support API. The API uses a multipart upload flow with presigned URLs.

**To upload an attachment using the API**

1. **Start the upload.** Call `GetAttachmentUploadLinks` with `fileName` and `fileSizeBytes`. The response returns an `uploadId`, `partSizeBytes`, `totalParts`, and a first batch of presigned upload URLs.

1. **Split and upload your file.** Divide your file into segments of `partSizeBytes` bytes by reading sequentially from the start of the file. The first segment corresponds to `partIndex` 1, the second to `partIndex` 2, and so on. The final segment may be smaller than `partSizeBytes`. PUT each segment to the presigned URL with the matching `partIndex`. Save the `ETag` that Amazon S3 returns for each successful PUT.

1. **Get more URLs if needed.** Each call returns up to 10 URLs. If your file has more than 10 parts, call `GetAttachmentUploadLinks` again with the same `uploadId`, passing `nextIndex` as `uploadRange.startIndex`. Repeat until `nextIndex` is null.

1. **Report completed parts.** Call `CompleteAttachmentUpload` with the `uploadId`, `partIndex`, and `ETag` for each part as soon as its PUT succeeds. Reporting parts immediately makes the upload resumable. If the upload is interrupted, only unreported parts need to be re-uploaded.

1. **Wait for the upload to be ready.** Poll `DescribeAttachmentUploadStatus` until `uploadStatus` is `attachment-ready`. Processing is asynchronous and may take a few minutes for larger files.

1. **Attach to a case.** Pass the `uploadId` in the `uploadIds` parameter of `CreateCase` or `AddCommunicationToCase`.

**uploadId vs. attachmentId**  
An `uploadId` identifies an in-progress upload session and is used with the upload operations (`GetAttachmentUploadLinks`, `CompleteAttachmentUpload`, `DescribeAttachmentUploadStatus`) and as input to `CreateCase` or `AddCommunicationToCase`.  
An `attachmentId` is generated after the upload is committed to a case communication. Use `GetAttachmentDownloadLink` with an `attachmentId` to download attachments. You can obtain the `attachmentId` from the `attachments` field of a `Communication` returned by `DescribeCommunications`.

**Note**  
`DescribeAttachment` only supports attachments that are 5 MB or smaller. Calling `DescribeAttachment` for a larger attachment returns `InvalidParameterValueException`. To download attachments larger than 5 MB, use `GetAttachmentDownloadLink`.

**Endpoints**

Presigned URLs returned by these operations are served from the following domains:
+ **Upload URLs** (`GetAttachmentUploadLinks`): `v1.uploads.attachments.support.us-east-1.amazonaws.com`
+ **Download URLs** (`GetAttachmentDownloadLink`): `v1.downloads.attachments.support.us-east-1.amazonaws.com`

If your environment restricts outbound traffic, ensure both domains are reachable.

**Constraints**
+ Maximum file size per upload: 150 MB.
+ Maximum upload URLs returned per call to `GetAttachmentUploadLinks`: 10.
+ Maximum number of `uploadIds` per `CreateCase` or `AddCommunicationToCase` request: 10.

------