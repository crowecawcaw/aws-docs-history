

# Actions, resources, and condition keys for AWS reInvent event pass amount charge to customer AWS account
<a name="list_eventsbilltoaws"></a>

AWS reInvent event pass amount charge to customer AWS account (service prefix: `eventsbilltoaws`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/eventsbilltoaws/latest/reference/what-is-eventsbilltoaws.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/eventsbilltoaws/latest/reference/what-is-eventsbilltoaws.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/eventsbilltoaws/latest/reference/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/eventsbilltoaws/eventsbilltoaws.json) for this service.

**Topics**
+ [Actions defined by AWS reInvent event pass amount charge to customer AWS account](#list_eventsbilltoaws-actions-as-permissions)
+ [Resource types defined by AWS reInvent event pass amount charge to customer AWS account](#list_eventsbilltoaws-resources-for-iam-policies)
+ [Condition keys for AWS reInvent event pass amount charge to customer AWS account](#list_eventsbilltoaws-policy-keys)

## Actions defined by AWS reInvent event pass amount charge to customer AWS account
<a name="list_eventsbilltoaws-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [approve](https://docs.aws.amazon.com/eventsbilltoaws/latest/reference/)  | Grants permission to approve or deny the reinvent pass charge to AWS account |  | [aws:RequestTag/${TagKey}](#list_eventsbilltoaws-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eventsbilltoaws-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventsbilltoaws-aws_TagKeys) | Write | 
|   [info](https://docs.aws.amazon.com/eventsbilltoaws/latest/reference/)  | Grants permission to get the AWS reinvent pass purchase details |  | [aws:RequestTag/${TagKey}](#list_eventsbilltoaws-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_eventsbilltoaws-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_eventsbilltoaws-aws_TagKeys) | Read | 

## Resource types defined by AWS reInvent event pass amount charge to customer AWS account
<a name="list_eventsbilltoaws-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [approve](https://docs.aws.amazon.com/eventsbilltoaws/latest/reference/security-iam.html)  | arn:${Partition}:eventsbilltoaws:${Region}:${Account}:${RelativeId} | [aws:ResourceTag/${TagKey}](#list_eventsbilltoaws-aws_ResourceTag___TagKey_) | 
|  [info](https://docs.aws.amazon.com/eventsbilltoaws/latest/reference/security-iam.html)  | arn:${Partition}:eventsbilltoaws:${Region}:${Account}:${RelativeId} | [aws:ResourceTag/${TagKey}](#list_eventsbilltoaws-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS reInvent event pass amount charge to customer AWS account
<a name="list_eventsbilltoaws-policy-keys"></a>

AWS reInvent event pass amount charge to customer AWS account defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/condition-keys-tagkeys)  | Filters access by a key that is present in the request | ArrayOfString | 