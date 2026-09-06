

# Rapid7
<a name="rapid7"></a>

Rapid7, Inc. is on a mission to create a safer digital world by making cybersecurity simpler and more accessible. Rapid7 empowers security professionals to manage a modern attack surface through best-in-class technology, leading-edge research, and broad, strategic expertise. Rapid7’s comprehensive security solutions help more than 10,000 global customers unite cloud risk management and threat detection to reduce attack surfaces and eliminate threats with speed and precision.

## AWS AppFabric audit log ingestion considerations
<a name="rapid7-ingestion-considerations"></a>

The following sections describe the AppFabric output schema, output format, and output destinations to use with Rapid7.

### Schema and format
<a name="rapid7-schema-and-format"></a>

Rapid7 supports the following AppFabric output schema and formats:
+ Raw - JSON
  + AppFabric outputs data in the original schema used by the source application in the JSON format.
+ OCSF - JSON
  + AppFabric normalizes the data using the Open Cybersecurity Schema Framework (OCSF) and outputs the data in the JSON format.

### Output locations
<a name="rapid7-output-locations"></a>

Rapid7 supports the following AppFabric output location:
+ Amazon Simple Storage Service (Amazon S3)
  + To configure Rapid7 to receive data from the Amazon S3 bucket that contains your audit logs, follow the instructions in the [How to Monitor Your Amazon S3 Activity with InsightIDR](https://www.rapid7.com/blog/post/2019/08/07/how-to-monitor-your-aws-s3-activity-with-insightidr/) blog post on the Rapid7 Blog website.