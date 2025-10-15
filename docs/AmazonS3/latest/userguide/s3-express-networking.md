# Networking for directory buckets

To access directory buckets and objects inside, you use Regional and Zonal
 API endpoints that are different from the standard Amazon S3 endpoints. Depending on the S3 API
 operation that you use, either a Zonal or Regional endpoint is required. For a complete list
 of API operations by endpoint type, see [Differences for directory buckets](s3-express-differences.md "s3-express-differences.md"). 

You can access both Zonal and Regional API operations through gateway virtual private
 cloud (VPC) endpoints.

The following topics describe the networking requirements for accessing S3 Express One Zone by
 using a gateway VPC endpoint.

###### Topics

* [Endpoints](#s3-express-endpoints "#s3-express-endpoints")
* [Configuring VPC gateway
 endpoints](#s3-express-networking-vpc-gateway-directory "#s3-express-networking-vpc-gateway-directory")

## Endpoints


You can access directory buckets and objects inside from your VPC by
 using gateway VPC endpoints. Directory buckets use Regional and Zonal API endpoints.
 Depending on the Amazon S3 API operation that you use, either a Regional or Zonal endpoint is
 required. There is no additional charge for using gateway endpoints.


Bucket-level (or control plane) API operations are available through Regional
 endpoints and are referred to as Regional endpoint API operations. Examples of Regional
 endpoint API operations are `CreateBucket` and `DeleteBucket`.
 When you create a directory bucket, you choose a single Zone (Availability Zone or Local Zone) where your
 directory bucket will be created. After you create a directory bucket, you can use Zonal
 endpoint API operations to upload and manage the objects in your directory
 bucket.


Object-level (or data plane) API operations are available through Zonal endpoints and
 are referred to as Zonal endpoint API operations. Examples of Zonal endpoint API
 operations are `CreateSession` and `PutObject`.


For more information about the endpoints and the locations that support directory buckets in Availability Zones, see [Endpoints for directory buckets in Availability Zones](directory-bucket-az-networking.md#s3-express-endpoints-az "directory-bucket-az-networking.md#s3-express-endpoints-az"). 
 


For more information about the endpoints and the locations that support directory buckets in Local Zones, see [Enable accounts for Local Zones](opt-in-directory-bucket-lz.md "opt-in-directory-bucket-lz.md"). 
 


## Configuring VPC gateway
 endpoints


To configure gateway VPC endpoints for access directory buckets in Availability Zones, see [Configuring VPC gateway
 endpoints](directory-bucket-az-networking.md#s3-express-networking-vpc-gateway "directory-bucket-az-networking.md#s3-express-networking-vpc-gateway").


To configure gateway VPC endpoints for access directory buckets in Local Zones, see [Private connectivity from your
 VPC](connectivity-lz-directory-buckets.md "connectivity-lz-directory-buckets.md").
