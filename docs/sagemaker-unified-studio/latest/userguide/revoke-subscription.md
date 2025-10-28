# Revoke an existing subscription in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio allows you to find, access and consume the assets in the Amazon SageMaker Unified Studio catalog. When
you find an asset in the catalog that you want to access, you need to _subscribe_ to the asset, which creates a subscription request. An approver can
then approve or request your request. You might need to revoke a subscription after you have
approved it, either because the approval was a mistake, or because the subscriber no longer
needs access to the asset.

You must be a member of the owning project (the project that published the asset) to
revoke a subscription.

###### To revoke a subscription

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the project that contains the asset that has a subscription request. You
   can do this by using the center menu at the top of the page and choosing **Browse
   all projects**, then choosing the name of the project that you want to navigate
   to.
3. Under **Project catalog**, choose **Subscription
   requests**.
4. Choose the **Incoming requests** tab.
5. Locate the subscription you want to revoke and choose **View
   subscription**.
6. (Optional) Enable the checkbox to allow the subscriber to keep the asset in the
   project's subscription targets. A subscription target is a reference to a set of resources
   where subscribed data can be made available within an environment.

If you want to revoke access to the asset from the subscription target at a later
time, you must do so in AWS Lake Formation. 7. Choose **Revoke subscription**.
You can't re-approve a subscription after you revoke it. The subscriber must request a
subscription to the asset again in order for you to approve it.
