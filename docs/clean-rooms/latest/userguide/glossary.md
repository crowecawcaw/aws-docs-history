# AWS Clean Rooms Glossary

Consult this glossary to become familiar with terminology that is used for AWS Clean Rooms.

## Aggregation analysis rule

The query restriction that allows queries that aggregate analysis using
COUNT, SUM, or AVG functions along optional
dimensions. These queries won't reveal row-level information.

Supports use cases such as campaign planning, media reach, frequency, and conversion
measurement.

Other types of analysis rules are [custom](#glossary-custom-analysis-rule "#glossary-custom-analysis-rule") and [list](#glossary-list-analysis-rule "#glossary-list-analysis-rule").

## Analysis rules

The query restrictions that authorize a specific type of query.

The analysis rule type determines what kind of analysis can be run on the configured
table. Each type has a predefined query structure. You control how your table columns can be
used in the structure through the query controls.

The types of analysis rules are [aggregation](#glossary-agg-analysis-rule "#glossary-agg-analysis-rule"), [list](#glossary-list-analysis-rule "#glossary-list-analysis-rule"), and [custom](#glossary-custom-analysis-rule "#glossary-custom-analysis-rule").

## Analysis template

A collaboration-specific, pre-approved query that can be reused.

Supported formats: SQL code or Python code for Spark.

If using SQL, the analysis template can contain parameters wherever a literal value could
typically appear in a SQL query. For more information about supported parameter types, see
[Data types](../sql-reference/c_Supported_data_types.md "../sql-reference/c_Supported_data_types.md") in the
_AWS Clean Rooms SQL Reference_.

Analysis templates only work with the [custom analysis rule](analysis-rules-custom.md "analysis-rules-custom.md").

## AWS Clean Rooms SQL analytics engine

A built-in query processing system within AWS Clean Rooms that allows users to query data stored in
Amazon S3 using SQL functions supported by AWS Clean Rooms. It supports various data formats and provides
capabilities for running SQL queries on collaborative datasets while maintaining data privacy
and control, including features like differential privacy. This engine is tailored for AWS Clean Rooms
use cases, offering a balance of SQL functionality, data privacy features, and integration
with other AWS Clean Rooms capabilities, making it suitable for users who don't require the advanced
capabilities or scale of the [Spark SQL
analytics engine](#glossary-spark-analytics-engine "#glossary-spark-analytics-engine").

When you create a collaboration using the [CreateCollaboration
API](../apireference/API_CreateCollaboration.md "../apireference/API_CreateCollaboration.md"), the value of the AWS Clean Rooms SQL analytics engine is
`CLEAN_ROOMS_SQL`.

## C3R encryption client

The Cryptographic Computing for Clean Rooms (C3R) encryption client.

Used to encrypt and decrypt data, C3R is a client-side encryption SDK with a
command line interface.

## Cleartext column

A column that isn't cryptographically protected for either a JOIN or
SELECT SQL construct.

Cleartext columns can be used in any part of the SQL query.

## Collaboration

A secure logical boundary in AWS Clean Rooms in which members can perform SQL queries on
configured tables.

Collaborations are created by the [collaboration creator](#glossary-collaboration-creator "#glossary-collaboration-creator").

Only members who have been invited to the collaboration can join the collaboration.

A collaboration can have only one [member who can query](#glossary-member-who-can-query "#glossary-member-who-can-query") data or one [member who can run queries and
jobs](#glossary-member-who-can-run-queries-jobs "#glossary-member-who-can-run-queries-jobs").

A collaboration can have only one [member who can receive
results](#glossary-member-who-can-receive-results "#glossary-member-who-can-receive-results").

A collaboration can have only one [member paying for query compute
costs](#glossary-member-paying-for-query-compute "#glossary-member-paying-for-query-compute") or one [member paying for query and job
compute costs](#glossary-member-paying-for-query-job-compute "#glossary-member-paying-for-query-job-compute").

All members can see the list of invited participants in the collaboration before they join
the collaboration.

## Collaboration creator

The member who creates a collaboration.

There is only one collaboration creator per collaboration.

Only the collaboration creator can remove members from the collaboration or delete the
collaboration.

## Configured table

Each configured table represents a reference to an existing table in the AWS Glue Data Catalog that
has been configured for use in AWS Clean Rooms. A configured table contains an analysis rule that
determines how the data can be used.

Currently, AWS Clean Rooms supports associating data stored in Amazon Simple Storage Service (Amazon S3) that is cataloged
through AWS Glue.

For more information about AWS Glue, see the [AWS Glue Developer
Guide](../../../glue/latest/dg/what-is-glue.md "../../../glue/latest/dg/what-is-glue.md").

Configured tables can be associated to one or more collaborations.

###### Note

AWS Clean Rooms doesn't currently support Amazon S3 bucket locations that are registered with
AWS Lake Formation.

## Custom analysis rule

The query restriction that allows a specific set of pre-approved queries ([analysis
templates](#glossary-analysis-template "#glossary-analysis-template")) or allows a specific set of accounts that can provide queries or jobs that
use your data.

Supports use cases such as first-touch attribution, incremental analyses, and audience
discovery analyses.

Supports differential privacy.

Other types of analysis rules are [aggregation](#glossary-agg-analysis-rule "#glossary-agg-analysis-rule") and [list](#glossary-list-analysis-rule "#glossary-list-analysis-rule").

## Decryption

The process of transforming encrypted data back to its original form. Decryption can only
be performed if you have access to the secret key.

## Differential privacy

A mathematically-rigorous technique that protects the collaboration data from the member
who can receive results learning about a specific individual.

## Encryption

The process of encoding data into a form that appears random using a secret value called a
key. It's impossible to determine the original plaintext without access to the key.

## Fingerprint column

A column that is cryptographically protected for a JOIN SQL
construct.

## ID mapping workflow method

How you want the ID mapping to be performed.

There are two ID mapping workflow methods:

- Rule-based ID mapping – The method by which you use matching rules to translate
  first-party data from a source to a target in an ID mapping workflow.
- Provider services ID mapping – The method by which you use a provider service
  to translate third party-encoded data from a source to a target in an ID mapping
  workflow.

AWS Clean Rooms currently supports LiveRamp as the provider services-based ID mapping workflow
method. You must have a subscription to LiveRamp through AWS Data Exchange to use this method. For
more information, see [Subscribe to a provider service on AWS Data Exchange](../../../entityresolution/latest/userguide/prepare-third-party-input-data.md#subscribe-provider-service "../../../entityresolution/latest/userguide/prepare-third-party-input-data.md#subscribe-provider-service") in the _AWS Entity Resolution User Guide._

## ID mapping table

A resource in AWS Clean Rooms that enables either first-party matching rules or multi-party identity
transcoding in a collaboration.

A ID mapping table is a reference to an existing table in the AWS Glue Data Catalog. It contains an
[ID mapping table analysis
rule](#glossary-id-mapping-table-analysis-rule "#glossary-id-mapping-table-analysis-rule") that determines how the data can be queried in AWS Clean Rooms. ID mapping tables can be
associated to one or more collaborations.

## ID mapping table analysis

rule

A type of analysis rule managed by AWS Clean Rooms and used to join disparate identity
data to facilitate querying. It's automatically added to [ID mapping
tables](#glossary-id-mapping-table "#glossary-id-mapping-table") and can't be edited. It inherits the behaviors of the other analysis rules in
the collaboration – as long as those analysis rules are homogeneous.

## ID mapping workflow

A data processing job that maps data from a source to a target based on the specified
[ID
mapping workflow method](#glossary-id-mapping-method "#glossary-id-mapping-method"). It produces an [ID mapping table](#glossary-id-mapping-table "#glossary-id-mapping-table").

## ID namespace

A resource in AWS Clean Rooms that contains metadata explaining datasets across multiple
AWS accounts and how to use these datasets in an [ID
mapping workflow](#glossary-id-mapping-workflow "#glossary-id-mapping-workflow").

## ID namespace association

An association of an ID namespace resource that helps you discover inputs into their [ID
mapping workflow](#glossary-id-mapping-workflow "#glossary-id-mapping-workflow").

## Job

A method to access and analyze configured tables in a collaboration using a supported set
of functions, classes, and variables.

AWS Clean Rooms currently supports the PySpark job type.

AWS Clean Rooms currently supports running jobs using a PySpark analysis template.

## List analysis rule

The query restriction that allows queries that output row-level attribute analysis of the
overlap between this table and the tables of the member who can query.

Supports use cases such as enrichment and audience building or suppression.

Other types of analysis rules are [aggregation](#glossary-agg-analysis-rule "#glossary-agg-analysis-rule") and [custom](#glossary-custom-analysis-rule "#glossary-custom-analysis-rule").

## Lookalike model

A model of a training data provider's data that allows a seed data provider to create a
[lookalike segment](#glossary-lookalike-segment "#glossary-lookalike-segment") of training data provider's data that most closely resembles their
[seed data](#glossary-seed-data "#glossary-seed-data").

## Lookalike segment

A subset of the training data that most closely resembles the [seed data](#glossary-seed-data "#glossary-seed-data").

## Member

An AWS customer who is a participant in a [collaboration](#glossary-collaboration "#glossary-collaboration").

A member is identified using their AWS account.

All members can contribute data.

## Member who can query

The member who can query data in the [collaboration](#glossary-collaboration "#glossary-collaboration").

There is only one member who can query per collaboration, and that member is
immutable.

An administrative user can use AWS Identity and Access Management (IAM) permissions to control which of their
IAM principals (such as users or roles) can query data in the collaboration. For more
information, see [Create a service role to read data
from Amazon S3](setting-up-roles.md#create-service-role-procedure "setting-up-roles.md#create-service-role-procedure").

## Member who can run queries and

jobs

The member who can run queries and jobs on the data in the [collaboration](#glossary-collaboration "#glossary-collaboration").

There is only one member who can run queries and jobs per collaboration, and that member
is immutable.

An administrative user can use AWS Identity and Access Management (IAM) permissions to control which of their
IAM principals (such as users or roles) can run queries and jobs in the collaboration. For
more information, see [Create a service role to read data
from Amazon S3](setting-up-roles.md#create-service-role-procedure "setting-up-roles.md#create-service-role-procedure").

## Member who can receive

results

A member who can receive query results. A member who can receive results specifies query
results settings for the Amazon S3 destination and the query result format (CSV or Parquet).

For analyses with the Spark analytics engine, a member who can receive results also
specifies whether files should be output as a single file or as multiple files.

There can be more than one member who can receive results in a collaboration.

## Member paying for query compute

costs

The member who is responsible for paying for query compute costs.

There is only one member who is responsible for paying for query compute costs per
collaboration, and that member is immutable.

If the collaboration creator hasn't specified anyone as the member paying for query
compute costs, then the [member who can query](#glossary-member-who-can-query "#glossary-member-who-can-query") is the default
payer.

The member paying for query compute costs receives a bill for the queries that have been
run in the collaboration.

## Member paying for query and job

compute costs

The member who is responsible for paying for query and job compute costs.

There is only one member who is responsible for paying for query and job compute costs per
collaboration, and that member is immutable.

If the collaboration creator hasn't specified anyone as the member paying for query and
job compute costs, then the [member who can query](#glossary-member-who-can-query "#glossary-member-who-can-query") is the default
payer.

The member paying for query and job compute costs receives a bill for the queries that
have been run in the collaboration.

## Membership

A resource created when a [member](#glossary-member "#glossary-member") joins a [collaboration](#glossary-collaboration "#glossary-collaboration").

All resources that the member associates to a collaboration are a part of the membership
or are associated with the membership.

Only the member that owns the membership can add, remove, or edit resources in that
membership.

## Sealed column

A column that is cryptographically protected for a SELECT SQL
construct.

## Seed data

The seed data provider's data, which is used to create a [lookalike
segment](#glossary-lookalike-segment "#glossary-lookalike-segment"). The seed data can be provided directly or it can come from the results of an
AWS Clean Rooms query. The lookalike segment output is a set of users from the training data that most
closely resembles the seed users.

## Spark analytics engine

An analytics option in AWS Clean Rooms that enables customers to run complex queries on large
datasets stored in Amazon S3, Amazon Athena, or Snowflake using Apache Spark SQL functions. It serves
as an alternative to the [AWS Clean Rooms SQL
analytics engine](#glossary-clean-rooms-sql-analytics-engine "#glossary-clean-rooms-sql-analytics-engine"), and also supports PySpark analysis in AWS Clean Rooms.

When you create a collaboration using the [CreateCollaboration
API](../apireference/API_CreateCollaboration.md "../apireference/API_CreateCollaboration.md"), the value of the Spark analytics engine is `SPARK`.

## Query

A method to access and analyze configured tables in a collaboration, using a supported set
of functions, classes, and variables.

AWS Clean Rooms currently supports the SQL query language.

AWS Clean Rooms currently supports running direct SQL queries or running queries using a SQL
analysis template.
