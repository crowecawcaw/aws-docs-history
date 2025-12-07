# Managing access to shared datasets with access points

Amazon S3 access points simplify data access for any AWS service or customer application that stores
data in S3. Access points are named network endpoints that are attached to a data source such
as a bucket, Amazon FSx for NetApp ONTAP volume, or Amazon FSx for OpenZFS volume. For information about working with buckets, see
[General purpose buckets overview](UsingBucket.md "UsingBucket.md"). For information about working
with FSx for NetApp ONTAP, see [What is Amazon FSx for NetApp ONTAP](../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md "../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md") in the _FSx for ONTAP User
Guide_. For information about working
with FSx for OpenZFS, see [What is Amazon FSx for OpenZFS](../../../fsx/latest/OpenZFSGuide/what-is-fsx.md "../../../fsx/latest/OpenZFSGuide/what-is-fsx.md") in the _FSx for OpenZFS User
Guide_.

You can use access points to perform S3 object operations, such as `GetObject` and
`PutObject`. Each access point has distinct permissions and network controls that S3
applies for any request that is made through that access point. Each endpoint enforces a customized
access point policy that allow you to control use by resource, user, or other conditions. If your
access point is attached to a bucket the access point policy works in conjunction with the underlying bucket
policy. You can configure any access point to accept requests only from a virtual private cloud
(VPC) to restrict Amazon S3 data access to a private network. You can also configure custom block
public access settings for each access point.

###### Note

You can only use access points to perform operations on objects. You can't use access points to
perform other Amazon S3 operations, such as deleting buckets or creating S3 Replication
configurations. For a complete list of S3 operations that support access points, see [Access point compatibility](access-points-service-api-support.md "access-points-service-api-support.md").

The topics in this section explain how to work with Amazon S3 access points. For topics on using access points with directory buckets see, [Managing access to shared datasets in directory buckets with access points](access-points-directory-buckets.md "access-points-directory-buckets.md").

###### Topics

- [Access points naming rules, restrictions, and
  limitations](access-points-restrictions-limitations-naming-rules.md "access-points-restrictions-limitations-naming-rules.md")
- [Referencing access points with ARNs, access point aliases, or virtual-hosted–style URIs](access-points-naming.md "access-points-naming.md")
- [Access point compatibility](access-points-service-api-support.md "access-points-service-api-support.md")
- [Configuring IAM policies for using access points](access-points-policies.md "access-points-policies.md")
- [Monitoring and logging access points](access-points-monitoring-logging.md "access-points-monitoring-logging.md")
- [Creating an access point](creating-access-points.md "creating-access-points.md")
- [Managing your Amazon S3 access points for general purpose buckets](access-points-manage.md "access-points-manage.md")
- [Using Amazon S3 access points for general purpose buckets](using-access-points.md "using-access-points.md")
- [Using tags with S3 Access Points for general purpose buckets](access-points-tagging.md "access-points-tagging.md")
