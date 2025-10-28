# Using attribute-based access control with DynamoDB

[Attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") is an authorization strategy that defines
access permissions based on [tag conditions](Tagging.md "Tagging.md") in your
identity-based policies or other AWS policies, such as resource-based policies and
organization IAM policies. You can attach tags to DynamoDB tables, which are then evaluated
against the tag-based conditions. The indexes associated with a table inherit the tags you
add to the table. You can add up to 50 tags for each DynamoDB table. The maximum size supported
for all the tags in a table is 10 KB. For more information about tagging DynamoDB resources and
tagging restrictions, see [Tagging resources in
DynamoDB](Tagging.md "Tagging.md") and [Tagging restrictions in DynamoDB](Tagging.md#TaggingRestrictions "Tagging.md#TaggingRestrictions").

For more information about using tags to control access to AWS resources, see the following topics in the IAM User Guide:

- [What is ABAC for AWS](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md")
- [Controlling access to AWS resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md")
  Using ABAC, you can enforce different access levels for your teams and applications to perform actions on DynamoDB tables using fewer policies. You can specify a tag in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of an IAM policy to control access to your DynamoDB tables or indexes. These conditions determine the level of access an IAM principal, a user, or role, has to DynamoDB tables and indexes. When an IAM principal makes an access request to DynamoDB, the resource and identity’s tags are evaluated against the tag conditions in the IAM policy. Thereafter, the policy becomes effective only if tag conditions are met. This enables you to create an IAM policy that effectively says one of the following:

- _Allow the user to manage only those resources that have a tag with a key `X` and a value `Y`_.
- _Deny access to all users to resources tagged with a key `X`_.
  For example, you can create a policy that allows users to update a table only if it has the tag key-value pair: `"environment": "staging"`. You can use the [aws:ResourceTag](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag") condition key to allow or deny access to a table based on the tags that are attached to that table.

You can include attribute-based conditions while creating the policy or later using the AWS Management Console, AWS API, AWS Command Line Interface (AWS CLI), AWS SDK, or AWS CloudFormation.

The following example allows the [UpdateItem](../APIReference/API_UpdateItem.md "../APIReference/API_UpdateItem.md") action on a table named `MusicTable` if it includes a tag key with the name `environment` and value `production`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:UpdateItem"
 ],
 "Resource": "arn:aws:dynamodb:*:*:table/MusicTable",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/environment": "production"
 }
 }
 }
 ]
}`

```

###### Topics

- [Why should I use ABAC?](#why-use-abac "#why-use-abac")
- [Condition keys to implement ABAC with DynamoDB](#condition-keys-implement-abac "#condition-keys-implement-abac")
- [Considerations for using ABAC with DynamoDB](#abac-considerations "#abac-considerations")
- [Enabling ABAC in DynamoDB](abac-enable-ddb.md "abac-enable-ddb.md")
- [Using ABAC with DynamoDB tables and indexes](abac-implementation-ddb-tables.md "abac-implementation-ddb-tables.md")
- [Examples for using ABAC with DynamoDB tables and indexes](abac-example-use-cases.md "abac-example-use-cases.md")
- [Troubleshooting common ABAC errors for DynamoDB tables and indexes](abac-troubleshooting.md "abac-troubleshooting.md")

## Why should I use ABAC?

- **Simpler policy management:** You use fewer policies because you don't have to create different policies to define the level of access for each IAM principal.
- **Scalable access control:** Scaling access control is easier with ABAC because you don't have to update your policies when you create new DynamoDB resources. You can use tags to authorize access to IAM principals that contain tags matching the resource's tags. You can onboard new IAM principals or DynamoDB resources and apply appropriate tags to automatically grant the necessary permissions without having to make any policy changes.
- **Fine-grained permission management:** It's a best practice to [grant least privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") when you create policies. Using ABAC, you can create tags for the IAM principal, and use them to grant access to specific actions and resources that match the tags on the IAM principal.
- **Alignment with corporate directory:** You can map tags with existing employee attributes from your corporate directory to align your access control policies with your organizational structure.

## Condition keys to implement ABAC with DynamoDB

You can use the following condition keys in your AWS policies to control the level of access to your DynamoDB tables and indexes:

- [aws:ResourceTag/tag-key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag"): Controls access based on whether or not the tag key-value pair on a DynamoDB table or index matches the tag key and value in a policy. This condition key is relevant to all APIs that operate on an existing table or index.

The `dynamodb:ResourceTag` conditions are evaluated as if you didn't attach any tags to a resource.

- [aws:RequestTag/tag-key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag"): Allows comparing the tag key-value pair that was passed in the request with the tag pair that you specify in the policy. This condition key is relevant to APIs that contain tags as part of the request payload. These APIs include [CreateTable](../APIReference/API_CreateTable.md "../APIReference/API_CreateTable.md") and [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md").
- [aws:TagKeys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys"): Compares the tag keys in a request with the keys that you specify in the policy. This condition key is relevant to APIs that contain tags as part of the request payload. These APIs include `CreateTable`, `TagResource`, and `UntagResource`.

## Considerations for using ABAC with DynamoDB

When you use ABAC with DynamoDB tables or indexes, the following considerations apply:

- Tagging and ABAC aren't supported for DynamoDB Streams.
- Tagging and ABAC aren't supported for DynamoDB backups. To use ABAC with backups, we recommend that you use [AWS Backup](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md").
- Tags aren't preserved in restored tables. You need to add tags to restored tables before you can use tag-based conditions in your policies.
