

# Tutorial: Export an Amazon Keyspaces table to Amazon S3 using AWS Glue
<a name="S3-tutorial"></a>

This tutorial shows you how to export an Amazon Keyspaces table to an Amazon S3 bucket using AWS Glue. The tutorial uses the `keyspaces-bulk-cli` CLI tool available in the Amazon Keyspaces [GitHub](https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/scala/datastax-v4/aws-glue) repo. Using this tool, you can export Amazon Keyspaces data to Amazon S3 without having to set up a Spark cluster.

**Topics**
+ [Prerequisites for exporting data from Amazon Keyspaces to Amazon S3](S3-tutorial-prerequisites.md)
+ [Step 1: Bootstrap the infrastructure and AWS Glue jobs](S3-tutorial-step1.md)
+ [Step 2: Run the export job](S3-tutorial-step2.md)
+ [Step 3: (Optional) Create a trigger to schedule the export job](S3-tutorial-step3.md)
+ [Step 4: (Optional) Cleanup](S3-tutorial-step4.md)