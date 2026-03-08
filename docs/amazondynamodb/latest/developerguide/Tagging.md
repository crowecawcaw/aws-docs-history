# Adding tags and labels to resources in DynamoDB

You can label Amazon DynamoDB resources using _tags_. Tags let you
categorize your resources in different ways, for example, by purpose, owner, environment, or
other criteria. Tags can help you do the following:

- Quickly identify a resource based on the tags that you assigned to it.
- See AWS bills broken down by tags.

###### Note

Any local secondary indexes (LSI) and global secondary indexes (GSI) related
to tagged tables are labeled with the same tags automatically. Currently, DynamoDB
Streams usage cannot be tagged.
Tagging is supported by AWS services like Amazon EC2, Amazon S3, DynamoDB, and more. Efficient
tagging can provide cost insights by enabling you to create reports across services that
carry a specific tag.

To get started with tagging, do the following:

1. Understand [Tagging restrictions in DynamoDB](#TaggingRestrictions "#TaggingRestrictions").
2. Create tags by using [Tagging resources in DynamoDB](Tagging.md "Tagging.md").
3. Use [Using DynamoDB tags to create cost allocation reports](#CostAllocationReports "#CostAllocationReports")
   to track your AWS costs per active tag.
   Finally, it is good practice to follow optimal tagging strategies. For information, see
   [AWS tagging
   strategies](https://d0.awsstatic.com/aws-answers/AWS_Tagging_Strategies.pdf "https://d0.awsstatic.com/aws-answers/AWS_Tagging_Strategies.pdf").

## Tagging restrictions in DynamoDB

Each tag consists of a key and a value, both of which you define. The following restrictions apply:

- Each DynamoDB table can have only one tag with the same key. If you try to add an existing
  tag (same key), the existing tag value is updated to the new value.
- Tag keys and values are case sensitive.
- The maximum key length is 128 Unicode characters.
- The maximum value length is 256 Unicode characters.
- The allowed characters are letters, white space, and numbers, plus the following special
  characters: `+ - = . _ : /`
- The maximum number of tags per resource is 50.
- The maximum size supported for all the tags in a table is 10 KB.
- AWS-assigned tag names and values are automatically assigned the `aws:`
  prefix, which you can't assign. AWS-assigned tag names don't count toward the tag
  limit of 50 or the 10 KB maximum size limit. User-assigned tag names have the prefix `user:` in the cost
  allocation report.
- You can't backdate the application of a tag.

## Using DynamoDB tags to create cost allocation reports

AWS uses tags to organize resource costs on your cost allocation report. AWS provides two
types of cost allocation tags:

- An AWS-generated tag. AWS defines, creates, and applies this tag for you.
- User-defined tags. You define, create, and apply these tags.
  You must activate both types of tags separately before they can appear in Cost
  Explorer or on a cost allocation report.

To activate AWS-generated tags:

1. Sign in to the AWS Management Console and open the Billing and Cost Management console at
   [https://console.aws.amazon.com/billing/home#/.](https://console.aws.amazon.com/billing/home#/. "https://console.aws.amazon.com/billing/home#/.")
2. In the navigation pane, choose **Cost Allocation Tags**.
3. Under **AWS-Generated Cost Allocation Tags**, choose
   **Activate**.

To activate user-defined tags:

1. Sign in to the AWS Management Console and open the Billing and Cost Management console at
   [https://console.aws.amazon.com/billing/home#/.](https://console.aws.amazon.com/billing/home#/. "https://console.aws.amazon.com/billing/home#/.")
2. In the navigation pane, choose **Cost Allocation Tags**.
3. Under **User-Defined Cost Allocation Tags**, choose
   **Activate**.

After you create and activate tags, AWS generates a cost allocation report
with your usage and costs grouped by your active tags. The cost allocation report includes
all of your AWS costs for each billing period. The report includes both tagged and untagged resources,
so that you can clearly organize the charges for resources.

###### Note

Currently, any data transferred out from DynamoDB won't be broken down by tags on cost
allocation reports.

For more information, see
[Using cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md").
