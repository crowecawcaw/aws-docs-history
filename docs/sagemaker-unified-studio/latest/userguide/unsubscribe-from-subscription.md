# Unsubscribe from an asset in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio allows you to find, access and consume the assets in the Amazon SageMaker Unified Studio catalog. When
you find an asset in the catalog that you want to access, you need to _subscribe_ to the asset, which creates a subscription request. An approver can
then approve or request your request. You might need to unsubscribe from an asset, either
because you subscribed by mistake and were approved, or because you no longer need read access
to the asset.

You must be a member of a project in order to unsubscribe from one of its assets.

###### To unsubscribe from an asset

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the project that contains the asset that has a subscription request. You
   can do this by using the center menu at the top of the page and choosing **Browse
   all projects**, then choosing the name of the project that you want to navigate
   to.
3. Under **Project catalog**, choose **Subscription
   requests**.
4. Choose the **Outgoing requests** tab.
5. Filter by **Approved** to see only requests that have been
   approved.
6. Locate the request and choose **View subscription**.
7. Review the subscription and choose **Unsubscribe**.
   If you want to re-subscribe to the asset (or to a different asset), see [Request subscription to assets in
   Amazon SageMaker Unified Studio](subscribe-to-data-assets-managed.md "subscribe-to-data-assets-managed.md").
