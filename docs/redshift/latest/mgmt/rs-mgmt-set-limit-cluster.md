Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Setting a usage limit on a cluster

You can add up to four usage limits to control usage for each of the following:

- Concurrency scaling
- Automatic optimizations run using extra compute resources
- Redshift Spectrum usage
- Cross-Region data sharing

##

Setting a usage limit for a provisioned cluster

Following is the procedure for
setting a usage limit on a provisioned cluster:

###### To set a usage limit for a cluster

1.  Sign in to the AWS Management Console and open the Amazon Redshift console at
    [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2.  Navigate to the provisioned
    cluster that you want to set a limit for.
3.  From the cluster’s details page, select
    **Manage usage limit** from the **Actions** drop-down menu.
    You can also select the **Maintenance** tab for a cluster,
    then scroll down and select **Create usage limits**.
4.  Select **Add limit** for the usage limit that you want to set.
    You can add up to 4 limits for a given feature.
5.  Set a **Time period** for the usage limit,
    which is either **Daily**,
    **Weekly**, or **Monthly**.
6.  Set a **Usage limit**.
    - For concurrency scaling and automatic optimizations run using extra compute resources limits,
      the usage limit is the amount of time that Amazon Redshift spends
      using the feature in the given time period. In this case, the
      usage limit is set in hours and minutes.
    - For Redshift Spectrum, the usage limit is the amount of data scanned from Amazon S3.
      In this case, the usage limit is set in terabytes (TB).
    - For cross-Region data sharing, the usage limit is the
      amount of data transferred from the producer Region
      to consumer Regions that consumers can query. In this
      case, the usage limit is set in terabytes (TB).

7.  Set the **Action** for Amazon Redshift
    to take when your cluster reaches the limit. These are the following:

        * **Log to system table** ‐
         Adds a record to the system view [SYS\_QUERY\_HISTORY](../dg/SYS_QUERY_HISTORY.md "../dg/SYS_QUERY_HISTORY.md"). You can query the usage\_limit
         column in this view to determine if a query exceeded the limit.
        * **Alert** ‐
         Uses Amazon SNS to set up notification subscriptions and send
         notifications if a limit is breached. You can choose an
         existing Amazon SNS topic, create a new topic, or proceed without one.
        * **Disable feature** ‐
         Disables the feature. You can also choose to use Amazon SNS to send
         a notification. Users can continue to use the cluster for other tasks.

    The first two actions are informational, but the
    last turns off use of the feature.

8.  Choose **Save changes** at the
    bottom of the page to save the limit. If you set
    more than one limit at once, **Save changes** will
    save all of them at once.
