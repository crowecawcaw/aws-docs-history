

# Working with Attachments
<a name="working-with-acps-api"></a>

This topic explains how to work with attachments for Chat and Cases in Connect Customer. For Chat Attachments, refer to the first section on the Connect Customer Participant Service API. For Case Attachments, refer to the second section on the Connect Customer service’s Attached Files APIs.

## Uploading Attachments with the Participant Service
<a name="uploading-attachments"></a>

There are three basic steps for uploading a file using the Connect Customer Participant Service API. 

1. HTTP POST file metadata to `StartAttachmentUpload` API, which will provide a signed Amazon S3 URL and attachment ID for uploading the file directly to Amazon S3.

1. HTTP PUT file data to the signed Amazon S3 URL.

1. HTTP POST attachment ID to `CompleteAttachmentUpload` to finalize the upload to Amazon S3.

Below is a basic JavaScript implementation for reference purposes.

```
//Define the html element for file using input tag

<input type="file" id="fileUpload">
<input type="button" id="btnUploadFile" onclick="uploadFile()" value="Upload file">


async function uploadFile() {
    //Initiate the file upload by calling StartAttachmentUpload, providing the name, size, and content type of the file you want to upload.
    //The response will include a pre-signed URL and headers to use when building the file upload request, as well as an AttachmentId.
    const files = document.getElementById('fileUpload').files;
    const file = files[0];

    const startUploadRequest = {
        AttachmentName: file.name,
        AttachmentSizeInBytes: file.size,
        ContentType: file.type
    };
    const { AttachmentId, UploadMetadata } = await startAttachmentUpload(startUploadRequest);

    //Send the file data to the pre-signed S3 URL.
    //The file is stored in a temporary location in the S3 bucket.

    await uploadFileToS3(file, UploadMetadata.Url, UploadMetadata.HeadersToInclude);

    //Finalize the file upload by calling CompleteAttachmentUpload, providing the AttachmentId.
    //This moves the file to the final Attachments S3 path configured for the connect instance.
    const completeUploadRequest = {
        AttachmentIds: [ AttachmentId ]
    };
    await completeAttachmentUpload(completeUploadRequest);
}

async function startAttachmentUpload(requestData){
    const response = await fetch(StartAttachmentUploadEndpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Amz-Bearer': ConnectionToken,
        },
        body: JSON.stringify(requestData)
    });

    return await response.json();
}

async function uploadFileToS3(file, signedUrl, headersToInclude) {
    return fetch(signedUrl, {
      method: 'PUT',
      headers: headersToInclude,
      body: file
    });
}

async function completeAttachmentUpload(requestData){
    return fetch(CompleteAttachmentUploadEndpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Amz-Bearer': ConnectionToken,
        },
        body: JSON.stringify(requestData)
    });
}
```

For an example of a real world implementation, view the [Connect Customer ChatJS JavaScript client](https://github.com/amazon-connect/amazon-connect-chatjs/blob/master/src/client/client.js#L164-L219) on GitHub.

## Uploading Attached Files with the Connect Service
<a name="uploading-attachments-connect-service"></a>

The same basic steps follow from the Participant service instructions, for usage with the Connect Customer service’s attached file APIs.

1. Call the `StartAttachedFileUpload` API with the required attached file information, which will provide a signed Amazon S3 URL, headers, and file ID for uploading the file directly to Amazon S3.

   1. If you are attaching a file to a Case, the calling identity must also have the `cases:CreateRelatedItem` permission on the target Case resource.

1. Using your http client of choice, PUT file data to the signed Amazon S3 URL, ensuring that you add the headers as required from the response of Step 1.

1. Call the `CompleteAttachedFileUpload` to finalize the upload to Amazon S3.