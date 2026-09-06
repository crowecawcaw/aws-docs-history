

# Tagging DynamoDB Streams
<a name="Tagging.Streams"></a>

**Tagging on creation not supported**  
DynamoDB Streams does not currently support tagging on creation. You can only add tags to existing streams.

You can use the Amazon DynamoDB console, AWS Command Line Interface (AWS CLI), or AWS SDK to manage tags on existing DynamoDB Streams. You can then activate these user-defined tags so that they appear on the AWS Billing and Cost Management console for cost allocation tracking. For more information, see [Using DynamoDB tags to create cost allocation reports](Tagging.md#CostAllocationReports).

**Topics**
+ [Tagging existing streams (AWS Management Console)](#Tagging.Streams.using-console)
+ [Tagging existing streams (AWS CLI)](#Tagging.Streams.using-cli)

## Tagging existing streams (AWS Management Console)
<a name="Tagging.Streams.using-console"></a>

You can use the DynamoDB console to add, edit, or delete tags for existing streams.

**To tag an existing stream (console)**

Open the DynamoDB console at [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/).

1. In the navigation pane, choose **Tables**.

1. Choose the table whose stream you want to tag.

1. Choose the **Exports and streams** tab.

1. In the **DynamoDB stream details** section, choose **Manage tags**.

1. Add the tags you want and choose **Save**.

   For information about tag structure, see [Tagging restrictions in DynamoDB](Tagging.md#TaggingRestrictions).

The following screenshot shows the **Manage tags** page for a DynamoDB stream, where you add key-value tag pairs and then choose **Save changes**.

![The Manage tags page in the DynamoDB console for a stream on the Movies table, showing empty Key and Value fields, an Add new tag button, and a Save changes button.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/manage-stream-tags-console.png)


## Tagging existing streams (AWS CLI)
<a name="Tagging.Streams.using-cli"></a>

The following examples show how to use the AWS CLI to tag existing streams and list tags for a stream.

**To tag an existing stream (AWS CLI)**
+ The following example adds the `Owner` tag with a value of `blueTeam` to an existing stream on the `Movies` table:

  ```
  aws dynamodb tag-resource \
      --resource-arn arn:aws:dynamodb:us-east-1:111122223333:table/Movies/stream/2024-01-01T00:00:00.000 \
      --tags Key=Owner,Value=blueTeam
  ```

**To list all tags for a stream (AWS CLI)**
+ The following example lists all the tags that are associated with a stream on the `Movies` table:

  ```
  aws dynamodb list-tags-of-resource \
      --resource-arn arn:aws:dynamodb:us-east-1:111122223333:table/Movies/stream/2024-01-01T00:00:00.000
  ```