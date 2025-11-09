# Regional and Zonal endpoints for directory buckets in an Availability Zone

To access your objects and directory buckets stored in S3 Express One Zone, you
use gateway VPC endpoints. Directory buckets use Regional and Zonal API endpoints.
Depending on the Amazon S3 API operation that you use, either a Regional or Zonal endpoint is
required. There is no additional charge for using gateway endpoints.

Bucket-level (or control plane) API operations are available through Regional
endpoints and are referred to as Regional endpoint API operations. Examples of Regional
endpoint API operations are `CreateBucket` and `DeleteBucket`.

When you create directory buckets that are stored in S3 Express One Zone, you choose the Availability Zone where your bucket will be located.
You can use Zonal endpoint API operations to upload and manage the objects in your directory
bucket.

Object-level (or data plane) API operations are available through Zonal endpoints and
are referred to as Zonal endpoint API operations. Examples of Zonal endpoint API
operations are `CreateSession` and `PutObject`.

| Region name           | Region           | Availability Zone IDs                  | Regional endpoint                                | Zonal endpoint                                                                                                                                  |
| --------------------- | ---------------- | -------------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (N. Virginia) | `us-east-1`      | `use1-az4`<br>`use1-az5`<br>`use1-az6` | `s3express-control.us-east-1.amazonaws.com`      | `s3express-use1-az4.us-east-1.amazonaws.com`<br>`s3express-use1-az5.us-east-1.amazonaws.com`<br>`s3express-use1-az6.us-east-1.amazonaws.com`    |
| US East (Ohio)        | `us-east-2`      | `use2-az1`<br>`use2-az2`               | `s3express-control.us-east-2.amazonaws.com`      | `s3express-use2-az1.us-east-2.amazonaws.com`<br>`s3express-use2-az2.us-east-2.amazonaws.com`                                                    |
| US West (Oregon)      | `us-west-2`      | `usw2-az1`<br>`usw2-az3`<br>`usw2-az4` | `s3express-control.us-west-2.amazonaws.com`      | `s3express-usw2-az1.us-west-2.amazonaws.com`<br>`s3express-usw2-az3.us-west-2.amazonaws.com`<br>`s3express-usw2-az4.us-west-2.amazonaws.com`    |
| Asia Pacific (Mumbai) | `ap-south-1`     | `aps1-az1`<br>`aps1-az3`               | `s3express-control.ap-south-1.amazonaws.com`     | `s3express-aps1-az1.ap-south-1.amazonaws.com`<br>`s3express-aps1-az3.ap-south-1.amazonaws.com`                                                  |
| Asia Pacific (Tokyo)  | `ap-northeast-1` | `apne1-az1`<br>`apne1-az4`             | `s3express-control.ap-northeast-1.amazonaws.com` | `s3express-apne1-az1.ap-northeast-1.amazonaws.com`<br>`s3express-apne1-az4.ap-northeast-1.amazonaws.com`                                        |
| Europe (Ireland)      | `eu-west-1`      | `euw1-az1`<br>`euw1-az3`               | `s3express-control.eu-west-1.amazonaws.com`      | `s3express-euw1-az1.eu-west-1.amazonaws.com`<br>`s3express-euw1-az3.eu-west-1.amazonaws.com`                                                    |
| Europe (Stockholm)    | `eu-north-1`     | `eun1-az1`<br>`eun1-az2`<br>`eun1-az3` | `s3express-control.eu-north-1.amazonaws.com`     | `s3express-eun1-az1.eu-north-1.amazonaws.com`<br>`s3express-eun1-az2.eu-north-1.amazonaws.com`<br>`s3express-eun1-az3.eu-north-1.amazonaws.com` |
