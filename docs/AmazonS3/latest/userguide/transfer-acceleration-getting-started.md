# Getting started with

Amazon S3 Transfer Acceleration

You can use Amazon S3 Transfer Acceleration for fast, easy, and secure transfers of files over long
distances between your client and an S3 bucket. Transfer Acceleration uses the globally distributed
edge locations in Amazon CloudFront. As the data arrives at an edge location, data is routed to Amazon S3
over an optimized network path.

To get started using Amazon S3 Transfer Acceleration, perform the following steps:

1. **Enable Transfer Acceleration on a bucket**

You can enable Transfer Acceleration on a bucket any of the following ways:

    * Use the Amazon S3 console.
    * Use the REST API [PutBucketAccelerateConfiguration](../API/RESTBucketPUTaccelerate.md "../API/RESTBucketPUTaccelerate.md") operation.
    * Use the AWS CLI and AWS SDKs. For more information, see [Developing with Amazon S3 using the AWS SDKs](../API/sdk-general-information-section.md "../API/sdk-general-information-section.md") in the *Amazon S3 API Reference*.

For more information, see [Enabling and using S3 Transfer Acceleration](transfer-acceleration-examples.md "transfer-acceleration-examples.md").

###### Note

For your bucket to work with transfer acceleration, the bucket name must conform to
DNS naming requirements and must not contain periods (`.`). 2. **Transfer data to and from the acceleration-enabled
bucket**

Use one of the following `s3-accelerate` endpoint domain names:

    * To access an acceleration-enabled bucket, use
     ``bucket-name`.s3-accelerate.amazonaws.com`.
    * To access an acceleration-enabled bucket over IPv6, use
     ``bucket-name`.s3-accelerate.dualstack.amazonaws.com`.


    Amazon S3 dual-stack endpoints support requests to S3 buckets over IPv6 and IPv4. The
     Transfer Acceleration dual-stack endpoint only uses the virtual hosted-style type of
     endpoint name. For more information, see [Making requests to Amazon S3 over IPv6](../API/ipv6-access.md "../API/ipv6-access.md")  in the *Amazon S3 API Reference* and [Using Amazon S3
     dual-stack endpoints](../API/dual-stack-endpoints.md "../API/dual-stack-endpoints.md")  in the *Amazon S3 API Reference*.

###### Note

Your data transfer application must use one of the following two types of endpoints to access the bucket for faster data transfer: `.s3-accelerate.amazonaws.com` or `.s3-accelerate.dualstack.amazonaws.com` for the dual-stack endpoint. If you want to use standard data transfer, you can continue to use the regular endpoints.

You can point your Amazon S3 `PUT` object and `GET` object requests
to the `s3-accelerate` endpoint domain name after you enable Transfer Acceleration.
For example, suppose that you currently have a REST API application using [PutObject](../API/RESTObjectPUT.md "../API/RESTObjectPUT.md") that uses the
hostname ``amzn-s3-demo-bucket`.s3.us-east-1.amazonaws.com` in the
 `PUT` request. To accelerate the `PUT`, you change the hostname in
 your request to ``amzn-s3-demo-bucket`.s3-accelerate.amazonaws.com`. To go back
to using the standard upload speed, change the name back to
``amzn-s3-demo-bucket`.s3.us-east-1.amazonaws.com`.

After Transfer Acceleration is enabled, it can take up to 20 minutes for you to realize the
performance benefit. However, the accelerate endpoint is available as soon as you enable
Transfer Acceleration.

You can use the accelerate endpoint in the AWS CLI, AWS SDKs, and other tools that
transfer data to and from Amazon S3. If you are using the AWS SDKs, some of the supported
languages use an accelerate endpoint client configuration flag so you don't need to
explicitly set the endpoint for Transfer Acceleration to
``bucket-name`.s3-accelerate.amazonaws.com`. For
examples of how to use an accelerate endpoint client configuration flag, see [Enabling and using S3 Transfer Acceleration](transfer-acceleration-examples.md "transfer-acceleration-examples.md").
You can use all Amazon S3 operations through the transfer acceleration endpoints _except_ for the following:

- [ListBuckets](../API/RESTServiceGET.md "../API/RESTServiceGET.md")
- [CreateBucket](../API/RESTBucketPUT.md "../API/RESTBucketPUT.md")
- [DeleteBucket](../API/RESTBucketDELETE.md "../API/RESTBucketDELETE.md")
  Also, Amazon S3 Transfer Acceleration does not support cross-Region copies using [CopyObject](../API/RESTObjectCOPY.md "../API/RESTObjectCOPY.md").
