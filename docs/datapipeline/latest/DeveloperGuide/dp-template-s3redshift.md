AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Load data from Amazon S3 into Amazon Redshift

The **Load data from S3 into Redshift** template copies data
from an Amazon S3 folder into an Amazon Redshift table. You can load the data into an existing
table or provide a SQL query to create the table.

The data is copied based on the Amazon Redshift `COPY` options. The Amazon Redshift table
must have the same schema as the data in Amazon S3. For `COPY` options,
see [COPY](../../../redshift/latest/dg/r_COPY.md "../../../redshift/latest/dg/r_COPY.md") in the Amazon Redshift
_Database Developer Guide_.

The template uses the following pipeline objects:

- [CopyActivity](dp-object-copyactivity.md "dp-object-copyactivity.md")
- [RedshiftCopyActivity](dp-object-redshiftcopyactivity.md "dp-object-redshiftcopyactivity.md")
- [S3DataNode](dp-object-s3datanode.md "dp-object-s3datanode.md")
- [RedshiftDataNode](dp-object-redshiftdatanode.md "dp-object-redshiftdatanode.md")
- [RedshiftDatabase](dp-object-redshiftdatabase.md "dp-object-redshiftdatabase.md")
- [Ec2Resource](dp-object-ec2resource.md "dp-object-ec2resource.md")
