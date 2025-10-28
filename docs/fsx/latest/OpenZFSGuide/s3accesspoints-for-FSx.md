# Accessing your data using Amazon S3 access points

Amazon S3 access points simplify managing data access for any application or AWS service that works with S3. With S3 access points,
customers with shared datasets, including data lakes, media archives, and user-generated content, can easily control and scale
data access for hundreds of applications, teams, or individuals by creating individualized access points with names and permissions
customized for each. You can also use S3 access points to access file data stored on Amazon FSx file systems as if it were in S3,
allowing you to use it with applications and services that work with S3 without application changes or moving data out of file storage.
These access points are named network endpoints that attach to either S3 general purpose buckets or FSx for OpenZFS volumes.

S3 access points attached to Amazon FSx for OpenZFS file systems support read and write access to your file data using S3 object operations
(for example, `GetObject`, `PutObject`, and `ListObjectsV2`) against an Amazon S3 endpoint.

Each S3 access point attached to an FSx for OpenZFS file system has an AWS Identity and Access Management (IAM) access point policy and an associated POSIX file system user
that is used to authorize all requests made through the access point. For each request, S3 first evaluates all the relevant policies, including
those on the user, access point, S3 VPC Endpoint, and service control policies, to authorize the request. Once the request is authorized by S3,
the request is then authorized by the file system, which evaluates whether the file system user associated with the S3 access point has permission
to access to the data on the file system. You can configure an access point to accept requests only from a virtual private cloud (VPC) to restrict
Amazon S3 data access to a private network. Amazon S3 enforces Block public access by default for all access points attached to an FSx for OpenZFS volume, and
you cannot modify or disable this setting.

You use the Amazon FSx console, CLI, and API to [create an S3 access point and attach](fsxz-creating-access-points.md "fsxz-creating-access-points.md") it to an FSx for OpenZFS volume. You can simultaneously access
your file data from the S3 access point using the S3 API, and from clients using the industry-standard Network File System (NFS) protocol (v3, v4.0, v4.1, v4.2).
Your data continues to reside on the FSx for OpenZFS file system.

Amazon S3 access points for FSx for OpenZFS ﬁle systems deliver latency in the tens of milliseconds range, consistent with S3 bucket access.
Performance scales with your Amazon FSx ﬁle system’s provisioned throughput, with maximum throughput and requests per second bound by
your underlying Amazon FSx ﬁle system conﬁguration. For more information about file system performance capabilities,
see [Performance for Amazon FSx for OpenZFS](performance.md "performance.md")

###### Topics

- [Access points naming rules, restrictions, and limitations](access-point-restrictions-limitations-naming-rules.md "access-point-restrictions-limitations-naming-rules.md")
- [Referencing access points with ARNs, access point aliases, or virtual-hosted-style URIs](referencing-access-points.md "referencing-access-points.md")
- [Access point compatibility](access-points-object-api-support.md "access-points-object-api-support.md")
- [Managing access point access](s3-ap-manage-access-fsx.md "s3-ap-manage-access-fsx.md")
- [Creating an access point](fsxz-creating-access-points.md "fsxz-creating-access-points.md")
- [Managing Amazon S3 access points](access-points-manage.md "access-points-manage.md")
- [Using access points](access-points-usage-examples.md "access-points-usage-examples.md")
- [Troubleshooting S3 access point issues](troubleshooting-access-points.md "troubleshooting-access-points.md")
