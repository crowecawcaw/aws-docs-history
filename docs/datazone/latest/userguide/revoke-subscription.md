# Revoke an existing subscription in

Amazon DataZone

Amazon DataZone allows you to find, access and consume the assets in the Amazon DataZone
catalog. When you find an asset in the catalog that you want to access, you need to
_subscribe_ to the asset, which creates a
subscription request. An approver can then approve or request your request. You might
need to revoke a subscription after you have approved it, either because the approval
was a mistake, or because the subscriber no longer needs access to the asset.

You must be a member of the owning project (the project that published the asset) to
revoke a subscription.

###### To revoke a subscription

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Choose **Select project** from the top navigation pane and
   select the project that contains the subscription you want to revoke.
3. Navigate to the **Data** tab, then choose **Incoming
   requests** from the left navigation pane.
4. Locate the subscription you want to revoke and choose **View
   subscription**.
5. (Optional) Enable the checkbox to allow the subscriber to keep the asset in
   the project's subscription targets. A subscription target is a reference to a
   set of resources where subscribed data can be made available within an
   environment.

If you want to revoke access to the asset from the subscription target at a
later time, you must do so in AWS Lake Formation. 6. Choose **Revoke subscription**.
You can't re-approve a subscription after you revoke it. The subscriber must subscribe
to the asset again in order for you to approve it.

###### Note

Revoking a subscription affects only the particular user’s access to the asset –
the subscriber whose subscription you’re revoking. The asset remains intact and the
user (subscriber) also remains intact. This user cannot access the asset until they
submit and get an approval of another subscription request.
