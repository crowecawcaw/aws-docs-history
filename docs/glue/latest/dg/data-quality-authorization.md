

# Configure IAM permissions for AWS Glue Data Quality

This topic provides information to help you understand the actions and resources that you an IAM administrator can use in an AWS Identity and Access Management (IAM) policy for AWS Glue Data Quality. It also includes sample IAM policies with the minimum permissions you need to use AWS Glue Data Quality with the AWS Glue Data Catalog.

For additional information about security in AWS Glue, see [Security in AWS Glue](security.md).

## IAM permissions for AWS Glue Data Quality
<a name="data-quality-authorization-permissions"></a>

The following table lists the permissions that a user needs in order to perform specific AWS Glue Data Quality operations. To set fine-grained authorization for AWS Glue Data Quality, you can specify these actions in the `Action` element of an IAM policy statement. 


**AWS Glue Data Quality actions**  

| Action | Description | Resource types | 
| --- | --- | --- | 
| glue:CreateDataQualityRuleset | Grants permission to create a data quality ruleset. | ::dataQualityRuleset/<name> | 
| glue:DeleteDataQualityRuleset | Grants permission to delete a data quality ruleset. | ::dataQualityRuleset/<name> | 
| glue:GetDataQualityRuleset | Grants permission to retrieve a data quality ruleset. | ::dataQualityRuleset/<name> | 
| glue:ListDataQualityRulesets | Grants permission to retrieve all data quality rulesets. | ::dataQualityRuleset/\* | 
| glue:UpdateDataQualityRuleset | Grants permission to update a data quality ruleset. | ::dataQualityRuleset/<name> | 
| glue:GetDataQualityResult |  Grants permission to retrieve a data quality task run result. This IAM action also provides permissions to the following APIS: +  `BatchGetDataQualityQualityResult` <br />+  `ListDataQualityStatistics` <br />+  `ListDataQualityStatisticAnnotations`   | ::dataQualityRuleset/<name> | 
| glue:ListDataQualityResults | Grants permission to retrieve all data quality task run results. | ::dataQualityRuleset/\* | 
| glue:CancelDataQualityRuleRecommendationRun | Grants permission to stop an in-progress data quality recommendation task run. | ::dataQualityRuleset/\* | 
| glue:GetDataQualityRuleRecommendationRun | Grants permission to retrieve a data quality recommendation task run. | ::dataQualityRuleset/\* | 
| glue:ListDataQualityRuleRecommendationRuns | Grants permission to retrieve all data quality recommendation task runs. | ::dataQualityRuleset/\* | 
| glue:StartDataQualityRuleRecommendationRun | Grants permission to start a data quality recommendation task run. | ::dataQualityRuleset/\* | 
| glue:CancelDataQualityRulesetEvaluationRun | Grants permission to stop an in-progress data quality task run. | ::dataQualityRuleset/\* | 
| glue:GetDataQualityRulesetEvaluationRun | Grants permission to retrieve a data quality task run. | ::dataQualityRuleset/\* | 
| glue:ListDataQualityRulesetEvaluationRuns | Grants permission to retrieve all data quality task runs. | ::dataQualityRuleset/\* | 
| glue:StartDataQualityRulesetEvaluationRun | Grants permission to start a data quality task run. | ::dataQualityRuleset/<name> | 
| glue:PublishDataQuality | Grants permission to publish data quality results. | ::dataQualityRuleset/<name> | 
| glue:GetDataQualityModel | Grants permission to retrieve Data Quality Model. | ::dataQualityRuleset/<name>, ::job/<name>  | 
| glue:GetDataQualityModelResult | Grants permission to retrieve Data Quality Model Results. | ::dataQualityRuleset/<name>, ::job/<name>  | 
| glue:PutDataQualityStatisticAnnotation |  Grants permission to add annotations to Statistics. This IAM action also provides permissions to the following APIS: +   `BatchPutDataQualityStatisticAnnotation`    | ::dataQualityRuleset/<name>, ::job/<name>  | 
| glue:PutDataQualityProfileAnnotation | Grants permission to put annotations to all Statistics in a Profile. | ::dataQualityRuleset/<name>, ::job/<name>  | 
| glue:CreateDataQualityEvaluationConfig | Grants permission to create a data quality evaluation configuration. If you specify tags, you also need glue:TagResource. | ::dataQualityEvaluationConfig/<name> | 
| glue:GetDataQualityEvaluationConfig | Grants permission to retrieve a data quality evaluation configuration. | ::dataQualityEvaluationConfig/<name> | 
| glue:UpdateDataQualityEvaluationConfig | Grants permission to update a data quality evaluation configuration. | ::dataQualityEvaluationConfig/<name> | 
| glue:DeleteDataQualityEvaluationConfig | Grants permission to delete a data quality evaluation configuration. | ::dataQualityEvaluationConfig/<name> | 
| glue:ListDataQualityEvaluationConfigs | Grants permission to retrieve all data quality evaluation configurations. | ::dataQualityEvaluationConfig/\* | 

## IAM setup required for scheduling evaluation runs
<a name="data-quality-iam-setup-evaluation-runs"></a>

### IAM permissions
<a name="data-quality-iam-setup-evaluation-runs-permissions"></a>

To run scheduled Data Quality evaluation runs, you must add the `IAM:PassRole` action to the permissions policy.


**AWS EventBridge Scheduler required permissions**  

| Action | Description | Resource types | 
| --- | --- | --- | 
| iam:PassRole | Grants permission for IAM to allow the user to pass the approved roles. | ARN of the role used to call StartDataQualityRulesetEvaluationRun | 

Without these permissions the following error occurs:

```
"errorCode": "AccessDenied"
"errorMessage": "User: arn:aws:sts::account_id:assumed-role/AWSGlueServiceRole is not 
authorized to perform: iam:PassRole on resource: arn:aws:iam::account_id:role/service-role/AWSGlueServiceRole 
because no identity-based policy allows the iam:PassRole action"
```

### IAM trusted entities
<a name="data-quality-iam-setup-evaluation-runs-trusted-entities"></a>

The AWS Glue and AWS EventBridge Scheduler services need to be listed in the trusted entities in order to create and run a scheduled `StartDataQualityEvaluationRun`.

------
#### [ JSON ]

****  

```json
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "glue.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    },
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "scheduler.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

------

## IAM permissions for data quality evaluation configurations
<a name="data-quality-authorization-evaluation-configs"></a>

A data quality evaluation configuration involves two sets of permissions:
+ **Caller permissions** – The permissions that you need to create and manage configurations, pass the configuration's role, and read the results.
+ **Role permissions** – The permissions that the configuration's role needs so that AWS Glue Data Quality can find the tables in scope, start an evaluation run for each table, and read each table's data during the run.

For an overview of evaluation configurations, see [Data quality monitoring at the catalog and database level](data-quality-catalog-monitoring.md).

### Permissions to manage evaluation configurations
<a name="data-quality-authorization-evaluation-configs-caller"></a>

The following identity-based policy allows a user to manage evaluation configurations and read their results. It includes the following permissions:
+ The evaluation configuration actions. Each action authorizes the configuration's ARN, so you can limit access to specific configurations by name or by tag.
+ `glue:TagResource`, which you need to create a configuration with tags and to tag it later.
+ `glue:GetCatalog`, `glue:GetDatabase`, and `glue:GetTable`. When you create or update a configuration, AWS Glue checks that you can describe the catalog, database, or table that it applies to.
+ `iam:PassRole` for the configuration's role. You need this permission whenever you specify the role in a create or update request.
+ Actions to read evaluation runs and results.

```JSON
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ManageEvaluationConfigs",
      "Effect": "Allow",
      "Action": [
        "glue:CreateDataQualityEvaluationConfig",
        "glue:GetDataQualityEvaluationConfig",
        "glue:UpdateDataQualityEvaluationConfig",
        "glue:DeleteDataQualityEvaluationConfig",
        "glue:ListDataQualityEvaluationConfigs",
        "glue:TagResource",
        "glue:UntagResource",
        "glue:GetTags"
      ],
      "Resource": "arn:aws:glue:{{us-east-1}}:111122223333:dataQualityEvaluationConfig/*"
    },
    {
      "Sid": "DescribeConfigurationTargets",
      "Effect": "Allow",
      "Action": [
        "glue:GetCatalog",
        "glue:GetDatabase",
        "glue:GetTable"
      ],
      "Resource": [
        "arn:aws:glue:{{us-east-1}}:111122223333:catalog",
        "arn:aws:glue:{{us-east-1}}:111122223333:database/{{database-name}}",
        "arn:aws:glue:{{us-east-1}}:111122223333:table/{{database-name}}/*"
      ]
    },
    {
      "Sid": "ReadEvaluationResults",
      "Effect": "Allow",
      "Action": [
        "glue:ListDataQualityResults",
        "glue:GetDataQualityResult",
        "glue:ListDataQualityRulesetEvaluationRuns",
        "glue:GetDataQualityRulesetEvaluationRun"
      ],
      "Resource": "arn:aws:glue:{{us-east-1}}:111122223333:dataQualityRuleset/*"
    },
    {
      "Sid": "PassEvaluationConfigRole",
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::111122223333:role/DataQualityEvaluationConfigRole",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "glue.amazonaws.com"
        }
      }
    }
  ]
}
```

If you use your own rulesets, also allow `glue:CreateDataQualityRuleset` and `glue:UpdateDataQualityRuleset`. If you use Lake Formation, you also need the `DESCRIBE` permission on the catalog, database, or table to create, get, or update a configuration that applies to it.

If a configuration applies to an Amazon S3 Tables catalog, also allow `lakeformation:GetDataAccess`, and add the Amazon S3 Tables forms of the catalog, database, and table ARNs to the `DescribeConfigurationTargets` statement. For example, for every table bucket in the account, add the following resources:

```JSON
"arn:aws:glue:{{us-east-1}}:111122223333:catalog/s3tablescatalog",
"arn:aws:glue:{{us-east-1}}:111122223333:catalog/s3tablescatalog/*",
"arn:aws:glue:{{us-east-1}}:111122223333:database/s3tablescatalog/*",
"arn:aws:glue:{{us-east-1}}:111122223333:table/s3tablescatalog/*"
```

To control access with tags, use the `aws:RequestTag/{{tag-key}}` and `aws:TagKeys` condition keys with `glue:CreateDataQualityEvaluationConfig`, and the `aws:ResourceTag/{{tag-key}}` condition key with the other actions. For more information, see [Specifying AWS Glue resource ARNs](glue-specifying-resource-arns.md).

### Trust policy for the configuration role
<a name="data-quality-authorization-evaluation-configs-trust"></a>

AWS Glue assumes the configuration's role to find tables and to start each evaluation run, and the evaluation run assumes the role to read the table. Use the following trust policy to allow AWS Glue to assume the role for your account's catalog and tables.

AWS Glue sets [aws:SourceArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) to your catalog's ARN or a table's ARN, and [aws:SourceAccount](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) to your account ID. The trust policy must allow both ARN forms. When you create or update a configuration, AWS Glue checks that it can assume the role with each form.

```JSON
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "glue.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        },
        "ArnLike": {
          "aws:SourceArn": [
            "arn:aws:glue:{{us-east-1}}:111122223333:catalog",
            "arn:aws:glue:{{us-east-1}}:111122223333:table/*"
          ]
        }
      }
    }
  ]
}
```

### Permissions policy for the configuration role
<a name="data-quality-authorization-evaluation-configs-permissions"></a>

The configuration's role needs permissions for each of the following tasks:
+ **Find the tables in scope** – `glue:GetCatalog`, `glue:GetDatabase`, and `glue:GetTable` to describe the catalog, database, or table, and `glue:SearchTables` to list the tables in a catalog or database.
+ **Prepare the ruleset** – `glue:GetDataQualityRuleset` to read the ruleset, and `glue:CreateDataQualityRuleset` and `glue:UpdateDataQualityRuleset` to create and maintain the built-in rulesets in your account.
+ **Start evaluation runs** – `glue:StartDataQualityRulesetEvaluationRun`, and `iam:PassRole` on the role itself, because AWS Glue starts each run with the same role.
+ **Evaluate the data** – The permissions that any data quality evaluation run needs: `glue:GetPartitions`, `glue:GetDataQualityRulesetEvaluationRun`, `glue:PublishDataQuality`, read access to the table's data in Amazon S3, and permissions to write logs to Amazon CloudWatch Logs.

Attach the following permissions policy to the role. Replace the bucket with the locations of your tables' data.

```JSON
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "FindTables",
      "Effect": "Allow",
      "Action": [
        "glue:GetCatalog",
        "glue:GetDatabase",
        "glue:GetTable",
        "glue:SearchTables",
        "glue:GetPartitions"
      ],
      "Resource": [
        "arn:aws:glue:{{us-east-1}}:111122223333:catalog",
        "arn:aws:glue:{{us-east-1}}:111122223333:catalog/*",
        "arn:aws:glue:{{us-east-1}}:111122223333:database/*",
        "arn:aws:glue:{{us-east-1}}:111122223333:table/*"
      ]
    },
    {
      "Sid": "PrepareRulesetsAndStartRuns",
      "Effect": "Allow",
      "Action": [
        "glue:GetDataQualityRuleset",
        "glue:CreateDataQualityRuleset",
        "glue:UpdateDataQualityRuleset",
        "glue:StartDataQualityRulesetEvaluationRun",
        "glue:GetDataQualityRulesetEvaluationRun",
        "glue:PublishDataQuality"
      ],
      "Resource": "arn:aws:glue:{{us-east-1}}:111122223333:dataQualityRuleset/*"
    },
    {
      "Sid": "PassThisRoleToGlue",
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::111122223333:role/DataQualityEvaluationConfigRole",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "glue.amazonaws.com"
        }
      }
    },
    {
      "Sid": "ReadTableData",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
      ]
    },
    {
      "Sid": "WriteRunLogs",
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:{{us-east-1}}:111122223333:log-group:/aws-glue/*"
    }
  ]
}
```

If a condition in this list applies, add the related permissions to the role:
+ If a catalog-level or database-level configuration applies to an Amazon S3 Tables catalog, add `s3tables:ListTableBuckets` and `s3tables:ListTables`. AWS Glue uses these actions instead of `glue:SearchTables` to find the tables in a table bucket.
+ If you use Lake Formation, grant the role the `DESCRIBE` permission on the tables to evaluate. The configuration evaluates only the tables that the role can describe.
+ If Lake Formation manages the tables' data, as it does for all Amazon S3 Tables, add `lakeformation:GetDataAccess` and grant the role the `SELECT` permission on each table, without column or data filters. In the Lake Formation data lake settings, also allow external engines to access data with full table access. For more information, see [Supported source types](data-quality-getting-started.md#data-quality-get-started-supported-source-types).
+ If you set `CloudWatchMetricsEnabled` in the run options, add `cloudwatch:PutMetricData`.
+ If you write results to Amazon S3 with `ResultsS3Prefix`, add `s3:PutObject` on that location. For information about writing results to AWS Glue Data Catalog tables, see [Prerequisites](data-quality-results-catalog-tables.md#data-quality-results-catalog-tables-prereqs).
+ If your data is encrypted with an AWS KMS key, add `kms:Decrypt` on that key.

## Example IAM policies
<a name="data-quality-authorization-example-policy"></a>

An IAM role for AWS Glue Data Quality needs the following types of permissions:
+ Permissions for AWS Glue Data Quality operations so that you can get recommended data quality rules and run a data quality task against a table in the AWS Glue Data Catalog. The example IAM policies in this section include the minimum permissions required for AWS Glue Data Quality operations.
+ Permissions that grant access to your Data Catalog table and the underlying data. These permissions vary depending on your use case. For example, for data that you catalog in Amazon S3, the permissions should include access to Amazon S3. 
**Note**  
You must configure Amazon S3 permissions in addition to the permissions described in this section.

### Minimum permissions to get recommended data quality rules
<a name="example-policy-get-dq-rule-recommendations"></a>

This example policy includes the permissions you need in order to generate recommended data quality rules. 

------
#### [ JSON ]

****  

```json
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowGlueRuleRecommendationRunActions",
      "Effect": "Allow",
      "Action": [
        "glue:GetDataQualityRuleRecommendationRun",
        "glue:PublishDataQuality",
        "glue:CreateDataQualityRuleset"
      ],
      "Resource": "arn:aws:glue:{{us-east-1}}:{{111122223333}}:dataQualityRuleset/*"
    },
	{
     "Sid": "AllowCatalogPermissions",
     "Effect": "Allow",
     "Action": [
        "glue:GetPartitions",
        "glue:GetTable"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Sid": "AllowS3GetObjectToRunRuleRecommendationTask",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::aws-glue-*"
    },
		{
			"Sid": "AllowPublishingCloudwatchLogs",
			"Effect": "Allow",
			"Action": [
			  "logs:CreateLogStream",
			  "logs:CreateLogGroup",
			  "logs:PutLogEvents"
			],
			"Resource": "*"
    }
  ]
}
```

------

### Minimum permissions to get advanced data quality rule recommendations
<a name="example-policy-get-advanced-dq-rule-recommendations"></a>

You must have `iam:PassRole` permission for the recommendation role. The role does not need Amazon Bedrock permissions.

#### Trust policy
<a name="example-policy-get-advanced-dq-rule-recommendations-trust"></a>

Use this trust policy to allow AWS Glue to assume the recommendation role for your source table.

Set [aws:SourceArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) to the full source table ARN. Use the account ID from that ARN for [aws:SourceAccount](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount).

```JSON
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "glue.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        },
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:glue:{{us-east-1}}:111122223333:table/{{database-name}}/{{table-name}}"
        }
      }
    }
  ]
}
```

#### Permissions policy
<a name="example-policy-get-advanced-dq-rule-recommendations-permissions"></a>

On the first `ADVANCED` run, AWS Glue creates the following resources in your account:
+ The `glue-dataquality-sampling` Athena workgroup to run queries for rule recommendations.
+ The `aws-glue-dataquality-sampling-{{account-id}}-{{region}}` Amazon S3 bucket to store query results.

For subsequent runs, AWS Glue reuses the existing workgroup and bucket. For details, see [Data protection for advanced data quality rule recommendations](data-protection-advanced-dq-recommendations.md).

Attach the following permissions policy to your recommendation role.

```JSON
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCatalogRead",
      "Effect": "Allow",
      "Action": [
        "glue:GetDatabase",
        "glue:GetPartitions",
        "glue:GetTable"
      ],
      "Resource": [
        "arn:aws:glue:{{us-east-1}}:111122223333:catalog",
        "arn:aws:glue:{{us-east-1}}:111122223333:database/{{database-name}}",
        "arn:aws:glue:{{us-east-1}}:111122223333:table/{{database-name}}/{{table-name}}"
      ]
    },
    {
      "Sid": "AllowDataQualityRecommendationResults",
      "Effect": "Allow",
      "Action": "glue:PublishDataQuality",
      "Resource": "arn:aws:glue:{{us-east-1}}:111122223333:dataQualityRuleset/*"
    },
    {
      "Sid": "AllowDataAccess",
      "Effect": "Allow",
      "Action": [
        "athena:CreateWorkGroup",
        "athena:GetQueryExecution",
        "athena:GetQueryResults",
        "athena:StartQueryExecution"
      ],
      "Resource": "arn:aws:athena:{{us-east-1}}:111122223333:workgroup/glue-dataquality-sampling"
    },
    {
      "Sid": "AllowSourceRead",
      "Effect": "Allow",
      "Action": [
        "s3:GetBucketLocation",
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::{{source-bucket}}",
        "arn:aws:s3:::{{source-bucket}}/*"
      ]
    },
    {
      "Sid": "AllowSamplingBucket",
      "Effect": "Allow",
      "Action": [
        "s3:AbortMultipartUpload",
        "s3:CreateBucket",
        "s3:GetBucketLocation",
        "s3:GetObject",
        "s3:ListBucket",
        "s3:PutLifecycleConfiguration",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::aws-glue-dataquality-sampling-111122223333-{{us-east-1}}",
        "arn:aws:s3:::aws-glue-dataquality-sampling-111122223333-{{us-east-1}}/athena-results/*"
      ]
    }
  ]
}
```

**Note**  
If the bucket exists, you can remove `s3:CreateBucket` from this policy. If you delete the bucket, AWS Glue needs this permission again. All other permissions in this policy remain necessary for subsequent runs.

#### Additional permissions
<a name="example-policy-get-advanced-dq-rule-recommendations-additional"></a>

If a condition in this list applies, add the related permissions to your recommendation role.
+ If Lake Formation controls table access, add `lakeformation:GetDataAccess`. Grant the role `DESCRIBE` on the database and `DESCRIBE` and `SELECT` on the table.
+ If you specify a data quality security configuration, add `glue:GetSecurityConfiguration` permission.
+ If you specify `CreatedRulesetName`, add `glue:CreateDataQualityRuleset` permission.
+ If you specify a data quality security configuration with a customer managed key, add the following statement for that key.

  ```JSON
  {
    "Sid": "AllowDataQualityEncryption",
    "Effect": "Allow",
    "Action": [
      "kms:Decrypt",
      "kms:DescribeKey",
      "kms:GenerateDataKey",
      "kms:GenerateDataKeyWithoutPlaintext",
      "kms:ReEncrypt*"
    ],
    "Resource": "arn:aws:kms:{{us-east-1}}:111122223333:key/{{key-id}}"
  }
  ```

  Your recommendation role needs these actions for query result encryption and AWS Glue Data Quality asset encryption. The key policy must also allow these actions for your role. For details, see [Key policy](data-quality-encryption.md#data-quality-encryption-customer-managed-key-policy).
+ If the source objects use SSE-KMS, add the following statement.

  ```JSON
  {
    "Sid": "AllowSourceDataDecryption",
    "Effect": "Allow",
    "Action": "kms:Decrypt",
    "Resource": "arn:aws:kms:{{us-east-1}}:111122223333:key/{{source-key-id}}"
  }
  ```

  The source key policy must also allow the recommendation role to decrypt the source objects.

### Minimum permissions to run a data quality task
<a name="example-policy-run-dq-task"></a>

This example policy includes the permissions you need in order to run a data quality evaluation task. 

The following policy statements are optional, depending on your use case:
+ `AllowCloudWatchPutMetricDataToPublishTaskMetrics` - Required if you want to publish data quality run metrics to Amazon CloudWatch.
+ `AllowS3PutObjectToWriteTaskResults` - Required if you want to write data quality run results to Amazon S3.

------
#### [ JSON ]

****  

```json
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowGlueGetDataQualityRuleset",
      "Effect": "Allow",
      "Action": [
        "glue:GetDataQualityRuleset"
      ],
      "Resource": "arn:aws:glue:{{us-east-1}}:{{111122223333}}:dataQualityRuleset/{{YOUR-RULESET-NAME}}"
    },
    {
      "Sid": "AllowGlueRulesetEvaluationRunActions",
      "Effect": "Allow",
      "Action": [
        "glue:GetDataQualityRulesetEvaluationRun",
        "glue:PublishDataQuality"
      ],
      "Resource": "arn:aws:glue:{{us-east-1}}:{{111122223333}}:dataQualityRuleset/*"
    },
    {
      "Sid": "AllowCatalogPermissions",
      "Effect": "Allow",
      "Action": [
        "glue:GetPartitions",
        "glue:GetTable"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Sid": "AllowS3GetObjectForRulesetEvaluationRun",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::aws-glue-*"
    },
    {
      "Sid": "AllowCloudWatchPutMetricDataToPublishTaskMetrics",
      "Effect": "Allow",
      "Action": [
        "cloudwatch:PutMetricData"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "cloudwatch:namespace": "Glue Data Quality"
        }
      }
    },
    {
      "Sid": "AllowS3PutObjectToWriteTaskResults",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject*"
      ],
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
    }
  ]
}
```

------

### Minimum permissions to run an data quality ETL job
<a name="example-policy-run-dq-etl-job"></a>

 This example policy includes the permissions you need in order to run an data quality ETL Job. 

------
#### [ JSON ]

****  

```json
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowGluePublishDataQualityResult",
      "Effect": "Allow",
      "Action": [
        "glue:PublishDataQuality"
      ],
      "Resource": "arn:aws:glue:{{us-east-1}}:{{111122223333}}:dataQualityRuleset/*"
    },
    {
      "Sid": "AllowGlueGetDataQualityResult",
      "Effect": "Allow",
      "Action": [
        "glue:GetDataQualityResult"
      ],
      "Resource": "arn:aws:glue:{{us-east-1}}:{{111122223333}}:dataQualityRuleset/*"
    },
    {
      "Sid": "AllowGlueDataQualityStatisticAnnotation",
      "Effect": "Allow",
      "Action": [
        "glue:PutDataQualityStatisticAnnotation"
      ],
      "Resource": [
        "arn:aws:glue:{{us-east-1}}:{{111122223333}}:dataQualityRuleset/*",
        "arn:aws:glue:{{us-east-1}}:{{111122223333}}::job/{JobName}"
      ]
    },
    {
      "Sid": "AllowGlueDataQualityProfileAnnotation",
      "Effect": "Allow",
      "Action": [
        "glue:PutDataQualityProfileAnnotation"
      ],
      "Resource": [
        "arn:aws:glue:{{us-east-1}}:{{111122223333}}:dataQualityRuleset/*",
        "arn:aws:glue:{{us-east-1}}:{{111122223333}}::job/{JobName}"
      ]
    }
	]
}
```

------