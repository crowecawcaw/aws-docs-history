# How to prevent object overwrites with conditional writes

By using conditional writes, you can add an additional header to your `WRITE` requests
to specify preconditions for your Amazon S3 operation. To conditionally write objects, add the
HTTP `If-None-Match` or `If-Match` header.

The `If-None-Match` header prevents overwrites of existing data by validating
that there's not an object with the same key name already in your bucket.

Alternatively, you can add the `If-Match` header to check an object's entity
tag (ETag) before writing an object. With this header, Amazon S3 compares the provided ETag value
with the ETag value of the object in S3. If the ETag values don't match, the operation
fails.

Bucket owners can use bucket policies to enforce conditional writes for uploaded objects. For
more information, see [Enforce conditional writes on Amazon S3 buckets](conditional-writes-enforce.md "conditional-writes-enforce.md").

###### Note

To use conditional writes, you must make the requests over HTTPS (TLS) or use AWS
Signature Version 4 to sign the request.

###### Topics

- [How to prevent object overwrites based on
  key names](#conditional-write-key-names "#conditional-write-key-names")
- [How to prevent overwrites if the object has changed](#conditional-write-etags "#conditional-write-etags")
- [Conditional write behavior](#conditional-error-response "#conditional-error-response")
- [Conditional write scenarios](#conditional-write-scenarios "#conditional-write-scenarios")
- [Enforce conditional writes on Amazon S3 buckets](conditional-writes-enforce.md "conditional-writes-enforce.md")

## How to prevent object overwrites based on

key names

You can use the HTTP `If-None-Match` conditional header to check whether an
object already exists in the specified bucket based on its key name before creating it
or copying it to the destination bucket.

Conditional writes with the HTTP `If-None-Match` header check for
the existence of an object during the `WRITE` operation. If an identical key
name is found in the bucket, the operation fails. Without the HTTP
`If-None-Match` header, if you upload or copy an object with an identical
key name in an unversioned or version-suspended bucket, the object is overwritten. For
more information about using key names, see [Naming Amazon S3 objects](object-keys.md "object-keys.md").

###### Note

The HTTP `If-None-Match` header only applies to the current version of an object in a version bucket.

To perform conditional writes with the HTTP `If-None-Match` header you must have
the `s3:PutObject` permission. This enables the caller to check for the
presence of objects in the bucket. The `If-None-Match` header expects the \*
(asterisk) value.

You can use the `If-None-Match` header with the following APIs:

- [PutObject](../API/API_PutObject.md "../API/API_PutObject.md")
- [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")
- [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md")

The following `put-object` example command attempts to perform a
conditional write for an object with the key name
`dir-1/my_images.tar.bz2`.

```
aws s3api put-object --bucket `amzn-s3-demo-bucket` --key dir-1/my_images.tar.bz2 --body my_images.tar.bz2 --if-none-match "*"
```

For more information, see [put-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html") in the _AWS CLI Command Reference_.

For information about the AWS CLI, see [What
is the AWS Command Line Interface?](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") in the _AWS Command Line Interface User Guide_.

The following `copy-object` example command attempts to copy an object to a destination bucket with a
conditional write for an object with the key name
`dir-1/my_images.tar.bz2`.

```
aws s3api copy-object --copy-source `amzn-s3-demo-bucket`/key --key dir-1/my_images.tar.bz2 --bucket `amzn-s3-demo-bucket2` --if-none-match "*"
```

For more information, see [copy-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html") in the _AWS CLI Command Reference_.

For information about the AWS CLI, see [What
is the AWS Command Line Interface?](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") in the _AWS Command Line Interface User Guide_.

The following `complete-multipart-upload` example command attempts to complete a multipart upload with a conditional write for an object with the key name
`dir-1/my_images.tar.bz2`. In this example, the
file:// prefix is used to load the JSON structure from a file in the local
folder named `mpustruct` which list of all the parts that
have been uploaded for tnis specific multipart upload.

```
aws s3api complete-multipart-upload --multipart-upload file://mpustruct --bucket `amzn-s3-demo-bucket` --key dir-1/my_images.tar.bz2 --upload-id `upload-id`  --if-none-match "*"
```

For more information, see [complete-multipart-upload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/complete-multipart-upload.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/complete-multipart-upload.html") in the _AWS CLI Command Reference_.

For information about the AWS CLI, see [What
is the AWS Command Line Interface?](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") in the _AWS Command Line Interface User Guide_.

## How to prevent overwrites if the object has changed

An object's ETag is a string that's unique to the object and reflects a change to the
object's content. You can use the `If-Match` header to compare the ETag value
of an object in an Amazon S3 bucket with one that you provide during the `WRITE`
operation. If the ETag values don't match, the operation fails. For more information
about ETags, see [Using Content-MD5 and the ETag
to verify uploaded objects](checking-object-integrity-upload.md#checking-object-integrity-etag-and-md5 "checking-object-integrity-upload.md#checking-object-integrity-etag-and-md5").

To perform conditional writes with an HTTP `If-Match` header you must have the
`s3:PutObject` and `s3:GetObject` permissions. This enables
the caller to check the ETag and verify the state of the objects in the bucket. The
`If-Match` header expects the ETag value as a string.

You can use the `If-Match` header with the following APIs:

- [PutObject](../API/API_PutObject.md "../API/API_PutObject.md")
- [CompleteMultipartUpload](../API/API_CompleteMultipartUpload.md "../API/API_CompleteMultipartUpload.md")
- [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md")

The following `put-object` example command attempts to perform a
conditional write with the provided ETag value
`6805f2cfc46c0f04559748bb039d69ae`.

```
aws s3api put-object --bucket `amzn-s3-demo-bucket` --key dir-1/my_images.tar.bz2 --body my_images.tar.bz2 --if-match "`6805f2cfc46c0f04559748bb039d69ae`"
```

For more information, see [put-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html") in the _AWS CLI Command Reference_.

For information about the AWS CLI, see [What
is the AWS Command Line Interface?](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") in the _AWS Command Line Interface User Guide_.

The following `copy-object` example command attempts to perform a
conditional write with the provided ETag value
`6805f2cfc46c0f04559748bb039d69ae`.

```
aws s3api copy-object --copy-source `amzn-s3-demo-bucket`/key --key dir-1/my_images.tar.bz2 --bucket `amzn-s3-demo-bucket2` --if-match "`6805f2cfc46c0f04559748bb039d69ae`"
```

For more information, see [copy-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html") in the _AWS CLI Command Reference_.

For information about the AWS CLI, see [What
is the AWS Command Line Interface?](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") in the _AWS Command Line Interface User Guide_.

The following `complete-multipart-upload` example command attempts
to complete a multipart upload with a conditional write using the provided ETag value
`6805f2cfc46c0f04559748bb039d69ae`. In this example, the
file:// prefix is used to load the JSON structure from a file in the local
folder named `mpustruct` which list of all the parts that
have been uploaded for tnis specific multipart upload.

```
aws s3api complete-multipart-upload --multipart-upload file://mpustruct --bucket `amzn-s3-demo-bucket` --key dir-1/my_images.tar.bz2 --upload-id `upload-id` --if-match "`6805f2cfc46c0f04559748bb039d69ae`"
```

For more information, see [complete-multipart-upload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/complete-multipart-upload.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/complete-multipart-upload.html") in the _AWS CLI Command Reference_.

For information about the AWS CLI, see [What
is the AWS Command Line Interface?](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") in the _AWS Command Line Interface User Guide_.

## Conditional write behavior

**Conditional writesor copies with `If-None-Match` header**

Conditional writes with the `If-None-Match` header evaluate
against existing objects in a bucket. If there's no existing object with the
same key name in the bucket, the write operation succeeds, resulting in a
`200 OK` response. If there's an existing object, the write
operation fails, resulting in a `412 Precondition Failed`
response.

For buckets with versioning enabled, if there's no current object version
with the same name, or if the current object version is a delete marker, the
write operation succeeds. Otherwise, it results in a failed write operation
with a `412 Precondition Failed` response.

If multiple conditional writes or copies occur for the same object name, the first write
operation to finish succeeds. Amazon S3 then fails subsequent writes with a
`412 Precondition Failed` response.

You can also receive a `409 Conflict` response in the case of
concurrent requests if a delete request to an object succeeds before a
conditional write operation on that object completes. When using conditional writes
with `PutObject`, uploads may be retried after receiving a
`409 Conflict` error. When using
`CompleteMultipartUpload`, the entire multipart upload must be
re-initiated with `CreateMultipartUpload` to upload the object
again after receiving a `409 Conflict` error.

**Conditional writes or copies with `If-Match` header**

The `If-Match` header evaluates against existing objects in a
bucket. If there's an existing object with the same key name and matching
ETag, the write operation succeeds, resulting in a `200 OK`
response. If the ETag doesn't match, the write operation fails with a
`412 Precondition Failed` response.

You can also receive a `409 Conflict` response in the case of
concurrent requests.

You will receive a `404 Not Found` response if a concurrent
delete request to an object succeeds before a conditional write operation on
that object completes, as the object key no longer exists. You should
reupload the object when you receive a `404 Not Found`
response.

If there's no current object version with the same name, or if the current
object version is a delete marker, the operation fails with a `404 Not
 Found` error.

## Conditional write scenarios

Consider the following scenarios where two clients are running operations on the same
bucket.

###### Conditional writes during multipart uploads

Conditional writes do not consider any in-progress multipart uploads requests since
those are not yet fully written objects. Consider the following example where Client
1 is uploading an object using multipart upload. During the multipart upload, Client 2 is able to
successfully write the same object with the conditional write operation. Subsequently, when
Client 1 tries to complete the multipart upload using a conditional write the upload fails.

###### Note

This scenario will result in a `412 Precondition Failed` response for both `If-None-Match` and `If-Match` headers.

![An example of two clients writing items with the same key name. One with UploadPart for MPU and one with PutObject and a conditional write. The CompleteMultipartUpload operation, which starts after, fails.](images/conwrite_put_mpu.png)

###### Concurrent deletes during multipart uploads

If a delete request succeeds before a conditional write request can complete, Amazon S3
returns a `409 Conflict` or `404 Not Found` response for the
write operation. This is because the delete request that was initiated earlier takes
precedence over the conditional write operation. In such cases, you must initiate a
new multipart upload.

###### Note

This scenario will result in a `409 Conflict` response for an
`If-None-Match` header and a `404 Not Found` response for
an `If-Match` header.

![An example of two clients, one using multipart upload and one sending a delete request after the MPU has started. The delete request finishes before the conditional write starts.](images/conwrite_delete_mpu.png)

###### Note

To minimize your storage costs, we recommend that you configure a lifecycle rule
to delete incomplete multipart uploads after a specified number of days by using the
`AbortIncompleteMultipartUpload` action. For more information about
creating a lifecycle rule to delete incomplete multipart uploads, see [Configuring a
bucket lifecycle configuration to delete incomplete multipart
uploads](mpu-abort-incomplete-mpu-lifecycle-config.md "mpu-abort-incomplete-mpu-lifecycle-config.md").
