# How to perform conditional deletes

You can use conditional deletes to evaluate if your object exists or is unchanged before deleting it.
You can perform conditional deletes using the `DeleteObject` or `DeleteObjects` API operations in S3 general purpose and directory buckets.
To get started, when making a conditional delete request, you can use the `HTTP If-Match` header with the precondition value `*`
to check if object exists or the `If-Match` header with your provided `ETag` to check if the object has been modified.

You can enforce conditional deletes at a general purpose bucket level using S3 bucket or Identity and Access Management (IAM) policies.
For more information, see [Enforce conditional deletes on Amazon S3 buckets](conditional-delete-enforce.md "conditional-delete-enforce.md").

###### Note

Conditional delete evaluations only apply to the current version of the object.

###### Topics

- [How to check if your object has been modified before deleting it](#conditional-deletes-etags "#conditional-deletes-etags")
- [How to check if your object exists before deleting it](#conditional-delete "#conditional-delete")
- [Enforce conditional deletes on Amazon S3 buckets](conditional-delete-enforce.md "conditional-delete-enforce.md")

## How to check if your object has been modified before deleting it

With conditional deletes, you can protect your application from accidental deletions of objects.
You can use the `HTTP If-Match` header with the `ETag` value to check if an object has been modified.
If the `ETag` value of an object in an S3 bucket doesn’t match with the `ETag` that you provide during
the delete operation, the operation fails. For conditionally deleting multiple objects using the `DeleteObjects` operation,
you must provide the `ETag` value in the `ETag` element of the object in the XML request body.
For more information, see [Using Content-MD5 and the ETag to verify uploaded objects](checking-object-integrity-upload.md#checking-object-integrity-etag-and-md5 "checking-object-integrity-upload.md#checking-object-integrity-etag-and-md5").

###### Note

To perform conditional deletes
with the `If-Match` header with the `ETag` value, you must have
the `s3:DeleteObject` and `s3:GetObject` permissions.

The `If-Match` header with the `ETag` value evaluates
against existing objects in a bucket. If there's an existing object with the same key name and matching `ETag`,
the `DeleteObject` requests succeeds, and returns a `204 No content` response.
If the `ETag` doesn't match, the delete operation fails with a `412 Precondition Failed` response.
If successful, The `DeleteObjects` API responds with a `200 OK` and
provides the status of each object in the response body of the batch delete request.
If preconditions aren’t satisfied for a `DeleteObjects` request,
Amazon S3 deletes the objects and returns a `Pre-condition` failed error response.

You can also receive a `409 Conflict` error response in the case of
concurrent requests if a `DELETE` or `PUT` request to an object succeeds before a
conditional delete operation on that object completes. You will receive a `404 Not
 Found` response if a concurrent delete request to an object succeeds before a
conditional write operation on that object completes, as the object key no longer
exists.

You can use the `If-Match` header with the `ETag` value for the following APIs:

- [DeleteObject](../API/API_DeleteObject.md "../API/API_DeleteObject.md")
- [DeleteObjects](../API/API_DeleteObjects.md "../API/API_DeleteObjects.md")

The following `delete-object` example command attempts to perform a
conditional delete with the provided ETag value
`6805f2cfc46c0f04559748bb039d69al`.

```
aws s3api delete-object --bucket `amzn-s3-demo-bucket` --key dir-1/`my_images.tar.bz2` --if-match "`6805f2cfc46c0f04559748bb039d69al`"
```

For more information, see [delete-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-object.html") in the _AWS CLI Command Reference_.

The following `delete-objects` example command attempts to perform a
conditional delete with the provided ETag value
`6805f2cfc46c0f04559748bb039d69al`.

```
aws s3api delete-objects --bucket `amzn-s3-demo-bucket` --delete '{"Objects":[{"Key":"my_images.tar.bz2", "ETag": "6805f2cfc46c0f04559748bb039d69al"}]}'
```

For more information, see [delete-objects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-objects.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-objects.html") in the _AWS CLI Command Reference_.

For information about the AWS CLI, see [What
is the AWS Command Line Interface?](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") in the _AWS Command Line Interface User Guide_.

## How to check if your object exists before deleting it

You can use the `If-Match` header with the `*` value to check if
the object exists before attempting to delete it. The `*` value signifies
that the operation should only proceed if the object exists, regardless of whether it has been modified or not.

Delete markers are special objects in versioned S3 general purpose buckets that
indicate that an object has been deleted. They are placeholders that make the object
appear deleted while preserving the previous versions. Therefore, when you use
`If-Match:*` with a `DeleteObject` API,
the operation will only succeed with a `204 No Content` if the object exists.
If the latest version of the object is a delete marker, the object doesn't exist and the `DeleteObject`
API will fail and return a `412 Precondition Failed` response. For more information about delete markers, see [Working with delete markers](DeleteMarker.md "DeleteMarker.md").

To conditionally delete multiple objects using the `DeleteObjects` operation,
you can provide the `*` in the `ETag` element of the object in the XML request body.
If the precondition succeeds, the `DeleteObjects` operation responds with a `200 OK`
and provides the status of each object in the response body.
If the precondition succeeds, the response for that object will be captured in the `<Deleted>` element of the response body.
If the precondition fails then the response for that object will be captured in the
`<Error>` element of the response body.
If the object doesn’t exist when evaluating either of the preconditions, S3 rejects the request and returns a `Not Found` error response.

###### Note

To perform conditional deletes with `If-Match:*`, you must have `s3:DeleteObject` permissions.

You can use the `If-Match` header with the `*` value for the following APIs:

- [DeleteObject](../API/API_DeleteObject.md "../API/API_DeleteObject.md")
- [DeleteObjects](../API/API_DeleteObjects.md "../API/API_DeleteObjects.md")

The following `delete-object` example command attempts to perform a
conditional delete for an object with the key name
`my_images.tar.bz2` that has a
value of `*` which represents any ETag.

```
aws s3api delete-object --bucket `amzn-s3-demo-bucket` --key dir-1/`my_images.tar.bz2` --if-match "`*`"
```

For more information, see [delete-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-object.html") in the _AWS CLI Command Reference_.

The following `delete-objects` example command attempts to perform
a conditional delete for an object with the key name
`my_images.tar.bz2` that has a
value of `*` which represents any ETag.

```
aws s3api delete-objects --bucket `amzn-s3-demo-bucket` --delete '{"Objects":[{"Key":"`my_images.tar.bz2`", "ETag": "`*`"}]}'
```

For more information, see [delete-objects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-objects.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-objects.html") in the _AWS CLI Command Reference_.

For information about the AWS CLI, see [What
is the AWS Command Line Interface?](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") in the _AWS Command Line Interface User Guide_.
