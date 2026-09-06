

# Manage topic permissions through dashboards in Amazon Quick Sight
<a name="gen-bi-manage-topic-permissions"></a>

**Note**  
The topics referenced in this section refer to legacy Topics that are linked to dashboards for Q&A. For information about the new multi-dataset Topics experience, see [Working with Amazon Quick Sight Topics](topics.md).

 Quick enables Authors to manage permissions for dashboards and their linked topics from a single location. When sharing dashboards with Q&A enabled, Authors can control topic viewer access directly from a dashboard's sharing preferences, eliminating the need to manage permissions in multiple locations. 

**To enable Q&A on a dashboard with a linked topic:**

1. Open the [Quick console](https://quicksight.aws.amazon.com/).

1. Open the analysis of the dashboard with Q&A enabled and topic linked that you want to publish.

1. Choose **Publish**.

1. Check the **Allow data Q&A** check box.

1. Choose **MANAGE Q&A** and select **Use a linked topic for Build visual and Q&A**.

1. Select the desired linked topic from the dropdown menu.

1. Choose **APPLY CHANGES**, then choose **Publish dashboard**.

**To conveniently manage topic access from a dashboard:**

1. Open the [Quick console](https://quicksight.aws.amazon.com/).

1. Open the dashboard with a linked topic that you are a co-owner of.

1. Select the share icon and choose **Share dashboard**.

1. In the row of your selected user, flip on/off the **Share as "topic viewer"** toggle to grant/revoke viewer access to the linked topic.

1. In the row of your selected shared folder, flip on/off the **Add topic to folder** toggle to add/remove the linked topic to/from the shared folder.

**To share the dashboard and its linked topic to all users and groups:**

1. Open the [Quick console](https://quicksight.aws.amazon.com/).

1. Open the dashboard with a linked topic that you are a co-owner of.

1. Select the share icon and choose **Share dashboard**.

1. On the bottom-left of the panel, under **Auto-share linked topic for**, flip the **All dashboard users and groups** toggle on. This will grant viewer access to the linked topic when the dashboared is shared. Flip the toggle off to cancel this behavior.

After the dashboard with a linked topic has been shared, users will immediately be able to ask questions about their data. Navigate to **Ask a question about <topic name>** at the top of the dashboard to start asking questions.