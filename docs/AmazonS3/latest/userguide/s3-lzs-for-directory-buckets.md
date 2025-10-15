# Concepts for directory buckets in
 Local Zones

Before creating a directory bucket in a Local Zone, you must have the Local Zone ID where you want to create a bucket. You can find all Local Zone information by using the
 [DescribeAvailabilityZones](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html "https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html") API operation. This API operation lists information about Local Zones, including their Local Zone IDs, parent Region names, network border
 groups, and opt-in status. After you have your Local Zone ID and you are opted in, you can create a directory bucket in the Local Zone. A directory bucket name consists of a base name that you provide and a suffix
 that contains the Zone ID of your bucket location, followed by `--x-s3`. 

A Local Zone is connected to the **parent Region** using the Amazon redundant and very high-bandwidth private network. This gives applications running in the
 Local Zone fast, secure, and seamless access to the rest of the AWS services in the parent Region. **Parent Zone ID** is the ID of the zone that handles the
 Local Zone control plane operations. **Network Border
 Group** is a unique group from which AWS advertises public IP addresses. For
 more information about Local Zones, parent Region, and parent Zone ID, see [AWS Local Zones
 concepts](https://docs.aws.amazon.com/local-zones/latest/ug/concepts-local-zones.html "https://docs.aws.amazon.com/local-zones/latest/ug/concepts-local-zones.html") in the AWS Local Zones *User Guide*.

All directory buckets use the `s3express` namespace, which is separate from
 the `s3` namespace for general purpose buckets. For directory buckets, requests are
 routed to either a **Regional endpoint** or a **Zonal endpoint**. The routing is handled automatically for you if
 you use the AWS Management Console, AWS CLI, or AWS SDKs. 

Most bucket-level API operations (such as `CreateBucket` and
 `DeleteBucket`) are routed to Regional endpoints, and are referred to as
 Regional endpoint API operations. Regional endpoints are in the format of
 `s3express-control.ParentRegionCode.amazonaws.com`. All object-level API
 operations (such as `PutObject`) and two bucket-level API operations
 (`CreateSession` and `HeadBucket`) are routed to Zonal endpoints,
 and are referred to as Zonal endpoint API operations. Zonal endpoints are in the format of
 `s3express-LocalZoneID.ParentRegionCode.amazonaws.com`. For a complete list
 of API operations by endpoint type, see [Directory bucket API operations](s3-express-differences.md#s3-express-differences-api-operations "s3-express-differences.md#s3-express-differences-api-operations").

To access directory buckets in Local Zones from your virtual private cloud (VPC), you can use gateway VPC
 endpoints. There is no additional charge for using gateway endpoints. To configure gateway
 VPC endpoints to access directory buckets and objects in Local Zones, see [Private connectivity from your
 VPC](connectivity-lz-directory-buckets.md "connectivity-lz-directory-buckets.md").
