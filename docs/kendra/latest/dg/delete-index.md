

Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

# Deleting an index
<a name="delete-index"></a>

You can delete an index from Amazon Kendra when you are no longer using the index. For example, delete an index when: 
+ You are no longer using the index and want to reduce charges to your AWS account. An Amazon Kendra index accrues charges while it is running whether or not you make queries on the index.
+ You want to reconfigure the index for a different edition of Amazon Kendra. Delete the existing index and then create a new one with the different edition.
+ You have reached the maximum number of indexes in your account and don't want to exceed your quota. Delete an existing index and add a new one. For information about the maximum number of indexes that you can create, see [Quotas](https://docs.aws.amazon.com/kendra/latest/dg/quotas.html).

To delete an index, use the console, the AWS Command Line Interface, the CloudFormation script, or the `DeleteIndex` API. Deleting an index removes the index and all associated data sources and document data. Deleting an index doesn't remove the original documents from your storage.

Deleting an index is an asynchronous operation. When you start deleting an index, the index status changes to `DELETING`. It remains in the `DELETING` state until all of the information related to the index is removed. Once the index is deleted, it no longer appears in the results of a call to the [ListIndices](https://docs.aws.amazon.com/kendra/latest/APIReference/API_ListIndices.html) API. If you call the [DescribeIndex](https://docs.aws.amazon.com/kendra/latest/APIReference/API_DescribeIndex.html) API with the deleted index's identifier, you receive and `ResourceNotFound` exception.

**To delete an index (console)**

1. Sign in to the AWS Management Console and open the Amazon Kendra console at [https://console.aws.amazon.com/kendra/](https://console.aws.amazon.com/kendra/).

1. In the navigation pane, choose **Indexes**, and then choose the index to delete.

1. Choose **Delete** to delete the selected index.

**To delete an index (CLI)**
+ In the AWS CLI, use the following command. The command is formatted for Linux and macOS. If you are using Windows, replace the Unix line continuation character (\\) with a caret (^).

  ```
  aws kendra delete-index \
     --id {{index-id}}
  ```