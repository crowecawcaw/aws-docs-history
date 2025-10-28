# Regional and Zonal endpoints for directory buckets

To access the Regional and Zonal endpoints for directory buckets from your
virtual private cloud (VPC), you can use gateway VPC endpoints. After you create a gateway
endpoint, you can add it as a target in your route table for traffic destined from your VPC
to your bucket. There is no additional charge for using gateway endpoints. For more
information about how to configure gateway VPC endpoints, see [Networking for directory buckets](s3-express-networking.md "s3-express-networking.md").

Bucket-level (control plane) API operations are
available through a Regional endpoint and are referred to as Regional endpoint API
operations. Examples of Regional endpoint API operations are `CreateBucket` and
`DeleteBucket`.

You use Zonal (object level, or data plane
endpoint API operations) to upload and manage your objects. Zonal
endpoint API operations are available through a Zonal endpoint. Examples of Zonal API
operations are `PutObject` and `CopyObject`.

For more information about Regional and Zonal endpoints for directory buckets in Availability Zones, see [Regional and Zonal endpoints for directory buckets in an Availability Zone](endpoint-directory-buckets-AZ.md "endpoint-directory-buckets-AZ.md").

For more information about Regional and Zonal endpoints for directory buckets in Local Zones, see [Concepts for directory buckets in
Local Zones](s3-lzs-for-directory-buckets.md "s3-lzs-for-directory-buckets.md").

| Region name           | Region           | Availability Zone IDs            | Regional endpoint                                | Zonal endpoint                                                                                                                            |
| --------------------- | ---------------- | -------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| US East (N. Virginia) | `us-east-1`      | `use1-az4` `use1-az5` `use1-az6` | `s3express-control.us-east-1.amazonaws.com`      | `s3express-use1-az4.us-east-1.amazonaws.com` `s3express-use1-az5.us-east-1.amazonaws.com` `s3express-use1-az6.us-east-1.amazonaws.com`    |
| US East (Ohio)        | `us-east-2`      | `use2-az1` `use2-az2`            | `s3express-control.us-east-2.amazonaws.com`      | `s3express-use2-az1.us-east-2.amazonaws.com` `s3express-use2-az2.us-east-2.amazonaws.com`                                                 |
| US West (Oregon)      | `us-west-2`      | `usw2-az1` `usw2-az3` `usw2-az4` | `s3express-control.us-west-2.amazonaws.com`      | `s3express-usw2-az1.us-west-2.amazonaws.com` `s3express-usw2-az3.us-west-2.amazonaws.com` `s3express-usw2-az4.us-west-2.amazonaws.com`    |
| Asia Pacific (Mumbai) | `ap-south-1`     | `aps1-az1` `aps1-az3`            | `s3express-control.ap-south-1.amazonaws.com`     | `s3express-aps1-az1.ap-south-1.amazonaws.com` `s3express-aps1-az3.ap-south-1.amazonaws.com`                                               |
| Asia Pacific (Tokyo)  | `ap-northeast-1` | `apne1-az1` `apne1-az4`          | `s3express-control.ap-northeast-1.amazonaws.com` | `s3express-apne1-az1.ap-northeast-1.amazonaws.com` `s3express-apne1-az4.ap-northeast-1.amazonaws.com`                                     |
| Europe (Ireland)      | `eu-west-1`      | `euw1-az1` `euw1-az3`            | `s3express-control.eu-west-1.amazonaws.com`      | `s3express-euw1-az1.eu-west-1.amazonaws.com` `s3express-euw1-az3.eu-west-1.amazonaws.com`                                                 |
| Europe (Stockholm)    | `eu-north-1`     | `eun1-az1` `eun1-az2` `eun1-az3` | `s3express-control.eu-north-1.amazonaws.com`     | `s3express-eun1-az1.eu-north-1.amazonaws.com` `s3express-eun1-az2.eu-north-1.amazonaws.com` `s3express-eun1-az3.eu-north-1.amazonaws.com` |
