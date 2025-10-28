Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Setting usage limits, including

setting RPU limits

Under the **Limits** tab for a workgroup, you can add one or more
usage limits to control the maximum RPUs you use in a given time period, or to set a
data sharing usage limit.

1.  Choose **Manage usage limits**. The limits section
    appears at the bottom of the **Compute usage by
    period** panel.
2.  Set a usage limit in number of RPU hours.
3.  Choose a **Frequency**, which is either
    **Daily**, **Weekly**, or
    **Monthly**. This sets the time period for the usage
    limit. Choosing **Daily** in this instance gives you more
    detailed control.
4.  Set a usage limit, in number of hours.
5.  Set the action. These are the following:

        * **Log to system table** - Adds a record to the
         system view [SYS\_QUERY\_HISTORY](../dg/SYS_QUERY_HISTORY.md "../dg/SYS_QUERY_HISTORY.md"). You can query the
         `usage_limit` column in this view to determine if a
         query exceeded the limit.
        * **Alert** - Uses Amazon SNS to set up notification
         subscriptions and send notifications if a limit is breached. You can
         choose an existing Amazon SNS topic or create a new one.
        * **Turn off user queries** - Disables queries to
         stop use of Amazon Redshift Serverless. It also sends a notification.

    The first two actions are informational, but the last turns off query
    processing.

6.  Optionally, you can set a **Cross-Region data sharing usage
    limit**, which limits how much data transferred from producer
    Region to consumer Region consumers can query. To do this, choose
    **Add limit** and follow the steps.
7.  Choose **Save changes** at the bottom of the page to
    save the limit.
8.  Set up to 3 more limits as necessary.
    For more conceptual information about RPUs and billing, see [Billing for
    Amazon Redshift Serverless](serverless-billing.md "serverless-billing.md").
