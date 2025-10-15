# Getting Amazon S3 request IDs for AWS Support

Whenever you contact AWS Support because you've encountered errors or unexpected behavior in
 Amazon S3, you must provide the request IDs associated with the failed action. AWS Support uses
 these request IDs to help resolve the problems that you're experiencing. 

Request IDs come in pairs, are returned in every response that Amazon S3 processes (even the
 erroneous ones), and can be accessed through verbose logs. There are a number of common
 methods for getting your request IDs, including S3 server access logs and AWS CloudTrail events or data
 events.

After you've recovered these logs, copy and retain those two values, because you'll need
 them when you contact AWS Support. For information about contacting AWS Support, see [Contact AWS](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") or the [AWS Support Documentation](https://aws.amazon.com/documentation/aws-support/ "https://aws.amazon.com/documentation/aws-support/").

###### Topics

* [Using the AWS CLI to obtain request IDs](#cli-request-id "#cli-request-id")
* [Using Windows PowerShell to obtain request IDs](#powershell-request-id "#powershell-request-id")
* [Using AWS CloudTrail data events to obtain request IDs](#cloudtrail-request-id "#cloudtrail-request-id")
* [Using S3 server access logging to obtain request IDs](#server-access-log-request-id "#server-access-log-request-id")
* [Using HTTP to obtain request IDs](#http-request-id "#http-request-id")
* [Using a web browser to obtain request IDs](#browser-request-id "#browser-request-id")
* [Using the AWS SDKs to obtain request IDs](#sdk-request-ids "#sdk-request-ids")

## Using the AWS CLI to obtain request IDs


To get your request IDs when using the AWS Command Line Interface (AWS CLI), add `--debug` to
 your command. For example you should see `x-amz-request-id` and `x-amz-id-2` in the debug log as shown below:



```
...
2025-04-30 14:35:28,572 - MainThread - botocore.parsers - DEBUG - Response headers: {'x-amz-id-2': 'a+zm50vDJH3LLmCiXvwEo0u0PtPS/qCJaBvB2ZMH9dzyzTiJhiLZkBFFoRfsPfOKztUKT/garCI=', 'x-amz-request-id': 'N4NMN0MJ4VDFZMX9', 'Date': 'Wed, 30 Apr 2025 21:35:29 GMT', 'Content-Type': 'application/xml', 'Transfer-Encoding': 'chunked', 'Server': 'AmazonS3'}
...
```

## Using Windows PowerShell to obtain request IDs


For information on recovering logs with Windows PowerShell, see the [Response Logging in AWS Tools for Windows PowerShell](https://aws.amazon.com/blogs/developer/response-logging-in-aws-tools-for-windows-powershell/ "https://aws.amazon.com/blogs/developer/response-logging-in-aws-tools-for-windows-powershell/") in the *AWS Developer Tools Blog*.


## Using AWS CloudTrail data events to obtain request IDs


An Amazon S3 bucket that is configured with CloudTrail data events to log S3 object-level API
 operations provides detailed information about actions that are taken by a user,
 role, or an AWS service in Amazon S3. You can identify
 S3 request IDs by querying CloudTrail events with Athena.


For more information, see [Identifying Amazon S3 requests using CloudTrail](../userguide/cloudtrail-request-identification.md "../userguide/cloudtrail-request-identification.md") in the *Amazon Simple Storage Service User Guide*.


## Using S3 server access logging to obtain request IDs


An Amazon S3 bucket configured for S3 server access logging provides detailed records for
 each request that is made to the bucket. You can identify S3 request IDs by querying the server access logs using Athena.


For more information, see [Querying access logs for requests by using Amazon Athena](../userguide/using-s3-access-logs-to-identify-requests.md#querying-s3-access-logs-for-requests "../userguide/using-s3-access-logs-to-identify-requests.md#querying-s3-access-logs-for-requests") in the *Amazon Simple Storage Service User Guide*.


## Using HTTP to obtain request IDs


You can obtain your request IDs, `x-amz-request-id` and
 `x-amz-id-2` by logging the bits of an HTTP request before it reaches the
 target application. There are a variety of third-party tools that can be used to recover
 verbose logs for HTTP requests. Choose one that you trust, and then run the tool to listen on the
 port that your Amazon S3 traffic travels on, as you send out another Amazon S3 HTTP
 request.


For HTTP requests, the pair of request IDs will look like the following:



```
x-amz-request-id: 79104EXAMPLEB723 
x-amz-id-2: IOWQ4fDEXAMPLEQM+ey7N9WgVhSnQ6JEXAMPLEZb7hSQDASK+Jd1vEXAMPLEa3Km

```

###### Note

HTTPS requests are encrypted and hidden in most packet captures.


## Using a web browser to obtain request IDs


Most web browsers have developer tools that you can use to view request
 headers.


For web browser-based requests that return an error, the pair of requests IDs will
 look like the following examples.



```
<Error><Code>AccessDenied</Code><Message>Access Denied</Message>
<RequestId>79104EXAMPLEB723</RequestId><HostId>IOWQ4fDEXAMPLEQM+ey7N9WgVhSnQ6JEXAMPLEZb7hSQDASK+Jd1vEXAMPLEa3Km</HostId></Error>
```

To obtain the request ID pair from successful requests, use your browser's developer
 tools to look at the HTTP response headers.


## Using the AWS SDKs to obtain request IDs


The following sections include information for configuring logging by using different AWS
 SDKs.


###### Note

Although you can enable verbose logging on every request and response, we don't
 recommend enabling logging in production systems, because large requests or responses
 can significantly slow down an application.


For AWS SDK requests, the pair of request IDs will look like the following:



```
Status Code: 403, AWS Service: Amazon S3, AWS Request ID: 79104EXAMPLEB723  
AWS Error Code: AccessDenied  AWS Error Message: Access Denied  
S3 Extended Request ID: IOWQ4fDEXAMPLEQM+ey7N9WgVhSnQ6JEXAMPLEZb7hSQDASK+Jd1vEXAMPLEa3Km
```


C++
The type of logger and the verbosity are specified during the SDK
 initialization in the `SDKOptions` argument. The following
 example specifies the verbosity level as `LogLevel::Debug`.


The default logger will write to the filesystem and the file is named
 using the following convention `aws_sdk_YYYY-MM-DD-HH.log`. The
 logger creates a new file on the hour.



```
Aws::SDKOptions options;
options.loggingOptions.logLevel = Aws::Utils::Logging::LogLevel::Debug;
Aws::InitAPI(options);
// ...
Aws::ShutdownAPI(options);
```

For more information, see [How do I turn on logging?](https://github.com/aws/aws-sdk-cpp/wiki#how-do-i-turn-on-logging "https://github.com/aws/aws-sdk-cpp/wiki#how-do-i-turn-on-logging") in the *AWS SDK for C++ wiki on
 GitHub*.



Go
You can configure logging by using SDK for Go. For more information, see [Logging](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-logging.html "https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-logging.html") in the
 *AWS SDK for Go v2 Developer Guide*.



Java
You can enable logging for specific requests or responses to catch and
 return only relevant headers. To do this, import the
 `com.amazonaws.services.s3.S3ResponseMetadata` class.
 Afterward, you can store the request in a variable before performing the
 actual request. To get the logged request or response, call
 `getCachedResponseMetadata(AmazonWebServiceRequest
 request).getRequestID()`.



```
PutObjectRequest req = new PutObjectRequest(bucketName, key, createSampleFile());
s3.putObject(req);
S3ResponseMetadata md = s3.getCachedResponseMetadata(req);
System.out.println("Host ID: " + md.getHostId() + " RequestID: " + md.getRequestId());
```

Alternatively, you can use verbose logging of every Java request and response. For
 more information, see [Verbose Wire Logging](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-logging.html#sdk-net-logging-verbose "https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/java-dg-logging.html#sdk-net-logging-verbose") in the
 *AWS SDK for Java Developer Guide*.



JavaScript
The AWS SDK for JavaScript has a built-in logger so you can log API calls you make with it. To
 turn on the logger and print log entries in the console, add the following
 statement to your code:



```
AWS.config.logger = console;
```

For more information, see [Logging AWS SDK for JavaScript Calls](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/logging-sdk-calls.html "https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/logging-sdk-calls.html") in the
 *AWS SDK for JavaScript Developer Guide*.



Kotlin
With the AWS SDK for Kotlin, you can specify log mode for wire-level messages
 using code or environment settings. You can set log mode for HTTP requests and HTTP responses.


To opt into additional logging, set the `logMode` property when you construct a service client:



```
import aws.smithy.kotlin.runtime.client.LogMode

// ...

val client = S3Client {
    // ...
    logMode = LogMode.LogRequestWithBody + LogMode.LogResponse
}
```

Alternatively, you can set log mode using an environment variable:



```
export SDK_LOG_MODE=LogRequestWithBody|LogResponse
```

For more information, see [Logging](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/logging.html "https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/logging.html") in the
 *AWS SDK for Kotlin Developer Guide*.



.NET
You can configure logging with the SDK for .NET by using the built-in
 `System.Diagnostics` logging tool. For more information, see the
 [Logging with the SDK for .NET](https://aws.amazon.com/blogs/developer/logging-with-the-aws-sdk-for-net/ "https://aws.amazon.com/blogs/developer/logging-with-the-aws-sdk-for-net/")
*AWS Developer Blog* post.


###### Note

By default, the returned log contains only error information. To get the
 request IDs, the config file must have `AWSLogMetrics` (and
 optionally, `AWSResponseLogging`) added.



PHP
You can get debug information, including the data sent over the wire,
 by setting the debug option to `true` in a client constructor.



```
$s3Client = new Aws\S3\S3Client([
    'region'  => 'us-standard',
    'version' => '2006-03-01',
    'debug'   => true
]);
```

For more information, see [How can I see what data is sent over the wire?](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/faq.html#how-can-i-see-what-data-is-sent-over-the-wire "https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/faq.html#how-can-i-see-what-data-is-sent-over-the-wire") in the
 *AWS SDK for PHP Developer Guide*.



Python (Boto3)
With the AWS SDK for Python (Boto3), you can log specific responses. You can use this feature
 to capture only the relevant headers. The following code shows how to log parts of
 the response to a file:



```
import logging
import boto3
logging.basicConfig(filename='logfile.txt', level=logging.INFO)
logger = logging.getLogger(__name__)
s3 = boto3.resource('s3')
response = s3.Bucket(bucket_name).Object(object_key).put()
logger.info("HTTPStatusCode: %s", response['ResponseMetadata']['HTTPStatusCode'])
logger.info("RequestId: %s", response['ResponseMetadata']['RequestId'])
logger.info("HostId: %s", response['ResponseMetadata']['HostId'])
logger.info("Date: %s", response['ResponseMetadata']['HTTPHeaders']['date'])
```

You can also catch exceptions and log relevant information when an exception is
 raised. For more information, see [Discerning useful information from error responses](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/error-handling.html#discerning-useful-information-from-error-responses "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/error-handling.html#discerning-useful-information-from-error-responses") in the *AWS SDK for Python (Boto) API Reference*.


Additionally, you can configure Boto3 to output verbose debugging logs by using
 the following code:



```
import logging
import boto3
boto3.set_stream_logger('', logging.DEBUG)
```

For more information, see [set\_stream\_logger](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/boto3.html#boto3.set_stream_logger "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/boto3.html#boto3.set_stream_logger") in the *AWS SDK for Python (Boto) API Reference*.



Ruby
You can get your request IDs using the SDK for Ruby Version 3. You can enable
 HTTP wire logging in your client using the following code:



```
s3 = Aws::S3::Client.new(http_wire_trace: true)
```

###### Note

Wire logging can include sensitive information, such as your access key ID. Sensitive information should be sanitized before sharing it with AWS Support.


You can also find the request ID of the request context object in the request response or error:



```
# Finding the request ID from an error:
begin
  s3.put_object(bucket: 'bucket', key: 'key', body: 'test')
rescue Aws::S3::Errors::ServiceError => e
  puts e.context[:request_id]
  puts e.context[:s3_host_id]
end

# Finding the request ID from a successful call:
resp = s3.put_object(bucket: 'bucket', key: 'key', body: 'test')
puts resp.context[:request_id]
puts resp.context[:s3_host_id]
```

For more information, see [Debugging using
 wire trace information from an AWS SDK for Ruby client](https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/debugging.html "https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/debugging.html") in the
 *AWS SDK for Ruby Developer Guide*.



Rust
To enable logging, add the `tracing-subscriber` crate and initialize it in your Rust application.


Add the tracing library to your `Cargo.toml` file:



```
tracing-subscriber = { version = "0.3", features = ["env-filter"] }
```

Then, in your Rust code, initialize the logger in the main function before you call any SDK operation:



```
tracing_subscriber::fmt::init();
```

For more information, see [Configuring and using logging
 in the AWS SDK for Rust](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/logging.html "https://docs.aws.amazon.com/sdk-for-rust/latest/dg/logging.html") in the *AWS SDK for Rust Developer
 Guide*.
