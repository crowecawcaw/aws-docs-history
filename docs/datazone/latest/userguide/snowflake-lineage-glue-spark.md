# Enable Snowflake lineage for AWS Glue Spark jobs

Amazon DataZone can capture column-level lineage from AWS Glue Spark jobs that read from or write
to a Snowflake data source. When you enable lineage on the AWS Glue job, the AWS Glue Spark
runtime emits lineage events as the job runs and Amazon SageMaker Unified Studio renders them in the lineage
view.

AWS Glue's Spark runtime already includes the OpenLineage Spark and Amazon DataZone integrations
that it uses to send events. The only additional step is to upgrade the OpenLineage core
client (`openlineage-java`) on the job to version
`1.49.0`.

## Prerequisites

Before you enable lineage on a AWS Glue Spark job, confirm the following:

- A Amazon DataZone domain and project with a Snowflake connection already
  configured. See [Connect Snowflake as a data source in Amazon DataZone](snowflake-data-source.md "snowflake-data-source.md").
- A AWS Glue Spark job that reads from or writes to the connected Snowflake
  source.
- Permission to modify the AWS Glue job's configuration.
- An Amazon S3 bucket that the AWS Glue job can read.

The following steps describe how to upgrade the OpenLineage core client on the
AWS Glue job and enable lineage event generation.

## Step 1: Upgrade the OpenLineage core client on the AWS Glue job

The AWS Glue Spark runtime bundles the OpenLineage Spark integration and the Amazon DataZone
integration. To make it compatible with Amazon DataZone, upgrade the
`openlineage-java` client on the job to version
`1.49.0`.

1. Download `openlineage-java-1.49.0.jar` from Maven Central. Use
   either:

   - [The Maven Repository page](https://mvnrepository.com/artifact/io.openlineage/openlineage-java/1.49.0 "https://mvnrepository.com/artifact/io.openlineage/openlineage-java/1.49.0").
     Choose **jar** to download.
   - [The direct Maven URL](https://repo1.maven.org/maven2/io/openlineage/openlineage-java/1.49.0/ "https://repo1.maven.org/maven2/io/openlineage/openlineage-java/1.49.0/").

2. Upload the JAR to an Amazon S3 bucket that your AWS Glue job can read.
3. In the AWS Glue console, open the job and choose **Job
   details**. Under **Advanced
   properties**, find **Dependent JARs
   path** and add the S3 URI of the uploaded JAR.
4. Still in **Job details**, add the following job
   parameter:

| Key                 | Value  |
| ------------------- | ------ |
| `--user-jars-first` | `true` |

This makes the AWS Glue Spark runtime load your uploaded
`openlineage-java` client instead of the version bundled with
AWS Glue.

## Step 2: Enable lineage event generation on the AWS Glue job

1. In the AWS Glue console, open the job and choose **Job
   details** → **Basic
   properties**.
2. Select **Generate lineage events**.
3. Enter your Amazon DataZone **Domain ID** in the field
   that appears. Use the same Domain ID you used when creating the Snowflake
   connection.
4. Save the job.

## Verify lineage is captured

Run the AWS Glue job. After the job completes, open the lineage view in Amazon SageMaker Unified Studio for
the target table in your project. Lineage records for the Snowflake sources read by the
job appear as upstream nodes in the graph.
