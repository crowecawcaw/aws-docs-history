# Monitoring AWS B2B Data Interchange with Amazon CloudWatch

You can monitor AWS B2B Data Interchange using CloudWatch, which publishes logs. You can access
historical information and gain a better perspective on how your web application or
service is performing. You can also set alarms that watch for certain thresholds, and
send notifications or take actions when those thresholds are met. For more information,
see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

Logging can be enabled for each profile. When you create a profile, logging is enabled
by default, unless you choose to turn off logging for the profile. When you enable
logging, you see the following log groups:

- One default log group.

This log group is named
`/aws/vendedlogs/b2bi/default`.

Entries to this log group are created after a file is added to an Amazon S3 bucket,
but the EDI file cannot be processed correctly.

- One log group for each profile that you create (if the profile has logging
  enabled).

This log group is named
`/aws/vendedlogs/b2bi/profile/`profile-id``.

Entries to this log group are created after a file is added to an Amazon S3 bucket,
unless the EDI file cannot be processed correctly (logging is to the default log
group in this case). The information in the EDI file is used to find a trading
capability to handle the processing, and the trading capability is associated
with a profile. If EDI processing fails, then there is no information available
to find the trading capability and profile, and the service is unable to log to
the profile log group.

- One log group for all transformers that you create (logging for transformers
  is always enabled).

This log group is named
`/aws/vendedlogs/b2bi/transformers`.

Entries to this log group are created when a user calls the
`StartTransformerJob` API. If the transformer is invoked from a
trading capability, no logs are written to this group.
The following matrix describes the states and statuses that are visible in CloudWatch
logs.

| State/Status                                                                                                                                         | Complete                                                   | Failed                                                    | In progress                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------------- |
| **Capability Match** The service attempts to match the incoming file with one of the customer’s existing trading capability resources                | The attempt to match is successful                         | Attempt to match the incoming file failed                 | System is searching for a trading capability match          |
| **Acknowledgement** The service generates acknowledgements whenever an EDI document is transformed.                                                  | An acknowledgement has been successfully completed         | An acknowledgement has failed to send                     | System is currently attempting to send an acknowledgement   |
| **File Transform** Pertains to requests for processing transformations when initiated by calling `StartTransformerJob`.                              | File transformation has successfully completed             | File transform has failed to complete                     | File transform is in progress                               |
| **File Deliver** The terminal state, where the system attempts to write the result of a transformation to the customer’s designated output location. | File has been stored to the appropriate Amazon S3 location | File has failed to be delivered to its Amazon S3 location | Storing the file to its appropriate location is in progress |
