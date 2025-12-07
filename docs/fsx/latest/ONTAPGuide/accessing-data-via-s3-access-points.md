# Accessing your data via Amazon S3 access points

You can also use S3 access points to access file data stored on Amazon FSx file systems as if it were in S3,
allowing you to use it with applications and services that work with S3 without application changes or moving data out of file storage.
Amazon S3 access points are S3 endpoints that attach to either S3 buckets or FSx for ONTAP and FSx for OpenZFS volumes. Amazon S3 access points simplify managing data access for any application or AWS service that works with S3. With S3 access points,
customers with shared datasets, including data lakes, media archives, and user-generated content, can easily control and scale
data access for hundreds of applications, teams, or individuals by creating individualized access points with names and permissions
customized for each.

S3 access points attached to Amazon FSx for NetApp ONTAP volumes support read and write access to your file data using S3 object operations
(for example, `GetObject`, `PutObject`, and `ListObjectsV2`) against an Amazon S3 endpoint.

Each S3 access point attached to an FSx for ONTAP file system has an AWS Identity and Access Management (IAM) access point policy and an associated UNIX or Windows file system user
that is used to authorize all requests made through the access point. For each request, S3 first evaluates all the relevant policies, including
those on the user, access point, S3 VPC Endpoint, and service control policies, to authorize the request. Once the request is authorized by S3,
the request is then authorized by the file system, which evaluates whether the file system user associated with the S3 access point has permission
to access to the data on the file system. You can configure an access point to accept requests only from a virtual private cloud (VPC) to restrict
Amazon S3 data access to a private network. Amazon S3 enforces Block public access by default for all access points attached to an FSx for ONTAP volume, and
you cannot modify or disable this setting.

You use the Amazon FSx console, CLI, and API to [create an S3 access point and attach](fsxn-creating-access-points.md "fsxn-creating-access-points.md") it to an FSx for ONTAP volume.
The access point allows you to access your file data using the S3 API, though your data continues to reside on your FSx for ONTAP file system and you can continue using the NFS and SMB protocols to access your data alongside the S3 API.

Amazon S3 access points for FSx for ONTAP ﬁle systems deliver latency in the tens of milliseconds range, consistent with S3 bucket access.
The throughput and requests per second you can drive to an Amazon FSx file system via the S3 API depends on the file system's provisioned throughput.
For more information about file system performance capabilities, see [Amazon FSx for NetApp ONTAP performance](performance.md "performance.md")

###### Topics

- [AWS Regions with Amazon S3 access points for FSx for ONTAP](#access-points-for-fsx-ontap-supported-regions "#access-points-for-fsx-ontap-supported-regions")
- [Access points naming rules, restrictions, and limitations](access-point-for-fsxn-restrictions-limitations-naming-rules.md "access-point-for-fsxn-restrictions-limitations-naming-rules.md")
- [Referencing access points with ARNs, access point aliases, or virtual-hosted-style URIs](referencing-access-points-for-fsxn.md "referencing-access-points-for-fsxn.md")
- [Access point compatibility](access-points-for-fsxn-object-api-support.md "access-points-for-fsxn-object-api-support.md")
- [Managing access point access](s3-ap-manage-access-fsxn.md "s3-ap-manage-access-fsxn.md")
- [Creating an access point](fsxn-creating-access-points.md "fsxn-creating-access-points.md")
- [Managing Amazon S3 access points](access-points-for-fsxn-manage.md "access-points-for-fsxn-manage.md")
- [Using access points](access-points-for-fsxn-usage-examples.md "access-points-for-fsxn-usage-examples.md")
- [Troubleshooting S3 access point issues](troubleshooting-access-points-for-fsxn.md "troubleshooting-access-points-for-fsxn.md")

## AWS Regions with Amazon S3 access points for FSx for ONTAP

Amazon S3 access points for FSx for ONTAP are supported in the following AWS Regions: Africa (Cape Town), Asia Pacific (Hong Kong, Hyderabad, Jakarta, Melbourne, Mumbai, Osaka, Seoul, Singapore, Sydney, Tokyo), Canada (Central), Canada West (Calgary), Europe (Frankfurt, Ireland, London, Milan, Paris, Spain, Stockholm, Zurich), Israel (Tel Aviv), Middle East (Bahrain, UAE), South America (São Paulo), US East (N. Virginia, Ohio), and US West (N. California, Oregon).
