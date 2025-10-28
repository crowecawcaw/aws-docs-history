# PySpark analysis templates

PySpark analysis templates require a Python user script and an optional virtual
environment to use custom and open-source libraries. These files are called artifacts.

Before you create an analysis template, you first create the artifacts and then store the
artifacts in an Amazon S3 bucket. AWS Clean Rooms uses these artifacts when running analysis jobs. AWS Clean Rooms only
accesses the artifacts when running a job.

Before running any code on a PySpark analysis template, AWS Clean Rooms validates artifacts by:

- Checking the specific S3 object version used when creating the template
- Verifying the SHA-256 hash of the artifact
- Failing any job where artifacts have been modified or removed

###### Note

The maximum size of all combined artifacts for a given PySpark analysis template in
AWS Clean Rooms is 1 GB.

## Security for PySpark analysis

templates

To preserve a secure compute environment, AWS Clean Rooms uses a two-tier compute architecture to
isolate user code from system operations. This architecture is based on Amazon EMR Serverless
Fine Grained Access Control technology, also know as Membrane. For more information, see
[Membrane – Safe and performant data access controls in Apache Spark in the presence of
imperative code](https://www.amazon.science/publications/membrane-safe-and-performant-data-access-controls-in-apache-spark-in-the-presence-of-imperative-code "https://www.amazon.science/publications/membrane-safe-and-performant-data-access-controls-in-apache-spark-in-the-presence-of-imperative-code").

The compute environment components are divided into a separate user space and system
space. The user space executes the PySpark code in the PySpark analysis template. AWS Clean Rooms uses
the system space to enable the job to run including using service roles provided by
customers to read data to run the job and implementing the column allowlist. As a result of
this architecture, a customer’s PySpark code that affects the system space, which could
include small number of Spark SQL and PySpark DataFrames APIs, is blocked.

## PySpark limitations in AWS Clean Rooms

When customers submit an approved PySpark analysis template, AWS Clean Rooms runs it on its own
secure compute environment which no customer can access. The compute environment implements
a compute architecture with a user space and system space to preserve a secure compute
environment. For more information, see [Security for PySpark analysis
templates](#pyspark-analysis-templates-security "#pyspark-analysis-templates-security").

Consider the following limitations before you use PySpark in AWS Clean Rooms.

**Limitations**

- Only DataFrame outputs are supported
- Single Spark session per job execution

**Unsupported features**

- **Data management**
  - Iceberg table formats
  - LakeFormation managed tables
  - Resilient distributed datasets (RDD)
  - Spark streaming
  - Access control for nested columns

- **Custom functions and extensions**
  - User-defined table functions (UDTFs)
  - HiveUDFs
  - Custom classes in user-defined functions
  - Custom data sources
  - Additional JAR files for:
    - Spark extensions
    - Connectors
    - Metastore configurations

- **Monitoring and analysis**
  - Spark logging
  - Spark UI
  - `ANALYZE TABLE` commands

###### Important

These limitations are in place to maintain the security isolation between user and
system spaces.

All restrictions apply regardless of collaboration configuration.

Future updates may add support for additional features based on security
evaluations.

## Best practices

We recommend the following best practices when creating PySpark analysis
templates.

- Design your analysis templates with the [PySpark limitations in AWS Clean Rooms](#pyspark-limitations "#pyspark-limitations") in mind.
- Test your code in a development environment first.
- Use supported DataFrame operations exclusively.
- Plan your output structure to work with DataFrame limitations.

We recommend the following best practices for managing artifacts

- Keep all PySpark analysis template artifacts in a dedicated S3 bucket or
  prefix.
- Use clear version naming for different artifact versions.
- Create new analysis templates when artifact updates are needed.
- Maintain an inventory of which templates use which artifact versions.

For more information about how to write Spark code, see the following:

- [Apache Spark
  Examples](https://spark.apache.org/examples.html "https://spark.apache.org/examples.html")
- [Write a Spark application](../../../emr/latest/ReleaseGuide/emr-spark-application.md "../../../emr/latest/ReleaseGuide/emr-spark-application.md") in the _Amazon EMR Release
  Guide_
- [Tutorial: Writing an AWS Glue for Spark script](../../../glue/latest/dg/aws-glue-programming-intro-tutorial.md "../../../glue/latest/dg/aws-glue-programming-intro-tutorial.md") in the _AWS Glue User Guide_
  The following topics explain how to create Python user scripts and libraries before
  creating and reviewing the analysis template.

###### Topics

- [Creating a user script](create-user-script.md "create-user-script.md")
- [Creating a virtual environment
  (optional)](create-virtual-environment.md "create-virtual-environment.md")
- [Storing a user script and virtual environment in
  S3](store-artifacts-in-s3.md "store-artifacts-in-s3.md")
- [Creating a PySpark analysis
  template](create-pyspark-analysis-template.md "create-pyspark-analysis-template.md")
- [Reviewing a PySpark analysis
  template](review-pyspark-analysis-template.md "review-pyspark-analysis-template.md")
