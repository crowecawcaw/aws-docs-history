# Tutorial: Export an Amazon Keyspaces table to Amazon S3 using AWS Glue

This tutorial shows you how to export an Amazon Keyspaces table to an Amazon S3 bucket using AWS Glue. For
this tutorial, many manual steps are automated using shell scripts available in the Amazon Keyspaces
[Github](https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/scala/datastax-v4/aws-glue "https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/scala/datastax-v4/aws-glue") repo. Using this process, you can export Amazon Keyspaces data to Amazon S3 without having to setup a Spark cluster.

###### Topics

- [Prerequisites for exporting data from Amazon Keyspaces to Amazon S3](S3-tutorial-prerequisites.md "S3-tutorial-prerequisites.md")
- [Step 1: Create the Amazon S3 bucket, download the required tools, and configure the environment](S3-tutorial-step1.md "S3-tutorial-step1.md")
- [Step 2: Configure the AWS Glue job that exports the
  Amazon Keyspaces table](S3-tutorial-step2.md "S3-tutorial-step2.md")
- [Step 3: Run the AWS Glue job to export the Amazon Keyspaces table to the Amazon S3 bucket from the
  AWS CLI](S3-tutorial-step3.md "S3-tutorial-step3.md")
- [Step 4: (Optional) Create a trigger to schedule the export job](S3-tutorial-step4.md "S3-tutorial-step4.md")
- [Step 5: (Optional) Cleanup](S3-tutorial-step5.md "S3-tutorial-step5.md")
