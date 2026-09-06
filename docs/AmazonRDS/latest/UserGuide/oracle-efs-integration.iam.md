

# Configuring IAM permissions for RDS for Oracle integration with Amazon EFS
<a name="oracle-efs-integration.iam"></a>

By default, Amazon EFS integration feature doesn't use an IAM role: the `USE_IAM_ROLE` option setting is `FALSE`. To integrate RDS for Oracle with Amazon EFS and an IAM role, your DB instance must have IAM permissions to access an Amazon EFS file system.

**Topics**
+ [Step 1: Create an IAM role for your DB instance and attach your policy](#oracle-efs-integration.iam.role)
+ [Step 2: Create a file system policy for your Amazon EFS file system](#oracle-efs-integration.iam.policy)
+ [Step 3: Associate your IAM role with your RDS for Oracle DB instance](#oracle-efs-integration.iam.instance)

## Step 1: Create an IAM role for your DB instance and attach your policy
<a name="oracle-efs-integration.iam.role"></a>

In this step, you create a role for your RDS for Oracle DB instance to allow Amazon RDS to access your EFS file system.

### Console
<a name="oracle-efs-integration.iam.role.console"></a>

**To create an IAM role to allow Amazon RDS access to an EFS file system**

1. Open the [IAM Management Console](https://console.aws.amazon.com/iam/home?#home).

1. In the navigation pane, choose **Roles**.

1. Choose **Create role**.

1. For **AWS service**, choose **RDS**.

1. For **Select your use case**, choose **RDS – Add Role to Database**.

1. Choose **Next**.

1. Don't add any permissions policies. Choose **Next**.

1. Set **Role name** to a name for your IAM role, for example `rds-efs-integration-role`. You can also add an optional **Description** value.

1. Choose **Create role**.

### AWS CLI
<a name="integration.preparing.role.CLI"></a>

To limit the service's permissions to a specific resource, we recommend using the [`aws:SourceArn`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) and [`aws:SourceAccount`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) global condition context keys in resource-based trust relationships. This is the most effective way to protect against the [confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html).

You might use both global condition context keys and have the `aws:SourceArn` value contain the account ID. In this case, the `aws:SourceAccount` value and the account in the `aws:SourceArn` value must use the same account ID when used in the same statement.
+ Use `aws:SourceArn` if you want cross-service access for a single resource.
+ Use `aws:SourceAccount` if you want to allow any resource in that account to be associated with the cross-service use.

In the trust relationship, make sure to use the `aws:SourceArn` global condition context key with the full Amazon Resource Name (ARN) of the resources accessing the role.

The following AWS CLI command creates the role named `{{rds-efs-integration-role}}` for this purpose.

**Example**  
For Linux, macOS, or Unix:  

```
aws iam create-role \
   --role-name {{rds-efs-integration-role}} \
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
                 "aws:SourceAccount": "{{my_account_ID}}",
                 "aws:SourceArn": "arn:aws:rds:{{Region}}:{{my_account_ID}}:db:{{dbname}}"
             }
         }
       }
     ]
   }'
```
For Windows:  

```
aws iam create-role ^
   --role-name {{rds-efs-integration-role}} ^
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
                 "aws:SourceAccount": "{{my_account_ID}}",
                 "aws:SourceArn": "arn:aws:rds:{{Region}}:{{my_account_ID}}:db:{{dbname}}"
             }
         }
       }
     ]
   }'
```

For more information, see [Creating a role to delegate permissions to an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.

## Step 2: Create a file system policy for your Amazon EFS file system
<a name="oracle-efs-integration.iam.policy"></a>

In this step, you create a file system policy for your EFS file system.

**To create or edit an EFS file system policy**

1. Open the [EFS Management Console](https://console.aws.amazon.com/efs/home?#home).

1. Choose **File Systems**.

1. On the **File systems** page, choose the file system that you want to edit or create a file system policy for. The details page for that file system is displayed.

1. Choose the **File system policy** tab.

   If the policy is empty, then the default EFS file system policy is in use. For more information, see [Default EFS file system policy](https://docs.aws.amazon.com/efs/latest/ug/iam-access-control-nfs-efs.html#default-filesystempolicy ) in the *Amazon Elastic File System User Guide*.

1. Choose **Edit**. The **File system policy** page appears.

1. In **Policy editor**, enter a policy such as the following, and then choose **Save**.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Id": "ExamplePolicy01",
       "Statement": [
           {
               "Sid": "ExampleStatement01",
               "Effect": "Allow",
               "Principal": {
                   "AWS": "arn:aws:iam::{{123456789012}}:role/rds-efs-integration-role"
               },
               "Action": [
                   "elasticfilesystem:ClientMount",
                   "elasticfilesystem:ClientWrite",
                   "elasticfilesystem:ClientRootAccess"
               ],
               "Resource": "arn:aws:elasticfilesystem:{{us-east-1}}:{{123456789012}}:file-system/{{fs-1234567890abcdef0}}"
           }
       ]
   }
   ```

------

## Step 3: Associate your IAM role with your RDS for Oracle DB instance
<a name="oracle-efs-integration.iam.instance"></a>

In this step, you associate your IAM role with your DB instance. Be aware of the following requirements:
+ You must have access to an IAM role with the required Amazon EFS permissions policy attached to it. 
+ You can associate only one IAM role with your RDS for Oracle DB instance at a time.
+ The status of your instance must be **Available**.

For more information, see [Identity and access management for Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/auth-and-access-control.html) in the *Amazon Elastic File System User Guide*.

### Console
<a name="oracle-efs-integration.iam.instance.console"></a>

**To associate your IAM role with your RDS for Oracle DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Choose **Databases**.

1. If your database instance is unavailable, choose **Actions** and then **Start**. When the instance status shows **Started**, go to the next step.

1. Choose the Oracle DB instance name to display its details.

1. On the **Connectivity & security** tab, in the **Manage IAM roles** section, do the following.

1. Choose the role to add in the **Add IAM roles to this instance** section.

1. For **Feature**, choose **EFS\_INTEGRATION**.

1. Choose **Add role**.

### AWS CLI
<a name="oracle-efs-integration.iam.instance.CLI"></a>

The following AWS CLI command adds the role to an Oracle DB instance named `{{mydbinstance}}`.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds add-role-to-db-instance \
   --db-instance-identifier {{mydbinstance}} \
   --feature-name EFS_INTEGRATION \
   --role-arn {{your-role-arn}}
```
For Windows:  

```
aws rds add-role-to-db-instance ^
   --db-instance-identifier {{mydbinstance}} ^
   --feature-name EFS_INTEGRATION ^
   --role-arn {{your-role-arn}}
```

Replace `{{your-role-arn}}` with the role ARN that you noted in a previous step. `EFS_INTEGRATION` must be specified for the `--feature-name` option.