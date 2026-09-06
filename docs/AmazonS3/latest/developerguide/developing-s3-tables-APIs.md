

# Supported Amazon S3 object-level API operations for S3 Tables
<a name="developing-s3-tables-APIs"></a>

 The following table includes supported S3 object-level API operations and corresponding headers for S3 Tables. For a list of Amazon S3 Tables APIs, see [Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_S3_Tables.html). For more information about Amazon S3 Tables, see [Working with Amazon S3 Tables and table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables.html) in the *Amazon S3 User Guide*.



- **[`AbortMultipartUpload`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html) **
  - **Supported headers:** `x-amz-expected-bucket-owner`
  - **Notes:** None

- **[`CompleteMultipartUpload`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html) **
  - **Supported headers:** `x-amz-checksum-crc32` / **Notes:** None
  - **Supported headers:** `x-amz-checksum-crc32c` / **Notes:** None
  - **Supported headers:** `x-amz-checksum-sha1` / **Notes:** None
  - **Supported headers:** `x-amz-checksum-sha256` / **Notes:** None
  - **Supported headers:** `x-amz-expected-bucket-owner` / **Notes:** None
  - **Supported headers:** `If-Match` / **Notes:** None
  - **Supported headers:** `If-None-Match` / **Notes:** None

- **[`CreateMultipartUpload`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html)**
  - **Supported headers:** `x-amz-acl: ACL` / **Notes:** For S3 Tables, the default value is `bucket-owner-full-control` and it can’t be changed.
  - **Supported headers:** `Cache-Control` / **Notes:** None
  - **Supported headers:** `Content-Disposition` / **Notes:** None
  - **Supported headers:** `Content-Encoding` / **Notes:** None
  - **Supported headers:** `Content-Language` / **Notes:** None
  - **Supported headers:** `Content-Type` / **Notes:** None
  - **Supported headers:** `Expires` / **Notes:** None
  - **Supported headers:** `x-amz-checksum-algorithm` / **Notes:** None
  - **Supported headers:** `x-amz-storage-class` / **Notes:** For S3 Tables, the default value is `STANDARD` and it can’t be changed. 
  - **Supported headers:** `x-amz-server-side-encryption` / **Notes:** For S3 Tables, the default value is (`SSE-S3`) (`AES256`) and it can't be changed. 

- ** [`GetObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) **
  - **Supported headers:** `If-Match` / **Notes:** None
  - **Supported headers:** `If-Modified-Since` / **Notes:** None
  - **Supported headers:** `If-None-Match` / **Notes:** None
  - **Supported headers:** `If-Unmodified-Since` / **Notes:** None
  - **Supported headers:** `Range` / **Notes:** None
  - **Supported headers:** `x-amz-expected-bucket-owner` / **Notes:** None
  - **Supported headers:** `x-amz-checksum-mode` / **Notes:** None

- ** [`HeadObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html) **
  - **Supported headers:** `If-Match` / **Notes:** None
  - **Supported headers:** `If-Modified-Since` / **Notes:** None
  - **Supported headers:** `If-None-Match` / **Notes:** None
  - **Supported headers:** `If-Unmodified-Since` / **Notes:** None
  - **Supported headers:** `Range` / **Notes:** None
  - **Supported headers:** `x-amz-checksum-mode` / **Notes:** None
  - **Supported headers:** `x-amz-expected-bucket-owner` / **Notes:** None

- ** [`ListParts`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html) **
  - **Supported headers:** `x-amz-expected-bucket-owner`
  - **Notes:** None

- ** [`PutObject`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) **
  - **Supported headers:** `x-amz-acl: ACL` / **Notes:** For S3 Tables, the default value is `bucket-owner-full-control` and it can’t be changed.
  - **Supported headers:** `Cache-Control` / **Notes:** None
  - **Supported headers:** `Content-Disposition` / **Notes:** None
  - **Supported headers:** `Content-Encoding` / **Notes:** None
  - **Supported headers:** `Content-Language` / **Notes:** None
  - **Supported headers:** `Content-Length` / **Notes:** None
  - **Supported headers:** `Content-MD5` / **Notes:** None
  - **Supported headers:** `Content-Type` / **Notes:** None
  - **Supported headers:** `x-amz-sdk-checksum-algorithm` / **Notes:** None
  - **Supported headers:** `x-amz-checksum-crc32` / **Notes:** None
  - **Supported headers:** `x-amz-checksum-crc32c` / **Notes:** None
  - **Supported headers:** `x-amz-checksum-sha1` / **Notes:** None
  - **Supported headers:** `x-amz-checksum-sha256` / **Notes:** None
  - **Supported headers:** `Expires` / **Notes:** None
  - **Supported headers:** `If-None-Match` / **Notes:** None
  - **Supported headers:** `x-amz-expected-bucket-owner` / **Notes:** None
  - **Supported headers:** `x-amz-storage-class` / **Notes:** For S3 Tables, the default value is `STANDARD` and it can’t be changed. 
  - **Supported headers:** `x-amz-server-side-encryption` / **Notes:** For S3 Tables, the default value is (`SSE-S3`) (`AES256`) and it can't be changed.

- ** [`UploadPart`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html) **
  - **Supported headers:** `Content-Length` / **Notes:** None
  - **Supported headers:** `Content-MD5` / **Notes:** None
  - **Supported headers:** `x-amz-checksum-crc32` / **Notes:** None
  - **Supported headers:** `x-amz-checksum-crc32c` / **Notes:** None
  - **Supported headers:** `x-amz-checksum-sha1` / **Notes:** None
  - **Supported headers:** `x-amz-checksum-sha256` / **Notes:** None
  - **Supported headers:** `x-amz-expected-bucket-owner` / **Notes:** None

