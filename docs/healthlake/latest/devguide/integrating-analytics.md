

# Analyzing HealthLake data

HealthLake stores each data store's FHIR data as Apache Iceberg tables, one for each resource type, and keeps them current. Lake Formation governs access to these tables, so any engine you authorize reads the same data in place, without exports or copies.

## How analytics access works
<a name="integrating-analytics-how-it-works"></a>

HealthLake keeps one Apache Iceberg table for each FHIR resource type and keeps it current. HealthLake owns the tables in a HealthLake service account and shares each data store into your account as an AWS Glue resource link. Lake Formation grants on the resource link and the tables decide who can read what. Every engine reads the tables in place, read-only.

![HealthLake keeps an Apache Iceberg table for each FHIR resource type current as the FHIR data store changes. HealthLake shares the tables into your AWS account as an AWS Glue resource link, and AWS Lake Formation grants on the resource link and tables control access. AWS analytics services, including Amazon Athena, Amazon Redshift Spectrum, and Apache Spark on Amazon EMR, read the tables through Lake Formation. Databricks, through the HealthLake OpenSharing server, and Snowflake, through an AWS Glue Iceberg REST catalog integration, use an IAM role. Spark on Amazon EMR, Databricks, and Snowflake also need full table access.](https://docs.aws.amazon.com/healthlake/latest/devguide/images/healthlake-analytics-overview.png)


### How each engine reads the tables
<a name="integrating-analytics-how-it-works-modes"></a>

AWS analytics services and third-party platforms get table credentials differently, and they need different setup.


**How each engine reads the tables**  

| Engine | How it gets credentials | What you set up | 
| --- | --- | --- | 
| Amazon Athena and Amazon Redshift Spectrum | Lake Formation integration for the user or role that runs the query | Grants | 
| Spark on Amazon EMR | Lake Formation-enabled Iceberg catalog, using the job's runtime role | Grants, full table access, runtime role | 
| Databricks | The HealthLake OpenSharing server assumes an IAM role through OIDC | Grants, full table access, IAM role | 
| Snowflake | The catalog integration assumes an IAM role with an external ID through the AWS Glue Iceberg REST endpoint | Grants, full table access, IAM role | 

### Key terms
<a name="integrating-analytics-how-it-works-terms"></a>

The following terms apply to analytics access:

Resource link  
An AWS Glue database in your account that points to a HealthLake data store's tables. HealthLake creates a resource link whose name ends in `_healthlake_view`, for example `{{data-store-name}}_{{data-store-id}}_healthlake_view`.

Target database  
The database in the HealthLake service account that the resource link points to. It holds one table for each FHIR resource type.

HealthLake service account  
The AWS account that HealthLake uses to own and share the tables. It isn't part of your AWS Organizations organization.

Credential vending  
The way Lake Formation returns temporary, table-scoped, read-only credentials for a query instead of granting direct access to the underlying files.

Full table access  
An account- and Region-wide Lake Formation setting for external engines, such as Spark on Amazon EMR, Databricks, and Snowflake. It lets them request credentials for tables on which they have full table access.

## Understanding the analytics tables
<a name="integrating-analytics-tables"></a>

The following sections describe the table structure, resource versions, and data freshness that apply to every engine.

### Table structure
<a name="integrating-analytics-tables-structure"></a>

HealthLake exposes one table for each FHIR resource type, with lowercase names, for example `patient` and `observation`. Nested elements, such as arrays and structs, follow FHIR cardinality, and `extension` is stored as an array of JSON strings.

Each element follows the cardinality that the FHIR specification defines. For example, consider some elements in [Resource type: Patient](https://hl7.org/fhir/R4/patient.html).
+ An element with cardinality `0..*` is an array, for example `Patient.name`.

  ```
  [{
  	id = null,
  	extension = null,
  	use = official,
  	_use = null,
  	text = null,
  	_text = null,
  	family = Wolf938,
  	_family = null,
  	given = [Noel608],
  	_given = null,
  	prefix = null,
  	_prefix = null,
  	suffix = null,
  	_suffix = null,
  	period = null
  }]
  ```
+ An element with cardinality `0..1` is a struct, for example `Patient.maritalStatus`.

  ```
  {
  	id = null,
  	extension = null,
  	coding = [
  		{
  			id = null,
  			extension = null,
  			system = http: //terminology.hl7.org/CodeSystem/v3-MaritalStatus,
  				_system = null,
  			version = null,
  			_version = null,
  			code = S,
  			_code = null,
  			display = Never Married,
  			_display = null,
  			userSelected = null,
  			_userSelected = null
  		}
  
  	],
  	text = Never Married,
  	_text = null
  }
  ```
+ `extension` elements are arrays of JSON strings, because their structure varies.

HealthLake integrated natural language processing (NLP) adds the `SYSTEM_GENERATED` tag in `meta.tag` to resources it generates. Filter on it to include or exclude them. For more information, see [Integrated natural language processing (NLP) for HealthLake](integrating-nlp.md).

The SQL syntax for nested data differs by engine. For Amazon Athena examples, see [Example queries for HealthLake data](integrating-analytics-example-queries.md). For how the syntax differs, see [Adapting the examples for other engines](integrating-analytics-example-queries.md#integrating-analytics-example-queries-translate).

Resources imported inside a `Bundle` don't produce rows. HealthLake stores an imported `Bundle` as one resource and doesn't create a `Bundle` table.

### Resource versions
<a name="integrating-analytics-tables-versions"></a>

The tables are append-only. Each create, update, and delete appends a row. A delete appends a marker row in which `isdelete` is `true` and every column except `id`, `resourceType`, `meta.lastUpdated`, and `isdelete` is null. A plain count therefore includes old versions and deleted resources. To get current resources, keep the latest row for each `id` and drop delete markers, as in the following query.

```SQL
SELECT *
FROM (
  SELECT p.*,
         ROW_NUMBER() OVER (PARTITION BY id ORDER BY meta.lastUpdated DESC) AS row_num
  FROM patient p
) AS latest
WHERE row_num = 1
  AND coalesce(isdelete, false) = false;
```

Don't use `meta.versionId` to find current or deleted rows. It's null in many current rows.

Qualify `patient` with the catalog and database names your engine uses.

Redshift Spectrum can't run this query as written. For a form that works, see [SQL differences in Redshift Spectrum](integrating-redshift-spectrum.md#integrating-redshift-spectrum-sql).

### Data freshness
<a name="integrating-analytics-tables-freshness"></a>

HealthLake updates the analytics tables asynchronously. Changes typically appear within a few minutes, but there's no guaranteed freshness target. Queries against the tables don't affect HealthLake FHIR REST API performance, because the REST API and the analytics tables are independent interfaces.

To set up access, see [Getting started with HealthLake analytics](integrating-analytics-getting-started.md).

**Topics**
+ [How analytics access works](#integrating-analytics-how-it-works)
+ [Understanding the analytics tables](#integrating-analytics-tables)
+ [Getting started](integrating-analytics-getting-started.md)
+ [AWS analytics services](integrating-analytics-aws.md)
+ [Databricks](integrating-databricks.md)
+ [Snowflake](integrating-snowflake.md)
+ [Example queries](integrating-analytics-example-queries.md)
+ [Troubleshooting](integrating-analytics-troubleshooting.md)