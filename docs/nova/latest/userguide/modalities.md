# Multimodal support for Amazon Nova

Amazon Nova Understanding Models are multimodal understanding models, that means they
support multimodal inputs such as images, videos, and documents to infer and answer question
based on the content provided. The Amazon Nova models are equipped with novel vision
capabilities that enable the model to comprehend and analyze images, documents, and videos
thereby realizing multimodal understanding use cases.

The following section outline guidelines for working with images, documents, and videos in
Amazon Nova. These include preprocessing strategies employed, code examples, and relevant
limitations to consider.

###### Topics

- [Supported content type by modality](#modalities-content "#modalities-content")
- [Image understanding](modalities-image.md "modalities-image.md")
- [Video understanding](modalities-video.md "modalities-video.md")
- [Document understanding](modalities-document.md "modalities-document.md")
- [Error handling](text-error-handing.md "text-error-handing.md")

## Supported content type by modality

The following information details the file formats supported by media file and the
accepted input method.

| Media File Type                      | File Formats supported                        | **Input Method**     | Parsing Strategy                              |
| ------------------------------------ | --------------------------------------------- | -------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Image                                | PNG, JPG, JPEG, GIF, WebP                     | Base64 Amazon S3 URI | Image Vision Understanding                    |
| Text Document _(Converse API Only)_  | CSV, XLS, XLSX, HTML, TXT, MD, DOC            | Bytes Amazon S3 URI  | Textual Understanding from the document only. |
| Media Document _(Converse API Only)_ | PDF, DOCX                                     | Bytes Amazon S3 URI  | Text with interleaved Image Understanding     |
| Video                                | MP4, MOV, MKV, WebM, FLV, MPEG, MPG, WMV, 3GP | Base64 Amazon S3 URI | Video Vision Understanding                    | ###### Note You can include up to five files from your computer or 1000 files from Amazon S3. Each file must be no more than 1 GB when uploaded from Amazon S3. The total size of the uploaded files cannot exceed 25 MB when uploading from your computer or 2 GB when uploading from Amazon S3. Because 25 MB is the overall payload limit, ensure that you account for the base64 overhead. While working, remember that libraries and frameworks maintain memory, and passed media content can quickly add up. When using video, specifying an `s3Location` should alleviate many storage issues. ###### Note Large videos and documents take time to process, regardless of input method. If boto3 SDK times-out while waiting for a response from Amazon Bedrock, ensure that you have an appropriate [read_timeout](https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html "https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html") value set and have upgraded boto3 to at least version 1.38. |
