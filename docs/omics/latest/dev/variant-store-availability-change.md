

# AWS HealthOmics variant store and annotation store availability change
<a name="variant-store-availability-change"></a>

After careful consideration, we decided to close AWS HealthOmics variant stores and annotation stores to new customers starting November 7th, 2025. Existing customers can continue to use the service as normal.

The following section describes migration options to help you move your variant stores and analytics stores to new solutions. For any questions or concerns, create a support case at [support.console.aws.amazon.com.](https://support.console.aws.amazon.com)

**Topics**
+ [Overview of migration options](#migrate-variant-store)
+ [Migration options for ETL logic](#migrate-variant-store-etl-logic)
+ [Migration options for storage](#migrate-variant-store-storage)
+ [Analytics](#migrate-variant-store-analytics)
+ [AWS Partners](#migrate-variant-store-partners)
+ [Examples](#migrate-variant-store-examples)

## Overview of migration options
<a name="migrate-variant-store"></a>

The following migration options provide an alternative to using variant stores and annotation stores:

1. Use the HealthOmics-provided [reference implementation of ETL logic](https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/glue-variant-etl) on GitHub. 

   Use S3 table buckets for storage and continue to use existing AWS analytics services. 

1. Create a solution using a combination of existing AWS services. 

   For ETL, you can write custom Glue ETL jobs, or use open-source HAIL or GLOW code on EMR, to transform variant data. 

   Use S3 table buckets for storage and continue to use existing AWS analytics services 

1. Select an [AWS partner](https://aws.amazon.com/partners/work-with-partners/) that offers a variant and annotation store alternative.

## Migration options for ETL logic
<a name="migrate-variant-store-etl-logic"></a>

Consider the following migration options for ETL logic:

1. HealthOmics provides the source code for the variant store ETL pipeline as a reference implementation on GitHub. You can use this pipeline to power the same variant data ETL process as the variant store, but with full control over the ETL logic. For more information, see [Glue Variant ETL](https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/glue-variant-etl) on GitHub.

1. To transform variant data, you can write custom Glue ETL jobs, or use open-source HAIL or GLOW code on EMR.

## Migration options for storage
<a name="migrate-variant-store-storage"></a>

As a replacement for service-hosted data store, you can use Amazon S3 table buckets to define a custom table schema.For more information about table buckets, see [Table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets.html) in the *Amazon S3 User Guide*.

You can use table buckets for fully managed Iceberg tables in Amazon S3.

You can raise a [support case](http://support.console.aws.amazon.com.) to request the HealthOmics team to migrate the data from your variant or annotation store to the Amazon S3 table bucket that you configured. 

After your data is populated in the Amazon S3 table bucket, you can delete your variant stores and annotation stores. For more information, see [Deleting HealthOmics analytics stores.](https://docs.aws.amazon.com/omics/latest/dev/deleting-a-store-examples.html) 

## Analytics
<a name="migrate-variant-store-analytics"></a>

For data analytics, continue to use AWS analytics services, such as [Amazon Athena](https://docs.aws.amazon.com/athena), [Amazon EMR](https://docs.aws.amazon.com/emr), [Amazon Redshift](https://docs.aws.amazon.com/redshift), or [Amazon Quick](https://docs.aws.amazon.com/quicksight).

## AWS Partners
<a name="migrate-variant-store-partners"></a>

You can work with an [AWS partner](https://aws.amazon.com/partners/work-with-partners/) that provides customizable ETL, table schemas, built-in query and analysis tools, and user interfaces for interacting with data. 

## Examples
<a name="migrate-variant-store-examples"></a>

The following examples show how to create tables suitable for storing VCF and GVCF data. 

### Athena DDL
<a name="migrate-variant-store-athena"></a>

You can use the following DDL example in Athena to create a table suitable for storing VCF and GVCF data in a single table. This example isn't the exact equivalent of the variant store structure, but it works well for a generic use case. 

Create your own values for DATABASE\_NAME and TABLE\_NAME when you create the table.

```
 CREATE TABLE <DATABASE_NAME>. <TABLE_NAME> (
  sample_name string,
  variant_name string COMMENT 'The ID field in VCF files, '.' indicates no name',
  chrom string,
  pos bigint,
  ref string,
  alt array <string>,
  qual double,
  filter string,
  genotype string,
  info map <string, string>,
  attributes map <string, string>,
  is_reference_block boolean COMMENT 'Used in GVCF for non-variant sites')
PARTITIONED BY (bucket(128, sample_name), chrom)
LOCATION '{URL}/'
TBLPROPERTIES (
  'table_type'='iceberg',
  'write_compression'='zstd'
);
```

### Create tables using Python (without Athena)
<a name="migrate-variant-store-python"></a>

The following Python code example shows how to create the tables without using Athena.

```
 import boto3
from pyiceberg.catalog import Catalog, load_catalog
from pyiceberg.schema import Schema
from pyiceberg.table import Table
from pyiceberg.table.sorting import SortOrder, SortField, SortDirection, NullOrder
from pyiceberg.partitioning import PartitionSpec, PartitionField
from pyiceberg.transforms import IdentityTransform, BucketTransform
from pyiceberg.types import (
    NestedField,
    StringType,
    LongType,
    DoubleType,
    MapType,
    BooleanType,
    ListType
)


def load_s3_tables_catalog(bucket_arn: str) -> Catalog:
    session = boto3.session.Session()
    region = session.region_name or 'us-east-1'
    
    catalog_config = {
        "type": "rest",
        "warehouse": bucket_arn,
        "uri": f"https://s3tables.{region}.amazonaws.com/iceberg",
        "rest.sigv4-enabled": "true",
        "rest.signing-name": "s3tables",
        "rest.signing-region": region
    }
    
    return load_catalog("s3tables", **catalog_config)


def create_namespace(catalog: Catalog, namespace: str) -> None:
    try:
        catalog.create_namespace(namespace)
        print(f"Created namespace: {namespace}")
    except Exception as e:
        if "already exists" in str(e):
            print(f"Namespace {namespace} already exists.")
        else:
            raise e


def create_table(catalog: Catalog, namespace: str, table_name: str, schema: Schema, 
                partition_spec: PartitionSpec = None, sort_order: SortOrder = None) -> Table:
    if catalog.table_exists(f"{namespace}.{table_name}"):
        print(f"Table {namespace}.{table_name} already exists.")
        return catalog.load_table(f"{namespace}.{table_name}")
    
    create_table_args = {
        "identifier": f"{namespace}.{table_name}",
        "schema": schema,
        "properties": {"format-version": "2"}
    }
    
    if partition_spec is not None:
        create_table_args["partition_spec"] = partition_spec
    if sort_order is not None:
        create_table_args["sort_order"] = sort_order
    
    table = catalog.create_table(**create_table_args)
    print(f"Created table: {namespace}.{table_name}")
    return table


def main(bucket_arn: str, namespace: str, table_name: str):
    # Schema definition
    genomic_variants_schema = Schema(
        NestedField(1, "sample_name", StringType(), required=True),
        NestedField(2, "variant_name", StringType(), required=True),
        NestedField(3, "chrom", StringType(), required=True),
        NestedField(4, "pos", LongType(), required=True),
        NestedField(5, "ref", StringType(), required=True),
        NestedField(6, "alt", ListType(element_id=1000, element_type=StringType(), element_required=True), required=True),
        NestedField(7, "qual", DoubleType()),
        NestedField(8, "filter", StringType()),
        NestedField(9, "genotype", StringType()),
        NestedField(10, "info", MapType(key_type=StringType(), key_id=1001, value_type=StringType(), value_id=1002)),
        NestedField(11, "attributes", MapType(key_type=StringType(), key_id=2001, value_type=StringType(), value_id=2002)),
        NestedField(12, "is_reference_block", BooleanType()),
        identifier_field_ids=[1, 2, 3, 4]
    )
    
    # Partition and sort specifications
    partition_spec = PartitionSpec(
        PartitionField(source_id=1, field_id=1001, transform=BucketTransform(128), name="sample_bucket"),
        PartitionField(source_id=3, field_id=1002, transform=IdentityTransform(), name="chrom")
    )
    
    sort_order = SortOrder(
        SortField(source_id=3, transform=IdentityTransform(), direction=SortDirection.ASC, null_order=NullOrder.NULLS_LAST),
        SortField(source_id=4, transform=IdentityTransform(), direction=SortDirection.ASC, null_order=NullOrder.NULLS_LAST)
    )
    
    # Connect to catalog and create table
    catalog = load_s3_tables_catalog(bucket_arn)
    create_namespace(catalog, namespace)
    table = create_table(catalog, namespace, table_name, genomic_variants_schema, partition_spec, sort_order)
    
    return table


if __name__ == "__main__":
    bucket_arn = 'arn:aws:s3tables:<REGION>:<ACCOUNT_ID>:bucket/<TABLE_BUCKET_NAME'
    namespace = "variant_db"
    table_name = "genomic_variants"
    
    main(bucket_arn, namespace, table_name)
```