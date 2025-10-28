# Adding or removing a notification hub in AWS User Notifications

You can add or remove a notification hub using the AWS Management Console. When you add a new
notification hub, User Notifications replicates new notifications into that Region. User Notifications doesn’t backfill
earlier notifications. When you remove a notification hub, User Notifications stops replicating new
notifications into that Region. User Notifications doesn’t remove previous notifications from that Region.
However, notifications expire 90 days after they are generated.

###### To add or remove notification hubs

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
   1. In the navigation pane, choose **Notification hubs**.

2. Choose **Edit**.
3. Either add Regions by selecting them or remove Regions by choosing the
   **×** next to a Region.
4. Choose **Update**.
