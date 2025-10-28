# Viewing changes

Private Marketplace administration actions are performed using Catalog API. Actions are started as change sets with one or more changes to create or update Private Marketplace entities. For details, see [Working with Private Marketplace](../../../marketplace-catalog/latest/api-reference/private-marketplace.md "../../../marketplace-catalog/latest/api-reference/private-marketplace.md") in the _AWS Marketplace API Reference_.

All Private Marketplace change sets are listed on the **Change sets** page. This also includes change sets which are started by directly calling the APIs.

###### To track the status of Private Marketplace administration actions

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. In the navigation pane, choose **Change sets** under **Private Marketplace**.
3. To view a specific change set, filter using the change set ID. You can also filter using status **Succeeded**, **Failed**, **In progress**, or **Cancelled**.
4. Select a change type and choose **View details** to view all the changes.
5. Choose a change to view its details including the JSON response.
   1. When a change fails, **ErrorCode** and **ErrorMessage** fields in the JSON response provides details about the cause.
   2. When a change succeeds, refresh the console to view the updates from the change.

## AWS CloudTrail logging

Change sets are only retained for a period of 90 days. You can use AWS CloudTrail to capture all calls to the AWS Marketplace Catalog API as events. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon Simple Storage Service (Amazon S3) bucket. For more information, see [Logging AWS Marketplace Catalog API calls with CloudTrail](../APIReference/logging-catalog-api-calls-with-cloudtrail.md "../APIReference/logging-catalog-api-calls-with-cloudtrail.md") in the _AWS Marketplace Catalog API Reference_.
