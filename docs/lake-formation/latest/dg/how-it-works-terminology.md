# Lake Formation terminology

The following are some important terms that you will encounter in this guide.

## Data lake

The _data lake_ is your persistent data that is stored in Amazon S3 and
managed by Lake Formation using a Data Catalog. A data lake typically stores the following:

- Structured and unstructured data
- Raw data and transformed data

For an Amazon S3 path to be within a data lake, it must be _registered_ with Lake Formation.

## Data access

Lake Formation provides secure and granular access to data through a new grant/revoke
permissions model that augments AWS Identity and Access Management (IAM) policies.

Analysts and data scientists can use the full portfolio of AWS analytic and
machine learning services, such as Amazon Athena, to access the data. The configured
Lake Formation security policies help ensure that users can access only the data that they are
authorized to access.

## Hybrid access mode

Hybrid access mode lets you secure and access the cataloged data using both Lake Formation permissions and IAM and Amazon S3 permissions.
Hybrid access mode allows data administrators to onboard Lake Formation permissions selectively and incrementally, focusing on one data lake use case at a time.

## Blueprint

A _blueprint_ is a data management template that enables you to
easily ingest data into a data lake. Lake Formation provides several blueprints, each for a
predefined source type, such as a relational database or AWS CloudTrail logs. From a
blueprint, you can create a workflow. Workflows consist of AWS Glue crawlers, jobs,
and triggers that are generated to orchestrate the loading and update of data.
Blueprints take the data source, data target, and schedule as input to configure the
workflow.

## Workflow

A _workflow_ is a container for a set of related AWS Glue jobs,
crawlers, and triggers. You create the workflow in Lake Formation, and it executes in the
AWS Glue service. Lake Formation can track the status of a workflow as a single entity.

When you define a workflow, you select the blueprint upon which it is based. You
can then run workflows on demand or on a schedule.

Workflows that you create in Lake Formation are visible in the AWS Glue console as a directed
acyclic graph (DAG). Using the DAG, you can track the progress of the workflow and
perform troubleshooting.

## Data Catalog

The _Data Catalog_ is your persistent metadata store. It is a
managed service that lets you store, annotate, and share metadata in the AWS Cloud
in the same way you would in an Apache Hive metastore. It provides a uniform
repository where disparate systems can store and find metadata to track data in data
silos, and then use that metadata to query and transform the data. Lake Formation uses the
AWS Glue Data Catalog to store metadata about data lakes, data sources, transforms, and
targets.

Metadata about data sources and targets is in the form of databases and tables.
Tables store schema information, location information, and more. Databases are
collections of tables. Lake Formation provides a hierarchy of permissions to control access to
databases and tables in the Data Catalog.

Each AWS account has one Data Catalog per AWS Region.

## Underlying data

_Underlying data_ refers to the source data or
data within the data lakes that Data Catalog tables point to.

## Principal

A _principal_ is an AWS Identity and Access Management (IAM) user or
role or an Active Directory user.

## Data lake administrator

A _data lake administrator_ is a principal who
can grant any principal (including self) any permission on any Data Catalog resource or
data location. Designate a data lake administrator as the first user of the Data Catalog.
This user can then grant more granular permissions of resources to other
principals.

###### Note

IAM administrative users—users with the `AdministratorAccess` AWS
managed policy—are not automatically data lake administrators. For example, they
can't grant Lake Formation permissions on catalog objects unless they have been granted
permissions to do so. However, they can use the Lake Formation console or API to designate
themselves as data lake administrators.

For information about the capabilities of a data lake administrator, see [Implicit Lake Formation permissions](implicit-permissions.md "implicit-permissions.md"). For
information about designating a user as a data lake administrator, see [Create a data lake administrator](initial-lf-config.md#create-data-lake-admin "initial-lf-config.md#create-data-lake-admin").
