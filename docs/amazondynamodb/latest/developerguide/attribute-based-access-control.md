

# Using attribute-based access control with DynamoDB
<a name="attribute-based-access-control"></a>

[Attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) is an authorization strategy that defines access permissions based on [tag conditions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tagging.html) in your identity-based policies or other AWS policies, such as resource-based policies and organization IAM policies. You can attach tags to DynamoDB tables, which are then evaluated against the tag-based conditions. The indexes associated with a table inherit the tags you add to the table. You can add up to 50 tags for each DynamoDB table. The maximum size supported for all the tags in a table is 10 KB. For more information about tagging DynamoDB resources and tagging restrictions, see [ Tagging resources in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tagging.Operations.html) and [Tagging restrictions in DynamoDB](Tagging.md#TaggingRestrictions).

For more information about using tags to control access to AWS resources, see the following topics in the IAM User Guide:
+ [What is ABAC for AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html)
+ [Controlling access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html)

Using ABAC, you can enforce different access levels for your teams and applications to perform actions on DynamoDB tables using fewer policies. You can specify a tag in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of an IAM policy to control access to your DynamoDB tables or indexes. These conditions determine the level of access an IAM principal, a user, or role, has to DynamoDB tables and indexes. When an IAM principal makes an access request to DynamoDB, the resource and identity’s tags are evaluated against the tag conditions in the IAM policy. Thereafter, the policy becomes effective only if tag conditions are met. This enables you to create an IAM policy that effectively says one of the following:
+ *Allow the user to manage only those resources that have a tag with a key `X` and a value `Y`*.
+ *Deny access to all users to resources tagged with a key `X`*.

For example, you can create a policy that allows users to update a table only if it has the tag key-value pair: `"environment": "staging"`. You can use the [aws:ResourceTag](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) condition key to allow or deny access to a table based on the tags that are attached to that table.

You can include attribute-based conditions while creating the policy or later using the AWS Management Console, AWS API, AWS Command Line Interface (AWS CLI), AWS SDK, or AWS CloudFormation.

The following example allows the [UpdateItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateItem.html) action on a table named `MusicTable` if it includes a tag key with the name `environment` and value `production`.

------
#### [ JSON ]

****  

```
{
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
}
```

------

**Topics**
+ [Why should I use ABAC?](#why-use-abac)
+ [Condition keys to implement ABAC with DynamoDB](#condition-keys-implement-abac)
+ [Considerations for using ABAC with DynamoDB](#abac-considerations)
+ [Using attribute-based access control with DynamoDB tables and indexes](abac-tables.md)
+ [Using attribute-based access control with DynamoDB Streams](abac-streams.md)

## Why should I use ABAC?
<a name="why-use-abac"></a>
+ **Simpler policy management:** You use fewer policies because you don't have to create different policies to define the level of access for each IAM principal.
+ **Scalable access control:** Scaling access control is easier with ABAC because you don't have to update your policies when you create new DynamoDB resources. You can use tags to authorize access to IAM principals that contain tags matching the resource's tags. You can onboard new IAM principals or DynamoDB resources and apply appropriate tags to automatically grant the necessary permissions without having to make any policy changes.
+ **Fine-grained permission management:** It's a best practice to [grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) when you create policies. Using ABAC, you can create tags for the IAM principal, and use them to grant access to specific actions and resources that match the tags on the IAM principal. 
+ **Alignment with corporate directory:** You can map tags with existing employee attributes from your corporate directory to align your access control policies with your organizational structure.

## Condition keys to implement ABAC with DynamoDB
<a name="condition-keys-implement-abac"></a>

You can use the following condition keys in your AWS policies to control the level of access to your DynamoDB tables and indexes:
+ [aws:ResourceTag/tag-key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag): Controls access based on whether or not the tag key-value pair on a DynamoDB table or index matches the tag key and value in a policy. This condition key is relevant to all APIs that operate on an existing table or index.

  The `dynamodb:ResourceTag` conditions are evaluated as if you didn't attach any tags to a resource.
+ [aws:RequestTag/tag-key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag): Allows comparing the tag key-value pair that was passed in the request with the tag pair that you specify in the policy. This condition key is relevant to APIs that contain tags as part of the request payload. These APIs include [CreateTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html) and [TagResource](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TagResource.html).
+ [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys): Compares the tag keys in a request with the keys that you specify in the policy. This condition key is relevant to APIs that contain tags as part of the request payload. These APIs include `CreateTable`, `TagResource`, and `UntagResource`.

## Considerations for using ABAC with DynamoDB
<a name="abac-considerations"></a>

When you use ABAC with DynamoDB tables or indexes, the following considerations apply:
+ For information about using ABAC with DynamoDB Streams, see [Using attribute-based access control with DynamoDB Streams](abac-streams.md).
+ Tagging and ABAC aren't supported for DynamoDB backups. To use ABAC with backups, we recommend that you use [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html).
+ Tags aren't preserved in restored tables. You need to add tags to restored tables before you can use tag-based conditions in your policies.