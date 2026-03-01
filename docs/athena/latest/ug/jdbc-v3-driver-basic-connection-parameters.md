# Basic connection parameters

The following sections describe the basic connection parameters for the JDBC 3.x
driver.

## Region

The AWS Region where queries will be run. For a list of regions, see [Amazon Athena endpoints and
quotas](../../../general/latest/gr/athena.md "../../../general/latest/gr/athena.md").

| Parameter name | Alias                  | Parameter type                                                                                                                                                                                                                                                                                                                             | Default value |
| -------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| Region         | AwsRegion (deprecated) | Mandatory (but if not provided, will be searched using the [DefaultAwsRegionProviderChain](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/regions/providers/DefaultAwsRegionProviderChain.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/regions/providers/DefaultAwsRegionProviderChain.html")) | none          |

## Catalog

The catalog that contains the databases and the tables that will be accessed with the
driver. For information about catalogs, see [DataCatalog](../APIReference/API_DataCatalog.md "../APIReference/API_DataCatalog.md").

| Parameter name | Alias | Parameter type | Default value  |
| -------------- | ----- | -------------- | -------------- |
| Catalog        | none  | Optional       | AwsDataCatalog |

## Database

The database where queries will run. Tables that are not explicitly qualified with a
database name are resolved to this database. For information about databases, see [Database](../APIReference/API_Database.md "../APIReference/API_Database.md").

| Parameter name | Alias  | Parameter type | Default value |
| -------------- | ------ | -------------- | ------------- |
| Database       | Schema | Optional       | default       |

## Workgroup

The workgroup in which queries will run. For information about workgroups, see [WorkGroup](../APIReference/API_WorkGroup.md "../APIReference/API_WorkGroup.md").

| Parameter name | Alias | Parameter type | Default value |
| -------------- | ----- | -------------- | ------------- |
| WorkGroup      | none  | Optional       | primary       |

## Output location

The location in Amazon S3 where query results will be stored. For information about output
location, see [ResultConfiguration](../APIReference/API_ResultConfiguration.md "../APIReference/API_ResultConfiguration.md").

| Parameter name | Alias                         | Parameter type                                                | Default value |
| -------------- | ----------------------------- | ------------------------------------------------------------- | ------------- |
| OutputLocation | S3OutputLocation (deprecated) | Mandatory (unless the workgroup specifies an output location) | none          |
