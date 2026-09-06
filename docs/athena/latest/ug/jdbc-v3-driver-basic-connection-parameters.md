

# Basic connection parameters
<a name="jdbc-v3-driver-basic-connection-parameters"></a>

The following sections describe the basic connection parameters for the JDBC 3.x driver.

## Region
<a name="jdbc-v3-driver-region"></a>

The AWS Region where queries will be run. For a list of regions, see [Amazon Athena endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/athena.html).



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| Region | AwsRegion (deprecated) | Mandatory (but if not provided, will be searched using the [DefaultAwsRegionProviderChain](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/regions/providers/DefaultAwsRegionProviderChain.html))  | none | 

## Catalog
<a name="jdbc-v3-driver-catalog"></a>

The catalog that contains the databases and the tables that will be accessed with the driver. For information about catalogs, see [DataCatalog](https://docs.aws.amazon.com/athena/latest/APIReference/API_DataCatalog.html).



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| Catalog | none | Optional | AwsDataCatalog | 

## Database
<a name="jdbc-v3-driver-database"></a>

The database where queries will run. Tables that are not explicitly qualified with a database name are resolved to this database. For information about databases, see [Database](https://docs.aws.amazon.com/athena/latest/APIReference/API_Database.html).



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| Database | Schema | Optional | default | 

## Workgroup
<a name="jdbc-v3-driver-workgroup"></a>

The workgroup in which queries will run. For information about workgroups, see [WorkGroup](https://docs.aws.amazon.com/athena/latest/APIReference/API_WorkGroup.html).



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| WorkGroup | none | Optional | primary | 

## Output location
<a name="jdbc-v3-driver-output-location"></a>

The location in Amazon S3 where query results will be stored. For information about output location, see [ResultConfiguration](https://docs.aws.amazon.com/athena/latest/APIReference/API_ResultConfiguration.html).



| Parameter name | Alias | Parameter type | Default value | 
| --- | --- | --- | --- | 
| OutputLocation | S3OutputLocation (deprecated) | Mandatory (unless the workgroup specifies an output location) | none | 