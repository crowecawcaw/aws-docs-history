# GAMESEC04-BP01 Restrict access of downloadable content to

authorized clients and users

Restrict access to game content by authorized applications and
clients. Consider using Amazon S3 as a cost-effective and scalable
origin for storing downloadable game content and Amazon CloudFront
to provide globally performant content delivery to players. Both
services provide built-in mechanisms for restricting access to
data that is stored, such as restricting access to authenticated
users.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

**Granting access to content that is stored
in Amazon S3**

When you need to grant access to content that is stored in S3,
there are several factors to consider. By default, only the AWS account that created an S3 bucket can access the objects stored
within it. To grant access to your internal applications and to
manage content stored in Amazon S3 buckets,
use [AWS Identity and Access Management (IAM)](../../../AmazonS3/latest/userguide/s3-access-control.md "../../../AmazonS3/latest/userguide/s3-access-control.md") to create policies
that provide appropriate access. 

[IAM
roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") can be associated with federated users, systems, or
applications hosted in services, such as Amazon EC2, AWS Lambda,
and container-based applications hosted in Amazon EKS and Amazon ECS. For example, you might use the AWS SDK or AWS CLI to publish
and manage game content assets in S3 buckets. To support this use
case, you can create an IAM role with appropriate access to read
and write game content to your S3 buckets and associate it with
the EC2 instances that host your software and scripts.

Resource-based policies can be defined for your bucket and for
specific objects.
[S3 bucket policies](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md")
are associated with an S3 bucket and can be used to restrict
access to the bucket and objects within it, as well as grant
access to your Amazon S3 resources from other accounts. For
example, in scenarios where multiple teams or separate game
development studios are working on the same game content
and require the same access to centrally hosted content in Amazon S3, you can use an S3 bucket policy to define permissions for
cross-account access to the S3 resources. Consider
using [S3
access points](../../../AmazonS3/latest/userguide/access-points.md "../../../AmazonS3/latest/userguide/access-points.md"), which can simplify managing data access to
shared data by creating access points with names and permissions
specific to each application or sets of applications. The Amazon S3
documentation contains
additional [best
practices for access control in Amazon S3](../../../AmazonS3/latest/userguide/access-control-best-practices.md#access-control-best-practices-store-share "../../../AmazonS3/latest/userguide/access-control-best-practices.md#access-control-best-practices-store-share").

```
**Granting short-term access to your content**
```

When access is only need for a specific limited time, generate
temporary URLs that grant short term access to your content.
Amazon S3 provides support for
generating [presigned
URLs](../../../AmazonS3/latest/userguide/using-presigned-url.md "../../../AmazonS3/latest/userguide/using-presigned-url.md"), which allow object owners to grant time-limited
access to objects in Amazon S3 without updating your bucket
policy. By doing so, the end user or application that is being
granted access is not required to have an account or IAM
permissions and instead uses the presigned URL to access the
content. 

This is a best practice that is commonly used in a variety of
games use cases, such as granting authorized players access to
downloadable content that they have been entitled to and providing
temporary access to limited time game content. Presigned URLs can
also be used to provide temporary permissions for uploading
content to an S3 bucket. For example, you might consider using a
presigned URL to provide a player with access to upload client
logs for assisting your support team with troubleshooting a player
support case.

**Using a content delivery network to
provide access to your content**

While your applications, game developers, artists, and other
personnel may need direct access to the content in S3 buckets for
development and management purposes, use a content delivery
network to provide access to content that is publicly available to
players or other users over the internet. This approach improves
download performance and reduces costs by caching frequently
accessed content. Amazon CloudFront can globally distribute your
content by caching and delivering it closer to your players while
reducing the load on your game's download origin, such as Amazon S3.

Rather than serving your public content directly from S3 buckets,
it is recommended to keep this content private and serve it
publicly by using CloudFront. CloudFront can be configured to
require players to access your private content (such as a new game
download for paid players only) by using
either [signed
URLs](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.md") or
[signed
cookies](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-signed-cookies.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-signed-cookies.md"). You can then develop your application either to
create and distribute signed URLs to authenticated users, or to
send set-cookie headers that set signed cookies for authenticated
users. When you create signed URLs or signed cookies to control
access to your files, you can specify an ending date and time,
after which the URL and cookies are no longer valid. 

Optionally, you can also specify the IP address or range of
addresses of the computers that can be used to access your
content, which is useful if you want to restrict access to specific
game development studio partners or contractor networks. Use
signed cookies when you want to provide access to multiple
restricted files, or if you don't want to change your current
URLs. Use signed URLs when you want to restrict access to
individual files or if your users are using a client that doesn't
support cookies. Signed URLs take precedence over signed cookies.

### Implementation steps

- Use IAM roles and bucket policies to grant appropriate
  access to S3 buckets for internal applications, teams, or
  cross-account scenarios.
- Generate presigned URLs for granting short-term access to S3
  objects, suitable for downloadable content or temporary
  uploads like client logs.
- Use Amazon CloudFront with signed URLs or cookies to more
  securely serve private content to authenticated users
