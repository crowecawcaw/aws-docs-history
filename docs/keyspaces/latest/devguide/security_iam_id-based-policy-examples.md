

# Amazon Keyspaces identity-based policy examples
<a name="security_iam_id-based-policy-examples"></a>

By default, IAM users and roles don't have permission to create or modify Amazon Keyspaces resources. They also can't perform tasks using the console, CQLSH, AWS CLI, or AWS API. An IAM administrator must create IAM policies that grant users and roles permission to perform specific API operations on the specified resources they need. The administrator must then attach those policies to the IAM users or groups that require those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy documents, see [Creating policies on the JSON tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor) in the *IAM User Guide*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Using the Amazon Keyspaces console](#security_iam_id-based-policy-examples-console)
+ [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)
+ [Accessing Amazon Keyspaces tables](#security_iam_id-based-policy-examples-access-one-table)
+ [Amazon Keyspaces resource access based on tags](#security_iam_id-based-policy-examples-tags)

## Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete Amazon Keyspaces resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

## Using the Amazon Keyspaces console
<a name="security_iam_id-based-policy-examples-console"></a>

Amazon Keyspaces doesn't require specific permissions to access the Amazon Keyspaces console. You need at least read-only permissions to list and view details about the Amazon Keyspaces resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (IAM users or roles) with that policy.

Two AWS managed policies are available to the entities for Amazon Keyspaces console access.
+ [AmazonKeyspacesReadOnlyAccess\_v2](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonKeyspacesReadOnlyAccess_v2.html) – This policy grants read-only access to Amazon Keyspaces.
+ [AmazonKeyspacesFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonKeyspacesFullAccess.html) – This policy grants permissions to use Amazon Keyspaces with full access to all features.

For more information about Amazon Keyspaces managed policies, see [AWS managed policies for Amazon Keyspaces](security-iam-awsmanpol.md).

## Allow users to view their own permissions
<a name="security_iam_id-based-policy-examples-view-own-permissions"></a>

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Accessing Amazon Keyspaces tables
<a name="security_iam_id-based-policy-examples-access-one-table"></a>

**Note**  
To access user keyspaces and tables in Amazon Keyspaces, your IAM policy must include `cassandra:Select` permissions on system tables:  

```
arn:${Partition}:cassandra:${Region}:${Account}:/keyspace/system*
```
This applies to the following scenarios:  
AWS Management Console access
SDK resource operations, for example `GetKeyspace`, `GetTable`, `ListKeyspaces`, and `ListTables`
Standard Apache Cassandra client driver connections, because drivers automatically read system tables during connection initialization
System tables are read-only and cannot be modified.

The following is a sample policy that grants read-only (`SELECT`) access to the Amazon Keyspaces system tables. For all samples, replace the Region and account ID in the Amazon Resource Name (ARN) with your own.

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "cassandra:Select"
         ],
         "Resource":[
            "arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/system*"
         ]
      }
   ]
}
```

The following sample policy adds read-only access to the user table `mytable` in the keyspace `mykeyspace`.

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "cassandra:Select"
         ],
         "Resource":[
            "arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/mykeyspace/table/mytable",
            "arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/system*"
         ]
      }
   ]
}
```

The following sample policy assigns read/write access to a user table and read access to the system tables.

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "cassandra:Select",
            "cassandra:Modify"
         ],
         "Resource":[
            "arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/mykeyspace/table/mytable",
            "arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/system*"
         ]
      }
   ]
}
```

The following sample policy allows a user to create tables in keyspace `mykeyspace`.

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "cassandra:Create",
            "cassandra:Select"
         ],
         "Resource":[
            "arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/mykeyspace/*",
            "arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/system*"
         ]
      }
   ]
}
```

The following sample policy assigns read access to the system tables, but restricts `SELECT` (read) and `MODIFY` (write) access to the user table `mytable`. 

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cassandra:Select"
      ],
      "Resource": [
        "arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/system*"
      ]
    },
    {
      "Effect": "Deny",
      "Action": [
        "cassandra:Select",
        "cassandra:Modify"
      ],
      "Resource": [
        "arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/mykeyspace/table/mytable"
      ]
    }
  ]
}
```

## Amazon Keyspaces resource access based on tags
<a name="security_iam_id-based-policy-examples-tags"></a>

You can use conditions in your identity-based policy to control access to Amazon Keyspaces resources based on tags. These policies control visibility of the keyspaces and tables in the account. Note that tag-based permissions for system tables behave differently when requests are made using the AWS SDK compared to Cassandra Query Language (CQL) API calls via Cassandra drivers and developer tools.
+ To make `List` and `Get` resource requests with the AWS SDK when using tag-based access, the caller needs to have read access to system tables. For example, `Select` action permissions are required to read data from system tables via the `GetTable` operation. If the caller has only tag-based access to a specific table, an operation that requires additional access to a system table will fail.
+ For compatibility with established Cassandra driver behavior, tag-based authorization policies are not enforced when performing operations on system tables using Cassandra Query Language (CQL) API calls via Cassandra drivers and developer tools.

The following example shows how you can create a policy that grants permissions to a user to view a table if the table's `Owner` contains the value of that user's user name. In this example you also give read access to the system tables.

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Sid":"ReadOnlyAccessTaggedTables",
         "Effect":"Allow",
         "Action":"cassandra:Select",
         "Resource":[
            "arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/mykeyspace/table/*",
            "arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/system*"
         ],
         "Condition":{
            "StringEquals":{
               "aws:ResourceTag/Owner":"${aws:username}"
            }
         }
      }
   ]
}
```

You can attach this policy to the IAM users in your account. If a user named `richard-roe` attempts to view an Amazon Keyspaces table, the table must be tagged `Owner=richard-roe` or `owner=richard-roe`. Otherwise, he is denied access. The condition tag key `Owner` matches both `Owner` and `owner` because condition key names are not case-sensitive. For more information, see [IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.

The following policy grants permissions to a user to create tables with tags if the table's `Owner` contains the value of that user's user name.

```
{ 
    "Version": "2012-10-17",		 	 	  
    "Statement": [ 
       { 
          "Sid": "CreateTagTableUser", 
          "Effect": "Allow", 
          "Action": [
              "cassandra:Create", 
              "cassandra:TagResource"
          ], 
          "Resource": "arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/mykeyspace/table/*", 
          "Condition":{
             "StringEquals":{
                "aws:RequestTag/Owner":"${aws:username}"
            }
         }
      }
   ]
}
```