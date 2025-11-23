# Getting and viewing your CloudTrail log files

After you create a trail and configure it to capture the log files you want, you need to
be able to find the log files and interpret the information they contain.

CloudTrail delivers your log files to an Amazon S3 bucket that you specify when you create the trail.
CloudTrail typically delivers logs within an average of about 5 minutes of an API call. This time
is not guaranteed. Review the [AWS CloudTrail Service
Level Agreement](https://aws.amazon.com/cloudtrail/sla "https://aws.amazon.com/cloudtrail/sla") for more information. Insights events are typically delivered to your
bucket within 30 minutes of unusual activity. After you enable Insights events for the first time,
allow up to 36 hours to see the first Insights events, if unusual activity is detected.

###### Note

If you misconfigure your trail (for example, the S3 bucket is unreachable),
CloudTrail will attempt to redeliver the log files to your S3 bucket for 30 days, and
these attempted-to-deliver events will be subject to standard CloudTrail charges.
To avoid charges on a misconfigured trail, you need to delete the trail.

###### Topics

- [Finding your CloudTrail log files](#cloudtrail-find-log-files "#cloudtrail-find-log-files")
- [Downloading your CloudTrail log files](cloudtrail-read-log-files.md "cloudtrail-read-log-files.md")

## Finding your CloudTrail log files

CloudTrail publishes log files to your S3 bucket in a gzip archive. In the S3 bucket, the log
file has a formatted name that includes the following elements:

- The bucket name that you specified when you created trail (found on the Trails
  page of the CloudTrail console)
- The (optional) prefix you specified when you created your trail
- The string "AWSLogs"
- The account number
- The string "CloudTrail" for data, management events
- The string "CloudTrail-Insight" for insights events
- The string "CloudTrail-NetworkActivity" for network activity events
- The string "CloudTrail-Aggregated" for aggregated events for data events
- A Region identifier such as us-west-1
- The year the log file was published in `YYYY` format
- The month the log file was published in `MM` format
- The day the log file was published in `DD` format
- An alphanumeric string that disambiguates the file from others that cover the
  same time period

The following example shows a complete log file object name for data, management events:

```
`amzn-s3-demo-bucket`/`prefix_name`/AWSLogs/`Account ID`/CloudTrail/`region`/`YYYY`/`MM`/`DD`/`file_name.json.gz`
```

The following example shows a complete log file object name for insight events:

```
`amzn-s3-demo-bucket`/`prefix_name`/AWSLogs/`Account ID`/CloudTrail-Insight/`region`/`YYYY`/`MM`/`DD`/`file_name.json.gz`
```

The following example shows a complete log file object name for network activity events:

```
`amzn-s3-demo-bucket`/`prefix_name`/AWSLogs/`Account ID`/CloudTrail-NetworkActivity/`region`/`YYYY`/`MM`/`DD`/`file_name.json.gz`
```

The following example shows a complete log file object name for data event aggregations:

```
`amzn-s3-demo-bucket`/`prefix_name`/AWSLogs/`Account ID`/CloudTrail-Aggregated/`region`/`YYYY`/`MM`/`DD`/`file_name.json.gz`
```

###### Note

For organization trails, the log file object name in the S3 bucket includes the organization unit ID in
the path, as follows:

```
`amzn-s3-demo-bucket`/`prefix_name`/AWSLogs/`O-ID`/`Account ID`/CloudTrail/`Region`/`YYYY`/`MM`/`DD`/`file_name.json.gz`
```

To retrieve a log file, you can use the Amazon S3 console, the Amazon S3 command line interface
(CLI), or the API.

###### To find your log files with the Amazon S3 console

1. Open the Amazon S3 console.
2. Choose the bucket you specified.
3. Navigate through the object hierarchy until you find the log file you want.

All log files have a .gz extension.

You will navigate through an object hierarchy that is similar to the following example,
but with a different bucket name, account ID, Region, and date.

```

All Buckets
    amzn-s3-demo-bucket
        AWSLogs
            123456789012
                CloudTrail
                    us-west-1
                        2014
                            06
                                20

```

A log file for the preceding object hierarchy will look like the following:

```

123456789012_CloudTrail_us-west-1_20140620T1255ZHdkvFTXOA3Vnhbc.json.gz

```

###### Note

Although uncommon, you may receive log files that contain one or more duplicate
events. In most cases, duplicate events will have the same `eventID`. For more
information about the `eventID` field, see [CloudTrail record contents for management, data, and network activity events](cloudtrail-event-reference-record-contents.md "cloudtrail-event-reference-record-contents.md").
