

# Tutorial: Create a Studio notebook in Managed Service for Apache Flink
<a name="example-notebook"></a>

The following tutorial demonstrates how to create a Studio notebook that reads data from a Kinesis data stream or an Amazon MSK cluster.

**Topics**
+ [Complete the prerequisites](#example-notebook-setup)
+ [Create an AWS Glue database](#example-notebook-glue)
+ [Next steps: Create a Studio notebook with Kinesis Data Streams or Amazon MSK](#examples-notebook-nextsteps)
+ [Create a Studio notebook with Kinesis Data Streams](example-notebook-streams.md)
+ [Create a Studio notebook with Amazon MSK](example-notebook-msk.md)
+ [Clean up your application and dependent resources](example-notebook-cleanup.md)

## Complete the prerequisites
<a name="example-notebook-setup"></a>

Make sure that your AWS CLI is version 2 or later. To install the latest AWS CLI, see [ Installing, updating, and uninstalling the AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

## Create an AWS Glue database
<a name="example-notebook-glue"></a>

Your Studio notebook uses an [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) database for metadata about your Amazon MSK data source.

**Create an AWS Glue Database**

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

1. Choose **Add database**. In the **Add database** window, enter **default** for **Database name**. Choose **Create**. 

## Next steps: Create a Studio notebook with Kinesis Data Streams or Amazon MSK
<a name="examples-notebook-nextsteps"></a>

With this tutorial, you can create a Studio notebook that uses either Kinesis Data Streams or Amazon MSK:
+ [Create a Studio notebook with Kinesis Data Streams](example-notebook-streams.md) : With Kinesis Data Streams, you quickly create an application that uses a Kinesis data stream as a source. You only need to create a Kinesis data stream as a dependent resource.
+ [Create a Studio notebook with Amazon MSK](example-notebook-msk.md) : With Amazon MSK, you create an application that uses a Amazon MSK cluster as a source. You need to create an Amazon VPC, an Amazon EC2 client instance, and an Amazon MSK cluster as dependent resources.