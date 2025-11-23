# Connection logs for your Application Load Balancer

ELB provides connection logs that capture detailed information about requests sent
to your load balancer. Each log contains information such as the client's IP address
and port, listener port, the TLS cipher and protocol used, TLS handshake latency,
connection status, and client certificate details. You can use these connection logs
to analyze request patterns and troubleshoot issues.

Connection logs is an optional feature of ELB that is disabled by default. After you
enable connection logs for your load balancer, ELB captures the logs and stores them in
the Amazon S3 bucket that you specify, as compressed files. You can disable connection logs at any
time.

You are charged storage costs for Amazon S3, but not charged for the bandwidth used by
ELB to send log files to Amazon S3. For more information about storage costs, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

###### Contents

- [Connection log files](#connection-log-file-format "#connection-log-file-format")
- [Connection log entries](#connection-log-entry-format "#connection-log-entry-format")
- [Example log entries](#connection-log-entry-examples "#connection-log-entry-examples")
- [Processing connection log files](#connection-log-processing-tools "#connection-log-processing-tools")
- [Enable connection logs](enable-connection-logging.md "enable-connection-logging.md")
- [Disable connection logs](disable-connection-logging.md "disable-connection-logging.md")

## Connection log files

ELB publishes a log file for each load balancer node every 5 minutes. Log
delivery is eventually consistent. The load balancer can deliver multiple logs for
the same period. This usually happens if the site has high traffic.

The file names of the connection logs use the following format:

```
`bucket`[/`prefix`]/AWSLogs/`aws-account-id`/elasticloadbalancing/`region`/`yyyy`/`mm`/`dd`/conn_log_`aws-account-id`_elasticloadbalancing_`region`_app.`load-balancer-id`_`end-time`_`ip-address`_`random-string`.log.gz
```

_bucket_

The name of the S3 bucket.

_prefix_

(Optional) The prefix (logical hierarchy) for the bucket. The prefix
that you specify must not include the string `AWSLogs`. For
more information, see [Organizing
objects using prefixes](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md").

`AWSLogs`

We add the portion of the file name starting with `AWSLogs` after the
bucket name and optional prefix that you specify.

_aws-account-id_

The AWS account ID of the owner.

_region_

The Region for your load balancer and S3 bucket.

_yyyy_/_mm_/_dd_

The date that the log was delivered.

_load-balancer-id_

The resource ID of the load balancer. If the resource ID contains any
forward slashes (/), they are replaced with periods (.).

_end-time_

The date and time that the logging interval ended. For example, an end
time of 20140215T2340Z contains entries for requests made between 23:35
and 23:40 in UTC or Zulu time.

_ip-address_

The IP address of the load balancer node that handled the request. For
an internal load balancer, this is a private IP address.

_random-string_

A system-generated random string.

The following is an example log file name with a prefix:

```
s3://amzn-s3-demo-logging-bucket/logging-prefix/AWSLogs/123456789012/elasticloadbalancing/us-east-2/2022/05/01/conn_log_123456789012_elasticloadbalancing_us-east-2_app.my-loadbalancer.1234567890abcdef_20220215T2340Z_172.160.001.192_20sg8hgm.log.gz
```

The following is an example log file name without a prefix:

```
s3://amzn-s3-demo-logging-bucket/AWSLogs/123456789012/elasticloadbalancing/us-east-2/2022/05/01/conn_log_123456789012_elasticloadbalancing_us-east-2_app.my-loadbalancer.1234567890abcdef_20220215T2340Z_172.160.001.192_20sg8hgm.log.gz
```

You can store your log files in your bucket for as long as you want, but you can
also define Amazon S3 lifecycle rules to archive or delete log files automatically. For
more information, see [Object
lifecycle management](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") in the _Amazon S3 User Guide_.

## Connection log entries

Each connection attempt has an entry in a connection log file. How client requests
are sent is determined by the connection being persistent, or nonpersistent. Nonpersistent
connections have a single request, which creates a single entry in the access
log and connection log. Persistent connections have multiple requests, which creates multiple
entries in the access log and a single entry in the connection log.

###### Contents

- [Syntax](#connection-log-entry-syntax "#connection-log-entry-syntax")
- [Error reason codes](#connection-error-reason-codes "#connection-error-reason-codes")

### Syntax

The following table describes the fields of a connection log entry, in order. All
fields are delimited by spaces. When we add a new field, we add it to the end of the
log entry. As we prepare to release a new field, you might see an additional trailing
"-" before the field is released. Ensure that you configure log parsing to stop after
the last documented field, and update log parsing after we release a new field.

| Field (position)                    | Description                                                                                                                                                                                                                                                                                                                                               |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| timestamp (1)                       | The time, in ISO 8601 format, when the load balancer successfully established or failed to establish a connection.                                                                                                                                                                                                                                        |
| client_ip (2)                       | The IP address of the requesting client.                                                                                                                                                                                                                                                                                                                  |
| client_port (3)                     | The port of the requesting client.                                                                                                                                                                                                                                                                                                                        |
| listener_port (4)                   | The port of the load balancer listener receiving the client request.                                                                                                                                                                                                                                                                                      |
| tls_protocol (5)                    | [HTTPS listener] The SSL/TLS protocol used during handshakes. This field is set to `-` for non SSL/TLS requests.                                                                                                                                                                                                                                          |
| tls_cipher (6)                      | [HTTPS listener] The SSL/TLS protocol used during handshakes. This field is set to `-` for non SSL/TLS requests.                                                                                                                                                                                                                                          |
| tls_handshake_latency (7)           | [HTTPS listener] The total time in seconds, with a millisecond precision, elapsed while establishing a successful handshake. This field is set to `-` when:<br>• The incoming request is not a SSL/TLS request.<br>• The handshake is not established successfully.                                                                                       |
| leaf_client_cert_subject (8)        | [HTTPS listener] The subject name of the leaf client certificate. This field is<br>set to `-` when:<br>• The incoming request is not a SSL/TLS request.<br>• The load balancer listener is not configured with mTLS enabled.<br>• The server is not able to load/parse the leaf client certificate.                                                       |
| leaf_client_cert_validity (9)       | [HTTPS listener] The validity, with `not-before` and `not-after`<br>in ISO 8601 format, of the leaf client certificate. This field is set to `-`<br>when:<br>• The incoming request is not a SSL/TLS request.<br>• The load balancer listener is not configured with mTLS enabled.<br>• The server is not able to load/parse the leaf client certificate. |
| leaf_client_cert_serial_number (10) | [HTTPS listener] The serial number of the leaf client certificate. This field is<br>set to `-` when:<br>• The incoming request is not a SSL/TLS request.<br>• The load balancer listener is not configured with mTLS enabled.<br>• The server is not able to load/parse the leaf client certificate.                                                      |
| tls_verify_status (11)              | [HTTPS listener] The status of the connection request. This<br>value is `Success` if the connection is<br>established successfully. On an unsuccessful connection the<br>value is `Failed:$error_code`.                                                                                                                                                   |
| conn_trace_id (12)                  | The connection traceability ID is a \*_unique opaque ID_<br>• used<br>to identify each connection. After a connection is established with a client, subsequent requests<br>from this client contain this ID in their respective access log entries. This ID acts as a<br>foreign key to create a link between the connection and access logs.             |
| tls_keyexchange (13)                | [HTTPS listener] The key exchange used during handshakes for TLS or PQ-TLS .<br>This field is set to `-` for non SSL/TLS requests.                                                                                                                                                                                                                        |

### Error reason codes

If the load balancer is unable to establish a connection, the load balancer
stores one of the following reason codes in the connection
log.

| Code                              | Description                                                  |
| --------------------------------- | ------------------------------------------------------------ |
| `ClientCertMaxChainDepthExceeded` | The maximum client certificate chain depth has been exceeded |
| `ClientCertMaxSizeExceeded`       | The maximum client certificate size has been exceeded        |
| `ClientCertCrlHit`                | Client certificate has been revoked by the CA                |
| `ClientCertCrlProcessingError`    | CRL processing error                                         |
| `ClientCertUntrusted`             | Client certificate is untrusted                              |
| `ClientCertNotYetValid`           | Client certificate is not yet valid                          |
| `ClientCertExpired`               | Client certificate is expired                                |
| `ClientCertTypeUnsupported`       | Client certificate type is unsupported                       |
| `ClientCertInvalid`               | Client certificate is invalid                                |
| `ClientCertPurposeInvalid`        | Client certificate purpose is invalid                        |
| `ClientCertRejected`              | Client certificate is rejected by custom server validation   |
| `UnmappedConnectionError`         | Unmapped runtime connection error                            |

## Example log entries

The following are example connection log entries. Note that the example text appears on
multiple lines only to make them easier to read.

The following is an example log entry for a successful connection with a HTTPS
listener with mutual TLS verify mode enabled on port 443.

```
2023-10-04T17:05:15.514108Z 203.0.113.1 36280 443 TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 4.036
"CN=amazondomains.com,O=endEntity,L=Seattle,ST=Washington,C=US" NotBefore=2023-09-21T22:43:21Z;NotAfter=2026-06-17T22:43:21Z
FEF257372D5C14D4 Success TID_3180a73013c8ca4bac2f731159d4b0fe
```

The following is an example log entry for a failed connection with a HTTPS
listener with mutual TLS verify mode enabled on port 443.

```
2023-10-04T17:05:15.514108Z 203.0.113.1 36280 443 TLSv1.2 ECDHE-RSA-AES128-GCM-SHA256 -
"CN=amazondomains.com,O=endEntity,L=Seattle,ST=Washington,C=US" NotBefore=2023-09-21T22:43:21Z;NotAfter=2026-06-17T22:43:21Z
FEF257372D5C14D4 Failed:ClientCertUntrusted TID_1c71a68d70587445ad5127ff8b2687d7
```

## Processing connection log files

The connection log files are compressed. If you open the files using the Amazon S3 console,
they are uncompressed and the information is displayed. If you download the files,
you must uncompress them to view the information.

If there is a lot of demand on your website, your load balancer can generate log
files with gigabytes of data. You might not be able to process such a large amount
of data using line-by-line processing. Therefore, you might have to use analytical
tools that provide parallel processing solutions. For example, you can use the
following analytical tools to analyze and process connection logs:

- Amazon Athena is an interactive query service that makes it easy to analyze
  data in Amazon S3 using standard SQL.
- [Loggly](https://documentation.solarwinds.com/en/success_center/loggly/content/admin/s3-ingestion-auto.htm "https://documentation.solarwinds.com/en/success_center/loggly/content/admin/s3-ingestion-auto.htm")
- [Splunk](https://splunk.github.io/splunk-add-on-for-amazon-web-services/ "https://splunk.github.io/splunk-add-on-for-amazon-web-services/")
- [Sumo
  logic](https://www.sumologic.com/application/elb/ "https://www.sumologic.com/application/elb/")
