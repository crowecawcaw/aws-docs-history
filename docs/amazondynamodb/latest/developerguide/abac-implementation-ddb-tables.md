# Using ABAC with DynamoDB tables and indexes

The following steps show how to set up permissions using ABAC. In this example scenario, you'll add tags to a DynamoDB table and create an IAM role with a policy that includes tag-based conditions. Then, you'll test the allowed permissions on the DynamoDB table by matching the tag conditions.

###### Topics

- [Step 1: Add tags to a DynamoDB table](#abac-add-table-tags "#abac-add-table-tags")
- [Step 2: Create an IAM role with a policy including tag-based conditions](#abac-create-iam-role "#abac-create-iam-role")
- [Step 3: Test allowed permissions](#abac-test-permissions "#abac-test-permissions")

## Step 1: Add tags to a DynamoDB table

You can add tags to new or existing DynamoDB tables using the AWS Management Console, AWS API, AWS Command Line Interface (AWS CLI), AWS SDK, or AWS CloudFormation. For example, the following [tag-resource](../../../cli/latest/reference/dynamodb/tag-resource.md "../../../cli/latest/reference/dynamodb/tag-resource.md") CLI command adds a tag to a table named `MusicTable`.

```
aws dynamodb tag-resource —resource-arn arn:aws:dynamodb:`us-east-1`:`123456789012`:table/MusicTable —tags Key=environment,Value=staging
```

## Step 2: Create an IAM role with a policy including tag-based conditions

[Create an IAM policy](../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor") using the [aws:ResourceTag/tag-key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag") condition key to compare the tag key-value pair that's specified in the IAM policy with the key-value pair that's attached to the table. The following example policy allows users to put or update items in tables if these tables contain the tag key-value pair: `"environment": "staging"`. If a table doesn't have the specified tag key-value pair, these actions are denied.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:PutItem",
 "dynamodb:UpdateItem"
 ],
 "Resource": "arn:aws:dynamodb:*:*:table/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/environment": "staging"
 }
 }
 }
 ]
}`

```

## Step 3: Test allowed permissions

1. Attach the IAM policy to a test user or role in your AWS account. Make sure that the IAM principal you use doesn’t already have access to the DynamoDB table through a different policy.
2. Make sure that your DynamoDB table contains the `"environment"` tag key with a value of `"staging"`.
3. Perform the `dynamodb:PutItem` and `dynamodb:UpdateItem` actions on the tagged table. These actions should succeed if the `"environment": "staging"` tag key-value pair is present.

If you perform these actions on a table that doesn’t have the `"environment": "staging"` tag key-value pair, your request will fail with an `AccessDeniedException`.

You can also review the other [sample use cases](abac-example-use-cases.md "abac-example-use-cases.md") described in the following section to implement ABAC and perform more tests.
