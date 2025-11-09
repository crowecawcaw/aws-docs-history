# Editing collaborations

As a collaboration creator, you can edit the different parts of a collaboration.

For information about how to edit a collaboration using the AWS SDKs, see the _[AWS
Clean Rooms API Reference](../apireference/Welcome.md "../apireference/Welcome.md")_.

###### Topics

- [Edit collaboration name and description](#edit-name-descrip "#edit-name-descrip")
- [Update collaboration analytics
  engine](#change-collab-analytics-engine "#change-collab-analytics-engine")
- [Turn off log storage](#turn-off-log-storage "#turn-off-log-storage")
- [Edit collaboration logs settings](#edit-logs-settings "#edit-logs-settings")
- [Edit collaboration tags](#edit-collab-tags "#edit-collab-tags")
- [Edit membership tags](#edit-membership-tags "#edit-membership-tags")
- [Edit associated table tags](#edit-associated-table-tags "#edit-associated-table-tags")
- [Edit analysis template tags](#edit-analysis-template-tags "#edit-analysis-template-tags")
- [Edit differential privacy policy tags](#edit-dp-policy-tags "#edit-dp-policy-tags")

## Edit collaboration name and description

After you create the collaboration, you can only edit the collaboration name and
description.

###### To edit the collaboration name and description

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose
   **Collaborations**.
3. Choose the collaboration that you created.
4. On the collaboration detail page, choose **Actions**, and
   then choose **Edit collaboration**.
5. On the **Edit collaboration** page, for
   **Details**, edit the **Name** and
   **Description** of the collaboration.
6. Choose **Save changes**.

## Update collaboration analytics

engine

After you create the collaboration, you can change the analytics engine from AWS Clean Rooms SQL
to Spark.

###### Note

Changing the analytics engine from AWS Clean Rooms SQL to Spark might break existing
workflows.

###### To update the collaboration analytics engine

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your AWS account (if you
   haven't yet done so).
2. In the left navigation pane, choose
   **Collaborations**.
3. Choose the collaboration that you created.
4. On the collaboration detail page, choose **Actions**, and
   then choose **Edit collaboration**.
5. On the **Edit collaboration** page, for **Analytics
   engine**,
   - If **AWS Clean Rooms SQL** is selected, choose
     **Spark**.
   - If **Spark** is selected, choose **Submit a
     support ticket** to submit a support ticket to change the
     analytics engine to AWS Clean Rooms SQL.

   ###### Note

   AWS Clean Rooms will end support for the legacy Clean Rooms SQL analytics
   engine on December 17th, 2025. Before July 16, 2025, you must
   request a limit increase via AWS Customer Support to create any
   new Clean Rooms SQL engine-based collaborations. After July 16,
   2025, the creation of new Clean Rooms SQL engine-based
   collaborations will no longer be available.

6. Choose **Save changes**.

## Turn off log storage

If you have enabled **Analysis logging**, you can edit whether the
analysis logs are stored in your Amazon CloudWatch Logs account.

###### To turn off log storage

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your AWS account (if you
   haven't yet done so).
2. In the left navigation pane, choose
   **Collaborations**.
3. Choose the collaboration that has analysis logging turned on.
4. On the collaboration detail page, choose **Actions**, and
   then choose **Turn off log storage**.

###### Note

A warning appears, indicating the following:

    * New queries will no longer be logged to your CloudWatch
     account.
    * Existing logs will be preserved according to your current
     retention settings.
    * If you reactivate logging in the future, it will only apply to
     queries made after reactivation.
    * This change affects only your logs - other team members' logging
     settings remain unchanged.

5. Choose **Turn off**.

## Edit collaboration logs settings

If you have enabled **Query logging**, you can edit whether the query
logs are stored in your Amazon CloudWatch Logs account.

###### To edit collaboration logs settings

1.  Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your AWS account (if you
    haven't yet done so).
2.  In the left navigation pane, choose
    **Collaborations**.
3.  Choose the collaboration that you created.
4.  On the collaboration detail page, do one of the following:
    - Choose **Actions**, and then choose **Edit
      logs settings**.
    - On the **Logs** tab, choose **Edit logs
      settings**.

5.  On the **Edit logs settings modal**, for **Log
    storage in Amazon CloudWatch Logs**:
    - If you don't want logs relevant to you to be stored in your Amazon CloudWatch Logs
      account, choose **Turn oﬀ**.
    - If you do want logs relevant to you to be stored in your Amazon CloudWatch Logs
      account, choose **Turn on**.

    You can only receive logs for queries that you initiated or that
    contain you data.

    The member who can receive results also receives logs for all queries
    run in a collaboration, even if their data isn't accessed in a
    query.

        1. Under **Supported log types**, choose from
         the log types the collaboration creator has chosen to
         support:




        	+ If you want to receive logs generated from SQL
        	 queries, choose the **Logs from
        	 queries** checkbox.
        	+ If you want to receive logs generated from jobs using
        	 PySpark, choose the **Logs from jobs**
        	 checkbox.

6.  Choose **Save changes**.

###### Note

After you turn on logging, it can take a few minutes for log storage to be set up
and start receiving logs in Amazon CloudWatch Logs. During this brief period, the
member who can query might run queries that don’t actually send logs.

## Edit collaboration tags

As a collaboration creator, after you have created a collaboration, you can manage the
tags on the collaboration resource.

###### To edit the collaboration tags

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your AWS account (if you
   haven't yet done so).
2. In the left navigation pane, choose
   **Collaborations**.
3. Choose the collaboration that you created.
4. Choose one of the following:

| If you are...                                                      | Then ...                                         |
| ------------------------------------------------------------------ | ------------------------------------------------ |
| The collaboration creator and a member of the<br>collaboration     | Choose the \*_Details_<br>• tab.                 |
| The collaboration creator but not a member of the<br>collaboration | Scroll down the page to the **Tags**<br>section. |

5. For **Collaboration details**, choose **Manage
   tags**.
6. On the **Manage tags** page, you can do the following:
   - To remove a tag, choose **Remove**.
   - To add a tag, choose **Add new tag**.
   - To save your changes, choose **Save changes**

## Edit membership tags

As a collaboration creator, after you have created a collaboration, you can manage the
tags on the membership resource.

###### To edit the membership tags

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your AWS account (if you
   haven't yet done so).
2. In the left navigation pane, choose
   **Collaborations**.
3. Choose the collaboration that you created.
4. Choose the **Details** tab.
5. For **Membership details**, choose **Manage
   tags**.
6. On the **Manage membership tags** page, you can do the
   following:
   - To remove a tag, choose **Remove**.
   - To add a tag, choose **Add new tag**.
   - To save your changes, choose **Save changes**.

## Edit associated table tags

As a collaboration creator, after you associate tables to a collaboration, you can
manage the tags on the associated table resource.

###### To edit the associated table tags

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your AWS account (if you
   haven't yet done so).
2. In the left navigation pane, choose
   **Collaborations**.
3. Choose the collaboration that you created.
4. Choose the **Tables** tab.
5. For **Tables associated by you**, choose a table.
6. On the configured table detail page, for **Tags**, choose
   **Manage tags**.

On the **Manage tags** page, you can do the following:

    * To remove a tag, choose **Remove**.
    * To add a tag, choose **Add new tag**.
    * To save your changes, choose **Save changes**.

## Edit analysis template tags

As a collaboration creator, after you have created a collaboration, you can manage the
tags on the analysis template resource.

###### To edit the membership tags

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your AWS account (if you
   haven't yet done so).
2. In the left navigation pane, choose
   **Collaborations**.
3. Choose the collaboration that you created.
4. Choose the **Templates** tab.
5. On the **Analysis templates created by you** section, choose
   the analysis template.
6. On the analysis template table detail page, scroll down to the
   **Tags** section.
7. Choose **Manage tags**.
8. On the **Manage tags** page, you can do the following:
   - To remove a tag, choose **Remove**.
   - To add a tag, choose **Add new tag**.
   - To save your changes, choose **Save changes**.

## Edit differential privacy policy tags

As a collaboration creator, after you have created a collaboration, you can manage the
tags on the analysis template resource.

###### To edit the membership tags

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your AWS account (if you
   haven't yet done so).
2. In the left navigation pane, choose
   **Collaborations**.
3. Choose the collaboration that contains the differential privacy policy you
   want to edit.
4. Choose the **Tables** tab.
5. On the **Tables** tab, choose the **Manage
   tags**.
6. On the **Manage tags** page, you can do the following:
   - To remove a tag, choose **Remove**.
   - To add a tag, choose **Add new tag**.
   - To save your changes, choose **Save changes**.
