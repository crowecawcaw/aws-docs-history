# Understand CloudTrail logs and Athena tables

Before you begin creating tables, you should understand a little more about CloudTrail and
how it stores data. This can help you create the tables that you need, whether you
create them from the CloudTrail console or from Athena.

CloudTrail saves logs as JSON text files in compressed gzip format
(`*.json.gz`). The location of the log files depends on how you
set up trails, the AWS Region or Regions in which you are logging, and other factors.

For more information about where logs are stored, the JSON structure, and the record
file contents, see the following topics in the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"):

- [Finding your CloudTrail log files](../../../awscloudtrail/latest/userguide/cloudtrail-find-log-files.md "../../../awscloudtrail/latest/userguide/cloudtrail-find-log-files.md")
- [CloudTrail Log File examples](../../../awscloudtrail/latest/userguide/cloudtrail-log-file-examples.md "../../../awscloudtrail/latest/userguide/cloudtrail-log-file-examples.md")
- [CloudTrail record contents](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md")
- [CloudTrail event reference](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference.md")
  To collect logs and save them to Amazon S3, enable CloudTrail from the AWS Management Console. For more
  information, see [Creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.md") in the _AWS CloudTrail User Guide_.
