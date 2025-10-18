# Interpret your AWS bill and usage
 reports for CloudFront

Once you have the [billing report](reports-billing.md#billing-report "reports-billing.md#billing-report") and the [usage report](reports-billing.md#usage-report "reports-billing.md#usage-report"), you can use this topic to understand how
 to interpret each CloudFront charge that appears on your bill and the corresponding usage type
 for each charge. This topic includes the codes and AWS Region abbreviations that can
 appear on both reports.

Most codes in both columns include a two-letter abbreviation that indicates the
 location of the activity. In the following table, `region` in a
 code is replaced in your AWS bill and in the usage report by one of the following
 two-letter abbreviations:


* **AP:** Hong Kong, Philippines, South Korea,
 Taiwan, and Singapore (Asia
 Pacific)
* **AU:** Australia
* **CA:** Canada
* **EU:** Europe and Israel
* **IN:** India
* **JP:** Japan
* **ME:** Middle East
* **SA:** South America
* **US:** United States
* **ZA:** South Africa
For more information about pricing by AWS Region, see [Amazon CloudFront pricing](https://aws.amazon.com/cloudfront/pricing/ "https://aws.amazon.com/cloudfront/pricing/").

###### Notes


* This table doesn't include charges for transferring your objects from an
 Amazon S3 bucket to CloudFront edge locations. These charges, if any, appear in the
 **AWS Data Transfer** portion of your AWS
 bill.
* The first column lists charges that appear in your AWS bill report and
 explains what each means.
* The second column lists items that appear in the AWS usage report and
 shows the correlation between bill charges and usage report items.


| CloudFront charges in your AWS bill | Values in the UsageType column in the AWS usage report |
| --- | --- |
| `region`**-DataTransfer-Out-Bytes** Total bytes served from CloudFront edge locations in `region` in response to user `GET` and `HEAD` requests. | `region`**-Out-Bytes-HTTP-Static:** Bytes served via HTTP for objects with TTL ≥ 3,600 seconds. `region`**-Out-Bytes-HTTPS-Static:** Bytes served via HTTPS for objects with TTL ≥ 3,600 seconds. `region`**-Out-Bytes-HTTP-Dynamic:** Bytes served via HTTP for objects with TTL < 3,600 seconds. `region`**-Out-Bytes-HTTPS-Dynamic:** Bytes served via HTTPS for objects with TTL < 3,600 seconds. `region`**-Out-Bytes-HTTP-Proxy:** Bytes returned from CloudFront to viewers via HTTP in response to `DELETE`, `OPTIONS`, `PATCH`, `POST`, and `PUT` requests. `region`**-Out-Bytes-HTTPS-Proxy:** Bytes returned from CloudFront to viewers via HTTPS in response to `DELETE`, `OPTIONS`, `PATCH`, `POST`, and `PUT` requests. This includes bytes returned from CloudFront to viewers via gRPC. |
| `region`**-DataTransfer-Out-OBytes** Total bytes transferred from CloudFront edge locations to your origin or [edge function](edge-functions.md "edge-functions.md") in response to `DELETE`, `OPTIONS`, `PATCH`, `POST`, and `PUT` requests. The charges include data transfer for WebSocket data from client to server. | `region`**-Out-OBytes-HTTP-Proxy** Total bytes transferred via HTTP from CloudFront edge locations to your origin or [edge function](edge-functions.md "edge-functions.md") in response to `DELETE`, `OPTIONS`, `PATCH`, `POST`, and `PUT` requests. `region`**-Out-OBytes-HTTPS-Proxy** Total bytes transferred via HTTPS from CloudFront edge locations to your origin or [edge function](edge-functions.md "edge-functions.md") in response to `DELETE`, `OPTIONS`, `PATCH`, `POST`, and `PUT` requests. This includes bytes transferred via gRPC from CloudFront edge locations to your origin or CloudFront Functions. |
| `region`**-Requests-Tier1** Number of HTTP `GET` and `HEAD` requests. | `region`**-Requests-HTTP-Static** Number of HTTP `GET` and `HEAD` requests served for objects with TTL ≥ 3,600 seconds. `region`**-Requests-HTTP-Dynamic** Number of HTTP `GET` and `HEAD` requests served for objects with TTL < 3,600 seconds. |
| `region`**-Requests-Tier2-HTTPS** Number of HTTPS `GET` and `HEAD` requests. | `region`**-Requests-HTTPS-Static** Number of HTTPS `GET` and `HEAD` requests served for objects with TTL ≥ 3,600 seconds. `region`**-Requests-HTTPS-Dynamic** Number of HTTPS `GET` and `HEAD` requests served for objects with TTL < 3,600 seconds. |
| `region`**-Requests-HTTP-Proxy** Number of HTTP `DELETE`, `OPTIONS`, `PATCH`, `POST`, and `PUT` requests that CloudFront forwards to your origin or [edge function](edge-functions.md "edge-functions.md"). Also includes the number of HTTP [WebSocket](distribution-working-with.md "distribution-working-with.md") requests (`GET` requests with the `Upgrade: websocket` header) that CloudFront forwards to your origin or edge function. | `region`**-Requests-HTTP-Proxy** Same as the corresponding item in your CloudFront bill. |
| `region`**-Requests-HTTPS-Proxy** Number of HTTPS `DELETE`, `OPTIONS`, `PATCH`, `POST`, and `PUT` requests that CloudFront forwards to your origin or [edge function](edge-functions.md "edge-functions.md"). Also includes the following request types: <br>• The number of HTTPS [WebSocket](distribution-working-with.md "distribution-working-with.md") requests (`GET` requests with the `Upgrade: websocket` header) that CloudFront forwards to your origin or edge function. <br>• The number of HTTPS gRPC requests. | `region`**-Requests-HTTPS-Proxy** Same as the corresponding item in your CloudFront bill. |
| `region`**-Requests-HTTPS-Proxy-FLE** Number of HTTPS `DELETE`, `OPTIONS`, `PATCH`, and `POST` requests processed with [field-level encryption](field-level-encryption.md "field-level-encryption.md") that CloudFront forwards to your origin or [edge function](edge-functions.md "edge-functions.md"). | `region`**-Requests-HTTPS-Proxy-FLE** Same as the corresponding item in your CloudFront bill. |
| `region`**-Bytes-OriginShield** Total bytes transferred from the origin to any [regional edge cache](HowCloudFrontWorks.md#CloudFrontRegionaledgecaches "HowCloudFrontWorks.md#CloudFrontRegionaledgecaches"), including the regional edge cache that is enabled as [Origin Shield](origin-shield.md "origin-shield.md"). | `region`**-Bytes-OriginShield** Same as the corresponding item in your CloudFront bill. |
| `region`**-OBytes-OriginShield** Total bytes transferred to the origin from any [regional edge cache](HowCloudFrontWorks.md#CloudFrontRegionaledgecaches "HowCloudFrontWorks.md#CloudFrontRegionaledgecaches"), including the regional edge cache that is enabled as [Origin Shield](origin-shield.md "origin-shield.md"). | `region`**-OBytes-OriginShield** Same as the corresponding item in your CloudFront bill. |
| `region`**-Requests-OriginShield** Number of requests that go to [Origin Shield](origin-shield.md "origin-shield.md") as an incremental layer. For dynamic (non-cacheable) requests that are proxied to the origin, Origin Shield is always an incremental layer. For cacheable requests, Origin Shield is sometimes an incremental layer. For more information, see [Estimate Origin Shield costs](origin-shield.md#origin-shield-costs "origin-shield.md#origin-shield-costs"). | `region`**-Requests-OriginShield** Same as the corresponding item in your CloudFront bill. |
| **Invalidations** The charge for invalidating objects (removing the objects from CloudFront edge locations). For more information, see [Pay for file invalidation](PayingForInvalidation.md "PayingForInvalidation.md"). | **Invalidations** Same as the corresponding item in your CloudFront bill. |
| **SSL-Cert-Custom** The charge for using an SSL certificate with a CloudFront alternate domain name such as example.com instead of using the default CloudFront SSL certificate and the domain name that CloudFront assigned to your distribution. | **SSL-Cert-Custom** Same as the corresponding item in your CloudFront bill. |
| **RealTimeLog-KinesisDataStream** The charge for the number of lines generated for [real-time logs](real-time-logs.md "real-time-logs.md"). | **RealTimeLog-KinesisDataStream** Same as the corresponding item in your CloudFront bill. |
| **Executions-CloudFrontFunctions** The charge for the number of [CloudFront Functions](cloudfront-functions.md "cloudfront-functions.md") invocations. | **Executions-CloudFrontFunctions** Same as the corresponding item in your CloudFront bill. |
| **`region`-Lambda-Edge-Request** The charge for the number of [Lambda@Edge](lambda-at-the-edge.md "lambda-at-the-edge.md") function invocations. | **`region`-Lambda-Edge-Request** Same as the corresponding item in your CloudFront bill. |
| **`region`-Lambda-Edge-GB-Second** The charge for the duration from when your [Lambda@Edge](lambda-at-the-edge.md "lambda-at-the-edge.md") function is invoked to when it returns or terminates. | **`region`-Lambda-Edge-GB-Second** Same as the corresponding item in your CloudFront bill. |
| **KeyValueStore-EdgeReads** The charge for the number of read calls to the [CloudFront KeyValueStore](kvs-with-functions.md "kvs-with-functions.md") methods, `get()`, `exists()`, and `meta()`. For more information, see [Helper methods for key value stores](functions-custom-methods.md "functions-custom-methods.md"). | **KeyValueStore-EdgeReads** Same as the corresponding item in your CloudFront bill. |
| **KeyValueStore-APIOperations** The charge for the number of calls to the [CloudFront KeyValueStore](kvs-with-functions.md "kvs-with-functions.md") API. | **KeyValueStore-APIOperations** Same as the corresponding item in your CloudFront bill. |
