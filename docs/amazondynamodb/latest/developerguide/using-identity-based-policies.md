

# Using identity-based policies with Amazon DynamoDB
<a name="using-identity-based-policies"></a>

This topic covers using identity-based AWS Identity and Access Management (IAM) policies with Amazon DynamoDB and provides examples. The examples show how an account administrator can attach permissions policies to IAM identities (users, groups, and roles) and thereby grant permissions to perform operations on Amazon DynamoDB resources.

The sections in this topic cover the following:
+ [IAM permissions required to use the Amazon DynamoDB console](#console-permissions)
+ [AWS managed (predefined) IAM policies for Amazon DynamoDB](#access-policy-examples-aws-managed)
+ [Customer managed policy examples](#access-policy-examples-for-sdk-cli)



The following is an example of a permissions policy.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "DescribeQueryScanBooksTable",
            "Effect": "Allow",
            "Action": [
                "dynamodb:DescribeTable",
                "dynamodb:Query",
                "dynamodb:Scan"
            ],
            "Resource": "arn:aws:dynamodb:us-west-2:{{111122223333}}:table/Books"
        }
    ]
}
```

------

 The preceding policy has one statement that grants permissions for three DynamoDB actions (`dynamodb:DescribeTable`, `dynamodb:Query`, and `dynamodb:Scan`) on a table in the `us-west-2` AWS Region, which is owned by the AWS account specified by `{{account-id}}`. The *Amazon Resource Name (ARN)* in the `Resource` value specifies the table that the permissions apply to.

## IAM permissions required to use the Amazon DynamoDB console
<a name="console-permissions"></a>

To work with the DynamoDB console, a user must have a minimum set of permissions that allow the user to work with their AWS account's DynamoDB resources. In addition to these DynamoDB permissions, the console requires permissions:
+ Amazon CloudWatch permissions to display metrics and graphs.
+ AWS Data Pipeline permissions to export and import DynamoDB data. 
+  AWS Identity and Access Management permissions to access roles necessary for exports and imports.
+ Amazon Simple Notification Service permissions to notify you whenever a CloudWatch alarm is triggered.
+ AWS Lambda permissions to process DynamoDB Streams records.

If you create an IAM policy that is more restrictive than the minimum required permissions, the console won't function as intended for users with that IAM policy. To make sure that those users can still use the DynamoDB console, also attach the `AmazonDynamoDBReadOnlyAccess` AWS managed policy to the user, as described in [AWS managed (predefined) IAM policies for Amazon DynamoDB](#access-policy-examples-aws-managed).

You don't need to allow minimum console permissions for users who are making calls only to the AWS CLI or the Amazon DynamoDB API.

**Note**  
 If you refer to a VPC endpoint, you will also need to authorize the DescribeEndpoints API call for the requesting IAM principal(s) with the IAM action (dynamodb:DescribeEndpoints). For more information see [Required policy for endpoints](inter-network-traffic-privacy.md#inter-network-traffic-DescribeEndpoints). 

## AWS managed (predefined) IAM policies for Amazon DynamoDB
<a name="access-policy-examples-aws-managed"></a>

AWS addresses some common use cases by providing standalone IAM policies that are created and administered by AWS. These AWS managed policies grant necessary permissions for common use cases so that you can avoid having to investigate which permissions are needed. For more information, see [AWS Managed Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

The following AWS managed policies, which you can attach to users in your account, are specific to DynamoDB and are grouped by use-case scenario:
+ **AmazonDynamoDBReadOnlyAccess** – Grants read-only access to DynamoDB resources through the AWS Management Console.
+ **AmazonDynamoDBFullAccess** – Grants full access to DynamoDB resources through the AWS Management Console.

You can review these AWS managed permissions policies by signing in to the IAM console and searching for specific policies there.

**Important**  
The best practice is to create custom IAM policies that grant [least-privilege ](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) to the users, roles, or groups that require them. 

## Customer managed policy examples
<a name="access-policy-examples-for-sdk-cli"></a>

In this section, you can find policy examples that grant permissions for various DynamoDB actions. These policies work when you use AWS SDKs or the AWS CLI. When you use the console, you need to grant additional permissions that are specific to the console. For more information, see [IAM permissions required to use the Amazon DynamoDB console](#console-permissions).

**Note**  
All of the following policy examples use one of the AWS Regions and contain fictitious account IDs and table names.

Examples:
+ [IAM policy to grant permissions to all DynamoDB actions on a table](grant-permissions-to-any-action-on-table.md)
+ [IAM policy to grant read-only permissions on items in a DynamoDB table](read-only-permissions-on-table-items.md)
+ [IAM policy to grant access to a specific DynamoDB table and its indexes](iam-policy-specific-table-indexes.md)
+ [IAM policy to read, write, update, and delete access on a DynamoDB table](iam-policy-example-data-crud.md)
+ [IAM policy to separate DynamoDB environments in the same AWS account](iam-policy-separate-environments.md)
+ [IAM policy to prevent the purchase of DynamoDB reserved capacity](iam-prevent-purchase-reserved-capacity.md)
+ [IAM policy to grant read access for a DynamoDB stream only (not for the table)](iam-policy-read-stream-only.md)
+ [IAM policy to allow an AWS Lambda function to access DynamoDB stream records](iam-policy-example-lamda-process-dynamodb-streams.md)
+ [IAM policy for read and write access to a DynamoDB Accelerator (DAX) cluster](iam-policy-example-read-write-dax-access.md)
+ [IAM policy to grant access to search a vector index](iam-policy-example-search-vectors.md)

 The *IAM User Guide*, includes [three additional DynamoDB examples](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_examples.html):
+ [Amazon DynamoDB: Allows Access to a Specific Table](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_dynamodb_specific-table.html)
+ [Amazon DynamoDB: Allows Access to Specific Columns](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_dynamodb_columns.html)
+ [Amazon DynamoDB: Allows Row-Level Access to DynamoDB Based on an Amazon Cognito ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_dynamodb_rows.html)