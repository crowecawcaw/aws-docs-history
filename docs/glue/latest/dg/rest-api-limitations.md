# Limitations

The following are limitations for the REST API connector

- REST API connector is only available through the AWS API, CLI, or SDK. You cannot configure REST connectors
  through the console.
- The AWS Glue REST ConnectionType can only be configured to READ data from the REST API-based data source.
  The connection can only be used as a SOURCE in AWS Glue ETL jobs.
- Filtering and partitioning is not supported.
- Field selection is not supported.
