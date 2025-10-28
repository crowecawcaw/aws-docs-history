# Find Amazon Resource Names (ARNs) in AMS

An Amazon Resource Name (ARN) is a string that uniquely identifies an AWS resource, such as EC2 instances, S3 buckets, accounts, Lambda functions,
and so forth. AWS requires an ARN when you want to specify a resource unambiguously across all of AWS, such as in IAM policies,
Amazon Relational Database Service (Amazon RDS) tags, and API calls. ARNs are constructed from identifiers that specify the service, Region, account, and other information. There are three ARN formats:

```
arn:aws:`service`:`region`:`account-id`:`resource-id`
arn:aws:`service`:`region`:`account-id`:`resource-type`/`resource-id`
arn:aws:`service`:`region`:`account-id`:`resource-type`:`resource-id`
```

###### Note

The exact format of an ARN depends on the service and resource type. To learn more about ARNs, see
[Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") and
[ARN Formats](../../../quicksight/latest/APIReference/qs-arn-format.md "../../../quicksight/latest/APIReference/qs-arn-format.md").

For ARN format examples by resource, see the AWS _Service Authorization Reference_
[resource types table](../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md#resources_table "../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md#resources_table").

Finding the ARN of an AWS object can be difficult. Here are three ways to try:

- AWS service console: Go to the relevant AWS service console, locate the resource and find the ARN in the details for the resource.
- AWS API/CLI (you must first install the AWS CLI): Look for the relevant service in the
  [AWS CLI Command Reference](../../../cli/latest/index.md "../../../cli/latest/index.md"), then, depending on the AWS service, look for the
  relevant operation, such as `describe`, or `get`, and so forth.
  For example, for all IAM roles, policies and users, you can get the ARN in the output from the CLI with:

```
aws iam get-role --role-name `EMR_DefaultRole`
```

- Construct the ARN based on the relevant format: Find the ARN format for the resource, by looking at the
  [Actions, resources, and condition keys for AWS services](../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md "../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md") page, finding the relevant service, and then the relevant action, and drilling down to the resource ARN format.
  Once you have the format, replace the variables with the relevant settings.
  You can construct the ARN yourself by following the appropriate format (the formats change per service and resource type) and filling in the information.
  Here are some ARN examples:

- An AWS account ARN has the following syntax:

```
arn:aws:iam::`ACCOUNT-ID`:root
```

- An S3 ARN has a flat hierarchy of buckets and associated objects:

```
arn:aws:s3:::ams-bucket
```

- An EC2 ARN has sub resource-types like image, security groups, instance, and so forth. This example includes the instance ID at the end:

```
arn:aws:ec2:us-east-1:123456789012:instance/i-012abcd34efghi56
```

- A Lambda ARN has the function name for the resource-id part, and you may need to include the version number at the end, as shown in this example:

```
arn:aws:lambda:us-east-1:123456789012:function:api-function:1
```

The AWS Key Management Service service provides this information:
[Finding the key ID and key ARN](../../../kms/latest/developerguide/find-cmk-id-arn.md "../../../kms/latest/developerguide/find-cmk-id-arn.md").

To find the ARN of a DynamoDB table, use the DynamoDB
[describe-table](../../../cli/latest/reference/dynamodb/describe-table.md "../../../cli/latest/reference/dynamodb/describe-table.md") CLI.

For an outsider's look at finding AWS ARNs, see
[AWS ARN Explained: Amazon Resource Name Guide](https://devopscube.com/aws-arn-guide/ "https://devopscube.com/aws-arn-guide/").
