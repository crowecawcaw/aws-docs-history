

# Metrics and dimensions for directory buckets
<a name="metrics-dimensions-directory-buckets"></a>

The metrics and dimensions that S3 Express One Zone send to Amazon CloudWatch are listed in the following tables.

**Best-effort CloudWatch metrics delivery**  
 CloudWatch metrics are delivered on a best-effort basis. Most requests for an Amazon S3 object that have request metrics result in a data point being sent to CloudWatch.

The completeness and timeliness of metrics are not guaranteed. The data point for a particular request might be returned with a timestamp that is later than when the request was actually processed. The data point for a minute might be delayed before being available through CloudWatch, or it might not be delivered at all. CloudWatch request metrics give you an idea of the nature of traffic against your bucket in near-real time. It is not meant to be a complete accounting of all requests.

It follows from the best-effort nature of this feature that the reports available at the [Billing & Cost Management Dashboard](https://console.aws.amazon.com/billing/home?#/) might include one or more access requests that do not appear in the bucket metrics.

**Topics**
+ [Amazon S3 daily storage metrics for directory buckets in CloudWatch](#s3-cloudwatch-metrics-directory-buckets)
+ [Amazon S3 request metrics for directory buckets in CloudWatch](#s3-cloudwatch-request-metrics-directory-buckets)
+ [Amazon S3 dimensions for directory buckets](#s3-cloudwatch-dimensions-directory-buckets)

## Amazon S3 daily storage metrics for directory buckets in CloudWatch
<a name="s3-cloudwatch-metrics-directory-buckets"></a>

The `AWS/S3` namespace includes the following daily storage metrics for directory buckets.


| Metric | Description | 
| --- | --- | 
| BucketSizeBytes | The amount of data in bytes that is stored in a directory bucket. This value is calculated by summing the size of all objects and metadata (such as bucket names) in the bucket, including the size of all parts for all incomplete multipart uploads to the bucket.<br />Units: Bytes<br />Valid statistics: Average | 
| NumberOfObjects | The total number of objects stored in a directory bucket. This value is calculated by counting all objects in the bucket and doesn't include incomplete multipart uploads to the bucket.<br />Units: Count<br />Valid statistics: Average | 

## Amazon S3 request metrics for directory buckets in CloudWatch
<a name="s3-cloudwatch-request-metrics-directory-buckets"></a>

The `AWS/S3` namespace includes the following request metrics for directory buckets.


| Metric | Description | 
| --- | --- | 
| AllRequests | The total number of HTTP requests made to a directory bucket, regardless of type. If you're using a metrics configuration with a filter, then this metric returns only the HTTP requests that meet the filter's requirements.<br />Units: Count<br />Valid statistics: Sum | 
| GetRequests | The number of HTTP `GET` requests made for objects in a directory bucket. This doesn't include list operations. This metric is incremented for the source of each `CopyObject` request.<br />Units: Count<br />Valid statistics: Sum Paginated list-oriented requests, such as [ListMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadListMPUpload.html), [ListParts](https://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadListParts.html), and others, are not included in this metric.  | 
| PutRequests | The number of HTTP `PUT` requests made for objects in a directory bucket. This metric is incremented for the destination of each `CopyObject` request.<br />Units: Count<br />Valid statistics: Sum | 
| DeleteRequests | The number of HTTP `DELETE` requests made for objects in a directory bucket. This metric also includes [DeleteObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/multiobjectdeleteapi.html) requests. This metric shows the number of requests made, not the number of objects deleted.<br />Units: Count<br />Valid statistics: Sum | 
| HeadRequests | The number of HTTP `HEAD` requests made to a directory bucket.<br />Units: Count<br />Valid statistics: Sum | 
| PostRequests | The number of HTTP `POST` requests made to a directory bucket.<br />Units: Count<br />Valid statistics: Sum [DeleteObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/multiobjectdeleteapi.html) requests are not included in this metric.   | 
| ListRequests | The number of HTTP requests that list the contents of a directory bucket.<br />Units: Count<br />Valid statistics: Sum | 
| BytesDownloaded | The number of bytes downloaded for requests made to a directory bucket, where the response includes a body.<br />Units: Bytes<br />Valid statistics: Average (bytes per request), Sum (bytes per period), Sample Count, Min, Max (same as p100), any percentile between p0.0 and p99.9 | 
| BytesUploaded | The number of bytes uploaded for requests made to a directory bucket, where the request includes a body.<br />Units: Bytes<br />Valid statistics: Average (bytes per request), Sum (bytes per period), Sample Count, Min, Max (same as p100), any percentile between p0.0 and p99.9 | 
| 4xxErrors | The number of HTTP 4*xx* client error status code requests made to a directory bucket with a value of either 0 or 1. The Average statistic shows the error rate, and the Sum statistic shows the count of that type of error, during each period.<br />Units: Count<br />Valid statistics: Average (reports per request), Sum (reports per period), Min, Max, Sample Count | 
| 5xxErrors | The number of HTTP 5*xx* server error status code requests made to a directory bucket with a value of either 0 or 1. The Average statistic shows the error rate, and the Sum statistic shows the count of that type of error, during each period.<br />Units: Count<br />Valid statistics: Average (reports per request), Sum (reports per period), Min, Max, Sample Count | 
| FirstByteLatency | The per-request time from the complete request being received by a directory bucket to when the response starts to be returned.<br />Units: Milliseconds<br />Valid statistics: Average, Sum, Min, Max (same as p100), Sample Count, any percentile between p0.0 and p100 | 
| TotalRequestLatency | The elapsed per-request time from the first byte received to the last byte sent to a directory bucket. This metric includes the time taken to receive the request body and send the response body, which is not included in `FirstByteLatency`.<br />Units: Milliseconds<br />Valid statistics: Average, Sum, Min, Max (same as p100), Sample Count, any percentile between p0.0 and p100 | 

## Amazon S3 dimensions for directory buckets
<a name="s3-cloudwatch-dimensions-directory-buckets"></a>

The following dimensions are used to filter Amazon S3 metrics for directory buckets.


| Dimension | Description | 
| --- | --- | 
| BucketName | This dimension filters the data that you request for the identified directory bucket only. | 
| FilterId | This dimension filters metrics configurations that you specify for request metrics on a directory bucket. You set up the metrics configuration filter when you configure request metrics. For more information, see [Configuring request metrics for directory buckets](metrics-configurations-directory-buckets.md). | 