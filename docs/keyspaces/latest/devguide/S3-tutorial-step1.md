

# Step 1: Bootstrap the infrastructure and AWS Glue jobs
<a name="S3-tutorial-step1"></a>

In this step, you use the `keyspaces-bulk-cli` CLI to create and configure all the AWS resources required for the automated data export of an Amazon Keyspaces table to an Amazon S3 bucket using AWS Glue. The `bootstrap` command performs all setup tasks in a single step.

The `bootstrap` command automates the following tasks.

1. Creates an **Amazon S3 bucket** and an **IAM service role** using CloudFormation.

1. Downloads the [Apache Spark Cassandra Connector](https://repo1.maven.org/maven2/com/datastax/spark/), the [SigV4 Authentication plugin](https://repo1.maven.org/maven2/software/aws/mcs/aws-sigv4-auth-cassandra-java-driver-plugin/), and the [Apache Spark Extensions](https://repo1.maven.org/maven2/uk/co/gresearch/spark/).

1. Downloads and builds the [Keyspaces Retry Policy](https://github.com/aws-samples/amazon-keyspaces-java-driver-helpers) helper using Maven.

1. Uploads all JAR files and the `keyspaces-application.conf` configuration file to the Amazon S3 bucket.

1. Deploys three AWS Glue jobs: export (export a table to Amazon S3), import (import data from Amazon S3 into a table), and count (count rows in a table).

1. Saves the stack configuration to a local `.keyspaces-bulk-cli.json` file for use by subsequent commands.

**To bootstrap the infrastructure and AWS Glue jobs**

1. Clone the files from the [aws-glue](https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/scala/datastax-v4/aws-glue) repository on GitHub to your local machine.

   ```
   $ git clone https://github.com/aws-samples/amazon-keyspaces-examples.git
   $ cd amazon-keyspaces-examples/scala/datastax-v4/aws-glue
   ```

1. Run the `bootstrap` command. The following example uses the default stack name `aksglue` and specifies the keyspace and table as defaults for the deployed jobs. You can override these values when running individual commands such as `export`, `import`, or `count`.

   ```
   $ ./keyspaces-bulk-cli bootstrap --stack {{aksglue}} --keyspace {{catalog}} --table {{book_awards}}
   ```

   The following table describes the optional parameters you can pass to customize the bootstrap.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/keyspaces/latest/devguide/S3-tutorial-step1.html)

   To confirm that the Amazon S3 bucket created by bootstrap exists, you can use the following AWS CLI command. Replace {{YOURACCOUNTID}} with your AWS account ID.

   ```
   $ aws s3 ls s3://amazon-keyspaces-bulk-cli-{{aksglue}}-{{YOURACCOUNTID}}
   ```

   The output of the command looks similar to the following:

   ```
                              PRE conf/
                              PRE jars/
                              PRE scripts/
   ```

   To confirm that the AWS Glue export job was deployed, you can use the following command.

   ```
   $ aws glue list-jobs
   ```

   The output lists the deployed jobs:

   ```
   {
       "JobNames": [
           "AmazonKeyspacesExportToS3-aksglue",
           "AmazonKeyspacesImportFromS3-aksglue",
           "AmazonKeyspacesCount-aksglue"
       ]
   }
   ```

If the CloudFormation stack process fails, you can review the detailed error information about the failed stack in the CloudFormation console. To retry, delete the failed stack using `aws cloudformation delete-stack --stack-name {{aksglue}}`, fix the underlying issue, and run the bootstrap command again. The bootstrap command is idempotent and skips resources that already exist.

After the bootstrap completes and all resources are created, proceed to [Step 2: Run the export job](S3-tutorial-step2.md).