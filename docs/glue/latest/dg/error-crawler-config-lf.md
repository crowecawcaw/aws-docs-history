# Crawler errors when the crawler is using Lake Formation

permissions

Use the information below to diagnose and fix various issues while configuring the crawler using Lake Formation
credentials.

## Error: The S3 location: s3://examplepath is not registered

For a crawler to run using Lake Formation credentials, you need to first set up Lake Formation permissions. To resolve this
error, please register the target Amazon S3 location with Lake Formation. For more information, see [Registering an Amazon S3 location](../../../lake-formation/latest/dg/register-location.md "../../../lake-formation/latest/dg/register-location.md").

## Error: User/Role is not authorized to perform:

lakeformation:GetDataAccess on resource

Please add the `lakeformation:GetDataAccess` permission to the crawler role using the IAM
console or AWS CLI. With this permission, Lake Formation grants the request for temporary credentials to access the data.
See the policy below:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "lakeformation:GetDataAccess"
 ],
 "Resource": "*"
 }
}`

```

## Error: Insufficient Lake Formation permission(s) on (Database name: exampleDatabase,

Table Name: exampleTable)

In the Lake Formation console ([https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/")), grant the crawler role access permissions ( `Create`,
`Describe`, `Alter`) on the database, which is specified as the output database. You can
grant permissions on the table as well. For more information, see [Granting database permissions using the
named resource method](../../../lake-formation/latest/dg/granting-cat-perms-named-resource.md "../../../lake-formation/latest/dg/granting-cat-perms-named-resource.md").

## Error: Insufficient Lake Formation permission(s) on s3://examplepath

1. **Cross-account crawling**
   1. Log in to the Lake Formation console ([https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/")) using the account where Amazon S3 bucket is registred
      (account B). Grant data location permissions to the account where the crawler will be run. This will
      allow the crawler to read data from the target Amazon S3 location.
   2. In the account where the crawler is created (account A), grant data location permissions on the
      target Amazon S3 location to the IAM role used for the crawler run so that the crawler can read the data
      from the destination in Lake Formation. For more information, see [Granting data location
      permissions (external account)](../../../lake-formation/latest/dg/granting-location-permissions-external.md "../../../lake-formation/latest/dg/granting-location-permissions-external.md").

2. **In-account (crawler and registered Amazon S3 location are in the same account)
   crawling** ‐ Grant data location permissions to the IAM role used for the crawler run on
   the Amazon S3 location so that the crawler can read the data from the target in Lake Formation. For more information, see
   [Granting
   data location permissions (same account)](../../../lake-formation/latest/dg/granting-location-permissions-local.md "../../../lake-formation/latest/dg/granting-location-permissions-local.md").

## Frequently asked questions about crawler configuration using Lake Formation

credentials

1. **How do I configure a crawler to run using Lake Formation credentials using the AWS
   console?**

In the AWS Glue console ([https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/")), while configuring the crawler, select the option
**Use Lake Formation credentials for crawling Amazon S3 data source**. For cross-account crawling, specify
the AWS account ID where the target Amazon S3 location is registered with Lake Formation. For in-account crawling, the
**accountId** field is optional. 2. **How do I configure a crawler to run using Lake Formation credentials using
AWS CLI?**

During `CreateCrawler` API call, add `LakeFormationConfiguration` :

```
"LakeFormationConfiguration": {
    "UseLakeFormationCredentials": true,
    "AccountId": "111111111111" (AWS account ID where the target Amazon S3 location is registered with Lake Formation)
  }
```

3. **What are the supported targets for a crawler using Lake Formation credentials?**

A crawler using Lake Formation credentials is only supported for Amazon S3 (in-account and cross-account crawling),
in-account Data Catalog targets (where the underlying location is Amazon S3), and Apache Iceberg targets. 4. **Can I crawl multiple Amazon S3 buckets as part of a single crawler using Lake Formation
credentials?**

No, for crawling targets using Lake Formation credential vending, the underlying Amazon S3 locations must belong to the
same bucket. For example, customers can use multiple target locations `(s3://bucket1/folder1,
 s3://bucket1/folder2)` if they are under the same bucket (bucket1). Specifying different buckets
(s3://bucket1/folder1, s3://bucket2/folder2) is not supported.
