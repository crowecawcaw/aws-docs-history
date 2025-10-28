# Troubleshooting Splunk

Check the following if data is not delivered to your Splunk endpoint.

- If your Splunk platform is in a VPC, make sure that Firehose can access it. For
  more information, see [Accessing Splunk in VPC](controlling-access.md#using-iam-splunk-vpc "controlling-access.md#using-iam-splunk-vpc").
- If you use an AWS load balancer, make sure that it is a Classic Load Balancer or an Application Load Balancer. Also, enable duration-based sticky sessions with
  cookie expiration disabled for Classic Load Balancer and expiration is set to the maximum (7 days) for Application Load Balancer. For information about how to do this, see Duration-Based Session Stickiness
  for [Classic Load Balancer](../../../elasticloadbalancing/latest/classic/elb-sticky-sessions.md#enable-sticky-sessions-duration "../../../elasticloadbalancing/latest/classic/elb-sticky-sessions.md#enable-sticky-sessions-duration") or
  an [Application Load Balancer](../../../elasticloadbalancing/latest/application/sticky-sessions.md "../../../elasticloadbalancing/latest/application/sticky-sessions.md").
- Review the Splunk platform requirements. The Splunk add-on for Firehose requires
  Splunk platform version 6.6.X or later. For more information, see [Splunk Add-on for Amazon Kinesis Firehose](http://docs.splunk.com/Documentation/AddOns/released/Firehose/Hardwareandsoftwarerequirements "http://docs.splunk.com/Documentation/AddOns/released/Firehose/Hardwareandsoftwarerequirements").
- If you have a proxy (Elastic Load Balancing or other) between Firehose and the HTTP Event
  Collector (HEC) node, enable sticky sessions to support HEC acknowledgements
  (ACKs).
- Make sure that you are using a valid HEC token.
- Ensure that the HEC token is enabled.
- Check whether the data that you're sending to Splunk is formatted correctly.
  For more information, see [Format events for HTTP Event Collector](http://docs.splunk.com/Documentation/Splunk/7.0.3/Data/FormateventsforHTTPEventCollector "http://docs.splunk.com/Documentation/Splunk/7.0.3/Data/FormateventsforHTTPEventCollector").
- Make sure that the HEC token and input event are configured with a valid
  index.
- When an upload to Splunk fails due to a server error from the HEC node, the
  request is automatically retried. If all retries fail, the data gets backed up
  to Amazon S3. Check if your data appears in Amazon S3, which is an indication of such a
  failure.
- Make sure that you enabled indexer acknowledgment on your HEC token.
- Increase the value of `HECAcknowledgmentTimeoutInSeconds` in the
  Splunk destination configuration of your Firehose stream.
- Increase the value of `DurationInSeconds` under
  `RetryOptions` in the Splunk destination configuration of your
  Firehose stream.
- Check your HEC health.
- If you're using data transformation, make sure that your Lambda function never
  returns responses whose payload size exceeds 6 MB. For more information, see
  [Amazon Data Firehose Data Transformation](data-transformation.md#data-transformation.title "data-transformation.md#data-transformation.title").
- Make sure that the Splunk parameter named `ackIdleCleanup` is set
  to `true`. It is false by default. To set this parameter to
  `true`, do the following:
  - For a [managed Splunk Cloud deployment](http://docs.splunk.com/Documentation/AddOns/released/Firehose/RequestFirehose "http://docs.splunk.com/Documentation/AddOns/released/Firehose/RequestFirehose"), submit a case using the
    Splunk support portal. In this case, ask Splunk support to enable the
    HTTP event collector, set `ackIdleCleanup` to
    `true` in `inputs.conf`, and create or modify
    a load balancer to use with this add-on.
  - For a [distributed Splunk Enterprise deployment](http://docs.splunk.com/Documentation/AddOns/released/Firehose/ConfigureHECdistributed "http://docs.splunk.com/Documentation/AddOns/released/Firehose/ConfigureHECdistributed"), set the
    `ackIdleCleanup` parameter to true in the
    `inputs.conf` file. For \*nix users, this file is located
    under `$SPLUNK_HOME/etc/apps/splunk_httpinput/local/`. For
    Windows users, it is under
    `%SPLUNK_HOME%\etc\apps\splunk_httpinput\local\`.
  - For a [single-instance Splunk Enterprise deployment](http://docs.splunk.com/Documentation/AddOns/released/Firehose/ConfigureHECsingle "http://docs.splunk.com/Documentation/AddOns/released/Firehose/ConfigureHECsingle"), set the
    `ackIdleCleanup` parameter to `true` in the
    `inputs.conf` file. For \*nix users, this file is located
    under `$SPLUNK_HOME/etc/apps/splunk_httpinput/local/`. For
    Windows users, it is under
    `%SPLUNK_HOME%\etc\apps\splunk_httpinput\local\`.

- Make sure that the IAM role that is specified in your Firehose stream can access
  the S3 backup bucket and the Lambda function for data transformation (if data transformation is enabled). Also, make sure that the IAM role has access to CloudWatch Logs group and log streams to check error logs.
  For more information, see [Grant FirehoseAccess to a Splunk Destination](controlling-access.md#using-iam-splunk "controlling-access.md#using-iam-splunk").
- To redrive the data that was delivered to S3 error bucket (S3 backup) back to
  Splunk, follow the steps mentioned in the [Splunk documentation](https://www.splunk.com/en_us/blog/tips-and-tricks/aws-technical-add-on-simplifying-error-data-re-ingestion.html "https://www.splunk.com/en_us/blog/tips-and-tricks/aws-technical-add-on-simplifying-error-data-re-ingestion.html").
- See [Troubleshoot the Splunk Add-on for Amazon Kinesis Firehose](http://docs.splunk.com/Documentation/AddOns/released/Firehose/Troubleshoot "http://docs.splunk.com/Documentation/AddOns/released/Firehose/Troubleshoot").
