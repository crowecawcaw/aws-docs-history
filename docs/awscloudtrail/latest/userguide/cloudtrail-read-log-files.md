# Downloading your CloudTrail log files

Log files are in JSON format. If you have a JSON viewer add-on installed, you can view the
files directly in your browser. Double-click the log file name in the bucket to open a new
browser window or tab. The JSON displays in a readable format.

CloudTrail log files are Amazon S3 objects. You can use the Amazon S3 console, the AWS Command Line Interface (CLI), or the
Amazon S3 API to retrieve log files.

For more information, see [Amazon S3 objects overview](../../../AmazonS3/latest/userguide/UsingObjects.md "../../../AmazonS3/latest/userguide/UsingObjects.md") in the _Amazon Simple Storage Service User Guide._

The following procedure describes how to download a log file with the AWS Management Console.

###### To download and read a log file

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the bucket and choose the log file that you want to download.
3. Choose **Download** or **Download as** and
   follow the prompts to save the file. This saves the file in compressed
   format.

###### Note

Some browsers, such as Chrome, automatically extract the log file for you. If
your browser does this for you, skip to step 5. 4. Use a product such as [7-Zip](https://www.7-zip.org/ "https://www.7-zip.org/") to extract
the log file. 5. Open the log file in a text editor such as Notepad++.
For more information about the event fields that can appear in a log file entry, see [CloudTrail record contents for management, data, and network activity events](cloudtrail-event-reference-record-contents.md "cloudtrail-event-reference-record-contents.md").

AWS partners with third-party specialists in logging and analysis to provide solutions
that use CloudTrail output. For more information, see [AWS CloudTrail
partners](https://aws.amazon.com/cloudtrail/partners/ "https://aws.amazon.com/cloudtrail/partners/").

###### Note

You can also use the **Event history** feature to look up events for
create, update, and delete API activity during the last 90 days.

For more information, see [Working with CloudTrail event history](view-cloudtrail-events.md "view-cloudtrail-events.md").
