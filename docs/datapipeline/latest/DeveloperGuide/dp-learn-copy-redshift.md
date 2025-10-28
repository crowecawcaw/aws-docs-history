AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Before You Begin: Configure COPY Options and Load

Data

Before copying data to Amazon Redshift within AWS Data Pipeline, ensure that you:

- Load data from Amazon S3.
- Set up the `COPY` activity in Amazon Redshift.
  Once you have these options working and successfully complete a data load, transfer
  these options to AWS Data Pipeline, for performing the copying within it.

For `COPY` options, see [COPY](../../../redshift/latest/dg/r_COPY.md "../../../redshift/latest/dg/r_COPY.md")
in the Amazon Redshift _Database Developer Guide_.

For steps to load data from Amazon S3, see [Loading data from Amazon S3](../../../redshift/latest/dg/t_Loading-data-from-S3.md "../../../redshift/latest/dg/t_Loading-data-from-S3.md") in the
Amazon Redshift _Database Developer Guide_.

For example, the following SQL command in Amazon Redshift creates a new table named
`LISTING` and copies sample data from a publicly available bucket in
Amazon S3.

Replace the `<iam-role-arn>` and region with your own.

For details about this example, see [Load Sample Data from Amazon S3](../../../redshift/latest/gsg/rs-gsg-create-sample-db.md "../../../redshift/latest/gsg/rs-gsg-create-sample-db.md") in
the Amazon Redshift _Getting Started Guide_.

```
create table listing(
	listid integer not null distkey,
	sellerid integer not null,
	eventid integer not null,
	dateid smallint not null  sortkey,
	numtickets smallint not null,
	priceperticket decimal(8,2),
	totalprice decimal(8,2),
	listtime timestamp);

copy listing from 's3://awssampledbuswest2/tickit/listings_pipe.txt'
credentials 'aws_iam_role=<iam-role-arn>'
delimiter '|' region 'us-west-2';

```
