

# Setting up access to an Amazon S3 bucket
<a name="USER_PostgreSQL.S3Import.AccessPermission"></a>

To import data from an Amazon S3 file, give the RDS for PostgreSQL DB instance permission to access the Amazon S3 bucket containing the file. You provide access to an Amazon S3 bucket in one of two ways, as described in the following topics.

**Topics**
+ [Using an IAM role to access an Amazon S3 bucket](#USER_PostgreSQL.S3Import.ARNRole)
+ [Using security credentials to access an Amazon S3 bucket](#USER_PostgreSQL.S3Import.Credentials)
+ [Troubleshooting access to Amazon S3](#USER_PostgreSQL.S3Import.troubleshooting)

## Using an IAM role to access an Amazon S3 bucket
<a name="USER_PostgreSQL.S3Import.ARNRole"></a>

Before you load data from an Amazon S3 file, give your RDS for PostgreSQL DB instance permission to access the Amazon S3 bucket the file is in. This way, you don't have to manage additional credential information or provide it in the [aws\_s3.table\_import\_from\_s3](USER_PostgreSQL.S3Import.Reference.md#aws_s3.table_import_from_s3) function call.

To do this, create an IAM policy that provides access to the Amazon S3 bucket. Create an IAM role and attach the policy to the role. Then assign the IAM role to your DB instance. 

**To give an RDS for PostgreSQL DB instance access to Amazon S3 through an IAM role**

1. Create an IAM policy. 

   This policy provides the bucket and object permissions that allow your RDS for PostgreSQL DB instance to access Amazon S3. 

   Include in the policy the following required actions to allow the transfer of files from an Amazon S3 bucket to Amazon RDS: 
   + `s3:GetObject` 
   + `s3:ListBucket` 

   Include in the policy the following resources to identify the Amazon S3 bucket and objects in the bucket. This shows the Amazon Resource Name (ARN) format for accessing Amazon S3.
   + arn:aws:s3:::{{amzn-s3-demo-bucket}}
   + arn:aws:s3:::{{amzn-s3-demo-bucket}}/\*

   For more information on creating an IAM policy for RDS for PostgreSQL, see [Creating and using an IAM policy for IAM database access](UsingWithRDS.IAMDBAuth.IAMPolicy.md). See also [Tutorial: Create and attach your first customer managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_managed-policies.html) in the *IAM User Guide*.

   The following AWS CLI command creates an IAM policy named `rds-s3-import-policy` with these options. It grants access to a bucket named {{amzn-s3-demo-bucket}}. 
**Note**  
Make a note of the Amazon Resource Name (ARN) of the policy returned by this command. You need the ARN in a subsequent step when you attach the policy to an IAM role.  
**Example**  

   For Linux, macOS, or Unix:

   ```
   aws iam create-policy \
      --policy-name rds-s3-import-policy \
      --policy-document '{
        "Version": "2012-10-17",		 	 	 
        "Statement": [
          {
            "Sid": "s3import",
            "Action": [
              "s3:GetObject",
              "s3:ListBucket"
            ],
            "Effect": "Allow",
            "Resource": [
              "arn:aws:s3:::{{amzn-s3-demo-bucket}}", 
              "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
            ] 
          }
        ] 
      }'
   ```

   For Windows:

   ```
   aws iam create-policy ^
      --policy-name rds-s3-import-policy ^
      --policy-document '{
        "Version": "2012-10-17",		 	 	 
        "Statement": [
          {
            "Sid": "s3import",
            "Action": [
              "s3:GetObject",
              "s3:ListBucket"
            ], 
            "Effect": "Allow",
            "Resource": [
              "arn:aws:s3:::{{amzn-s3-demo-bucket}}", 
              "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
            ] 
          }
        ] 
      }'
   ```

1. Create an IAM role. 

   You do this so Amazon RDS can assume this IAM role to access your Amazon S3 buckets. For more information, see [Creating a role to delegate permissions to an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.

   We recommend using the `[aws:SourceArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn)` and `[aws:SourceAccount](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount)` global condition context keys in resource-based policies to limit the service's permissions to a specific resource. This is the most effective way to protect against the [confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html). 

   If you use both global condition context keys and the `aws:SourceArn` value contains the account ID, the `aws:SourceAccount` value and the account in the `aws:SourceArn` value must use the same account ID when used in the same policy statement.
   + Use `aws:SourceArn` if you want cross-service access for a single resource. 
   + Use `aws:SourceAccount` if you want to allow any resource in that account to be associated with the cross-service use.

   In the policy, be sure to use the `aws:SourceArn` global condition context key with the full ARN of the resource. The following example shows how to do so using the AWS CLI command to create a role named `rds-s3-import-role`.   
**Example**  

   For Linux, macOS, or Unix:

   ```
   aws iam create-role \
      --role-name rds-s3-import-role \
      --assume-role-policy-document '{
        "Version": "2012-10-17",		 	 	 
        "Statement": [
          {
            "Effect": "Allow",
            "Principal": {
               "Service": "rds.amazonaws.com"
             },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                   "aws:SourceAccount": "{{111122223333}}",
                   "aws:SourceArn": "{{arn:aws:rds:us-east-1:111122223333:db:dbname}}"
                   }
                }
          }
        ] 
      }'
   ```

   For Windows:

   ```
   aws iam create-role ^
      --role-name rds-s3-import-role ^
      --assume-role-policy-document '{
        "Version": "2012-10-17",		 	 	 
        "Statement": [
          {
            "Effect": "Allow",
            "Principal": {
               "Service": "rds.amazonaws.com"
             },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                   "aws:SourceAccount": "{{111122223333}}",
                   "aws:SourceArn": "{{arn:aws:rds:us-east-1:111122223333:db:dbname}}"
                   }
                }
          }
        ] 
      }'
   ```

1. Attach the IAM policy that you created to the IAM role that you created.

   The following AWS CLI command attaches the policy created in the previous step to the role named `rds-s3-import-role` Replace `{{your-policy-arn}}` with the policy ARN that you noted in an earlier step.   
**Example**  

   For Linux, macOS, or Unix:

   ```
   aws iam attach-role-policy \
      --policy-arn {{your-policy-arn}} \
      --role-name rds-s3-import-role
   ```

   For Windows:

   ```
   aws iam attach-role-policy ^
      --policy-arn {{your-policy-arn}} ^
      --role-name rds-s3-import-role
   ```

1. Add the IAM role to the DB instance. 

   You do so by using the AWS Management Console or AWS CLI, as described following. 

### Console
<a name="collapsible-section-1"></a>

**To add an IAM role for a PostgreSQL DB instance using the console**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Choose the PostgreSQL DB instance name to display its details.

1. On the **Connectivity & security** tab, in the **Manage IAM roles **section, choose the role to add under **Add IAM roles to this instance **. 

1. Under **Feature**, choose **s3Import**.

1. Choose **Add role**.

### AWS CLI
<a name="collapsible-section-2"></a>

**To add an IAM role for a PostgreSQL DB instance using the CLI**
+ Use the following command to add the role to the PostgreSQL DB instance named `my-db-instance`. Replace {{`your-role-arn`}} with the role ARN that you noted in a previous step. Use `s3Import` for the value of the `--feature-name` option.   
**Example**  

  For Linux, macOS, or Unix:

  ```
  aws rds add-role-to-db-instance \
     --db-instance-identifier {{my-db-instance}} \
     --feature-name s3Import \
     --role-arn {{your-role-arn}}   \
     --region {{your-region}}
  ```

  For Windows:

  ```
  aws rds add-role-to-db-instance ^
     --db-instance-identifier {{my-db-instance}} ^
     --feature-name s3Import ^
     --role-arn {{your-role-arn}} ^
     --region {{your-region}}
  ```

### RDS API
<a name="collapsible-section-3"></a>

To add an IAM role for a PostgreSQL DB instance using the Amazon RDS API, call the [ AddRoleToDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_AddRoleToDBInstance.html) operation. 

## Using security credentials to access an Amazon S3 bucket
<a name="USER_PostgreSQL.S3Import.Credentials"></a>

If you prefer, you can use security credentials to provide access to an Amazon S3 bucket instead of providing access with an IAM role. You do so by specifying the `credentials` parameter in the [aws\_s3.table\_import\_from\_s3](USER_PostgreSQL.S3Import.Reference.md#aws_s3.table_import_from_s3) function call. 

The `credentials` parameter is a structure of type `aws_commons._aws_credentials_1`, which contains AWS credentials. Use the [aws\_commons.create\_aws\_credentials](USER_PostgreSQL.S3Import.Reference.md#USER_PostgreSQL.S3Import.create_aws_credentials) function to set the access key and secret key in an `aws_commons._aws_credentials_1` structure, as shown following. 

```
postgres=> SELECT aws_commons.create_aws_credentials(
   '{{sample_access_key}}', '{{sample_secret_key}}', '')
AS creds \gset
```

After creating the `aws_commons._aws_credentials_1 `structure, use the [aws\_s3.table\_import\_from\_s3](USER_PostgreSQL.S3Import.Reference.md#aws_s3.table_import_from_s3) function with the `credentials` parameter to import the data, as shown following.

```
postgres=> SELECT aws_s3.table_import_from_s3(
   't', '', '(format csv)',
   :'s3_uri', 
   :'creds'
);
```

Or you can include the [aws\_commons.create\_aws\_credentials](USER_PostgreSQL.S3Import.Reference.md#USER_PostgreSQL.S3Import.create_aws_credentials) function call inline within the `aws_s3.table_import_from_s3` function call.

```
postgres=> SELECT aws_s3.table_import_from_s3(
   't', '', '(format csv)',
   :'s3_uri', 
   aws_commons.create_aws_credentials('{{sample_access_key}}', '{{sample_secret_key}}', '')
);
```

## Troubleshooting access to Amazon S3
<a name="USER_PostgreSQL.S3Import.troubleshooting"></a>

If you encounter connection problems when attempting to import data from Amazon S3, see the following for recommendations:
+ [Troubleshooting Amazon RDS identity and access](security_iam_troubleshoot.md)
+ [Troubleshooting Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/troubleshooting.html) in the *Amazon Simple Storage Service User Guide*
+ [Troubleshooting Amazon S3 and IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_iam-s3.html) in the *IAM User Guide*