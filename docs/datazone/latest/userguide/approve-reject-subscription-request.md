# Approve or reject a subscription

request in Amazon DataZone

Amazon DataZone allows you to find, access and consume the assets in the Amazon DataZone
catalog. When you find an asset in the catalog that you want to access, you must
_subscribe_ to the asset, which creates a subscription request.
An approver can then approve or reject your request.

You must be a member of the owning project (the project that published the asset) to
approve or reject a subscription request.

###### To approve or reject a subscription request

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. In the data portal, choose **Browse projects list** and
   select the project that contains the asset with the subscription request.
3. Navigate to the **Data** tab, then choose **Incoming
   requests** from the left navigation pane.
4. Locate the request and choose **View request**. You can
   filter by **Pending** to see only requests that are still
   open.
5. Review the subscription request and reason for access, and decide whether to
   approve or reject it.
6. To approve, select between the two options:
   - **Full access**: If you choose to approve the
     subscription with full access option, the subscriber will get access to
     all the rows and columns in your data asset.
   - **Approve with row and column filters**: To limit
     access to specific rows and columns of data, you can choose the option
     to approve with row and column filters. For more information, see [Fine-grained access control to data in
     Amazon DataZone](fine-grained-access-control.md "fine-grained-access-control.md").
     - Select **Choose filters**, and then from the
       drop down select one or more available filters you want to apply
       to the subscription.
     - To create a new filter you can choose Create new filter
       option, which opens a new page to create a new row or column
       filter. For more information, see [Create column filters in Amazon DataZone](create-column-filter.md "create-column-filter.md") and [Create row filters in Amazon DataZone](create-row-filter.md "create-row-filter.md").

7. (Optional) Enter a response that explains your reason for accepting or
   rejecting the request.
8. Choose either **Approve** or
   **Reject**.
   As the project owner, you can revoke the subscription at any time. For more
   information, see [Revoke an existing subscription in
   Amazon DataZone](revoke-subscription.md "revoke-subscription.md").

To view all subscription requests, see [Amazon DataZone events and
notifications](working-with-events-and-notifications.md "working-with-events-and-notifications.md").

###### Note

Amazon DataZone supports fine-grained access control for AWS Glue tables, Amazon
Redshift tables, and Amazon Redshift views.

## Automatic approval of

subscription requests

By default, subscription requests to a published asset require manual approval by
a data owner. However, Amazon DataZone supports two scenarios where subscription requests
can be automatically approved:

- Approval disabled during asset publishing - when publishing a data asset,
  you can choose to not require subscription approval. In this case, all
  incoming subscription requests to that asset are automatically approved. To
  learn how to disable approval for an asset, see [Publish assets to the Amazon DataZone catalog from
  the project inventory](publishing-data-asset.md "publishing-data-asset.md")
  .
- Requester is an owner or contributor in the project that published the
  asset - a subscription request is also automatically approved if the
  requester is already authorized to approve it manually. Specifically, if
  they are a member of both the project that published the asset and the
  project requesting access.

To qualify for auto-approval:

    + The requester must be listed as an owner or contributor in the
     project where the asset was originally published.
    + The requester must also be listed as an owner or contributor in
     the project making the subscription request.

This ensures that auto-approval only occurs when the requester has
visibility and permissions in both projects — the one sharing the asset and
the one requesting access. If the requester meets both conditions, the
system auto-approves the request.
