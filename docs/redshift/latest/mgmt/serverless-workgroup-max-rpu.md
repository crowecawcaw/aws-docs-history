

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Setting usage limits, including setting RPU limits
<a name="serverless-workgroup-max-rpu"></a>

Under the **Limits** tab for a workgroup, you can add one or more usage limits to control the maximum RPUs you use in a given time period, or to set a data sharing usage limit.

1. Choose **Manage usage limits**. The limits section appears at the bottom of the **Compute usage by period** panel.

1. Set a usage limit in number of RPU hours.

1. Choose a **Frequency**, which is either **Daily**, **Weekly**, or **Monthly**. This sets the time period for the usage limit. Choosing **Daily** in this instance gives you more detailed control.

1. Set a usage limit, in number of hours.

1. Set the action. These are the following:
   + **Log to system table** - Adds a record to the system view [SYS\_QUERY\_HISTORY](https://docs.aws.amazon.com/redshift/latest/dg/SYS_QUERY_HISTORY.html). You can query the `usage_limit` column in this view to determine if a query exceeded the limit.
   + **Alert** - Uses Amazon SNS to set up notification subscriptions and send notifications if a limit is breached. You can choose an existing Amazon SNS topic or create a new one.
   + **Turn off user queries** - Disables queries to stop use of Amazon Redshift Serverless. It also sends a notification.

   The first two actions are informational, but the last turns off query processing.

1. Optionally, you can set a **Cross-Region data sharing usage limit**, which limits how much data transferred from producer Region to consumer Region consumers can query. To do this, choose **Add limit** and follow the steps.

1. Choose **Save changes** at the bottom of the page to save the limit.

1. Set up to 3 more limits as necessary.

For more conceptual information about RPUs and billing, see [Billing for Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-billing.html).