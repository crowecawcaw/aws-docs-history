# Access points for directory buckets naming rules, restrictions, and
 limitations

Access points simplify managing data access at scale for shared datasets in Amazon S3. The
 following topics provide information about access point naming rules and restrictions and
 limitations.

###### Topics

* [Naming rules for access points for directory buckets](#access-points-directory-buckets-names "#access-points-directory-buckets-names")
* [Restrictions and limitations for access points for directory buckets](#access-points-directory-buckets-restrictions-limitations "#access-points-directory-buckets-restrictions-limitations")

## Naming rules for access points for directory buckets


An access point must be created in the same zone that the bucket is in. An access point name must be unique within the zone.


Access point names must be DNS-compliant and must meet the following conditions:



* Must begin with a number or lowercase letter
* The base name you provide must be between 3 and 50 characters long
* Can't begin or end with a hyphen (`-`)
* Can't contain underscores (`_`), uppercase letters, spaces, or periods
 (`.`)
* Must end with the suffix ``zoneid`--xa--s3`.

## Restrictions and limitations for access points for directory buckets


Access points for directory buckets have the following restrictions and limitations:



* Each access point is associated to one directory bucket. After you create an access point, you can't associate it to a different
 bucket. However, you can delete an access point, and then create a new one with the same name and associate it to a different bucket.
* After you create an access point, you can't change its virtual private cloud (VPC)
 configuration.
* Access point policies are limited to 20 KB in size.
* Access point scope prefixes are limited to 256 bytes in total size.
* You can create a maximum of 10,000 access points per AWS account per AWS Region. If you need
 more than 10,000 access points for a single account in a single Region, you can request a
 service quota increase. For more information about service quotas and requesting an
 increase, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html "https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html") in
 the *AWS General Reference*.
* You can only use access points to perform operations on objects. You can't use access points
 to perform Amazon S3 bucket operations, such as modifying or deleting buckets. For a
 complete list of supported operations, see [Object operations for access points for directory buckets](access-points-directory-buckets-service-api-support.md "access-points-directory-buckets-service-api-support.md").
* You can refer to access points by name, access point alias, or virtual-hosted-style URI. You cannot address access points by ARN. For more information, see [Referencing access points for directory buckets](access-points-directory-buckets-naming.md "access-points-directory-buckets-naming.md").
* API operations that control access point functionality (for example,
 `PutAccessPointPolicy` and `GetAccessPointPolicy`) must specify the AWS account that owns the access point.
* You must use AWS Signature Version 4 when making requests to an access point by using
 the REST API. For more information about authenticating requests, see [Authenticating
 Requests (AWS Signature Version 4)](../API/sig-v4-authenticating-requests.md "../API/sig-v4-authenticating-requests.md") in the *Amazon Simple Storage Service API Reference*.
* Access points only support requests over HTTPS. Amazon S3 will automatically respond with
 an HTTP redirect for any requests made through HTTP, to upgrade the request to
 HTTPS.
* Access points don't support anonymous access.
* If you create an access point to a bucket that's owned by another account (a cross-account access point), the 
 cross-account access point doesn't grant you access to data until the bucket owner grants you permission to access the bucket. 
 The bucket owner always retains ultimate control over access
 to the data and must update the bucket policy to authorize requests from the
 cross-account access point. To view a bucket policy example, see [Configuring IAM policies for using access points for directory buckets](access-points-directory-buckets-policies.md "access-points-directory-buckets-policies.md").
