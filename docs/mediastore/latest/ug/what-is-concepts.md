End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# AWS Elemental MediaStore concepts and terminology

ARN

An [Amazon Resource Name](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

Body

The data to be uploaded into an object.

(Byte) range

A subset of object data to be addressed. For more information, see [range](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35 "https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35") from the HTTP specification.

Container

A namespace that holds objects. A container has an endpoint that you can use for writing and retrieving objects and attaching access
policies.

Endpoint

An entry point to the MediaStore service, given as an HTTPS root URL.

ETag

An [entity tag](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.19 "https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.19"), which is a hash of the object
data.

Folder

A division of a container. A folder can hold objects and other folders.

Item

A term used to refer to objects and folders.

Object

An asset, similar to an [Amazon S3 object](../../../s3.md "../../../s3.md"). Objects are the fundamental entities that are stored in
MediaStore. The service accepts all file types.

Origination service

MediaStore is considered an _origination service_ because it is the point of distribution for
media content delivery.

Path

A unique identifier for an object or folder, which indicates its location in the container.

Part

A subset of data (chunk) of an object.

Policy

An [IAM policy](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md").

Resource

An entity in AWS that you can work with. Each AWS resource is assigned an Amazon Resource Name (ARN) that acts as a unique identifier.
In MediaStore, this is the resource and its ARN format:

- Container:
  `aws:mediastore:`region`:`account-id`:container/:`containerName``
