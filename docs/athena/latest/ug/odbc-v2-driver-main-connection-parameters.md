

# Main ODBC 2.x connection parameters
<a name="odbc-v2-driver-main-connection-parameters"></a>

The following sections describe each of the main connection parameters.

## Data source name
<a name="odbc-v2-driver-main-connection-parameters-data-source-name"></a>

Specifies the name of your data source.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| DSN | Optional for DSN-less connection types | none | DSN=AmazonAthenaOdbcUsWest1; | 

## Description
<a name="odbc-v2-driver-main-connection-parameters-description"></a>

Contains description of your data source.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| Description | Optional | none | Description=Connection to Amazon Athena us-west-1; | 

## Catalog
<a name="odbc-v2-driver-main-connection-parameters-catalog"></a>

Specifies the data catalog name. For more information about catalogs, see [DataCatalog](https://docs.aws.amazon.com/athena/latest/APIReference/API_DataCatalog.html) in the Amazon Athena API Reference.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| Catalog | Optional | AwsDataCatalog | Catalog=AwsDataCatalog; | 

## Region
<a name="odbc-v2-driver-region"></a>

Specifies the AWS Region. For information about AWS Regions, see [Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/).



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AwsRegion | Mandatory | none | AwsRegion=us-west-1; | 

## Database
<a name="odbc-v2-driver-database"></a>

Specifies the database name. For more information about databases, see [Database](https://docs.aws.amazon.com/athena/latest/APIReference/API_Database.html) in the *Amazon Athena API Reference*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| Schema | Optional | default | Schema=default; | 

## Workgroup
<a name="odbc-v2-driver-workgroup"></a>

Specifies the workgroup name. For more information about workgroups, see [WorkGroup](https://docs.aws.amazon.com/athena/latest/APIReference/API_WorkGroup.html) in the *Amazon Athena API Reference*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| Workgroup | Optional | primary | Workgroup=primary; | 

## Output location
<a name="odbc-v2-driver-output-location"></a>

Specifies the location in Amazon S3 where query results are stored. For more information about output location, see [ResultConfiguration](https://docs.aws.amazon.com/athena/latest/APIReference/API_ResultConfiguration.html) in the *Amazon Athena API Reference*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| S3OutputLocation | Mandatory | none | S3OutputLocation=s3://amzn-s3-demo-bucket/; | 

## Encryption options
<a name="odbc-v2-driver-encryption-options"></a>

**Dialog parameter name**: Encryption options

Specifies encryption option. For more information about encryption options, see [EncryptionConfiguration](https://docs.aws.amazon.com/athena/latest/APIReference/API_EncryptionConfiguration.html) in the *Amazon Athena API Reference*.



| **Connection string name** | **Parameter type** | **Default value** | **Possible values** | **Connection string example** | 
| --- | --- | --- | --- | --- | 
| S3OutputEncOption | Optional | none | NOT\_SET, SSE\_S3, SSE\_KMS, CSE\_KMS | S3OutputEncOption=SSE\_S3; | 

## KMS key
<a name="odbc-v2-driver-kms-key"></a>

Specifies a KMS key for encryption. For more information about encryption configuration for KMS Keys, see [EncryptionConfiguration](https://docs.aws.amazon.com/athena/latest/APIReference/API_EncryptionConfiguration.html) in the *Amazon Athena API Reference*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| S3OutputEncKMSKey | Optional | none | S3OutputEncKMSKey=your\_key; | 

## Connection test
<a name="odbc-v2-driver-connection-test"></a>

ODBC Data Source Administrator provides a **Test** option that you can use to test your ODBC 2.x connection to Amazon Athena. For steps, see [Configuring a data source name on Windows](odbc-v2-driver-getting-started-windows.md#odbc-v2-driver-configuring-dsn-on-windows). When you test a connection, the ODBC driver calls the [GetWorkGroup](https://docs.aws.amazon.com/athena/latest/APIReference/API_GetWorkGroup.html) Athena API action. The call uses the authentication type and corresponding credentials provider that you specified to retrieve the credentials. There is no charge for the connection test when you use the ODBC 2.x driver. The test does not generate query results in your Amazon S3 bucket.