AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Copy Data to Amazon Redshift Using AWS Data Pipeline

This tutorial walks you through the process of creating a pipeline that periodically moves data from Amazon S3 to Amazon Redshift
using either the **Copy to Redshift** template in the AWS Data Pipeline console,
or a pipeline definition file with the AWS Data Pipeline CLI.

Amazon S3 is a web service that enables you to store data in the cloud. For more information,
see the [Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md").

Amazon Redshift is a data warehouse service in the cloud. For more information, see the
[Amazon Redshift Management Guide](../../../redshift/latest/mgmt.md "../../../redshift/latest/mgmt.md").

This tutorial has several prerequisites. After completing the following steps, you can
continue the tutorial using either the console or the CLI.

###### Contents

- [Before You Begin: Configure COPY Options and Load
  Data](dp-learn-copy-redshift.md "dp-learn-copy-redshift.md")
- [Set up Pipeline, Create a Security Group, and
  Create an Amazon Redshift Cluster](dp-copydata-redshift-prereq.md "dp-copydata-redshift-prereq.md")
- [Copy Data to Amazon Redshift Using the Command Line](dp-copydata-redshift-cli.md "dp-copydata-redshift-cli.md")
