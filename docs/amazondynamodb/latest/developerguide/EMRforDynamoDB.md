# Tutorial: Working with Amazon DynamoDB and Apache

Hive

In this tutorial, you will launch an Amazon EMR cluster, and then use Apache Hive to
process data stored in a DynamoDB table.

_Hive_ is a data warehouse application for Hadoop that allows you
to process and analyze data from multiple sources. Hive provides a SQL-like language,
_HiveQL_, that lets you work with data stored locally in the
Amazon EMR cluster or in an external data source (such as Amazon DynamoDB).

For more information, see to the [Hive
Tutorial](https://cwiki.apache.org/confluence/display/Hive/Tutorial "https://cwiki.apache.org/confluence/display/Hive/Tutorial").

###### Topics

- [Before you begin](#EMRforDynamoDB.Tutorial.BeforeYouBegin "#EMRforDynamoDB.Tutorial.BeforeYouBegin")
- [Step 1: Create an Amazon EC2 key
  pair](EMRforDynamoDB.Tutorial.md "EMRforDynamoDB.Tutorial.md")
- [Step 2: Launch an Amazon EMR
  cluster](EMRforDynamoDB.Tutorial.md "EMRforDynamoDB.Tutorial.md")
- [Step 3: Connect
  to the Leader node](EMRforDynamoDB.Tutorial.md "EMRforDynamoDB.Tutorial.md")
- [Step 4: Load data into
  HDFS](EMRforDynamoDB.Tutorial.md "EMRforDynamoDB.Tutorial.md")
- [Step 5: Copy data to
  DynamoDB](EMRforDynamoDB.Tutorial.md "EMRforDynamoDB.Tutorial.md")
- [Step 6: Query the data
  in the DynamoDB table](EMRforDynamoDB.Tutorial.md "EMRforDynamoDB.Tutorial.md")
- [Step 7: (Optional) clean
  up](EMRforDynamoDB.Tutorial.md "EMRforDynamoDB.Tutorial.md")

## Before you begin

For this tutorial, you will need the following:

- An AWS account. If you do not have one, see [Signing up for AWS](SettingUp.md#SettingUp.DynamoWebService.SignUpForAWS "SettingUp.md#SettingUp.DynamoWebService.SignUpForAWS").
- An SSH client (Secure Shell). You use the SSH client to connect to the
  leader node of the Amazon EMR cluster and run interactive commands. SSH
  clients are available by default on most Linux, Unix, and Mac OS X
  installations. Windows users can download and install the [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/ "http://www.chiark.greenend.org.uk/~sgtatham/putty/")
  client, which has SSH support.

###### Next step

[Step 1: Create an Amazon EC2 key
pair](EMRforDynamoDB.Tutorial.md "EMRforDynamoDB.Tutorial.md")
