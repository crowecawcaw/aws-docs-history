# Supported Amazon S3 object-level API operations for S3 Tables

 The following table includes supported S3 object-level API operations and corresponding
 headers for S3 Tables. For a list of Amazon S3 Tables APIs, see [Amazon S3 Tables](API_Operations_Amazon_S3_Tables.md "API_Operations_Amazon_S3_Tables.md").
 For more information about Amazon S3 Tables, see [Working with Amazon S3 Tables and table
 buckets](../userguide/s3-tables.md "../userguide/s3-tables.md") in the *Amazon S3 User Guide*.



| Object-level API | Supported headers | Notes  |
| --- | --- | --- |
| [`AbortMultipartUpload`](API_AbortMultipartUpload.md "API_AbortMultipartUpload.md") | `x-amz-expected-bucket-owner` | None |
| [`CompleteMultipartUpload`](API_CompleteMultipartUpload.md "API_CompleteMultipartUpload.md") | `x-amz-checksum-crc32` | None |
| `x-amz-checksum-crc32c` | None |
| `x-amz-checksum-sha1` | None |
| `x-amz-checksum-sha256` | None |
| `x-amz-expected-bucket-owner` | None |
| `If-Match` | None |
| `If-None-Match` | None |
| [`CreateMultipartUpload`](API_CreateMultipartUpload.md "API_CreateMultipartUpload.md") | `x-amz-acl: ACL` | For S3 Tables, the default value is
 `bucket-owner-full-control` and it can’t be changed. |
| `Cache-Control` | None |
| `Content-Disposition` | None |
| `Content-Encoding` | None |
| `Content-Language` | None |
| `Content-Type` | None |
| `Expires` | None |
| `x-amz-checksum-algorithm` | None |
| `x-amz-storage-class` | For S3 Tables, the default value is `STANDARD` and it can’t be
 changed.  |
| `x-amz-server-side-encryption` | For S3 Tables, the default value is (`SSE-S3`)
 (`AES256`) and it can't be changed.  |
| [`GetObject`](API_GetObject.md "API_GetObject.md") | `If-Match` | None |
| `If-Modified-Since` | None |
| `If-None-Match` | None |
| `If-Unmodified-Since` | None |
| `Range` | None |
| `x-amz-expected-bucket-owner` | None |
| `x-amz-checksum-mode` | None |
| [`HeadObject`](API_HeadObject.md "API_HeadObject.md") | `If-Match` | None |
| `If-Modified-Since` | None |
| `If-None-Match` | None |
| `If-Unmodified-Since` | None |
| `Range` | None |
| `x-amz-checksum-mode` | None |
| `x-amz-expected-bucket-owner` | None |
| [`ListParts`](API_ListParts.md "API_ListParts.md") | `x-amz-expected-bucket-owner` | None |
| [`PutObject`](API_PutObject.md "API_PutObject.md") | `x-amz-acl: ACL` | For S3 Tables, the default value is
 `bucket-owner-full-control` and it can’t be changed. |
| `Cache-Control` | None |
| `Content-Disposition` | None |
| `Content-Encoding` | None |
| `Content-Language` | None |
| `Content-Length` | None |
| `Content-MD5` | None |
| `Content-Type` | None |
| `x-amz-sdk-checksum-algorithm` | None |
| `x-amz-checksum-crc32` | None |
| `x-amz-checksum-crc32c` | None |
| `x-amz-checksum-sha1` | None |
| `x-amz-checksum-sha256` | None |
| `Expires` | None |
| `If-None-Match` | None |
| `x-amz-expected-bucket-owner` | None |
| `x-amz-storage-class` | For S3 Tables, the default value is `STANDARD` and it can’t be
 changed.  |
| `x-amz-server-side-encryption` | For S3 Tables, the default value is (`SSE-S3`)
 (`AES256`) and it can't be changed. |
| [`UploadPart`](API_UploadPart.md "API_UploadPart.md") | `Content-Length` | None |
| `Content-MD5` | None |
| `x-amz-checksum-crc32` | None |
| `x-amz-checksum-crc32c` | None |
| `x-amz-checksum-sha1` | None |
| `x-amz-checksum-sha256` | None |
| `x-amz-expected-bucket-owner` | None |
