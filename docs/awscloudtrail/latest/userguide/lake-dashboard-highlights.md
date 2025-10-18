# Enable the Highlights dashboard with the
 CloudTrail console

Enable the Highlights dashboard to view an at-a-glance overview of the 
AWS activity collected by the event data stores in your account. The Highlights dashboard is managed by CloudTrail 
and includes widgets that are relevant to your account. The widgets shown on the Highlights 
dashboard are unique to each account. These widgets could surface detected abnormal activity or anomalies. 
For example, your Highlights dashboard could include the **Total cross-account access widget**, 
which shows if there is an increase in abnormal cross-account activity.

CloudTrail updates the Highlights dashboard every 6 hours. The dashboard shows the last 24 hours of data from the last update.

###### Note

You can only enable the Highlights dashboard for event data stores that exist in your account.

You cannot set a refresh schedule for the Highlights dashboard, or add or remove widgets.


## To enable the Highlights
 dashboard


Use the following procedure to enable the Highlights dashboard.


1. Sign in to the AWS Management Console and open the CloudTrail console at
 [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the left navigation pane, under **Lake**, choose
 **Dashboard**.
3. Choose the **Highlights** tab.
4. Because running queries incurs CloudTrail charges, CloudTrail asks you to review the
 cost information before enabling the **Highlights**
 dashboard. For information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").


Choose **Agree and enable Highlights** to enable the Highlights dashboard.
5. For **Permissions**, choose the event data stores that
 you want to apply permissions to. CloudTrail requires permissions to run queries
 on your event data stores and refresh the dashboard on your behalf. To
 provide permissions, CloudTrail attaches a default resource-based policy to each
 event data store selected in this step to allow CloudTrail to run queries on the
 event data store. CloudTrail attaches a resource-based policy to the dashboard to
 allow CloudTrail to refresh the dashboard every 6 hours.


You can modify the resource-based policy for an event data store from its
 details page. You can modify the resource-based policy for a dashboard by
 selecting **Edit policy** from the
 **Actions** menu for the dashboard.
6. Choose **Confirm**.

 When you enable the **Highlights** dashboard, termination
 protection is automatically enabled. Termination protection protects a dashboard
 from being accidentally deleted. You'll need to disable termination protection, if
 you want to disable the dashboard.
