# AWS service integrations with Athena

You can use Athena to query data from the AWS services listed in this section. To see the
Regions that each service supports, see [Regions and
endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the _Amazon Web Services General Reference_.

###### AWS services integrated with Athena

- [CloudFormation](#integ-ate-cfn "#integ-ate-cfn")
- [Amazon CloudFront](#integ-ate-cf "#integ-ate-cf")
- [AWS CloudTrail](#integ-ate-ct "#integ-ate-ct")
- [Amazon
  DataZone](#integ-ate-dz "#integ-ate-dz")
- [Elastic Load Balancing](#integ-ate-eb "#integ-ate-eb")
- [Amazon EMR
  Studio](#integ-ate-emr-studio "#integ-ate-emr-studio")
- [AWS Glue Data Catalog](#integ-ate-gc "#integ-ate-gc")
- [AWS Identity and Access Management
  (IAM)](#integ-ate-iam "#integ-ate-iam")
- [Amazon Quick](#integ-ate-qs "#integ-ate-qs")
- [Amazon S3
  Inventory](#integ-ate-s3 "#integ-ate-s3")
- [AWS Step Functions](#integ-ate-sf "#integ-ate-sf")
- [AWS Systems Manager
  Inventory](#integ-ate-sys "#integ-ate-sys")
- [Amazon Virtual Private Cloud](#integ-ate-vpc "#integ-ate-vpc")
  For information about each integration, see the following sections.

**CloudFormation**

_Capacity reservation_

Reference topic: [AWS::Athena::CapacityReservation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-athena-capacityreservation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-athena-capacityreservation.md") in the
_AWS CloudFormation User Guide_

Specifies a capacity reservation with the provided name and number
of requested data processing units. For more information, see [Manage query processing capacity](capacity-management.md "capacity-management.md") in the
_Amazon Athena User Guide_ and [CreateCapacityReservation](../APIReference/API_CreateCapacityReservation.md "../APIReference/API_CreateCapacityReservation.md") in the _Amazon Athena API Reference_.

_Data catalog_

Reference topic: [AWS::Athena::DataCatalog](../../../AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.md") in the
_AWS CloudFormation User Guide_

Specify an Athena data catalog, including a name, description,
type, parameters, and tags. For more information, see [Understanding tables, databases, and data catalogs in Athena](understanding-tables-databases-and-the-data-catalog.md "understanding-tables-databases-and-the-data-catalog.md") in the _Amazon Athena User Guide_ and [CreateDataCatalog](../APIReference/API_CreateDataCatalog.md "../APIReference/API_CreateDataCatalog.md") in the _Amazon
Athena API Reference_.

_Named query_

Reference topic: [AWS::Athena::NamedQuery](../../../AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.md") in the
_AWS CloudFormation User Guide_

Specify named queries with CloudFormation and run them in Athena. Named
queries allow you to map a query name to a query and then run it as
a saved query from the Athena console. For more information, see
[Use saved queries](saved-queries.md "saved-queries.md") in
the _Amazon Athena User Guide_ and [CreateNamedQuery](../APIReference/API_CreateNamedQuery.md "../APIReference/API_CreateNamedQuery.md") in the
_Amazon Athena API Reference_.

_Prepared statement_

Reference topic: [AWS::Athena::PreparedStatement](../../../AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.md") in the
_AWS CloudFormation User Guide_

Specifies a prepared statement for use with SQL queries in Athena.
A prepared statement contains parameter placeholders whose values
are supplied at execution time. For more information, see [Use parameterized queries](querying-with-prepared-statements.md "querying-with-prepared-statements.md") in the
_Amazon Athena User Guide_ and [CreatePreparedStatement](../APIReference/API_CreatePreparedStatement.md "../APIReference/API_CreatePreparedStatement.md") in the
_Amazon Athena API Reference_.

_Workgroup_

Reference topic: [AWS::Athena::WorkGroup](../../../AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.md") in the _CloudFormation User
Guide_

Specify Athena workgroups using AWS CloudFormation. Use Athena workgroups to
isolate queries for you or your group from other queries in the same
account. For more information, see [Use workgroups to control query access and costs](workgroups-manage-queries-control-costs.md "workgroups-manage-queries-control-costs.md")
in the _Amazon Athena User Guide_ and [CreateWorkGroup](../APIReference/API_CreateWorkGroup.md "../APIReference/API_CreateWorkGroup.md") in the _Amazon Athena API
Reference_.

**Amazon CloudFront**

Reference topic: [Query Amazon CloudFront logs](cloudfront-logs.md "cloudfront-logs.md")

Use Athena to query Amazon CloudFront logs. For more information about using CloudFront, see
the [Amazon CloudFront Developer Guide](../../../AmazonCloudFront/latest/DeveloperGuide.md "../../../AmazonCloudFront/latest/DeveloperGuide.md").

**AWS CloudTrail**

Reference topic: [Query AWS CloudTrail logs](cloudtrail-logs.md "cloudtrail-logs.md")

Using Athena with CloudTrail logs is a powerful way to enhance your analysis of AWS
service activity. For example, you can use queries to identify trends and
further isolate activity by attribute, such as source IP address or user. You
can create tables for querying logs directly from the CloudTrail console, and use
those tables to run queries in Athena. For more information, see [Use the CloudTrail console to create an Athena table for CloudTrail logs](create-cloudtrail-table-ct.md "create-cloudtrail-table-ct.md").

**Amazon DataZone**

Reference topic: [Use Amazon DataZone in Athena](datazone-using.md "datazone-using.md")

Use [Amazon DataZone](https://aws.amazon.com/datazone "https://aws.amazon.com/datazone") to share, search,
and discover data at scale across organizational boundaries. DataZone
simplifies your experience across AWS analytics services like Athena, AWS Glue,
and AWS Lake Formation. If you have large amounts of data in different data sources, you
can use Amazon DataZone to build business use case based groupings of people, data and
tools.

In Athena, you can use the query editor to access and query DataZone
environments. For more information, see [Use Amazon DataZone in Athena](datazone-using.md "datazone-using.md").

**Elastic Load Balancing**

Reference topic: [Query Application Load Balancer logs](application-load-balancer-logs.md "application-load-balancer-logs.md")

Querying Application Load Balancer logs allows you to see the source of
traffic, latency, and bytes transferred to and from Elastic Load Balancing instances and
backend applications. For more information, see [Query Application Load Balancer logs](application-load-balancer-logs.md "application-load-balancer-logs.md").

Reference topic: [Query Classic Load Balancer logs](elasticloadbalancer-classic-logs.md "elasticloadbalancer-classic-logs.md")

Query Classic Load Balancer logs to analyze and understand traffic patterns to
and from Elastic Load Balancing instances and backend applications. You can see the source of
traffic, latency, and bytes transferred. For more information, see [Query Classic Load Balancer logs](elasticloadbalancer-classic-logs.md "elasticloadbalancer-classic-logs.md").

**Amazon EMR Studio**

Reference topic: [Use the Amazon Athena
SQL editor in EMR Studio](../../../emr/latest/ManagementGuide/emr-studio-athena.md "../../../emr/latest/ManagementGuide/emr-studio-athena.md")

You can use Athena in an EMR Studio to develop and run interactive queries.
This makes it possible for you to use EMR Studio for SQL analytics on Athena
from the same Amazon EMR interface that you use for your Spark, Scala, and other
workloads. With the Athena integration in EMR Studio, you can perform the
following tasks:

- Perform Athena SQL queries
- View query results
- View query history
- View saved queries
- Perform parameterized queries
- View databases, tables, and views for a data catalog

The following Athena features are not available in Amazon EMR Studio:

- Admin features like creating or updating Athena workgroups, data
  sources, or capacity reservations
- Athena for Spark or Spark notebooks
- DataZone integration
- Step Functions

EMR Studio integration with Athena is available in all AWS Regions where
EMR Studio and Athena are available. For more information about using Athena
in EMR Studio, see [Use the Amazon Athena
SQL editor in EMR Studio](../../../emr/latest/ManagementGuide/emr-studio-athena.md "../../../emr/latest/ManagementGuide/emr-studio-athena.md") in the
_Amazon EMR Management Guide_.

**AWS Glue Data Catalog**

Reference topic: [Use AWS Glue Data Catalog to connect to your data](data-sources-glue.md "data-sources-glue.md")

Athena integrates with the AWS Glue Data Catalog, which offers a persistent metadata
store for your data in Amazon S3. This allows you to create tables and query data in
Athena based on a central metadata store available throughout your Amazon Web Services
account and integrated with the ETL and data discovery features of AWS Glue.
For more information, see [Use AWS Glue Data Catalog to connect to your data](data-sources-glue.md "data-sources-glue.md") and [What is AWS Glue](../../../glue/latest/dg/what-is-glue.md "../../../glue/latest/dg/what-is-glue.md") in the
_AWS Glue Developer Guide_.

**AWS Identity and Access Management (IAM)**

Reference topic: [Actions for
Amazon Athena](../../../IAM/latest/UserGuide/list_amazonathena.md "../../../IAM/latest/UserGuide/list_amazonathena.md")

You can use Athena API actions in IAM permission policies. For more
information, see [Actions for
Amazon Athena](../../../IAM/latest/UserGuide/list_amazonathena.md "../../../IAM/latest/UserGuide/list_amazonathena.md") and [Identity and access management in Athena](security-iam-athena.md "security-iam-athena.md").

**Amazon Quick**

Reference topic: [Connect to Amazon Athena with ODBC and JDBC drivers](athena-bi-tools-jdbc-odbc.md "athena-bi-tools-jdbc-odbc.md")

Athena integrates with Amazon Quick for easy data visualization. You can use Athena
to generate reports or to explore data with business intelligence tools or SQL
clients connected with a JDBC or an ODBC driver. For more information about
Quick, see [What
is Amazon Quick](../../../quicksight/latest/user/welcome.md "../../../quicksight/latest/user/welcome.md") in the _Amazon Quick User Guide_. For
information about using JDBC and ODBC drivers with Athena, see [Connecting to Amazon Athena with ODBC and
JDBC Drivers](athena-bi-tools-jdbc-odbc.md "athena-bi-tools-jdbc-odbc.md").

**Amazon S3 Inventory**

Reference topic: [Querying inventory with Athena](../../../AmazonS3/latest/dev/storage-inventory.md#storage-inventory-athena-query "../../../AmazonS3/latest/dev/storage-inventory.md#storage-inventory-athena-query") in the _Amazon Simple Storage Service User Guide_

You can use Amazon Athena to query Amazon S3 inventory using standard SQL. You can use
Amazon S3 inventory to audit and report on the replication and encryption status of
your objects for business, compliance, and regulatory needs. For more
information, see [Amazon S3 inventory](../../../AmazonS3/latest/dev/storage-inventory.md "../../../AmazonS3/latest/dev/storage-inventory.md") in
the _Amazon Simple Storage Service User Guide_.

**AWS Step Functions**

Reference topic: [Call Athena with
Step Functions](../../../step-functions/latest/dg/connect-athena.md "../../../step-functions/latest/dg/connect-athena.md") in the _AWS Step Functions Developer Guide_

Call Athena with AWS Step Functions. AWS Step Functions can control select AWS services
directly using the [Amazon States Language](../../../step-functions/latest/dg/concepts-amazon-states-language.md "../../../step-functions/latest/dg/concepts-amazon-states-language.md"). You can use Step Functions with Athena to start and stop query
execution, get query results, run ad-hoc or scheduled data queries, and retrieve
results from data lakes in Amazon S3. The Step Functions role must have permissions to use
Athena. For more information, see the [AWS Step Functions Developer Guide](../../../step-functions/latest/dg.md "../../../step-functions/latest/dg.md").

###### Video: Orchestrate Amazon Athena Queries using AWS Step Functions

The following video demonstrates how to use Amazon Athena and AWS Step Functions to run
a regularly scheduled Athena query and generate a corresponding
report.

For an example that uses Step Functions and Amazon EventBridge to orchestrate AWS Glue DataBrew, Athena,
and Amazon Quick, see [Orchestrating an AWS Glue DataBrew job and Amazon Athena query with AWS Step Functions](https://aws.amazon.com/blogs/big-data/orchestrating-an-aws-glue-databrew-job-and-amazon-athena-query-with-aws-step-functions/ "https://aws.amazon.com/blogs/big-data/orchestrating-an-aws-glue-databrew-job-and-amazon-athena-query-with-aws-step-functions/")
in the AWS Big Data Blog.

**AWS Systems Manager Inventory**

Reference topic: [Querying inventory data from multiple regions and accounts](../../../systems-manager/latest/userguide/systems-manager-inventory-query.md "../../../systems-manager/latest/userguide/systems-manager-inventory-query.md") in the
_AWS Systems Manager User Guide_

AWS Systems Manager Inventory integrates with Amazon Athena to help you query inventory data
from multiple AWS Regions and accounts. For more information, see the
[AWS Systems Manager User Guide](../../../systems-manager/latest/userguide.md "../../../systems-manager/latest/userguide.md").

**Amazon Virtual Private Cloud**

Reference topic: [Query Amazon VPC flow logs](vpc-flow-logs.md "vpc-flow-logs.md")

Amazon Virtual Private Cloud flow logs capture information about the IP traffic going to and from
network interfaces in a VPC. Query the logs in Athena to investigate network
traffic patterns and identify threats and risks across your Amazon VPC network. For
more information about Amazon VPC, see the [Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md").
