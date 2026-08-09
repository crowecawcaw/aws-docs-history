# Amazon S3 Tables integration with AWS analytics services overview

To make tables in your account accessible by AWS analytics services, you integrate your Amazon S3
table buckets with AWS Glue Data Catalog. This integration allows AWS analytics services to
automatically discover and access your table data. You can use this integration to work with your tables
in these services:

- [Amazon Athena](s3-tables-integrating-athena.md "s3-tables-integrating-athena.md")
- [Amazon Redshift](s3-tables-integrating-redshift.md "s3-tables-integrating-redshift.md")
- [Amazon EMR](s3-tables-integrating-emr.md "s3-tables-integrating-emr.md")
- [Quick](s3-tables-integrating-quicksight.md "s3-tables-integrating-quicksight.md")
- [Amazon Data Firehose](s3-tables-integrating-firehose.md "s3-tables-integrating-firehose.md")

###### Note

This integration uses AWS Glue
and AWS Lake Formation services and might incur AWS Glue request and storage costs. For more information,
see [AWS Glue Pricing.](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/")

Additional pricing applies for running queries on your S3 tables. For more information, see
pricing information for the query engine that you're using.

## How the integration works

When you integrate S3 Tables with the AWS analytics services, Amazon S3 adds the catalog named `s3tablescatalog` to the AWS Glue Data Catalog in the current Region.
Adding the `s3tablescatalog` allows all your table buckets, namespaces, and
tables to be populated in the Data Catalog.

###### Note

These actions are automated through the Amazon S3 console. If you perform this integration programmatically,
you must manually take these actions.

You integrate your table buckets once per AWS Region. After the integration is completed, all
current and future table buckets, namespaces, and tables are added to the AWS Glue Data Catalog in that
Region.

The following illustration shows how the `s3tablescatalog` catalog automatically
populates table buckets, namespaces, and tables in the current Region as corresponding objects in the
Data Catalog. Table buckets are populated as subcatalogs. Namespaces within a table bucket are populated as
databases within their respective subcatalogs. Tables are populated as tables in their respective
databases.

![The ways that table resources are represented in AWS Glue Data Catalog.](images/S3Tables-glue-catalog.png)

After integrating with Data Catalog, you can create Apache Iceberg tables in table buckets and access them through AWS analytics engines such as Amazon Athena, Amazon EMR, as well as third-party analytics engines.

###### How permissions work

We recommend integrating your table buckets with AWS analytics services so that you can work
with your table data across services that use the AWS Glue Data Catalog as a metadata store. Once the integration
is enabled, you can use AWS Identity and Access Management (IAM) permissions to grant access to S3 Tables resources and their
associated Data Catalog objects.

Make sure that you follow the steps in [Integrating S3 Tables with AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md") so that you have the appropriate permissions to access the
AWS Glue Data Catalog and your table resources, and to work with AWS analytics services.

## Regions supported

S3 Tables integration with AWS analytics services uses AWS Glue Data Catalog with IAM-based access controls in the following regions. In all other regions, the integration also requires AWS Lake Formation.

- US East (N. Virginia)
- US East (Ohio)
- US West (N. California)
- US West (Oregon)
- Africa (Cape Town)
- Asia Pacific (Hong Kong)
- Asia Pacific (Taipei)
- Asia Pacific (Tokyo)
- Asia Pacific (Seoul)
- Asia Pacific (Osaka)
- Asia Pacific (Mumbai)
- Asia Pacific (Hyderabad)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Jakarta)
- Asia Pacific (Melbourne)
- Asia Pacific (Malaysia)
- Asia Pacific (New Zealand)
- Asia Pacific (Thailand)
- Canada (Central)
- Canada West (Calgary)
- Europe (Frankfurt)
- Europe (Zurich)
- Europe (Stockholm)
- Europe (Milan)
- Europe (Spain)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- Israel (Tel Aviv)
- Mexico (Central)
- South America (São Paulo)

## Next steps

- [Integrating S3 Tables with AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md")
- [Create a namespace](s3-tables-namespace-create.md "s3-tables-namespace-create.md")
- [Create a table](s3-tables-create.md "s3-tables-create.md")
