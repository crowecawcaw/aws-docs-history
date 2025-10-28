# Email archiving

Email archiving provides a way for you to archive the types of email you specify coming into your
ingress endpoint, or emails you send through a configuration set, as well as providing a way to
find your archived messages through a rich set of advanced search filters and the ability to
export the results.

Email archiving saves and protects your emails by storing data in persistent and secure long-term
storage, and gives you a way to quickly search and archive email. It provides full-time,
enterprise-level archiving without increasing the storage requirements of your mailbox
server.

An archive can contain a combination of both sent and received email:

- **Sent email archiving** – When you send
  (outbound) email through a configuration set with the archiving option enabled, all
  email sent using that configuration set will be archived to the email archive you
  designate.
- **Received email archiving** – When your
  ingress endpoint receives (inbound) email, it uses a traffic policy to determine which emails
  to block or allow. The email you allow in passes to a rule set that applies
  conditional rules to execute the actions you've defined for specific types of email.
  One of the rule actions you can define is _Archive
  action_—if you select this action, the email will be archived to
  the email archive you designate.
  You must first create an archive before it can be specified in a rule action or
  configuration set. The procedure in the next section will walk you through creating an
  archive in the SES console.

## Using email archiving in the Amazon SES console

The **Email archiving** page in the SES console consists of four
interactive tables, **Search archive**, **Search
history**, **Export history**, and **Manage
archives**, that you can use to search for email in your archives, export
the results, and manage your archives. In the following procedures, instructions are
provided for each table.

###### To use the **Email archiving** page to search, export, and manage your

archives

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the left navigation panel, choose **Email archiving** under
   **Mail Manager**.
3. The **Email archiving** page consists of four tables **Search
   archive**, **Search history**, **Export
   history**, and **Manage archives**. For
   instructions specific to each of these tables, select its corresponding tab
   below:

Search archive
**Search archive** is an interactive table that provides
a way for you to search and find your archived messages with a rich filter
and date set offering detailed search criteria to find anything from a
specific email to many emails matching a broader category. Messages matching
your search criteria can be downloaded individually or can be exported in
bulk to an S3 bucket.

###### To search, download, or export archived email

1. On the **Email archiving** page, choose
   the **Search archive** tab to display the
   **Search archive** table.
2. Click inside the **Archive**
   field and choose an archive from the list followed by
   **Search**, or refine your search using the
   following steps.
3. Select the **Date range** field
   to expand date range options for your search:
   - **Relative range** (default) –
     Select the radio button that corresponds with the number of
     days desired, or choose a **Custom range**
     by selecting a time unit and a date range up to 30 days.
   - **Absolute range** – Enter a
     **Start date** and an **End
     date**
     _(and time if desired)_ up to 30 days.

###### Note

    * Searching within an archive is limited to 30 days at a
     time. For example, if you want to search for messages
     from June 1st through July 31st, you would have to break
     it up into three searches as follows:




    	1. 30 days in June.
    	2. The first 30 days in July.
    	3. The 31st day of July.
    * For **Relative range** dates, the
     last day ends at midnight. For example, if you choose
     *Last 7 days*, the seventh day
     would be yesterday, ending at midnight.

[Show moreShow less](# "#") 4. (Optional) Select the **Filters** field to choose
from among the following filters: _From_,
_To_ , _CC_,
_Subject line_,

and _Has
attachments_—the following properties apply:

    * You can create up to 10 filters.
    * A filter can be edited by clicking on it, or removed by
     selecting the **X**.

5. Choose **Search** and the archived email matching
   your search criteria will be populated in the **Search
   results** table.
   - The **Message ID**

   column is hidden by default, but can be displayed by
   selecting the gear icon to customize how you view the
   table.
   - Every search you execute is automatically saved with a
     unique search id and will be listed in the **Search
     history** table.

6. To view the text of a message along with its envelope and header
   information, select the message’s radio button followed by
   **View details** to open the **Message
   details** sidebar.
7. To create a local file of the message,
   select the message’s radio button followed by **Download
   message**.
8. Your filtered search can be saved to an Amazon S3 bucket by selecting
   **Export to S3**.
   1. If you know the URI of the S3 bucket you want to
      use, enter it in the **S3 URI**
      field; otherwise, choose **Browse S3** and
      select an S3 bucket and folder to use on the
      S3
      page.
   2. (Optional) You can encrypt your exported messages either
      by entering your own AWS KMS key into the **KMS key
      ARN** field, or by selecting **Create
      new key**. Otherwise, encryption will be set to
      whatever method is being used on the destination S3
      bucket (even if none).
   3. Choose **Export** and all the messages
      found in your filtered search will be saved as individual
      files in the S3 folder you
      selected.

###### Note

While there's no limit on how many messages your archive can contain,
search results are limited to 1000 rows in the **Search
results** table.

Search history
A history of your searches is listed in this table so that you can restore
the result set or access complex filter sets created previously. You can
also create new searches based on the original search by editing the filters
and dates. Any new searches are automatically saved with a unique search ID
and will be listed in this table.

###### To view and work with your previous searches

1. On the **Email archiving** page, choose
   the **Search history** tab to display the
   **Search history** table which lists a history
   of all your archived email searches with the most recent on top.
   _This table loads data the first time you visit
   it—if you switch tabs and come back, use the refresh icon
   to retrieve the latest data._
2. Click inside the **Archive**
   field and choose an archive from the list—all the searches
   belonging to that archive will be populated in the table.

You can view and do more with individual searches in the steps
below. 3. Select the radio button of a previous search
followed by **View search results** to restore its
original search results—the **Search
archive** page will open displaying the filter set and
date range used for the original search along with all the messages
previously found based on that criteria. You can expand upon the
original search in the following ways:

    * Create a new search by modifying the date range and
     filters followed by **Search**.
    * Any new searches you perform are automatically saved with
     a unique search ID and will be listed in the
     **Search history** table.

Export history
A history of your exports is listed in this table enabling easy access to
the contents of the export folder in the S3 console.

###### To view your recent exports

1. On the **Email archiving** page, choose
   the **Export history** tab to display the
   **Export history** table which lists all of the
   archived email searches you exported to an S3 bucket within
   the last 30 days. _This table loads data the first time you
   visit it—if you switch tabs and come back, use the
   refresh icon to retrieve the latest data._
2. If the status of an export is
   _Queued_, _Preprocessing_
   or _Processing_, you can cancel it by choosing
   **Cancel**.
3. Select an **S3 URI** to open
   the export's bucket folder in the S3 console where you can
   see the files it contains.

Manage archives
This table lists your archives where you have options to create a new
archive, search for a particular archive and view its details, edit an
archive, or delete an archive.

###### To create and manage archives

1. On the **Email archiving** page, choose
   the **Manage archives** tab to display the
   **Archives** table which lists all of your
   email archives. _This table loads data the first time you
   visit it—if you switch tabs and come back, use the
   refresh icon to retrieve the latest data._
2. To search for a particular archive, begin typing
   in the **Archives** field.
3. To view details of an archive, select its name
   in the **Archive name** column.
4. To create an archive, select **Create
   archive**.
   1. Enter a unique name in the **Archive
      name** field.
   2. (Optional) Select a retention period in the
      **Retention period** field to override
      the default retention period of 180 days.
   3. (Optional) You can encrypt your archive either by entering
      your own AWS KMS key into the **KMS key ARN**
      field, or by selecting **Create new
      key**.Choose **Create archive**.

5. Now that you've created an archive, you can use it in a [rule set](eb-rules.md#eb-rules-create-console "eb-rules.md#eb-rules-create-console") to archive
   received (inbound) email, or designate it in a [configuration set](creating-configuration-sets.md#config-sets-create-console "creating-configuration-sets.md#config-sets-create-console") to
   archive sent (outbound) email.
6. To edit an archive, select its radio button followed by
   **Edit**.
   1. Edit or change the name in the **Archive
      name** field.
   2. Change the retention period in the **Retention
      period** field.Choose **Update archive**.

7. To delete an archive, select its radio button followed by
   **Delete**.
   1. Type `delete` in the
      **Confirm** field followed by
      **Delete**.

   The archive state will switch to _Pending
   deletion_ in the **Archives**
   table and will be automatically deleted after 30 days.
