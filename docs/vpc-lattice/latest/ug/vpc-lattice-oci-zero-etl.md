# Zero-ETL for Amazon Redshift

You can use the service network provisioned by VPC Lattice to enable [Zero-ETL](../../../redshift/latest/mgmt/zero-etl-using.md "../../../redshift/latest/mgmt/zero-etl-using.md"). This managed integration connects your ODB network databases to Amazon Redshift
to help analyze data across different databases. You can initiate the Zero-ETL setup
using AWS Glue integration APIs and use the ODB APIs to turn on the
managed integration and setup the network path. For more information, see [Zero-ETL integration with Amazon Redshift](../../../odb/latest/UserGuide/zero-etl-integration.md "../../../odb/latest/UserGuide/zero-etl-integration.md").

## Considerations

The following are considerations for the managed Zero-ETL integration:

- If you enable the managed Zero-ETL integration, you can only use Zero-ETL
  to access instances in your ODB network. Other services and
  resources associated with your service network are isolated from
  Zero-ETL.
