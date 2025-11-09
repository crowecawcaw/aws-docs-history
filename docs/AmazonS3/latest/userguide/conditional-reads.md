# How to retrieve or copy objects based on metadata with conditional reads

With conditional reads, you can add an additional header to your read request in order to add
preconditions to your S3 operation. If these preconditions are not met the read request will
fail.

You can use conditional reads on `GET`, `HEAD`, or `COPY` requests to only return an
object based on its metadata.

When you upload an object, Amazon S3 creates system controlled metadata that can only be
modified by S3. Entity tags (ETags) and Last-Modified are examples of system controlled
metadata. An object's ETag is a string representing a specific version of an object.
Last-Modified date is metadata representing an object's creation date or the last modified
date, whichever is the latest.

With conditional reads, you can return an object based on the
object's ETag or Last-Modified date. You can specify an ETag value with your request and
return the object only if the ETag value matches. This can ensure you only return or copy a specific
version of an object. You can specify a Last-Modified value with your read request
and return an object only if that object has been modified since a date you provide.

## Supported APIs

The following S3 APIs support using conditional reads:

- [GetObject](../API/API_GetObject.md "../API/API_GetObject.md")
- [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md")
- [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md")

You can use the following headers to return an object dependent on the entity tag
(ETag) or last modified date. For more information about object metadata such as ETags
and Last-Modified, see [System-defined object metadata](UsingMetadata.md#SysMetadata "UsingMetadata.md#SysMetadata").

###### [GetObject](../API/API_GetObject.md "../API/API_GetObject.md")

- `If-Match` — Return the object only if its ETag matches the one provided.
- `If-Modified-Since` — Return the object only if it has been modified
  since the time specified.
- `If-None-Match` — Return the object only if its ETag does not matches the
  one provided.
- `If-Unmodified-Since` — Return the object only if it has not been
  modified since the time specified.

For more information about these headers, errors returned, and the order S3 handles
multiple conditional headers in a single request, see [GetObject](../API/API_GetObject.md "../API/API_GetObject.md") in the
Amazon Simple Storage Service API Reference.

###### [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md")

- `If-Match` — Return the object only if its ETag matches the one provided.
- `If-Modified-Since` — Return the object only if it has been modified
  since the time specified.
- `If-None-Match` — Return the object only if its ETag does not matches the
  one provided.
- `If-Unmodified-Since` — Return the object only if it has not been
  modified since the time specified.

For more information about these headers, errors returned, and the order S3 handles
multiple conditional headers in a single request, see [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md") in the
Amazon Simple Storage Service API Reference.

###### [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md")

- `x-amz-copy-source-if-match` — Copies the source object only if its ETag
  matches the one provided.
- `x-amz-copy-source-if-modified-since` — Copies the source object only if
  it has been modified since the time specified.
- `x-amz-copy-source-if-none-match` — Copies the source object only if its
  ETag does not matches the one provided.
- `x-amz-copy-source-if-unmodified-since` — Copies the source object only
  if it has not been modified since the time specified.
- `If-Match` — Copies the object only if its ETag matches the
  one provided. `If-Match` expects the ETag value as a string.
- `If-None-Match` — Copies the object only if its ETag does
  not match the one provided. `If-None-Match` expects the '\*' (asterisk)
  character.

For more information about these headers, errors returned, and the order S3 handles
multiple conditional headers in a single request, see [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") in the
Amazon Simple Storage Service API Reference.
