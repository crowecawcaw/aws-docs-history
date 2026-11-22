

# Governing AWS Glue Data Catalog user-defined functions with Lake Formation

A Lake Formation-governed user-defined function (UDF) is a function registered in the AWS Glue Data Catalog with `GovernanceMode` set to `LAKE_FORMATION`. Its code is packaged in JARs stored in Amazon S3. For information about Data Catalog UDFs, see [User-defined function API](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-functions.html).

You can use Lake Formation permissions to control who can create, execute, update, and delete governed UDFs. You can also control which tables a UDF can operate on.

## Why use governed UDFs?
<a name="governing-udfs-why"></a>

When you run Amazon EMR Spark jobs with Lake Formation fine-grained access control, only governed UDFs are permitted in the Spark system space.

When you create the UDF in the AWS Glue Data Catalog with `GovernanceMode` set to `LAKE_FORMATION`, you can grant `EXECUTE` to specific job execution roles and choose which tables the UDF can be used with. CloudTrail records the related AWS Glue and Lake Formation API calls.

## Who can create a governed UDF?
<a name="governing-udfs-creators"></a>

A data lake administrator in the account that owns the Data Catalog can create a governed UDF.

Before creating the UDF, upload its JAR to Amazon S3 and register the JAR location with Lake Formation. For registration requirements, see [Adding an Amazon S3 location to your data lake](register-data-lake.md).

When you create a governed UDF, it is automatically enabled to be executed against all tables in your account, including tables added later. You can review and narrow this default grant after creating the UDF.

## Create a governed UDF
<a name="governing-udfs-create"></a>

Save the following AWS Glue Data Catalog UDF input as `udf-input.json`. Replace the function name, class name, owner, and Amazon S3 locations with your values.

```json
{
  "FunctionName": "normalize_region",
  "ClassName": "com.example.NormalizeRegion",
  "OwnerName": "example-user",
  "OwnerType": "USER",
  "GovernanceMode": "LAKE_FORMATION",
  "ArtifactLocation": "s3://amzn-s3-demo-bucket/udfs/normalize_region/",
  "ResourceUris": [
    {
      "ResourceType": "JAR",
      "Uri": "s3://amzn-s3-demo-bucket/udfs/normalize_region/normalize-region.jar"
    }
  ]
}
```

Create the UDF with the AWS CLI or an AWS SDK. The AWS CLI `--function-input` option passes `GovernanceMode` from `udf-input.json`.

------
#### [ AWS CLI ]

```bash
aws glue create-user-defined-function \
  --database-name security_db \
  --function-input file://udf-input.json
```

------
#### [ Python (Boto3) ]

```python
import json
import boto3

with open("udf-input.json", encoding="utf-8") as input_file:
    function_input = json.load(input_file)

boto3.client("glue").create_user_defined_function(
    DatabaseName="security_db",
    FunctionInput=function_input,
)
```

------

## Control which tables a UDF can operate on
<a name="governing-udfs-table-access"></a>

The automatic `SELECT` grant is on `AnyResource` with `ResourceType=TABLE` in the owning catalog. It covers existing and future tables. To limit the UDF's access, revoke that grant, then grant the UDF principal full-table `SELECT` on the tables you wish to use it for.

### View the default table permission
<a name="governing-udfs-list-permissions"></a>

After creating the UDF, list its default table permission. Replace the AWS Region and account ID with the UDF's values:

```bash
aws lakeformation list-permissions \
  --catalog-id 111122223333 \
  --principal DataLakePrincipalIdentifier=arn:aws:glue:us-east-1:111122223333:userDefinedFunction/security_db/normalize_region \
  --resource '{"AnyResource":{"CatalogId":"111122223333","ResourceType":"TABLE"}}'
```

For the example UDF, the response has this form:

```json
{
  "PrincipalResourcePermissions": [
    {
      "Principal": {
        "DataLakePrincipalIdentifier": "arn:aws:glue:us-east-1:111122223333:userDefinedFunction/security_db/normalize_region"
      },
      "Resource": {
        "AnyResource": {
          "CatalogId": "111122223333",
          "ResourceType": "TABLE"
        }
      },
      "Permissions": [
        "SELECT"
      ],
      "PermissionsWithGrantOption": []
    }
  ]
}
```

The principal identifies the UDF, and `AnyResource` with `ResourceType=TABLE` identifies tables in its owning catalog. The `SELECT` permission is granted automatically when you create the UDF.

## Control access to a governed UDF
<a name="governing-udfs-permissions"></a>

### Grant permissions on a governed UDF
<a name="governing-udfs-actions"></a>

You can use Lake Formation permissions to control who can discover (`DESCRIBE`), run (`EXECUTE`), update (`ALTER`), and delete (`DROP`) a governed UDF. Users with `EXECUTE` permission, or applications acting on their behalf, can fetch the temporary credentials required to access the UDF's resource artifacts.

Grant `DESCRIBE` and `ALTER` to a role that inspects and updates the UDF. Grant the job execution role `DESCRIBE` and `EXECUTE` to let it discover and use the function. Replace the account ID and role names in these examples:

------
#### [ AWS CLI ]

```bash
aws lakeformation grant-permissions \
  --principal DataLakePrincipalIdentifier=arn:aws:iam::111122223333:role/UdfMaintainerRole \
  --resource '{"UserDefinedFunction":{"CatalogId":"111122223333","DatabaseName":"security_db","Name":"normalize_region"}}' \
  --permissions DESCRIBE ALTER

aws lakeformation grant-permissions \
  --principal DataLakePrincipalIdentifier=arn:aws:iam::111122223333:role/JobExecutionRole \
  --resource '{"UserDefinedFunction":{"CatalogId":"111122223333","DatabaseName":"security_db","Name":"normalize_region"}}' \
  --permissions DESCRIBE EXECUTE
```

------
#### [ Python (Boto3) ]

```python
import boto3

lakeformation = boto3.client("lakeformation")
udf_resource = {
    "UserDefinedFunction": {
        "CatalogId": "111122223333",
        "DatabaseName": "security_db",
        "Name": "normalize_region",
    }
}

lakeformation.grant_permissions(
    Principal={
        "DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/UdfMaintainerRole"
    },
    Resource=udf_resource,
    Permissions=["DESCRIBE", "ALTER"],
)

lakeformation.grant_permissions(
    Principal={
        "DataLakePrincipalIdentifier": "arn:aws:iam::111122223333:role/JobExecutionRole"
    },
    Resource=udf_resource,
    Permissions=["DESCRIBE", "EXECUTE"],
)
```

------

## Update a governed UDF
<a name="governing-udfs-update"></a>

After replacing the JAR at the Amazon S3 URI in `udf-input.json`, call the AWS Glue `UpdateUserDefinedFunction` operation with the complete function input. Lake Formation records the replacement JAR's last-modified time during the update so that engines can verify the JAR. If the replacement has a different URI, update `ResourceUris` in the input file first.

The caller needs Lake Formation `ALTER` permission to update `normalize_region`. The grant example above gives this permission to `UdfMaintainerRole`.

------
#### [ AWS CLI ]

```bash
aws glue update-user-defined-function \
  --database-name security_db \
  --function-name normalize_region \
  --function-input file://udf-input.json
```

------
#### [ Python (Boto3) ]

```python
import json
import boto3

with open("udf-input.json", encoding="utf-8") as input_file:
    function_input = json.load(input_file)

boto3.client("glue").update_user_defined_function(
    DatabaseName="security_db",
    FunctionName="normalize_region",
    FunctionInput=function_input,
)
```

------

## Delete a governed UDF
<a name="governing-udfs-delete"></a>

The caller needs Lake Formation `DROP` on the UDF. Deleting the UDF removes its Data Catalog registration; the JAR remains in Amazon S3. Use either the AWS CLI or an AWS SDK:

------
#### [ AWS CLI ]

```bash
aws glue delete-user-defined-function \
  --database-name security_db \
  --function-name normalize_region
```

------
#### [ Python (Boto3) ]

```python
import boto3

boto3.client("glue").delete_user_defined_function(
    DatabaseName="security_db",
    FunctionName="normalize_region",
)
```

------

## Restrictions
<a name="governing-udfs-considerations"></a>
+ For a governed UDF, `ResourceUris` must contain at least one and at most 10 entries. Each entry specifies an artifact type, such as `JAR`, and an Amazon S3 `Uri`. Every `Uri` must be under the Amazon S3 prefix in `ArtifactLocation`, which must be registered with Lake Formation.
+ You cannot rename a governed UDF or change its `GovernanceMode` after creation.
+ You cannot share a governed UDF through AWS Resource Access Manager (AWS RAM). A UDF principal can still receive Lake Formation permissions on tables in another account.