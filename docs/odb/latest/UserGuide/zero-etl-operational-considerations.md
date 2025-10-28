# Considerations for zero-ETL

integration in Oracle Database@AWS

When setting up Zero-ETL integration between Oracle Database@AWS and Amazon Redshift, consider the following
guidelines:

**Initial data load time**

The initial full load time depends on the size of your database. Large databases might
take several hours or days to complete the initial synchronization.

**Oracle database performance**

Change data capture might impact Oracle database performance, especially during high
transaction volumes. After enabling Zero-ETL integration, monitor your database
performance.

**Schema changes**

Data Definition Language (DDL) changes in the source Oracle database might require you
to intervene manually to re-create the integration. Plan schema changes carefully.

For general considerations, see [Considerations when using zero-ETL
integrations with Amazon Redshift](../../../redshift/latest/mgmt/zero-etl.md "../../../redshift/latest/mgmt/zero-etl.md").
