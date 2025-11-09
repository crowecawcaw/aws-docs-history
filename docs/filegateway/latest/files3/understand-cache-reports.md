# Understanding the information provided in

S3 File Gateway cache reports

Cache reports list files that are currently in the local cache for a specific file
share, according to filters and criteria that you specify. Each cache report includes
the following information:

- **Bucket** — The Amazon S3 bucket or Access Point that is
  associated with the file share.
- **S3ObjectKey** — The Amazon S3 object that stores the data
  and metadata for this file. This object has the latest data that has been
  uploaded to S3, but it could be missing data which is failing to upload to
  S3.
- **FilePath** — The file path for the file entry in the
  gateway cache. This is where you can find the file when mounting and browsing
  the file share.
- **RenamedTo** — The new path of a renamed file. When
  you rename a file on your file share, the gateway needs to track both the old
  and new locations of the file. This field shows where the file was moved to,
  helping you track file rename operations - even if a file has been renamed
  multiple times. This information is particularly useful when you need to
  understand how files in your file share correspond to objects in your Amazon S3
  bucket.

The following example shows the cache report entries for a complex scenario
involving a file being overwritten directly in Amazon S3, while also being renamed
through File Gateway. In this scenario, the gateway uploads file
`A.txt` to S3, and then evicts the file contents to make space in
the local cache. The associated S3 object is then overwritten directly in
S3—not through an action taken by the gateway—which results in an
`InvalidObjectState` due to the mismatch between the S3 object
and what the gateway expects. At the same time, file `A.txt` was
renamed to `B.txt` through the gateway.

| Bucket           | S3ObjectKey | FilePath | RenamedTo | Type | IsDirty | IsDataDirty | IsDeleted | IsFailingToUpload | UploadError        | SizeInBytes | IsWholeFileInCache |
| ---------------- | ----------- | -------- | --------- | ---- | ------- | ----------- | --------- | ----------------- | ------------------ | ----------- | ------------------ |
| samplebucket-iad | A.txt       | /B.txt   |           | FILE | TRUE    | FALSE       | FALSE     | TRUE              | InvalidObjectState | 4           | FALSE              |
| samplebucket-iad | A.txt       | /A.txt   | /B.txt    | FILE | TRUE    | FALSE       | TRUE      | FALSE             |                    | 4           | FALSE              |

- **Type** — Denotes whether the entry is for a
  `FILE` or `DIRECTORY`.
- **IsDirty** — Reports `TRUE` if there is
  any type of change to the file which have not been uploaded to Amazon S3. This
  includes changes to metadata such as file name and read/write permissions, even
  if the file's data has not changed.
- **IsDataDirty** — Reports `TRUE` if there
  are changes to the file's data which have not been uploaded to Amazon S3.
- **IsDeleted** — Reports `TRUE` if the file
  was deleted on the gateway. If a file is marked as deleted, then it will always
  be marked as dirty.
- **IsFailingToUpload** — Reports `TRUE` if
  there is a problem uploading the file to Amazon S3. This status resets every 24 hours
  to allow the gateway to retry the upload and check whether the issue has been
  resolved. The gateway rejects any new write operations for a file that is
  failing to upload. If the gateway does not have the entire file in cache, then
  it also rejects read operations.
- **UploadError** — The error that is preventing the
  file from uploading to Amazon S3. For more information and recommended steps to
  resolve these errors, see [Troubleshooting: File Gateway issues](troubleshooting-file-gateway-issues.md "troubleshooting-file-gateway-issues.md").
- **SizeInBytes** — The total size of the file.
- **IsWholeFileInCache** — Reports `TRUE` if
  all of the file's data is currently stored in the gateway cache. If this is
  TRUE for a file failing to upload to Amazon S3, then the gateway will allow
  the file to be read.
