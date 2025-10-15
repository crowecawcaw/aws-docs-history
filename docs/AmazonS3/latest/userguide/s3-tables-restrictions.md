# Security considerations and limitations for
 S3 Tables

The following list describes which security and access control features and functionality
 are unsupported or limited for S3 Tables.


* Public access policies are not supported. Users can't modify bucket or table
 policies to allow public access.
* Presigned URLs to access objects associated with a table are not supported.
* Tags are not supported for table buckets and tables. Therefore, support for
 attribute-based access control and tag-based allocation is unavailable.
* Requests made over HTTP are not supported. Amazon S3 automatically responds with an
 HTTP redirect for any requests made via HTTP to upgrade the requests to
 HTTPS.
* You must use AWS Signature Version 4 when making requests to an access point by
 using the REST APIs.
* Requests made over the Internet Protocol version 6 (IPv6) are supported only for
 object-level actions over table storage endpoints, and not for the table- and
 bucket-level actions.
* Table bucket and table access policies are limited to 20 KB in size.
