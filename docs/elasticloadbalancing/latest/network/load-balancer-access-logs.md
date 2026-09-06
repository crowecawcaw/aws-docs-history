

# Access logs for your Network Load Balancer
<a name="load-balancer-access-logs"></a>

Elastic Load Balancing provides access logs that capture detailed information about the TLS connections established with your Network Load Balancer. You can use these access logs to analyze traffic patterns and troubleshoot issues.

**Important**  
 While traditional "legacy" access logs (described in this section) remain available, Network Load Balancer now offers enhanced logging options through CloudWatch Logs. CloudWatch Logs provide more flexible delivery options, including to Amazon CloudWatch Logs, Amazon Data Firehose, and Amazon Simple Storage Service. To configure these improved logging options, visit your load balancer's * **Integrations*** tab. For more information on CloudWatch Logs, see [CloudWatch logs for your Network Load Balancer](load-balancer-cloudwatch-logs.md). 

**Important**  
Access logs are created only if the load balancer has a TLS listener, and the logs contain information about TLS requests only. Access logs record requests on a best-effort basis. We recommend that you use access logs to understand the nature of the requests, not as a complete accounting of all requests.

Access logging is an optional feature of Elastic Load Balancing that is disabled by default. After you enable access logging for your load balancer, Elastic Load Balancing captures the logs as compressed files and stores them in the Amazon S3 bucket that you specify. You can disable access logging at any time.

You can enable server-side encryption with Amazon S3-managed encryption keys (SSE-S3), or using Key Management Service with Customer Managed Keys (SSE-KMS CMK) for your S3 bucket. Each access log file is automatically encrypted before it is stored in your S3 bucket and decrypted when you access it. You do not need to take any action as there is no difference in the way you access encrypted or unencrypted log files. Each log file is encrypted with a unique key, which is itself encrypted with a KMS key that is regularly rotated. For more information, see [Specifying Amazon S3 encryption (SSE-S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/specifying-s3-encryption.html) and [Specifying server-side encryption with AWS KMS (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/specifying-kms-encryption.html) in the *Amazon S3 User Guide*.

There is no additional charge for access logs. You are charged storage costs for Amazon S3, but not charged for the bandwidth used by Elastic Load Balancing to send log files to Amazon S3. For more information about storage costs, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/).

**Topics**
+ [Access log files](#access-log-file-format)
+ [Access log entries](#access-log-entry-format)
+ [Processing access log files](#log-processing-tools)
+ [Enable access logs](enable-access-logs.md)
+ [Disable access logs](disable-access-logs.md)

## Access log files
<a name="access-log-file-format"></a>

Elastic Load Balancing publishes a log file for each load balancer node every 5 minutes. Log delivery is eventually consistent. The load balancer can deliver multiple logs for the same period. This usually happens if the site has high traffic.

The file names of the access logs use the following format:

```
{{bucket}}[/{{prefix}}]/AWSLogs/{{aws-account-id}}/elasticloadbalancing/{{region}}/{{yyyy}}/{{mm}}/{{dd}}/{{aws-account-id}}_elasticloadbalancing_{{region}}_net.{{load-balancer-id}}_{{end-time}}_{{random-string}}.log.gz
```

*bucket*  
The name of the S3 bucket.

*prefix*  
The prefix (logical hierarchy) in the bucket. If you don't specify a prefix, the logs are placed at the root level of the bucket.

*aws-account-id*  
The AWS account ID of the owner.

*region*  
The Region for your load balancer and S3 bucket.

*yyyy*/*mm*/*dd*  
The date that the log was delivered.

*load-balancer-id*  
The resource ID of the load balancer. If the resource ID contains any forward slashes (/), they are replaced with periods (.).

*end-time*  
The date and time that the logging interval ended. For example, an end time of 20181220T2340Z contains entries for requests made between 23:35 and 23:40.

*random-string*  
A system-generated random string.

The following is an example log file name:

```
s3://my-bucket/prefix/AWSLogs/123456789012/elasticloadbalancing/us-east-2/2020/05/01/123456789012_elasticloadbalancing_us-east-2_net.my-loadbalancer.1234567890abcdef_20200501T0000Z_20sg8hgm.log.gz
```

You can store your log files in your bucket for as long as you want, but you can also define Amazon S3 lifecycle rules to archive or delete log files automatically. For more information, see [Manage your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) in the *Amazon S3 User Guide*.

## Access log entries
<a name="access-log-entry-format"></a>

The following table describes the fields of an access log entry, in order. All fields are delimited by spaces. When new fields are introduced, they are added to the end of the log entry. When processing the log files, you should ignore any fields at the end of the log entry that you were not expecting.


| Field | Description | 
| --- | --- | 
| type | The type of listener. The supported value is `tls`. | 
| version | The version of the log entry. The current version is 2.0. | 
| time | The time recorded at the end of the TLS connection, in ISO 8601 format. | 
| elb | The resource ID of the load balancer. | 
| listener | The resource ID of the TLS listener for the connection. | 
| client\_port | The IP address and port of the client. | 
| destination\_port | The IP address and port of the destination. If the client connects directly to the load balancer, the destination is the listener. If the client connects using a VPC endpoint service, the destination is the VPC endpoint. | 
| connection\_time | The total time for the connection to complete, from start to closure, in milliseconds. | 
| tls\_handshake\_time | The total time for the TLS handshake to complete after the TCP connection is established, including client-side delays, in milliseconds. This time is included in the `connection_time` field. If there is no TLS handshake or a TLS handshake failure, this value is set to `-`. | 
| received\_bytes | The count of bytes received by the load balancer from the client, after decryption. | 
| sent\_bytes | The count of bytes sent by the load balancer to the client, before encryption. | 
| incoming\_tls\_alert | The integer value of TLS alerts received by the load balancer from the client, if present. Otherwise, this value is set to `-`. | 
| chosen\_cert\_arn | The ARN of the certificate served to the client. If no valid client hello message is sent, this value is set to `-`. | 
| chosen\_cert\_serial | Reserved for future use. This value is always set to `-`. | 
| tls\_cipher | The cipher suite negotiated with the client, in OpenSSL format. If TLS negotiation does not complete, this value is set to `-`. | 
| tls\_protocol\_version | The TLS protocol negotiated with the client, in string format. The possible values are `tlsv10`, `tlsv11`, `tlsv12`, and `tlsv13`. If TLS negotiation does not complete, this value is set to `-`. | 
| tls\_keyexchange | The key exchange used during handshakes for TLS or PQ-TLS . If TLS or PQ-TLS negotiation does not complete, this value is set to `-`. | 
| domain\_name | The value of the server\_name extension in the client hello message. This value is URL-encoded. If no valid client hello message is sent or the extension is not present, this value is set to `-`. | 
| alpn\_fe\_protocol | The application protocol negotiated with the client, in string format. The possible values are `h2`, `http/1.1`, and `http/1.0`. If no ALPN policy is configured in the TLS listener, no matching protocol is found, or no valid protocol list is sent, this value is set to `-`. | 
| alpn\_be\_protocol | The application protocol negotiated with the target, in string format. The possible values are `h2`, `http/1.1`, and `http/1.0`. If no ALPN policy is configured in the TLS listener, no matching protocol is found, or no valid protocol list is sent, this value is set to `-`. | 
| alpn\_client\_preference\_list | The value of the application\_layer\_protocol\_negotiation extension in the client hello message. This value is URL-encoded. Each protocol is enclosed in double quotes and protocols are separated by a comma. If no ALPN policy is configured in the TLS listener, no valid client hello message is sent, or the extension is not present, this value is set to `-`. The string is truncated if it is longer than 256 bytes. | 
| tls\_connection\_creation\_time | The time recorded at the beginning of the TLS connection, in ISO 8601 format. | 

### Example log entries
<a name="access-log-entry-examples"></a>

The following are example log entries. Note that the text appears on multiple lines only to make it easier to read.

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
<a name="log-processing-tools"></a>

The access log files are compressed. If you open the files using the Amazon S3 console, they are uncompressed and the information is displayed. If you download the files, you must uncompress them to view the information.

If there is a lot of demand on your website, your load balancer can generate log files with gigabytes of data. You might not be able to process such a large amount of data using line-by-line processing. Therefore, you might have to use analytical tools that provide parallel processing solutions. For example, you can use the following analytical tools to analyze and process access logs:
+ Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. For more information, see [Querying Network Load Balancer logs](https://docs.aws.amazon.com/athena/latest/ug/networkloadbalancer-classic-logs.html) in the *Amazon Athena User Guide*.
+ [Loggly](https://documentation.solarwinds.com/en/success_center/loggly/content/admin/s3-ingestion-auto.htm)
+ [Splunk](https://splunk.github.io/splunk-add-on-for-amazon-web-services/)
+ [Sumo Logic](https://www.sumologic.com/application/elb/)