# Deleting an object from an MFA delete-enabled

bucket

When you configure MFA delete, only the root user can permanently delete object versions or
change the versioning configuration on your S3 bucket. You must use an MFA device to authenticate the root user to perform the delete action.

If a bucket's versioning configuration is MFA delete enabled, the bucket owner
must include the `x-amz-mfa` request header in requests to permanently
delete an object version or change the versioning state of the bucket. Requests that
include `x-amz-mfa` must use HTTPS.

The header's value is the concatenation of your authentication device's serial
number, a space, and the authentication code displayed on it. If you don't include
this request header, the request fails.

When using the AWS CLI include the same information as the value of the `mfa` parameter.

For more information about authentication devices, see [Multi-factor
Authentication](https://aws.amazon.com/iam/details/mfa/ "https://aws.amazon.com/iam/details/mfa/").

For more information about enabling MFA delete, see [Configuring MFA delete](MultiFactorAuthenticationDelete.md "MultiFactorAuthenticationDelete.md").

###### Note

Deleting an object in a versioning-enabled bucket that is MFA delete enabled is not available through the AWS Management Console.

To delete an object in a versioning-enabled bucket that is MFA
delete enabled, use the following command. When you
use the following example command, replace the `user input
 placeholders` with your own information.

```

 aws s3api delete-object --bucket ``amzn-s3-demo-bucket`` --key `OBJECT-KEY` --version-id `"VERSION ID"` --mfa "`MFA_DEVICE_SERIAL_NUMBER` `MFA_DEVICE_CODE`"

```

The following example deletes `my-image.jpg` (with the
specified version), which is in a bucket configured with MFA delete enabled.

For more information, see
[DeleteObject](../API/RESTObjectDELETE.md "../API/RESTObjectDELETE.md") in the Amazon Simple Storage Service API Reference

```

DELETE /my-image.jpg?versionId=3HL4kqCxf3vjVBH40Nrjfkd HTTPS/1.1
Host: bucketName.s3.amazonaws.com
x-amz-mfa: 20899872 301749
Date: Wed, 28 Oct 2009 22:32:00 GMT
Authorization: AWS AKIAIOSFODNN7EXAMPLE:0RQf4/cRonhpaBX5sCYVf1bNRuU=
```
