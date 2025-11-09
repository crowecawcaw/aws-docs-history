# Amazon S3 multipart upload limits

Multipart upload allows you to upload a single object as a set of parts. Each part is a
contiguous portion of the object's data. After all parts of your object are uploaded, Amazon S3
assembles these parts and creates the object. In general, when your object size reaches 100
MB, you should consider using multipart uploads instead of uploading the object in a single
operation. For more information about multipart uploads, see [Uploading and copying objects using multipart upload in Amazon S3](mpuoverview.md "mpuoverview.md").

The following table provides multipart upload core specifications. These include maximum
object size, maximum number of parts, maximum part size, and more. There is no minimum size
limit on the last part of your multipart upload.

| Item                                                                                | Specification                                                                                |
| ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Maximum object size                                                                 | 5 TiB                                                                                        |
| Maximum number of parts per upload                                                  | 10,000                                                                                       |
| Part numbers                                                                        | 1 to 10,000 (inclusive)                                                                      |
| Part size                                                                           | 5 MiB to 5 GiB. There is no minimum size limit on the last part of your multipart<br>upload. |
| Maximum number of parts returned for a list parts request                           | 1000                                                                                         |
| Maximum number of multipart uploads returned in a list multipart uploads<br>request | 1000                                                                                         |
