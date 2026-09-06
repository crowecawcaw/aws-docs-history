

# Viewing changes
<a name="view-changes"></a>

Private Marketplace administration actions are performed using Catalog API. Actions are started as change sets with one or more changes to create or update Private Marketplace entities. For details, see [Working with Private Marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/private-marketplace.html) in the *AWS Marketplace API Reference*.

All Private Marketplace change sets are listed on the **Change sets** page. This also includes change sets which are started by directly calling the APIs.

**To track the status of Private Marketplace administration actions**

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/).

1. In the navigation pane, choose **Change sets** under **Private Marketplace**.

1. To view a specific change set, filter using the change set ID. You can also filter using status **Succeeded**, **Failed**, **In progress**, or **Cancelled**.

1. Select a change type and choose **View details** to view all the changes.

1. Choose a change to view its details including the JSON response.

   1. When a change fails, **ErrorCode** and **ErrorMessage** fields in the JSON response provides details about the cause.

   1. When a change succeeds, refresh the console to view the updates from the change.

## AWS CloudTrail logging
<a name="cloudtrail-logging"></a>

Change sets are only retained for a period of 90 days. You can use AWS CloudTrail to capture all calls to the AWS Marketplace Catalog API as events. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon Simple Storage Service (Amazon S3) bucket. For more information, see [Logging AWS Marketplace Catalog API calls with CloudTrail](https://docs.aws.amazon.com/marketplace/latest/APIReference/logging-catalog-api-calls-with-cloudtrail.html) in the *AWS Marketplace Catalog API Reference*.