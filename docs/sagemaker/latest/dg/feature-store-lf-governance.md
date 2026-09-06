

# Enable Lake Formation with Feature Groups
<a name="feature-store-lf-governance"></a>

When you enable AWS Lake Formation on a feature group in Amazon SageMaker Feature Store, you can enforce column-level, row-level, and cell-level security for the feature data in your offline store. Instead of managing access through individual IAM policies on Amazon S3 and AWS Glue resources, you use the Lake Formation grant and revoke permission model to control which users and roles can access specific features and records. For more information about Lake Formation, see the [AWS Lake Formation Developer Guide](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html).

**Important**  
Lake Formation access control applies to the offline store only. The offline store is backed by Amazon S3 and registered in the AWS Glue Data Catalog, which Lake Formation governs. Online store access continues to be controlled through IAM policies. To set up Lake Formation, you use the `FeatureGroupManager` and `LakeFormationConfig` classes from the SageMaker AI Python SDK (`sagemaker.mlops.feature_store`). Lake Formation supports [hybrid access mode](https://docs.aws.amazon.com/lake-formation/latest/dg/hybrid-access-mode.html), which allows both IAM policies and Lake Formation permissions to coexist during a gradual migration.

## Prerequisites
<a name="feature-store-lf-prerequisites"></a>

Before you enable Lake Formation, verify that you have the following:
+ A SageMaker AI feature group with an offline store configured, or you can create a new one with an offline store as part of the setup. Lake Formation requires an offline store because it governs access through the AWS Glue Data Catalog table that the offline store creates.
+ An IAM execution role with appropriate permissions. The following example shows the minimum IAM policy required. Replace the placeholder values with your own.

  ```
  {
      "Version": "2012-10-17", 		 	 	 
      "Statement": [
          {
              "Sid": "SageMakerFeatureGroupOperations",
              "Effect": "Allow",
              "Action": [
                  "sagemaker:CreateFeatureGroup",
                  "sagemaker:DescribeFeatureGroup"
              ],
              "Resource": "arn:aws:sagemaker:*:*:feature-group/*"
          },
          {
              "Sid": "LakeFormation",
              "Effect": "Allow",
              "Action": [
                  "lakeformation:RegisterResource",
                  "lakeformation:GrantPermissions",
                  "lakeformation:RevokePermissions",
                  "lakeformation:ListPermissions"
              ],
              "Resource": "*"
          },
          {
              "Sid": "GlueCatalogReadAccess",
              "Effect": "Allow",
              "Action": [
                  "glue:GetTable",
                  "glue:GetDatabase"
              ],
              "Resource": [
                  "arn:aws:glue:*:*:catalog",
                  "arn:aws:glue:*:*:database/sagemaker_featurestore",
                  "arn:aws:glue:*:*:table/sagemaker_featurestore/*"
              ]
          },
          {
              "Sid": "GlueCatalogTableCreate",
              "Effect": "Allow",
              "Action": [
                  "glue:CreateTable"
              ],
              "Resource": [
                  "arn:aws:glue:*:*:catalog",
                  "arn:aws:glue:*:*:database/sagemaker_featurestore",
                  "arn:aws:glue:*:*:table/sagemaker_featurestore/*"
              ]
          },
          {
              "Sid": "PassOfflineStoreRole",
              "Effect": "Allow",
              "Action": "iam:PassRole",
              "Resource": "arn:aws:iam::<account-id>:role/<offline-store-role-name>"
          },
          {
              "Sid": "S3FeatureStoreStorage",
              "Effect": "Allow",
              "Action": [
                  "s3:GetBucketAcl",
                  "s3:GetBucketLocation",
                  "s3:ListBucket"
              ],
              "Resource": "arn:aws:s3:::<offline-store-bucket-name>"
          },
          {
              "Sid": "LakeFormationRegistrationRole",
              "Effect": "Allow",
              "Action": [
                  "iam:GetRole",
                  "iam:GetRolePolicy"
              ],
              "Resource": "arn:aws:iam::<account-id>:role/<registration-role-name>"
          }
      ]
  }
  ```
**Note**  
The `LakeFormationRegistrationRole` statement grants permissions to read the role used to register the Amazon S3 location with Lake Formation. If you use the Lake Formation service-linked role (`use_service_linked_role=True`), set the resource to `arn:aws:iam::<account-id>:role/aws-service-role/lakeformation.amazonaws.com/AWSServiceRoleForLakeFormationDataAccess`. If you provide your own registration role, set it to that role's ARN.
**Note**  
If hybrid access mode is disabled on the `sagemaker_featurestore` database, the caller must also have the Lake Formation `CREATE_TABLE` permission on the database. The Lake Formation administrator can grant this permission through the Lake Formation console or API.
+ A Lake Formation administrator configured in your account. You must designate at least one IAM user or role as a Lake Formation administrator. For setup instructions, see [Getting started with Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-setup.html) in the Lake Formation documentation.
+ The SageMaker AI Python SDK version 3.8.0 or later. Install or upgrade the `sagemaker` package: `pip install --upgrade sagemaker>=3.8.0`
+ Cross-account configuration (if applicable). If the feature group's offline store Amazon S3 bucket is in a different AWS account, additional Lake Formation cross-account sharing configuration is required, including AWS Glue resource policies, AWS RAM share acceptance, resource links, and consumer database setup. For more information, see [Sharing data across accounts](https://docs.aws.amazon.com/lake-formation/latest/dg/sharing-catalog-resources.html) in the Lake Formation documentation.

## Key concepts
<a name="feature-store-lf-concepts"></a>

The following concepts are important for understanding how Lake Formation works with Feature Store.

### Lake Formation permission model compared to IAM-only model
<a name="feature-store-lf-permission-model"></a>

By default, access to AWS Glue Data Catalog tables, including those created by Feature Store, is controlled through IAM policies alone. When you enable Lake Formation, access requires both IAM permissions and Lake Formation permissions. Lake Formation uses a grant and revoke model where you explicitly grant permissions, such as `SELECT` or `DESCRIBE`, on specific databases, tables, or columns to IAM principals.

### Hybrid access mode
<a name="feature-store-lf-hybrid-access"></a>

When you enable Lake Formation, you choose whether to use hybrid access mode or Lake Formation-only mode:
+ **Hybrid access mode** (`hybrid_access_mode_enabled=True`): Both IAM policies and Lake Formation permissions are evaluated. Principals that have access through existing IAM policies continue to have access, and you can additionally grant fine-grained access through Lake Formation. This is useful for gradual migration.
+ **Lake Formation-only mode** (`hybrid_access_mode_enabled=False`): Only Lake Formation permissions are evaluated. Existing IAM-based access to the AWS Glue table is revoked. This provides the strongest access control but can break existing workloads.

**Warning**  
When you set `hybrid_access_mode_enabled=False`, the SDK revokes the `IAMAllowedPrincipal` grant on the AWS Glue table. Any existing jobs, notebooks, or pipelines that access this table through IAM permissions alone immediately lose access. Verify that you have granted the necessary Lake Formation permissions to all principals that need access before you disable hybrid access mode.

**Note**  
You must disable hybrid access mode for cross-account access when the table format is Iceberg.

### S3 deny policy
<a name="feature-store-lf-s3-deny-policy"></a>

Even after you enable Lake Formation on the AWS Glue Data Catalog table, users with direct Amazon S3 access (through IAM policies) can bypass Lake Formation by reading the underlying Amazon S3 objects directly. To close this gap, apply an Amazon S3 bucket policy that denies direct access to the offline store prefix for all principals except the Lake Formation service role and the Feature Store execution role.

**Important**  
The SDK does not automatically apply the Amazon S3 deny policy. After you enable Lake Formation, the SDK logs a recommended bucket policy as a warning message. Review this policy and apply it to your Amazon S3 bucket to enforce access control end-to-end.

## Configuration reference
<a name="feature-store-lf-configuration"></a>

Use the `LakeFormationConfig` class to configure Lake Formation. You pass this configuration to `FeatureGroupManager.create()` when creating a new feature group, or use the individual parameters directly with `enable_lake_formation()` for existing feature groups.


| Parameter | Type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| enabled | bool | False | No | Set to True to activate Lake Formation on the feature group's offline store. | 
| use\_service\_linked\_role | bool | True | No | Whether to use the Lake Formation service-linked role for registering the S3 location. Set to False if you use a custom registration role. You cannot use a service-linked role for cross-account access or when using third-party query engines (such as Apache Spark). For third-party engines, you must provide your own registration role through registration\_role\_arn. | 
| registration\_role\_arn | str | None | Conditional | The ARN of a custom IAM role for registering the offline store S3 location with Lake Formation. Required when use\_service\_linked\_role is False. | 
| hybrid\_access\_mode\_enabled | bool | — | Yes | Whether to revoke IAMAllowedPrincipal from the AWS Glue table. False = Lake Formation-only permissions. True = hybrid mode (both IAM and Lake Formation). You must explicitly choose. | 
| acknowledge\_risk | bool | — | Yes | Must be True to proceed. This is a safety confirmation. Setting to False raises a RuntimeError before any operations are performed. | 

### Understanding acknowledge\_risk
<a name="feature-store-lf-acknowledge-risk"></a>

The `acknowledge_risk` parameter is a safety gate. By setting it to `True`, you acknowledge the following:
+ If `hybrid_access_mode_enabled=False`: Existing IAM-based jobs, notebooks, and pipelines that query this AWS Glue table lose access immediately. You must grant Lake Formation permissions to those principals before or shortly after enabling.
+ If Lake Formation permissions are not correctly configured: The data in the feature group might become inaccessible to all users until permissions are corrected.
+ The operation modifies AWS Glue Data Catalog permissions: These changes affect all consumers of the AWS Glue table, not just Feature Store users. Any Athena queries, Spark jobs, or other services that read from this table are affected.

## How it works
<a name="feature-store-lf-how-it-works"></a>

When you enable Lake Formation, the SDK performs a three-phase setup:

1. **Register the S3 location.** The SDK registers the offline store's S3 path with Lake Formation using either the Lake Formation service-linked role or a custom registration role you specify. If you use third-party query engines (such as Apache Spark), you must provide your own registration role because the service-linked role does not support third-party engine access.

1. **Grant Lake Formation permissions.** The SDK grants `SELECT`, `INSERT`, `DELETE`, `DESCRIBE`, and `ALTER` permissions on the AWS Glue Data Catalog table to the feature group's execution role.

1. **Optionally revoke IAMAllowedPrincipal.** If you set `hybrid_access_mode_enabled=False`, the SDK revokes the `IAMAllowedPrincipal` grant on the AWS Glue table.

After all phases complete, the SDK logs a recommended S3 bucket deny policy. Review and apply this policy to prevent direct Amazon S3 access that bypasses Lake Formation access control.

**Note**  
If the setup fails partway through (for example, after registering the S3 location but before granting permissions), you can safely rerun the `enable_lake_formation()` method. The SDK is idempotent and skips steps that have already completed successfully.

## Usage examples
<a name="feature-store-lf-examples"></a>

### Create a new feature group with Lake Formation access control
<a name="feature-store-lf-example-new-fg"></a>

The following example creates a new feature group with an offline store and enables Lake Formation access control in a single operation.

```
from sagemaker.core.helper.session_helper import Session
from sagemaker.core.shapes import (
    FeatureDefinition,
    OfflineStoreConfig,
    OnlineStoreConfig,
    S3StorageConfig,
)
from sagemaker.mlops.feature_store import FeatureGroupManager, LakeFormationConfig

session = Session()
region = session.boto_region_name

role_arn = "arn:aws:iam::<account-id>:role/<execution-role-name>"
registration_role_arn = "arn:aws:iam::<account-id>:role/<registration-role-name>"
fg_name = "my-feature-group"
bucket = session.default_bucket()
offline_s3_uri = f"s3://{bucket}/feature-store/{fg_name}"

feature_definitions = [
    FeatureDefinition(feature_name="customer_id", feature_type="String"),
    FeatureDefinition(feature_name="event_time", feature_type="String"),
    FeatureDefinition(feature_name="age", feature_type="Integral"),
    FeatureDefinition(feature_name="total_purchases", feature_type="Integral"),
    FeatureDefinition(feature_name="avg_order_value", feature_type="Fractional"),
]

fg = FeatureGroupManager.create(
    feature_group_name=fg_name,
    record_identifier_feature_name="customer_id",
    event_time_feature_name="event_time",
    feature_definitions=feature_definitions,
    online_store_config=OnlineStoreConfig(enable_online_store=False),
    offline_store_config=OfflineStoreConfig(
        s3_storage_config=S3StorageConfig(s3_uri=offline_s3_uri),
        table_format="Iceberg",
    ),
    role_arn=role_arn,
    description="A feature group with Lake Formation-managed offline store",
    # Example configuration — adjust parameters for your use case.
    lake_formation_config=LakeFormationConfig(
        enabled=True,
        use_service_linked_role=False,
        registration_role_arn=registration_role_arn,
        # Set to True to keep existing IAM-based access (hybrid mode).
        hybrid_access_mode_enabled=False,
        acknowledge_risk=True,
    ),
    region=region,
)
```

### Enable Lake Formation on an existing feature group
<a name="feature-store-lf-example-existing-fg"></a>

The following example enables Lake Formation on a feature group that already exists.

```
from sagemaker.mlops.feature_store import FeatureGroupManager

fg = FeatureGroupManager.get(feature_group_name="my-existing-feature-group")
result = fg.enable_lake_formation(
    use_service_linked_role=False,
    registration_role_arn="arn:aws:iam::<account-id>:role/<registration-role-name>",
    hybrid_access_mode_enabled=False,
    acknowledge_risk=True,
)
```

## Use Lake Formation-enabled feature groups with SageMaker AI jobs
<a name="feature-store-lf-sagemaker-jobs"></a>

You can access Lake Formation-enabled feature groups from SageMaker AI training and processing jobs. To read Lake Formation-enabled feature data, you can either query the data through Athena or use the Lake Formation [GetTemporaryGlueTableCredentials](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetTemporaryGlueTableCredentials.html) API to vend temporary Amazon S3 credentials scoped to the AWS Glue table. For more information about configuring Lake Formation permissions for compute roles, see [Lake Formation permissions reference](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-reference.html) in the Lake Formation documentation.

## Cross-account access
<a name="feature-store-lf-cross-account"></a>

Lake Formation supports sharing feature group data across AWS accounts. When the producer account enables Lake Formation on a feature group, it can grant cross-account access to consumer accounts using either the named resource method or Lake Formation tag-based access control (LF-TBAC).

Cross-account sharing requires the following setup:

1. The producer account grants cross-account permissions on the AWS Glue Data Catalog table to the consumer account, AWS Organization, or organizational unit.

1. If the accounts are not in the same AWS Organization, the consumer account accepts the AWS RAM resource share invitation. For more information, see [Accepting a resource share invitation](https://docs.aws.amazon.com/lake-formation/latest/dg/accepting-ram-invite.html).

1. The consumer account creates a resource link to the shared table in a local database. Resource links are required for services such as Athena and Amazon Redshift Spectrum to query shared resources. For more information, see [About resource links](https://docs.aws.amazon.com/lake-formation/latest/dg/resource-links-about.html).

1. The Lake Formation administrator in the consumer account grants permissions on the resource link and the underlying shared table to the IAM principals that need access.

**Important**  
If you use third-party query engines (such as Apache Spark), you must enable full table access for the shared table. Third-party engines require full table credential vending because they do not support Lake Formation's column-level or cell-level filtering through session tags. You must also register the Amazon S3 location with a custom registration role instead of the service-linked role. For more information, see [Full table access for third-party engines](https://docs.aws.amazon.com/lake-formation/latest/dg/full-table-credential-vending.html).

For prerequisites, step-by-step instructions, and best practices for cross-account sharing, see the following topics in the AWS Lake Formation Developer Guide:
+ [Cross-account access](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-permissions.html) — Overview of cross-account sharing methods and AWS RAM integration.
+ [Cross-account prerequisites](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-prereqs.html) — Required configuration for both producer and consumer accounts.
+ [Sharing Data Catalog tables and databases](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-data-share-steps.html) — Step-by-step instructions for both the named resource method and LF-TBAC method.
+ [Tag-based access control](https://docs.aws.amazon.com/lake-formation/latest/dg/tag-based-access-control.html) — Recommended for managing permissions at scale across multiple accounts.

## Grant fine-grained access after setup
<a name="feature-store-lf-fine-grained-access"></a>

After you enable Lake Formation, the Lake Formation administrator can grant fine-grained permissions to other IAM principals using the Lake Formation console, API, or CLI. Lake Formation supports column-level, row-level, and cell-level access control.

For instructions on granting and managing Lake Formation permissions, see the following topics in the AWS Lake Formation Developer Guide:
+ [Granting and revoking Data Catalog permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-catalog-permissions.html)
+ [Data filters in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filters-about.html) for row-level and cell-level filtering
+ [Lake Formation permissions reference](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-reference.html)