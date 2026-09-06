

# Connection logs for your Application Load Balancer
<a name="load-balancer-connection-logs"></a>

Elastic Load Balancing provides connection logs that capture detailed information about requests sent to your load balancer. Each log contains information such as the client's IP address and port, listener port, the TLS cipher and protocol used, TLS handshake latency, connection status, and client certificate details. You can use these connection logs to analyze request patterns and troubleshoot issues.

Connection logs is an optional feature of Elastic Load Balancing that is disabled by default. After you enable connection logs for your load balancer, Elastic Load Balancing captures the logs and stores them in the Amazon S3 bucket that you specify, as compressed files. You can disable connection logs at any time.

You are charged storage costs for Amazon S3, but not charged for the bandwidth used by Elastic Load Balancing to send log files to Amazon S3. For more information about storage costs, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

**Important**  
While traditional "legacy" logs (described in this section) remain available, Application Load Balancer now offers enhanced logging options through CloudWatch Logs. CloudWatch Logs provide more flexible delivery options, including to Amazon CloudWatch Logs, Amazon Data Firehose, and Amazon Simple Storage Service. To configure these improved logging options, visit your load balancer's **Integrations** tab. For more information on CloudWatch Logs, see [CloudWatch Logs for your Application Load Balancer](load-balancer-cloudwatch-logs.md).

**Topics**
+ [Connection log files](#connection-log-file-format)
+ [Connection log entries](#connection-log-entry-format)
+ [Example log entries](#connection-log-entry-examples)
+ [Processing connection log files](#connection-log-processing-tools)
+ [Enable connection logs](enable-connection-logging.md)
+ [Disable connection logs](disable-connection-logging.md)

## Connection log files
<a name="connection-log-file-format"></a>

Elastic Load Balancing publishes a log file for each load balancer node every 5 minutes. Log delivery is eventually consistent. The load balancer can deliver multiple logs for the same period. This usually happens if the site has high traffic.

The file names of the connection logs use the following format:

```
{{bucket}}[/{{prefix}}]/AWSLogs/{{aws-account-id}}/elasticloadbalancing/{{region}}/{{yyyy}}/{{mm}}/{{dd}}/conn_log_{{aws-account-id}}_elasticloadbalancing_{{region}}_app.{{load-balancer-id}}_{{end-time}}_{{ip-address}}_{{random-string}}.log.gz
```

*bucket*  
The name of the S3 bucket.

*prefix*  
(Optional) The prefix (logical hierarchy) for the bucket. The prefix that you specify must not include the string `AWSLogs`. For more information, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html).

`AWSLogs`  
We add the portion of the file name starting with `AWSLogs` after the bucket name and optional prefix that you specify.

*aws-account-id*  
The AWS account ID of the owner.

*region*  
The Region for your load balancer and S3 bucket.

*yyyy*/*mm*/*dd*  
The date that the log was delivered.

*load-balancer-id*  
The resource ID of the load balancer. If the resource ID contains any forward slashes (/), they are replaced with periods (.).

*end-time*  
The date and time that the logging interval ended. For example, an end time of 20140215T2340Z contains entries for requests made between 23:35 and 23:40 in UTC or Zulu time.

*ip-address*  
The IP address of the load balancer node that handled the request. For an internal load balancer, this is a private IP address.

*random-string*  
A system-generated random string.

The following is an example log file name with a prefix:

```
s3://amzn-s3-demo-logging-bucket/logging-prefix/AWSLogs/123456789012/elasticloadbalancing/us-east-2/2022/05/01/conn_log_123456789012_elasticloadbalancing_us-east-2_app.my-loadbalancer.1234567890abcdef_20220215T2340Z_172.160.001.192_20sg8hgm.log.gz
```

The following is an example log file name without a prefix:

```
s3://amzn-s3-demo-logging-bucket/AWSLogs/123456789012/elasticloadbalancing/us-east-2/2022/05/01/conn_log_123456789012_elasticloadbalancing_us-east-2_app.my-loadbalancer.1234567890abcdef_20220215T2340Z_172.160.001.192_20sg8hgm.log.gz
```

You can store log files in your bucket indefinitely. You can also define Amazon S3 lifecycle rules to archive or delete log files automatically. For more information, see [Object lifecycle management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) in the *Amazon S3 User Guide*.

## Connection log entries
<a name="connection-log-entry-format"></a>

Each connection attempt has an entry in a connection log file. How client requests are sent is determined by the connection being persistent, or nonpersistent. Nonpersistent connections have a single request, which creates a single entry in the access log and connection log. Persistent connections have multiple requests, which creates multiple entries in the access log and a single entry in the connection log.

**Topics**
+ [Syntax](#connection-log-entry-syntax)
+ [Error reason codes](#connection-error-reason-codes)

### Syntax
<a name="connection-log-entry-syntax"></a>

The following table describes the fields of a connection log entry, in order. All fields are delimited by spaces. When we add a new field, we add it to the end of the log entry. As we prepare to release a new field, you might see an additional trailing "-" before the field is released. Ensure that you configure log parsing to stop after the last documented field, and update log parsing after we release a new field.


| Field (position) | Description | 
| --- | --- | 
| timestamp (1) | The time, in ISO 8601 format, when the load balancer successfully established or failed to establish a connection. | 
| client\_ip (2) | The IP address of the requesting client. | 
| client\_port (3) | The port of the requesting client. | 
| listener\_port (4) | The port of the load balancer listener receiving the client request. | 
| tls\_protocol (5) | [HTTPS listener] The SSL/TLS protocol used during handshakes. This field is set to `-` for non SSL/TLS requests. | 
| tls\_cipher (6) | [HTTPS listener] The SSL/TLS protocol used during handshakes. This field is set to `-` for non SSL/TLS requests. | 
| tls\_handshake\_latency (7) | [HTTPS listener] The total time in seconds, with a millisecond precision, elapsed while establishing a successful handshake. This field is set to `-` when:+  The incoming request is not a SSL/TLS request. <br />+  The handshake is not established successfully.  | 
| leaf\_client\_cert\_subject (8) | [HTTPS listener] The subject name of the leaf client certificate. This field is set to `-` when:+  The incoming request is not a SSL/TLS request. <br />+  The load balancer listener is not configured with mTLS enabled. <br />+  The server is not able to load/parse the leaf client certificate.  | 
| leaf\_client\_cert\_validity (9) | [HTTPS listener] The validity, with `not-before` and `not-after` in ISO 8601 format, of the leaf client certificate. This field is set to `-` when:+  The incoming request is not a SSL/TLS request. <br />+  The load balancer listener is not configured with mTLS enabled. <br />+  The server is not able to load/parse the leaf client certificate.  | 
| leaf\_client\_cert\_serial\_number (10) | [HTTPS listener] The serial number of the leaf client certificate. This field is set to `-` when:+  The incoming request is not a SSL/TLS request. <br />+  The load balancer listener is not configured with mTLS enabled. <br />+  The server is not able to load/parse the leaf client certificate.  | 
| tls\_verify\_status (11) | [HTTPS listener] The status of the connection request. This value is `Success` if the connection is established successfully. On an unsuccessful connection the value is `Failed:$error_code`. | 
| conn\_trace\_id (12) | The connection traceability ID is a **unique opaque ID** used to identify each connection. After a connection is established with a client, subsequent requests from this client contain this ID in their respective access log entries. This ID acts as a foreign key to create a link between the connection and access logs. | 
| tls\_keyexchange (13) | [HTTPS listener] The key exchange used during handshakes for TLS or PQ-TLS . This field is set to `-` for non SSL/TLS requests.  | 
| elb (14) | The resource ID of the load balancer. If you are parsing access log entries, note that resources IDs can contain forward slashes (/). | 
| ip\_address (15) | The IP address of the load balancer node that handled the request. For an internal load balancer, this is a private IP address. | 

### Error reason codes
<a name="connection-error-reason-codes"></a>

If the load balancer is unable to establish a connection, the load balancer stores one of the following reason codes in the connection log.


| Code | Description | 
| --- | --- | 
| `ClientCertMaxChainDepthExceeded` | The maximum client certificate chain depth has been exceeded | 
| `ClientCertMaxSizeExceeded` | The maximum client certificate size has been exceeded | 
| `ClientCertCrlHit` | Client certificate has been revoked by the CA | 
| `ClientCertCrlProcessingError` | CRL processing error | 
| `ClientCertUntrusted` | Client certificate is untrusted | 
| `ClientCertNotYetValid` | Client certificate is not yet valid | 
| `ClientCertExpired` | Client certificate is expired | 
| `ClientCertTypeUnsupported` | Client certificate type is unsupported | 
| `ClientCertInvalid` | Client certificate is invalid | 
| `ClientCertPurposeInvalid` | Client certificate purpose is invalid | 
| `ClientCertRejected` | Client certificate is rejected by custom server validation | 
| `UnmappedConnectionError` | Unmapped runtime connection error | 
| `ClientCertIncompatible` | Client certificate is incompatible with the chosen listener security policy | 

## Example log entries
<a name="connection-log-entry-examples"></a>

The following are example connection log entries. Note that the example text appears on multiple lines only to make them easier to read.

The following is an example log entry for a successful connection with a HTTPS listener with mutual TLS verify mode enabled on port 443.

```
2023-10-04T17:05:15.514108Z 203.0.113.1 36280 443 TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 4.036 
"CN=amazondomains.com,O=endEntity,L=Seattle,ST=Washington,C=US" NotBefore=2023-09-21T22:43:21Z;NotAfter=2026-06-17T22:43:21Z 
FEF257372D5C14D4 Success TID_3180a73013c8ca4bac2f731159d4b0fe
```

The following is an example log entry for a failed connection with a HTTPS listener with mutual TLS verify mode enabled on port 443.

```
2023-10-04T17:05:15.514108Z 203.0.113.1 36280 443 TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 - 
"CN=amazondomains.com,O=endEntity,L=Seattle,ST=Washington,C=US" NotBefore=2023-09-21T22:43:21Z;NotAfter=2026-06-17T22:43:21Z 
FEF257372D5C14D4 Failed:ClientCertUntrusted TID_1c71a68d70587445ad5127ff8b2687d7
```

## Processing connection log files
<a name="connection-log-processing-tools"></a>

The connection log files are compressed. If you open the files using the Amazon S3 console, they are uncompressed and the information is displayed. If you download the files, you must uncompress them to view the information.

If there is a lot of demand on your website, your load balancer can generate log files with gigabytes of data. You might not be able to process such a large amount of data using line-by-line processing. Therefore, you might have to use analytical tools that provide parallel processing solutions. For example, you can use the following analytical tools to analyze and process connection logs:
+ Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL.
+ [Loggly](https://documentation.solarwinds.com/en/success_center/loggly/content/admin/s3-ingestion-auto.htm)
+ [Splunk](https://splunk.github.io/splunk-add-on-for-amazon-web-services/)
+ [Sumo logic](https://www.sumologic.com/application/elb/)