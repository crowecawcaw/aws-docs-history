

# Zero-ETL for Amazon Redshift
<a name="vpc-lattice-oci-zero-etl"></a>

You can use the service network provisioned by VPC Lattice to enable [Zero-ETL](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.html). This managed integration connects your ODB network databases to Amazon Redshift to help analyze data across different databases. You can initiate the Zero-ETL setup using AWS Glue integration APIs and use the ODB APIs to turn on the managed integration and setup the network path. For more information, see [Zero-ETL integration with Amazon Redshift](https://docs.aws.amazon.com/odb/latest/UserGuide/zero-etl-integration.html).

## Considerations
<a name="vpc-lattice-oci-zero-etl-considerations"></a>

The following are considerations for the managed Zero-ETL integration:
+ If you enable the managed Zero-ETL integration, you can only use Zero-ETL to access instances in your ODB network. Other services and resources associated with your service network are isolated from Zero-ETL.