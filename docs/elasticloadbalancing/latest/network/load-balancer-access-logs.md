# Access logs for your Network Load Balancer

Elastic Load Balancing provides access logs that capture detailed information about the TLS connections
established with your Network Load Balancer. You can use these access logs to analyze traffic patterns and
troubleshoot issues.

###### Important

While traditional "legacy" access logs (described in this section) remain available, Network Load Balancer now offers enhanced logging options through CloudWatch Logs. CloudWatch Logs provide more flexible delivery options, including to Amazon CloudWatch Logs, Amazon Data Firehose, and Amazon Simple Storage Service. To configure these improved logging options, visit your load balancer's **_Integrations_** tab. For more information on CloudWatch Logs, see [CloudWatch logs for your Network Load Balancer](load-balancer-cloudwatch-logs.md "load-balancer-cloudwatch-logs.md").

###### Important

Access logs are created only if the load balancer has a TLS listener, and the logs
contain information about TLS requests only. Access logs record requests on a best-effort
basis. We recommend that you use access logs to understand the nature of the requests,
not as a complete accounting of all requests.

Access logging is an optional feature of Elastic Load Balancing that is disabled by default. After you
enable access logging for your load balancer, Elastic Load Balancing captures the logs as compressed
files and stores them in the Amazon S3 bucket that you specify. You can disable access
logging at any time.

You can enable server-side encryption with Amazon S3-managed encryption keys (SSE-S3), or
using Key Management Service with Customer Managed Keys (SSE-KMS CMK) for your S3
bucket. Each access log file is automatically encrypted before it is stored in your S3
bucket and decrypted when you access it. You do not need to take any action as there is
no difference in the way you access encrypted or unencrypted log files. Each log file is
encrypted with a unique key, which is itself encrypted with a KMS key that is
regularly rotated. For more information, see [Specifying Amazon S3 encryption
(SSE-S3)](../../../AmazonS3/latest/userguide/specifying-s3-encryption.md "../../../AmazonS3/latest/userguide/specifying-s3-encryption.md") and [Specifying server-side encryption with AWS KMS (SSE-KMS)](../../../AmazonS3/latest/userguide/specifying-kms-encryption.md "../../../AmazonS3/latest/userguide/specifying-kms-encryption.md") in the
_Amazon S3 User Guide_.

There is no additional charge for access logs. You are charged storage costs for Amazon S3,
but not charged for the bandwidth used by Elastic Load Balancing to send log files to Amazon S3. For more
information about storage costs, see [Amazon S3
Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

###### Contents

- [Access log files](#access-log-file-format "#access-log-file-format")
- [Access log entries](#access-log-entry-format "#access-log-entry-format")
- [Processing access log files](#log-processing-tools "#log-processing-tools")
- [Enable access logs](enable-access-logs.md "enable-access-logs.md")
- [Disable access logs](disable-access-logs.md "disable-access-logs.md")

## Access log files

Elastic Load Balancing publishes a log file for each load balancer node every 5 minutes. Log
delivery is eventually consistent. The load balancer can deliver multiple logs for
the same period. This usually happens if the site has high traffic.

The file names of the access logs use the following format:

```
`bucket`[/`prefix`]/AWSLogs/`aws-account-id`/elasticloadbalancing/`region`/`yyyy`/`mm`/`dd`/`aws-account-id`_elasticloadbalancing_`region`_net.`load-balancer-id`_`end-time`_`random-string`.log.gz
```

_bucket_

The name of the S3 bucket.

_prefix_

The prefix (logical hierarchy) in the bucket. If you don't specify a
prefix, the logs are placed at the root level of the bucket.

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
time of 20181220T2340Z contains entries for requests made between 23:35
and 23:40.

_random-string_

A system-generated random string.

The following is an example log file name:

```
s3://my-bucket/prefix/AWSLogs/123456789012/elasticloadbalancing/us-east-2/2020/05/01/123456789012_elasticloadbalancing_us-east-2_net.my-loadbalancer.1234567890abcdef_20200501T0000Z_20sg8hgm.log.gz
```

You can store your log files in your bucket for as long as you want, but you can
also define Amazon S3 lifecycle rules to archive or delete log files automatically. For
more information, see [Manage your
storage lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") in the _Amazon S3 User Guide_.

## Access log entries

The following table describes the fields of an access log entry, in order. All
fields are delimited by spaces. When new fields are introduced, they are added to
the end of the log entry. When processing the log files, you should ignore any
fields at the end of the log entry that you were not expecting.

| Field                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type                         | The type of listener. The supported value is<br>`tls`.                                                                                                                                                                                                                                                                                                                                                                                        |
| version                      | The version of the log entry. The current version is<br>2.0.                                                                                                                                                                                                                                                                                                                                                                                  |
| time                         | The time recorded at the end of the TLS connection, in ISO<br>8601 format.                                                                                                                                                                                                                                                                                                                                                                    |
| elb                          | The resource ID of the load balancer.                                                                                                                                                                                                                                                                                                                                                                                                         |
| listener                     | The resource ID of the TLS listener for the connection.                                                                                                                                                                                                                                                                                                                                                                                       |
| client_port                  | The IP address and port of the client.                                                                                                                                                                                                                                                                                                                                                                                                        |
| destination_port             | The IP address and port of the destination. If the client<br>connects directly to the load balancer, the destination is the<br>listener. If the client connects using a VPC endpoint service,<br>the destination is the VPC endpoint.                                                                                                                                                                                                         |
| connection_time              | The total time for the connection to complete, from start to<br>closure, in milliseconds.                                                                                                                                                                                                                                                                                                                                                     |
| tls_handshake_time           | The total time for the TLS handshake to complete after<br>the TCP connection is established, including client-side<br>delays, in milliseconds. This time is included in the<br>`connection_time` field. If there is no TLS<br>handshake or a TLS handshake failure, this value is set<br>to `-`.                                                                                                                                              |
| received_bytes               | The count of bytes received by the load balancer from the<br>client, after decryption.                                                                                                                                                                                                                                                                                                                                                        |
| sent_bytes                   | The count of bytes sent by the load balancer to the client,<br>before encryption.                                                                                                                                                                                                                                                                                                                                                             |
| incoming_tls_alert           | The integer value of TLS alerts received by the load balancer<br>from the client, if present. Otherwise, this value is set to<br>`-`.                                                                                                                                                                                                                                                                                                         |
| chosen_cert_arn              | The ARN of the certificate served to the client. If no valid<br>client hello message is sent, this value is set to `-`.                                                                                                                                                                                                                                                                                                                       |
| chosen_cert_serial           | Reserved for future use. This value is always set to `-`.                                                                                                                                                                                                                                                                                                                                                                                     |
| tls_cipher                   | The cipher suite negotiated with the client, in OpenSSL<br>format. If TLS negotiation does not complete, this value is set<br>to `-`.                                                                                                                                                                                                                                                                                                         |
| tls_protocol_version         | The TLS protocol negotiated with the client, in string format.<br>The possible values are `tlsv10`,<br>`tlsv11`, `tlsv12`, and `tlsv13`.<br>If TLS negotiation does not complete, this value is set to `-`.                                                                                                                                                                                                                                   |
| tls_keyexchange              | The key exchange used during handshakes for TLS or PQ-TLS .<br>If TLS or PQ-TLS negotiation does not complete, this value is set to `-`.                                                                                                                                                                                                                                                                                                      |
| domain_name                  | The value of the server_name extension in the client hello<br>message. This value is URL-encoded. If no valid client hello<br>message is sent or the extension is not present, this value is<br>set to `-`.                                                                                                                                                                                                                                   |
| alpn_fe_protocol             | The application protocol negotiated with the client, in string<br>format. The possible values are `h2`,<br>`http/1.1`, and `http/1.0`. If no ALPN<br>policy is configured in the TLS listener, no matching protocol<br>is found, or no valid protocol list is sent, this value is set<br>to `-`.                                                                                                                                              |
| alpn_be_protocol             | The application protocol negotiated with the target, in string<br>format. The possible values are `h2`,<br>`http/1.1`, and `http/1.0`. If no ALPN<br>policy is configured in the TLS listener, no matching protocol<br>is found, or no valid protocol list is sent, this value is set<br>to `-`.                                                                                                                                              |
| alpn_client_preference_list  | The value of the application_layer_protocol_negotiation<br>extension in the client hello message. This value is<br>URL-encoded. Each protocol is enclosed in double quotes and<br>protocols are separated by a comma. If no ALPN policy is<br>configured in the TLS listener, no valid client hello message is<br>sent, or the extension is not present, this value is set to `-`.<br>The string is truncated if it is longer than 256 bytes. |
| tls_connection_creation_time | The time recorded at the beginning of the TLS connection,<br>in ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                              |

### Example log entries

The following are example log entries. Note that the text appears on multiple
lines only to make it easier to read.

The following is an example for a TLS listener without an ALPN policy.

```
tls 2.0 2018-12-20T02:59:40 net/my-network-loadbalancer/c6e77e28c25b2234 g3d4b5e8bb8464cd
72.21.218.154:51341 172.100.100.185:443 5 2 98 246 -
arn:aws:acm:us-east-2:671290407336:certificate/2a108f19-aded-46b0-8493-c63eb1ef4a99 -
ECDHE-RSA-AES128-SHA tlsv12 -
my-network-loadbalancer-c6e77e28c25b2234.elb.us-east-2.amazonaws.com
- - - 2018-12-20T02:59:30
```

The following is an example for a TLS listener with an ALPN policy.

```
tls 2.0 2020-04-01T08:51:42 net/my-network-loadbalancer/c6e77e28c25b2234 g3d4b5e8bb8464cd
72.21.218.154:51341 172.100.100.185:443 5 2 98 246 -
arn:aws:acm:us-east-2:671290407336:certificate/2a108f19-aded-46b0-8493-c63eb1ef4a99 -
ECDHE-RSA-AES128-SHA tlsv12 -
my-network-loadbalancer-c6e77e28c25b2234.elb.us-east-2.amazonaws.com
h2 h2 "h2","http/1.1" 2020-04-01T08:51:20
```

## Processing access log files

The access log files are compressed. If you open the files using the Amazon S3 console,
they are uncompressed and the information is displayed. If you download the files,
you must uncompress them to view the information.

If there is a lot of demand on your website, your load balancer can generate log
files with gigabytes of data. You might not be able to process such a large amount
of data using line-by-line processing. Therefore, you might have to use analytical
tools that provide parallel processing solutions. For example, you can use the
following analytical tools to analyze and process access logs:

- Amazon Athena is an interactive query service that makes it easy to analyze
  data in Amazon S3 using standard SQL. For more information, see [Querying Network Load Balancer
  logs](../../../athena/latest/ug/networkloadbalancer-classic-logs.md "../../../athena/latest/ug/networkloadbalancer-classic-logs.md") in the _Amazon Athena User Guide_.
- [Loggly](https://documentation.solarwinds.com/en/success_center/loggly/content/admin/s3-ingestion-auto.htm "https://documentation.solarwinds.com/en/success_center/loggly/content/admin/s3-ingestion-auto.htm")
- [Splunk](https://splunk.github.io/splunk-add-on-for-amazon-web-services/ "https://splunk.github.io/splunk-add-on-for-amazon-web-services/")
- [Sumo
  Logic](https://www.sumologic.com/application/elb/ "https://www.sumologic.com/application/elb/")
