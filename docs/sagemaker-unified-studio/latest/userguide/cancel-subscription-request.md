# Cancel a subscription request in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio allows you to find, access and consume the assets in the Amazon SageMaker Unified Studio catalog. When
you find an asset in the catalog that you want to access, you need to _subscribe_ to the asset, which creates a subscription request. An approver can
then approve or request your request. You might need to cancel a pending subscription request,
either because you submitted it by mistake, or because you no longer need read access to the
asset.

To cancel a subscription request, you must be either a project owner or
contributor.

###### To cancel a subscription request

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the project that contains the asset that has a subscription request. You
   can do this by choosing a project from the project selector dropdown at the top of the page.
3. In the left navigation pane, choose **Manage**, then under **Catalog management**, choose **Subscription
   requests**.
4. Choose the **Outgoing requests** tab.
5. Filter by **Requested** to see only requests that are still
   pending.
6. Locate the request and choose **View request**.
7. Review the subscription request and choose **Cancel request**.
   If you want to re-subscribe to the asset (or to a different asset), see [Request subscription to assets in Amazon SageMaker Unified Studio](subscribe-to-data-assets-managed.md "subscribe-to-data-assets-managed.md").
