# Configuring a crawler to use Lake Formation credentials

You can configure a crawler to use AWS Lake Formation credentials to access an Amazon S3 data store or a Data Catalog table with
an underlying Amazon S3 location within the same AWS account or another AWS account. You can configure an existing Data Catalog table as a crawler's target, if the crawler and
the Data Catalog table reside in the same account. Currently, only a single catalog target with a single catalog table is allowed when using a Data Catalog table as a crawler’s target.

###### Note

When you are defining a Data Catalog table as a crawler target, make sure that the underlying location of
the Data Catalog table is an Amazon S3 location. Crawlers that use Lake Formation credentials only support Data Catalog targets with underlying Amazon S3 locations.

## Setup required when the crawler and registered Amazon S3 location or Data Catalog table reside in the same account (in-account crawling)

To allow the crawler to access a data store or Data Catalog table by using Lake Formation credentials, you need to register
the data location with Lake Formation. Also, the crawler's IAM role must have permissions to read the data from the destination where the Amazon S3 bucket is registered.

You can complete the following configuration steps using the AWS Management Console or AWS Command Line Interface (AWS CLI).

AWS Management Console

1. Before configuring a crawler to access the crawler source, register the data
   location of the data store or the Data Catalog with Lake Formation. In the Lake Formation console
   ([https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/")), register an Amazon S3 location as the root location of your data
   lake in the AWS account where the crawler is defined. For more information, see [Registering an Amazon S3
   location](../../../lake-formation/latest/dg/register-location.md "../../../lake-formation/latest/dg/register-location.md").
2. Grant **Data location** permissions to the IAM
   role that's used for the crawler run so that the crawler can read the data from the
   destination in Lake Formation. For more information, see [Granting data location permissions (same account)](../../../lake-formation/latest/dg/granting-location-permissions-local.md "../../../lake-formation/latest/dg/granting-location-permissions-local.md").
3. Grant the crawler role access permissions (`Create`) to the database, which is specified
   as the output database. For more information, see [Granting database permissions using the Lake Formation console and the named resource method](../../../lake-formation/latest/dg/granting-database-permissions.md "../../../lake-formation/latest/dg/granting-database-permissions.md").
4. In the IAM console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")), create an IAM role for the crawler. Add the `lakeformation:GetDataAccess` policy to the role.
5. In the AWS Glue console ([https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/")), while configuring the crawler,
   select the option **Use Lake Formation credentials for crawling Amazon S3 data
   source**.

###### Note

The accountId field is optional for in-account crawling.

AWS CLI

```
aws glue --profile demo create-crawler --debug --cli-input-json '{
    "Name": "prod-test-crawler",
    "Role": "arn:aws:iam::111122223333:role/service-role/AWSGlueServiceRole-prod-test-run-role",
    "DatabaseName": "prod-run-db",
    "Description": "",
    "Targets": {
    "S3Targets":[
                {
                 "Path": "s3://amzn-s3-demo-bucket"
                }
                ]
                },
   "SchemaChangePolicy": {
      "UpdateBehavior": "LOG",
      "DeleteBehavior": "LOG"
  },
  "RecrawlPolicy": {
    "RecrawlBehavior": "CRAWL_EVERYTHING"
  },
  "LineageConfiguration": {
    "CrawlerLineageSettings": "DISABLE"
  },
  **"LakeFormationConfiguration": {
 "UseLakeFormationCredentials": true,
 "AccountId": "111122223333"**
  },
  "Configuration": {
           "Version": 1.0,
           "CrawlerOutput": {
             "Partitions": { "AddOrUpdateBehavior": "InheritFromTable" },
             "Tables": {"AddOrUpdateBehavior": "MergeNewColumns" }
           },
           "Grouping": { "TableGroupingPolicy": "CombineCompatibleSchemas" }
         },
  "CrawlerSecurityConfiguration": "",
  "Tags": {
    "KeyName": ""
  }
}'
```
